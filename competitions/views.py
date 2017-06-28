from django.shortcuts import render
from competitions.managers import CompetitionManager
from permissions.managers import PermissionsManager
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def list(request):
	user = PermissionsManager.getPermissionsForUser(request.user)
	headerDto = PermissionsManager.getUserHeaderDto(user).getDto()
	
	competitions = {}

	if user.National:
		competitions = CompetitionManager.getAllCompetitions()
	else:
		competitions = CompetitionManager.getCompetitionsRegion(user)
	
	return render(request, 'competitionList.html', {'headerDto': headerDto,
													'competitions': competitions})
													
def new(request):
	pass
