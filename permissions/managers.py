from . import models
from FAFAWeb.constants import *
from regions.managers import RegionManager
from teams.managers import TeamManager


class PermissionsManager():

	@classmethod
	def getPermissions(self,user, password):
		user = RegionManager.getResponsible(user,password)
		if user is None:
			user = TeamManager.getResponsible(user,password)


		return user
