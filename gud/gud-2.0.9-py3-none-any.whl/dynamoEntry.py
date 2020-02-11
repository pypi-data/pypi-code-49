import json
from .utils import rinse
from .entity import Entity


class DynamoEntry(Entity):

    def __init__(self, group, state):
        super(DynamoEntry, self).__init__(group, state)
        self.type = 'DynamoEntry'
        self.name = group['Group']['name'] + '_dynamoEntry'

        self._requirements = ['Group']
        self._iot_data_plane = Entity._session.client("iot-data")

    def _do_create(self):
        message = {
            "device":self._group['Cores'][0]['name'],
            "type":"D1",
            "var1":"weightF",
            "var2":"waterL",
            "var3":"bay",
            "var4":"weightB"
        }

        response =  self._iot_data_plane.publish(
            topic='d1/register/'+self._group['Cores'][0]['name'],
            payload= json.dumps(message)
        )
        self._state.update('DynamoEntry.config', message)


    def _do_remove(self):
        # to do remove dns entry
        message = {
            "device":self._group['Cores'][0]['name'],
        }

        response =  self._iot_data_plane.publish(
            topic='d1/remove/'+self._group['Cores'][0]['name'],
            payload= json.dumps(message)
        )
