# -*- coding: utf-8 -*-

class RegionDto:
	def __init__(self,region):		
		self.Id = region.id
		self.ShortFederationName = region.ShortFederationName
		self.FederationName = region.FederationName
		self.UserName = region.User.username
		self.RegionName = region.RegionName
		self.Type = "Region"
		self.Photo = region.FederationLogo
		self.National = region.National
		if self.Photo is None:
			self.Photo = 'default.png'	
	
	def getDto(self):
		context = {}
		context['Id'] = self.Id
		context['ShortName'] = self.ShortFederationName
		context['Name'] = self.FederationName
		context['UserName'] = self.UserName
		context['Region'] = self.RegionName
		context['Type'] = self.Type
		context['Photo'] = self.Photo
		context['National'] = self.National
		return context
