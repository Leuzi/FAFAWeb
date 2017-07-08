# -*- coding: utf-8 -*-

class RegionPlayersDto:
	def __init__(self,region,teams):		
		self.Id = region.id
		self.Shortening = region.ShortRegionName
		self.Name = region.RegionName
		self.Teams = []		

		for team in teams:
			self.Teams.append(TeamPlayersDto(team).getDto())
	
	def getDto(self):
		context = {}
		context['Id'] = self.Id
		context['Shortening'] = self.Shortening
		context['Name'] = self.Name
		context['Teams'] = self.Teams
		return context

class TeamPlayersDto:
	def __init__(self,team):
		self.Name = team.Name
		self.Logo = team.Logo
		self.Players = []

		for player in team.players:
			self.Players.append(PlayerDto(player.Player,player.Licence).getDto())

	def getDto(self):
		context = {}
		context['Name'] = self.Name
		context['Logo'] = self.Logo
		context['Players'] = self.Players
		return context

class PlayerDto:
	def __init__(self,player,licence):
		self.Id = player.id
		self.Licence = licence.Type.Region.ShortRegionName + player.LicenceId + licence.Type.Shortening
		self.StartDate = licence.Session.StartDate
		self.EndDate = licence.Session.EndDate
		self.Price = licence.Session.Price
		self.LicenceName = licence.Type.Name
		self.State = 'OK'
		self.DNI = player.DNI
		self.Name = player.Name
		self.Surname = player.Surname
		self.BirthDate = player.BirthDate
		self.Country = player.Country
		self.ZIPCode = player.ZIPCode
		self.City = player.City
		self.Region = player.Region
		self.Mail = player.Mail
		self.LicenceId = player.LicenceId
		self.Gender = player.Gender
		

	def getDto(self):
		context = {}
		context['Id'] = self.Id
		context['DNI'] = self.DNI
		context['Name'] = self.Name
		context['Surname'] = self.Surname
		context['BirthDate'] = self.BirthDate
		context['Country'] = self.Country
		context['ZIPCode'] = self.ZIPCode
		context['City'] = self.City
		context['Region'] = self.Surname
		context['Mail'] = self.Mail
		context['LicenceId'] = self.LicenceId
		context['Gender'] = self.Gender
		context['Licence'] = self.Licence
		context['StartDate'] = self.StartDate
		context['EndDate'] = self.EndDate
		context['Price'] = self.Price
		context['LicenceName'] = self.LicenceName
		context['State'] = self.State

		return context
