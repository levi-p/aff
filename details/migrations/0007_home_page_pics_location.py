# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-08-14 16:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0006_auto_20160808_1530'),
    ]

    operations = [
        migrations.AddField(
            model_name='home_page_pics',
            name='Location',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
