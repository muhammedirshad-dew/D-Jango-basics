from django.apps import AppConfig


class AdminConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'admin'
    # The default label would be 'admin' which conflicts with
    # Django's built-in 'django.contrib.admin' app. Set a unique
    # label so both can coexist.
    label = 'custom_admin'
