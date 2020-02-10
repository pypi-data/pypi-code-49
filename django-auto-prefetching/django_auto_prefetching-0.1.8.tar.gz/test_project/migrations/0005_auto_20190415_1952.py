# Generated by Django 2.2 on 2019-04-15 17:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("test_project", "0004_auto_20190415_1921")]

    operations = [
        migrations.CreateModel(
            name="DeeplyNestedChildren",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                )
            ],
        ),
        migrations.CreateModel(
            name="DeeplyNestedParent",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                )
            ],
        ),
        migrations.CreateModel(
            name="GrandKids",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "parent",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="children",
                        to="test_project.DeeplyNestedChildren",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="DeeplyNestedChildrenToys",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "owners",
                    models.ManyToManyField(
                        related_name="toys", to="test_project.DeeplyNestedChildren"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="deeplynestedchildren",
            name="parent",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="children_set",
                to="test_project.DeeplyNestedParent",
            ),
        ),
        migrations.CreateModel(
            name="DeeplyNestedChild",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "parent",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="child",
                        to="test_project.DeeplyNestedParent",
                    ),
                ),
            ],
        ),
    ]
