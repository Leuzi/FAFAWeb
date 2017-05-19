from django.conf.urls import include, url
from . import views


urlpatterns = [
	url(r'^$', views.list,name='playerList'),
	url(r'^new$', views.new, name='newPlayer')
]