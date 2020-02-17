import requests

from imis.manager import BasicManager


class Manager(BasicManager):

    object_name = 'Party'

    def fetch_raw_data(self, imis_id=None):
        return super().fetch_raw_data(object_name=Manager.object_name, imis_id=imis_id)

    def update_raw_data(self, imis_id=None, data=None):
        return super().update_raw_data(object_name=Manager.object_name,
                                       imis_id=imis_id, data=data)
