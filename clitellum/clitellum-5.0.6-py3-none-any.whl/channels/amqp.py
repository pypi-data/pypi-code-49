import socket

import librabbitmq

from clitellum import logger_manager

from clitellum.channels.configuration import ChannelConfiguration
from clitellum.exceptions import ConnectionException
import threading


class AmqpMessageProperties:
    """
    Propiedades de los mensajes amqp
    """
    def __init__(self):
        self.content_type = 'application/json'
        self.content_encoding = 'utf-8'
        self.headers = dict()
        self.delivery_mode = 2
        self.priority = 0
        self.correlation_id = None
        self.reply_to = None
        self.expiration = None
        self.app_id = None
        self.message_id = None

    def to_dict(self):
        """
        Convierte la propiedades en un objeto del tipo pika BasicProperties
        para el envio del mensaje
        :return: pika.BasicProperties
        """
        properties = dict()
        if self.content_type is not None:
            properties['content_type'] = self.content_type

        if self.content_encoding is not None:
            properties['content_encoding'] = self.content_encoding

        if self.headers is not None and len(self.headers) > 0:
            properties['headers'] = self.headers

        properties['delivery_mode'] = self.delivery_mode
        properties['priority'] = self.priority

        if self.correlation_id is not None:
            properties['correlation_id'] = self.correlation_id

        if self.reply_to is not None:
            properties['reply_to'] = self.reply_to

        if self.expiration is not None:
            properties['expiration'] = self.expiration

        if self.app_id is not None:
            properties['app_id'] = self.app_id

        if self.message_id is not None:
            properties['message_id'] = self.message_id

        return properties

    @classmethod
    def from_basic_properties(cls, properties):
        """
        Crea una instancia de AmqpMessageProperties a partir de las BasicProperties
        recibidas
        :param properties: propiedades
        :return:
        """
        amp = AmqpMessageProperties()
        amp.content_encoding = properties['content_encoding'] if 'content_encoding' in properties else None
        amp.message_id = properties['message_id'] if 'message_id' in properties else None
        amp.reply_to = properties['reply_to'] if 'reply_to' in properties else None
        amp.app_id = properties['app_id'] if 'app_id' in properties else None
        amp.expiration = properties['expiration'] if 'expiration' in properties else None
        amp.correlation_id = properties['correlation_id'] if 'correlation_id' in properties else None
        amp.priority = properties['priority'] if 'priority' in properties else None
        amp.headers = properties['headers'] if 'headers' in properties else None
        amp.content_type = properties['content_type'] if 'content_type' in properties else None
        return amp

    @classmethod
    def create(cls):
        properties = AmqpMessageProperties()
        properties.delivery_mode = 2
        return properties


class AmqpMesageFrame:

    @classmethod
    def from_message_frame(cls, frame):
        """
        Crea una instance de AmqpMessageFrame a partir de las propiedades
        del mensaje que se ha recibido
        :param frame: Basic.Deliver
        :return: AmqpMessageFrame
        """
        amf = AmqpMesageFrame()
        amf.exchange = frame['exchange'] if 'exchange' in frame else None
        amf.consumer_tag = frame['consumer_tag'] if 'consumer_tag' in frame else None
        amf.delivery_tag = frame['delivery_tag'] if 'delivery_tag' in frame else None
        amf.routing_key = frame['routing_key'] if 'routing_key' in frame else None
        amf.redelivered = frame['redelivered'] if 'redelivered' in frame else None
        return amf

    def __init__(self):
        self.consumer_tag = None
        self.delivery_tag = None
        self.routing_key = None
        self.exchange = None
        self.redelivered = None


class AmqpMessage:

    @classmethod
    def create_from_message(cls, message):
        """
        Crea una instancia de AmqpMessage a partir del mensaje recibido
        :param message:
        :return:
        :rtype: clitellum.channels.amqp.AmqpMessage
        """
        amf = AmqpMesageFrame.from_message_frame(message.delivery_info)
        amp = AmqpMessageProperties.from_basic_properties(message.properties)
        return AmqpMessage(amf, amp, message.body.tobytes())

    def __init__(self, frame: AmqpMesageFrame, properties: AmqpMessageProperties, body: bytes):
        self.frame = frame
        self.properties = properties
        self.body = body


