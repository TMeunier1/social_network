# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import *
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView

def homepage(request):
    return render(request, "homepage.html")

def profile(request, slug):
    profile = Profile.objects.get(user__username = slug)
    context = {'profile' : profile}
    return render(request, "profile.html")

class ProfileListView(ListView):
    model = Profile
    context_object_name = "profile_list"

class ProfileDetailView(DetailView):
    model = Profile
    slug_field = "user__username"

class ProfileUpdateView(UpdateView):
    model = Profile
    fields = ['city', 'zipcode', 'website', 'skills', 'interests']
    slug_field = "user__username"
    success_url='/profil/list'
