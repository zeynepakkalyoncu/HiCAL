# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-06-22 19:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('progress', '0018_auto_20171027_1344'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='setting',
        ),
        migrations.DeleteModel(
            name='TaskSetting',
        ),
    ]