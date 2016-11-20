from django.db import models

# Create your models here.

class Template(models.Model):
	name = models.CharField(max_length=25)

	def __str__(self):
		return self.name

class New(models.Model):
	Header = models.CharField(max_length=25)
	SubHeader = models.CharField(max_length=50)
	Body = models.CharField(max_length=5000)
	Date = models.DateTimeField(auto_now=True)
	Likes = models.PositiveSmallIntegerField(default=0)
	Facebook = models.PositiveSmallIntegerField(default=0)
	Pinterest = models.PositiveSmallIntegerField(default=0)
	GooglePlus = models.PositiveSmallIntegerField(default=0)
	Slug = models.SlugField(max_length=50)
	Template = models.ForeignKey(Template, blank=True, null=True)

	def __str__(self):
		return self.Header+'('+str(self.Date)+')'


	class Meta:
		ordering = ['Date']
		

