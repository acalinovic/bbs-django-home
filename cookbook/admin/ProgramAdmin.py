from django.contrib import admin
from cookbook.models import Program


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    pass
