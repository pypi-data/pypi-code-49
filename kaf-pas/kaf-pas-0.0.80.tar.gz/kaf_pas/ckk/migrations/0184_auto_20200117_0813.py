# Generated by Django 3.0.2 on 2020-01-17 08:13

import bitfield.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ckk', '0183_auto_20200117_0811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item_refs',
            name='props',
            field=bitfield.models.BitField((('relevant', 'Актуальность'), ('relevant_in_planing', 'Учавствует в планировании')), db_index=True, default=3),
        ),
    ]
