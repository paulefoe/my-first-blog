# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-01 17:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='like_counter',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
