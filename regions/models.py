from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Region(models.Model):
	
	RegionName = models.CharField(max_length=50)
	ShortRegionName = models.CharField(max_length=3)
	FederationName = models.CharField(max_length=50)
	ShortFederationName = models.CharField(max_length=6)
	Flag = models.ImageField(blank=True,upload_to='.')
	FederationLogo = models.ImageField(blank=True, upload_to='.')
	User = models.OneToOneField(User)
	National = models.BooleanField(default=False)

	def __str__ (self):
		return self.RegionName + '(login:' + self.User.username+ ')'

	def class_name(self):
		return self.__class__.__name__
