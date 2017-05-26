from . import models
from FAFAWeb.constants import *
from .dto import CompetitionDto

class CompetitionManager():
	@classmethod
	def getAllCompetitions(self):
		competitions = {}
		result = models.Competition.objects.all()
		
		for competition in result:
			competitions[competition.Type.Region.RegionName] = []
		
		for competition in result:
			dto = CompetitionDto(competition).getDto()
						
			competitions[licence.Type.Region.RegionName].append(dto)
		
		return competitions
