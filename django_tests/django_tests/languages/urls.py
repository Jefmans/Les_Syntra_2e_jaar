from django.urls import path
from . import views

app_name = "lang"
urlpatterns = [
    path('show_language/', views.show_language, name='show_language'),
    path('settings_language/', views.settings_language, name='settings_language'),

]
