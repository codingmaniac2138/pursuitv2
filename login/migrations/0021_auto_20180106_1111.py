# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-06 11:11
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0020_auto_20180106_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='search_details',
            name='date_pulled',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 1, 6, 11, 11, 0, 518991)),
        ),
    ]