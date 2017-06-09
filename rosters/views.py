from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from permissions.managers import PermissionsManager

# Create your views here.
@login_required
def rosterList(request):
	user = PermissionsManager.getPermissionsForUser(request.user)
	headerDto = PermissionsManager.getUserHeaderDto(user).getDto()
	return render(request, 'rosterList.html', {'headerDto' : headerDto})