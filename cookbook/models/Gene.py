from django.db import models


class Gene(models.Model):
    name = models.CharField(max_length=32, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    recipe = models.ForeignKey('Recipe', models.DO_NOTHING, blank=True, null=True)
    program = models.ForeignKey('Program', models.DO_NOTHING, blank=True, null=True)
    used_in_batch = models.BooleanField(default=False)

    class Meta:
        managed = True
        db_table = 'cookbook_gene'

    def __str__(self):
        return self.name
