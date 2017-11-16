# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-14 11:23
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20171114_1736'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='pub_time',
            field=models.TimeField(default='00:00:00'),
        ),
        migrations.AlterField(
            model_name='choice',
            name='cho_date',
            field=models.DateField(default=datetime.datetime(2017, 11, 14, 11, 23, 8, 471000, tzinfo=utc), verbose_name='date choice'),
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2017, 11, 14, 11, 23, 8, 451000, tzinfo=utc), verbose_name='date published'),
        ),
    ]
