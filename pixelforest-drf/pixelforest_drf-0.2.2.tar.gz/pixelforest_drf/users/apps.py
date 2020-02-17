from django.apps import AppConfig


class IamConfig(AppConfig):
    name = 'users'

    # noinspection PyUnresolvedReferences
    def ready(self):
        import users.handlers
