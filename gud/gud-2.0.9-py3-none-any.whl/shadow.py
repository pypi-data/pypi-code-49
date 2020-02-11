import json
from .utils import rinse
from .entity import Entity


class Shadow(Entity):

    def __init__(self, group, state):
        super(Shadow, self).__init__(group, state)
        self.type = 'Shadow'
        self.name = group['Group']['name'] + '_shadow'

        self._requirements = ['Group']
        self._iot_data_plane = Entity._session.client("iot-data")

    def _do_create(self):
        exists = os.path.isfile('./initShadow.json')
        if exists:
            f = open('./initShadow.json', encoding='utf-8')
            text = f.read()    # unicode, not bytes
            response = self._iot_data_plane.update_thing_shadow(
                thingName=self._group['Cores'][0]['name'],
                payload=text
            )
        else:
            print("No file named initShadow.json defined !")

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
