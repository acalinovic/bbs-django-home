from django.contrib import admin
from cookbook.models import RecipeItem


@admin.register(RecipeItem)
class RecipeItemAdmin(admin.ModelAdmin):
    pass
