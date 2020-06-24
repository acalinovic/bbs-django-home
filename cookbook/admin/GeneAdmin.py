from django.contrib import admin
from cookbook.models import Gene


@admin.register(Gene)
class GeneAdmin(admin.ModelAdmin):
    pass
