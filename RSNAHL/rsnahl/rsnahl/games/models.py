from django.db import models
from teams.models import Team
import datetime

# Create your models here.

class Game(models.Model):
	t1Score = models.IntegerField(default=0)
	t2Score = models.IntegerField(default=0)
	date = models.DateField()
	teams = models.ManyToManyField(Team)

  	#FIGURE OUT HOW TO COMPUTE WINNER!!!!

	def __str__(self):

		return ("%s vs. %s " % (self.teams.all()[0], self.teams.all()[1]))
