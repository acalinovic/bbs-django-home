# Generated by Django 3.1a1 on 2020-07-10 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook', '0009_auto_20200710_1521'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='archived',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]