# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-07-09 20:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20180708_2342'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobopportunity',
            name='availability',
            field=models.BooleanField(default=True),
        ),
    ]
