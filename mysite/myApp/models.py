from django.db import models

# Create your models here.
from django.db import models


class NewDog(models.Model):
    name = models.CharField(max_length=200)
    breed = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)


class Account(models.Model):
    username = models.CharField(max_length=200)
    realName = models.CharField(max_length=200)
    accountNumber = models.DecimalField(max_digits=20,decimal_places=0)
    balance = models.DecimalField(max_digits=10,decimal_places=4)