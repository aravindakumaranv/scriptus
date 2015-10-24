# -*- coding: utf-8 -*-
# Generated by Django 1.10.dev20151014033929 on 2015-10-19 10:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=16)),
                ('n_blogs', models.IntegerField()),
            ],
        ),
    ]
