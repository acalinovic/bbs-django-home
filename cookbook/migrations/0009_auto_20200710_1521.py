# Generated by Django 3.1a1 on 2020-07-10 15:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook', '0008_auto_20200710_1424'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='batchitem',
            options={'managed': True, 'ordering': ['ingredient__nature__order_nbr']},
        ),
        migrations.AlterField(
            model_name='recipeitem',
            name='ingredient',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='ingredient', to='cookbook.ingredient'),
        ),
    ]
