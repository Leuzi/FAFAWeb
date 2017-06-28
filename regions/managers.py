from regions.models import Region
from FAFAWeb.constants import *
from django.contrib.auth import authenticate
from regions.dto import RegionDto

class RegionManager():

	@classmethod
	def getRegionDto(self,region):
		return RegionDto(region)

	@classmethod
	def getUserForRegion(self,user):
		try:
			userRegion = Region.objects.get(User=user)
		except:
			userRegion = None
			
		return userRegion

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
		regions = Region.objects.all()
		
		if regions == []:
			regions = None
			
		return regions


	@classmethod
	def getRegionById(self, regionId):
		regions = Region.objects.get(id=regionId)
		
		if regions == []:
			regions = None
			
		return regions
	
