import base64
import json
import logging

import requests
import jwt
from cryptography.x509 import load_pem_x509_certificate
from cryptography.hazmat.backends import default_backend
from jwt.exceptions import InvalidTokenError

_default_options = {
    "verify_signature": True,
    "verify_exp": True,
    "verify_nbf": True,
    "verify_iat": True,
    "verify_aud": False,
    "require_exp": True,
    "require_iat": True,
    "require_nbf": True,
    "algorithms": [
        # Microsoft Azure Active Directory algorithm
        "RS256"
    ],
}


def validate(jwt_token: str, identity_provider_url: str, **options) -> (dict, dict):
    """
    Validate base64 encoded token and return JSON header and body as a tuple.

    :param jwt_token: JWT Token (base64 encoded) as provided in Bearer header.
    :param identity_provider_url: URL to fetch keys from (will certainly ends with /common/discovery/keys)

    :param verify_signature: Default to True
    :param verify_exp: Check token expiry. Default to True
    :param verify_nbf: Default to True
    :param verify_iat: Default to True
    :param verify_aud: Default to False
    :param require_exp: Default to True
    :param require_iat: Default to True
    :param require_nbf: Default to True
    :param algorithms: Default to ["RS256"]
    :raises InvalidTokenError
    :raises InvalidKeyError
    """
    json_header, json_body = decode(jwt_token)
    _validate_json_token(jwt_token, json_header, options, identity_provider_url)
    return json_header, json_body


def decode(jwt_token: str) -> (dict, dict):
    """
    Decode base64 encoded token and return JSON decoded header and body as a tuple.
    :raises InvalidTokenError
    """
    if not jwt_token:
        raise InvalidTokenError("JWT Token is mandatory.")

    if jwt_token.count(".") < 2:
        raise InvalidTokenError(
            "Invalid JWT Token (header, body and signature must be separated by dots)."
        )

    (jwt_header, jwt_body, jwt_signature) = jwt_token.split(".", maxsplit=2)

    return _to_json(jwt_header), _to_json(jwt_body)


def _validate_json_token(
    jwt_token: str, json_header: dict, options: dict, identity_provider_url: str
):
    public_key = _get_public_key(json_header, identity_provider_url)
    logging.debug(f"Public key: {public_key}")
    options = {**_default_options, **options}
    jwt.decode(
        jwt_token, key=public_key, algorithms=options.pop("algorithms"), options=options
    )


def _get_public_key(json_header: dict, identity_provider_url: str) -> str:
    key_identifier = json_header.get("kid", "not provided")

    # TODO cache this
    x5c = _request_x5c(key_identifier, identity_provider_url)

    certificate_text = (
        b"-----BEGIN CERTIFICATE-----\n"
        + x5c.encode("utf-8")
        + b"\n-----END CERTIFICATE-----"
    )
    certificate = load_pem_x509_certificate(certificate_text, default_backend())
    return certificate.public_key()


def _request_x5c(key_identifier: str, identity_provider_url: str) -> str:
    keys = requests.get(identity_provider_url)
    if not keys:
        raise InvalidTokenError(f"Identify provider cannot be reached: {keys.text}")
    keys = keys.json().get("keys", [])
    keys = {key["kid"]: key["x5c"][0] for key in keys}

    if key_identifier not in keys:
        raise InvalidTokenError(
            f"{key_identifier} is not a valid key identifier. Valid ones are {list(keys)}."
        )
    return keys[key_identifier]


def _to_json(base_64_json: str) -> dict:
    decoded_json = _decode_base64(base_64_json)
    return json.loads(decoded_json.decode("unicode_escape"))


def _decode_base64(base64_encoded_string: str) -> bytes:
    """
    Decode base64, padding (with = character) being optional.

    :param base64_encoded_string: Base64 data as an ASCII byte string
    :returns: The decoded byte string.
    """
    missing_padding = len(base64_encoded_string) % 4
    if missing_padding != 0:  # Pad with extra = characters at the end
        base64_encoded_string += "=" * (4 - missing_padding)
    return base64.b64decode(base64_encoded_string, altchars="_+")
