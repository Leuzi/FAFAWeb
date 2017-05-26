# -*- coding: utf-8 -*-

class CompetitionDto:
	def __init__(self,competition):		
		
		self.Name = competition.Type.Name
		self.Shortening = competition.Type.Shortening
		self.Region = competition.Type.Region.RegionName
		self.StartDate = competition.Conditions.StartDate
		self.EndDate = competition.Conditions.EndDate
		self.MinimumAge = competition.Conditions.MinimumAge
		self.MaximunAge = competition.Conditions.MaximunAge
		self.Active = competition.Active
		
	
	def getDto(self):
		context = {}
		context['Name'] = self.Name
		context['Shortening'] = self.Shortening
		context['Region'] = self.Region
		context['StartDate'] = self.StartDate
		context['EndDate'] = self.EndDate
		context['MinimumAge'] = self.MinimumAge
		context['MaximunAge'] = self.MaximunAge
		context['Active'] = self.Active
		return context
