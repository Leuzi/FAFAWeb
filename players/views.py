from django.shortcuts import render,redirect
from teams.managers import TeamManager
from permissions.managers import PermissionsManager
from django.contrib.auth.decorators import login_required
from .forms import PlayerForm
from .managers import PlayerManager
# Create your views here.

@login_required
def listTeam(request):
	user = PermissionsManager.getPermissionsForUser(request.user)
	regionId = user.id
	headerDto = PermissionsManager.getUserHeaderDto(user).getDto()
	
	teams = TeamManager.getTeam(user)
	
	teamsDto = PlayerManager.getTeams(teams)
	

	print(headerDto)
	return render(request, 'playersList.html', {'headerDto' : headerDto})

def listRegion(request,regionId):
	user = PermissionsManager.getPermissionsForUser(request.user)
	regionId = user.id
	headerDto = PermissionsManager.getUserHeaderDto(user).getDto()

	if PermissionsManager.canListPlayersRegion(user,regionId):
		playersDto = PlayerManager.getPlayersForRegion(user)
		
		

	else:

		return redirect('/')
	
@login_required
def new(request):
	user = PermissionsManager.getPermissionsForUser(request.user)
	headerDto = PermissionsManager.getUserHeaderDto(user).getDto()
	form = PlayerForm()
	return render(request, 'newPlayer.html', { 'form': form,'headerDto' : headerDto})
