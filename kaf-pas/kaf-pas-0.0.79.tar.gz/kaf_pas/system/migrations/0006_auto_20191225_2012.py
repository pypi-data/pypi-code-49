# Generated by Django 2.2.8 on 2019-12-25 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0005_contants_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contants',
            name='value',
            field=models.TextField(blank=True, db_index=True, null=True),
        ),
    ]
