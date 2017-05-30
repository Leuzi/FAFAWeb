# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth import login, logout
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
		user = PermissionsManager.getPermissionsForUser(request.user)
		print(request.user.is_authenticated)
		if request.user.is_authenticated:
			return landingPage(request,user)
		else:
			return render(request, 'login.html')

def log_out(request):
	logout(request)
	return render(request, 'login.html')

def landingPage(request, user):	
	
	headerDto = PermissionsManager.getUserHeaderDto(user).getDto()
	
	return render(request, 'index.html', {'headerDto' : headerDto})