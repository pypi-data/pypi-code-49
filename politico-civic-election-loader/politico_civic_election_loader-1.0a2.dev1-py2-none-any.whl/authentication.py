# Imports from Django.
from django.conf import settings
from django.contrib.auth.models import AnonymousUser
from django.utils.translation import gettext_lazy as _


# Imports from other dependencies.
from rest_framework import authentication
from rest_framework import exceptions


# Imports from election_loader.
from election_loader.models import LoaderToken


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
