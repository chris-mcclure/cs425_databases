from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from persons.models import Person

# Create your models here.

class Manager(models.Model):
    manager = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="manager", unique=True)
    
    def __str__(self):
        return ("%s %s" % (self.manager.first_name, self.manager.last_name))