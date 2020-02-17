from imis.manager import BasicManager
from imis.record import GenericEntityDataRecord

import requests


class Manager(BasicManager):

    def __init__(self, client, object_name):
        self.object_name = object_name
        super().__init__(client)

    @property
    def service_url(self):
        return '{0}/api/{1}'.format(self.client.url, self.object_name)

    def fetch_raw_data(self, imis_id=None, offset=0):
        return super().fetch_raw_data(object_name=self.object_name, imis_id=imis_id, offset=offset)

    def fetch_record(self, imis_id):
        api_data = self.fetch_raw_data(imis_id=imis_id)
        return GenericEntityDataRecord(api_data)

    def update_raw_data(self, imis_id, data):
        return super().update_raw_data(object_name=self.object_name,
                                       imis_id=imis_id, data=data)

    def update_record(self, generic_entity_data_record):
        return self.update_raw_data(imis_id=generic_entity_data_record.primary_identifier,
                                    data=generic_entity_data_record.api_data)
