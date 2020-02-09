# Generated by Django 2.2.3 on 2019-07-18 09:09

import bitfield.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ckk', '0130_remove_materials_ed_izm'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='props',
            field=bitfield.models.BitField((('relevant', 'Актуальность'), ('from_cdw', 'Получено из чертежа'), ('from_spw', 'Получено из спецификации'), ('for_line', 'Строка спецификации'), ('from_pdf', 'Получено из бумажного архива'), ('man_input', 'Занесено вручную'), ('draged_from_cdw', 'Перенесего из чертежей')), db_index=True, default=1),
        ),
    ]
