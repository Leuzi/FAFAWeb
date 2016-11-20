from django.db import models
from colorful.fields import RGBColorField

# Create your models here.

class Uniform(models.Model):
	JerseyColor = models.CharField(max_length=25)
	JerseyColorRGB = RGBColorField()
	PantsColor = models.CharField(max_length=25)
	PantsColorRGB = RGBColorField()
	HelmetColor = models.CharField(max_length=25)
	HelmetColorRGB = RGBColorField()
	FaceMaskColor = models.CharField(max_length=25)
	FaceMaskColorRGB = RGBColorField()
	SocksColor = models.CharField(max_length=25)
	SocksColorRGB = RGBColorField()

class Equipment(models.Model):
	FirstUniform = models.ForeignKey(Uniform,related_name='firstUniform')
	SecondUniform = models.ForeignKey(Uniform,related_name='secondUniform')
	Season = models.DateField()



class Stadium(models.Model):
	Name = models.CharField(max_length=25)
	City = models.CharField(max_length=25)
	Location = models.URLField(max_length=50)
	Address = models.CharField(max_length=25)
	
	def __str__(self):
		return self.Name

class Field(models.Model):
	Field = models.ForeignKey(Stadium)
	Season = models.DateField()
	
	def __str__(self):
		return self.Field.Name

class Team(models.Model):
	
	Name = models.CharField(max_length=25)
	City = models.CharField(max_length=25)
	CreationDate = models.DateField()
	Slug = models.SlugField(max_length=50)
	Equipments = models.ManyToManyField(Equipment)
	PracticeFields = models.ManyToManyField(Field,related_name='practiceFields')
	GameFields = models.ManyToManyField(Field,related_name='gameFields')

	def __str__(self):
		return self.Name

	class Meta:
		ordering = ['Name']







