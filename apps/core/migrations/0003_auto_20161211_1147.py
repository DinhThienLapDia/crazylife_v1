# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-12-11 04:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20161209_1331'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='action',
            name='likeby',
        ),
        migrations.RemoveField(
            model_name='action',
            name='listComment',
        ),
    ]