# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-21 13:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employees',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('full_name', models.CharField(db_column='full_name', max_length=70)),
                ('first_name', models.CharField(db_column='first_name', max_length=25)),
                ('last_name', models.CharField(db_column='last_name', max_length=35)),
                ('adhesive', models.IntegerField(db_column='adhesive')),
            ],
        ),
    ]
