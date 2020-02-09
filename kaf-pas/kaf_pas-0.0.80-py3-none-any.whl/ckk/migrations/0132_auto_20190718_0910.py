# Generated by Django 2.2.3 on 2019-07-18 09:10

import bitfield.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ckk', '0131_auto_20190718_0909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='props',
            field=bitfield.models.BitField((('relevant', 'Актуальность'), ('from_cdw', 'Получено из чертежа'), ('from_spw', 'Получено из спецификации'), ('for_line', 'Строка спецификации'), ('from_pdf', 'Получено из бумажного архива'), ('man_input', 'Занесено вручную'), ('draged', 'Перенесего из чертежей')), db_index=True, default=1),
        ),
    ]
