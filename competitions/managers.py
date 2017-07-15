from . import models
from FAFAWeb.constants import *
from .dto import CompetitionTypeDto, CompetitionDto
from regions.managers import RegionManager
from datetime import datetime, timedelta, time

class CompetitionManager():

	@classmethod
	def getAllCompetitionTypes(self):
		return CompetitionManager.getCompetitionsTypes()
	
	@classmethod
	def getCompetitionsTypesRegion(self,Region):
		return CompetitionManager.getCompetitionsTypes(Region)

	@classmethod
	def getCompetitionsTypes(self, filter=None):
		
		if filter is None:
			result = models.CompetitionType.objects.all()
			regions = RegionManager.getAllRegions()
		else:
			result = models.CompetitionType.objects.filter(Region=filter)
			regions = [filter]
		competitions = {}
		
		for region in regions:
			competitions[region] = []
		
		for competition in result:
			dto = CompetitionTypeDto(competition).getDto()
						
			competitions[competition.Region].append(dto)
		
		return competitions
		
	@classmethod
	def getCompetitionTypeById(self, competitionTypeId):
	
		competition = models.CompetitionType.objects.get(id=competitionTypeId)

		return competition

	@classmethod
	def getCompetitionById(self, competitionId):
		return models.Edition.objects.get(id=competitionId)
		
	@classmethod
	def getEditions(self, competitionTypeId):
		
		competition = CompetitionManager.getCompetitionTypeById(competitionTypeId)	
		
		editions =  models.Edition.objects.filter(Competition=competition)
		
		return CompetitionDto(competition, editions).getDto()		

	def getCompetitionsForTeam(team):
		today = datetime.now().date()
		return models.Edition.objects.filter(Teams__in=[team]).filter(Conditions__StartDate__lte=today,Conditions__EndDate__gte=today)

	def getCompetitionsForRegion(region):
		today = datetime.now().date()
		return models.Edition.objects.filter(Competition__Region=region).filter(Conditions__StartDate__lte=today,Conditions__EndDate__gte=today)
