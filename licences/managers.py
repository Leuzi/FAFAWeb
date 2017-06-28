from . import models
from FAFAWeb.constants import *
from .dto import LicenceDto
from regions.managers import RegionManager

class LicenceManager():
	
	@classmethod
	def getAllLicences(self):
		return LicenceManager.getLicences()
		
	@classmethod
	def getLicenceRegion(self,Region):
		return LicenceManager.getLicences(Region)
		
	@classmethod
	def getLicences(self, filter=None):

		if filter is None:
			result = models.Licence.objects.all()
			regions = RegionManager.getAllRegions()
		else:
			result = models.Licence.objects.filter(Type__Region=filter)
			regions = [filter]

		licences = {}
		
		for region in regions:
			licences[region] = []
		
		for licence in result:
			dto = LicenceDto(licence).getDto()
						
			licences[licence.Type.Region].append(dto)
		
		return licences
	

	@classmethod
	def getLicenceById(self, licenceId):
		
		licence = models.Licence.objects.get(id=licenceId)

		return licence
