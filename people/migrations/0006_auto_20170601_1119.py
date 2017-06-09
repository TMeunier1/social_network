# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-01 09:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0005_auto_20170601_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.CharField(blank=True, max_length=85, null=True, verbose_name='Ville'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='interests',
            field=models.TextField(blank=True, max_length=50, null=True, verbose_name="Centre d'int\xe9r\xeat"),
        ),
        migrations.AlterField(
            model_name='profile',
            name='skills',
            field=models.TextField(blank=True, max_length=50, null=True, verbose_name='Comp\xe9tences'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='website',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Site Web'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='zipcode',
            field=models.IntegerField(blank=True, null=True, verbose_name='ZipCode'),
        ),
    ]
