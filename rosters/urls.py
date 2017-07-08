from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
	url(r'^(?P<regionId>(\d+))/$', views.rosterListRegion, name='rosterListRegion'),
	url(r'^', views.rosterListTeam,name='rosterListTeam'),
]
