from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


PRICE_CHOICES = (
    ('₹ 40','₹ 40'),
    ('₹ 45', '₹ 45'),
    ('₹ 50','₹ 50'),
    ('₹ 55','₹ 55'),
    ('₹ 60','₹ 60'),
    ('₹ 70','₹ 70'),
    ('₹ 80','₹ 80'),
    ('₹ 90','₹ 90'),
    ('*','*'),
)

class Post(models.Model):
	menu = models.TextField(max_length=150)
	date_posted = models.DateTimeField(default=timezone.now)
	session = models.CharField(max_length=10, blank=True)
	price = models.CharField(max_length=5,choices=PRICE_CHOICES, default='40')
	active = models.BooleanField(default=True)
	city = models.CharField(max_length=40,default='VADODARA')
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.menu

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk': self.pk})