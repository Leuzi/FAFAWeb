from django.db import models
from colorful.fields import RGBColorField
from seasons.models import Season

class Team(models.Model):
	
	Name = models.CharField(max_length=50)
	Shortening = models.CharField(max_length=12)
	History = models.CharField(max_length= 4000,blank=True)
	City = models.CharField(max_length=25)
	CreationDate = models.DateField(blank=True)
	Slug = models.SlugField(max_length=50)
	WebSite = models.URLField(max_length=50,blank=True)
	Twitter = models.CharField(max_length=15,blank=True)
	Facebook = models.URLField(max_length=50,blank=True)
	Instagram = models.CharField(max_length=15,blank=True)
	Youtube = models.URLField(max_length=50,blank=True)
	Active = models.BooleanField(default=True)

	def __str__(self):
		return self.Name

	class Meta:
		ordering = ['Name']

class Stadium(models.Model):
	Name = models.CharField(max_length=50)
	City = models.CharField(max_length=35)
	Region = models.CharField(max_length=25)
	Map = models.URLField(max_length=50,blank=True)
	Address = models.CharField(max_length=25,blank=True)
	
	def __str__(self):
		return self.Name

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
	Team = models.ForeignKey(Team,related_name='uniform_of')	

	def __str__(self):
		return self.JerseyColor+'/'+self.PantsColor

class Logo(models.Model):
	image = models.ImageField()
	belongs_to = models.ForeignKey(Team)

	def __str__(self):
		return self.Team.name


class UniformSeason(models.Model):
	FirstUniform = models.ForeignKey(Uniform,related_name='firstUniform')
	SecondUniform = models.ForeignKey(Uniform,related_name='secondUniform',blank=True,null=True)
	Season = models.ForeignKey(Season)
	Team = models.ForeignKey(Team,related_name='equipment_of')	

class StadiumSeason(models.Model):
	PracticeField = models.ForeignKey(Stadium,related_name='practiceField')
	GameField = models.ForeignKey(Stadium,related_name='gameField')
	Season = models.ForeignKey(Season)
	Team = models.ForeignKey(Team,related_name='stadium_of')	

class LogoSeason(models.Model):
	Logo = models.ForeignKey(Logo)
	Season = models.ManyToManyField(Season)
	Team = models.ForeignKey(Team,related_name='logo_of')	







