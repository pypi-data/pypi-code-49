import json

class AddToConference(object):
    openapi_types = {
        'conference_id': 'str',
        'call_id': 'str',
        'start_conf_on_enter': 'bool',
        'talk': 'bool',
        'listen': 'bool',
        'leave_conference_url': 'str',
        'notification_url': 'str',
        'allow_call_control': 'bool',
        'call_control_sequence': 'str',
        'call_control_url': 'str'
    }

    attribute_map = {
        'conference_id': 'conference_id',
        'call_id': 'call_id',
        'start_conf_on_enter': 'start_conf_on_enter',
        'talk': 'talk',
        'listen': 'listen',
        'leave_conference_url': 'leave_conference_url',
        'notification_url': 'notification_url',
        'allow_call_control': 'allow_call_control',
        'call_control_sequence': 'call_control_sequence',
        'call_control_url': 'call_control_url'
    }

    def __init__(self, conference_id, call_id):
        self._conference_id = conference_id
        self._call_id = call_id
        self._start_conf_on_enter = None
        self._talk = None
        self._listen = None
        self._leave_conference_url = None
        self._notification_url = None
        self._allow_call_control = None
        self._call_control_sequence = None
        self._call_control_url = None

    @property
    def conference_id(self):
        return self._conference_id

    @property
    def call_id(self):
        return self._call_id

    @property
    def start_conf_on_enter(self):
        return self._start_conf_on_enter

    @property
    def talk(self):
        return self._talk

    @property
    def listen(self):
        return self._listen
    
    @property
    def leave_conference_url(self):
        return self._leave_conference_url

    @property
    def notification_url(self):
        return self._notification_url
 
    @property
    def allow_call_control(self):
        return self._allow_call_control

    @property
    def call_control_sequence(self):
        return self._call_control_sequence

    @property
    def call_control_url(self):
        return self._call_control_url

    @conference_id.setter
    def conference_id(self, conference_id):
        self._conference_id = conference_id

    @call_id.setter
    def call_id(self, call_id):
        self._call_id = call_id

    @start_conf_on_enter.setter
    def start_conf_on_enter(self, start_conf_on_enter):
        self._start_conf_on_enter = start_conf_on_enter

    @talk.setter
    def talk(self, talk):
        self._talk = talk

    @listen.setter
    def listen(self, listen):
        self._listen = listen

    @leave_conference_url.setter
    def leave_conference_url(self, leave_conference_url):
        self._leave_conference_url = leave_conference_url

    @notification_url.setter
    def notification_url(self, notification_url):
        self._notification_url = notification_url

    @allow_call_control.setter
    def allow_call_control(self, allow_call_control):
        self._allow_call_control = allow_call_control

    @call_control_sequence.setter
    def call_control_sequence(self, call_control_sequence):
        self._call_control_sequence = call_control_sequence

    @call_control_url.setter
    def call_control_url(self, call_control_url):
        self._call_control_url = call_control_url

    def to_dict(self):
        as_dict = {
            self.__class__.__name__ : {
                'conference_id': self._conference_id,
                'call_id': self._call_id,
                'start_conf_on_enter': self._start_conf_on_enter,
                'talk': self._talk,
                'listen': self._listen,
                'leave_conference_url': self._leave_conference_url,
                'notification_url': self._notification_url,
                'allow_call_control': self._allow_call_control,
                'call_control_sequence': self._call_control_sequence,
                'call_control_url': self._call_control_url
            }
        }
        return as_dict

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)
