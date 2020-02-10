from django.apps import AppConfig


class HoLoggerConfig(AppConfig):
    name = "hologger"

    def ready(self):
        from . import signal
        from . import handlers
