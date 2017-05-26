from django import forms
from .models import *

class CompetitionTypeForm(forms.ModelForm):
			
	class Meta:
		model = CompetitionType
		fields = ['Name', 'Shortening', 'Region']
		
class CompetitionConditionsForm(forms.ModelForm):
			
	class Meta:
		model = CompetitionConditions
		fields = ['Edition','Years','StartDate', 'EndDate', 'MinimumBirthDate', 'MaximumBirthDate']