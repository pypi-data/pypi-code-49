# Copyright Netflix, 2019
import json
import logging
from threading import Event
from threading import Lock
from threading import Timer
from traceback import format_exc
from uuid import uuid4

from paho.mqtt.client import Client

# Implementation libs
from kaiju_mqtt_py.mqtt_enum import QOS_AT_LEAST_ONCE
from kaiju_mqtt_py.sslconfig import SslConfig
from kaiju_mqtt_py.sslconfigmanager import SslConfigManager

TIMEOUT_IN_SECONDS = 60
TOPIC = "TEST_TOPIC_DAVIDB"


class ReturnMe:
    """A value inside a reference-safe object."""

    def __init__(self):
        """Constructor."""
        self.value = None


class MqttPayload:
    """Named value payload class."""

    def __init__(self):
        """Constructor."""
        self.value = None


class MqttPacket:
    """Topic and payload struct."""

    def __init__(self):
        """Constructor."""
        self.topic = ""
        self.payload = MqttPayload()


class MqttStatusException(Exception):
    """Shaped exception for easier forming of a structured exception."""

    def __init__(self, status=500, *args, extra={}, **kwargs):
        """Constructor."""
        super(MqttStatusException, self).__init__(*args, **kwargs)
        self.status = status
        self.extra = extra


class MqttResponse(object):
    def __init__(self, status, body):
        self.status = status
        self.body = body

    def as_dict(self):
        return {"status": self.status, "body": self.body}


def get_json_unwrapped_callback(callback):
    """
    Handle the user code after decoding the JSON for them.

    The default message handler must have the client, userdata, packet signature.
    This allows us to call that by creating a closure that already handles the boring json work.

    :param callback: User provided code with the signature def x(client, userdata, packet)
    :return: the new closure to call later
    """

    def json_unwrapper_around_callback(client, userdata, packet):
        """
        First unwrap strings containing json, then forward to the intended callback.

        :param client:
        :param userdata:
        :param packet:
        :return:
        """
        response = {}
        if packet:
            try:
                response = json.loads(packet.payload)
                if not isinstance(response, dict):
                    response = json.loads(str(response))
            except ValueError:
                response = {"error": "failed to parse msg", "msg": str(packet)}
        load = MqttPacket()
        load.topic = packet.topic
        load.payload = response
        callback(client, userdata, load)

    return json_unwrapper_around_callback


def get_error_handler_for_client_callback(kaiju, logger, topic, client_function):
    """
    Return a closure around the client callback for a handle command

    Handle typical errors by forming an appropriate error structure.
    If the client_function returns a dict, the result will be serialized (and deserialized) automatically to json.
    An MqttStatusException thrown or returned from client_function is an ideal way to respond with errors.
    Other errors will be rewrapped in a shape something like the MqttStatusException and rethrown.

    :param callback: Function in the form of def x(request_topic: Text, msg: MqttPacket) -> dict
    :return: Closure around the client_function with the above error handling done.
    """

    def handle_errors_from_client_code(client, userdata, msg):
        """
        Closure to capture the intended user message handler and call it on request.

        :param client:
        :param userdata:
        :param msg:
        :return:
        """
        request_topic = msg.topic
        if request_topic is None:
            raise SyntaxError(f"FATAL: Handler for topic {topic} failed to receive request topic.")
        response_topic = f"_response/{request_topic}"

        try:
            logger.debug(f"Calling client code for {request_topic} message")
            result_msg = client_function(request_topic, msg)
            if not isinstance(result_msg, MqttResponse):
                result_msg = MqttResponse(200, result_msg)
            kaiju.publish(response_topic, result_msg)
        except MqttStatusException as error:
            logger.debug("Got an MqttStatusException, passing along")
            return kaiju.publish(
                response_topic,
                {
                    "status": error.status,
                    "body": {"error": {"message": str(error), "trace": format_exc(), **error.extra}, "request": msg.payload},
                },
            )
        except Exception as error:
            logger.exception(
                error, "Got a normal exception processing handle functions, wrapping in 500 error",
            )
            return kaiju.publish(
                response_topic, {"status": 500, "body": {"error": {"message": str(error), "trace": format_exc()}, "request": msg.payload}},
            )

    return handle_errors_from_client_code


def get_custom_request_responder(logger, clear_timeout, return_me, handled_event):
    """
    Get a custom request handler function that captures some closure data.

    :param logger:
    :param clear_timeout:
    :param return_me:
    :param handled_event:
    :return:
    """

    def handle_response_to_this_request(client, user_data, packet):
        """
        This is the success path : the response has arrived, let the requester know.

        Closure around the return_me and handled_event variables to indicate completion and values.
        :param packet:
        :return:
        """
        logger.debug("Got response to my request")
        # cleanup()  # subscription.end()
        clear_timeout()

        response = packet.payload
        if packet:
            try:
                # yes, twice
                if not isinstance(response, dict):
                    response = json.loads(str(packet.payload))
                if not isinstance(response, dict):
                    response = json.loads(str(response))
            except ValueError:
                response = {"error": "failed to parse msg", "msg": str(packet)}

        if isinstance(response, dict) or not "status" not in response:
            # strings
            return_me.value = response
            handled_event.set()

        if response["status"] > 299:
            # if the body is any normal exception stored as a string, we want to rewrap it
            if isinstance(response["body"], str):
                # todo stack?
                response["body"] = {
                    "message": response["body"],
                    "name": response["body"],
                }
            return_me.value = response
            handled_event.set()
            return

    return handle_response_to_this_request


