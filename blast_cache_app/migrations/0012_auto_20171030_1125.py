# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-10-30 11:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blast_cache_app', '0011_auto_20171026_1551'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cache_entry',
            name='settings_hash',
        ),
        migrations.AddField(
            model_name='cache_entry',
            name='sequence',
            field=models.CharField(db_index=True, default='AAAAAAAAA', max_length=65536),
            preserve_default=False,
        ),
    ]
