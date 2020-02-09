# Generated by Django 2.2.8 on 2019-12-15 20:48

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import isc_common.fields.name_field
import isc_common.fields.related


class Migration(migrations.Migration):

    dependencies = [
        ('kd', '0113_auto_20191215_1120'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lotsman_documents_hierarcy_view',
            fields=[
                ('deleted_at', models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='Дата мягкого удаления')),
                ('editing', models.BooleanField(default=True, verbose_name='Возможность редактирования')),
                ('deliting', models.BooleanField(default=True, verbose_name='Возможность удаления')),
                ('lastmodified', models.DateTimeField(db_index=True, default=django.utils.timezone.now, editable=False, verbose_name='Последнее обновление')),
                ('id', models.BigIntegerField(primary_key=True, serialize=False, verbose_name='Идентификатор')),
                ('parent_id', models.BigIntegerField(blank=True, null=True)),
                ('STMP_1', isc_common.fields.name_field.NameField(blank=True, null=True)),
                ('STMP_2', isc_common.fields.name_field.NameField(blank=True, null=True)),
                ('STMP_120', isc_common.fields.name_field.NameField(blank=True, null=True)),
                ('SPC_CLM_KOD', isc_common.fields.name_field.NameField(blank=True, null=True)),
                ('SPC_CLM_FORMAT', isc_common.fields.name_field.NameField(blank=True, null=True)),
                ('SPC_CLM_MASSA', isc_common.fields.name_field.NameField(blank=True, null=True)),
                ('SPC_CLM_POS', isc_common.fields.name_field.NameField(blank=True, null=True)),
                ('SPC_CLM_NAME', isc_common.fields.name_field.NameField(blank=True, null=True)),
                ('SPC_CLM_MARK', isc_common.fields.name_field.NameField(blank=True, null=True)),
                ('SPC_CLM_COUNT', isc_common.fields.name_field.NameField(blank=True, null=True)),
                ('Документ_на_материал', isc_common.fields.name_field.NameField(blank=True, null=True)),
                ('Наименование_материала', isc_common.fields.name_field.NameField(blank=True, null=True)),
                ('Документ_на_сортамент', isc_common.fields.name_field.NameField(blank=True, null=True)),
                ('Наименование_сортамента', isc_common.fields.name_field.NameField(blank=True, null=True)),
                ('section', isc_common.fields.name_field.NameField(blank=True, null=True)),
                ('subsection', isc_common.fields.name_field.NameField(blank=True, null=True)),
                ('isFolder', models.BooleanField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Иерархия документа из Лоцмана',
                'db_table': 'kd_lotsman_documents_hierarcy_mview',
                'managed': False,
            },
        ),
        migrations.AddField(
            model_name='documents_thumb',
            name='lotsman_document',
            field=isc_common.fields.related.ForeignKeyProtect(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='kd.Lotsman_documents_hierarcy', verbose_name='Лоцман'),
        ),
        migrations.AddField(
            model_name='documents_thumb10',
            name='lotsman_document',
            field=isc_common.fields.related.ForeignKeyProtect(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='kd.Lotsman_documents_hierarcy', verbose_name='Лоцман'),
        ),
        migrations.AlterField(
            model_name='documents_thumb',
            name='document',
            field=isc_common.fields.related.ForeignKeyProtect(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='kd.Documents', verbose_name='КД'),
        ),
        migrations.AlterField(
            model_name='documents_thumb10',
            name='document',
            field=isc_common.fields.related.ForeignKeyProtect(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='kd.Documents', verbose_name='КД'),
        ),
    ]
