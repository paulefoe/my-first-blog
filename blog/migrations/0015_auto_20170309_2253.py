# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-09 20:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20170309_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='like',
            field=models.ManyToManyField(blank=True, default=0, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
    ]