# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-12-15 04:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20161215_1011'),
    ]

    operations = [
        migrations.AddField(
            model_name='action',
            name='isverified',
            field=models.BooleanField(default=False, verbose_name=b'isverified'),
        ),
    ]
