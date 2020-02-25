import json

class Redirect(object):
    openapi_types = {
        'action_url': 'int'
    }

    attribute_map = {
        'action_url': 'action_url'
    }

    def __init__(self, action_url):
        self._action_url = action_url

    @property
    def action_url(self):
        return self._action_url

    @action_url.setter
    def action_url(self, action_url):
        self._action_url = action_url
 
    def to_dict(self):
        """Returns the json representation of redirect"""
        as_dict = {
            self.__class__.__name__ : {
                "action_url": self._action_url
            }
        }
        return as_dict

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)
