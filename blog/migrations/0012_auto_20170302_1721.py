# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-02 15:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20170302_1706'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='like',
            name='user',
        ),
        migrations.AddField(
            model_name='comment',
            name='likes',
            field=models.IntegerField(default=0, verbose_name='like'),
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]