from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from persons.models import Person


# Create your models here.
class Player(models.Model):
    player = models.ForeignKey(Person, on_delete=models.CASCADE, unique=True)
    number = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(99)])
    weight = models.IntegerField(validators=[MinValueValidator(130), MaxValueValidator(500)])
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
    goals = models.IntegerField(validators=[MinValueValidator(0)])
    assist = models.IntegerField(validators=[MinValueValidator(0)])
    hits = models.IntegerField(validators=[MinValueValidator(0)])
    toi = models.CharField(max_length=15, default="")

    def __str__(self):
        return ("%s %s: %s" % (self.player.first_name, self.player.last_name, self.player.id))











