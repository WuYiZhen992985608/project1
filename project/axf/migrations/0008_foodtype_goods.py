# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2020-06-17 15:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('axf', '0007_auto_20200617_1935'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeid', models.CharField(max_length=10)),
                ('typename', models.CharField(max_length=20)),
                ('typesort', models.IntegerField()),
                ('childtypenames', models.CharField(max_length=150)),
            ],
        ),

    ]
