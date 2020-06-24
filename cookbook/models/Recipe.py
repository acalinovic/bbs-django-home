from django.db import models


class Recipe(models.Model):
    name = models.CharField(max_length=32, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'cookbook_recipe'

    def __str__(self):
        return self.name
