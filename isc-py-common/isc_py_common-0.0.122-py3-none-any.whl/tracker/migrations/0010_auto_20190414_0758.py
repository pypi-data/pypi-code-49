# Generated by Django 2.2 on 2019-04-14 07:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0009_auto_20190414_0756'),
    ]

    operations = [
        migrations.RenameField(
            model_name='messages',
            old_name='deleted',
            new_name='deleted_at',
        ),
        migrations.RenameField(
            model_name='messages_state',
            old_name='deleted',
            new_name='deleted_at',
        ),
        migrations.RenameField(
            model_name='messages_theme',
            old_name='deleted',
            new_name='deleted_at',
        ),
    ]
