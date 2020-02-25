import json

class PlayEarlyMedia(object):
    openapi_types = {
        'file': 'str'
    }

    attribute_map = {
        'file': 'file'
    }

    def __init__(self, file):
        self._file = file

    @property
    def file(self):
        return self._file

    @file.setter
    def file(self, file):
        self._file = file

    def to_dict(self):
        """Returns the json representation of play"""
        as_dict = {
            self.__class__.__name__ : {
                "file": self._file
            }
        }
        return as_dict

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)
