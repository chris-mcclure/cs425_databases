import datetime
from django.db import models
from django.urls import reverse


class Person(models.Model):
    first_name = models.CharField(max_length=64, default="")
    middle_initial = models.CharField(max_length=1, default="")
    last_name = models.CharField(max_length=64, default="")
    ssn = models.IntegerField(default=0)
    dob = models.DateField()
    pob = models.CharField(max_length=200, default="")

    def __str__(self):
        return self.first_name + " " + self.middle_initial + " " + self.last_name

class Player(models.Model):
    player = models.ForeignKey(Person, on_delete=models.CASCADE)
    number = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)
    height = models.CharField(max_length=10, default="")
    POSITION_CHOICES = [
        ('Forward', (
                ('C', 'Center'),
                ('RW', 'Right Wing'),
                ('LW', 'Left Wing'),
            )
        ),
        ('Defense', (
                ('RD', 'Right Defense'),
                ('LD', 'Left Defense'),
            )
        ),
        ('Goalie', 'Goalie'),
    ]
    # position = models.CharField(max_length=20, default="") #should consist of "left" and "right"
    position = models.CharField(max_length=20, choices=POSITION_CHOICES, default='')

    ORIENTATION_CHOICES = [
        ('Right', 'Right'), ('Left', 'Left'),
    ]
    stick_orientation = models.CharField(max_length=5, choices=ORIENTATION_CHOICES, default='')

    def __str__(self):
        return ("%s %s" % (self.player.first_name, self.player.last_name))


class Team(models.Model):
    name = models.CharField(max_length=64, default="")
    city = models.CharField(max_length=64, default="")
    division = models.CharField(max_length=64, default="") #should only be a couple of divisions, need to create divisions

    def __str__(self):
        return ("%s %s" % (self.city, self.name))

class Coach(models.Model):
    coach = models.ForeignKey(Person, null=True, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, null =True, on_delete=models.CASCADE)
    head = models.BooleanField(default=False)

    def __str__(self):
        return ("%s %s" % (self.coach.first_name, self.coach.last_name))

class Manager(models.Model):
    manager = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return ("%s %s" % (self.manager.first_name, self.manager.last_name))

class Referee(models.Model):
    referee = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return ("%s %s" % (self.referee.first_name, self.referee.last_name))

# class Winner(models.Model):
#     goals = models.IntegerField(default=0)
    
class Game(models.Model):
    team1 = models.ForeignKey(Team, related_name="team_1", on_delete=models.CASCADE)
    team2 = models.ForeignKey(Team, related_name="team_2", on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today)
    # winning_team = models.ForeignKey(Team, related_name="winner", on_delete=models.CASCADE)
    def __str__(self):
        return("%s vs. %s" % (self.team1.name, self.team2.name))

