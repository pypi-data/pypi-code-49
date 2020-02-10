#!/usr/bin/env python

import logging
import sys
from os.path import dirname

import django
from django.conf import settings
from django.test.runner import DiscoverRunner

sys.path.insert(0, dirname(__file__))

installed_apps = [
    "django.contrib.contenttypes",
    "django.contrib.auth",
    "django.contrib.sessions",
    "django.contrib.admin",
    "django.contrib.messages",
    "django_audit_events",
    "django_audit_events.tests",
    "django_audit_events.tests.utils",
]


class DisableMigrations:
    def __contains__(self, item):
        return True

    def __getitem__(self, item):
        return None


DEFAULT_SETTINGS = dict(
    ALLOWED_HOSTS=["localhost"],
    ROOT_URLCONF="django_audit_events.tests.urls",
    INSTALLED_APPS=installed_apps,
    DATABASES={
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": "postgres",
            "USER": "postgres",
            "PASSWORD": "",
            "HOST": "localhost",
            "PORT": "5432",
        },
        "other": {"ENGINE": "django.db.backends.sqlite3"},
    },
    MIGRATION_MODULES=DisableMigrations(),
    TEMPLATES=[
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "APP_DIRS": True,
            "OPTIONS": {
                "context_processors": [
                    "django.contrib.auth.context_processors.auth",
                    "django.contrib.messages.context_processors.messages",
                ]
            },
        }
    ],
)
MIDDLEWARE = [
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django_audit_events.middleware.AuditContextMiddleware",
]

if django.__version__ >= "2.0":
    DEFAULT_SETTINGS["MIDDLEWARE"] = MIDDLEWARE
else:
    DEFAULT_SETTINGS["MIDDLEWARE_CLASSES"] = MIDDLEWARE


def main():
    if not settings.configured:
        settings.configure(**DEFAULT_SETTINGS)
    django.setup()
    failures = DiscoverRunner(failfast=False).run_tests(["django_audit_events.tests"])
    sys.exit(failures)


if __name__ == "__main__":
    logging.basicConfig()
    main()
