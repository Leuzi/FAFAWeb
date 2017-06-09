from django.shortcuts import render,redirect
from permissions.managers import PermissionsManager
from licences.managers import LicenceManager
from .forms import LicenceTypeForm,LicenceDurationForm
from .models import Licence

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
		
		print("licenceFormValid")
		print(licenceTypeForm.is_valid())
		print("licenceDurationForm")
		print(licenceDurationForm.is_valid())
		
		if licenceTypeForm.is_valid() and licenceDurationForm.is_valid():
			duration = licenceDurationForm.save()
			type = licenceTypeForm.save()
			
			licence = Licence(Type=type,Session = duration)
			licence.save()
			
		return redirect(list)
		
	else:	
		licenceTypeForm =  LicenceTypeForm()
		licenceDurationForm = LicenceDurationForm()
		
		return render(request, 'licencesDetail.html', {'headerDto': headerDto,
													'licenceTypeForm': licenceTypeForm,
													'licenceDurationForm': licenceDurationForm})
													
def editLicence(request,id):
	pass