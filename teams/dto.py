# -*- coding: utf-8 -*-

class TeamDto:
	def __init__(self,team):		
		self.ShortName = team.Shortening
		self.TeamName = team.Name
		self.UserName = team.User.username
		self.Region = team.Region.RegionName
		self.Type = "Team"
		
	
	def getDto(self):
		context = {}
		context['ShortName'] = self.ShortName
		context['Name'] = self.TeamName
		context['UserName'] = self.UserName
		context['Region'] = self.Region
		context['Type'] = self.Type
		return context

