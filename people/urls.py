from django.conf.urls import url, include
from django.conf.urls.i18n import i18n_patterns
from .views import *

urlpatterns = [
    url(r'^list/$', ProfileListView.as_view(), name='list'),
    url(r'^map/$', ProfileMapView.as_view(), name='map'),
    url(r'^(?P<slug>[\w-]+)/$', ProfileDetailView.as_view(), name='profile-detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', ProfileUpdateView.as_view(), name='profile-edit'),
]
