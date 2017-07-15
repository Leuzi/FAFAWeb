from django import forms
from .models import *
from django.db.models import Q
from crispy_forms.helper import FormHelper
from licences.models import Licence
from teams.models import Team


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

class CompetitionEditionForm(forms.ModelForm):
	
	class Meta:
		model = Edition
		fields = ['Edition']

	def __init__(self,*args, **kwargs):
		super(CompetitionEditionForm,self).__init__(*args, **kwargs)
		self.helper = FormHelper(self)
		self.helper.form_tag = False
		

class CompetitionTeamsForm(forms.ModelForm):	

	class Meta:
		model = Edition
		fields = ['Teams']

	def __init__(self,*args, **kwargs):
		region = kwargs.pop('region')
		super(CompetitionTeamsForm, self).__init__(*args,**kwargs)
		self.helper = FormHelper(self)
		self.helper.form_tag = False
		
		if region.National:
			regions = Team.objects.all()
		else:
			regions = Team.objects.filter(Region=region)

class CompetitionLicencesForm(forms.ModelForm):	

	class Meta:
		model = Edition
		fields = ['Licences']

	def __init__(self,*args, **kwargs):
		region = kwargs.pop('region')
		super(CompetitionLicencesForm, self).__init__(*args,**kwargs)
		self.helper = FormHelper(self)
		self.helper.form_tag = False
		criteria1 = Q(Type__Region=region)
		criteria2 = Q(Type__Region__National=True)
		regions = Licence.objects.filter(criteria1 | criteria2)
		self.fields['Licences'].queryset = regions
