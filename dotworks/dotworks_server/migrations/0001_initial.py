# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-23 22:23
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('e_mail', models.EmailField(max_length=254, unique=True)),
                ('description', models.TextField(max_length=500)),
                ('website', models.URLField(blank=True, max_length=100)),
                ('facebook', models.URLField(blank=True, max_length=100)),
                ('phone_number', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'.Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Inscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curriculum', models.FileField(upload_to='curriculums/')),
            ],
        ),
        migrations.CreateModel(
            name='Internship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('CUR', 'Curricular'), ('PRO', 'Profissional'), ('VER', 'Verao')], max_length=20)),
                ('description', models.CharField(max_length=200)),
                ('area', models.CharField(max_length=50)),
                ('beginning_date', models.DateField(blank=True, verbose_name='Beggining date')),
                ('duration', models.PositiveSmallIntegerField(choices=[(1, '1 mês'), (2, '2 meses'), (3, '3 meses'), (4, '4 meses'), (5, '5 meses'), (6, '6 meses'), (7, '7 meses'), (8, '8 meses'), (9, '9 meses'), (10, '10 meses'), (11, '11 meses'), (12, '12 meses')])),
                ('working_time', models.CharField(choices=[('P_T', 'Part time'), ('F_T', 'Full time')], max_length=15)),
                ('application_deadline', models.DateField(verbose_name='aplications deadline')),
                ('payment', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=100)),
                ('n_positions', models.SmallIntegerField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dotworks_server.Company')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('e_mail', models.EmailField(max_length=254, unique=True)),
                ('description', models.TextField(max_length=500)),
                ('github', models.URLField(blank=True, max_length=100)),
                ('linkedin', models.URLField(blank=True, max_length=100)),
                ('facebook', models.URLField(blank=True, max_length=100)),
                ('phone_number', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'.Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('name', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('birth_date', models.DateField()),
                ('degree', models.CharField(choices=[('SECUNDARIO', 'Secundario'), ('LICENCIATURA', 'Licenciatura'), ('MESTRADO', 'Mestrado'), ('DOUTORAMENTO', 'Doutoramento')], max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='inscription',
            name='internship',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dotworks_server.Internship'),
        ),
        migrations.AddField(
            model_name='inscription',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dotworks_server.Student'),
        ),
    ]
