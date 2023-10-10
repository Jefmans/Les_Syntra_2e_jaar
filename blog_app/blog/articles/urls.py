
from django.contrib import admin
from django.urls import path
from . import views


app_name= "articles"
urlpatterns = [
    path("", views.article_list, name="article_list"),
    path("<int:article_id>/", views.article_detail, name="article_detail"),
    path("create/", views.article_create, name="article_create"),
    path("authors/", views.author_list, name="author_list"),
    path("authors/<int:author_id>/", views.author_detail, name="author_detail"),
    path("authors/<int:author_id>/articles/", views.articles_per_author_list, name ="articles_per_author_list"),
    path("authors/create/", views.author_create, name="author_create"),
]
