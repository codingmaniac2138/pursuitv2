# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-06 11:13
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0010_auto_20180106_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='amount',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='sale',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 6, 11, 13, 48, 42159)),
        ),
        migrations.AlterField(
            model_name='sale',
            name='emails_balance_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='sale',
            name='emails_count',
            field=models.IntegerField(default=0),
        ),
    ]
