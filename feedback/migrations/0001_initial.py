# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-02 17:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Имя')),
                ('second_name', models.CharField(max_length=30, verbose_name='Фамилия')),
                ('email', models.EmailField(max_length=70)),
                ('message', models.TextField(max_length=1000, verbose_name='Сообщение')),
                ('data', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата отправки')),
            ],
            options={
                'db_table': 'contact',
                'verbose_name': 'Обратная связь',
                'verbose_name_plural': 'Обратная связь',
            },
        ),
    ]
