# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-11-13 11:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blast_cache_app', '0012_auto_20171030_1125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cache_entry',
            name='file_type',
            field=models.IntegerField(choices=[(1, 'pssm'), (2, 'mtx')], default=2),
        ),
    ]
