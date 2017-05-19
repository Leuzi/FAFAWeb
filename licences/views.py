from django.shortcuts import render
from permissions.managers import PermissionsManager
from licences.managers import LicenceManager

# Create your views here.
def list(request):
	user = PermissionsManager.getPermissionsForUser(request.user)
	headerDto = PermissionsManager.getUserHeaderDto(user).getDto()
	licences = {}
	
	if user.National:
		licences = LicenceManager.getAllLicences()
	
	else:
		licences = LicenceManager.getLicenceRegion(user.Region)
	
	return render(request, 'playersList.html', {'headerDto' : headerDto,
												'licences': licences})
	
def new(request):
	pass