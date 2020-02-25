import json

class Play(object):
    openapi_types = {
        'file': 'str',
        'loop': 'int',
        'conference_id': 'str'
    }

    attribute_map = {
        'file': 'file',
        'loop': 'loop',
        'conference_id': 'conference_id'
    }

    def __init__(self, file):
        self._file = file
        self._loop = None
        self._conference_id = None

    @property
    def file(self):
        return self._file
    
    @property
    def loop(self):
        return self._loop

    @property
    def conference_id(self):
        return self._conference_id

    @file.setter
    def file(self, file):
        self._file = file

    @loop.setter
    def loop(self, loop):
        self._loop = loop

    @conference_id.setter
    def conference_id(self, conference_id):
        self._conference_id = conference_id
 
    def to_dict(self):
        """Returns the json representation of play"""
        as_dict = {
            self.__class__.__name__ : {
                "file": self._file,
                "loop": self._loop,
                "conference_id": self._conference_id
            }
        }
        return as_dict

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)
