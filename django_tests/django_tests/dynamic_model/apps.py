from django.apps import AppConfig


class DynamicModelConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dynamic_model'
