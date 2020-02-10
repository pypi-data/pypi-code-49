# Imports from Django.
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator


# Imports from other dependencies.
from rest_framework import authentication
from rest_framework import exceptions


# Imports from elections.
from election.conf import settings


class CsrfExemptSessionAuthentication(authentication.SessionAuthentication):
    def enforce_csrf(self, request):
        pass


class SimpleAuthentication(authentication.TokenAuthentication):
    """"""

    keyword = "CivicElectionToken"
    working_token = getattr(settings, "API_TOKEN")

    # model = LoaderToken
    model = None

    def authenticate_credentials(self, key):
        if key == self.working_token:
            return (
                User.objects.filter(is_superuser=True)[0],
                self.working_token,
            )

        raise exceptions.AuthenticationFailed("Invalid token.")
        # model = self.get_model()
        # try:
        #     token = model.objects.get(key=key)
        # except model.DoesNotExist:
        #     if settings.DEBUG:
        #         return (AnonymousUser, "")
        #     raise exceptions.AuthenticationFailed(_("Invalid token."))
        #
        # return (token.user, token)
