from players.models import Player
from licences.managers import LicenceManager
from teams.managers import TeamManager
from .dto import RegionPlayersDto

class PlayerManager():


	@classmethod
	def getPlayersForRegion(self,region):
		teams = TeamManager.getTeamsForRegion(region)
		
		teamPlayers = {}
		for team in teams:
			team.players = LicenceManager.getLicencesForTeam(team)
			teamPlayers[team] = team

		print( RegionPlayersDto(region,teamPlayers).getDto())
		return RegionPlayersDto(region,teamPlayers)
		

	@classmethod
	def getCurrentPlayers(self,team):
		return LicenceManager.getCurrentPlayers(team)

	@classmethod
	def getPlayerById(self, playerId):
		return Player.objects.get(id=playerId)

	
