# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth import login
from permissions.managers import PermissionsManager
from players.managers import PlayerManager
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
			return landingPageTeam(request,user)

		else:
			return render(request, 'login.html')
	else:
		print(request.user.is_authenticated)
		if request.user.is_authenticated:
			return render(request, 'login.html')
		else:
			return render(request, 'login.html')

			
def landingPageTeam(request, team):	
	players = PlayerManager.getCurrentPlayers(team)
	dto = LandingPageDto(players)
	return render(request, 'login.html', {dto : dto})
	
def landingPageRegion(request, region):
	pass