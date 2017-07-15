from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from permissions.managers import PermissionsManager
from .managers import RostersManager
from regions.dto import RegionDto
from regions.managers import RegionManager

# Create your views here.
@login_required
def rosterListRegion(request, regionId):
	user = PermissionsManager.getPermissionsForUser(request.user)
	headerDto = PermissionsManager.getUserHeaderDto(user).getDto()
	
	regions = {}
	result = RegionManager.getAllRegions()
	for regionElement in result:
		regions[regionElement.RegionName] = RegionDto(regionElement)

	if PermissionsManager.canListPlayersRegion(user,regionId):
		competitionsDto = RostersManager.getCompetitionRostersRegion(regionId)
		return render(request, 'rosterList.html', {'headerDto' : headerDto,
												'regions': regions,
												'competitionsDto': competitionsDto})
	
	else:
		return redirect('/')
	
@login_required
def rosterListTeam(request):
	user = PermissionsManager.getPermissionsForUser(request.user)
	headerDto = PermissionsManager.getUserHeaderDto(user).getDto()
	competitionsDto = RostersManager.getCompetitionRostersTeam(user)
	print(competitionsDto)
	return render(request, 'rosterList.html', {'headerDto' : headerDto,
											   'competitionsDto': competitionsDto})
