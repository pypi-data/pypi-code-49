import base64
import json
import os

from django.conf import settings
from django.urls import reverse
from jwt import decode as jwt_decode, DecodeError, ExpiredSignature
from social_core.backends.azuread_b2c import AzureADB2COAuth2
from social_core.backends.azuread_tenant import AzureADTenantOAuth2
from social_core.exceptions import AuthTokenError


class UNICEFAzureADTenantOAuth2Ext(AzureADTenantOAuth2):
    def user_data(self, access_token, *args, **kwargs):
        response = kwargs.get('response')
        id_token = response.get('id_token')

        # decode the JWT header as JSON dict
        jwt_header = json.loads(
            base64.b64decode(id_token.split('.', 1)[0]).decode()
        )

        # get key id and algorithm
        key_id = jwt_header['kid']
        algorithm = jwt_header['alg']
        verify = os.environ.get('OAUTH2_VERIFY', False)
        key = ''
        try:
            # retrieve certificate for key_id
            if verify:
                certificate = self.get_certificate(key_id)
                key = certificate.public_key()

            return jwt_decode(
                id_token,
                verify=verify,
                key=key,
                algorithms=algorithm,
                audience=self.setting('KEY')
            )
        except (DecodeError, ExpiredSignature) as error:
            raise AuthTokenError(self, error)


class UNICEFAzureADB2COAuth2(AzureADB2COAuth2):
    """UNICEF Azure ADB2C Custom Backend"""

    name = 'unicef-azuread-b2c-oauth2'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.redirect_uri = settings.HOST + reverse('social:complete', kwargs={'backend': 'unicef-azuread-b2c-oauth2'})
