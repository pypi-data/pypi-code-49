import json
from openapi_client.percl.play_beep import PlayBeep

class CreateConference(object):
    openapi_types = {
        'alias': 'str',
        'play_beep': 'str',
        'action_url': 'str',
        'status_callback_url': 'str',
        'wait_url': 'str',
        'record': 'bool'
    }

    attribute_map = {
        'alias': 'alias',
        'play_beep': 'play_beep',
        'action_url': 'action_url',
        'status_callback_url': 'status_callback_url',
        'wait_url': 'wait_url',
        'record': 'record'
    }

    def __init__(self, action_url):
        self._action_url = action_url
        self._alias = None
        play_beep_instance = PlayBeep('')
        self._play_beep = play_beep_instance.ALWAYS
        self._wait_url = None
        self._record = None
        self._status_callback_url = None

    @property
    def alias(self):
        return self._alias

    @property
    def play_beep(self):
        return self._play_beep

    @property
    def action_url(self):
        return self._action_url

    @property
    def wait_url(self):
        return self._wait_url

    @property
    def record(self):
        return self._record
 
    @property
    def status_callback_url(self):
        return self._status_callback_url

    @alias.setter
    def alias(self, alias):
        self._alias = alias

    @play_beep.setter
    def play_beep(self, play_beep):
        play_beep_instance = PlayBeep('')
        try:
            play_beep_code = getattr(play_beep_instance, play_beep.upper())
            self._play_beep = play_beep_code
        except AttributeError:
            raise ValueError("Within conferences, play_beep must be set to one of the following values: 'ALWAYS', 'NEVER', 'ENTRY_ONLY', OR 'EXIT_ONLY'. Default value is 'ALWAYS'")

    @action_url.setter
    def action_url(self, action_url):
        self._action_url = action_url

    @wait_url.setter
    def wait_url(self, wait_url):
        self._wait_url = wait_url

    @record.setter
    def record(self, record):
        self._record = record

    @status_callback_url.setter
    def status_callback_url(self, status_callback_url):
        self._status_callback_url = status_callback_url

    def to_dict(self):
        as_dict = {
            self.__class__.__name__ : {
                'alias': self._alias,
                'play_beep': self._play_beep,
                'action_url': self._action_url,
                'wait_url': self._wait_url,
                'record': self._record,
                'status_callback_url': self._status_callback_url
            }
        }
        return as_dict

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)
