# -*- coding: utf-8 -*-

class LicenceDto:
	def __init__(self,licence):		
		
		self.Name = licence.LicenceType.Name
		self.Shortening = licence.LicenceType.Shortening
		self.Region = licence.Region.Name
		self.StartDate = licence.Session.StartDate
		self.EndDate = licence.Session.EndDate
		self.Price = licence.Session.price
		sele.Active = licence.Active
		
	
	def getDto(self):
		context = {}
		context['Name'] = self.Name
		context['Shortening'] = self.Shortening
		context['Region'] = self.Region
		context['StartDate'] = self.StartDate
		context['EndDate'] = self.EndDate
		context['Price'] = self.Price
		context['Active'] = self.Active
		return context
