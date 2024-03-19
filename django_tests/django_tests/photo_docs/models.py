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


from django.utils.text import slugify
class Blog(models.Model):
    title = models.CharField(max_length=50)
    url = models.URLField(unique=True, blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.title}  -  {self.url}'

    def save(self, *args, **kwargs):
        if not self.pk:
            url = slugify(self.title)
            self.url = url
            unique_url = self.create_unique_url(url)
            # print('unique_url : ', unique_url)
            self.url = unique_url
            super(Blog, self).save(*args, **kwargs)
        
    def create_unique_url(self, url, counter=0):
        # print(url, counter)
        if self.url_exists(url):
            # print('---1---')
            counter += 1
            new_url = self.url + f'_{counter}'
            return self.create_unique_url(new_url, counter)
        else:
            print(url)
            return url

        
    def url_exists(self, new_url):
        try:
            Blog.objects.get(url = new_url)
            return True
        except:
            return False




        