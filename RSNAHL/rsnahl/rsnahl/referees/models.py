from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from persons.models import Person

# Create your models here.

class Referee(models.Model):
    referee = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="referee")

    def __str__(self):
        return ("%s %s" % (self.referee.first_name, self.referee.last_name))