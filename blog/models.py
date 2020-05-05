from django.db import models

# Create your models here.
class Blog(models.Model):
	image = models.ImageField(upload_to = 'images/')
	title = models.CharField(max_length=250)
	pub_date = models.DateTimeField(max_length=200)
	body = models.TextField()
	
	def summary(self):
		return self.body[:40]+(self.body[40:] and '...')
	def pub_date_pretty(self):
		return self.pub_date.strftime('%b %e %Y')
	def __str__(self):
		return self.title 