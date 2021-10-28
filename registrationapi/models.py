from django.db import models

# Create your models here.

#creating object
class UserRegistration(models.Model):
    first_name=models.CharField(max_length=10)
    last_name=models.CharField(max_length=10)
    username=models.CharField(max_length=20)
    email=models.TextField()
    password=models.TextField()
    confirmpassword=models.TextField()
    

    