from django.shortcuts import render
from competitions.managers import CompetitionManager
from permissions.managers import PermissionsManager
from django.contrib.auth.decorators import login_required
from .forms import CompetitionTypeForm, CompetitionConditionsForm

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
													
def new(request, regionId):
	
	user = PermissionsManager.getPermissionsForUser(request.user)

	if not PermissionsManager.canCreateCompetition(user, regionId):
		return list(request)

	headerDto = PermissionsManager.getUserHeaderDto(user).getDto()

	if request.method == "POST":
		form = CompetitionTypeForm(request.POST)
		if form.is_valid():
			form.save()
			return list(request)
		else:
			pass

	else:
		competitionTypeForm = CompetitionTypeForm(initial={'Region': user})
		
		return render(request, 'competitionsDetail.html', {'headerDto': headerDto,
														'competitionTypeForm': competitionTypeForm})

def editCompetition(request, competitionId):
	
	user = PermissionsManager.getPermissionsForUser(request.user)
	region = CompetitionManager.getLicenceById(licenceId).Type.Region
