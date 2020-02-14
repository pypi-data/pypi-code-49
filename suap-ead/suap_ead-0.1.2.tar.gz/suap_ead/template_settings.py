from sc4py.env import env, env_as_int, env_as_bool, env_as_list, env_from_json
import sc4net

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Development
DEBUG = env_as_bool('DJANGO_DEBUG', True)
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {'console': {'class': 'logging.StreamHandler'}, },
    'loggers': {
        '': {'handlers': ['console'], 'level': 'DEBUG'},
        'parso': {'handlers': ['console'], 'level': 'INFO'},
    },
}
DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': lambda request: request.get_host() in ['localhost', '127.0.0.1', 'sso'],
}


# Apps
MY_APPS = env_as_list('MY_APPS', '')
SUAP_EAD_LIBS = env_as_list('SUAP_EAD_LIBS', 'suap_ead')
DEV_APPS = env_as_list('DEV_APPS', 'debug_toolbar,django_extensions' if DEBUG else '')
THIRD_APPS = env_as_list('THIRD_APPS', 'rest_framework')
DJANGO_APPS = env_as_list('DJANGO_APPS', 'django.contrib.admin,'
                                         'django.contrib.auth,'
                                         'django.contrib.contenttypes,'
                                         'django.contrib.sessions,'
                                         'django.contrib.messages,'
                                         'django.contrib.staticfiles')
INSTALLED_APPS = MY_APPS + SUAP_EAD_LIBS + THIRD_APPS + DEV_APPS + DJANGO_APPS


# Middleware
MIDDLEWARE = env_as_list('MIDDLEWARE', 'django.middleware.security.SecurityMiddleware,'
                                       'django.contrib.sessions.middleware.SessionMiddleware,'
                                       'django.middleware.common.CommonMiddleware,'
                                       'django.middleware.csrf.CsrfViewMiddleware,'
                                       'django.contrib.auth.middleware.AuthenticationMiddleware,'
                                       'django.contrib.messages.middleware.MessageMiddleware,'
                                       'django.middleware.clickjacking.XFrameOptionsMiddleware')
if DEBUG:
    MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']


# Template engine
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'suap_ead.context_processors.suap_ead',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# Database
DATABASES = {
    'default': {
        'ENGINE': env('POSTGRES_ENGINE', 'django.db.backends.postgresql_psycopg2'),
        'HOST': env('POSTGRES_HOST', 'db'),
        'PORT': env('POSTGRES_PORT', '5432'),
        'NAME': env('POSTGRES_DB', None),
        'USER': env('POSTGRES_USER', 'postgres'),
        'PASSWORD': env('POSTGRES_PASSWORD', 'postgres'),
    }
}


# Routing
WSGI_APPLICATION = env('DJANGO_WSGI_APPLICATION', 'suap_ead.wsgi.application')
ALLOWED_HOSTS = env_as_list('DJANGO_ALLOWED_HOSTS', '*' if DEBUG else '')
USE_X_FORWARDED_HOST = True
ROOT_URLCONF = env('DJANGO_ROOT_URLCONF', 'urls')
URL_PATH_PREFIX = env('URL_PATH_PREFIX', 'ead/perfil/')
STATIC_URL = env('DJANGO_STATIC_URL', "/%s%s" % (URL_PATH_PREFIX, 'static/'))
STATIC_ROOT = "/static/" + URL_PATH_PREFIX


# Localization
LANGUAGE_CODE = env('DJANGO_USE_I18N', 'pt-br')
TIME_ZONE = env('DJANGO_USE_I18N', 'UTC')
USE_I18N = env_as_bool('DJANGO_USE_I18N', True)
USE_L10N = env_as_bool('DJANGO_USE_L10N', True)
USE_TZ = env_as_bool('DJANGO_USE_TZ', True)


# REST Framework
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.BrowsableAPIRenderer',
        'rest_framework.renderers.JSONRenderer',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'suap_ead.auth.SecretDelegateAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
    ],
}


