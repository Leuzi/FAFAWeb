from . import models
from FAFAWeb.constants import *
from regions.managers import RegionManager
from teams.managers import TeamManager


class PermissionsManager():

	@classmethod
	def getPermissions(self,username, password):
		user = RegionManager.getResponsible(username,password)
		
		if user is None:
			user = TeamManager.getResponsible(username,password)

		return user
