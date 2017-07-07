from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^$', views.list,name='competitionList'),
	url(r'^new/(?P<regionId>(\d+))/$', views.new, name='newCompetition'),
	url(r'^edit/(?P<competitionId>(\d+))/$', views.editCompetition, name='editCompetition'),
	url(r'^manage/(?P<competitionId>(\d+))/$', views.manageCompetition, name='manageCompetition'),
]
