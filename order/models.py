from django.db import models
from django.utils import timezone

class Number(models.Model):
	date_posted = models.DateTimeField(default=timezone.now)
	number = models.CharField(max_length=10, blank=True)

	def __str__(self):
		return self.number