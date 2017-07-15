from . import models
from FAFAWeb.constants import *
from .dto import LicenceDto
from regions.managers import RegionManager
from datetime import datetime, timedelta, time

class LicenceManager():
	
	@classmethod 
	def getLicencesForUser(self, user):
		if user.National:
			return self.getAllLicences()
		else:
			return self.getLicencesForRegion(user)

	@classmethod
	def getAllLicences(self):
		return LicenceManager.getLicences()
		
	@classmethod
	def getLicencesForRegion(self,Region):
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
		print(licences)
		return licences
	

	@classmethod
	def getLicenceById(self, licenceId):
		
		return models.Licence.objects.get(id=licenceId)

	@classmethod
	def getLicenceSessionById(self, sessionId):
		return models.LicenceDuration.objects.get(id=sessionId)

	@classmethod
	def getActivePlayers(self, team):	
		today = datetime.now().date()		

		return models.ValidFor.objects.filter(Team=team).filter(Licence__StartDate__lte=today,Licence__EndDate__gte=today)

	@classmethod
	def getLicencesForTeam(self, team):
		return models.ValidFor.objects.filter(Team=team)


	@classmethod
	def getPlayersWithValidLicences(self, team, validLicences):
		
		return models.ValidFor.objects.filter(Team=team, Licence__in=validLicences)

		
