# -*- coding: utf-8 -*-

class LicenceDto:
	def __init__(self,licence):		
		
		self.Name = licence.Type.Name
		self.Shortening = licence.Type.Shortening
		self.Region = licence.Type.Region.RegionName
		self.StartDate = licence.Session.StartDate
		self.EndDate = licence.Session.EndDate
		self.MinimumBirthDate = licence.Session.MinimumBirthDate
		self.MaximumBirthDate = licence.Session.MaximumBirthDate
		self.Price = licence.Session.Price
		self.Active = licence.Active
		self.Id = licence.id
		
	
	def getDto(self):
		context = {}
		context['Name'] = self.Name
		context['Shortening'] = self.Shortening
		context['Region'] = self.Region
		context['StartDate'] = self.StartDate
		context['EndDate'] = self.EndDate
		context['MinimumBirthDate'] = self.MinimumBirthDate
		context['MaximumBirthDate'] = self.MaximumBirthDate
		context['Price'] = self.Price
		context['Active'] = self.Active
		context['Id'] = self.Id
		return context
