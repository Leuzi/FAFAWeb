from crispy_forms.helper import FormHelper
from crispy_forms.layout import  Layout, Fieldset, ButtonHolder,Field
from django import forms
from .models import *

class LicenceTypeForm(forms.ModelForm):	
	
	def __init__(self, *args, **kwargs):
		super(LicenceTypeForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper(self)
		self.helper.form_tag = False
		self.helper.layout = Layout(
            Fieldset(
                'Tipo de Licencia',
                'Name',
                'Shortening',
                Field('Region', type="hidden")
            )
        )
	
	class Meta:
		model = LicenceType
		fields = ['Name', 'Shortening', 'Region']
		
	
class LicenceDurationForm(forms.ModelForm):
			
	class Meta:
		model = LicenceDuration
		fields = ['StartDate', 'EndDate', 'Price', 'MinimumBirthDate', 'MaximumBirthDate']
		
	def __init__(self, *args, **kwargs):
		super(LicenceDurationForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_tag = False
		self.helper.layout = Layout(
            Fieldset(
                'Características',
                Field('StartDate', css_id="datepicker"),
                'EndDate',
                'Price',
                'MinimumBirthDate',
                'MaximumBirthDate'
            )
        )
