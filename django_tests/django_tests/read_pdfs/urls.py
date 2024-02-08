from django.urls import path
from . import views

app_name = "front_end"
urlpatterns = [
    path('pdf', views.read_pdf, name='read_pdf'),
    path('xbrl', views.read_xbrl, name='read_xbrl'),
]
