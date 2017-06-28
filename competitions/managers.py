from . import models
from FAFAWeb.constants import *
from .dto import CompetitionDto
from regions.managers import RegionManager

class CompetitionManager():

	@classmethod
	def getAllCompetitions(self):
		return CompetitionManager.getCompetitions()
	
	@classmethod
	def getCompetitionsRegion(self,Region):
		return CompetitionManager.getCompetitions(Region)

	@classmethod
	def getCompetitions(self, filter=None):
		
		if filter is None:
			result = models.Competition.objects.all()
			regions = RegionManager.getAllRegions()
		else:
			result = models.Competition.objects.filter(Type__Region=filter)
			regions = []
		competitions = {}
		
		for region in regions:
			competitions[region] = []
		
		for competition in result:
			dto = CompetitionDto(competition).getDto()
						
			competitions[licence.Type.Region].append(dto)
		
		return competitions
