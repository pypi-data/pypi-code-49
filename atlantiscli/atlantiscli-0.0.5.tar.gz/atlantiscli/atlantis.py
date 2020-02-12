import jwt
from authlib.jose import JsonWebKey
from authlib.jose import JWK_ALGORITHMS

from atlantiscli.apiclient import ApiClient
from atlantiscli import config

api_client = ApiClient(url=config.ATLANTIS_URL)


def issue_token(code, client_id, client_secret):
    if not code:
        raise RuntimeError('Code is required')

    return api_client.issue_token(code, client_id, client_secret)


def validate_token(token, client_id):
    public_key = api_client.get_public_key()
    jwk = JsonWebKey(algorithms=JWK_ALGORITHMS)
    key = jwk.loads(public_key)

    try:
        return jwt.decode(token, key, audience=client_id)
    except Exception as err:
        raise InvalidTokenError(err)


class InvalidTokenError(RuntimeError):
    pass
