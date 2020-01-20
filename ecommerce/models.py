from django.conf import settings
from django.db import models
from django.utils import timezone


# Create your models here.
class Customer(models.Model):
    cus_user=models.CharField(max_length=200)
    user = models.CharField(max_length=200)
    password= models.TextField()


