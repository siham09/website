# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-18 10:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticker', models.CharField(max_length=50)),
                ('initial', models.FloatField()),
                ('latest', models.FloatField()),
                ('times', models.IntegerField()),
            ],
        ),
    ]