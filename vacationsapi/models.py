from django.contrib import admin
from django.db import models

from django.db import models
# Create your models here.
class Vacations(models.Model):

    place=models.CharField(max_length=10)
    image=models.ImageField(upload_to='pics')
    price=models.CharField(max_length=7)
    travel=models.BooleanField()
    food=models.BooleanField()
    accomodation=models.BooleanField()
    