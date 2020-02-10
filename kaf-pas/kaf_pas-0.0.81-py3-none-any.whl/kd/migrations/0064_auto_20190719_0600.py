# Generated by Django 2.2.3 on 2019-07-19 06:00

import bitfield.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kd', '0063_auto_20190715_0842'),
    ]

    operations = [
        migrations.AddField(
            model_name='documents_thumb',
            name='props',
            field=bitfield.models.BitField((('relevant', 'Актуальность'),), db_index=True, default=1),
        ),
        migrations.AddField(
            model_name='documents_thumb10',
            name='props',
            field=bitfield.models.BitField((('relevant', 'Актуальность'),), db_index=True, default=1),
        ),
        migrations.AlterModelTable(
            name='documents_view',
            table='kd_documents_mview',
        ),
    ]
