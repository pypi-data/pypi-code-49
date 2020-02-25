import json

class Enqueue(object):
    openapi_types = {
        'queue_id': 'str',
        'action_url': 'str',
        'wait_url': 'str',
        'notification_url': 'str'
    }

    attribute_map = {
        'queue_id': 'queue_id',
        'action_url': 'action_url',
        'wait_url': 'wait_url',
        'notification_url': 'notification_url'
    }

    def __init__(self, queue_id, action_url):
        self._queue_id = queue_id
        self._action_url = action_url
        self._wait_url = None
        self._notification_url = None

    @property
    def queue_id(self):
        return self._queue_id

    @property
    def action_url(self):
        return self._action_url

    @property
    def wait_url(self):
        return self._wait_url

    @property
    def notification_url(self):
        return self._notification_url

    @queue_id.setter
    def queue_id(self, queue_id):
        self._queue_id = queue_id

    @action_url.setter
    def action_url(self, action_url):
        self._action_url = action_url

    @wait_url.setter
    def wait_url(self, wait_url):
        self._wait_url = wait_url

    @notification_url.setter
    def notification_url(self, notification_url):
        self._notification_url = notification_url

    def to_dict(self):
        as_dict = {
            self.__class__.__name__ : {
                'queue_id': self._queue_id,
                'action_url': self._action_url,
                'wait_url': self._wait_url,
                'notification_url': self._notification_url
            }
        }
        return as_dict

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)
