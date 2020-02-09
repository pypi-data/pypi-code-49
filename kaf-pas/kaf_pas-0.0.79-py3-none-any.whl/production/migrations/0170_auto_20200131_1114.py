# Generated by Django 3.0.2 on 2020-01-31 11:14

from django.db import migrations, models
import django.db.models.expressions


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0169_operation_def_resources_props'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='launch_item_refs',
            constraint=models.CheckConstraint(check=models.Q(_negated=True, child=django.db.models.expressions.F('parent')), name='Launch_item_refs_not_circulate_refs'),
        ),
    ]
