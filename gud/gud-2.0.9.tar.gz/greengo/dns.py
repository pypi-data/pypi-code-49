import json
from .utils import rinse
from .entity import Entity


class Dns(Entity):

    def __init__(self, group, state):
        super(Dns, self).__init__(group, state)
        self.type = 'DNS'
        self.name = group['Group']['name'] + '_dns'

        self._requirements = ['Group']
        self._iot_data_plane = Entity._session.client("iot-data")

    def _do_create(self):
        message = {
          'hostname': self._group['Cores'][0]['name']+'.dyn.doop.co.nz.', 
          'record_type': 'A',
          'ttl': 60,
          'shared_secret': self._group['DNS']['secret'],
          'lock_record': False, 
          'read_privilege': False, 
          'allow_internal': True,
        }

        response =  self._iot_data_plane.publish(
            topic='d1/dnsregister/'+self._group['Cores'][0]['name'],
            payload= json.dumps(message)
        )
        self._state.update('DNS.config', message)


    def _do_remove(self):
        # to do remove dns entry
        return
        # message = {
        #   'hostname': self._group['Cores'][0]['name']+'.dyn.doop.co.nz.', 
        #   'record_type': 'A',
        #   'ttl': 60,
        #   'shared_secret': self._group['DNS']['secret'],
        #   'lock_record': False, 
        #   'read_privilege': False, 
        #   'allow_internal': True,
        # }

        # response =  self._iot_data_plane.publish(
        #     topic='d1/dnsregister/'+self._group['Cores'][0]['name'],
        #     payload= json.dumps(message)
        # )
        # self._state.update('DNS.config', message)
