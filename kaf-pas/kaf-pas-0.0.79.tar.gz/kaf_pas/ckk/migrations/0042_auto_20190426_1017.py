# Generated by Django 2.2 on 2019-04-26 10:17

from django.db import migrations
import isc_common.fields.code_field


class Migration(migrations.Migration):

    dependencies = [
        ('ckk', '0041_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='code',
            field=isc_common.fields.code_field.CodeField(unique=True),
        ),
    ]
