# Generated by Django 2.2.8 on 2019-12-06 22:02

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import isc_common.fields.related


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0155_auto_20191206_2152'),
        ('planing', '0033_operation_launch_operations_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='operation_launch_operations_item',
            name='operation',
            field=isc_common.fields.related.ForeignKeyProtect(default=None, on_delete=django.db.models.deletion.PROTECT, to='planing.Operations'),
        ),
        migrations.CreateModel(
            name='Operation_launch_operation_resources',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='Идентификатор')),
                ('deleted_at', models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='Дата мягкого удаления')),
                ('editing', models.BooleanField(default=True, verbose_name='Возможность редактирования')),
                ('deliting', models.BooleanField(default=True, verbose_name='Возможность удаления')),
                ('lastmodified', models.DateTimeField(db_index=True, default=django.utils.timezone.now, editable=False, verbose_name='Последнее обновление')),
                ('launch_operation_resources', isc_common.fields.related.ForeignKeyProtect(on_delete=django.db.models.deletion.PROTECT, to='production.Launch_operation_resources')),
                ('operation', isc_common.fields.related.ForeignKeyProtect(on_delete=django.db.models.deletion.PROTECT, to='planing.Operations')),
            ],
            options={
                'verbose_name': 'Кросс таблица',
            },
        ),
    ]
