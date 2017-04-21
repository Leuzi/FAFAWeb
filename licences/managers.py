from . import models
from FAFAWeb.constants import *

class PlayerManager():
	@classmethod
	def get_player(self,dni):
		player = models.Player.objects.filter(dni=dni)
		if season == [] :
			season = None
		return season
	
class LicenceTypeManager():
	@classmethod
	def get_licences(self,active=True):
		licences = models.Licences.objects.filter(Active=active)
		
class LicenceManager():
	@classmethod
	def getCurrentPlayers(self, team):		
		licences = models.ValidFor.objects.filter(Team=team)
		
		
	def getValidLicenses(self):
		pass