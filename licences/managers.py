from . import models
from FAFAWeb.constants import *
from .dto import LicenceDto

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
		else:
			result = models.Licence.objects.filter(Type__Region=filter)
		licences = {}
		
		for licence in result:
			licences[licence.Type.Region.RegionName] = []
		
		for licence in result:
			dto = LicenceDto(licence).getDto()
						
			licences[licence.Type.Region.RegionName].append(dto)
		
		return licences
	

	@classmethod
	def getLicenceById(self, licenceId):
		
		licence = models.Licence.objects.get(id=licenceId)

		return licence
