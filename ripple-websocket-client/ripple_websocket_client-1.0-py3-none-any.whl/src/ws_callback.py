from abc import ABCMeta, abstractmethod
import mqtt_codec.packet as packet
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
