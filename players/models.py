from django.db import models

# Create your models here.

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

class LicenceId(models.Model):
	LicenceId = models.CharField(max_length=25)
	Player = models.ForeignKey(Player)
