# Generated by Django 2.2.7 on 2019-11-17 16:20

import bitfield.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0115_auto_20191117_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statusdogovor',
            name='props',
            field=bitfield.models.BitField((('real', 'Реальный статус'), ('disabled', 'Неактивная запись в гриде')), db_index=True, default=1),
        ),
    ]
