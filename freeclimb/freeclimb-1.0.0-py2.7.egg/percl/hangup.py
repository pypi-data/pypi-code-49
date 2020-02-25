import json

class Hangup(object):
    openapi_types = {
        'call_id': 'str',
        'reason': 'str'
    }

    attribute_map = {
        'call_id': 'call_id',
        'reason': 'reason'
    }

    def __init__(self):
        self._call_id = None
        self._reason = None

    @property
    def call_id(self):
        return self._call_id
    
    @property
    def reason(self):
        return self._reason

    @call_id.setter
    def call_id(self, call_id):
        self._call_id = call_id

    @reason.setter
    def reason(self, reason):
        self._reason = reason
 
    def to_dict(self):
        """Returns the json representation of hangup"""
        as_dict = {
            self.__class__.__name__ : {
                "call_id": self._call_id,
                "reason": self._reason
            }
        }
        return as_dict

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)
