import sys
import tempfile
from aristotle_mdr.required_settings import *
import os

BASE = os.path.join(os.path.dirname(os.path.dirname(__file__)), '..')

sys.path.insert(1, BASE)
sys.path.insert(1, os.path.join(BASE, "tests"))
sys.path.insert(1, os.path.join(BASE, "tests/apps"))

TEMPLATES[0]['DIRS'] = [
    os.path.join(BASE, 'tests/apps/bulk_actions_test/templates')
]
TEMPLATES[0]['OPTIONS']['debug'] = True  # This makes sure template exceptions are not squashed

SECRET_KEY = 'inara+oscar+vtkprm7@0(fsc$+grbz9-s+tmo9d)e#k(9uf8m281&$7xhdkjr'

# We set this up so we can point wcag_zoo in the right place
BASE_STATICPATH = tempfile.mkdtemp(suffix='_staticfiles')

STATIC_ROOT = BASE_STATICPATH + STATIC_URL
if not os.path.exists(STATIC_ROOT):
    os.makedirs(STATIC_ROOT)

MEDIA_ROOT = os.path.join(BASE, "media")
MEDIA_URL = '/media/'
CKEDITOR_UPLOAD_PATH = 'uploads/'

skip_migrations = ("ARISTOTLE_DEV_SKIP_MIGRATIONS" in os.environ)

ARISTOTLE_ASYNC_SIGNALS = False

print("Running test-suite with connection string %s" % os.environ.get('DATABASE_URL'))

if skip_migrations:  # pragma: no cover
    print("Skipping migrations")


    class DisableMigrations(object):

        def __contains__(self, item):
            return True

        def __getitem__(self, item):
            return None


    MIGRATION_MODULES = DisableMigrations()


if os.environ.get('SEARCH') == 'whoosh':
    print("Running test-suite with whoosh")
    HAYSTACK_CONNECTIONS = {
        'default': {
            'ENGINE': 'aristotle_mdr.contrib.search_backends.facetted_whoosh.FixedWhooshEngine',
            'PATH': os.environ.get('WHOOSH_PATH', tempfile.mkdtemp()),
            'INCLUDE_SPELLING': True,
        },
    }
else:
    print("Running test-suite with elasticsearch")
    HAYSTACK_CONNECTIONS = {
        'default': {
            'ENGINE': 'haystack_elasticsearch.elasticsearch5.Elasticsearch5SearchEngine',
            'URL': os.environ.get('ELASTICSEARCH_URL', 'http://localhost:9200'),
            'INDEX_NAME': 'test_index',
            'INCLUDE_SPELLING': True,
            'KWARGS': {
                'http_auth': 'elastic:changeme'
            }
        }
    }


INSTALLED_APPS = (
    'aristotle_glossary',
    'extension_test',
    'aristotle_dse',
    'comet',
) + INSTALLED_APPS

# We do a lot of user login in testing, so switching to a faster password hasher will
# speed things up.
# For more context:
# https://docs.djangoproject.com/en/3.0/topics/testing/overview/#speeding-up-the-tests
PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.MD5PasswordHasher',
)

ARISTOTLE_SETTINGS = ARISTOTLE_SETTINGS.copy()

ARISTOTLE_SETTINGS['SEPARATORS']['DataElementConcept'] = '--'
ARISTOTLE_SETTINGS['CONTENT_EXTENSIONS'] = ARISTOTLE_SETTINGS['CONTENT_EXTENSIONS'] + [
    'extension_test', 'aristotle_mdr_links', 'aristotle_mdr_backwards'
]
ARISTOTLE_SETTINGS['BULK_ACTIONS'] = ARISTOTLE_SETTINGS['BULK_ACTIONS'] + [
    'bulk_actions_test.actions.StaffDeleteActionForm',
    'bulk_actions_test.actions.IncompleteActionForm',
    'aristotle_mdr.contrib.slots.forms.BulkAssignSlotsForm',
]
ROOT_URLCONF = 'extension_test.urls'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
    }
}

# disable
LOGGING = {
    'version': 1,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(name)s: %(levelname)s %(message)s'
        }
    },
    'handlers': {
        'console-simple': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'aristotle_mdr': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['console-simple'],
            'level': 'CRITICAL'
        },
        'django': {
            'handlers': ['console-simple'],
            'level': 'INFO',
            'propagate': True,
        }
    }
}

# Webpack Loading
WEBPACK_LOADER['DEFAULT']['STATS_FILE'] = os.path.join(REPO_BASE_DIR, 'assets/dist/webpack-stats.json')
WEBPACK_LOADER['DEFAULT']['CACHE'] = False

DATA_UPLOAD_MAX_NUMBER_FIELDS = 20000

# Allows migrations to print text on success (disabled during testing)
MIGRATION_PRINT = False

# This makes tasks functions be called directly
# This is not ideal as serialization is not tested
# More info here http://docs.celeryproject.org/en/latest/userguide/testing.html
CELERY_TASK_ALWAYS_EAGER = True
