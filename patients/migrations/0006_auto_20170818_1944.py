# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-18 13:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0005_auto_20170818_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pulse_data',
            name='name',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='temp_data',
            name='name',
            field=models.TextField(max_length=100),
        ),
    ]
