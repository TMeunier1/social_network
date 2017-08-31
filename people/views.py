# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import *
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.http import JsonResponse

def homepage(request):
    return render(request, "homepage.html")

def profile(request, slug):
    profile = Profile.objects.get(user__username = slug)
    context = {'profile' : profile}
    return render(request, "profile.html")

class ProfileListView(ListView):
    model = Profile
    context_object_name = "profile_list"
    def get_data(self, context):
        data = {
            'profile' : []
        }
        for profiles in context["profile_list"]:
            if profiles.point:
                profile_data = {
                    'username' : profiles.user.username,
                    'lat' : profiles.point.y,
                    'long' : profiles.point.x,
                    'zipcode' : profiles.zipcode,
                }
                data['profile'].append(profile_data)
        return data
    def render_to_response(self, context, **response_kwargs):
        if self.request.is_ajax():
            return JsonResponse(
                self.get_data(context),
                **response_kwargs
            )
        return ListView.render_to_response(self, context, **response_kwargs)

class ProfileDetailView(DetailView):
    model = Profile
    slug_field = "user__username"

class ProfileUpdateView(UpdateView):
    model = Profile
    fields = ['city', 'zipcode', 'website', 'skills', 'interests']
    slug_field = "user__username"
    success_url='/profil/list'

class ProfileMapView(ListView):
    model = Profile
    template_name = "people/profile_map.html"
    context_object_name = "profile"
