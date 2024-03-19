from django.urls import path
from . import views

app_name = "lang"
urlpatterns = [
    path('show_language/', views.show_language, name='show_language'),
    path('set_language/', views.set_language, name='set_language'),

]
