# Generated by Django 2.2.3 on 2019-07-09 19:14

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import isc_common.fields.related


class Migration(migrations.Migration):

    dependencies = [
        ('kd', '0053_auto_20190629_1256'),
    ]

    operations = [
        migrations.CreateModel(
            name='Uploades',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='Идентификатор')),
                ('id_old', models.BigIntegerField(blank=True, null=True, verbose_name='Идентификатор старый')),
                ('deleted_at', models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='Дата мягкого удаления')),
                ('editing', models.BooleanField(default=True, verbose_name='Возможность редактирования')),
                ('deliting', models.BooleanField(default=True, verbose_name='Возможность удаления')),
                ('lastmodified', models.DateTimeField(db_index=True, default=django.utils.timezone.now, editable=False, verbose_name='Последнее обновление')),
                ('path', isc_common.fields.related.ForeignKeyProtect(on_delete=django.db.models.deletion.PROTECT, to='kd.Pathes')),
            ],
            options={
                'verbose_name': 'Загрузки внешних данных',
            },
        ),
        migrations.CreateModel(
            name='Uploades_documents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', isc_common.fields.related.ForeignKeyProtect(on_delete=django.db.models.deletion.PROTECT, to='kd.Documents')),
                ('upload', isc_common.fields.related.ForeignKeyProtect(on_delete=django.db.models.deletion.PROTECT, to='kd.Uploades')),
            ],
            options={
                'verbose_name': 'Кросс таблица',
            },
        ),
    ]
