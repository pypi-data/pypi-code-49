import logging

from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseServerError
from social_core.exceptions import AuthCanceled, AuthMissingParameter
from social_django.middleware import SocialAuthExceptionMiddleware

from unicef_security.backends import UNICEFAzureADB2COAuth2

logger = logging.getLogger("healthz")


class HealthCheckMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        if request.method == "GET":
            if request.path == "/readiness/":
                return self.readiness(request)
            elif request.path == "/healthz/":
                return self.healthz(request)
        return self.get_response(request)

    def healthz(self, request):
        """
        Returns that the server is alive.
        """
        return HttpResponse("OK")

    def readiness(self, request):
        # Connect to each database and do a generic standard SQL query
        # that doesn't write any data and doesn't depend on any tables
        # being present.
        try:
            from django.db import connections
            for name in connections:
                cursor = connections[name].cursor()
                cursor.execute("SELECT 1;")
                row = cursor.fetchone()
                if row is None:
                    return HttpResponseServerError("db: invalid response")
        except Exception as e:
            logger.exception(e)
            return HttpResponseServerError("db: cannot connect to database.")

        # Call get_stats() to connect to each memcached instance and get it's stats.
        # This can effectively check if each is online.
        try:
            from django.core.cache import caches
            from django.core.cache.backends.memcached import BaseMemcachedCache
            for cache in caches.all():
                if isinstance(cache, BaseMemcachedCache):
                    stats = cache._cache.get_stats()
                    if len(stats) != len(cache._servers):
                        return HttpResponseServerError("cache: cannot connect to cache.")
        except Exception as e:
            logger.exception(e)
            return HttpResponseServerError("cache: cannot connect to cache.")

        return HttpResponse("OK")


class UNICEFSocialAuthExceptionMiddleware(SocialAuthExceptionMiddleware):
    """Middleware to ignore Forgot Password Exceptions"""

    def process_exception(self, request, exception):
        if isinstance(exception, (AuthCanceled, AuthMissingParameter)):
            return HttpResponseRedirect(self.get_redirect_uri(request, exception))
        else:
            raise exception

    def get_redirect_uri(self, request, exception):
        error = request.GET.get('error', None)

        # This is what we should expect:
        # ['AADB2C90118: The user has forgotten their password.\r\n
        # Correlation ID: 7e8c3cf9-2fa7-47c7-8924-a1ea91137ba9\r\n
        # Timestamp: 2018-11-13 11:37:56Z\r\n']
        error_description = request.GET.get('error_description', None)
        if error == "access_denied" and error_description is not None:
            if 'AADB2C90118' in error_description:
                auth_class = UNICEFAzureADB2COAuth2()
                redirect_home = auth_class.get_redirect_uri()
                redirect_url = 'https://login.microsoftonline.com/' + \
                               settings.TENANT_ID + \
                               "/oauth2/v2.0/authorize?p=" + \
                               settings.SOCIAL_PASSWORD_RESET_POLICY + \
                               "&client_id=" + settings.KEY + \
                               "&nonce=defaultNonce&redirect_uri=" + redirect_home + \
                               "&scope=openid+email&response_type=code"
                return redirect_url

        # TODO: In case of password reset the state can't be verified figure out a way to log the user in after reset
        return settings.LOGIN_URL
