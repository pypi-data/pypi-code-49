# Generated by Django 2.2.6 on 2019-10-29 19:34

import django.utils.timezone
from django.db import migrations, models

import isc_common.fields.related


class Migration(migrations.Migration):

    dependencies = [
        ('ckk', '0158_delete_status'),
        ('production', '0081_remove_ready_2_launch_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='ready_2_launch',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Ready_2_launch_detail',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='Идентификатор')),
                ('deleted_at', models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='Дата мягкого удаления')),
                ('editing', models.BooleanField(default=True, verbose_name='Возможность редактирования')),
                ('deliting', models.BooleanField(default=True, verbose_name='Возможность удаления')),
                ('lastmodified', models.DateTimeField(db_index=True, default=django.utils.timezone.now, editable=False, verbose_name='Последнее обновление')),
                ('notes', models.TextField(blank=True, null=True)),
                ('item', isc_common.fields.related.ForeignKeyCascade(on_delete=django.db.models.deletion.CASCADE, to='ckk.Item')),
                ('ready', isc_common.fields.related.ForeignKeyCascade(on_delete=django.db.models.deletion.CASCADE, to='production.Ready_2_launch')),
            ],
            options={
                'verbose_name': 'Детализация готовности к запуску',
            },
        ),
    ]
