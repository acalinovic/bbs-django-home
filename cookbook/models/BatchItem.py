from django.db import models
from cookbook.models import Batch


class BatchItem(models.Model):
    batch = models.ForeignKey(Batch, models.CASCADE, blank=True, null=True)
    ingredient = models.ForeignKey('Ingredient', models.DO_NOTHING, blank=True, null=True)
    computed_vol = models.FloatField(blank=True, null=True)
    is_manual = models.IntegerField(blank=True, null=True)
    manager = models.Manager()

    class Meta:
        managed = True
        db_table = 'cookbook_batch_item'

    def __str__(self):
        return self.batch.gene.name + ' ' + self.ingredient.name
