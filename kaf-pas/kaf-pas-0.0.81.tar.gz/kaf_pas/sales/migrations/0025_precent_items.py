# Generated by Django 2.2.1 on 2019-05-23 17:04

from django.db import migrations, models
import django.db.models.deletion
import isc_common.fields.related


class Migration(migrations.Migration):

    dependencies = [
        ('ckk', '0055_auto_20190523_1125'),
        ('sales', '0024_remove_precent_operation_plan_templates'),
    ]

    operations = [
        migrations.CreateModel(
            name='Precent_items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', isc_common.fields.related.ForeignKeyProtect(on_delete=django.db.models.deletion.PROTECT, to='ckk.Item')),
                ('precent', isc_common.fields.related.ForeignKeyProtect(on_delete=django.db.models.deletion.PROTECT, to='sales.Precent')),
            ],
            options={
                'verbose_name': 'Кросс таблица',
                'unique_together': {('item', 'precent')},
            },
        ),
    ]
