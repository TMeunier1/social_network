# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-29 13:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0003_auto_20170529_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='zipcode',
            field=models.IntegerField(verbose_name='ZipCode'),
        ),
    ]
