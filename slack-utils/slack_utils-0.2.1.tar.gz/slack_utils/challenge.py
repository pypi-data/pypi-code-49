import json
import os

from slack_utils.exceptions import SlackException


def verify_token(token):
    """Verifies Slack verification token

    :param token: Slack verification token
    """
    if token != os.getenv('SLACK_VERIFICATION_TOKEN'):
        raise SlackException('Invalid verification token')


def respond(challenge, token):
    """Responds to Slack challenge

    :param challenge: Slack challenge string
    :param token: Slack verification token
    :returns: Slack challenge string in json format
    """
    verify_token(token)
    return {
        'statusCode': 200,
        'body': json.dumps({
            'challenge': challenge
        }),
        'headers': {
            'Content-Type': 'application/json'
        }
    }
