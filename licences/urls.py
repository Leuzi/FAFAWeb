from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^$', views.list,name='licenceList'),
	url(r'^new/(?P<regionId>(\d+))/$', views.new, name='newLicence'),
	url(r'^edit/(?P<licenceId>(\d+))/$', views.editLicence, name='editLicence')
]
