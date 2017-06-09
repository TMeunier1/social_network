# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from PIL import Image
from django.db.models.signals import post_save
from django.dispatch import receiver
from taggit.managers import TaggableManager
from taggit.models import Tag

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    zipcode = models.IntegerField(null=True, blank=True, verbose_name = "ZipCode")
    city = models.CharField(null=True, blank=True, max_length=85, verbose_name = "Ville")
    website = models.CharField(null=True, blank=True, max_length=50, verbose_name = "Site Web")
    avatar = models.ImageField(null=True, blank=True, upload_to='upload',)
    skills = TaggableManager()
    interests = models.TextField(null=True, blank=True, max_length=50, verbose_name = "Centre d'intérêt")

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
     if created:
       Profile.objects.create(user=instance)
