from django import forms
from .models import Post


class AddMenuForm(forms.ModelForm):

	class Meta:
		model = Post
		fields = ['menu', 'price']

		def __init__(self, *args, **kwargs):
			super(ProductForm, self).__init__(*args, **kwargs)
			self.fields['description'].widget.attrs={ 'id': 'autocomplete'}