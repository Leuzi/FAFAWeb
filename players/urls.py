from django.conf.urls import include, url
from . import views


urlpatterns = [
	url(r'^$', views.listTeam,name='playerListTeam'),
	url(r'^(?P<regionId>(\d+))/$', views.listRegion, name='playerListRegion'),
	url(r'^(?P<playerId>(\d+))/edit', views.editPlayer, name='editPlayer'),
	url(r'^new$', views.new, name='newPlayer'),
]
