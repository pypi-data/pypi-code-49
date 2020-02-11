import hashlib
import hmac
from calendar import timegm
from datetime import datetime
from urllib.parse import urlencode


def sign_payload(url, timestamp, secret, payload=None):
    if payload:
        payload = urlencode(sorted(payload.items()))
    parts = [url, str(timestamp), payload]
    sign_url = "|".join(parts)
    signer = hmac.new(secret.encode("utf8"), sign_url.encode("utf8"), hashlib.sha512)
    return signer.hexdigest()


def generate_request_timestamp():
    return timegm(datetime.utcnow().utctimetuple())
