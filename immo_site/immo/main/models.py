from django.db import models
from django.conf import settings

# Create your models here.


class Contact(models.Model):
    subject = models.CharField(max_length=100)
    message = models.TextField()
    sender = models.EmailField()
    cc_myself = models.BooleanField()


class Review(models.Model):
    subject = models.CharField(max_length=100)
    message = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    