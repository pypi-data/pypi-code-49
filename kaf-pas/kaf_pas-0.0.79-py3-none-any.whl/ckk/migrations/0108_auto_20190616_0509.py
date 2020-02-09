# Generated by Django 2.2.2 on 2019-06-16 05:09

from django.db import migrations
import isc_common.fields.code_field
import isc_common.fields.description_field
import isc_common.fields.name_field


class Migration(migrations.Migration):

    dependencies = [
        ('ckk', '0107_auto_20190616_0450'),
    ]

    operations = [
        migrations.AddField(
            model_name='materials',
            name='code',
            field=isc_common.fields.code_field.CodeField(),
        ),
        migrations.AddField(
            model_name='materials',
            name='description',
            field=isc_common.fields.description_field.DescriptionField(),
        ),
        migrations.AddField(
            model_name='materials',
            name='name',
            field=isc_common.fields.name_field.NameField(),
        ),
    ]
