# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.gis.db import models as geomodels
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from PIL import Image
from django.db.models.signals import post_save
from django.dispatch import receiver
from taggit.managers import TaggableManager
from taggit.models import Tag
from taggit.models import TaggedItemBase
from django.utils.translation import ugettext as _
from hvad.models import TranslatableModel, TranslatedFields


class Taggedtags(TaggedItemBase):
    content_object = models.ForeignKey('Profile')


class Profile(TranslatableModel, geomodels.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    zipcode = models.IntegerField(null=True, blank=True, verbose_name = _("ZipCode"))
    city = models.CharField(null=True, blank=True, max_length=85, verbose_name = _("City"))
    website = models.CharField(null=True, blank=True, max_length=50, verbose_name = _("Website"))
    avatar = models.ImageField(null=True, blank=True, upload_to='upload', verbose_name = _("avatar"))
    skills = TaggableManager(related_name='profile_skills', verbose_name=_('Skills'))
    interests = TaggableManager(through=Taggedtags, related_name='profile_interests', verbose_name=_("Interests"))
    point = geomodels.PointField(null=True)
    translations = TranslatedFields(
        bio = models.TextField(verbose_name=_("Biography"))
    )
