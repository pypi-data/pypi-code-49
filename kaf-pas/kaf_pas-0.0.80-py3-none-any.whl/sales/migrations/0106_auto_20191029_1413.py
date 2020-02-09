# Generated by Django 2.2.6 on 2019-10-29 14:13

import django.db.models.deletion
from django.db import migrations

import isc_common.fields.related


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0105_auto_20191029_0729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dogovors',
            name='parent',
            field=isc_common.fields.related.ForeignKeyProtect(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='sales.Dogovors'),
        ),
    ]
