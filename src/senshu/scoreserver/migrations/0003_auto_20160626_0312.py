# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-25 18:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoreserver', '0002_delete_notice'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ('-points',)},
        ),
        migrations.AddField(
            model_name='user',
            name='points',
            field=models.IntegerField(default=0),
        ),
    ]
