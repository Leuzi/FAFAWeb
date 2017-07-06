from django.db import models
from regions.models import Region
from teams.models import Team
from licences.models import Licence

class CompetitionType(models.Model):
	Name = models.CharField(max_length=45)
	Shortening = models.CharField(max_length=5)
	Region = models.ForeignKey(Region)
	
	def __str__(self):
		return self.Name
	
class CompetitionConditions(models.Model):
	Edition = models.CharField(max_length=10)
	StartDate = models.DateField()
	EndDate = models.DateField()
	MinimumBirthDate = models.DateField()
	MaximumBirthDate = models.DateField()
	GENDER_CHOICES = (
		('H', 'Hombre'),
		('M', 'Mujer'),
		('O', 'Open')
	)
	
	Gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='O')
	
class Competition(models.Model):
	Type = models.ForeignKey(CompetitionType)
	Conditions = models.ForeignKey(CompetitionConditions)
	Teams = models.ManyToManyField(Team)
	Licences = models.ManyToManyField(Licence)
	Active = models.BooleanField(default=False)