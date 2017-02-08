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
	def get_licences(self,active=ACTIVE):
		licences = models.Licences.objects.filter(active=active)