from teams.models import Team
from teams.dto import TeamDto
from FAFAWeb.constants import *
from django.contrib.auth import authenticate,login

class TeamManager():

	@classmethod
	def getResponsible(self,username,password):
		user = authenticate(username=username, password=password)
		responsible = None		
		if user is not None:
			responsible = Team.objects.get(User=user)
		
		return responsible

	@classmethod
	def getTeamDto(self,team):
		return TeamDto(team)

	@classmethod
	def get_teams(self,SEASON=CSEASON):
		season = SeasonManager.get_season(season)
		if season == []:
			teams = None
		else:
			teams = Team.objects.filter(season=season)
		return teams

	@classmethod
	def get_active_teams(self):
		teams = Team.objects.all()

		return teams

	@classmethod
	def get_all_teams(self):
		teams = Team.objects.filter(active=false)
		
		return teams

	@classmethod
	def get_team(self,name):
		category = Category.objects.filter(name=team)
		if not category:			
			category = Category.objects.filter(shortening=team)
			if not category:
				category = None
		
		return category

