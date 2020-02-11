# pylint: disable=unused-variable,unused-import
from django.apps import AppConfig


class AriadneExtensionsConfig(AppConfig):
    name = "ariadne_extensions"

    def ready(self):
        pass
