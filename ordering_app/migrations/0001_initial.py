# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-19 21:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buy', models.CharField(max_length=25)),
                ('customer', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('byn', models.CharField(default=0, max_length=8)),
                ('byr', models.CharField(default=0, max_length=8)),
                ('comment', models.CharField(max_length=50)),
            ],
        ),
    ]
