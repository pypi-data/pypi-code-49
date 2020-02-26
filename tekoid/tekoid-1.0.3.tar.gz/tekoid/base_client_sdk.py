import base64
import jwt
import json
from . client import Client

DEFAULT_SCOPE = ["openid", "profile"]
DEFAULT_BASE_URI = "https://oauth.develop.tekoapis.net"
DEFAULT_AUTHORIZE_PATH = "/oauth/authorize"
DEFAULT_TOKEN_PATH = "/oauth/token"
DEFAULT_REFRESH_TOKEN_PATH = "/oauth/token"
DEFAULT_REVOKE_TOKEN_PATH = "/oauth/revoke"
DEFAULT_JWKS_PATH = "/.well-known/jwks.json"


class BaseClientSDK(object):
    def __init__(self, client_id, client_secret, **kwargs):
        self.client_id = client_id
        self.client_secret = client_secret
        self.scope = kwargs.get("scope", DEFAULT_SCOPE)
        self.base_uri = kwargs.get("base_uri", DEFAULT_BASE_URI)
        self.authorize_path = kwargs.get(
            "authorize_path", DEFAULT_AUTHORIZE_PATH)
        self.token_path = kwargs.get("token_path", DEFAULT_TOKEN_PATH)
        self.refresh_token_path = kwargs.get(
            "refresh_token_path", DEFAULT_REFRESH_TOKEN_PATH)
        self.revoke_token_path = kwargs.get(
            "revoke_token_path", DEFAULT_REVOKE_TOKEN_PATH)
        self.jwks_path = kwargs.get("jwks_path", DEFAULT_JWKS_PATH)
        self.client = Client(verify_ssl=kwargs.get("verify_ssl") or True)


