# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-18 21:39
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dotworks_server', '0010_internship_questions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='internship',
            name='questions',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), default=['What do you do in your free time?', 'Why are you applying?'], size=None),
        ),
    ]
