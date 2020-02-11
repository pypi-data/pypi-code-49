from django.apps import AppConfig
from django.db.models.signals import post_migrate


class DjangoPressConfig(AppConfig):
    name = 'django_press'

    def ready(self):
        from django_press.models.initialize import create_initial_context, create_initial_pages, create_super_user
    #     post_migrate.connect(create_initial_pages, self)
        post_migrate.connect(create_initial_context, self)
    #     post_migrate.connect(create_super_user, self)
