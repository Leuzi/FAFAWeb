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
	licences = LicenceManager.getLicencesForUser(user)
	
	return render(request, 'licencesList.html', {'headerDto' : headerDto,
												'licences': licences})
	
def new(request, regionId):

	user = PermissionsManager.getPermissionsForUser(request.user)

	if not PermissionsManager.canCreateLicence(user,regionId):	
		return list(request)

	headerDto = PermissionsManager.getUserHeaderDto(user).getDto()
	licenceTypeForm = LicenceTypeForm(request.POST or None,initial={'Region': user})
	licenceDurationForm = LicenceDurationForm(request.POST or None)	

	if request.method == "POST":
		if licenceTypeForm.is_valid() and licenceDurationForm.is_valid():
			duration = licenceDurationForm.save()
			type = licenceTypeForm.save()			
			licence = Licence(Type=type,Session = duration)
			licence.save()

			return redirect(list)
		
	return render(request, 'licencesDetail.html', {'headerDto': headerDto,
													'licenceTypeForm': licenceTypeForm,
													'licenceDurationForm': licenceDurationForm})
													
def editLicence(request,licenceId):
	user = PermissionsManager.getPermissionsForUser(request.user)
	region =  LicenceManager.getLicenceById(licenceId).Type.Region

	if not PermissionsManager.canEditLicence(user,region):
		return list(request)
		
	headerDto = PermissionsManager.getUserHeaderDto(user).getDto()

	licence = LicenceManager.getLicenceById(licenceId)
	licenceTypeForm = LicenceTypeForm(request.POST or None, instance = licence.Type)
	licenceDurationForm = LicenceDurationForm(request.POST or None, instance =  licence.Session)
	
	if request.method == "POST":		
		if licenceTypeForm.is_valid() and licenceDurationForm.is_valid():
			licenceTypeForm.save()			
			licenceDurationForm.save()			
			return list(request)

	
	return render(request, 'licencesDetail.html', {'headerDto': headerDto,
													'licenceTypeForm': licenceTypeForm,
													'licenceDurationForm': licenceDurationForm})
	
