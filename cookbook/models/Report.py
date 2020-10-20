from django.db import models
from django.utils.timezone import now


class Report(models.Model):
    pdf = models.FileField(upload_to='reports', null=True, blank=True)
    creation_date = models.DateTimeField(blank=False, null=False, default=now)
    archived = models.BooleanField(blank=True, null=True, default=False)

    class Meta:
        managed = True
        db_table = 'cookbook_report'

    def __str__(self):
        return self.pdf.name or 'undefined'
