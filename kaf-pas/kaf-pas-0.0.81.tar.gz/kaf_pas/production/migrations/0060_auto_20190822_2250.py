# Generated by Django 2.2.4 on 2019-08-22 22:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0059_auto_20190821_0950'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='operation_material',
            name='id_old',
        ),
        migrations.RemoveField(
            model_name='operation_plan_types',
            name='id_old',
        ),
        migrations.RemoveField(
            model_name='operation_resources',
            name='id_old',
        ),
        migrations.RemoveField(
            model_name='operations',
            name='id_old',
        ),
        migrations.RemoveField(
            model_name='operations_item',
            name='id_old',
        ),
        migrations.RemoveField(
            model_name='operationsplan',
            name='id_old',
        ),
        migrations.RemoveField(
            model_name='resource',
            name='id_old',
        ),
    ]
