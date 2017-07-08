from django.conf.urls import include, url
from . import views


urlpatterns = [
	url(r'^$', views.listTeam,name='playerListTeam'),
	url(r'^(?P<regionId>(\d+))/$', views.listRegion, name='playerListRegion'),
	url(r'^new$', views.new, name='newPlayer'),
]
