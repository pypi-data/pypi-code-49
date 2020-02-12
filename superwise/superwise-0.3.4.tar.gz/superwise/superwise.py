import logging
import os

from superwise.controller.connection import Connection
from superwise.controller.trace import Trace
from superwise.exceptions.superwise_exceptions import SuperwiseDataError, SuperwiseENVError
from superwise.validations.superwise_validator import valid_trace_prediction_batch, valid_trace_prediction_emit


class Superwise:

    def __init__(self, token=None):
        """
        Create connection to working with superwise sdk.
        :param sw_username:
        :param sw_password:
        """
        self._logger = logging.getLogger('superwise')
        self._token,self._host = self._fetch_user_params(token)
        self._session = Connection(token=self._token).login()
        self.trace = Trace(self._session, self._token,self._host)

    @staticmethod
    def _fetch_user_params(token) -> (str,str):
        host = os.environ.get("SW_HOST")
        if host is None:
            raise SuperwiseENVError("problem fetch SW_HOST environment variable")
        if token is not None:
            return token
        token = os.environ.get("SW_TOKEN")

        if token is None:
            raise SuperwiseENVError("problem fetch SW_TOKEN environment variable")
        return token, host

    @staticmethod
    def validate_prediction_emit_req(data):
        """
        validate data getting from user is in the right format.
        :param data: single record of data from user
        :return: Boolean, Error
        """
        if valid_trace_prediction_emit(data):
            return True
        raise SuperwiseDataError("Data don't in the right format..")

    @staticmethod
    def validate_prediction_batch_req(data):
        """
           validate data getting from user is in the right format.
           :param data: multiple record of data from user
           :return: Boolean, Error
       """
        if valid_trace_prediction_batch(data):
            return True
        raise SuperwiseDataError("Data don't in the right format..")
