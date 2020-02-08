# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-19 13:10
import django.core.validators
from django.db import migrations, models
import re
import waldur_freeipa.models


class Migration(migrations.Migration):

    dependencies = [
        ('waldur_freeipa', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.CharField(help_text='Letters, numbers and ./+/-/_ characters', max_length=32, unique=True, validators=[waldur_freeipa.models.validate_username, django.core.validators.RegexValidator(re.compile(r'^[a-zA-Z0-9_.][a-zA-Z0-9_.-]*[a-zA-Z0-9_.$-]?$'), 'Enter a valid username.', 'invalid')], verbose_name='username'),
        ),
    ]
