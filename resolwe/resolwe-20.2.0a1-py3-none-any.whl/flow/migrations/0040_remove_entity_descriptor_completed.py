# Generated by Django 2.2.4 on 2019-08-22 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("flow", "0039_entity_collection_cascade"),
    ]

    operations = [
        migrations.RemoveField(model_name="entity", name="descriptor_completed",),
    ]
