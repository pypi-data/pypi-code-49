"""Constants used in the Unimatrix One/CM platforms,
for deployments for Django.
"""
import os


DEFAULT_LOG_LEVEL = 'ERROR'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
        'null': {
            'class': 'logging.NullHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', DEFAULT_LOG_LEVEL),
        },
        'django.db.backends': {
            'handlers': ['null'],
            'propagate': False,
        },
        'proton': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', DEFAULT_LOG_LEVEL),
        },
        'aorta': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', DEFAULT_LOG_LEVEL),
        },
        'drone': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', DEFAULT_LOG_LEVEL),
        },
    },
}

SESSIONS_PERSISTENT = os.getenv('SESSIONS_PERSISTENT') == '1'

STATICFILES_DIRS = ['dist/assets']

STATIC_ROOT = 'static'
