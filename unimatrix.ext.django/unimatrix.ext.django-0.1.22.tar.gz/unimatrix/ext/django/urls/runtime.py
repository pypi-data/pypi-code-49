import importlib
import os
import sys
import inspect

import django.views.static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from django.urls import include


urlpatterns = []
if getattr(settings, 'STATIC_SERVE', False):
    # We assume here that the django.contrib.staticfiles app is enabled
    # and that STATIC_URL is a relative path. TODO: implement checks.
    urlpatterns += staticfiles_urlpatterns()


# Provide a configuration to enable or disable the
# Django Rest Framework API browser.
if getattr(settings, 'API_BROWSER_ENABLED', False)\
and 'rest_framework' in settings.INSTALLED_APPS:
    urlpatterns += [
        path(getattr(settings, 'API_BROWSER_PATH', 'browse/'),
            include('rest_framework.urls'))
    ]

# Since we use unimatrix.ext.django.settings.runtime,
# we know that 1) UNIMATRIX_SETTINGS_MODULE is defined
# in the environment and 2) we imported it succesfully.
# No need to perform any checks here.
base_settings = importlib.import_module(
    os.environ['UNIMATRIX_SETTINGS_MODULE'])

module_name = os.environ.get('UNIMATRIX_URLS_MODULE')\
    or base_settings.ROOT_URLCONF
if module_name:
    urls = importlib.import_module(module_name)
    if not hasattr(urls, 'urlpatterns'):
        raise ValueError(
            "%s must declare urlpatterns" % os.environ['UNIMATRIX_SETTINGS_MODULE'])

    urlpatterns.extend(urls.urlpatterns)

    # Check if error code handlers are present.
    if hasattr(urls, 'handler400'):
        handler400 = urls.handler400
    if hasattr(urls, 'handler403'):
        handler403 = urls.handler403
    if hasattr(urls, 'handler404'):
        handler404 = urls.handler404
    if hasattr(urls, 'handler500'):
        handler500 = urls.handler500
