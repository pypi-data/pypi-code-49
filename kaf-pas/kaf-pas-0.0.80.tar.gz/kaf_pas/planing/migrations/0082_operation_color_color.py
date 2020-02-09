# Generated by Django 3.0.2 on 2020-01-22 07:52

from django.db import migrations
import django.db.models.deletion
import isc_common.fields.related


class Migration(migrations.Migration):

    dependencies = [
        ('isc_common', '0034_standard_colors_color'),
        ('planing', '0081_remove_operation_color_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='operation_color',
            name='color',
            field=isc_common.fields.related.ForeignKeyProtect(default=None, on_delete=django.db.models.deletion.PROTECT, to='isc_common.Standard_colors'),
        ),
    ]
