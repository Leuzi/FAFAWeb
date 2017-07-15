from . import models
from competitions.managers import CompetitionManager
from licences.managers import LicenceManager
from .dto import RosterCompetitionDto

class RostersManager():

	@classmethod
	def getCompetitionRostersTeam(self, team):
		
		competitions = CompetitionManager.getCompetitionsForTeam(team)

		editions = {}		

		for competition in competitions:
			editions[competition] = []
			editions[competition] = competition, RostersManager.getPlayersForCompetition(competition,team)
		
		return RosterCompetitionDto(team, editions).getDto()

	@classmethod
	def getCompetitionRostersRegion(self, region):
		competitions = CompetitionManager.getCompetitionsForRegion(region)

		for competition in competitions:
			for team in competition.Teams:
				print(RostersManager.getCompetitionRostersTeam(team))

	@classmethod
	def getPlayersForCompetition(self,competition,team):
		
		validLicences = competition.Licences.all()
		players = LicenceManager.getPlayersWithValidLicences(team,validLicences)

		return RostersManager.filterPlayersByConditions(players,competition)

	@classmethod
	def filterPlayersByConditions(self, players,conditions):
		validPlayers = []
		
		for player in players:
			if RostersManager.passTheConditions(player.Player, conditions.Conditions):
				validPlayers.append(player)


		return validPlayers


	@classmethod
	def passTheConditions(self, player, conditions):
		
		if conditions.Gender is not "O" and player.Gender is not conditions.Gender:
			return False

		if player.BirthDate > conditions.MinimumBirthDate:
			return False

		if conditions.MaximumBirthDate is not None and player.BirthDate < conditions.MaximumBirthDate:
			return False

		return True

		
