from django.db import models
from datetime import datetime
from teams.models import Team, TeamScore
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime

# Create your models here.

class Game(models.Model):
	# t1Score = models.IntegerField(default=0)
	# t2Score = models.IntegerField(default=0)
	date = models.DateField(default=datetime.date.today)
	# teams = models.ManyToManyField(Team)
	homeTeam = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="home_team", null=True)
	# homeScore = models.ForeignKey(TeamScore, on_delete=models.CASCADE, related_name="home_team_score", null=True)
	homeScore = models.IntegerField(validators=[MinValueValidator(0)], default=0)
	visitingTeam = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="visiting_team", null=True)
	# visitingScore = models.ForeignKey(TeamScore, on_delete=models.CASCADE, related_name="visiting_team_score", null=True)
	visitingScore = models.IntegerField(validators=[MinValueValidator(0)], default=0)
  	#FIGURE OUT HOW TO COMPUTE WINNER!!!!

	# def __str__(self):
	# 	return ("%s vs. %s " % (self.teams.all()[0], self.teams.all()[1]))
	
	def __str__(self):
		return("%s %s vs. %s %s" % (self.homeTeam.city, self.homeTeam.name, 
			self.visitingTeam.city, self.visitingTeam.name))
