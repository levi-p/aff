# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-07-04 12:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0003_home_page_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='place_details',
            name='Discription',
            field=models.TextField(blank=True),
        ),
    ]
