from django.db import models

# Create your models here.

class ImmoWebData(models.Model):
    original_url = models.URLField()