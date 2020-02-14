from sc4net import get_json
from django.contrib.auth import get_user_model, login
from django.utils.translation import ugettext_lazy as _
from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication, get_authorization_header


class SuapEadUser:
    def __init__(self, user, profile):
        self.user = user
        self.profile = profile


class SecretDelegateAuthentication(BaseAuthentication):
    """
        Authorization: Secret 401f7ac837da42b97f613d789819ff93537bee6a
    """

    keyword = 'Secret'

    def authenticate(self, request):
        auth = get_authorization_header(request).split()

        if not auth or auth[0].decode() != self.keyword:
            return None

        if len(auth) == 1:
            msg = _('Invalid secret header. No credentials provided.')
            raise exceptions.AuthenticationFailed(msg)
        elif len(auth) > 2:
            msg = _('Invalid secret header. Secret string should not contain spaces.')
            raise exceptions.AuthenticationFailed(msg)

        try:
            token = auth[1].decode()
        except UnicodeError:
            msg = _('Invalid token header. Secret string should not contain invalid characters.')
            raise exceptions.AuthenticationFailed(msg)

        return self.authenticate_credentials(token)

    def authenticate_credentials(self, secret):
        result = get_json('http://id:8000/sead/id/api/v1/secret/%s/' % secret)
        print(result)
        return None

    def authenticate_header(self, request):
        return self.keyword


class PreExistentUserJwtBackend:
    def login_user(self, request, user_data):
        user = get_user_model().objects.get(username=user_data['username'])
        login(request, user, backend=None)
        request.session['suap_ead'] = SuapEadUser(user_data)


class CreateNewUserJwtBackend:
    def login_user(self, request, user_data):
        user, created = get_user_model().objects.get_or_create(username=user_data['username'])
        login(request, user, backend=None)
        request.session["suap_ead"] = {"user": user_data}