class AmqpConnection:
    """
    Conexion a amqp
    """
    def __init__(self, configuration: ChannelConfiguration):
        self._configuration = configuration
        """
        :type: channels.configuration.ChannelConfiguration
        """

        self._connection = None
        """
        :type: amqp.connection.Connection
        """

        self._isConnected = False
        self._channel = None
        """
        :type: librabbitmq.Channel
        """
        self._closing = False
        self._consumer_tag = None
        self._channel_send = None
        """
        :type: librabbitmq.Channel
        """
        self._mutex = threading.Lock()
        self._mutex_ack = threading.Lock()

        self.on_message_received = None

    def connect(self):
        """
        Realiza la conexion con el host
        """

        if self._isConnected:
            return

        self._isConnected = False

        while not self._closing:
            try:
                logger_manager.get_logger().info('Conectando a %s', self._configuration.uri)
                self._connect_point()
                self._isConnected = True
                return
            except ConnectionError as ex:
                logger_manager.get_logger().error("Error al conectar: %s", ex)
                logger_manager.get_logger().error("Intentado reconectar... Host: %s", self._configuration.uri)

    def _connect_point(self):
        try:
            if self._connection is not None and self._connection.is_open:
                self._connection.close()

            parameters = self._configuration.get_connection_parameters()

            logger_manager.get_logger().debug('Creando conexion')
            self._connection = librabbitmq.Connection(
                host=parameters.host,
                userid=parameters.userid,
                password=parameters.password,
                virtual_host=parameters.virtual_host
            )

            logger_manager.get_logger().debug('Creando channel')
            self._channel = self._connection.channel(1)
            self._channel_send = self._connection.channel(2)

            if self._configuration.exchange.create:
                logger_manager.get_logger().debug('Creando exchange')
                self._channel.exchange_declare(self._configuration.exchange.name,
                                               self._configuration.exchange.type.value,
                                               durable=True,
                                               auto_delete=False)

            if self._configuration.queue.create and self._configuration.queue.name is not None:
                logger_manager.get_logger().debug('Creando cola')
                self._channel.queue_declare(queue=self._configuration.queue.name,
                                            durable=True, auto_delete=False)

                for key in self._configuration.queue.get_routing_keys():
                    self._channel.queue_bind(queue=self._configuration.queue.name,
                                             exchange=self._configuration.exchange.name,
                                             routing_key=key)
            self._channel.basic_qos(0, 100, True)

        except Exception as ex:
            logger_manager.get_logger().error('Error Creando conexion', ex)
            raise ConnectionException(ex)

    def close(self):
        """
        Cierra la conexion del channel
        """
        logger_manager.get_logger().info('Cerrando conexion')
        self._closing = True
        try:
            if self._isConnected:
                self._channel.close()
                self._channel_send.close()
                self._connection.close()
                self._connection = None
        except Exception as ex:
            logger_manager.get_logger().error("Error al cerrar: %s", ex)

        self._isConnected = False

    def publish(self, message: bytes, routing_key: str, amqp_message_properties: AmqpMessageProperties):
        """
        Publica un mensaje en el amqp
        :param amqp_message_properties: Propiedades del mensaje
        :param message: Cadena con el mensaje
        :param routing_key: Clave de enrutamiento del mensaje
        """
        self._mutex.acquire()
        while not self._closing:
            try:
                properties = amqp_message_properties.to_dict()
                self._channel_send.basic_publish((message, properties),
                                                 exchange=self._configuration.exchange.name,
                                                 routing_key=routing_key)
                break
            except Exception as ex:
                logger_manager.get_logger().error("Error de conexion al enviar el mensaje %s" % ex)
                self.connect()

        self._mutex.release()

    def consume(self):
        self._consumer_tag = self._channel.basic_consume(queue=self._configuration.queue.name,
                                                         callback=self.__read_message)
        logger_manager.get_logger().info("Start Consuming %s", self._consumer_tag)

    def drain_events(self, timeout):
        self._connection.drain_events(timeout=timeout)

    def __read_message(self, message):
        logger_manager.get_logger().debug("Message Received %s", message.body.tobytes())
        amqp_message = AmqpMessage.create_from_message(message)
        self.on_message_received(amqp_message)

    def ack(self, message: AmqpMessage):
        """
        Realiza el ack del mensaje en el servidor amqp
        :param message: Mensaje del que se realiza el ack
        """

        try:
            self._mutex_ack.acquire()
            self._channel.basic_ack(delivery_tag=message.frame.delivery_tag, multiple=False)
        except Exception as ex:
            logger_manager.get_logger().error("Error al enviar el ack", ex)
        finally:
            self._mutex_ack.release()

    def basic_cancel(self):
        self._channel.basic_cancel(self._consumer_tag)
