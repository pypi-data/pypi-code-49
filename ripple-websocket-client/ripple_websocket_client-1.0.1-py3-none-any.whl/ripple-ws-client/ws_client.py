import websocket
import time
import jwt as py_jwt
import mqtt_codec.packet as packet
from io import BytesIO
import ws_callback


class RippleWsClient(object):
    def __init__(self, uri=None, client_id=None, secret=None, callback=None, ws=None, enable_trace=False):
        self._uri = uri
        self._client_id = client_id
        self._secret = secret
        self._ws = ws
        if callback is None:
            self._callback = ws_callback.DefaultRipWebSocketCallback()
        else:
            self._callback = callback
        self._enable_trace = enable_trace

    def uri(self, uri):
        self._uri = uri

    def client_id(self, client_id):
        self._client_id = client_id

    def secret(self, secret):
        self._secret = secret

    def ws(self, ws):
        self._ws = ws

    def get_uri(self):
        return self._uri

    def get_client_id(self):
        return self._client_id

    def get_secret(self):
        return self._secret

    def get_ws(self):
        return self._ws

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
