# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-05 02:34
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0012_auto_20180104_0903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='search_details',
            name='date_pulled',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 1, 5, 2, 34, 58, 696803)),
        ),
    ]