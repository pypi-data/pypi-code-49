""" Anonymous Device Client (calls Anonymous TEEM API) """

import os
import uuid
import platform
from time import time
from datetime import datetime

from f5teem.constants import ENVIRONMENTS, ENDPOINTS
from f5teem.utils import http_utils
from f5teem.exceptions import EnvironmentInputError

class AnonymousDeviceClient(object):
    """Anonymous Device Client Class

    Attributes
    ----------

    Methods
    -------
    """

    def __init__(self, client_info, **kwargs):
        """Class initialization

        Parameters
        ----------
        client_info : str
            client information
        **kwargs :
            optional keyword arguments

        Keyword Arguments
        -----------------
        api_key : str
            the api key to use

        Returns
        -------
        None
        """

        self._endpoint_info = self._get_endpoint_info()

        self._client_info = client_info
        self._api_key = kwargs.pop('api_key', self._endpoint_info['api_key'])

        self._telemetry_type = None
        self._telemetry_type_version = None

        self._service_host = self._endpoint_info['endpoint']

    @staticmethod
    def _get_endpoint_info():
        """Get endpoint information

        Parameters
        ----------
        None

        Returns
        -------
        str
            service host to use
        """

        environment = os.environ.get(ENVIRONMENTS['env_var']) or ENVIRONMENTS['published'][0]

        # validate environment is valid
        if environment not in ENVIRONMENTS['published']:
            raise EnvironmentInputError(
                'Environment must be one of {}'.format(ENVIRONMENTS['published'])
            )

        return ENDPOINTS['anonymous'][environment]

    def report(self, telemetry, **kwargs):
        """Class initialization

        Parameters
        ----------
        telemetry : dict
            telemetry record to send
        **kwargs :
            optional keyword arguments

        Keyword Arguments
        -----------------
        telemetry_type : str
            the telemetry type to use
        telemetry_type_version : str
            the telemetry type version to use

        Returns
        -------
        None
        """

        self._telemetry_type = kwargs.pop('telemetry_type', None)
        self._telemetry_type_version = kwargs.pop('telemetry_type_version', None)

        telemetry.update({
            'telemetryClientProperties': {
                'os': platform.system()
            }
        })

        return http_utils.make_request(
            self._service_host,
            '/ee/v1/telemetry',
            method='POST',
            headers={
                'F5-ApiKey': self._api_key,
                'F5-DigitalAssetId': self._client_info.get('id'),
                'F5-TraceId': str(uuid.uuid4())
            },
            body={
                'digitalAssetName': self._client_info.get('name'),
                'digitalAssetVersion': self._client_info.get('version'),
                'digitalAssetId': self._client_info.get('id'),
                'documentType': self._telemetry_type,
                'documentVersion': self._telemetry_type_version,
                'observationStartTime': datetime.now().isoformat(),
                'observationEndTime': datetime.now().isoformat(),
                'epochTime': time(),
                'telemetryId': str(uuid.uuid4()),
                'telemetryRecords': [telemetry]
            }
        )
