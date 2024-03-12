from django.urls import path
from . import views

app_name = "front_end"
urlpatterns = [
    path('', views.overview, name='overview'),
    path('ocr/', views.tesseract_view, name='ocr'),
    path('data_test/', views.test_data_from_front_to_back, name='data_test'),
]
