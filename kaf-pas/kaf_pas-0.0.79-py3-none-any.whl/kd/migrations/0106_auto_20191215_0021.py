# Generated by Django 2.2.8 on 2019-12-15 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kd', '0105_auto_20191214_1540'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lotsman_documents_hierarcy',
            name='id_lotsman',
        ),
        migrations.AlterField(
            model_name='lotsman_documents_hierarcy',
            name='id',
            field=models.BigIntegerField(primary_key=True, serialize=False, verbose_name='Идентификатор'),
        ),
    ]
