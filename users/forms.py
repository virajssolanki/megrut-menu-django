from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
		widgets = {
			'username' : forms.TextInput(attrs = {'placeholder': 'create username or mobile number'}),
			}

class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
	location = forms.URLField(required=True)
	close = forms.BooleanField(required=False)
	mess_name = forms.CharField(required=True)
	number = forms.CharField(required=True)

	class Meta:
		model = Profile
		fields = ['location', 'close', 'mess_name', 'city', 'area', 'number', 'zone']

	def __init__(self, *args, **kwargs):
		super(ProfileUpdateForm, self).__init__(*args, **kwargs) # Call to ModelForm constructor
		self.fields['city'].widget.attrs['cols'] = 5
		self.fields['city'].widget.attrs['rows'] = 5