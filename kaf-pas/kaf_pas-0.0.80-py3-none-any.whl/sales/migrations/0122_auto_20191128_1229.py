# Generated by Django 2.2.7 on 2019-11-28 12:29

from django.db import migrations
import django.db.models.deletion
import isc_common.fields.related


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0121_auto_20191128_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tec_spc_item_line',
            name='item_line',
            field=isc_common.fields.related.ForeignKeyProtect(on_delete=django.db.models.deletion.PROTECT, to='ckk.Item_line'),
        ),
        migrations.AlterField(
            model_name='tec_spc_item_refs',
            name='item_refs',
            field=isc_common.fields.related.ForeignKeyProtect(on_delete=django.db.models.deletion.PROTECT, to='ckk.Item_refs'),
        ),
    ]
