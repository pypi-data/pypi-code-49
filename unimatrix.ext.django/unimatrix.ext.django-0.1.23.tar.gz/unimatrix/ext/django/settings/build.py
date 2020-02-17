"""Django settings used during a container build; used
mainly to support ``collectstatic``.
"""
from unimatrix.ext.django.settings.const import *

DEBUG = False

INSTALLED_APPS = [
    'django.contrib.staticfiles'
]

SECRET_KEY = ('0' * 32)

STATIC_URL = '/assets/'
