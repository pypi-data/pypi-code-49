from . import token, exceptions
import requests
import logging
import sentry_sdk



logger = logging.getLogger(__name__)



class TriggeredSend(object):
    url_base = 'https://www.exacttargetapis.com/messaging/v1/messageDefinitionSends'

    def __init__(self, external_key):
        self.external_key = external_key
        self.token = token.CachedTokenGenerator()


    def dispatch(self, email, attrs):
        url = '%s/key:%s/send' % (self.url_base, self.external_key)
        headers = self.token.headers()
        req_data = {
            "To": {
                "Address": email,
                "SubscriberKey": email,
                "ContactAttributes": {
                    "SubscriberAttributes": attrs
                },
            },
            "OPTIONS": {
                "RequestType": "SYNC"
            },
        }

        resp = requests.post(url, headers=headers, json=req_data)
        resp.raise_for_status()
        reply = resp.json()
        with sentry_sdk.configure_scope() as scope:
            scope.set_extra("reply_data", reply)
        for response in reply['responses']:
            if response['hasErrors']:
                error_messages = response.get('messageErrors', [])
                # set of error codes in messages
                error_codes = {err.get('messageErrorCode') for err in error_messages}
                # coerce ET_IGNORED_ERROR_CODES into set
                from . import settings
                codes_to_ignore = set(settings.ET_IGNORED_ERROR_CODES)

                # if response has any ignorable codes... set intersection
                if len(codes_to_ignore & error_codes) > 0:
                    # log error, but don't send ignored error codes to Sentry
                    logger.warn("Suppressed exception for ET API exception. Error response: {}".format(reply))
                else:
                    sentry_sdk.capture_message('Error occurred while submitting subscriber to exact target')
                    reg_messages = response.get('messages')
                    # sometimes there are structured errors
                    if len(error_messages):
                        raise exceptions.TriggeredSendException(error_messages[0]['messageErrorStatus'])
                    # sometimes there are plain text errors
                    elif len(reg_messages):
                        raise exceptions.TriggeredSendException(reg_messages[0])
                    else:
                        raise exceptions.TriggeredSendException('Unknown TriggeredSend Error Occurred')
        return reply
