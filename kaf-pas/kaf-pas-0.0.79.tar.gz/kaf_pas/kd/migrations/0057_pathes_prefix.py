# Generated by Django 2.2.3 on 2019-07-10 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kd', '0056_uploades_log'),
    ]

    operations = [
        migrations.AddField(
            model_name='pathes',
            name='prefix',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Префикс к полному пути'),
        ),
    ]
