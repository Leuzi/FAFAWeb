from django.shortcuts import render
from teams.managers import TeamManager
from permissions.managers import PermissionsManager
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def list(request):
	user = PermissionsManager.getPermissionsForUser(request.user)
	headerDto = PermissionsManager.getUserHeaderDto(user).getDto()
	return render(request, 'playersList.html', {'headerDto' : headerDto})
	
def new(request):
	pass