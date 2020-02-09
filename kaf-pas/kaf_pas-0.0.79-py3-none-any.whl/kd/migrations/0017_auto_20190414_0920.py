# Generated by Django 2.2 on 2019-04-14 09:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('kd', '0016_auto_20190414_0919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document_attrs',
            name='lastmodified',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Последнее обновление'),
        ),
        migrations.AlterField(
            model_name='documents',
            name='lastmodified',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Последнее обновление'),
        ),
        migrations.AlterField(
            model_name='documents_thumb',
            name='lastmodified',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Последнее обновление'),
        ),
        migrations.AlterField(
            model_name='documents_thumb10',
            name='lastmodified',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Последнее обновление'),
        ),
        migrations.AlterField(
            model_name='pathes',
            name='lastmodified',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Последнее обновление'),
        ),
    ]
