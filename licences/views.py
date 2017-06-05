from django.shortcuts import render
from permissions.managers import PermissionsManager
from licences.managers import LicenceManager
from .forms import LicenceTypeForm,LicenceDurationForm

# Create your views here.
def list(request):
	user = PermissionsManager.getPermissionsForUser(request.user)
	headerDto = PermissionsManager.getUserHeaderDto(user).getDto()
	licences = {}
	
	if user.National:
		licences = LicenceManager.getAllLicences()
	
	else:
		licences = LicenceManager.getLicenceRegion(user)
	
	return render(request, 'licencesList.html', {'headerDto' : headerDto,
												'licences': licences})
	
def new(request):
	
	user = PermissionsManager.getPermissionsForUser(request.user)
	headerDto = PermissionsManager.getUserHeaderDto(user).getDto()
	
	if request.method == "POST":
		licenceTypeForm = LicenceTypeForm(request.POST)
		licenceDurationForm = LicenceDurationForm(request.POST)
		
		if licenceTypeForm.is_valid() and licenceDurationForm.is_valid():
			licenceDurationForm.save()
			licenceTypeForm.save()
		
	else:	
		licenceTypeForm =  LicenceTypeForm()
		licenceDurationForm = LicenceDurationForm()
		
		return render(request, 'licencesDetail.html', {'headerDto': headerDto,
													'licenceTypeForm': licenceTypeForm,
													'licenceDurationForm': licenceDurationForm})