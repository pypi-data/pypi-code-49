# Generated by Django 2.2.4 on 2019-08-30 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ckk', '0151_auto_20190830_1745'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='status',
            name='code_owner',
        ),
    ]
