import io

from django.core.files import File
from django.http import FileResponse
from django.utils.timezone import now
from reportlab.lib.colors import red, black
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas

from cookbook.models import Batch, BatchItem, Report


def batch_report(report_id: int):
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

    batches = Batch.objects.exclude(is_backup=True)

    if DEBUG:
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
    report_name = 'batch_report_' + str(now()) + '.pdf'
    report = Report.objects.get(id=report_id)
    report.pdf = File(name=report_name, file=buffer)
    report.save()
    return report


def batch_report_save(request, report_id: int):
    report = batch_report(report_id)
    return FileResponse(report.pdf, filename=report.pdf.name, as_attachment=True)


def batch_report_print(request, report_id: int):
    report = batch_report(report_id)
    return FileResponse(report.pdf, filename=report.pdf.name, as_attachment=False)
