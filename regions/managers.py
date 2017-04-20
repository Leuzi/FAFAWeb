from models import Region
from FAFAWeb.constants import *
from django.contrib.auth import authenticate

class RegionManager():

	@classmethod
	def getResponsible(self,user,password):
		user = authenticate(username=user, password=password)
		
		responsible = None		
		if user is not None:
			try:
				responsible = Region.objects.get(User=user)
			except:
				responsible = None
		return responsible

		
	@classmethod
	def getAllRegions(self):
		regions = models.Region.all()
		
		if regions == []:
			regions = None
			
		return regions
	
	def getRegionByShortname(self,shortname):
		
		return models.Region.objects.get(ShortRegionName=shortname)
