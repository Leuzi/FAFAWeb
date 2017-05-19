from django import forms
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, ButtonHolder
from crispy_forms.bootstrap import FormActions

class PlayerForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(PlayerForm, self).__init__(*args, **kwargs)

		# If you pass FormHelper constructor a form instance
		# It builds a default layout with all its fields
		self.helper = FormHelper(self)
		self.helper.form_method = 'post'
		self.helper.form_action = 'submit_player'
		self.helper.add_input(Submit('submit', 'Submit'))
			
	class Meta:
		model = Player
		fields = ['DNI', 'Name', 'Surname','BirthDate','Country','ZIPCode','City','Region','Phone','Mail','Photo']