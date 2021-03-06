# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2020-08-07 19:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trash',
            name='content_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='contenttypes.ContentType'),
        ),
        migrations.AlterField(
            model_name='versionhistory',
            name='content_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='contenttypes.ContentType'),
        ),
        migrations.AlterField(
            model_name='versionhistory',
            name='object_id',
            field=models.PositiveIntegerField(verbose_name='\u5bf9\u8c61ID'),
        ),
        migrations.AlterField(
            model_name='versionhistory',
            name='version',
            field=models.PositiveIntegerField(verbose_name='\u7248\u672c'),
        ),
    ]
