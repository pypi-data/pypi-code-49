# Generated by Django 2.2.6 on 2019-10-29 15:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planing', '0009_auto_20191020_1914'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='operations_plan_refs',
            name='child',
        ),
        migrations.RemoveField(
            model_name='operations_plan_refs',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='operationsplan',
            name='opertype',
        ),
        migrations.RemoveField(
            model_name='operationsplan',
            name='status',
        ),
        migrations.DeleteModel(
            name='Prod_task_status',
        ),
        migrations.RemoveField(
            model_name='prod_tasks',
            name='creator',
        ),
        migrations.RemoveField(
            model_name='prod_tasks',
            name='importances',
        ),
        migrations.RemoveField(
            model_name='prod_tasks',
            name='item',
        ),
        migrations.RemoveField(
            model_name='prod_tasks',
            name='status',
        ),
        migrations.RemoveField(
            model_name='operations_plan_view',
            name='operationsplan_ptr',
        ),
        migrations.DeleteModel(
            name='Operation_plan_types',
        ),
        migrations.DeleteModel(
            name='Operations_plan_refs',
        ),
        migrations.DeleteModel(
            name='OperationsPlan',
        ),
        migrations.DeleteModel(
            name='OperationsPlanStatus',
        ),
        migrations.DeleteModel(
            name='Prod_task_importances',
        ),
        migrations.DeleteModel(
            name='Prod_tasks',
        ),
        migrations.DeleteModel(
            name='Operations_plan_view',
        ),
    ]
