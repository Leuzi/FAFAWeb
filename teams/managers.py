from teams.models import Team
from teams.dto import TeamDto
from FAFAWeb.constants import *
from django.contrib.auth import authenticate,login
from licences.managers import LicenceManager

class TeamManager():

	@classmethod
	def getUserForTeam(self,user):
		return Team.objects.get(User=user)

	@classmethod
	def getResponsible(self,username,password):
		user = authenticate(username=username, password=password)
		responsible = None	
		
		if user is not None and user.is_active:
			try:
				responsible = Team.objects.get(User=user)
			except:
				responsible = None
				
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

	@classmethod
	def getTeams(self, teams):

		teams = {}
		
		for team in teams:
			teams[team] = getTeamDto(team)
	
	@classmethod
	def getTeamsForRegion(self, region):		
		return Team.objects.filter(Region=region)

