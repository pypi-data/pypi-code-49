import hashlib
import json
import uuid
from base64 import b64encode
from calendar import timegm
from datetime import datetime, timedelta
from functools import wraps

import requests
from jose import jwk, jws, jwt

from flask import request

from .dicplus import DicPlus

ALGORITHMS = ["RS256"]


def hash_digest(body):
    myhash = hashlib.sha512()
    myhash.update(body)
    digest = b64encode(myhash.digest()).decode()
    return digest


class Verifyer ():

    def __init__(self, issuer, audience, jti_cache=None, keySet=None):

        self.issuer = str(issuer)
        self.jti_cache = jti_cache
        self.algorithms = ALGORITHMS
        self.audience = audience
        if not keySet:
            url = self.issuer+"/.well-known/jwks.json"
            self.jwks = requests.get(url=url).json()['keys']
        else:
            self.jwks = keySet

    def get_signature_token_header(self, request):
        """Obtains the Access Token from the Authorization Header
        """
        auth = request.headers.get("Authorization", None)
        if not auth:
            raise Exception("No Authorization Header")

        auth_parts = auth.split()

        if auth_parts[0].lower() != "signature":
            raise Exception("Authorization Header must start with Signature")
        elif len(auth_parts) == 1:
            raise Exception("No Signature attached")
        elif len(auth_parts) > 2:
            raise Exception("Invalid Header")
        token = auth_parts[1]

        return token

    def verify(self, f):
        @wraps(f)
        def decorated(*args, **kwargs):
            # Assumes the request is available
            try:
                token = self.get_signature_token_header(request)
                verified_token = DicPlus(json.loads(
                    jws.verify(token, self.jwks, self.algorithms)))
                hashed_body = hash_digest(request.get_data())
            except:
                raise Exception("Error occured during Verification")
            if verified_token.digest != hashed_body:
                raise Exception("Digest Not Equal")
            if verified_token.aud != self.audience:
                raise Exception("Audience Not Equal")
            if verified_token.iss != self.issuer:
                raise Exception("Issuer Not Equal")
            if verified_token.exp < timegm(datetime.utcnow().utctimetuple()):
                raise Exception("Token Expired")

            return f(*args, **kwargs)

        return decorated


class Signer():

    def __init__(self, issuer, audience, private_key, algorithm=ALGORITHMS[0], expiration=100):
        self.audience = audience
        self.algorithm = algorithm
        self.expiration = expiration
        self.issuer = issuer
        self.private_key = private_key

    def sign(self, body, is_json=False):
        jti = str(uuid.uuid4())
        enc_body = json.dumps(body, separators=(',', ': ')).encode()
        digest = hash_digest(enc_body)
        token_payload = {
            "digest": digest,
            "jti": jti,
            "iat": timegm(datetime.utcnow().utctimetuple()),
            "exp": timegm(datetime.utcnow().utctimetuple()) + self.expiration,
            "iss": self.issuer,
            "aud": self.audience
        }
        signed_token = jws.sign(
            token_payload, self.private_key, algorithm=self.algorithm)

        return signed_token
