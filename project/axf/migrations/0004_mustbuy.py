# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2020-06-16 13:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('axf', '0003_nav'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mustbuy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=150)),
                ('name', models.CharField(max_length=20)),
                ('track', models.CharField(max_length=20)),
            ],
        ),
    ]
