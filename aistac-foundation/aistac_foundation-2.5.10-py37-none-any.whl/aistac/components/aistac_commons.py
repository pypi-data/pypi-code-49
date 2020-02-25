from datetime import datetime
from typing import Any

__author__ = 'Darryl Oatridge'


class AistacCommons(object):

    @staticmethod
    def list_formatter(value: Any) -> list:
        """ Useful utility method to convert any type of str, list, tuple or pd.Series into a list"""
        if isinstance(value, (int, float, str, datetime)):
            return [value]
        if isinstance(value, (list, tuple, set)):
            return list(value)
        if isinstance(value, dict):
            return list(value.items())
        return list()
