# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-03-08 12:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saas', '0004_auto_20180817_0026'),
    ]

    operations = [
        migrations.AddField(
            model_name='party',
            name='type',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, '\u516c\u53f8'), (2, '\u5b66\u6821')], default=1, verbose_name='\u7c7b\u522b'),
        ),
    ]
