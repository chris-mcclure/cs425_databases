from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from persons.models import Person

# Create your models here.

class Coach(models.Model):
    coach = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="coach")
    COACH_CHOICES = [
        ('head coach', 'head coach'), ('assistant coach', 'assistant coach'),
    ]
    position = models.CharField(max_length=20, choices=COACH_CHOICES, default="")
   
    def __str__(self):
        return ("%s %s (%s)" % (self.coach.first_name, self.coach.last_name, self.position))