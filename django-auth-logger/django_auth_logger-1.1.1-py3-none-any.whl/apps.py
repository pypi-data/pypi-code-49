from django.apps import AppConfig


class AuthLoggerConfig(AppConfig):
    name = 'auth_logger'

    def ready(self):
        from .signals import handlers  # NOQA
