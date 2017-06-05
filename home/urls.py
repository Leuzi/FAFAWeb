from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
	url(r'^logout', views.loginout, name='logout'),
	url(r'^', views.home),
]