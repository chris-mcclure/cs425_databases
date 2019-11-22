from django.db import models
from django.urls import reverse


# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=64, default="")
    middle_initial = models.CharField(max_length=1, default="")
    last_name = models.CharField(max_length=64, default="")
    dob = models.DateField()
    pob = models.CharField(max_length=200, default="")
    def __str__(self):
        return self.first_name + " " + self.middle_initial + " " + self.last_name