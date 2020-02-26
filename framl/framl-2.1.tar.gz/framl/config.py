import os
from typing import Union
import getpass
import yaml


class Config:

    @staticmethod
    def keys_exist(needles: list, haystack: dict) -> bool:
        for key in needles:
            if not Config.get_key(key, haystack):
                return False
        return True

    @staticmethod
    def get_key(needle: str, haystack: dict) -> Union[None, str, int, dict]:
        pieces = needle.split('.')
        for piece in pieces:
            if piece not in haystack:
                return None
            haystack = haystack[piece]
        return haystack

    @staticmethod
    def value_match(needles: list, key: str, haystack: dict) -> bool:
        value = Config.get_key(key, haystack)
        if not value:
            return False

        if value not in needles:
            return False

        return True
