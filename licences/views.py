# -*- coding: utf-8 -*-
from __future__ import unicode_literals
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
	
def new(request, regionId):

	user = PermissionsManager.getPermissionsForUser(request.user)

	if not PermissionsManager.canCreateLicence(user,regionId):	
		return list(request)

	user = PermissionsManager.getPermissionsForUser(request.user)
	headerDto = PermissionsManager.getUserHeaderDto(user).getDto()
		
	if request.method == "POST":
		licenceTypeForm = LicenceTypeForm(request.POST,initial={'Region': user})
		licenceDurationForm = LicenceDurationForm(request.POST)
		
		if licenceTypeForm.is_valid() and licenceDurationForm.is_valid():
			duration = licenceDurationForm.save()
			type = licenceTypeForm.save()
			
			licence = Licence(Type=type,Session = duration)
			licence.save()
			
		return redirect(list)
		
	else:	
		licenceTypeForm =  LicenceTypeForm(initial={'Region': user})
		licenceDurationForm = LicenceDurationForm()
		
		return render(request, 'licencesDetail.html', {'headerDto': headerDto,
													'licenceTypeForm': licenceTypeForm,
													'licenceDurationForm': licenceDurationForm})
													
def editLicence(request,licenceId):
	user = PermissionsManager.getPermissionsForUser(request.user)
	region =  LicenceManager.getLicenceById(licenceId).Type.Region
	headerDto = PermissionsManager.getUserHeaderDto(user).getDto()

	if PermissionsManager.canEditLicence(user,region):
		licence = LicenceManager.getLicenceById(licenceId)
		licenceDurationForm = LicenceTypeForm(instance=licence.Session)
		licenceTypeForm = LicenceDurationForm(instance=licence.Type)

		return render(request, 'licencesDetail.html', {'headerDto': headerDto,
													'licenceTypeForm': licenceTypeForm,
													'licenceDurationForm': licenceDurationForm})
