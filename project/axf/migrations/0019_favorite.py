# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2020-06-23 03:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('axf', '0018_auto_20200623_0941'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userAccount', models.CharField(max_length=20)),
                ('productid', models.CharField(max_length=10)),
            ],
        ),
    ]
