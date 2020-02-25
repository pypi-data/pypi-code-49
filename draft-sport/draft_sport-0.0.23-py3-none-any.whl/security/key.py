"""
Draft Sport
API Key Module
author: hugh@blinkybeach.com
"""
from draft_sport.errors.type import DSTypeError


class ApiKey:

    def __init__(self, key: str) -> None:

        DSTypeError.assert_type(key, 'key', str)

        self._key = key

        return
