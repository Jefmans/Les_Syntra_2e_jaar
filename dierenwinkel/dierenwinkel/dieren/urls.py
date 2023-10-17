
from django.contrib import admin
from django.urls import path
from . import views

app_name ="dieren"
urlpatterns = [
    path("", views.dier_list, name="dier_list"),
    path("<int:dier_id>/", views.dier_detail, name='dier_detail'),
    path("create/", views.dier_create, name="dier_create"),
]
