# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-03-16 23:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=10)),
                ('aadhar', models.CharField(max_length=12)),
            ],
        ),
    ]
