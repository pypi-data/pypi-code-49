# Generated by Django 2.1.2 on 2018-12-11 19:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("survey", "0008_translated_name_for_models")]

    operations = [
        migrations.AlterField(
            model_name="question",
            name="category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="questions",
                to="survey.Category",
                verbose_name="Category",
            ),
        ),
        migrations.AlterField(
            model_name="response",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
                verbose_name="User",
            ),
        ),
    ]
