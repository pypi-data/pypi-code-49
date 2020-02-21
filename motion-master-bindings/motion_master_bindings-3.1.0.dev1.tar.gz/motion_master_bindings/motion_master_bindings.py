"""
Motion Master Bindings

This module provides basic connectivity for the Motion Master.
"""
import logging

# Provides the message API for the Motion Master
from motion_master_proto.motion_master_pb2 import MotionMasterMessage
# The classes that manage the network connection
from motion_master_bindings.network import Network

logger = logging.getLogger(__name__)


class MotionMasterBindings:
    """
    Provide an interface to the network
    """

    def __init__(self, address: str = '127.0.0.1', dealer_port: int = 62524, subscribe_port: int = 62525) -> None:
        self.network = Network(address, dealer_port, subscribe_port)

    def connect(self):
        """Connect to the motion-master on DEALER and SUBSCRIBE ports"""
        self.network.connect()

    def enable_keepalive(self):
        """Monitor the network and ping the Motion Master to keep the connection active

        For safety purposes, the Motion Master will automatically stop any started processes within 250 milliseconds
        if a message is not transmitted in that time window. A heartbeat ping should normally be handled in your main
        application, not these bindings! Use this keepalive feature _only_ for debugging purposes.
        """
        self.network.enable_keepalive()

    def disable_keepalive(self):
        """Disable the automated network ping"""
        self.network.disable_keepalive()

    def disconnect(self):
        """Disconnect and close connections"""
        self.network.disconnect()

    def subscribe_to_topic(self, topic: str):
        """Subscribe to an additional topic"""
        self.network.add_topic(topic)

    def send_message(self, message: MotionMasterMessage):
        """Send a message over the DEALER socket. Connect() first."""
        self.network.send_message(message)

    def get_topics_subject(self):
        """Return the rx.Subject used to publish messages from the Motion Master subscription (topics) channel"""
        return self.network.get_topics_subject()

    def get_dealer_subject(self):
        """Return the rx.Subject used to publish messages from the Motion Master dealer channel"""
        return self.network.get_dealer_subject()

    def get_healthstatus_subject(self):
        """Return the rx.Subject used to publish messages about the health status"""
        return self.network.get_healthstatus_subject()
