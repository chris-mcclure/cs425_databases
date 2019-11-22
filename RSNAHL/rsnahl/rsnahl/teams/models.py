from django.db import models

# Create your models here.

class Team(models.Model):
	city = models.CharField(max_length=100, default="")
	name = models.CharField(max_length=100, default="")
	slug = models.CharField(max_length=100, default="")
	DIVISION_CHOICES = [
		('good', 'good'), ('bad', 'bad'),
	]
	division = models.CharField(max_length=4, choices=DIVISION_CHOICES, default="")

	def __str__(self):
		return ("%s %s" % (self.city, self.name))