# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-20 12:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_login', '0016_auto_20170811_1400'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='invoice_bank',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='invoice_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='invoice_tel',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='invoice_type',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
