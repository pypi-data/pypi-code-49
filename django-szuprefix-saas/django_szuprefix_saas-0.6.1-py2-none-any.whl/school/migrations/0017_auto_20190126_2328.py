# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-01-26 15:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_auto_20180822_2359'),
        ('school', '0016_auto_20190115_1628'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClazzCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),

        migrations.AddField(
            model_name='clazzcourse',
            name='clazz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clazz_course_relations', to='school.Clazz'),
        ),
        migrations.AddField(
            model_name='clazzcourse',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clazz_course_relations', to='course.Course'),
        ),
        migrations.AddField(
            model_name='clazzcourse',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='clazz_course_relations', to='school.Teacher'),
        ),
        # migrations.RunSQL("insert into school_clazzcourse(id,clazz_id,course_id) select * from school_clazz_courses"),
        migrations.AddField(
            model_name='teacher',
            name='classes',
            field=models.ManyToManyField(blank=True, related_name='teachers', through='school.ClazzCourse', to='school.Clazz', verbose_name='\u73ed\u7ea7'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='courses',
            field=models.ManyToManyField(blank=True, related_name='school_teachers', through='school.ClazzCourse', to='course.Course', verbose_name='\u8bfe\u7a0b'),
        ),
    ]
