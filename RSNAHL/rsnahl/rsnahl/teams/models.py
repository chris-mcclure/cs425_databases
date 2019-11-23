from django.db import models
from players.models import Player

# Create your models here.

class Team(models.Model):
	city = models.CharField(max_length=100, default="")
	name = models.CharField(max_length=100, default="")
	slug = models.CharField(max_length=100, default="")
	DIVISION_CHOICES = [
		('good', 'good'), ('bad', 'bad'),
	]
	division = models.CharField(max_length=4, choices=DIVISION_CHOICES, default="")
	players = models.ManyToManyField(Player)
	# coach = models.ForeignKey(Coach, on_delete=models.CASCADE, default=None, related_name="team_coach")
	# manager = models.ForeignKey(Manager, on_delete=models.CASCADE, default=None, related_name="team_manager")
	def __str__(self):
		return ("%s %s" % (self.city, self.name))


		