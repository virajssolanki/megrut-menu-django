from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
#from PIL import Image 

CITY_CHOICES = (
    ('VADODARA','VADODARA'),
    ('AHEMDAVAD', 'AHEMDAVAD'),
    ('VIDHYANAGAR','VIDHYANAGAR'),
)

PIN_CHOICES = (
    ('390002','Fateganj'),
    ('390024', 'Nizampura'),
)

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='default.jpg', upload_to='profile_pics')
	mess_name = models.CharField(max_length=30, blank=True)
	area = models.CharField(max_length=40,choices=PIN_CHOICES, default='Fateganj')
	number = models.CharField(max_length=10, blank=True)
	location = models.URLField(max_length=300, blank=True)
	city = models.CharField(max_length=40,choices=CITY_CHOICES, default='VADODARA')
	close = models.BooleanField(default=False)

	def __str__(self):
		return f'{self.user.username} Profile'

#	def save(self, *args, **kwrgs ):
#		super().save(*args, **kwrgs)

#		img = Image.open(self.image.path)
#		if img.height > 300 or img.width > 300:
#			output_size = (300, 300)
#			img.thumbnail(output_size)
#			img.save(self.image.path)