from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
	url(r'^$', views.showNews),
	url(r'^(?P<page>\d+)/(?P<items>\d+)/$', views.showNews),
	url(r'^(?P<slug>\w+)/$', views.showNew),
]
