# Generated by Django 3.0.3 on 2020-02-08 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ckk', '0202_auto_20200208_1406'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='locations_users',
            unique_together=set(),
        ),
        migrations.AddConstraint(
            model_name='locations_users',
            constraint=models.UniqueConstraint(condition=models.Q(parent=None), fields=('location', 'user'), name='Locations_users_unique_constraint_0'),
        ),
        migrations.AddConstraint(
            model_name='locations_users',
            constraint=models.UniqueConstraint(fields=('location', 'parent', 'user'), name='Locations_users_unique_constraint_1'),
        ),
    ]
