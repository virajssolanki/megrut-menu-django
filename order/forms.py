from django import forms
from .models import Number


class AddNumberForm(forms.ModelForm):
	number = forms.CharField(max_length=10, min_length=10)
	class Meta:
		model = Number
		fields = ['number']