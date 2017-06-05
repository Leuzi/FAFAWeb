# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
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
		if request.user.is_authenticated:
			user = PermissionsManager.getPermissionsForUser(request.user)		
			return landingPage(request,user)
		else:
			return render(request, 'login.html')

def loginout(request):
	logout(request)
	return redirect('/')

def landingPage(request, user):	
	
	headerDto = PermissionsManager.getUserHeaderDto(user).getDto()
	
	return render(request, 'index.html', {'headerDto' : headerDto})