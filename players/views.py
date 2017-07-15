from django.shortcuts import render,redirect
from teams.managers import TeamManager
from permissions.managers import PermissionsManager
from regions.managers import RegionManager
from django.contrib.auth.decorators import login_required
from .forms import PlayerForm,SelectPlayerForm
from .managers import PlayerManager
from regions.dto import RegionDto
# Create your views here.

@login_required
def listTeam(request):
	user = PermissionsManager.getPermissionsForUser(request.user)
	regionId = user.id
	region = RegionManager.getRegionById(regionId)
	headerDto = PermissionsManager.getUserHeaderDto(user).getDto()
	
	playersDto = PlayerManager.getPlayersForTeam(region, user)
	
	return render(request, 'playersListTeam.html', {'headerDto' : headerDto,
												'playersDto': playersDto})

def listRegion(request,regionId):
	user = PermissionsManager.getPermissionsForUser(request.user)
	headerDto = PermissionsManager.getUserHeaderDto(user).getDto()
	regions = {}
	region = RegionManager.getRegionById(regionId)

	result = RegionManager.getAllRegions()
	for regionElement in result:
		regions[regionElement.RegionName] = RegionDto(regionElement)
	if PermissionsManager.canListPlayersRegion(user,regionId):
		playersDto = PlayerManager.getPlayersForRegion(region)
		
		return render(request, 'playersList.html', {'headerDto': headerDto,
													'regions': regions,
													'playersDto': playersDto})
	else:
		return redirect('/')
	
@login_required
def newPlayer(request, teamId):
	user = PermissionsManager.getPermissionsForUser(request.user)
	headerDto = PermissionsManager.getUserHeaderDto(user).getDto()
	selectPlayerForm = SelectPlayerForm(request.POST or None)

	if request.method == "POST:
		if selePlayerForm.is_valid():
		
			player = PlayerManager.findPlayerByIdNumber(selectPlayerForm.cleaned_data['my_form_field_name'])
			return editPlayerLicence(None, player)

	
	return render(request, 'findPlayer.html', { 'selectPlayerForm': selectPlayerForm,'headerDto' : headerDto})

def editPlayerLicence(request,player):

	user = PermissionsManager.getPermissionsForUser(request.user)
	headerDto = PermissionsManager.getUserHeaderDto(user).getDto()

	playerForm = PlayerForm(request.POST or None, instance= player)

	if request.method == "POST":
		if playerForm.is_valid():
			playerForm.save()
			return selectLicences(None, player)
			

	return render(request, 'newPlayer.html', {'headerDto':headerDto,
											'playerForm':playerForm})


def selectLicences(request, player):
	user = PermissionsManager.getPermissionsForUser(request.user)
	headerDto = PermissionsManager.getUserHeaderDto(user).getDto()
	player = PlayerManager.getPlayerById(playerId)

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
