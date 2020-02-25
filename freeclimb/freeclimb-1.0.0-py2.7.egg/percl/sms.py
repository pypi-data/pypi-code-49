import json

class Sms(object):
    openapi_types = {
        'to': 'str',
        'from': 'str',
        'text': 'str',
        'notification_url': 'str'
    }

    attribute_map = {
        'to': 'to',
        'from': 'from',
        'text': 'text',
        'notification_url': 'notification_url'
    }

    def __init__(self, to, from, text):
        self._to = to
        self._from = from
        self._text = text
        self._notification_url = None

    @property
    def to(self):
        return self._to
    
    @property
    def from(self):
        return self._from

    @property
    def notification_url(self):
        return self._notification_url
    
    @property
    def text(self):
        return self._text

    @to.setter
    def to(self, to):
        self._to = to

    @from.setter
    def from(self, from):
        self._from = from
    
    @notification_url.setter
    def notification_url(self, notification_url):
        self._notification_url = notification_url
    
    @text.setter
    def text(self, text):
        self._text = text
 
    def to_dict(self):
        """Returns the dictionary representation of sms"""
        as_dict = {
            self.__class__.__name__ : {
                "from": self._from,
                "to": self._to,
                "text": self._text,
                "notificationUrl": self._notification_url 
            }
        }
        return as_dict

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)
