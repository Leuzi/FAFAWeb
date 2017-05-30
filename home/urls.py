from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
	url(r'^', views.home),
	url(r'^log_out/$', views.log_out, name='log_out'),
]