# Auth and Security... some another points impact on security, take care!
SUAP_EAD_ID_JWT_AUTHORIZE = env("SUAP_EAD_ID_JWT_AUTHORIZE", '/ead/id/jwt/authorize/')
SUAP_EAD_ID_JWT_VALIDATE = env("SUAP_EAD_ID_JWT_VALIDATE", 'http://id:8000/ead/id/jwt/validate/')
SUAP_EAD_ID_JWT_LOGOUT = env("SUAP_EAD_ID_JWT_LOGOUT", 'http://id:8000/ead/id/logout/')
SUAP_EAD_ID_JWT_CLIENT_ID = env("SUAP_EAD_ID_JWT_CLIENT_ID", '_SUAP_EAD_ID_JWT_CLIENT_ID_')
SUAP_EAD_ID_JWT_SECRET = env("SUAP_EAD_ID_JWT_SECRET", '_SUAP_EAD_ID_JWT_SECRET_')
SUAP_EAD_UTILS_AUTH_JWT_BACKEND = env("SUAP_EAD_UTILS_AUTH_JWT_BACKEND", 'suap_ead.backends.PreExistentUserJwtBackend')
SECRET_KEY = env('DJANGO_SECRET_KEY', 'changeme')
LOGIN_URL = env("DJANGO_LOGIN_URL", URL_PATH_PREFIX + 'jwt/login')
LOGOUT_URL = env("DJANGO_LOGOUT_URL", URL_PATH_PREFIX + 'logout/')
LOGIN_REDIRECT_URL = env("DJANGO_LOGIN_REDIRECT_URL", URL_PATH_PREFIX)
LOGOUT_REDIRECT_URL = env("DJANGO_LOGOUT_REDIRECT_URL", URL_PATH_PREFIX)
AUTH_USER_MODEL = env("DJANGO_AUTH_USER_MODEL", 'auth.User')
AUTHENTICATION_BACKENDS = env_as_list('DJANGO_AUTHENTICATION_BACKENDS', 'django.contrib.auth.backends.ModelBackend')
USE_LDAP = env('LDAP_AUTH_URL', None) is not None and env('LDAP_AUTH_URL', None) != 'ldap://0.0.0.0'
if USE_LDAP:
    LDAP_AUTH_URL = env('LDAP_AUTH_URL', '')
    LDAP_AUTH_USE_TLS = env_as_bool('LDAP_AUTH_USE_TLS')
    LDAP_AUTH_SEARCH_BASE = env('LDAP_AUTH_SEARCH_BASE', None)
    LDAP_AUTH_OBJECT_CLASS = env('LDAP_AUTH_OBJECT_CLASS', 'user')
    LDAP_AUTH_USER_FIELDS = env_from_json('LDAP_AUTH_USER_FIELDS', None, True)
    LDAP_AUTH_USER_LOOKUP_FIELDS = env_as_list('LDAP_AUTH_USER_LOOKUP_FIELDS', 'username')
    LDAP_AUTH_CLEAN_USER_DATA = env('LDAP_AUTH_CLEAN_USER_DATA')
    LDAP_AUTH_SYNC_USER_RELATIONS = env('LDAP_AUTH_SYNC_USER_RELATIONS')
    LDAP_AUTH_FORMAT_SEARCH_FILTERS = env('LDAP_AUTH_FORMAT_SEARCH_FILTERS')
    LDAP_AUTH_ACTIVE_DIRECTORY_DOMAIN = env('LDAP_AUTH_ACTIVE_DIRECTORY_DOMAIN')
    LDAP_AUTH_CONNECT_TIMEOUT = env_as_int('LDAP_AUTH_CONNECT_TIMEOUT', 10)
    LDAP_AUTH_RECEIVE_TIMEOUT = env_as_int('LDAP_AUTH_RECEIVE_TIMEOUT', 10)
    LDAP_AUTH_FORMAT_USERNAME = env('LDAP_AUTH_FORMAT_USERNAME', 'django_python3_ldap.format_username_active_directory')
    LDAP_ACTIVE_VALUE = env('LDAP_ACTIVE_VALUE', '512')
    AUTHENTICATION_BACKENDS = env_as_list('DJANGO_AUTHENTICATION_BACKENDS', 'django_python3_ldap.auth.LDAPBackend')

sc4net.default_headers = {"Authorization": "Secret %s" % SUAP_EAD_ID_JWT_SECRET}
