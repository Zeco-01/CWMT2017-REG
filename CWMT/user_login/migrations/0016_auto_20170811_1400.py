# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-11 14:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_login', '0015_auto_20170811_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='register_number',
            field=models.AutoField(max_length=20, primary_key=True, serialize=False, unique=True),
        ),
    ]
