from django.urls import path
from . import views

app_name = "scrapers"
urlpatterns = [
    path('', views.overview, name='overview'),
    path('scrape_immoweb/', views.scrape_immoweb, name='scrape_immoweb'),
    path('original_urls/', views.show_original_urls, name='original_urls'),
]
