# Generated by Django 2.2.3 on 2019-07-09 21:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('kd', '0054_uploades_uploades_documents'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploades_documents',
            name='deleted_at',
            field=models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='Дата мягкого удаления'),
        ),
        migrations.AddField(
            model_name='uploades_documents',
            name='deliting',
            field=models.BooleanField(default=True, verbose_name='Возможность удаления'),
        ),
        migrations.AddField(
            model_name='uploades_documents',
            name='editing',
            field=models.BooleanField(default=True, verbose_name='Возможность редактирования'),
        ),
        migrations.AddField(
            model_name='uploades_documents',
            name='id_old',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='Идентификатор старый'),
        ),
        migrations.AddField(
            model_name='uploades_documents',
            name='lastmodified',
            field=models.DateTimeField(db_index=True, default=django.utils.timezone.now, editable=False, verbose_name='Последнее обновление'),
        ),
        migrations.AlterField(
            model_name='uploades_documents',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False, verbose_name='Идентификатор'),
        ),
    ]
