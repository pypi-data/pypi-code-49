from Crypto.PublicKey import RSA
from arrow import get as _, now
from jose import jwt


RSA_KEY = RSA.generate(bits=1024)
RSA_ID = RSA_KEY.export_key().decode()
RSA_PUB = RSA_KEY.publickey().publickey().export_key().decode()

PAYLOAD = {
    "scope": "test:testing",
    "permissions": ["test:testing"],
    "iss": "https://testing.provider.com/",
    "aud": "https://testing.com/service",
    "iat": (now() - _("1970-01-01")).total_seconds(),
    "exp": (now().shift(days=1) - _("1970-01-01")).total_seconds(),
    "gty": "client-credentials",
}

WITHOUT_SCOPES_PAYLOAD = {
    "iss": "https://testing.provider.com/",
    "aud": "https://testing.com/service",
    "iat": (now() - _("1970-01-01")).total_seconds(),
    "exp": (now().shift(days=1) - _("1970-01-01")).total_seconds(),
    "gty": "client-credentials",
}

EMPTY_PAYLOAD = {}


ALGORITHM = "RS256"

TOKEN_HEADERS = {"kid": "my-k-id"}


VALID_TOKEN = jwt.encode(
    PAYLOAD, key=RSA_ID, algorithm=ALGORITHM, headers=TOKEN_HEADERS
)

INVALID_TOKEN_NO_SCOPES = jwt.encode(
    WITHOUT_SCOPES_PAYLOAD, key=RSA_ID, algorithm=ALGORITHM, headers=TOKEN_HEADERS
)

INVALID_TOKEN_NO_CLAIMS = jwt.encode(
    EMPTY_PAYLOAD, key=RSA_ID, algorithm=ALGORITHM, headers=TOKEN_HEADERS
)
