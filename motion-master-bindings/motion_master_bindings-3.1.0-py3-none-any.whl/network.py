"""
Network : Motion Master Bindings
"""

import logging
import threading

import rx
from rx import operators as ops
import zmq

# Provides the message API for the Motion Master
from motion_master_proto.motion_master_pb2 import MotionMasterMessage
# Common objects to describe health state
from motion_master_bindings.health_status import HealthCode, HealthStatus

logger = logging.getLogger(__name__)
# False until a message arrives. Used to detect a dropped connection.
_was_message_received = False


class PollSocketWorker(threading.Thread):
    """
    Polls the socket over and over and publishes anything it finds.

    Assumes the socket is connected and working.
    """

    def __init__(self, thread_name: str, socket: zmq.Socket, rx_subject: rx.subject.Subject) -> None:
        threading.Thread.__init__(self)
        self.name = thread_name
        self.socket = socket
        self.rx_subject = rx_subject
        self._stop_thread_event = threading.Event()
        logger.debug("Init thread %s", thread_name)

    def stop(self):
        """Issues an event that stops the thread."""
        self._stop_thread_event.set()
        logger.debug("Stopping thread %s", self.name)

    def run(self):
        global _was_message_received
        """Polls the socket and publishes on the given subject"""
        logger.debug("Running thread %s", self.name)
        while not self._stop_thread_event.is_set():
            try:
                # Poll the socket for new messages.
                message = self.socket.recv_multipart()
                # Publish the message for others to use.
                self.rx_subject.on_next(message)
                _was_message_received = True
            except Exception:
                # This can happen due to a timeout on the socket.
                pass


class ServerConnectivity:
    """
    Holds connectivity information.
    """

    def __init__(self, address: str, dealer_port: int, subscribe_port: int, receive_timeout_ms: int = 500) -> None:
        self.address = address
        self.dealer_port = dealer_port
        self.subscribe_port = subscribe_port

        # Set up the sockets for connecting to the Motion Master.
        self.zmq_context = zmq.Context()
        self.socket_dealer = self.zmq_context.socket(zmq.DEALER)
        self.socket_dealer.RCVTIMEO = receive_timeout_ms
        self.socket_subscr = self.zmq_context.socket(zmq.SUB)
        self.socket_subscr.RCVTIMEO = receive_timeout_ms


