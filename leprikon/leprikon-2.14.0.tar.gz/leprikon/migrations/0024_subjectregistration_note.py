# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-03 12:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leprikon', '0023_accountclosure'),
    ]

    operations = [
        migrations.AddField(
            model_name='subjectregistration',
            name='note',
            field=models.CharField(blank=True, default='', max_length=300, verbose_name='note'),
        ),
    ]
