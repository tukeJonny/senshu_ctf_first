# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-28 08:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoreserver', '0013_auto_20160628_0929'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='problem_url',
            new_name='url',
        ),
    ]