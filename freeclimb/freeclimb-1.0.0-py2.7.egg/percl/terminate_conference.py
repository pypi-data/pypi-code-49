import json

class TerminateConference(object):
    openapi_types = {
        'conference_id': 'str'
    }

    attribute_map = {
        'conference_id': 'conference_id'
    }

    def __init__(self, conference_id):
        self._conference_id = conference_id

    @property
    def conference_id(self):
        return self._conference_id

    @conference_id.setter
    def conference_id(self, conference_id):
        self._conference_id = conference_id

    def to_dict(self):
        """Returns the json representation of terminate_conference"""
        as_dict = {
            self.__class__.__name__ : {
                "conference_id": self._conference_id
            }
        }
        return as_dict

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)
