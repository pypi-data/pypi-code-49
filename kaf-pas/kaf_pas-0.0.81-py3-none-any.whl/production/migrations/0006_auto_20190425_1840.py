# Generated by Django 2.2 on 2019-04-25 18:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0005_auto_20190425_1808'),
    ]

    operations = [
        migrations.RenameField(
            model_name='operation_plan_templates_item_lines',
            old_name='itemLine',
            new_name='item_line',
        ),
    ]
