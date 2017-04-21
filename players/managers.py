from players.models import Player
from licences.managers import LicenceManager

class PlayerManager():

	@classmethod
	def getCurrentPlayers(self,team):
		return LicenceManager.getCurrentPlayers(team)
