import time

from django.core import signing
from django.db import transaction


def generate_token(token_params):

    return signing.dumps(token_params)


def generate_verify_email_token(user_id, email):
    return generate_token({
        'user_id': user_id,
        'email': email,
        'action': 'verify_email',
    })
