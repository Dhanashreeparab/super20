from datetime import datetime, date
from django.db import models

# Create your models here.
class Register(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone  = models.CharField(max_length=12)
    address = models.TextField()
    qualification = models.CharField(max_length=150)
    college = models.CharField(max_length=200)
    message = models.TextField()
    date = models.DateField()

    def __str__(self):
        return 'Message from' + ' ' +  self.name


class Feedback(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone  = models.CharField(max_length=12)
    message = models.TextField() 
    date = models.DateField()

    def __str__(self):
        return 'Message from' + ' ' +  self.name