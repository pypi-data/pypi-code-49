# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-21 09:16
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('waldur_jira', '0017_project_action'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='runtime_state',
            field=models.CharField(blank=True, max_length=150, verbose_name='runtime state'),
        ),
    ]
