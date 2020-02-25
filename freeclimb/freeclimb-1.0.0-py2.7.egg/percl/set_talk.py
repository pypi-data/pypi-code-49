import json

class SetTalk(object):
    openapi_types = {
        'call_id': 'str',
        'talk': 'bool'
    }

    attribute_map = {
        'call_id': 'call_id',
        'talk': 'talk'
    }

    def __init__(self, call_id):
        self._call_id = call_id
        self._talk = None

    @property
    def call_id(self):
        return self._call_id
    
    @property
    def talk(self):
        return self._talk

    @call_id.setter
    def call_id(self, call_id):
        self._call_id = call_id

    @talk.setter
    def talk(self, talk):
        self._talk = talk
 
    def to_dict(self):
        """Returns the json representation of set_talk"""
        as_dict = {
            self.__class__.__name__ : {
                "call_id": self._call_id,
                "talk": self._talk
            }
        }
        return as_dict

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)
