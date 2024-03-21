from django.urls import path
from . import views

app_name = "docs"
urlpatterns = [
    path('aa/', views.overview, name='overview'),
    path('upload_image/', views.upload_image, name='upload_image'),
    path('show_images/', views.show_images, name='show_images'),
    
    path('upload_doc/', views.upload_doc, name='upload_doc'),
    path('show_docs/', views.show_docs, name='show_docs'),
]
