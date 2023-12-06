from django.urls import path
from . import views

app_name = "scrapers"
urlpatterns = [
    path('', views.overview, name='overview'),
    path('scrape-immoweb/', views.scrape_immoweb, name='scrape_immoweb'),
    path('original-urls/', views.show_original_urls, name='original_urls'),
    path('cat-facts/', views.show_cat_facts, name='cat_facts'),
]
