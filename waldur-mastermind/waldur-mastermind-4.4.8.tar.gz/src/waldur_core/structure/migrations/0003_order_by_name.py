# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-10-11 15:27
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0002_immutable_default_json'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'ordering': ('name',), 'verbose_name': 'organization'},
        ),
        migrations.AlterModelOptions(
            name='servicesettings',
            options={'ordering': ('name',), 'verbose_name': 'Service settings', 'verbose_name_plural': 'Service settings'},
        ),
    ]
