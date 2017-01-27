from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Region(models.Model):
	
	RegionName = models.CharField(max_length=50)
	ShortRegionName = models.CharField(max_length=3)
	FederationName = models.CharField(max_length=50)
	ShortFederationName = models.CharField(max_length=6)
	Flag = models.ImageField(blank=True)
	FederationLogo = models.ImageField(blank=True)
	User = models.OneToOneField(User)