def on_connect(client, userdata, flags, rc):
    """Set the connected state and subscribe to existing known topics."""

    userdata.logger.info("KaijuMQTT Connected")
    with userdata.unsub_lock:  # threads might enter here simultaneously. Stop that.
        userdata.connected_event.set()
        userdata.disconnected_event.clear()

        for subscribe_args in userdata.subscribe_list[:]:
            userdata.subscribe(*subscribe_args)


def on_disconnect(client, userdata, rc):
    """Set the disconnected state."""

    userdata.logger.info("KaijuMQTT Disconnected")
    userdata.connected_event.clear()
    userdata.disconnected_event.set()


def on_message(client, userdata, packet):
    """
    Handle MQTT messages that are not directly being looked for.

    :param client:
    :param userdata:
    :param packet:
    :return:
    """
    response = {}
    if packet:
        try:
            response = json.loads(str(packet.payload))
            if not isinstance(response, dict):
                response = json.loads(str(response))
        except ValueError:
            response = {"error": "failed to parse msg", "msg": str(packet)}
    # todo topic remote vs. local
    logging.debug("emitting on " + packet.topic)

    # point of interest: this function should never actually get called any more


class KaijuMqtt:
    """
    A pub/sub and request/response protocol over an mqtt session.
    """

    logger = logging.getLogger(__name__)

    def __init__(self, json_stringify=json.dumps):
        """Construct, but no more."""
        self.handler_unsubscribe_function_list = []

        self.connected_event = Event()
        self.disconnected_event = Event()

        self.subscribe_list = []
        self.topic_callback_list = []

        self.client = Client(userdata=self)
        self.client.enable_logger(self.logger)
        self.client.on_connect = on_connect
        self.client.on_message = on_message
        self.client.on_disconnect = on_disconnect

        self.subscribe_topic_to_json_wrapped_functions_map = {}  # type Dict[Text, Any]
        self.handle_topic_to_function_map = {}  # type Dict[Text, Any]
        self.request_topic_to_responder_map = {}  # type Dict[Text, Any]

        self.unsub_lock = Lock()

        self.json_stringify = json_stringify

    def close(self):
        """
        Call all deferred cleanup functions.

        :return:
        """
        for cleanup in self.handler_unsubscribe_function_list:
            cleanup()
        self._end()

    def connect(self, host="localhost", port=1883):
        """
        Connect to the host and port specified via mqtt.

        :param host: This is the hostname or configuration name to use
        :param port: This is the port to connect to if not determined by the configuration
        :return: None
        """

        if not self.connected_event.is_set():
            mgr = SslConfigManager()
            if mgr.has(host):
                conf = mgr.get(host)
                self.use_configuration(conf)
                self.client.connect(conf.host, conf.port)
            else:
                self.client.connect(host, port)
            self.client.loop_start()
            self.connected_event.wait(15.0)
            if not self.connected_event.is_set():
                raise Exception("Connect timed out after 15 seconds.")

    def connect_async(self, host="localhost", port=1883):
        """
        Connect to the host and port specified via mqtt.

        :param host:
        :param port:
        :return: None
        """
        if not self.connected_event.is_set():
            mgr = SslConfigManager()
            if mgr.has(host):
                conf = mgr.get(host)
                self.use_configuration(conf)
                self.client.connect_async(conf.host, conf.port)
            else:
                self.client.connect_async(host, port)
            self.client.loop_start()

    def _end(self):
        """
        End the session.

        :return: None
        """
        if self.connected_event.is_set():
            self.client.loop_stop()
            self.client.disconnect()
            self.disconnected_event.wait(15.0)

    def subscribe(self, topic, callback, options=None):
        """
        Call a callback when a matching topic gets a message.

        :param topic:
        :param callback:
        :return: un-listen un-subscribe function
        """

        # todo topic remote vs. local
        args = (topic, callback, options)
        if not self.connected_event.is_set():
            self.subscribe_list.append(args)
        else:
            if options is None:
                options = {"qos": QOS_AT_LEAST_ONCE}

            # now we track the callbacks by topic, so we can replace them if required
            self.subscribe_topic_to_json_wrapped_functions_map[topic] = get_json_unwrapped_callback(callback)

            self.client.message_callback_add(topic, self.subscribe_topic_to_json_wrapped_functions_map[topic])

            self.client.subscribe(topic, qos=options["qos"])

            self.logger.debug(f"Subscribed to topic {topic}")

        def undo_subscribe():
            with self.unsub_lock:  # threads might enter here simultaneously. Stop that.
                if topic in self.subscribe_topic_to_json_wrapped_functions_map.keys():
                    self.client.message_callback_remove(topic)
                    self.client.unsubscribe(topic)
                    del self.subscribe_topic_to_json_wrapped_functions_map[topic]
                    self.logger.debug(f"Unsubscribed from topic {topic}")

        return undo_subscribe

    def publish(self, topic, what, options=None):
        """
        Publish something to a topic.

        :param options: dict. key "qos" will be looked for.
        :param topic:
        :param what: json dumpable string, or a string
        :return:
        """
        self.logger.debug(f"publish on {topic}")
        if options is None:
            options = {"qos": QOS_AT_LEAST_ONCE}
        if "qos" not in options:
            options["qos"] = QOS_AT_LEAST_ONCE
        tosend = what
        if isinstance(what, MqttStatusException) or isinstance(what, MqttResponse):
            tosend = self.json_stringify(what.as_dict())
        elif isinstance(what, dict):
            tosend = self.json_stringify(what)
        self.client.publish(topic, payload=tosend, qos=options["qos"])
        # note to self: do not block on publish state here - it blocks downstream actions

    def request(self, topic, payload=None, options=None):  # noqa: C901
        """
        Request a response to a specific payload.

        This is a synchronous call. A request will be sent to the topic <topic>/<uuid>,
        and will wait for a response on topic _responses/<topic>/<uuid> for up to the timeout (passed in via the
        options dict). Timeouts will return an error shaped dictionary, with keys 'status' and 'body'.

        :param topic:
        :param payload: dict, to be delivered as json
        :param options: dict with keys "qos" and "timeoutMs"
        :return:
        """
        # arg defaults take a lot of space!
        self.logger.debug(f"request {topic}")
        payload = {} if payload is None else payload
        options = {"qos": QOS_AT_LEAST_ONCE, "timeoutMs": 5000} if options is None else options
        request_id = uuid4()
        timeout_ms = options["timeoutMs"] if "timeoutMs" in options else 5000
        if "qos" not in options:
            options["qos"] = QOS_AT_LEAST_ONCE

        request_topic = f"{topic}/{request_id}"
        response_topic = f"_response/{request_topic}"

        cleanup = None
        timer = None
        handled_event = Event()

        # initialized here for the closures below
        return_me = ReturnMe()

        def unsub_and_fail():
            """
            Unsubscribe, clean up, and return None.

            Closure around the return_me and handled_event variables to indicate completion and values.

            :return:
            """
            if cleanup is not None:
                cleanup()
            clear_timeout()
            return_me.value = {"status": 500, "body": {"error": "Timed out."}}
            handled_event.set()

        def clear_timeout():
            """
            If the timer is set, clear it.

            Closure around the timer object.
            :return: None
            """
            if hasattr(timer, "cancel"):
                timer.cancel()

        self.request_topic_to_responder_map[request_topic] = get_custom_request_responder(
            self.logger, clear_timeout, return_me, handled_event
        )
        cleanup = self.subscribe(response_topic, self.request_topic_to_responder_map[request_topic], options=options)

        timer = Timer((timeout_ms / 1000.0), unsub_and_fail)
        timer.start()
        self.logger.debug(f"publishing request on {request_topic}")
        self.publish(request_topic, payload, options)
        handled_event.wait(timeout=(timeout_ms / 1000.0) + 1.0)
        clear_timeout()
        cleanup()
        return return_me.value

    def handle(self, topic, client_function, options=None):  # noqa: C901
        """
        Handle "topic" events by running "handler". Results of "handler" are posted as a response.

        When messages one layer under "topic" are posted, run handler, and post the result to a response channel.
        Subscribe to topics one layer under "topic" with the new handler func.
        The handler func calls "handler" to get a result message and publishes the response on "responseTopic"

        :param topic:
        :param client_function:
        :return:
        """
        if options is None:
            options = {"qos": QOS_AT_LEAST_ONCE}
        if "qos" not in options:
            options["qos"] = QOS_AT_LEAST_ONCE

        self.logger.debug(f"handle {topic} messages")

        # subscribe to this topic, and send (requests that start with this topic name) to this inner_handler that wraps the original callback
        self.handle_topic_to_function_map[topic] = get_error_handler_for_client_callback(self, self.logger, topic, client_function)
        cleanup = self.subscribe(f"{topic}/+", self.handle_topic_to_function_map[topic], options)
        self.handler_unsubscribe_function_list.append(cleanup)

    def use_configuration(self, conf: "SslConfig"):
        if not conf.exists():
            raise ValueError(f"There is no configuration named {conf.dir}")
        if not conf.iscomplete():
            raise ValueError(f"The configuration {conf.dir} is missing a required file.")

        self.client.tls_set(str(conf.rootcert), str(conf.certificate), str(conf.privatekey))
