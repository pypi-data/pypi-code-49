# Generated by Django 2.2.3 on 2019-07-02 22:19

from django.db import migrations
import isc_common.fields.code_field


class Migration(migrations.Migration):

    dependencies = [
        ('ckk', '0119_auto_20190702_1440'),
    ]

    operations = [
        migrations.AddField(
            model_name='material_type',
            name='gost',
            field=isc_common.fields.code_field.CodeField(blank=True, null=True),
        ),
    ]
