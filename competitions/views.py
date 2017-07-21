from django.shortcuts import render
from competitions.managers import CompetitionManager
from permissions.managers import PermissionsManager
from django.contrib.auth.decorators import login_required
from .models import Edition,CompetitionConditions
from .forms import CompetitionTypeForm, CompetitionConditionsForm, CompetitionLicencesForm, CompetitionTeamsForm,CompetitionEditionForm

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
	
	
	if not PermissionsManager.canEditCompetition(user,region.id):
		return redirect('/')

	headerDto = PermissionsManager.getUserHeaderDto(user).getDto()
	form = CompetitionTypeForm(request.POST or None, instance = competition)
	if request.method == "POST":		
		if form.is_valid():
			form.save()
			return list(request)
			
	return render(request, 'competitionsDetail.html', {'headerDto': headerDto,
														'competitionTypeForm': form})
		
	
	
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
		
		formCompetition = CompetitionEditionForm(request.POST or None, instance = competition)
		formConditions = CompetitionConditionsForm(request.POST or None, instance = competition.Conditions)
		formLicences = CompetitionLicencesForm(request.POST or None, region = region)
		formTeams = CompetitionTeamsForm(request.POST or None, region = region)

		if request.method == "POST":
			if formCompetition.is_valid() and formConditions.is_valid() and formLicences.is_valid() and formTeams.is_valid():
				formCompetition.save()
				formConditions.save()
				formLicences.save()
				formTeams.save()

				return manageCompetition(request, competition.Type.id)
			
		return render(request, 'competitionConditions.html', {'headerDto': headerDto,
													'formCompetition': formCompetition,
													'formConditions': formConditions,
													'formLicences': formLicences,
													'formTeams': formTeams})		

	return redirect('/')

def newEdition(request, competitionId):
	user = PermissionsManager.getPermissionsForUser(request.user)
	competition = CompetitionManager.getCompetitionTypeById(competitionId)
	region = competition.Region
	
	
	if not PermissionsManager.canCreateEdition(user,region.id):
		return redirect('/')

	if request.method == "GET":
		headerDto = PermissionsManager.getUserHeaderDto(user).getDto()
		formCompetition = CompetitionEditionForm()
		formConditions = CompetitionConditionsForm()		
		formLicences = CompetitionLicencesForm(region = region)
		formTeams = CompetitionTeamsForm(region = region)
		
		return render(request, 'competitionConditions.html', {'headerDto': headerDto,
												'formCompetition': formCompetition,
												'formConditions': formConditions,
												'formLicences': formLicences,
												'formTeams': formTeams})	
	



	elif request.method == "POST":
		edition = Edition()
		
		formCompetition = CompetitionEditionForm(request.POST, instance = edition)
		formConditions = CompetitionConditionsForm(request.POST)		
		formLicences = CompetitionLicencesForm(request.POST,region = region)
		formTeams = CompetitionTeamsForm(request.POST,region = region)
	
		print(formCompetition.is_valid())
		print(formConditions.is_valid())
		print(formLicences.is_valid())
		print(formCompetition.is_valid())
	
		if formCompetition.is_valid() and formConditions.is_valid() and formLicences.is_valid() and formTeams.is_valid():
			conditions = formConditions.save(commit=False)
			edition = formCompetition.save(commit=False)
			
			edition.Conditions = conditions
			edition.save()
			
			edition.Licences = formLicences.save(commit=False)
			edition.Teams = formTeams.save(commit=False)
			
			edition.save()

			return manageCompetition(request, competition.Type.id)
		
		else:
			return render(request, 'competitionConditions.html', {'headerDto': headerDto,
												'formCompetition': formCompetition,
												'formConditions': formConditions,
												'formLicences': formLicences,
												'formTeams': formTeams})	

