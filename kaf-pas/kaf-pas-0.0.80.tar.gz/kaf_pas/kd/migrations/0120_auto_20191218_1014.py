# Generated by Django 2.2.8 on 2019-12-18 10:14

from django.db import migrations
import django.db.models.deletion
import isc_common.fields.related


class Migration(migrations.Migration):

    dependencies = [
        ('kd', '0119_lotsman_documents_hierarcy_attr_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lotsman_documents_hierarcy',
            name='attr_type',
            field=isc_common.fields.related.ForeignKeyProtect(on_delete=django.db.models.deletion.PROTECT, to='ckk.Attr_type', verbose_name='Тип документа'),
        ),
    ]
