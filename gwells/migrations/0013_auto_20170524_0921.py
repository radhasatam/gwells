# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-24 16:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('gwells', '0012_auto_20170524_0902'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wellactivity',
            name='well_owner',
        ),
        migrations.AddField(
            model_name='wellactivity',
            name='effective_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AddField(
            model_name='wellactivity',
            name='expiry_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='wellowner',
            name='effective_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AddField(
            model_name='wellowner',
            name='expiry_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='wellowner',
            name='well_activity',
            field=models.ForeignKey(blank=True, db_column='gwells_well_activity_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='gwells.WellActivity'),
        ),
    ]