from django import forms
from .models import Number
from order.models import Bugs


class AddNumberForm(forms.ModelForm):
	mobile_number = forms.CharField(max_length=10, min_length=10)
	class Meta:
		model = Number
		fields = ['mobile_number']

class ReportBugForm(forms.ModelForm):
	
	class Meta:
		model = Bugs
		fields = ['bugs']
	def __init__(self, *args, **kwargs):
		super(ReportBugForm, self).__init__(*args, **kwargs) # Call to ModelForm constructor
		self.fields['bugs'].widget.attrs['cols'] = 5
		self.fields['bugs'].widget.attrs['rows'] = 5