import json

class RemoveFromConference(object):
    openapi_types = {
        'call_id': 'str'
    }

    attribute_map = {
        'call_id': 'call_id'
    }

    def __init__(self, call_id):
        self._call_id = call_id

    @property
    def call_id(self):
        return self._call_id

    @call_id.setter
    def call_id(self, call_id):
        self._call_id = call_id
 
    def to_dict(self):
        """Returns the json representation of remove_from_conference"""
        as_dict = {
            self.__class__.__name__ : {
                "call_id": self._call_id
            }
        }
        return as_dict

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)
