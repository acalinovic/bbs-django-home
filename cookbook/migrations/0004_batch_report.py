# Generated by Django 3.1a1 on 2020-07-08 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook', '0003_auto_20200708_1533'),
    ]

    operations = [
        migrations.AddField(
            model_name='batch',
            name='report',
            field=models.FileField(blank=True, default=None, null=True, upload_to='reports'),
        ),
    ]
