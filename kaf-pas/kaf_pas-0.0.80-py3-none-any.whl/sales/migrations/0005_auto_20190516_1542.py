# Generated by Django 2.2.1 on 2019-05-16 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0004_auto_20190425_0829'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='full_name',
            field=models.TextField(blank=True, default=None, null=True, verbose_name='Полное наименование'),
        ),
        migrations.AddField(
            model_name='customer',
            name='name',
            field=models.CharField(db_index=True, default=None, max_length=255, verbose_name='Наименование'),
        ),
    ]
