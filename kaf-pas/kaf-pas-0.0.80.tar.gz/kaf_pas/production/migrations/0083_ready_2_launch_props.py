# Generated by Django 2.2.6 on 2019-10-30 16:48

import bitfield.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0082_auto_20191029_1934'),
    ]

    operations = [
        migrations.AddField(
            model_name='ready_2_launch',
            name='props',
            field=bitfield.models.BitField((('check_qty', 'Проверять длительность'), ('check_num', 'Проверять № п/п'), ('check_material', 'Проверять материалы'), ('check_resources', 'Проверять ресурсы'), ('check_edizm', 'Проверять еденицу измерения')), db_index=True, default=0),
        ),
    ]
