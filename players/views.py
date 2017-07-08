from django.shortcuts import render,redirect
from teams.managers import TeamManager
from permissions.managers import PermissionsManager
from regions.managers import RegionManager
from django.contrib.auth.decorators import login_required
from .forms import PlayerForm
from .managers import PlayerManager
from regions.dto import RegionDto
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
	headerDto = PermissionsManager.getUserHeaderDto(user).getDto()
	region = RegionManager.getRegionById(regionId)
	regions = {}

	result = RegionManager.getAllRegions()
	for regionElement in result:
		regions[regionElement.RegionName] = RegionDto(regionElement)
	if PermissionsManager.canListPlayersRegion(user,regionId):
		playersDto = PlayerManager.getPlayersForRegion(region)
		
		print(headerDto)
		return render(request, 'playersList.html', {'headerDto': headerDto,
													'regions': regions,
													'playersDto': playersDto})
	else:

		return redirect('/')
	
@login_required
def new(request):
	user = PermissionsManager.getPermissionsForUser(request.user)
	headerDto = PermissionsManager.getUserHeaderDto(user).getDto()
	form = PlayerForm()
	return render(request, 'newPlayer.html', { 'form': form,'headerDto' : headerDto})


def editPlayer(request,playerId):

	user = PermissionsManager.getPermissionsForUser(request.user)
	headerDto = PermissionsManager.getUserHeaderDto(user).getDto()
	player = PlayerManager.getPlayerById(playerId)

	playerForm = PlayerForm(request.POST or None, instance= player)

	if request.method == "POST":
		if playerForm.is_valid():
			playerForm.save()
			return redirect('/')
			

	return render(request, 'newPlayer.html', {'headerDto':headerDto,
											'playerForm':playerForm})
