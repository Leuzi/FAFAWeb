from django.db import models

# Create your models here.

class Season(models.Model):
	Name = models.CharField(max_length=9)
	Shortening = models.CharField(max_length=5)
	StartDate = models.DateTimeField()
	EndDate = models.DateTimeField()

	def __str__(self):
		return self.Name;
