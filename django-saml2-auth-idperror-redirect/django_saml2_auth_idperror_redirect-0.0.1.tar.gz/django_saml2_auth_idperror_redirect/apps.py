from django import apps


class AppConfig(apps.AppConfig):
    name = 'django_saml2_auth_idperror_redirect'

    def ready(self):
        # import plugins
        # noinspection PyUnresolvedReferences
        from . import plugins
