# -*- coding: utf-8 -*-
from players.dto import PlayerDto
from teams.dto import TeamDto

class RosterCompetitionDto():
	def __init__(self,team, editions):
		self.Team = TeamDto(team)
		self.Editions = []
		for edition,players in editions.items():
			self.Editions.append(EditionDto(edition,players[1]).getDto())
		
	def getDto(self):
		context = self.Team.getDto()
		context['Editions'] = self.Editions
		return context

class EditionDto():
	def __init__(self,edition,players):
		self.Name = edition.Edition + ' ' + edition.Competition.Name
		self.Shortening = edition.Edition + ' ' + edition.Competition.Shortening
		self.CompetitionId = edition.id
		self.StartDate = edition.Conditions.StartDate
		self.EndDate = edition.Conditions.EndDate
		self.MinimumBirthDate = edition.Conditions.MinimumBirthDate
		self.MaximumBirthDate = edition.Conditions.MaximumBirthDate
		self.Gender = edition.Conditions.Gender
		self.Players = []
		
		for player in players:
			self.Players.append(PlayerDto(player.Player,player.Licence).getDto())

	def getDto(self):
		context = {}
		context['Name'] = self.Name
		context['Shortening'] = self.Shortening
		context['CompetitionId'] = self.CompetitionId
		context['StartDate'] = self.StartDate
		context['EndDate'] = self.EndDate
		context['MinimumBirthDate'] = self.MinimumBirthDate
		context['MaximumBirthDate'] = self.MaximumBirthDate
		context['Gender'] = self.Gender
		context['Players'] = self.Players

		return context
