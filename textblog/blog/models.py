from django.db import models

class Book(models.Model):

	name = models.CharField(max_length=30000)
	url = models.CharField(max_length=30000)

	def __unicode__(self):
		return self.name
