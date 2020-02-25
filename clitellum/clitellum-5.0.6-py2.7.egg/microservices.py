from clitellum.channels.configuration import ChannelConfiguration
from clitellum.handlers import HandlerManager
from clitellum.services import ServiceFactory, Service


def microservice(bc, bc_publisher=None):
    def decorator(f):
        MicroServiceBuilder.get_instance().set_bc(bc)
        MicroServiceBuilder.get_instance().set_bc_publisher(bc_publisher)
        return f
    return decorator


def add_service(service_type, service_id, package):
    def decorator(f):
        MicroServiceBuilder.get_instance().add_service(service_type, service_id, package)
        return f
    return decorator


class ServiceInfo:
    def __init__(self, service_type, service_id, package):
        self.package = package
        self.service_id = service_id
        self.service_type = service_type


class Microservices:
    def __init__(self):
        self.__services = []

    def add(self, service: Service):
        self.__services.append(service)

    def run(self):
        for service in self.__services:
            service.run()

    def stop(self):
        for service in self.__services:
            service.stop()


class MicroServiceBuilder:
    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = MicroServiceBuilder()
        return cls._instance

    def __init__(self):
        self.__bc = None
        self.__bc_publisher = None
        self.__amqp_uri = "amqp://guest:guest@localhost:5672/"
        self.__max_threads = 4
        self.__services = []

    def set_bc(self, bc):
        self.__bc = bc

    def add_service(self, service_type, service_id, package):
        service = ServiceInfo(service_type, service_id, package)
        self.__services.append(service)

    def set_bc_publisher(self, bc_publisher):
        self.__bc_publisher = bc_publisher

    def set_amqp_uri(self, amqp_uri):
        self.__amqp_uri = amqp_uri

    def set_max_thread(self, max_threads):
        self.__max_threads = max_threads

    def build(self):
        micro = Microservices()

        for service_info in self.__services:
            # Load handlers packages
            __import__(service_info.package)

            config_receiver = ChannelConfiguration()
            config_receiver.uri = self.__amqp_uri
            config_receiver.exchange.name = self.__bc
            config_receiver.queue.name = '%s.%s.%s' % (self.__bc, service_info.service_type, service_info.service_id)

            for routing_key in HandlerManager.get_instance().get_routing_keys():
                config_receiver.queue.add_routing_key(routing_key)

            config_receiver.max_threads = 4

            config_sender = ChannelConfiguration()
            config_sender.uri = self.__amqp_uri
            config_sender.exchange.name = self.__bc_publisher if self.__bc_publisher is not None else self.__bc

            handler_manager = HandlerManager.get_instance().clone()
            service = ServiceFactory.create_service(service_id=service_info.service_type,
                                                    service_type=service_info.service_id,
                                                    config_sender=config_sender,
                                                    config_receiver=config_receiver,
                                                    handler_manager=handler_manager)
            HandlerManager.get_instance().clear()
            micro.add(service)
        return micro

