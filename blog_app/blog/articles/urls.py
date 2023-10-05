
from django.contrib import admin
from django.urls import path
from . import views


app_name= "articles"
urlpatterns = [
    path("", views.article_list, name="article_list"),
    path("<int:article_id>/", views.article_detail, name="article_detail"),
    path("authors/", views.author_list, name="author_list"),
    path("authors/<int:author_id>/", views.author_detail, name="author_detail"),
]
