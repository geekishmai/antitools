# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-12 13:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import subject_sytem.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RelationStudentSubject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateField(verbose_name='上课日期')),
                ('create_time', models.DateTimeField(verbose_name='创建日期')),
            ],
            bases=(models.Model, subject_sytem.models.ModelMixin),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='姓名')),
            ],
            bases=(models.Model, subject_sytem.models.ModelMixin),
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='课程名称')),
            ],
            bases=(models.Model, subject_sytem.models.ModelMixin),
        ),
        migrations.CreateModel(
            name='SubjectTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField(verbose_name='上课时间')),
                ('end_time', models.TimeField(verbose_name='下课时间')),
            ],
            bases=(models.Model, subject_sytem.models.ModelMixin),
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='姓名')),
            ],
            bases=(models.Model, subject_sytem.models.ModelMixin),
        ),
        migrations.AddField(
            model_name='subject',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='subject_sytem.Teacher', verbose_name='教师姓名'),
        ),
        migrations.AddField(
            model_name='subject',
            name='time',
            field=models.ManyToManyField(to='subject_sytem.SubjectTime', verbose_name='上课时间'),
        ),
        migrations.AddField(
            model_name='relationstudentsubject',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subject_sytem.Student', verbose_name='学生姓名'),
        ),
        migrations.AddField(
            model_name='relationstudentsubject',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subject_sytem.Subject', verbose_name='课程名称'),
        ),
    ]