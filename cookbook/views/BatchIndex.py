import io

from django.db.models import Sum
from django.http import HttpResponse, HttpResponseRedirect, FileResponse
from django.shortcuts import render
from django.utils.timezone import now
from django.views import generic
from reportlab.lib.colors import black, red
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas

from cookbook.models import Batch, Gene, BatchItem, Ingredient, RecipeItem


class BatchIndex(generic.ListView):
    model = Batch

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['gene_list'] = Gene.objects.exclude(used_in_batch=True)
        return context


def batch_add(request, gene_id):
    new_batch = Batch()
    new_batch.gene = Gene.objects.get(id=gene_id)
    new_batch.gene.used_in_batch = True
    new_batch.gene.save()
    new_batch.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def batch_set(request, batch_id, value):
    batch = Batch.objects.get(id=batch_id)
    batch.quantity = value
    batch.save()
    return HttpResponse(value)


def batch_del(request, batch_id):
    batch = Batch.objects.get(id=batch_id)
    batch.gene.used_in_batch = False
    batch.gene.save()
    BatchItem.manager.filter(batch_id=batch_id).delete()
    Batch.objects.get(id=batch_id).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def batch_set_item(request, batch_item_id, value):
    item = BatchItem.manager.get(id=batch_item_id)
    print(item)
    item.computed_vol = value
    item.is_manual = True
    item.save()
    return HttpResponse(value)


def batch_process(request):
    # water vol = 22 - [all vols]
    context = dict()
    batch_items = dict()
    checksums = dict()
    batches = Batch.objects.all()
    for batch in batches:
        BatchItem.manager.filter(batch_id=batch.id, is_manual=0).delete()
        for recipe_item in RecipeItem.objects.filter(recipe_id=batch.gene.recipe.id).exclude(ingredient__name='H20'):
            print(f'Item {recipe_item.ingredient.name} started @: ' + str(now()))
            if len(BatchItem.manager.filter(batch_id=batch.id, is_manual=True, ingredient=recipe_item.ingredient)) == 0:
                new_batch_item = BatchItem()
                new_batch_item.batch = batch
                new_batch_item.ingredient = recipe_item.ingredient
                new_batch_item.computed_vol = recipe_item.volume * (batch.quantity + 4)
                new_batch_item.is_manual = False
                new_batch_item.save()
        h2o = BatchItem()
        h2o.batch = batch
        h2o.ingredient = Ingredient.objects.get(id=1)
        vol_sum = BatchItem.manager.filter(batch_id=batch.id).aggregate(Sum('computed_vol'))
        h2o.computed_vol = (22 * (batch.quantity + 4)) - vol_sum['computed_vol__sum']
        h2o.is_manual = False
        h2o.save()

        checksums[batch.gene.name] = vol_sum['computed_vol__sum']
        batch_items[batch.gene.name] = BatchItem.manager.filter(batch_id=batch.id)
    context['batch_items'] = batch_items
    context['checksums'] = checksums

    return render(request, 'cookbook/batch_result.html', context)


def batch_report(request):
    DEBUG = False
    width, height = A4[0], A4[1]
    top_m, right_m, bottom_m, left_m = 10, 10, 10, 10
    x, y, tab1, col = 10, 287, 50, width / 3 / mm - 5
    header_h, footer_h = 20, 20
    border_p = 5

    top_m *= mm
    right_m *= mm
    bottom_m *= mm
    left_m *= mm
    x *= mm
    y *= mm
    tab1 *= mm
    col *= mm
    header_h *= mm
    footer_h *= mm
    border_p *= mm

    header_o = (left_m, height - top_m - header_h)
    header_d = (width - left_m - right_m, header_h)

    footer_o = (left_m, bottom_m)
    footer_d = (width - left_m - right_m, footer_h)

    buffer = io.BytesIO()
    p = canvas.Canvas(buffer, pagesize=A4)

    p.setFont('Helvetica', 12)

    batches = Batch.objects.all()

    if DEBUG:
        print(p.getAvailableFonts())
        print(width / mm, height / mm, header_o[0] / mm, header_o[1] / mm)
        p.rect(header_o[0], header_o[1], header_d[0], header_d[1])
        p.rect(footer_o[0], footer_o[1], footer_d[0], footer_d[1])
    else:

        for batch in batches:
            if y <= 60 * mm:
                x, y = x + col, 287 * mm
            if x >= col * 3:
                x = 0 + left_m
                y = 287 * mm
                p.showPage()

            border_x = x
            border_y = y
            p.setFont('Helvetica', 12)
            p.drawString(x, y, str(batch))
            x += 7 * mm
            y -= 5 * mm
            for batch_item in BatchItem.manager.filter(batch_id=batch.id):
                if batch_item.is_manual:
                    p.setFillColor(red, 1)
                else:
                    p.setFillColor(black, 1)
                p.setFont('Helvetica', 10)
                p.drawString(x, y, batch_item.ingredient.name)
                p.drawRightString(x + tab1, y, str(batch_item.computed_vol) + ' µl')
                y -= 5 * mm
            y -= 1 * mm
            p.drawRightString(x + tab1, y, batch.gene.program.name)
            y -= 5 * mm
            p.roundRect(border_x - 3 * mm, y + 2 * mm, col, border_y - y + 3 * mm, 10)
            x -= 7 * mm
            y -= 3 * mm

    # to = p.beginText(x, y)
    # resp = batch_process(request)
    # print(type(resp.tell()))
    # for i in resp.tell():
    #     print(str(i))
    #     to.textLine(str(i))
    # p.drawText(to)
    # p.showPage()
    p.save()
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=False, filename='batch_report_' + str(now()) + '.pdf')

