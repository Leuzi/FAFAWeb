from . import models
from FAFAWeb.constants import *


class SeasonManager():

	@classmethod
	def get_season(self,season=CSEASON):
		season = models.Season.objects.filter(name=season)
		if season == [] :
			season = None
		return season

