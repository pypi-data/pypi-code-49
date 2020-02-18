"""
Mixins used for backend requests.
The mixins aim to reduce the complexity of the requests classes rather than
creating reusable classes
"""
import json
import logging
import os

import requests

from ..core import constants, utils


class _RequestsMixin:
    """`_RequestsMixin` handles urls generation, error handling and
    common headers for requests to DISCO backend.
    """
    MAX_500_RETRIES = 3
    # 504 is skipped as it it usually caused by long/big requests
    HANDLED_500_CODES = {500, 502}

    @staticmethod
    def handle_500_errors(src_function):
        """Wraps function and retries on 500 errors.
        Args:
            src_function: Function to be executed and retried.

        Returns:
            Wrapped function.
        """

        def _try(*args, **kwargs):
            last_error = None
            for _ in range(_RequestsMixin.MAX_500_RETRIES):
                try:
                    return src_function(*args, **kwargs)
                except requests.HTTPError as http_error:

                    status = http_error.response.status_code
                    if status in _RequestsMixin.HANDLED_500_CODES:
                        logging.warning("Got %s error during request to %s",
                                        status, http_error.response.url)
                        last_error = http_error
                    else:
                        raise
            raise last_error

        return _try

    @classmethod
    def _raw_base_url(cls):
        #Retrieves the base url from various data sources (env, file, default)
        #return: The base url **configured** for DISCO requests
        environ_base_url = os.environ.get(constants.ENV_VAR_BASE_URL_NAME)
        if environ_base_url is not None:
            return environ_base_url

        if constants.DISCO_CONFIG_PATH.exists():
            conf_file = json.loads(
                constants.DISCO_CONFIG_PATH.read_text())
            return conf_file.get('base_url', constants.DEFAULT_BASE_URL)

        return constants.DEFAULT_BASE_URL

    @classmethod
    def base_url(cls):
        """Provides the base url to be used for requests made to
        DISCOs backend.

        Returns:
            str: Base url for DISCO backend server.
        """
        b_url = cls._raw_base_url()
        # allow the old suffix in configuration for backward compatibility
        b_url = utils.str_without_suffix(b_url, '/')
        b_url = utils.str_without_suffix(b_url, constants.REST_API_SUFFIX)
        return b_url

    @classmethod
    def get_graphql_endpoint(cls):
        """Url url for DISCO GQL requests.

        Returns:
            str: Base url for DISCO GQL requests.
        """
        return '/'.join([cls.base_url(), 'graphql'])

    @classmethod
    def get_rest_endpoint(cls, path):
        """Builds url for REST request to the backend servers.

        Returns:
            str: Url for specific REST url.
        """
        rest_part = utils.str_without_prefix(constants.REST_API_SUFFIX)
        path_part = utils.str_without_prefix(path, '/')
        return '/'.join([cls.base_url(), rest_part, path_part])

    @property
    def disco_headers(self):
        """Default headers for REST/GQL request.

        Returns:
            dict: Dictionary of headers.
        """
        return {
            'User-Agent': f"disco-python-sdk version={utils.disco_version()}" \
                f" request_id={self.request_id}"

        }
