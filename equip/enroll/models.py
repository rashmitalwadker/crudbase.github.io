from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=25)
    price = models.BigIntegerField(max_length=10)
    warrenty = models.BooleanField(max_length=1)