from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from .models import *

class LicenceTypeForm(forms.ModelForm):
			
	class Meta:
		model = LicenceType
		fields = ['Name', 'Shortening', 'Region']
	
	def __init__(self, *args, **kwargs):
		super(LicenceTypeForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper(self)
		self.helper.form_id = 'id-LicenceForm'
		self.helper.form_class = 'blueForms'
		self.helper.form_method = 'post'
		self.helper.form_action = 'submit_licence'
		self.helper.form_tag = False
		
	
class LicenceDurationForm(forms.ModelForm):
			
	class Meta:
		model = LicenceDuration
		fields = ['StartDate', 'EndDate', 'Price', 'MinimumBirthDate', 'MaximumBirthDate']
		
	def __init__(self, *args, **kwargs):
		super(LicenceDurationForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_id = 'id-LicenceDuration'
		self.helper.form_class = 'blueForms'
		self.helper.form_method = 'post'
		self.helper.form_action = 'submit_licence'
		self.helper.form_tag = False