"""
Start a django server from command line,
this module is not intended to use for production deployment.
"""
import os
from . import views


def run(sub_source, sub_content, purls):
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'submix.settings')
    argv = ['manage.py', 'runserver']
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(argv)
