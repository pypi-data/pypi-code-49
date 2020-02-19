import websocket
import time
import jwt as py_jwt
import mqtt_codec.packet as packet
from io import BytesIO
from abc import ABCMeta, abstractmethod
import mqtt_codec.io


class RipWebSocketCallback(metaclass=ABCMeta):

    def on_open(self):
        self.connected()

    def on_message(self, *args):
        message = args[0]
        header = packet.MqttFixedHeader.decode(mqtt_codec.io.BytesReader(message))
        fixed_header = header[1]
        msg_type = int(fixed_header.packet_type)
        if msg_type == packet.MqttControlPacketType.publish:
            publish_msg = packet.MqttPublish.decode(mqtt_codec.io.BytesReader(message))
            payload = str(publish_msg[1].payload)
            self.receive(payload)
        elif msg_type == packet.MqttControlPacketType.puback:
            pub_ack_msg = packet.MqttPuback.decode(mqtt_codec.io.BytesReader(message))
            self.ack(pub_ack_msg[1].packet_id)

    def on_close(self):
        self.closed()

    def on_pong(self, *args):
        pass

    def on_error(self, *args):
        self.error(*args)

    @abstractmethod
    def connected(self):
        pass

    @abstractmethod
    def receive(self, message):
        pass

    @abstractmethod
    def ack(self, msg_id):
        pass

    @abstractmethod
    def closed(self):
        pass

    @abstractmethod
    def error(self, *args):
        pass


class DefaultRipWebSocketCallback(RipWebSocketCallback):

    def connected(self):
        print('connected')

    def receive(self, message):
        print('receive:' + message)

    def ack(self, msg_id):
        print('ack:' + str(msg_id))

    def closed(self):
        print("closed")

    def error(self, *args):
        print("error:" + str(args))


class RippleWsClient(object):
    def __init__(self, uri=None, client_id=None, secret=None, callback=None, ws=None, enable_trace=False):
        self._uri = uri
        self._client_id = client_id
        self._secret = secret
        self._ws = ws
        if callback is None:
            self._callback = DefaultRipWebSocketCallback()
        else:
            self._callback = callback
        self._enable_trace = enable_trace

    def connect(self):
        websocket.enableTrace(self._enable_trace)
        exp_time = int(round(time.time() * 1000)) + 604800000
        token = py_jwt.encode({'client_id': self._client_id, 'client_type': 2, 'exp': exp_time},
                              self._secret,
                              algorithm='HS256', headers={'alg': 'HS512', "typ": "JWT"})
        self._ws = websocket.WebSocketApp(self._uri,
                                          header=["Authorization:Bearer " + token.decode("utf-8")],
                                          on_message=self._callback.on_message,
                                          on_error=self._callback.on_error,
                                          on_close=self._callback.on_close,
                                          on_pong=self._callback.on_pong,
                                          on_open=self._callback.on_open)
        self._ws.run_forever(ping_interval=15)
        return self

    def close(self):
        if not self.closed():
            self._ws.sock.close()

    def closed(self):
        if not self._ws:
            return self._ws.sock.connected
        return True

    def publish(self, msg_id, payload):
        if not self.closed():
            print('send:{}-{}'.format(str(msg_id), str(payload)))
            pub_msg = packet.MqttPublish(msg_id, self._client_id, bytes(payload, 'UTF-8'), True, 1, True)
            with BytesIO() as f:
                pub_msg.encode(f)
            buf = f.getvalue()
            self._ws.sock.send_binary(buf)
