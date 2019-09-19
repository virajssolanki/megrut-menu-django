from django import forms
from .models import Post, Msg


class AddMenuForm(forms.ModelForm):

	class Meta:
		model = Post
		fields = ['menu', 'price']
	def __init__(self, *args, **kwargs):
		super(AddMenuForm, self).__init__(*args, **kwargs) # Call to ModelForm constructor
		self.fields['menu'].widget.attrs['cols'] = 5
		self.fields['menu'].widget.attrs['rows'] = 5

class MsgForm(forms.ModelForm):

	class Meta:
		model = Msg
		fields = ['message', 'to']

	def __init__(self, *args, **kwargs):
		super(MsgForm, self).__init__(*args, **kwargs) # Call to ModelForm constructor
		self.fields['message'].widget.attrs['cols'] = 2
		self.fields['message'].widget.attrs['rows'] = 2