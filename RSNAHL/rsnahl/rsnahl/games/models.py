from django.db import models
from teams.models import Team

# Create your models here.

class Game(models.Model):
	t1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="t1")
	t1Score = models.IntegerField(default=0)
	t2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="t2")
	t2Score = models.IntegerField(default=0)
	date = models.DateField()

	def __str__(self):
		return ("%s vs. %s" % (self.t1.name, self.t2.name))


#finish winner!!!
class Winner(models.Model):
	winner = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="winner")