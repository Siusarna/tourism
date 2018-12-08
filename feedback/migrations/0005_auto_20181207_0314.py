# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-07 01:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0004_remove_contact_how_much'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='second_name',
        ),
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(max_length=1000, verbose_name='Вкажіть свої побажання на рахунок путівки'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=30, verbose_name="Ім'я та Прізвище"),
        ),
    ]
