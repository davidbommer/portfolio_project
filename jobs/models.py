from django.db import models
import django.utils

# Create your models here.
class Job(models.Model): 
	image = models.ImageField(upload_to = 'images/')
	text = models.TextField(max_length=200)
	title = models.CharField(max_length=250, default='default title')
	pub_date = models.DateTimeField(max_length=200, default= django.utils.timezone.now)

	def __str__(self):
		return self.title

	def pub_date_pretty(self):
		return self.pub_date.strftime('%b %e, %Y')

