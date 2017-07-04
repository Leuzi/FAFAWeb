# -*- coding: utf-8 -*-

class CompetitionDto:
	def __init__(self,competition):		
		
		self.Name = competition.Name
		self.Shortening = competition.Shortening
		self.Region = competition.Region.RegionName
		self.Id = competition.id
		
	
	def getDto(self):
		context = {}
		context['Name'] = self.Name
		context['Shortening'] = self.Shortening
		context['Region'] = self.Region
		context['Id'] = self.Id
		return context
