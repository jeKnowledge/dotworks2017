# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-19 19:04
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dotworks_server', '0014_auto_20161019_1857'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inscription',
            name='questions',
        ),
        migrations.AlterField(
            model_name='inscription',
            name='answers',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), default=['', ''], size=2),
        ),
    ]
