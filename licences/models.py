from django.db import models
from django_countries.fields import CountryField
from seasons.models import Season
from teams.models import Team
from regions.models import Region
from players.models import Player

class LicenceType(models.Model):
	
	Name = models.CharField(max_length=50)
	Active = models.BooleanField(default=True)
	Shortening = models.CharField(max_length=4)
	Region = models.ForeignKey(Region)
	
class States(models.Model):
	Name = models.CharField(max_length=20)
	Shortening = models.CharField(max_length=6)
	
class LicenceDuration(models.Model):
	StartDate = models.DateField()
	EndDate = models.DateField()
	Price = models.DecimalField(max_digits=5,decimal_places=2)
	
class LicenceSesion(models.Model):
	Licence = models.ForeignKey(LicenceType)
	Duration = models.ForeignKey(LicenceDuration)
	
class ValidFor(models.Model):
	Player = models.ForeignKey(Player)
	Licence = models.ForeignKey(LicenceSesion)
	Team = models.ForeignKey(Team)
	State = models.ForeignKey(States)
