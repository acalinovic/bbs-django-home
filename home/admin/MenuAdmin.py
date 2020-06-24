from django.contrib import admin
from home.models import Menu, MenuItem


class SubMenuInline(admin.TabularInline):
    verbose_name = 'Sub Menu'
    fk_name = 'parent'
    extra = 0
    model = Menu
    show_change_link = True


class MenuItemInline(admin.TabularInline):
    extra = 0
    model = MenuItem
    show_change_link = True


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = [
        'label',
        'parent',
        'order_nbr',
    ]
    inlines = [
        SubMenuInline,
        MenuItemInline,
    ]
    ordering = ('parent', 'order_nbr',)

