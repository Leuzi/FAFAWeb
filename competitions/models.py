from django.db import models
from regions.models import Region
from teams.models import Team
from licences.models import Licence

class CompetitionType(models.Model):
	Name = models.CharField(max_length=45)
	Shortening = models.CharField(max_length=5)
	Region = models.ForeignKey(Region)
		
	class Meta:
		unique_together = ('Shortening', 'Region')
	
	def __str__(self):
		return self.Name
	
class CompetitionConditions(models.Model):
	
	StartDate = models.DateField()
	EndDate = models.DateField()
	MinimumBirthDate = models.DateField()
	MaximumBirthDate = models.DateField(null=True, blank=True)
	GENDER_CHOICES = (
		('H', 'Hombre'),
		('M', 'Mujer'),
		('O', 'Open')
	)
	
	Gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='O')

class Edition(models.Model):
	Edition = models.CharField(max_length=10)
	Conditions = models.ForeignKey(CompetitionConditions)
	Teams = models.ManyToManyField(Team)
	Licences = models.ManyToManyField(Licence)	
	Competition = models.ForeignKey(CompetitionType)
	Active = models.BooleanField(default=False)

	class Meta:
		unique_together = ('Edition', 'Competition')


	

