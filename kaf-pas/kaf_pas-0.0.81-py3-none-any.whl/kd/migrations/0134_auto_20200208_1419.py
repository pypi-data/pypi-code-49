# Generated by Django 3.0.3 on 2020-02-08 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kd', '0133_auto_20200208_1418'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='documents_thumb10',
            unique_together=set(),
        ),
        migrations.AddConstraint(
            model_name='documents_thumb10',
            constraint=models.UniqueConstraint(condition=models.Q(('document', None), ('lotsman_document', None)), fields=('path',), name='Documents_thumb10_unique_constraint_0'),
        ),
        migrations.AddConstraint(
            model_name='documents_thumb10',
            constraint=models.UniqueConstraint(condition=models.Q(document=None), fields=('lotsman_document', 'path'), name='Documents_thumb10_unique_constraint_1'),
        ),
        migrations.AddConstraint(
            model_name='documents_thumb10',
            constraint=models.UniqueConstraint(condition=models.Q(lotsman_document=None), fields=('document', 'path'), name='Documents_thumb10_unique_constraint_2'),
        ),
        migrations.AddConstraint(
            model_name='documents_thumb10',
            constraint=models.UniqueConstraint(fields=('document', 'lotsman_document', 'path'), name='Documents_thumb10_unique_constraint_3'),
        ),
    ]
