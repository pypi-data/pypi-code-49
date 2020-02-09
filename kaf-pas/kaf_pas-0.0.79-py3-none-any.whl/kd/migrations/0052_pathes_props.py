# Generated by Django 2.2.2 on 2019-06-28 11:26

import bitfield.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kd', '0051_documents_load_error'),
    ]

    operations = [
        migrations.AddField(
            model_name='pathes',
            name='props',
            field=bitfield.models.BitField((('relevant', 'Актуальность'), ('ignored_on_load', 'Не пересматривать обновление контента')), db_index=True, default=1),
        ),
    ]
