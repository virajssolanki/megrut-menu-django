from django import forms
from .models import Post


class AddMenuForm(forms.ModelForm):

	class Meta:
		model = Post
		fields = ['menu', 'price']