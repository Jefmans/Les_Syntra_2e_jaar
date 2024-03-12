from django.contrib import admin
from .models import Image, Document, Blog

# Register your models here.

admin.site.register(Image)
admin.site.register(Document)
admin.site.register(Blog)