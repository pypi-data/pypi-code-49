from clitellum.channels.amqp import AmqpMessage, AmqpMessageProperties
from clitellum.channels.channel import Channel
import json
from clitellum import logger_manager

from clitellum.channels.configuration import ChannelConfiguration


class Identification:
    """
    Clase de identificacion de los servicios
    """
    def __init__(self, _id: str, _type: str):
        """
        Constructor
        :param _id: Id del servicio
        :param _type: Tipo del servicio
        """
        self.type = _type
        self.id = _id


class Context:
    """
    Contiene la informacion del contexto de ejecución del mensaje
    """

    def __init__(self, properties: AmqpMessageProperties):
        """
        Crea una instancia del contexto
        :param properties: Propiedades del contexto
        """
        self.properties = properties

    def get_headers(self) -> dict:
        """
        Devuelve el diccionario de las cabeceras
        :return: Diccionario
        :rtype: dict
        """
        return self.properties.headers

    def get_item(self, key: str) -> str:
        """
        Devuelve el elemento en funcion de su clave, si la clave no existe devuelve None
        :param key: Clave del elemento
        :return: Cadena con el elemento o None
        :rtype: str
        """
        return self.properties.headers[key] if key in self.properties.headers else None

    def add_header(self, key: str, value: str):
        """
        Añade o actualiza una cabecera en el contexto
        :param key: Clave de la cabecera
        :param value: Valor de la cabecera
        """
        self.properties.headers[key] = value


class ContextFactory:
    """
    Factoria para la creacion de contextos
    """

    @classmethod
    def create_from_amqp_message(cls, message: AmqpMessage) -> Context:
        """
        Crea una instancia del contexto a partir del mensaje que ha llegado
        :param message:
        :return:
        """
        properties = AmqpMessageProperties.create()
        properties.headers = message.properties.headers
        properties.correlation_id = message.properties.correlation_id
        properties.app_id = message.properties.app_id

        return Context(properties)

    @classmethod
    def create_empty(cls) -> Context:
        """
        Crea una instancia del contexto vacia
        :return: Contexto
        :rtype: clitellum.services.Context
        """
        properties = AmqpMessageProperties.create()

        return Context(properties)


class PublisherConfiguration:

    def __init__(self, identification, config: ChannelConfiguration):
        self._sender_config = config
        self._identification = identification

    def get_sender_config(self) -> ChannelConfiguration:
        return self._sender_config

    def get_identification(self) -> Identification:
        return self._identification

class Publisher:
    """
    Publicador de mensajes
    """
    def __init__(self, config: PublisherConfiguration, channel: Channel):
        self._channel = channel
        self.config = config

    def connect(self):
        """
        Realiza la conexion del canal
        """
        logger_manager.get_logger().debug("Service - Conectando Canal de envio")
        self._channel.connect()

    def publish(self, message: str, routing_key: str, context: Context = None):
        """
        Publica un mensaje en el canal
        :param routing_key: Clave de enrutamiento
        :param message: Cuerpo del mensaje
        :param context: Contexto del mensaje
        """
        if context is None:
            context = ContextFactory.create_empty()

        logger_manager.get_logger().debug("Service - Publicando Mensaje")
        encoding = context.properties.content_encoding if context.properties.content_encoding is not None else 'utf-8'
        self._channel.publish(bytes(message, encoding), routing_key, context.properties)

    def close(self):
        """
        Cierra la conexion del canal
        """
        self._channel.close()


class PublisherFactory:
    """
    Factory de publicadores
    """
    @classmethod
    def create(cls, publisher_id: str, publisher_type: str, config: ChannelConfiguration) -> Publisher:
        """
        Crea una instancia de un publicador
        :param publisher_id: PublisherConfiguration
        :param publisher_type: PublisherConfiguration
        :param config: Configuracion del publicador
        :return:
        """
        channel = Channel.create(config)
        config = PublisherConfiguration(Identification(publisher_id, publisher_type), config)
        return Publisher(config, channel)


class ServiceConfiguration(PublisherConfiguration):

    def __init__(self, identification, sender_config: ChannelConfiguration, receiver_config: ChannelConfiguration):
        PublisherConfiguration.__init__(self, identification, sender_config)
        self._receiver_config = receiver_config

    def get_receiver_config(self) -> ChannelConfiguration:
        return self._receiver_config


class Service(Publisher):
    """
    Clase de Servicio
    """

    def __init__(self, config: ServiceConfiguration, channel_sender: Channel,
                 channel_receiver: Channel, handler_manager):
        Publisher.__init__(self, config, channel_sender)
        self.channel_receiver = channel_receiver
        self.channel_receiver.on_message_received = self._message_received
        self.handler_manager = handler_manager

    def run(self):
        self.connect()
        logger_manager.get_logger().debug("Service - Run %s - %s", self.config.get_identification().id,
                                          self.config.get_identification().type)
        self.channel_receiver.consume()

    def stop(self):
        logger_manager.get_logger().debug("Service - Stop - Waiting for channel")
        self.channel_receiver.stop_consuming()
        self.close()

    def connect(self):
        Publisher.connect(self)
        logger_manager.get_logger().debug("Service - Conectando Canal de recepcion")
        self.channel_receiver.connect()

    def close(self):
        Publisher.close(self)
        self.channel_receiver.close()

    def _send_error(self, message: bytes, ex: Exception):
        message_error = dict()
        message_error['description'] = str(ex)
        message_error['message'] = message
        str_error = json.dumps(message_error)
        self._channel.publish(bytes(str_error, 'utf-8'), 'Message.Error', AmqpMessageProperties.create())

    def _message_received(self, message: AmqpMessage):
        try:
            logger_manager.get_logger().debug("Service - Received Message")
            encoding = message.properties.content_encoding \
                if message.properties.content_encoding is not None else 'utf-8'

            message_str = str(message.body, encoding=encoding)
            handler_class = self.handler_manager.get_handler(message.frame.routing_key)
            handler = handler_class()
            handler.initialize(self,
                               ContextFactory.create_from_amqp_message(message),
                               message_str)
            handler.handle()

        except Exception as ex:
            logger_manager.get_logger().error("Service - Error al procesar el mensaje", ex)
            self._send_error(message.body, ex)
        finally:
            self.channel_receiver.ack(message)


class ServiceFactory:
    """
    Factoria para los servicios
    """

    @classmethod
    def create_service(cls, service_id: str, service_type: str, config_sender: ChannelConfiguration,
                       config_receiver: ChannelConfiguration, handler_manager) -> Service:
        """
        Crea una instancia de un servicio
        :param handler_manager: controlador de los handlers de los mensajes
        :param config_receiver: configuracion del receptor
        :param config_sender: configuracion del publicador
        :param service_id: identificador del servicio
        :param service_type: tipo del servicio
        :return: Service
        :rtype: clitellum.services.Service
        """
        channel_sender = Channel.create(config_sender)
        channel_receiver = Channel.create(config_receiver)
        service_config = ServiceConfiguration(Identification(service_id, service_type), config_sender, config_receiver)
        return Service(service_config, channel_sender, channel_receiver, handler_manager)
