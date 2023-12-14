from django.db import models

# Create your models here.


class Contact(models.Model):
    subject = models.CharField(max_length=100)
    message = models.TextField()
    sender = models.EmailField()
    cc_myself = models.BooleanField()