from django import forms
from .models import *
from crispy_forms.helper import FormHelper

class CompetitionTypeForm(forms.ModelForm):
			
	class Meta:
		model = CompetitionType
		fields = ['Name', 'Shortening', 'Region']
	
	def __init__(self,*args, **kwargs):
		super(CompetitionTypeForm, self).__init__(*args,**kwargs)
		self.helper = FormHelper(self)
		self.helper.form_tag = False
		
class CompetitionConditionsForm(forms.ModelForm):
			
	class Meta:
		model = CompetitionConditions
		fields = ['StartDate', 'EndDate', 'MinimumBirthDate', 'MaximumBirthDate', 'Gender']

	def __init__(self,*args, **kwargs):
		super(CompetitionConditionsForm, self).__init__(*args,**kwargs)
		self.helper = FormHelper(self)
		self.helper.form_tag = False

class CompetitionTeamsForm(forms.ModelForm):	

	class Meta:
		model = Edition
		fields = ['Teams']

	def __init__(self,*args, **kwargs):
		super(CompetitionTeamsForm, self).__init__(*args,**kwargs)
		self.helper = FormHelper(self)
		self.helper.form_tag = False

class CompetitionLicencesForm(forms.ModelForm):	

	class Meta:
		model = Edition
		fields = ['Licences']

	def __init__(self,*args, **kwargs):
		super(CompetitionLicencesForm, self).__init__(*args,**kwargs)
		self.helper = FormHelper(self)
		self.helper.form_tag = False
