# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-21 18:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('threads', '0002_auto_20171121_1751'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Forum',
            new_name='Thread',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='threads',
            new_name='thread',
        ),
    ]
