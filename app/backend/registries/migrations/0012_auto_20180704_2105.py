# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-04 21:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registries', '0011_auto_20180619_2315'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactinfo',
            name='person',
        ),
        migrations.DeleteModel(
            name='ContactInfo',
        ),
    ]
