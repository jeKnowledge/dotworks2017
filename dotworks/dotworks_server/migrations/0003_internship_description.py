# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-17 16:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dotworks_server', '0002_auto_20160317_1633'),
    ]

    operations = [
        migrations.AddField(
            model_name='internship',
            name='description',
            field=models.CharField(default='muito fixe', max_length=200),
            preserve_default=False,
        ),
    ]