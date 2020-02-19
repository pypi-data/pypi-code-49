import json

from sixgill.sixgill_request_classes.sixgill_auth_request import SixgillAuthRequest
from sixgill.sixgill_request_classes.sixgill_base_request import SixgillBaseRequest
from sixgill.sixgill_exceptions import BadResponseException, AuthException
from sixgill.sixgill_utils import get_logger
from sixgill.sixgill_constants import VALID_STATUS_CODES
import traceback
import requests


class SixgillBaseClient(object):

    def __init__(self, client_id, client_secret, channel_id, logger=None, bulk_size=1000, session=None):
        self.client_id = client_id
        self.client_secret = client_secret
        self.channel_id = channel_id
        self.logger = get_logger(self.__class__.__name__) if logger is None else logger
        self.bulk_size = bulk_size
        self.session = session if session else requests.Session()

    def _send_request(self, sixgill_api_request: SixgillBaseRequest):
        try:
            response = self.session.send(request=sixgill_api_request.prepare(), verify=False)

            if response.status_code not in VALID_STATUS_CODES:
                self.logger.error(f'Error in API call [{response.status_code}] - {response.reason}')
                raise BadResponseException(status_code=response.status_code, reason=response.reason, url=response.url,
                                           method=response.request.method)

            return response.json()

        except json.decoder.JSONDecodeError as e:
            self.logger.error(f'Failed parsing response {e}')
            raise

        except Exception as e:
            self.logger.error(f'Error {e}, traceback: {traceback.format_exc()}')
            raise

    def _get_access_token(self) -> str:
        try:
            response = self.session.send(request=SixgillAuthRequest(self.client_id, self.client_secret).prepare(),
                                         verify=False)

            if response.status_code not in VALID_STATUS_CODES:
                raise AuthException(status_code=response.status_code, reason=response.reason, url=response.url,
                                    method=response.request.method)

            json_response = response.json()
            return json_response.get('access_token')

        except Exception as e:
            self.logger.error(f'Failed getting access token: {e}, traceback: {traceback.format_exc()}')
            raise
