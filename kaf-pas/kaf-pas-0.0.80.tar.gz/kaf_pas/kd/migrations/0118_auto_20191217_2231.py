# Generated by Django 2.2.8 on 2019-12-17 22:31

from django.db import migrations
import django.db.models.deletion
import isc_common.fields.related


class Migration(migrations.Migration):

    dependencies = [
        ('kd', '0117_auto_20191217_0709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lotsman_documents_hierarcy',
            name='document',
            field=isc_common.fields.related.ForeignKeyProtect(on_delete=django.db.models.deletion.PROTECT, to='kd.Documents'),
        ),
        migrations.AlterField(
            model_name='lotsman_documents_hierarcy_refs',
            name='child',
            field=isc_common.fields.related.ForeignKeyProtect(on_delete=django.db.models.deletion.PROTECT, related_name='Lotsman_documents_hierarcy_child', to='kd.Lotsman_documents_hierarcy'),
        ),
        migrations.AlterField(
            model_name='lotsman_documents_hierarcy_refs',
            name='parent',
            field=isc_common.fields.related.ForeignKeyProtect(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='Lotsman_documents_hierarcy_parent', to='kd.Lotsman_documents_hierarcy'),
        ),
    ]
