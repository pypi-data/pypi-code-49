import json
from openapi_client.percl.finish_on_key import FinishOnKey

class RecordUtterance(object):
    openapi_types = {
        'action_url': 'str',
        'silence_timeout_ms': 'int',
        'finish_on_key': 'str',
        'max_length_sec': 'int',
        'play_beep': 'bool',
        'auto_start': 'bool'
    }

    attribute_map = {
        'action_url': 'action_url',
        'silence_timeout_ms': 'silence_timeout_ms',
        'finish_on_key': 'finish_on_key',
        'max_length_sec': 'max_length_sec',
        'play_beep': 'play_beep',
        'auto_start': 'auto_start'
    }

    def __init__(self, action_url):
        self._action_url = action_url
        self._silence_timeout_ms = None
        finish_on_key_instance = FinishOnKey('')
        self._finish_on_key = finish_on_key_instance.POUND
        self._max_length_sec = None
        self._play_beep = None
        self._auto_start = None

    @property
    def silence_timeout_ms(self):
        return self._silence_timeout_ms

    @property
    def action_url(self):
        return self._action_url

    @property
    def finish_on_key(self):
        return self._finish_on_key

    @property
    def max_length_sec(self):
        return self._max_length_sec
    
    @property
    def play_beep(self):
        return self._play_beep

    @property
    def auto_start(self):
        return self._auto_start

    @silence_timeout_ms.setter
    def silence_timeout_ms(self, silence_timeout_ms):
        self._silence_timeout_ms = silence_timeout_ms

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

    @max_length_sec.setter
    def max_length_sec(self, max_length_sec):
        self._max_length_sec = max_length_sec

    @play_beep.setter
    def play_beep(self, play_beep):
        self._play_beep = play_beep

    @auto_start.setter
    def auto_start(self, auto_start):
        self._auto_start = auto_start

    def to_dict(self):
        as_dict = {
            self.__class__.__name__ : {
                'silence_timeout_ms': self._silence_timeout_ms,
                'digit_play_beep_ms': self._digit_play_beep_ms,
                'action_url': self._action_url,
                'finish_on_key': self._finish_on_key,
                'max_length_sec': self._max_length_sec,
                'play_beep': self._play_beep,
                'auto_start': self._auto_start
            }
        }
        return as_dict

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)
