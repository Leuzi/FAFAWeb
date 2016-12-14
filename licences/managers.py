from . import models
from FAFAWeb.constants import *


class PlayerManager():

	@classmethod
	def get_player(self,dni):
		player = models.Player.objects.filter(dni=dni)
		if season == [] :
			season = None
		return season

