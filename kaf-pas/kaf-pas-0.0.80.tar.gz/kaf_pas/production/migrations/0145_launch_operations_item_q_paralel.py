# Generated by Django 2.2.8 on 2019-12-04 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0144_auto_20191204_2013'),
    ]

    operations = [
        migrations.AddField(
            model_name='launch_operations_item',
            name='q_paralel',
            field=models.PositiveIntegerField(default=None),
        ),
    ]
