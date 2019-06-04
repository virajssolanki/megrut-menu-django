from django import forms
from .models import Post


class AddMenuForm(forms.ModelForm):

	class Meta:
		model = Post
		fields = ['menu', 'price']
	def __init__(self, *args, **kwargs):
		super(AddMenuForm, self).__init__(*args, **kwargs) # Call to ModelForm constructor
		self.fields['menu'].widget.attrs['cols'] = 5
		self.fields['menu'].widget.attrs['rows'] = 5