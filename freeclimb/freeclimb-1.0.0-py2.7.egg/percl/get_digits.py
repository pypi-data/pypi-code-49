import json
from openapi_client.percl.finish_on_key import FinishOnKey

class GetDigits(object):
    openapi_types = {
        'action_url': 'str',
        'initial_max_digits_ms': 'int',
        'digit_max_digits_ms': 'str',
        'finish_on_key': 'str',
        'min_digits': 'int',
        'max_digits': 'int',
        'flush_buffer': 'bool',
        'prompts': 'str'
    }

    attribute_map = {
        'action_url': 'action_url',
        'initial_max_digits_ms': 'initial_max_digits_ms',
        'digit_max_digits_ms': 'digit_max_digits_ms',
        'finish_on_key': 'finish_on_key',
        'min_digits': 'min_digits',
        'max_digits': 'max_digits',
        'flush_buffer': 'flush_buffer',
        'prompts': 'prompts'
    }

    def __init__(self, action_url):
        self._action_url = action_url
        self._initial_max_digits_ms = None
        self._digit_max_digits_ms = None
        finish_on_key_instance = FinishOnKey('')
        self._finish_on_key = finish_on_key_instance.POUND
        self._min_digits = None
        self._max_digits = None
        self._flush_buffer = None
        self._prompts = None

    @property
    def initial_max_digits_ms(self):
        return self._initial_max_digits_ms

    @property
    def digit_max_digits_ms(self):
        return self._digit_max_digits_ms

    @property
    def action_url(self):
        return self._action_url

    @property
    def finish_on_key(self):
        return self._finish_on_key

    @property
    def min_digits(self):
        return self._min_digits
    
    @property
    def max_digits(self):
        return self._max_digits

    @property
    def flush_buffer(self):
        return self._flush_buffer
 
    @property
    def prompts(self):
        return self._prompts

    @initial_max_digits_ms.setter
    def initial_max_digits_ms(self, initial_max_digits_ms):
        self._initial_max_digits_ms = initial_max_digits_ms

    @digit_max_digits_ms.setter
    def digit_max_digits_ms(self, digit_max_digits_ms):
        self._digit_max_digits_ms = digit_max_digits_ms

    @action_url.setter
    def action_url(self, action_url):
        self._action_url = action_url

    @finish_on_key.setter
    def finish_on_key(self, finish_on_key):
        finish_on_key_instance = FinishOnKey('')
        try:
            finish_on_key_code = getattr(finish_on_key_instance, finish_on_key.upper())
        except AttributeError:
            raise ValueError("finish_on_key must be set to the written form of a number from 0-9 or 'STAR'. Default value is 'POUND'")
        self._finish_on_key = finish_on_key_code

    @min_digits.setter
    def min_digits(self, min_digits):
        self._min_digits = min_digits

    @max_digits.setter
    def max_digits(self, max_digits):
        self._max_digits = max_digits

    @flush_buffer.setter
    def flush_buffer(self, flush_buffer):
        self._flush_buffer = flush_buffer

    @prompts.setter
    def prompts(self, prompts):
        self._prompts = prompts

    def to_dict(self):
        as_dict = {
            self.__class__.__name__ : {
                'initial_max_digits_ms': self._initial_max_digits_ms,
                'digit_max_digits_ms': self._digit_max_digits_ms,
                'action_url': self._action_url,
                'finish_on_key': self._finish_on_key,
                'min_digits': self._min_digits,
                'max_digits': self._max_digits,
                'flush_buffer': self._flush_buffer,
                'prompts': self._prompts
            }
        }
        return as_dict

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)
