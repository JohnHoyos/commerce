from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listing(models.Model):
    title : models.CharField(max_length=64)
    description: models.CharField(max_length=64)
    currentprice: models.IntegerField()
    category : models.CharField(max_length=64)
    photourl : models.CharField(max_length=64)
