# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-18 11:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Data',
            new_name='Temp_Data',
        ),
    ]
