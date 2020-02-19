# -*- coding: UTF-8 -*
'''
Created on 2018年11月23日

@author: Robin
'''
from __future__ import print_function

__version__ = '1.4.0'


def md5(s):
    import hashlib
    m2 = hashlib.md5()
    m2.update(s.encode("utf8"))
    return m2.hexdigest()


def get_sign(salt, key):
    salt = str(salt)
    key = str(key)
    return md5(md5(salt) + md5(key))


class App(object):
    '''用户应用'''

    def __init__(self, servurl, appid, appkey):
        '''创建需要应用'''
        self.servurl = servurl.rstrip('/')
        self.appid = appid
        self.appkey = appkey

    def doApi(self, apiname, data):
        import requests, json, time
        time = int(time.time())
        data['_appid'] = self.appid
        data['_time'] = time
        data['_sign'] = get_sign(time, self.appkey)

        url = '%s/iot/%s' % (self.servurl, apiname)
        headers = {"Content-Type": "application/json"}
        res = requests.post(url, data=json.dumps(data), headers=headers).json()
        if not res or res['code'] != 0:
            raise Exception('%s:%s' % (res.get('code', -1), res.get('msg', '')))
        return res


class DTU(object):
    def __init__(self, app, dtu_id):
        '''app: 应用对象  dtu_id:DTU的ID(字符串)'''
        self.app = app
        self.dtu_id = str(dtu_id)
        self.running = True

    def doApi(self, apiname, data):
        '''执行API'''
        return self.app.doApi(apiname, data)

    def updateDevices(self, devs):
        '''批量更新多个设备'''
        data = {
            'dtu_id': self.dtu_id,
            'devices': devs,
        }
        return self.doApi('update', data)

    def updateValues(self, dev_id, vals, time=None):
        '''批量更新单个设备的多个值。'''
        dev = {'dev_id': str(dev_id), 'attr': vals}
        if time != None:
            dev['time'] = time
        return self.updateDevices([dev])

    def updateValue(self, dev_id, attr_id, value, time=None):
        '''更新指定设备的指定值。dev_id:设备ID(字符串), attr_id:属性ID(字符串), value:属性值(任意Python类型)，time:时间戳(time.time()获取)'''
        return self.updateValues(dev_id, {str(attr_id): value}, time=time)

    def sendEvent(self, dev_id, evt_id, value='', time=None):
        data = {
            'dtu_id': self.dtu_id,
            'dev_id': dev_id,
            'evt_id': evt_id,
            'value': value,
        }
        if time != None:
            data['time'] = time
        return self.doApi('event', data)

    def stop(self):
        self.running = False


# MQTT
class MQTTClient(object):
    def __init__(self, host='127.0.0.1', port=1883, username=None, password=None):
        import uuid
        from paho.mqtt.client import Client
        self.host = host
        self.port = port
        self.username = username
        self.password = password

        clientid = str(uuid.uuid4())
        self.mqttclient = Client(client_id=clientid, clean_session=True)
        self.mqttclient.on_connect = self._on_connect  # lambda client, userdata, flags, rc: self._on_connect(client, userdata, flags, rc)
        self.mqttclient.on_message = self._on_message  # lambda client, userdata, msg: self._on_message(client, userdata, msg)
        self.mqttclient.on_disconnect = self._on_disconnect
        self.submap = {}
        self.connected = False

    def connect(self):
        import threading
        if self.username:
            self.mqttclient.username_pw_set(self.username, self.password)
        self.mqttclient.connect(self.host, self.port)
        threading.Thread(target=self._forloop).start()

    def disconnect(self):
        self.mqttclient.disconnect()

    def _subscribe(self, topic, qos=0):
        self.mqttclient.subscribe(topic=topic, qos=qos)

    def subscribe(self, topic, qos=0):
        self.submap[topic] = {
            'topic': topic,
            'qos': qos
        }
        if self.connected:
            self._subscribe(topic=topic, qos=qos)

    def publish(self, topic, payload=None, qos=0, retain=False):
        import six
        if not isinstance(payload, six.string_types):
            import json
            payload = json.dumps(payload)
        return self.mqttclient.publish(topic, payload=payload, qos=qos, retain=retain)

    def _forloop(self):
        self.mqttclient.loop_forever()

    def _on_connect(self, client, userdata, flags, rc):
        # print("_on_connect", client, userdata, flags, rc)
        self.connected = True
        for v in self.submap.values():
            self._subscribe(topic=v['topic'], qos=v['qos'])

    def _on_disconnect(self, client, userdata, rc):
        # print("_on_disconnect", client, userdata, rc)
        # if rc != 0:
        #     print('retry')
        self.connected = False

    def _on_message(self, client, userdata, msg):
        import json
        # print("_on_message", client, userdata, msg.topic, msg.payload)
        try:
            self.on_message(msg.topic, json.loads(msg.payload.decode('utf-8')))
        except:
            import traceback
            traceback.print_exc()

    def on_message(self, topic, data):
        pass


