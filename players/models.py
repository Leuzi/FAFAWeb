from django.db import models
from django_countries.fields import CountryField

class Player(models.Model):
	MALE = 'H'
	FEMALE = 'M'
	GENDERS = (
		(MALE, 'Hombre'),
		(FEMALE, 'Mujer')
	)
	
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
	Photo = models.ImageField(upload_to='.')
	LicenceId = models.CharField(max_length=25)
	Gender = models.CharField(
        max_length=1,
        choices=GENDERS
    )