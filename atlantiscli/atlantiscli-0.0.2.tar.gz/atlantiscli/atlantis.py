import jwt

from atlantiscli.apiclient import ApiClient


def issue_token(code, client_id, client_secret):
    return ApiClient.issue_token(code, client_id, client_secret)


def verify_token(token):
    public_key = ApiClient.get_public_key()
    decoded = jwt.decode(token, public_key, algorithms='RS256')
