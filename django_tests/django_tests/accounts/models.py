from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.conf import settings

# Create your models here.

class CustomUser(AbstractUser):
    is_active = models.BooleanField(default = True)


class Client(models.Model):
    user= models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    company = models.CharField(max_length= 30)

class Provider(models.Model):
    user= models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    company = models.CharField(max_length= 30)