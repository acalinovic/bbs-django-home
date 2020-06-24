from django.contrib import admin

from home.models import MenuItem, MenuItemOption


class MenuItemOptionInline(admin.TabularInline):
    extra = 0
    model = MenuItemOption
    show_change_link = True


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = [
        'label',
        'parent',
        'command',
        'order_nbr',
    ]
    inlines = [
        MenuItemOptionInline,
    ]
    ordering = ('order_nbr',)
