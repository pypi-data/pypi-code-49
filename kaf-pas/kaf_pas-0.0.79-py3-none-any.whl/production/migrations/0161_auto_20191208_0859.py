# Generated by Django 2.2.8 on 2019-12-08 08:59

from django.db import migrations

from kaf_pas.production.models.launch_operation_resources import Launch_operation_resourcesManager
from kaf_pas.production.models.operation_resources import Operation_resourcesManager


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0160_auto_20191208_0812'),
    ]

    operations = [
        migrations.RunPython(Launch_operation_resourcesManager.refresh_resource),
        migrations.RunPython(Operation_resourcesManager.refresh_resource),
    ]
