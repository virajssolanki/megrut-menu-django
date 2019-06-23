from django.db import models
from django.utils import timezone

class Number(models.Model):
	date_posted = models.DateTimeField(default=timezone.now)
	number = models.CharField(max_length=10, default='7046717674')

	def __str__(self):
		return self.number

class Bugs(models.Model):
	date_posted = models.DateTimeField(default=timezone.now)
	bugs = models.TextField(max_length=150)

	def __str__(self):
		return self.bugs