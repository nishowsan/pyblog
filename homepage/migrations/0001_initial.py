# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-03 16:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=600)),
                ('body', models.CharField(max_length=1000000)),
                ('picture', models.FileField(upload_to='')),
            ],
        ),
    ]
