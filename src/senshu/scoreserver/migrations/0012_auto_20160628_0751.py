# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-27 22:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoreserver', '0011_auto_20160628_0211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flag',
            name='flag',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]