from django.urls import path
from . import views

app_name = "dynamic_model"
urlpatterns = [
    path('', views.test, name='test'),

]
