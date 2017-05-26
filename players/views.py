from django.shortcuts import render
from teams.managers import TeamManager
from permissions.managers import PermissionsManager
from django.contrib.auth.decorators import login_required
from .forms import PlayerForm
# Create your views here.

@login_required
def list(request):
	user = PermissionsManager.getPermissionsForUser(request.user)
	headerDto = PermissionsManager.getUserHeaderDto(user).getDto()
	return render(request, 'playersList.html', {'headerDto' : headerDto})
	
@login_required
def new(request):
	user = PermissionsManager.getPermissionsForUser(request.user)
	headerDto = PermissionsManager.getUserHeaderDto(user).getDto()
	form = PlayerForm()
	return render(request, 'newPlayer.html', { 'form': form,'headerDto' : headerDto})