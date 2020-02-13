import hashlib
import hmac
import os
import time

from slack_utils.exceptions import SlackException


def verify(signature, timestamp, body, slack_signing_secret=None):
    """Validate Slack signature

    :param signature: X-Slack-Signature HTTP header value
    :param timestamp: X-Slack-Request-Timestamp HTTP header value
    :param body: Request body
    :param slack_signing_secret: Slack signing secret. You can use
                                 SLACK_SIGNING_SECRET env var instead
    """
    if slack_signing_secret is None:
        slack_signing_secret = os.getenv('SLACK_SIGNING_SECRET', '')

    if time.time() - int(timestamp) > 60:
        raise SlackException('Message is older than 60 seconds, '
                             'probably someone is doing something nasty.')

    base_string = f'v0:{timestamp}:{body}'
    hashed_string = 'v0=' + hmac.new(
        slack_signing_secret.encode(),
        msg=base_string.encode(),
        digestmod=hashlib.sha256
    ).hexdigest()

    if not hmac.compare_digest(signature, hashed_string):
        raise SlackException('Invalid signature.')

    return True
