# tutorial/models.py
from django.contrib.auth import get_user_model
from django.db import models
import django_filters

class Person(models.Model):
    name = models.CharField(max_length=200,verbose_name="First Name")
    surname = models.CharField(max_length=200, verbose_name="Last Name")
    posit = models.CharField(max_length=200, verbose_name="Position")
    university=models.CharField(max_length=200, verbose_name="University")
    


