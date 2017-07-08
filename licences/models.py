# -*- coding: latin-1 -*-
from django.db import models
from django_countries.fields import CountryField
from seasons.models import Season
from teams.models import Team
from regions.models import Region
from players.models import Player

class LicenceType(models.Model):	
	Name = models.CharField(max_length=50)
	Shortening = models.CharField(max_length=4)
	Region = models.ForeignKey(Region)
	GENDER_CHOICES = (
		('H', 'Hombre'),
		('M', 'Mujer'),
		('O', 'Open')
	)
	
	Gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='O')
	
	def __str__ (self):
		return self.Name + '(Región:' + self.Region.RegionName+ ')'
	
class LicenceState(models.Model):
	Name = models.CharField(max_length=20)
	Shortening = models.CharField(max_length=6)
	
	def __str__ (self):
		return self.Name + '(' + self.Shortening+ ')'

class LicenceDuration(models.Model):
	StartDate = models.DateField()
	EndDate = models.DateField()
	Price = models.DecimalField(max_digits=5,decimal_places=2)
	MinimumBirthDate = models.DateField(null=True)
	MaximumBirthDate = models.DateField(null=True, blank=True)
	
	def __str__ (self):
		return  'Desde: '+ str(self.StartDate) + ' Hasta:' + str(self.EndDate) +'(' + str(self.Price) + '€)'
	
class Licence(models.Model):
	Type = models.ForeignKey(LicenceType)
	Session= models.ForeignKey(LicenceDuration)	
	Active = models.BooleanField(default=True)
	
	def __str__ (self):
		return str(self.Type) + '(' + str(self.Session)+ ')'
	
class ValidFor(models.Model):
	Player = models.ForeignKey(Player)
	Licence = models.ForeignKey(Licence)
	Team = models.ForeignKey(Team)
	
class LicenceHistory(models.Model):
	State = models.ForeignKey(LicenceState)
	Date = models.DateTimeField()
	Player = models.ForeignKey(ValidFor)
