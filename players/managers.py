from players.models import Player
from licences.managers import LicenceManager
from teams.managers import TeamManager

class PlayerManager():


	@classmethod
	def getPlayersForRegion(self,region):
		teams = TeamManager.getTeamsForRegion(region)
		print(region)
		print(teams)
		teamPlayers = []
		for team in teams:
			teamPlayers[team.Name] = LicenceManager.getLicencesForTeam(team)
		

	@classmethod
	def getCurrentPlayers(self,team):
		return LicenceManager.getCurrentPlayers(team)

	
