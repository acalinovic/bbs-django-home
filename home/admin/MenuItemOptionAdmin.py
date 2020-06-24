from django.contrib import admin

from home.models import MenuItemOption


@admin.register(MenuItemOption)
class MenuItemOptionAdmin(admin.ModelAdmin):
    pass

