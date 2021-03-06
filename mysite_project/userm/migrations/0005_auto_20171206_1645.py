# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-06 08:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userm', '0004_auto_20171206_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='body_text',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='mod_date',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='n_comments',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='n_pingbacks',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='pub_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='rating',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
