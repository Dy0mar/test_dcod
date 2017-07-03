# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-23 12:21
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=255)),
                ('value', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region_name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='place',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_parser.Region'),
        ),
    ]
