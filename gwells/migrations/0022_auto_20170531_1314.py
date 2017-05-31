# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-31 20:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gwells', '0021_auto_20170531_0946'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activitysubmission',
            name='driller_responsible',
        ),
        migrations.RemoveField(
            model_name='activitysubmission',
            name='intended_water_use',
        ),
        migrations.RemoveField(
            model_name='activitysubmission',
            name='legal_land_district',
        ),
        migrations.RemoveField(
            model_name='activitysubmission',
            name='owner_province_state',
        ),
        migrations.RemoveField(
            model_name='activitysubmission',
            name='well',
        ),
        migrations.RemoveField(
            model_name='activitysubmission',
            name='well_activity_type',
        ),
        migrations.RemoveField(
            model_name='activitysubmission',
            name='well_class',
        ),
        migrations.RemoveField(
            model_name='activitysubmission',
            name='well_subclass',
        ),
        migrations.RemoveField(
            model_name='activitysubmission',
            name='well_yield_unit',
        ),
        migrations.RemoveField(
            model_name='driller',
            name='drilling_company',
        ),
        migrations.RemoveField(
            model_name='ltsaowner',
            name='province_state',
        ),
        migrations.RemoveField(
            model_name='ltsaowner',
            name='well',
        ),
        migrations.RemoveField(
            model_name='well',
            name='intended_water_use',
        ),
        migrations.RemoveField(
            model_name='well',
            name='legal_land_district',
        ),
        migrations.RemoveField(
            model_name='well',
            name='owner_province_state',
        ),
        migrations.RemoveField(
            model_name='well',
            name='well_class',
        ),
        migrations.RemoveField(
            model_name='well',
            name='well_subclass',
        ),
        migrations.RemoveField(
            model_name='well',
            name='well_yield_unit',
        ),
        migrations.RemoveField(
            model_name='wellsubclass',
            name='well_class',
        ),
    ]
