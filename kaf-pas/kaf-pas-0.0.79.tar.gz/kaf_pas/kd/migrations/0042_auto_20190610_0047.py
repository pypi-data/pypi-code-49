# Generated by Django 2.2.2 on 2019-06-10 00:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kd', '0041_auto_20190609_1918'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='document_attr_cross',
            unique_together=set(),
        ),
    ]
