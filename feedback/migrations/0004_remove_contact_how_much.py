# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-07 01:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0003_auto_20181206_1930'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='how_much',
        ),
    ]
