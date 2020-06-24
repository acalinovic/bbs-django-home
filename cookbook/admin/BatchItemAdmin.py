from django.contrib import admin
from cookbook.models import BatchItem


@admin.register(BatchItem)
class BatchItemAdmin(admin.ModelAdmin):
    pass
