from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    nature = models.ForeignKey('Nature', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'cookbook_ingredient'

    def __str__(self):
        return self.name
