from django.urls import path
from . import views

app_name = "docs"
urlpatterns = [
    path('', views.overview, name='overview'),
    path('upload_image/', views.upload_image, name='upload_image'),
    path('show_images/', views.show_images, name='show_images'),
]
