from django.db import models
import datetime
from accounts.models import Client
from django.conf import settings
import os
# Create your models here.

def create_upload_string(instance, file_name):
    today = datetime.date.today()
    day_string = f'uploads/{today.year}_{today.month}_{today.day}/{file_name}'
    return day_string

class Image(models.Model):
    file = models.ImageField(upload_to=create_upload_string)
    file_name = models.CharField(max_length = 50)   

    def save(self, *args, **kwargs):
        if self.file:
            self.file_name = os.path.basename(self.file.name)
        super(Image, self).save(*args, **kwargs)

class Document(models.Model):
    file = models.FileField(upload_to=create_upload_string)
    file_name = models.CharField(max_length = 50)

    def save(self, *args, **kwargs):
        if self.file:
            self.file_name = os.path.basename(self.file.name)
        super(Document, self).save(*args, **kwargs)