class MQTTDTU(DTU):
    def __init__(self, app, dtu_id, mqtt_host='127.0.0.1', mqtt_port=1883):
        '''app: 应用对象  dtu_id:DTU的ID(字符串) mqtt_host:MQTT主机 mqtt_port:MQTT端口'''
        super(MQTTDTU, self).__init__(app, dtu_id)
        self.mqtt_host = mqtt_host
        self.mqtt_port = mqtt_port
        dtu = self

        class Client(MQTTClient):
            def on_message(self, topic, data):
                if not data or type(data) != dict:
                    return
                if not data or type(data) != dict:
                    return
                typename = data.get('type')
                datafrom = data.get('_from')
                topicls = topic.split('/')
                # print(topic, data)
                if len(topicls) == 3:
                    appid, dtu_id, dev_id = topicls
                    if typename == 'action' and data.get('data', {}).get('action'):
                        dtu.on_action(dev_id, action=data['data']['action'], value=data['data'].get('value'))
                    elif typename == 'notify' and data.get('data'):
                        dtu.on_notify(dev_id, data=data['data'])

        client = Client(host=self.mqtt_host, port=self.mqtt_port, username=None, password=None)
        client.connect()
        topic = '%s/%s/#' % (self.app.appid, self.dtu_id)
        client.subscribe(topic)
        self.client = client

    def doApi(self, apiname, data):
        topic = '%s/%s' % (self.app.appid, self.dtu_id)
        return self.client.publish(topic, {'type': apiname, 'data': data})

    def stop(self):
        super(MQTTDTU, self).stop()
        self.client.disconnect()

    def on_action(self, dev_id, action, value=None):
        '''执行动作'''
        print('on_action', dev_id, action, value)

    def on_notify(self, dev_id, data):
        '''通知'''
        print('on_notify', dev_id, data)

    def sendNotify(self, dev_id, data):
        '''发送通知'''
        topic = '%s/%s/%s' % (self.app.appid, self.dtu_id, dev_id)
        return self.client.publish(topic, {'type': 'notify', 'data': data})


def test():
    # 需python requests包，如果没安装的话执行: pip install requests
    import time
    # servurl = 'https://xiot.inruan.com/'
    servurl = 'http://127.0.0.1:8080/'
    app = App(servurl, 'xt15429507412810938', '775563e1cce37176cc33aa5d053d9e07')

    # 创建DTU对象
    dtu = DTU(app, 'dtu1')

    # print(dtu.updateValue('dev1', 'voltage', int(time.time()) % 50 / 10.0))
    # return

    class TestMQTTDTU(MQTTDTU):
        def on_action(self, dev_id, action, value=None):
            print(dev_id, action, value)

    # dtu = TestMQTTDTU(app, 'dtu2', mqtt_host='172.16.1.142')

    import signal
    def stop(a, b):
        print('stop')
        dtu.stop()

    signal.signal(signal.SIGINT, stop)
    import random
    while dtu.running:
        try:
            # print(dtu.updateValue('dev3', 'time', int(time.time()) - 1545700000 - 6442565))
            # print(dtu.sendEvent(dev_id='dev1', evt_id=random.choices(['normal', 'warn', 'error'])[0], value=random.choices(['电压过低设备警告', '未知故障', '紧急报警'])[0]))
            # print(dtu.updateValue('dev1', 'time', int(time.time()) - 1545700000 - 6442565))
            print(dtu.updateValue('dev1', 'status', 'error'))
            time.sleep(5)
            print(dtu.updateValue('dev1', 'status', 'connected'))
            time.sleep(5)
            print(dtu.updateValue('dev1', 'status', 'warning'))
            time.sleep(5)
        except:
            import traceback
            traceback.print_exc()
        ct = 1
        while ct and dtu.running:
            time.sleep(0.5)
            ct -= 1


if __name__ == '__main__':
    test()
