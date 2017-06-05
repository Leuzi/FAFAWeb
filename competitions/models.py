from django.db import models
from regions.models import Region
from teams.models import Team

class CompetitionType(models.Model):
	Name = models.CharField(max_length=45)
	Shortening = models.CharField(max_length=5)
	Region = models.ForeignKey(Region)
	
class CompetitionConditions(models.Model):
	Edition = models.CharField(max_length=10)
	Years = models.CharField(max_length=9)
	StartDate = models.DateField()
	EndDate = models.DateField()
	MinimumBirthDate = models.DateField()
	MaximumBirthDate = models.DateField()
	
class Competition(models.Model):
	Type = models.ForeignKey(CompetitionType)
	Conditions = models.ForeignKey(CompetitionConditions)
	Teams = models.ManyToManyField(Team)
	Active = models.BooleanField(default=False)