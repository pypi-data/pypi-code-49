import hashlib
import hmac
from datetime import datetime

import pytest

from slack_utils.exceptions import SlackException
from slack_utils.signature import verify


def test_verify_request():
    timestamp = datetime.now().timestamp()
    body = 'some_body'
    slack_signing_secret = 'secret'

    base_string = f'v0:{timestamp}:{body}'
    hashed_string = 'v0=' + hmac.new(
        slack_signing_secret.encode(),
        msg=base_string.encode(),
        digestmod=hashlib.sha256
    ).hexdigest()

    assert verify(hashed_string, timestamp, body, slack_signing_secret)


def test_invalid_signature():
    hashed_string = 'invalid string'
    timestamp = datetime.now().timestamp()
    body = 'some_body'
    slack_signing_secret = 'secret'

    with pytest.raises(SlackException):
        verify(hashed_string, timestamp, body, slack_signing_secret)


def test_invalid_timestamp():
    timestamp = datetime.now().timestamp() - 100
    body = 'some_body'
    slack_signing_secret = 'secret'

    base_string = f'v0:{timestamp}:{body}'
    hashed_string = 'v0=' + hmac.new(
        slack_signing_secret.encode(),
        msg=base_string.encode(),
        digestmod=hashlib.sha256
    ).hexdigest()

    with pytest.raises(SlackException):
        verify(hashed_string, timestamp, body, slack_signing_secret)


def test_missing_slack_signing_secret():
    timestamp = datetime.now().timestamp() - 100
    body = 'some_body'
    slack_signing_secret = 'secret'

    base_string = f'v0:{timestamp}:{body}'
    hashed_string = 'v0=' + hmac.new(
        slack_signing_secret.encode(),
        msg=base_string.encode(),
        digestmod=hashlib.sha256
    ).hexdigest()

    with pytest.raises(SlackException):
        verify(hashed_string, timestamp, body)
