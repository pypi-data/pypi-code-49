import json

class Pause(object):
    openapi_types = {
        'length': 'int'
    }

    attribute_map = {
        'length': 'length'
    }

    def __init__(self, length):
        self._length = length

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, length):
        self._length = length
 
    def to_dict(self):
        """Returns the json representation of pause """
        as_dict = {
            self.__class__.__name__ : {
                "length": self._length
            }
        }
        return as_dict

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)
