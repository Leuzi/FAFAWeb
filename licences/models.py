from django.db import models
from django_countries.fields import CountryField
from seasons.models import Season
from teams.models import Team

class Player(models.Model):
	
	DNI = models.CharField(max_length=12)
	Name = models.CharField(max_length=50)
	Surname = models.CharField(max_length=50)
	BirthDate = models.DateField()
	Country = CountryField()
	ZIPCode = models.CharField(max_length=7)
	City = models.CharField(max_length=20)
	Region = models.CharField(max_length=20)
	Phone = models.CharField(max_length=20)
	Mail = models.EmailField()
	Photo = models.ImageField()

class LicenceType(models.Model):
	
	Name = models.CharField(max_length=50)
	Price = models.DecimalField(max_digits=5,decimal_places=2)
	Active = models.BooleanField(default=True)
	
class State(models.Model):
	Name = models.CharField(max_length=50)
	Shortening = models.CharField(max_length=12)
	Active = models.BooleanField(default=True)
	
class ValidFor(models.Model):
	Player = models.ForeignKey(Player)
	Season = models.ForeignKey(Season)
	Team = models.ForeignKey(Team)
	State = models.ForeignKey(State)
