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

class MyData(models.Model):
    image = models.ImageField(upload_to=create_upload_string)
    file_name = models.CharField(max_length = 50)
    
    # file = models.FileField()
    # owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    # owner = models.ForeignKey(Client)
    

    def save(self, *args, **kwargs):
        if self.image:
            self.file_name = os.path.basename(self.image.name)
        super(MyData, self).save(*args, **kwargs)