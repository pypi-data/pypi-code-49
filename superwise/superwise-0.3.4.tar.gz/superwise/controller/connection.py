"""
Connection module
"""
import json
import logging

import requests

from superwise.config import Config
from superwise.exceptions.superwise_exceptions import SuperwiseConnectionError


class Connection:
    """
    Connection class aims to manage connection with superwise
    """
    def __init__(self, token: str):
        """
        create connection for user
        :type token: token of user
        """
        self._logger = logging.getLogger('superwise')
        self._token = token

    def login(self):
        """
        create session object and update token for user
        :return: return requests session object with contains jwt from superwise.
        """
        self._logger.debug(f"start work with superwise using token {self._token}")
        session = requests.session()
        session.headers.update({'Authorization': 'Bearer ' + self._token})
        self._logger.info("Logg")
        return session

