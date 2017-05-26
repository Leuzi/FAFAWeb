from django import forms
from .models import *

class LicenceTypeForm(forms.ModelForm):
			
	class Meta:
		model = LicenceType
		fields = ['Name', 'Shortening', 'Region']
		
class LicenceDurationForm(forms.ModelForm):
			
	class Meta:
		model = LicenceDuration
		fields = ['StartDate', 'EndDate', 'Price', 'MinimumBirthDate', 'MaximumBirthDate']