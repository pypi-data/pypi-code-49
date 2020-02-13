from .code_client_sdk import CodeClientSDK
from .credentials_sdk import CredentialsClientSDK


class ClientSDK(object):
    def __init__(self, client_id, client_secret, redirect_uri, **kwargs):
        self.code = CodeClientSDK(
            client_id, client_secret, redirect_uri, **kwargs)

        self.credentials = CredentialsClientSDK(
            client_id, client_secret, **kwargs)
