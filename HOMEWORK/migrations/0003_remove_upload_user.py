# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-02-26 07:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HOMEWORK', '0002_auto_20180226_0657'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='upload',
            name='user',
        ),
    ]
