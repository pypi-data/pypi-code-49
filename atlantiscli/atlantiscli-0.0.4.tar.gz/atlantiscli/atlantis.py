import os
import jwt

from atlantiscli.apiclient import ApiClient
from atlantiscli import config

def issue_token(code, client_id, client_secret):
    api_client = ApiClient(url=config.ATLANTIS_URL)
    return api_client.issue_token(code, client_id, client_secret)


def verify_token(token):
    public_key = ApiClient.get_public_key()
    decoded = jwt.decode(token, public_key, algorithms='RS256')
