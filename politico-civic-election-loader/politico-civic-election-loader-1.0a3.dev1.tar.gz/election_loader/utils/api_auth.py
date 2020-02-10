# Imports from Django.
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator


# Imports from other dependencies.
from rest_framework import authentication
from rest_framework import exceptions


# Imports from elections.
from election_loader.models import LoaderToken


class CsrfExemptSessionAuthentication(authentication.SessionAuthentication):
    def enforce_csrf(self, request):
        pass


class TokenAPIAuthentication(authentication.TokenAuthentication):
    """"""

    keyword = "CivicLoaderToken"
    model = LoaderToken

    def authenticate_credentials(self, key):
        model = self.get_model()
        try:
            token = model.objects.get(key=key)
        except model.DoesNotExist:
            if settings.DEBUG:
                return (AnonymousUser, "")
            raise exceptions.AuthenticationFailed(_("Invalid token."))

        return (token.user, token)
