# Generated by Django 2.2.1 on 2019-05-23 17:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0027_auto_20190523_1710'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='precent_items',
            options={'verbose_name': 'Комплектация распоряжения'},
        ),
        migrations.AddField(
            model_name='precent_items',
            name='deleted_at',
            field=models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='Дата мягкого удаления'),
        ),
        migrations.AddField(
            model_name='precent_items',
            name='deliting',
            field=models.BooleanField(default=True, verbose_name='Возможность удаления'),
        ),
        migrations.AddField(
            model_name='precent_items',
            name='editing',
            field=models.BooleanField(default=True, verbose_name='Возможность редактирования'),
        ),
        migrations.AddField(
            model_name='precent_items',
            name='id_old',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='Идентификатор старый'),
        ),
        migrations.AddField(
            model_name='precent_items',
            name='lastmodified',
            field=models.DateTimeField(db_index=True, default=django.utils.timezone.now, editable=False, verbose_name='Последнее обновление'),
        ),
        migrations.AlterField(
            model_name='precent_items',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False, verbose_name='Идентификатор'),
        ),
    ]
