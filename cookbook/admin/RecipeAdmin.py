from django.contrib import admin
from cookbook.models import RecipeItem, Recipe


class RecipeItemInLine(admin.TabularInline):
    model = RecipeItem
    extra = 1


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeItemInLine, ]
    pass
