# Generated by Django 2.2.7 on 2019-11-21 06:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planing', '0011_launch_item_refs_timing'),
    ]

    operations = [
        migrations.RenameField(
            model_name='launch_item_refs_timing',
            old_name='child',
            new_name='launch_item_refs',
        ),
    ]
