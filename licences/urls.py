from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^$', views.list,name='licenceList'),
	url(r'^new$', views.new, name='newLicence'),
	url(r'^edit/(?P<id>(\d+)/)?$', views.editLicence, name='editLicence')
]