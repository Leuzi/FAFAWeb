from . import models
from FAFAWeb.constants import *
from .dto import LicenceDto

class LicenceManager():
	@classmethod
	def getAllLicences(self):
		licences = {}
		result = models.Licence.objects.all()
		
		for licence in result:
			licences[licence.Type.Region.RegionName] = []
		
		for licence in result:
			dto = LicenceDto(licence).getDto()
						
			licences[licence.Type.Region.RegionName].append(dto)
		
		return licences
		
	def getValidLicenses(self):
		pass