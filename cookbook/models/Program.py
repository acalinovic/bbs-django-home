from django.db import models


class Program(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'cookbook_program'

    def __str__(self):
        return self.name
