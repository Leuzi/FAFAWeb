# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth import login
from permissions.managers import PermissionsManager
from players.managers import PlayerManager
from teams.managers import TeamManager
from home.dto import LandingPageDto

# Create your views here.

def home(request):
	print(request.method)
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = PermissionsManager.getPermissions(username,password)

		if user:
			login(request, user.User)
			return landingPage(request,user)

		else:
			return render(request, 'login.html')
	else:
		print(request.user.is_authenticated)
		if request.user.is_authenticated:
			return render(request, 'login.html')
		else:
			return render(request, 'login.html')

			
def landingPage(request, user):	
	
	if user.class_name() == "Region":
		return landingPageRegion(request,user)
	else:
		return landingPageTeam(request,user)

def landingPageTeam(request, team):
	headerDto = TeamManager.getTeamDto(team).getDto()
	print(headerDto)
	#players = PlayerManager.getCurrentPlayers(team)
	#dto = LandingPageDto(players)
	return render(request, 'index.html', {'headerDto' : headerDto})
	
def landingPageRegion(request, region):
		#players = PlayerManager.getCurrentPlayers(team)
	#dto = LandingPageDto(players)
	return render(request, 'index.html', {})
