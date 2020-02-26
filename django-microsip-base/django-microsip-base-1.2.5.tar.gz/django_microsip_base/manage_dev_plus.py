#!/usr/bin/env python
import os
import sys


def add_debug_apps():

    """
        Para que se pueda estar depurando una aplicacion
        sin instalar la aplicacion realmente app como microsip_api.
    """
    REPOSITORIES_PATH = str(os.path.abspath(__file__ + "/../../../"))

    # ADD API
    new_path = "{}\{}".format(REPOSITORIES_PATH, 'django-microsip-api')
    print new_path
    sys.path.append(new_path)

    # ADD APPS
    DJMICROSIP_APPS = str(os.path.join(REPOSITORIES_PATH, 'djmicrosip_apps'))
    debug_apps = []
    #obtenemos las carpetas que esten en DJMICROSIP_APPS
    debug_apps = os.listdir(DJMICROSIP_APPS)
    for debug_app in debug_apps:
        new_path = "{}\{}".format(DJMICROSIP_APPS, debug_app)
        sys.path.append(new_path)

# Para poder depurar aplicaciones sin isntalar
add_debug_apps()

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_microsip_base.settings.dev_plus")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
