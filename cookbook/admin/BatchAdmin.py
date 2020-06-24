from django.contrib import admin
from cookbook.models import Batch, BatchItem


class BatchItemInLine(admin.TabularInline):
    model = BatchItem
    extra = 1


@admin.register(Batch)
class BatchAdmin(admin.ModelAdmin):
    inlines = [BatchItemInLine, ]
