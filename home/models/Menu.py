from django.db import models
from django.db.models import Manager


class Menu(models.Model):
    name = models.CharField(max_length=32, null=True, blank=True)
    label = models.CharField(max_length=32, null=True, blank=True)
    parent = models.ForeignKey('self', on_delete=models.DO_NOTHING, blank=True, null=True, default=None, related_name='sub_menus')
    order_nbr = models.IntegerField(null=True, blank=True)
    gui_menu = models.BooleanField(default=False)

    repository = Manager()

    @property
    def is_root(self):
        if self.parent:
            return False
        else:
            return True

    @property
    def has_sub_menus(self):
        return hasattr(self, 'sub_menus')

    @property
    def has_commands(self):
        return hasattr(self, 'commands')

    @property
    def get_sub_menus(self):
        return self.__class__.repository.filter(parent=self)

    @property
    def get_commands(self):
        return self.commands

    def __str__(self):
        return self.label

    class Meta:
        ordering = ['order_nbr', ]
