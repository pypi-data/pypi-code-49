# Generated by Django 2.2.8 on 2019-12-08 12:52

import bitfield.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ckk', '0163_locations_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='item_refs',
            name='props',
            field=bitfield.models.BitField((('relevant', 'Актуальность'),), db_index=True, default=1),
        ),
    ]
