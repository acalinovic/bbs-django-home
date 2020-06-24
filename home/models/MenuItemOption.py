from django.db import models


class MenuItemOption(models.Model):
    param = models.CharField(max_length=16, blank=True, null=True, verbose_name='Parameter name')
    value = models.CharField(max_length=16, blank=True, null=True, verbose_name='Parameter value')
    menu_item = models.ForeignKey('MenuItem', blank=False, null=False, related_name='menu_item', verbose_name='options', on_delete=models.CASCADE)
