# Generated by Django 2.2.7 on 2020-01-21 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace_checklist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='solution',
            field=models.TextField(blank=True, null=True),
        ),
    ]
