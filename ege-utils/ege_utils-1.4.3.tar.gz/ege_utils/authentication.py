from sc4net import get_json
from django.utils.translation import ugettext_lazy as _
from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication, get_authorization_header


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
        result = get_json('http://acesso:8000/ege/acesso/api/v1/secret/%s/' % secret)
        print(result)
        return None

    def authenticate_header(self, request):
        return self.keyword
