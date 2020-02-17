import importlib
import os
import sys
import inspect

import yaml

import unimatrix.const
import unimatrix.lib.environ
from unimatrix.ext.django.lib import etc


__all__ = []

assert 'UNIMATRIX_SETTINGS_MODULE' in os.environ


# Retrieve the current module from the sys.modules dictionary;
# we can then dynamically copy over settings from the real
# Django settings module.
self = sys.modules[__name__]
base_settings = importlib.import_module(os.environ['UNIMATRIX_SETTINGS_MODULE'])

# Iterate over all attributes in the original settings module
# and set them as attributes.
for attname, value in inspect.getmembers(base_settings):
    if attname == 'INSTALLED_APPS':
        value = tuple(['unimatrix.ext.django'] + list(value))
    setattr(self, attname, value)


# The following settings are hard-coded and needed for proper
# deployment on the Unimatrix platform.
from unimatrix.ext.django.settings.const import *


# Below members are operational configurations that are enforced
# by the Unimatrix platform. Since they are mandatory for deployment,
# we have the assignments raise an exception if the keys do
# not exist.
ALLOWED_HOSTS = unimatrix.lib.environ.parselist(os.environ,
    'HTTP_ALLOWED_HOSTS', sep=';')

API_BROWSER_ENABLED = os.getenv('API_BROWSER_ENABLED') == '1'

API_BROWSER_PATH = os.getenv('API_BROWSER_PATH') or 'browse/'

CSRF_COOKIE_DOMAIN = os.getenv('CSRF_COOKIE_DOMAIN')

CSRF_COOKIE_SECURE = True

DEBUG = os.getenv('DEBUG') == '1'

DATABASES = etc.load_databases(
    os.path.join(unimatrix.const.SECDIR, 'rdbms', 'connections'))

DEPLOYMENT_ENV = os.getenv('DEPLOYMENT_ENV') or 'testing'

ROOT_URLCONF = 'unimatrix.ext.django.urls.runtime'

SECRET_KEY = os.getenv('SECRET_KEY') or ('0' * 64)

SECURE_HSTS_SECONDS = 86400 * 365

SECURE_HSTS_PRELOAD = True

SESSION_COOKIE_DOMAIN = os.getenv('SESSION_COOKIE_DOMAIN')

SESSION_COOKIE_SECURE = True

SESSION_COOKIE_HTTPONLY = True

SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
if os.getenv('SESSIONS_PERSISTENT') == '1':
    raise NotImplementedError

STATIC_SERVE = os.getenv('STATIC_SERVE') == '1'

STATIC_URL = os.getenv('STATIC_URL') or '/assets/'
if not str.endswith(STATIC_URL, '/'):
    STATIC_URL = STATIC_URL + '/'


# We check here if DEBUG is True and the SECRET_KEY consist
# of all zeroes, to prevent insecure keys getting deployed
# in a production environment.
if (not DEBUG and SECRET_KEY == ('0' * 64))\
and (DEPLOYMENT_ENV != 'build'):
    raise RuntimeError("Insecure SECRET_KEY configured.")
