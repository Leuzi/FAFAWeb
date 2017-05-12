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
		
	@classmethod
	def getPermissionsForUser(self, user):
		userLogged = RegionManager.getUserForRegion(user)
		
		if userLogged is None:
			userLogged = TeamManager.getUserForTeam(user)

		return userLogged
		
	@classmethod
	def getUserHeaderDto(self, user):
		
		if user.class_name() == "Region":
			headerDto =  RegionManager.getRegionDto(user)
		else:
			headerDto =  TeamManager.getTeamDto(user)
			
		return headerDto