class Network:
    """
    Manage network connectivity to the Motion Master
    """
    # pylint: disable=too-many-instance-attributes
    # Because COME ON.

    # The motion-master requires that messages are transmitted every 250 ms.
    _SENT_MESSAGE_TIMEOUT_SECOND = 0.200

    def __init__(self, address: str, request_port: int, subscribe_port: int) -> None:
        # Set up server connection parameters.
        self.server = ServerConnectivity(address, request_port, subscribe_port)
        # By default, don't keep the connection alive. That's the client's job.
        self.keepalive_is_enabled = False
        # Set up the timer for tracking transmitted messages.
        self.keepalive_timer = threading.Timer(
            self._SENT_MESSAGE_TIMEOUT_SECOND, self._send_ping)
        # Init the subjects used to publish socket data.
        # Configure threads to monitor the two sockets.
        self.topics_subject = rx.subject.Subject()
        self.dealer_subject = rx.subject.Subject()
        self.thread_poll_topic = PollSocketWorker("SUB Poll",
                                                  self.server.socket_subscr, self.topics_subject)
        self.thread_poll_dealer = PollSocketWorker("DEALER Poll",
                                                   self.server.socket_dealer, self.dealer_subject)
        # This is where health status is published.
        self.health_subject = rx.subject.Subject()
        self.health_subject.on_next(HealthStatus(HealthCode.OKAY, "network", "initialized"))

    def _send_ping(self):
        """Send a ping message to the master to keep the connection alive"""
        message = MotionMasterMessage()
        message.request.ping_system.SetInParent()
        self.send_message(message)

    def disconnect(self):
        """Disconnect and close threads"""
        # Shut down the incoming message watchdog
        self._dispose_watchdog_monitor.dispose()
        # Stop threads
        self.thread_poll_topic.stop()
        self.thread_poll_dealer.stop()
        self.thread_poll_topic.join()
        self.thread_poll_dealer.join()
        # Turn off the keepalive timer (if it's running)
        self.keepalive_timer.cancel()
        logger.debug("Network disconnected")

    def _reset_flag_for_timeout(self):
        def _passthrough_source(source):
            def subscribe(observer, scheduler=None):
                def on_next(value):
                    # Reset the flag.
                    global _was_message_received
                    _was_message_received = False
                    # Pass on the value for further study.
                    observer.on_next(value)

                return source.subscribe(on_next,
                                        observer.on_error,
                                        observer.on_completed,
                                        scheduler)

            return rx.create(subscribe)

        return _passthrough_source

    def connect(self):
        """Connect to both request and subscriber ports"""
        global _was_message_received
        endpoint = "tcp://{}:{}".format(self.server.address,
                                        self.server.subscribe_port)
        if self.server.socket_subscr.connect(endpoint):
            logger.error("Connection to %s failed", endpoint)
        else:
            logger.debug("Connected to %s", endpoint)

        endpoint = "tcp://{}:{}".format(self.server.address,
                                        self.server.dealer_port)
        if self.server.socket_dealer.connect(endpoint):
            logger.error("Connection to %s failed", endpoint)
        else:
            logger.debug("Connected to %s", endpoint)

        # Start the threads that monitor and publish incoming messages.
        self.thread_poll_topic.start()
        self.thread_poll_dealer.start()
        # Monitor incoming messages. If the flag is ever false (means no message
        # came in since the last check), send this state to the Health subject.
        received_composed = rx.interval(0.100).pipe(
            ops.map(lambda x: _was_message_received),
            self._reset_flag_for_timeout(),
            ops.filter(lambda b: b == False))
        self._dispose_watchdog_monitor = received_composed.subscribe(lambda crickets: self.health_subject.on_next(
            HealthStatus(HealthCode.ERROR_MESSAGE_RECEIVED_WATCHDOG,
                         "watchdog", "no messages received within 100 ms")))

    def get_topics_subject(self):
        """Return the rx.Subject used to publish messages from the Motion Master subscription (topics) channel"""
        return self.topics_subject

    def get_dealer_subject(self):
        """Return the rx.Subject used to publish messages from the Motion Master dealer channel"""
        return self.dealer_subject

    def get_healthstatus_subject(self):
        """Return the rx.Subject used to publish messages about the health status"""
        return self.health_subject

    def add_topic(self, topic: str):
        """Subscribe to a new topic on the subscription socket"""
        self.server.socket_subscr.subscribe(topic)

    def send_message(self, message: MotionMasterMessage):
        """Serializes the message and sends through the DEALER socket.

        This also resets the timer to manage the motion-master heartbeat.
        """
        self.server.socket_dealer.send(message.SerializeToString())

        if self.keepalive_is_enabled:
            # Reload the keepalive timer
            self.keepalive_timer.cancel()
            self.keepalive_timer = threading.Timer(
                self._SENT_MESSAGE_TIMEOUT_SECOND, self._send_ping)
            self.keepalive_timer.start()

    def enable_keepalive(self):
        """Send pings automatically to keep the connection alive if no messages are being sent"""
        logger.warning("The server will be pinged to keep the connection alive.")
        self.keepalive_is_enabled = True
        self.keepalive_timer = threading.Timer(
            self._SENT_MESSAGE_TIMEOUT_SECOND, self._send_ping)
        self.keepalive_timer.start()

    def disable_keepalive(self):
        """Stop sending pings to keep the connection alive"""
        logger.warning("The server keepalive ping has been disabled.")
        self.keepalive_is_enabled = False
        self.keepalive_timer.cancel()
