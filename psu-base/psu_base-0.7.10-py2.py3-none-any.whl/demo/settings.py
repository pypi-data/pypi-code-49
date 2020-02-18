"""
Django settings for demo project.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""
import os
import psu_base
from django.contrib.messages import constants as messages

# For encrypting/decrypting setting values (requires PSU Key file, otherwise returns NULL values)
from psu_base.classes.Encryptor import Encryptor
encryptor = Encryptor()

# -------------------------------------------------------------------------
# Application Metadata
# -------------------------------------------------------------------------
# The current version of the DEMO application
APP_VERSION = '0.1.0'

# App identifiers
APP_CODE = 'DEMO'.upper()   # Used for database lookups
APP_NAME = 'The Demo Site'  # Displayed in some generic UI scenarios

# On-premises apps will have additional "context" appended to the URL
#   i.e. https://app.banner.pdx.edu/demo/index
# AWS apps will not have this (set to None)
URL_CONTEXT = 'demo'

# I needed this in APC, but it causes issues in demo.
# APPEND_SLASH = False

# -------------------------------------------------------------------------
# -------------------------------------------------------------------------

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Finti test instance for Quick-start only. Delete these and set them in local_settings.py
if encryptor.has_psu_key():
    # Define these in local_settings.py:
    FINTI_URL = 'https://ws-test.oit.pdx.edu'
    FINTI_TOKEN = encryptor.decrypt(b'\xcb\xa0,m2\xcd\xee\xfe\x1f\x936\xdd/\x9b!\xb8\x8e\r\x92K\x93\xec\xa1\xd2p\xc9p\xfc\xa1L\xc2\x98\x87j\xc1\x9cF\x81\x96\xd0W\xbc\xd4\x97\xe8\xd0j\xa3+\xf0\xd1\xd7\xf8a_\xec7\xdeC\xc2C\x96\xac\x0f5}\x05\xf1\xd2]8\x0c\x05\xeb\xb6Py,\xc3N\x9e\x18\x85F*\x0e]q\x91HM\xc6\xe2O\x11\x0b\xe6;\xbc\t"\x7f\x83\xf8\xe3\xa2E\xdfJ\xa1:[n\xfc>\x132\xa3\x8f$\x11\x8fr\x17./\t8\xd6\xea\x9ce\xb8nc\\\xbc\xe4\xc2F\xf5\xf1\xf6F\x8d-\nc<6\xedpw/j\x92%\xb7\x90\x1f\x1e\xe6\x06\xb0\x95\r\xa3O=\xa0\xfc\x01h\xf7\x86\x9f\xe5\x89\xda\x08\x05\xf7\xfbs\x05\xef\xb5R\x8e\xec\xeb\xfb\xe8H\xd6`\x12N1ng\xce\x99\x9b[\xef!m\xdc\xe5\xee9\x94\xfa\xad\xf3\xbfl\xf6.\xcd\xe7\x97\xd0\x9bN|]t\xeb\xf2\xc6N\x0c\x10\xa9\xe8\xa8\x7fT\xe8\x18`>\xc9\xee5\x9b\x0e\xce5#\xa5\xb6&$\xd1*H\xde\x90C\n\x8e:2J\'2QQ\x8e\xe0Z(i_\xf7\x82\xf0I\xe3\x8d\x11pC[,(\xbe\x03\xfcO\x9b\x12\x1cn\x8a\xc6S\xa7\xff\x87\x1d\x0cj\x8ecL\x0fq\xb6\xb9B\xd0\xf5\r\x91\xf0\x94\xbc\xa5\xfe\x84t1\x0e+\xe0\xa1\x08"D\xbeH\x7f\xa7\x90\n\x97\xc6\xe1\x12<\n6:\x08\xe4\x1b\xcf\x9ba \xdb\x94S\xa5\xabdE\xf4\x839x\xeb8a\xbf<cx\xac\x81t\xac\x17\x1f\xf8\xf5\xf9#*j\x10\xd7r\x0fg\xc1H2\xfd\xa7\x19\x02\x9bl\x08w\x894P\x82\x95e\x95"\xea\x0ff=\xdb\x04&\x92\x15\xc1\x17\xf5\x81p\xdaxn\xe5\xc0\xaa<\xacY\xc3\xe0\xe8\x84`l\x8e\xaa\xdd%H\x0b\x07qR\x18aAS[\xcah\xeci\xb1\x87\xa8L\xfb\x06\xcf1\x03\xe1\xe7W-\xed\x83^<B:J\xba\xd5\xc3\x96\xa0\xe2\xe8\x91\xf5\xc5\x89\xb5?\xc1Dn\xc9WY@\xa4_{\xa6\xc7_g\x82\x0ci\xea\x8fN2y&\xd7')

# SECURITY WARNING: Overwrite this key in local_settings.py for production!
SECRET_KEY = 'somesecretkey123'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # PSU Base Plugin:
    'django_cas_ng',
    'crequest',
    'psu_base',
    'sass_processor',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'demo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['demo/templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'psu_base.context_processors.auth',
                'psu_base.context_processors.util'
            ],
            'libraries':{
                # If demo had a taglib, it would need to be defined here:
                # 'demo_taglib': 'demo.templatetags.demo_taglib',
            }
        },
    },
]

WSGI_APPLICATION = 'demo.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
if os.path.isfile('demo/local_settings.py'):
    # Local development database
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        },
    }
else:
    # AWS Database
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.environ['RDS_DB_NAME'],
            'USER': os.environ['RDS_USERNAME'],
            'PASSWORD': os.environ['RDS_PASSWORD'],
            'HOST': os.environ['RDS_HOSTNAME'],
            'PORT': os.environ['RDS_PORT'],
        }
    }


# For caching things (like database results)
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

# SESSION_ENGINE = "django.contrib.sessions.backends.cache"

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# SASS (https://github.com/jrief/django-sass-processor)
SASS_PROCESSOR_ROOT = os.path.join(BASE_DIR, 'sass_build')
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'sass_processor.finders.CssFinder',
]

SASS_PROCESSOR_INCLUDE_DIRS = [
    os.path.join('demo', 'static', 'css'),
]
SASS_PROCESSOR_AUTO_INCLUDE = True  # App specific static folders are added to the libsass include dirs
SASS_PROCESSOR_INCLUDE_FILE_PATTERN = r'^.+\.scss$'
SASS_PRECISION = 8

SASS_PROCESSOR_CUSTOM_FUNCTIONS = {
    'get-color': 'psu_base.services.template_service.get_sass_color',
    'get-string': 'psu_base.services.template_service.get_sass_string',
}

# #########################################################################
# PSU Base Plugin Settings
# #########################################################################

# Version of psu-base plugin
PSU_BASE_VERSION = psu_base.__version__

# PSU Centralized Repository
CENTRALIZED_NONPROD = 'https://content.oit.pdx.edu/nonprod'
CENTRALIZED_PROD = 'https://content.oit.pdx.edu'

# Set Timezone
TIME_ZONE = 'America/Vancouver'

# Message classes
MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}

# Logging Settings
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': "[%(asctime)s] %(levelname)s %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'WARN',
        },
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': False,
        },
        'psu': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    }
}

# SSO SETTINGS
CAS_APPLY_ATTRIBUTES_TO_USER = True
CAS_CREATE_USER = True
CAS_IGNORE_REFERER = True
CAS_LOGIN_MSG = None
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'django_cas_ng.backends.CASBackend',
)

# EMAIL SETTINGS
EMAIL_HOST = 'mailhost.pdx.edu'
EMAIL_PORT = 25
EMAIL_SENDER = 'noreply@pdx.edu'

# Session expiration
SESSION_COOKIE_AGE = 30 * 60  # 30 minutes

# Globally require authentication by default
REQUIRE_LOGIN = True

# List of URLs in your app that should be excluded from global authentication requirement
# By default, the root (landing page) is public
APP_PUBLIC_URLS = ['^/$']
# If deployed on-prem, root URL will contain additional context:
if URL_CONTEXT:
    APP_PUBLIC_URLS.append(f'^/{URL_CONTEXT}/?$')

# Some PSU Base paths must be public:
PSU_PUBLIC_URLS = ['.*/psu/test', '.*/accounts/login']

# CAS will return users to the root of the application
CAS_REDIRECT_URL = f'/{URL_CONTEXT if URL_CONTEXT else ""}'
LOGIN_URL = 'cas:login'

# May be overwritten in local_settings (i.e. to use sso.stage):
CAS_SERVER_URL = 'https://sso.oit.pdx.edu/idp/profile/cas/login'

# Get SASS Variables
if os.path.isfile('demo/sass_variables.py'):
    from .sass_variables import *

# Override settings with values for the local environment
if os.path.isfile('demo/local_settings.py'):
    from .local_settings import *

# In AWS (Elastic Beanstalk), values will be in environment variables
else:
    HOST_NAME = os.environ.get('HOST_NAME', 'localhost')
    HOST_IP = os.environ.get('HOST_IP')
    HOST_URL = os.environ.get('HOST_URL')

    # https://docs.djangoproject.com/en/2.2/topics/security/#ssl-https
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    # SECURE_SSL_REDIRECT = True
    # SECURE_SSL_HOST = f"https://{HOST_URL}"

    # https://docs.djangoproject.com/en/2.2/ref/middleware/#http-strict-transport-security
    # SECURE_HSTS_SECONDS = 31536000  # One Year

    ALLOWED_HOSTS = ['localhost', HOST_NAME, HOST_IP, HOST_URL]
    ENVIRONMENT = os.environ.get('ENVIRONMENT', 'DEV')
    CAS_SERVER_URL = os.environ.get('CAS_SERVER_URL', 'https://sso-stage.oit.pdx.edu/idp/profile/cas/login')
    DEBUG = str(os.environ.get('DEBUG', 'False')).lower() == 'true'
    SECRET_KEY = os.environ.get('SECRET_KEY', 'somesecretkey')
    FINTI_URL = os.environ.get('FINTI_URL', 'https://ws-test.oit.pdx.edu')
    FINTI_TOKEN = os.environ.get('FINTI_TOKEN', None)
