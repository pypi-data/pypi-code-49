import json

class SendDigits(object):
    openapi_types = {
        'digits': 'str',
        'pause_ms': 'int'
    }

    attribute_map = {
        'digits': 'digits',
        'pause_ms': 'pause_ms'
    }

    def __init__(self, digits):
        self._digits = digits
        self._pause_ms = None

    @property
    def digits(self):
        return self._digits
    
    @property
    def pause_ms(self):
        return self._pause_ms

    @digits.setter
    def digits(self, digits):
        self._digits = digits

    @pause_ms.setter
    def pause_ms(self, pause_ms):
        self._pause_ms = pause_ms
 
    def to_dict(self):
        """Returns the json representation of send_digits"""
        as_dict = {
            self.__class__.__name__ : {
                "digits": self._digits,
                "pause_ms": self._pause_ms
            }
        }
        return as_dict

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)
