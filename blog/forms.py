from django import forms
from .models import Post

PRICE_CHOICES = (
    ('40','40'),
    ('45', '45'),
    ('50','50'),
    ('55','55'),
    ('60','60'),
    ('70','70'),
    ('80','80'),
)

class AddMenuForm(forms.ModelForm):

	class Meta:
		model = Post
		fields = ['menu', 'price']
	def __init__(self, *args, **kwargs):
		super(AddMenuForm, self).__init__(*args, **kwargs) # Call to ModelForm constructor
		self.fields['menu'].widget.attrs['cols'] = 5
		self.fields['menu'].widget.attrs['rows'] = 5