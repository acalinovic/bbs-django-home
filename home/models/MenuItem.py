from django.db import models
from django.db.models import Manager


class MenuItem(models.Model):
    name = models.CharField(max_length=32, null=True, blank=True)
    label = models.CharField(max_length=32, null=True, blank=True)
    command = models.CharField(max_length=1024, blank=True, null=True, default='home')
    parent = models.ForeignKey('Menu',
                               related_name='commands',
                               on_delete=models.CASCADE,
                               blank=True,
                               null=True,
                               default=None
                               )
    order_nbr = models.IntegerField(null=True, blank=True)

    repository = Manager()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['order_nbr', ]
