import logging

import connexion

import connexion_buzz

import sentry_sdk
from sentry_sdk.integrations.celery import CeleryIntegration
from sentry_sdk.integrations.flask import FlaskIntegration

from . import settings, VERSION
from .extensions import celery, clickhouse

__all__ = ["create_celery", "create_app"]

logging.basicConfig(level=logging.INFO)


def create_celery(app, settings_override=None):
    if settings_override:
        app.config.update(settings_override)

    celery.config_from_object(app.config, namespace="CELERY")

    TaskBase = celery.Task

    class ContextTask(TaskBase):  # noqa
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery.Task = ContextTask

    return celery


def create_app(settings_override=None):
    app = connexion.App(__name__, specification_dir="./spec/", options={"swagger_ui": False}, debug=settings.DEBUG)
    app.add_api("openapi.yaml", arguments={"title": "AFFO Event API"})
    app.app.register_error_handler(connexion_buzz.ConnexionBuzz, connexion_buzz.ConnexionBuzz.build_error_handler())

    application = app.app
    application.config.from_object(settings)

    if settings_override:
        application.config.update(settings_override)

    # Initialize extensions/add-ons/plugins.
    clickhouse.init_app(application)

    sentry_sdk.init(
        integrations=[CeleryIntegration(), FlaskIntegration()],
        dsn=application.config.get("SENTRY_DSN"),
        environment=application.config.get("ENV"),
        release=VERSION,
    )

    return application
