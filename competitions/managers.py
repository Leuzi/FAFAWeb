from . import models
from FAFAWeb.constants import *
from .dto import CompetitionDto

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
		else:
			result = models.Competition.objects.filter(Type__Region=filter)
		competitions = {}
		
		for competition in result:
			competitions[competition.Type.Region.RegionName] = []
		
		for competition in result:
			dto = CompetitionDto(competition).getDto()
						
			competitions[licence.Type.Region.RegionName].append(dto)
		
		return competitions
