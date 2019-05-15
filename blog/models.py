from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
	menu = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	price = models.CharField(max_length=3, default='40')
	active = models.BooleanField(default=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk': self.pk})