from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.

# class Client(AbstractUser):

#     def __str__(self):
#         return self.username
    

# class CornerstoneUser(AbstractUser):
#     pass

class CustomUser(AbstractUser):
    active = models.BooleanField()