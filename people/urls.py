from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'^list/$', ProfileListView.as_view(), name='list'),
    url(r'^(?P<slug>[\w-]+)/$', ProfileDetailView.as_view(), name='profile-detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', ProfileUpdateView.as_view(), name='profile-edit'),
]
