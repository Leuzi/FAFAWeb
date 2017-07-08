from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from permissions.managers import PermissionsManager

# Create your views here.
@login_required
def rosterListRegion(request):
	user = PermissionsManager.getPermissionsForUser(request.user)
	headerDto = PermissionsManager.getUserHeaderDto(user).getDto()
	competitionsDto = RosterManager.getRostersDto()
	
	return render(request, 'rosterList.html', {'headerDto' : headerDto})

def rosterListTeam(request):
	user = PermissionsManager.getPermissionsForUser(request.user)
	headerDto = PermissionsManager.getUserHeaderDto(user).getDto()
	competitionsDto = RosterManager.getRostersDto()

	return render(request, 'rosterList.html', {'headerDto' : headerDto})
