from managers import models
from FAFAWeb.constants import *

class RegionManager():

	@classmethods
	def getAllRegions(self):
		regions = models.Region.all()
		
		if regions == []:
			regions = None
			
		return regions
	
	def getRegionByShortname(self,shortname):
		
		return models.Region.objects.get(ShortRegionName=shortname)		