from . import models
from webLions.constants import *


class TeamManager():

	@classmethod
	def get_teams(self,SEASON=CSEASON):
		season = SeasonManager.get_season(season)
		if season == []:
			teams = None
		else:
			teams = models.Team.objects.filter(season=season)
		return teams

	@classmethod
	def get_active_teams(self):
		teams = models.Team.objects.all()

		return teams

	@classmethod
	def get_all_teams(self):
		teams = models.Team.objects.filter(active=false)
		
		return teams

	@classmethod
	def get_team(self,name):
		category = models.Category.objects.filter(name=team)
		if not category:			
			category = models.Category.objects.filter(shortening=team)
			if not category:
				category = None
		
		return category

