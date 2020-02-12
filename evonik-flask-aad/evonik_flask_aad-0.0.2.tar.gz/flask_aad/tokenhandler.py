
from six.moves.urllib.request import urlopen
import os
from jose import jwt
import traceback
import json
from flask import request, _request_ctx_stack
from functools import wraps

from .autherror import AuthError

# TEMP Workaround: https://stackoverflow.com/questions/35569042/ssl-certificate-verify-failed-with-python3
if os.getenv("AAD_SSL_VERIFY") == "false":
    import ssl
    ssl._create_default_https_context = ssl._create_unverified_context
# END workaround


class TokenHandler:

    def __init__(self, audience=None, tenant_id=None):
        self.API_AUDIENCE = audience if audience is not None else os.getenv(
            "AAD_API_AUDIENCE")
        self.TENANT_ID = tenant_id if tenant_id is not None else  os.getenv(
            "AAD_TENANT_ID")
        if self.API_AUDIENCE is None or self.API_AUDIENCE == "":
            raise ValueError("API Audience is not defined")
        if self.TENANT_ID is None or self.TENANT_ID == "":
            raise ValueError("Tenant ID is not defined")

    def __enter__(self):
        if self.API_AUDIENCE is None or self.API_AUDIENCE == "":
            raise ValueError("API Audience is not defined")
        if self.TENANT_ID is None or self.TENANT_ID == "":
            raise ValueError("Tenant ID is not defined")

        return self

    def __exit__(self, exc_type, exc_value, tb):
        if exc_type is not None:
            traceback.print_exception(exc_type, exc_value, tb)
        # self.client.close()
        return True

    def get_token_auth_header(self):
        """Obtains the Access Token from the Authorization Header
        """
        auth = request.headers.get("Authorization", None)
        if not auth:
            raise AuthError({"code": "authorization_header_missing",
                             "description":
                             "Authorization header is expected"}, 401)

        parts = auth.split()

        if parts[0].lower() != "bearer":
            raise AuthError({"code": "invalid_header",
                             "description":
                             "Authorization header must start with"
                             " Bearer"}, 401)
        elif len(parts) == 1:
            raise AuthError({"code": "invalid_header",
                             "description": "Token not found"}, 401)
        elif len(parts) > 2:
            raise AuthError({"code": "invalid_header",
                             "description":
                             "Authorization header must be"
                             " Bearer token"}, 401)

        token = parts[1]
        return token

    def verify_token(self, token):
        try:
            jsonurl = urlopen("https://login.microsoftonline.com/" +
                              self.TENANT_ID + "/discovery/v2.0/keys")
            jwks = json.loads(jsonurl.read())
            unverified_header = jwt.get_unverified_header(token)
            rsa_key = {}
            token_issuer = ""  # "https://login.microsoftonline.com/" + self.TENANT_ID + "/v2.0"
            for key in jwks["keys"]:
                if key["kid"] == unverified_header["kid"]:
                    rsa_key = {
                        "kty": key["kty"],
                        "kid": key["kid"],
                        "use": key["use"],
                        "n": key["n"],
                        "e": key["e"]
                    }
                    token_issuer = key['issuer']
        except Exception as e:
            raise AuthError({"code": "invalid_header",
                             "description":
                             "Unable to parse authentication"
                             " token. Error: {}".format(e)}, 401)
        if rsa_key:
            try:
                payload = jwt.decode(
                    token,
                    rsa_key,
                    algorithms=["RS256"],
                    audience=self.API_AUDIENCE,
                    # issuer="https://sts.windows.net/" + TENANT_ID + "/"
                    issuer=token_issuer
                )
            except jwt.ExpiredSignatureError:
                raise AuthError({"code": "token_expired",
                                 "description": "token is expired"}, 401)
            except jwt.JWTClaimsError as e:
                raise AuthError({"code": "invalid_claims",
                                 "description":
                                 "incorrect claims,"
                                 "please check the audience and issuer. ERROR: {}".format(e)}, 401)
            except Exception as e:
                raise AuthError({"code": "invalid_header",
                                 "description":
                                 "Unable to parse authentication"
                                 " token. Error: {}".format(e)}, 401)
            # _request_ctx_stack.top.current_user = payload
            # print(_request_ctx_stack.top.current_user)
            return payload
        raise AuthError({"code": "invalid_header",
                         "description": "Unable to find appropriate key"}, 401)

    def requires_auth(self, f):
        """Determines if the Access Token is valid
        """

        @wraps(f)
        def decorated(*args, **kwargs):

            _request_ctx_stack.top.current_user = self.verify_token(
                self.get_token_auth_header())
            return f(*args, **kwargs)

        return decorated

    def get_roles(self, token=None):
        if token is None:
            token = self.get_token_auth_header()
            claims = jwt.get_unverified_claims(token)
        if "roles" in claims:
            return claims["roles"]
        else:
            return []

    def requires_role(role: str):
        def decorator(f):
            @wraps(f)
            def decorated(*args, **kwargs):
                if not role in get_roles():
                    raise AuthError({"code": "missing_role",
                                     "description":
                                     "Required Role {} is not assigned".format(
                                         role)
                                     }, 401)
                return f(*args, **kwargs)
            return decorated
        return decorator
    # Controllers API
