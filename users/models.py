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
	('Fateganj','Fateganj'),
	('Nizampura', 'Nizampura'),
	('Waghodia road', 'Waghodia road'),
	('MS campus', 'MS campus'),
	('Sama', 'Sama'),
	('Amitnagar', 'Amitnagar'),
	('MS girls campus', 'MS girls campus'),
)

ZONE_CHOICES = (
	('zone-1','zone-1'),
	('zone-2', 'zone-2'),
	('zone-3','zone-3'),
)

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='default.jpg', upload_to='profile_pics')
	mess_name = models.CharField(max_length=30, blank=True)
	area = models.CharField(max_length=40,choices=PIN_CHOICES, default='Fateganj')
	number = models.CharField(max_length=10, blank=True)
	location = models.URLField(max_length=300, blank=True)
	city = models.CharField(max_length=40,choices=CITY_CHOICES, default='VADODARA')
	zone = models.CharField(max_length=40,choices=ZONE_CHOICES, default='zone-1')
	close = models.BooleanField(default=False)
	follower = models.IntegerField(default=0)
	verified = models.BooleanField(default=False)
	profile_comp = models.BooleanField(default=False)

	def __str__(self):
		return f'{self.user.username} Profile'

#	def save(self, *args, **kwrgs ):
#		super().save(*args, **kwrgs)

#		img = Image.open(self.image.path)
#		if img.height > 300 or img.width > 300:
#			output_size = (300, 300)
#			img.thumbnail(output_size)
#			img.save(self.image.path)