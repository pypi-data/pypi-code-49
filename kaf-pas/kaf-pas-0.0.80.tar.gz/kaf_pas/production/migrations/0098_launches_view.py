# Generated by Django 2.2.7 on 2019-11-17 18:58

from django.db import migrations, models
import django.utils.timezone
import isc_common.fields.code_field
import isc_common.fields.description_field
import isc_common.fields.name_field


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0097_auto_20191117_1758'),
    ]

    operations = [
        migrations.CreateModel(
            name='Launches_view',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='Идентификатор')),
                ('deleted_at', models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='Дата мягкого удаления')),
                ('editing', models.BooleanField(default=True, verbose_name='Возможность редактирования')),
                ('deliting', models.BooleanField(default=True, verbose_name='Возможность удаления')),
                ('lastmodified', models.DateTimeField(db_index=True, default=django.utils.timezone.now, editable=False, verbose_name='Последнее обновление')),
                ('code', isc_common.fields.code_field.CodeField(blank=True, null=True)),
                ('name', isc_common.fields.name_field.NameField(blank=True, null=True)),
                ('description', isc_common.fields.description_field.DescriptionField()),
                ('date', models.DateTimeField()),
                ('qty', models.PositiveIntegerField()),
                ('isFolder', models.BooleanField()),
            ],
            options={
                'verbose_name': 'Запуски',
                'db_table': 'production_launches_view',
                'managed': False,
            },
        ),
    ]
