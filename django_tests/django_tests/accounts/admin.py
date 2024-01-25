from django.contrib import admin
from .models import Client, Provider, CustomUser
from django.contrib.auth.admin import UserAdmin



# Register your models here.

admin.site.register(Client)
admin.site.register(Provider)
admin.site.register(CustomUser,UserAdmin )