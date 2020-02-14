from imis.manager import BasicManager

import requests


class Manager(BasicManager):

    def __init__(self, client, object_name):
        self.object_name = object_name
        super().__init__(client)

    def fetch_raw_data(self, imis_id=None):
        return super().fetch_raw_data(object_name=self.object_name, imis_id=imis_id)

    def update_raw_data(self, imis_id, data):
        return super().update_raw_data(object_name=self.object_name,
                                       imis_id=imis_id, data=data)
