from django.shortcuts import render
from competitions.managers import CompetitionManager
from permissions.managers import PermissionsManager
from django.contrib.auth.decorators import login_required
from .forms import CompetitionTypeForm, CompetitionConditionsForm, CompetitionLicencesForm, CompetitionTeamsForm

# Create your views here.
@login_required
def list(request):
	user = PermissionsManager.getPermissionsForUser(request.user)
	headerDto = PermissionsManager.getUserHeaderDto(user).getDto()
	
	competitions = {}

	if user.National:
		competitions = CompetitionManager.getAllCompetitionTypes()
	else:
		competitions = CompetitionManager.getCompetitionsTypesRegion(user)
	
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
			return render(request, 'competitionsDetail.html', {'headerDto': headerDto,
															'competitionTypeForm': form})

	else:
		competitionTypeForm = CompetitionTypeForm(initial={'Region': user})
		
		return render(request, 'competitionsDetail.html', {'headerDto': headerDto,
														'competitionTypeForm': competitionTypeForm})

def editCompetition(request, competitionId):	
	user = PermissionsManager.getPermissionsForUser(request.user)
	competition = CompetitionManager.getCompetitionTypeById(competitionId)
	region = competition.Region
	headerDto = PermissionsManager.getUserHeaderDto(user).getDto()
	
	if PermissionsManager.canEditCompetition(user,region.id):
		if request.method == "POST":
			form = CompetitionTypeForm(request.POST, instance = competition)
			if form.is_valid():
				form.save()
				return list(request)
			else:
				return render(request, 'competitionsDetail.html', {'headerDto': headerDto,
															'competitionTypeForm': form})
		
		else:		
			competitionTypeForm = CompetitionTypeForm(instance=competition)			
			return render(request, 'competitionsDetail.html', {'headerDto': headerDto,
															'competitionTypeForm': competitionTypeForm})
		
	return redirect('/')
	
def manageCompetition(request, competitionId):
	user = PermissionsManager.getPermissionsForUser(request.user)
	competition = CompetitionManager.getCompetitionTypeById(competitionId)
	region = competition.Region
	headerDto = PermissionsManager.getUserHeaderDto(user).getDto()
	
	if PermissionsManager.canManageEditions(user, region.id):
		competition = CompetitionManager.getEditions(competitionId)
		return render(request, 'competitionManage.html', {'headerDto': headerDto,
														  'competition': competition})
	
	return redirect('/')

def editConditions(request, competitionId):
	user = PermissionsManager.getPermissionsForUser(request.user)
	competition = CompetitionManager.getCompetitionById(competitionId)
	region = competition.Competition.Region
	headerDto = PermissionsManager.getUserHeaderDto(user).getDto()

	if PermissionsManager.canEditConditions(user,region.id):
		
		formConditions = CompetitionConditionsForm(request.POST or None, instance = competition.Conditions)
		formLicences = CompetitionLicencesForm(request.POST or None, region = region)
		formTeams = CompetitionTeamsForm(request.POST or None, region = region)

		if request.method == "POST":
			if formConditions.is_valid() and formLicences.is_valid() and formTeams.is_valid():
				formConditions.save()
				
				formLicences.save()
				formTeams.save()

				return manageCompetition(request, competition.Type.id)
			
		return render(request, 'competitionConditions.html', {'headerDto': headerDto,
													'formConditions': formConditions,
													'formLicences': formLicences,
													'formTeams': formTeams})		

	return redirect('/')


