# Generated by Django 2.2.4 on 2019-08-24 12:50

from django.db import migrations
import isc_common.fields.description_field


class Migration(migrations.Migration):

    dependencies = [
        ('clndr', '0044_auto_20190824_1230'),
    ]

    operations = [
        migrations.AddField(
            model_name='shift_day',
            name='description',
            field=isc_common.fields.description_field.DescriptionField(),
        ),
    ]
