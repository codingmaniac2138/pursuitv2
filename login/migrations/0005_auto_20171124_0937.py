# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-24 09:37
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_auto_20171123_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='search_details',
            name='date_pulled',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 11, 24, 9, 37, 36, 531934)),
        ),
    ]