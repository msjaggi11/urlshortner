# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-05-28 14:24
from __future__ import unicode_literals

from django.db import migrations, models
import shortener.validators


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0004_auto_20190527_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mehnurl',
            name='url',
            field=models.CharField(max_length=200, validators=[shortener.validators.validate_url, shortener.validators.validate_dot_com]),
        ),
    ]
