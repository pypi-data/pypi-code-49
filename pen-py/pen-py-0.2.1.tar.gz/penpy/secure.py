import hashlib
import json
import os
import socket
import time
import uuid
from base64 import b64encode
from calendar import timegm
from datetime import datetime, timedelta
from functools import wraps

import requests
from jose import jwk, jws, jwt

from flask import g, request

from .dicplus import DicPlus

ALGORITHMS = ["RS256"]
EXPIRATION = 1000


def hash_digest(body):
    myhash = hashlib.sha512()
    myhash.update(body)
    digest = b64encode(myhash.digest()).decode()
    return digest


def get_token_header(auth_type, request):
    """Obtains the Access Token from the Authorization Header
    """
    auth = request.headers.get("Authorization", None)
    if not auth:
        raise Exception("No Authorization Header")

    auth_parts = auth.split()

    if auth_parts[0].lower() != auth_type.lower():
        raise Exception(
            "Authorization Header must start with {}".format(auth_type))
    elif len(auth_parts) == 1:
        raise Exception("No Signature attached")
    elif len(auth_parts) > 2:
        raise Exception("Invalid Header")
    token = auth_parts[1]

    return token


class Secure():
    def __init__(self, service, private_key, keySet=None, signer=None, authenticator=None):
        self.service = service
        self.keySet = keySet
        self.private_key = private_key
        if authenticator:
            self.authenticator = Authenticator(
                client_id=authenticator['client_id'],
                client_secret=authenticator['client_secret'],
                audience=self.service,
                domain=authenticator['domain']
            )
        self.authorizer = Authorizer(audience=self.service, keySet=self.keySet)
        self.signer = Signer(issuer=signer or self.service,
                             private_key=self.private_key)
        self.verifyer = Signature_Verifyer(
            audience=self.service, keySet=self.keySet)

    def validate_scope(self, scope, token=None):
        if not token:
            token_payload = g.authorize_token_payload
        else:
            token_payload = jwt.get_unverified_claims(token)
        if scope == None or scope == "":
            return True
        if token_payload.get("scope"):
            scope = scope.split()
            for s in scope:
                if s not in token_payload['scope']:
                    return False
        return True

    def authorize(self, scope, issuers=None):
        def inner_authorize(f):
            @wraps(f)
            def decorated(*args, **kwargs):
                try:
                    token = get_token_header("Bearer", request)
                    payload = self.authorizer.decode(token, issuers)
                    g.authorize_token_payload = payload
                except:
                    raise Exception("Invalid Header", 401)
                if not self.validate_scope(scope, token):
                    raise Exception("Invalid Scope", 401)
                return f(*args, **kwargs)
            return decorated
        return inner_authorize

    def get_access_token(self):
        return self.authenticator.access_token

    def verify(self, issuers=None):
        def inner_verify(f):
            @wraps(f)
            def decorated(*args, **kwargs):
                # Assumes the request is available
                token = get_token_header("signature", request)
                body = request.get_data()
                if not self.verifyer.verify(token, body, issuers):
                    raise Exception("Wrong Signature", 401)

                return f(*args, **kwargs)

            return decorated
        return inner_verify

    def sign(self, body, audience):
        return self.signer.sign(body, audience)

    def signed_headers(self, body, audience):
        headers = {
            "Authorization": "Signature {}".format(self.sign(body, audience))
        }
        return headers

    def auth_headers(self):
        headers = {
            "Authorization": "Bearer {}".format(self.authenticator.access_token)
        }
        return headers


class KeySet():
    def __init__(self, jsonfile=None):
        self.issuers = []
        if jsonfile:
            self.from_json(jsonfile)

    def add_issuer(self, issuer, keys=None):
        if not keys:
            try:
                url = issuer+".well-known/jwks.json"
                keys = requests.get(url=url).json()['keys']
            except:
                raise Exception(
                    "No keys provided nor found on {}.well-known/jwks.json".format(issuer))
        if type(keys) != list:
            keys = [keys]
        self.issuers.append({"issuer": issuer, "keys": keys})

    def from_json(self, jsonfile):
        dp = DicPlus.from_json(jsonfile)
        for ks in dp.keySet:
            issuer = ks.toDict()
            if "keys" not in ks:
                self.add_issuer(issuer["issuer"])
            else:
                self.add_issuer(issuer["issuer"], issuer["keys"])

    def get_keys(self, issuers=None):
        keys = []
        if type(issuers) != list and issuers is not None:
            issuers = [issuers]
        for i in self.issuers:
            if issuers:
                if i['issuer'] not in issuers:
                    continue
            for key in i['keys']:
                keys.append(key)

        return {"keys": keys}


class Authenticator():
    # Using Auth0
    def __init__(self, domain, client_id, client_secret, audience):
        self.domain = domain
        self.client_id = client_id
        self.client_secret = client_secret
        self.audience = audience
        self.getAccessToken()
        if self._access_token is None:
            raise Exception("Request for access token failed")

    def getAccessToken(self):
        body = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "audience": self.audience,
            "grant_type": "client_credentials"
        }
        try:
            response = requests.post(
                url="{}/oauth/token".format(self.domain), json=body)
        except Exception as e:
            raise Exception(e)
            return None
        else:
            json_response = DicPlus.json_loads(response.text)
            self._access_token = json_response.access_token
            self._access_token_expiration = time.time() + float(json_response.expires_in)

    @property
    def access_token(self):
        if time.time() > self._access_token_expiration:
            self.getAccessToken()
        return self._access_token


class Authorizer():
    def __init__(self, audience, keySet):
        self.audience = audience
        self.keySet = keySet

    def decode(self, token, issuers=None):
        try:
            jwks = self.keySet.get_keys(issuers)
            payload = jwt.decode(
                token,
                jwks,
                audience=self.audience
            )
        except jwt.ExpiredSignatureError:
            raise Exception("Expired Signature", 401)
        except jwt.JWTClaimsError:
            raise Exception("Please check audience and issuer", 401)
        except Exception:
            raise Exception("Invalid header", 401)

        return payload


class Signature_Verifyer():

    def __init__(self, audience, keySet, jti_cache=None):

        self.jti_cache = jti_cache
        self.algorithms = ALGORITHMS
        self.audience = audience
        self.keySet = keySet

    def verify(self, token, body, issuers=None):
        jwks = self.keySet.get_keys(issuers)
        verified_token = DicPlus(json.loads(
            jws.verify(token, jwks, self.algorithms)))
        hashed_body = hash_digest(body)
        if verified_token.digest != hashed_body:
            raise Exception("Digest Not Equal")
        if verified_token.aud != self.audience:
            raise Exception("Audience Not Equal")
        if verified_token.exp < timegm(datetime.utcnow().utctimetuple()):
            raise Exception("Token Expired")
        return True


class Signer():

    def __init__(self, issuer, private_key, algorithm=ALGORITHMS[0], expiration=EXPIRATION):
        self.algorithm = algorithm
        self.expiration = expiration
        self.issuer = issuer
        self.private_key = private_key

    def sign(self, body, audience, is_json=False):
        jti = str(uuid.uuid4())
        enc_body = json.dumps(body, separators=(',', ': ')).encode()
        digest = hash_digest(enc_body)
        token_payload = {
            "digest": digest,
            "jti": jti,
            "iat": timegm(datetime.utcnow().utctimetuple()),
            "exp": timegm(datetime.utcnow().utctimetuple()) + self.expiration,
            "iss": self.issuer,
            "aud": audience
        }
        signed_token = jws.sign(
            token_payload, self.private_key, algorithm=self.algorithm)

        return signed_token
