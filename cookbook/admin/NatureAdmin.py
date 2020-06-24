from django.contrib import admin
from cookbook.models import Nature


@admin.register(Nature)
class NatureAdmin(admin.ModelAdmin):
    pass
