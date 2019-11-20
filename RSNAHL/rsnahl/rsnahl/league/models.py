from django.db import models
from django.urls import reverse

class Person(models.Model):
    first_name = models.CharField(max_length=64, default="")
    middle_initial = models.CharField(max_length=1, default='')
    last_name = models.CharField(max_length=64, default="")
    ssn = models.IntegerField(default=0)
    dob = models.DateField()
    pob = models.CharField(max_length=200, default="")

    def __str__(self):
        self.first_name + " " + self.middle_initial + " " + self.last_name

class Player(models.Model):
    first_name = Person.first_name
    middle_initial = Person.middle_initial
    last_name = Person.last_name
    ssn = Person.ssn
    dob = Person.dob
    pob = Person.pob
    number = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)
    height = models.CharField(max_length=10, default="")
    position = models.CharField(max_length=20, default="") #should consist of "left" and "right"
    stick_orientation = models.CharField(max_length=5, default="")



class Team(models.Model):
    name = models.CharField(max_length=64, default="")
    city = models.CharField(max_length=64, default="")
    division = models.CharField(max_length=64, default="") #should only be a couple of divisions, need to create divisions

    def __str__(self):
        return ("%s %s" % (self.city, self.name))

class Coach(models.Model):
    first_name = Person.first_name
    middle_initial = Person.middle_initial
    last_name = Person.last_name
    ssn = Person.ssn
    dob = Person.dob
    pob = Person.pob

class Manager(models.Model):
    first_name = Person.first_name
    middle_initial = Person.middle_initial
    last_name = Person.last_name
    ssn = Person.ssn
    dob = Person.dob
    pob = Person.pob

class Referee(models.Model):
    first_name = Person.first_name
    middle_initial = Person.middle_initial
    last_name = Person.last_name
    ssn = Person.ssn
    dob = Person.dob
    pob = Person.pob