from . import models
from FAFAWeb.constants import *
from regions.managers import RegionManager
from teams.managers import TeamManager
from licences.managers import LicenceManager


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

	@classmethod
	def canEditLicence(self,user,region):

		if region is not None and user is not None:
			if region == user or user.National:
				return True

		return False
		

	@classmethod
	def canCreateLicence(self,user,regionId):
		
		region = RegionManager.getRegionById(regionId)

		if region is not None and user is not None:
			if region == user or user.National:
				return True

		return False

	@classmethod
	def canCreateCompetition(self,user,regionId):
		
		region = RegionManager.getRegionById(regionId)

		if region is not None and user is not None:
			if region == user or user.National:
				return True

		return False
		
	@classmethod
	def canEditCompetition(self,user,regionId):
		
		region = RegionManager.getRegionById(regionId)

		if region is not None and user is not None:
			if region == user or user.National:
				return True

		return False

	@classmethod
	def canManageEditions(self, user, regionId):
		region = RegionManager.getRegionById(regionId)

		if region is not None and user is not None:
			if region == user or user.National:
				return True

		return False

	@classmethod
	def canEditConditions(self, user, regionId):
		region = RegionManager.getRegionById(regionId)

		if region is not None and user is not None:
			if region == user or user.National:
				return True

		return False

	@classmethod
	def canListPlayersRegion(self, user, regionId):
		region = RegionManager.getRegionById(regionId)

		if region is not None and user is not None:
			if region == user or user.National:
				return True

		return False

