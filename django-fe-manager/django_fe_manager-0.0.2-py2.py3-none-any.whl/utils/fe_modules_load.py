#!/usr/bin/env

'''
Reads corresponding settings and loads a list of front end modules and dependencies.
'''

from django.conf import settings


def fe_modules_load():
    return getattr(settings, 'FE_MANAGER', {})
