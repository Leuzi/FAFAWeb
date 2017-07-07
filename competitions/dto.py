# -*- coding: utf-8 -*-
from teams.dto import TeamDto
from licences.dto import LicenceDto

class CompetitionTypeDto:
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

		
class CompetitionDto:
	def __init__(self, competition, editions):
	
		self.Name = competition.Name
		self.Shortening = competition.Shortening
		self.Region = competition.Region
		self.Id = competition.id
		
		self.Editions = []
		
		for edition in editions:
			self.Editions.append(EditionDto(competition,edition).getDto())
		
		
	def getDto(self):
		context = {}
		context['Name'] = self.Name
		context['Shortening'] = self.Shortening
		context['Region'] = self.Region
		context['Id'] = self.Id
		context['Editions'] = self.Editions
		
		print(context)
		return context
		
		
class EditionDto:
	def __init__(self,competition ,edition):
		self.EditionId = edition.id
		self.Edition = competition.Shortening+' '+edition.Edition
		self.StartDate = edition.Conditions.StartDate
		self.EndDate = edition.Conditions.EndDate
		self.MinimumBirthDate = edition.Conditions.MinimumBirthDate
		self.MaximumBirthDate = edition.Conditions.MaximumBirthDate
		self.Gender = edition.Conditions.Gender
		self.Teams = []
		self.Licences = []
		
		for team in edition.Teams.all():
			self.Teams.append(TeamDto(team).getDto())
		
		for licence in edition.Licences.all():
			self.Licences.append(LicenceDto(licence))
			
	
	def getDto(self):
		context = {}
		context['EditionId'] = self.EditionId
		context['Edition'] = self.Edition
		context['StartDate'] = self.StartDate
		context['EndDate'] = self.EndDate
		context['MinimumBirthDate'] = self.MinimumBirthDate
		context['MaximumBirthDate'] = self.MaximumBirthDate
		context['Gender'] = self.Gender
		context['Teams'] = self.Teams
		context['Licences'] = self.Licences
		
		return context	
