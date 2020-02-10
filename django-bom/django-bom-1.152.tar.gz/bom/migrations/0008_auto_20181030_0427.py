# Generated by Django 2.1.1 on 2018-10-30 04:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bom', '0007_auto_20181009_0256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='part',
            name='primary_manufacturer_part',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='primary_manufacturer_part', to='bom.ManufacturerPart'),
        ),
    ]
