from django.db import models


class Nature(models.Model):
    name = models.CharField(max_length=16, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'cookbook_nature'

    def __str__(self):
        return self.name
