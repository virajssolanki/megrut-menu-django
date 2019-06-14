from django import forms
from .models import Number


class AddNumberForm(forms.ModelForm):
	
	class Meta:
		model = Number
		fields = ['number']