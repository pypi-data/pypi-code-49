# Generated by Django 2.2.5 on 2019-09-03 05:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('capacity', '0003_remove_resources_id_old'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Resources',
        ),
    ]
