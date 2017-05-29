# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from autoslug import AutoSlugField
from PIL import Image

class Profile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    slug = AutoSlugField(populate_from='username', unique_with="username")
    zipcode = models.IntegerField(verbose_name = "ZipCode")
    city = models.CharField(max_length=85, verbose_name = "Ville")
    website = models.CharField(max_length=50, verbose_name = "Site Web")
    avatar = models.ImageField(upload_to='upload', null=True, blank=True)
    skills = models.TextField(max_length=50, verbose_name = "Compétences")
    interests = models.TextField(max_length=50, verbose_name = "Centre d'intérêt")
