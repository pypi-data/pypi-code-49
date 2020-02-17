"""Common HTTP and browser related settings."""
import os
import unimatrix.lib.environ


ALLOWED_HOSTS = unimatrix.lib.environ.parselist(os.environ,
    'HTTP_ALLOWED_HOSTS', sep=';')

CSRF_COOKIE_DOMAIN = os.getenv('CSRF_COOKIE_DOMAIN')

CSRF_COOKIE_SECURE = os.getenv('CSRF_COOKIE_INSECURE') != '1'

CSRF_COOKIE_HTTPONLY = os.getenv('CSRF_COOKIE_ALLOWHTTP') != '1'

SECURE_HSTS_SECONDS = 86400 * 365

SECURE_HSTS_PRELOAD = os.getenv('HSTS_PRELOAD') == '1'

SESSION_COOKIE_DOMAIN = os.getenv('SESSION_COOKIE_DOMAIN')

SESSION_COOKIE_NAME = os.getenv('SESSION_COOKIE_NAME') or 'sessionid'

SESSION_COOKIE_PATH = os.getenv('SESSION_COOKIE_PATH') or '/'

SESSION_COOKIE_SECURE = os.getenv('SESSION_COOKIE_INSECURE') != '1'

SESSION_COOKIE_HTTPONLY = os.getenv('SESSION_COOKIE_ALLOWHTTP') != '1'
