from django.db import models
from django.utils.timezone import now


class Batch(models.Model):
    gene = models.ForeignKey('Gene', models.DO_NOTHING, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True, default=0)
    date_created = models.DateTimeField(blank=True, null=True, default=now)
    date_modified = models.CharField(max_length=45, blank=True, null=True)
    is_backup = models.BooleanField(default=False)
    report = models.ForeignKey('Report', models.DO_NOTHING, blank=True, null=True, default=None, related_name='batches')

    class Meta:
        managed = True
        db_table = 'cookbook_batch'

    def __str__(self):
        return self.gene.name + ' X ' + str(self.quantity)
