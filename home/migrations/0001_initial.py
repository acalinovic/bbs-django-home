# Generated by Django 3.0.7 on 2020-06-10 14:07

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=32, null=True)),
                ('label', models.CharField(blank=True, max_length=32, null=True)),
                ('order_nbr', models.IntegerField(blank=True, null=True)),
                ('parent', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='sub_menus', to='home.Menu')),
            ],
            options={
                'ordering': ['order_nbr'],
            },
            managers=[
                ('repository', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=32, null=True)),
                ('label', models.CharField(blank=True, max_length=32, null=True)),
                ('command', models.CharField(blank=True, default='home', max_length=1024, null=True)),
                ('order_nbr', models.IntegerField(blank=True, null=True)),
                ('parent', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='commands', to='home.Menu')),
            ],
            options={
                'ordering': ['order_nbr'],
            },
            managers=[
                ('repository', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='MenuItemOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('param', models.CharField(blank=True, max_length=16, null=True, verbose_name='Parameter name')),
                ('value', models.CharField(blank=True, max_length=16, null=True, verbose_name='Parameter value')),
                ('menu_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menu_item', to='home.MenuItem', verbose_name='options')),
            ],
        ),
    ]
