# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-26 03:53
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0023_auto_20180116_0024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='search_details',
            name='date_pulled',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 1, 26, 3, 53, 30, 54475)),
        ),
    ]
