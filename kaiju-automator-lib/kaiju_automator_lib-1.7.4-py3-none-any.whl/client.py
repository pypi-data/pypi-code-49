# Copyright Netflix, 2019
import json
import re
from contextlib import contextmanager
from enum import Enum
from logging import getLogger
from socket import gaierror
from typing import Any
from typing import Dict
from typing import Generator
from typing import List
from typing import Optional
from typing import Text

from kaiju_mqtt_py.kaiju_mqtt_py import KaijuMqtt
from kaiju_mqtt_py.topicmaker import DestinationType
from kaiju_mqtt_py.topicmaker import topicmaker
from kaiju_mqtt_py.topicmaker import TopicType

from .automator_help import INCOMPLETE_PLAN_REQUEST_ERROR
from .automator_help import MISSING_RAE_TARGET
from .automator_help import REQUEST_STATUS_FAILED
from .retry_with_backoff import retry

logger = getLogger(__name__)
CLOUD_BROKER_NAME = "cloud"


class MqttRetryableError(Exception):
    pass


class DeviceIdentifier:
    """
    Identify a device to the Automator module with an IP, a serial number, or an ESN.
    """

    def __init__(self, **kwargs):
        """Constructor."""
        self.esn = kwargs["esn"] if "esn" in kwargs else None
        self.ip = kwargs["ip"] if "ip" in kwargs else None
        self.serial = kwargs["serial"] if "serial" in kwargs else None

    def as_dict(self) -> Dict:
        """
        Get the dict representation of this identifier.

        If there is no valid value set, raise a ValueError.
        :return:
        """
        result = {"target": {}}
        if self.esn is not None:
            result["target"].update({"esn": self.esn})

        if self.ip is not None:
            result["target"].update({"ip": self.ip})

        if self.serial is not None:
            result["target"].update({"serial": self.serial})

        if len(result["target"].keys()) < 1:
            raise ValueError("No device identifier was set.")

        return result

    def as_json(self) -> Text:
        """
        Get the json serialized representation of this as a string.

        :return:
        """
        return json.dumps(self.as_dict())

    @staticmethod
    def sanity_check(id: Dict) -> bool:
        """
        Perform a basic sanity check on a dict to see if it contains an identifier.

        Note that the value of the identifier is not checked, even for formatting.

        :param id:
        :return:
        """
        valid = ("device_esn" in id or "device_serial" in id or "device_ip" in id) or (
            "target" in id and ("esn" in id["target"] or "ip" in id["target"] or "serial" in id["target"])
        )
        if not valid:
            logger.error("The device identifier is in the wrong form.")
            logger.error("There are two working forms:")

            logger.error("The new form is an object stored at the key 'target', with one or more of the keys 'esn', 'ip', and 'serial':")
            logger.error('{"target": {"esn": "NFANDROID...", "ip", "192..."}, ...')

            logger.error(
                "The old form is only one of the keys 'device_esn', 'device_ip', or 'device_serial' "
                "stored in the object at the top level:"
            )
            logger.error('{"device_esn": "esn", ...')
            logger.error('{"device_ip": "esn", ...')
            logger.error('{"device_serial": "esn", ...')
        return valid


class Request:
    """
    Check the format of a request to the Automator module over the MQTT bus.

    Note that this class used to be bigger and now this is all that's left.
    """

    @staticmethod
    def sanity_check(plan: Dict) -> bool:
        """Perform a basic sanity check on a dict to see if it's mostly the right shape for a request."""
        results = [DeviceIdentifier.sanity_check(plan)]

        try:
            if "testplan" in plan:
                if "testcases" not in plan["testplan"]:
                    logger.error("The testplan is missing the key 'testcases'")
                results.append("testcases" in plan["testplan"])

                if not type(plan["testplan"]["testcases"]) is list:
                    logger.error("The test plan member 'testcases' is not a list")
                results.append(type(plan["testplan"]["testcases"]) is list)

                if len(plan["testplan"]["testcases"]) <= 0:
                    logger.error("The test cases list is present, but empty")
                results.append(len(plan["testplan"]["testcases"]) > 0)
            else:
                logger.error("The key 'testplan' is missing in the request to the automator")
        except KeyError:
            results.append(False)
        except TypeError:
            results.append(False)
        except ValueError:
            results.append(False)

        return all(results)


class SessionConnectionType(Enum):
    LOCAL_FAILOVER_TO_CLOUD = 1
    CLOUD_FAILOVER_TO_LOCAL = 2
    LOCAL_ONLY = 3
    CLOUD_ONLY = 4


class Session:
    """
    A connection to remote MQTT brokers for running tests.

    This object only tracks state surrounding the KaijuMqtt connection.
    """

    automation_status_topic_pattern = "test_runner/{}"

    def __init__(self):
        """Constructor."""
        self.kaiju: KaijuMqtt = KaijuMqtt()
        self.cleanup_funcs: List = []
        self.cloud_topic_format: bool = False
        # this is the intended rae target in the format r3000123 so we can for topics with it
        self.rae_topic_string: Optional[Text] = None
        self.connected_to_cloud: bool = False

    def _host_to_rae_name(self, userstring: Text) -> None:
        """
        Set the internal rae topic string part to r3000123 from pretty much anything a user types.

        :param userstring: The RAE host/ip or connection configuration to connect to.
        :return: None
        """
        pattern = r"r\d{7}"
        foundparts = re.findall(pattern, userstring)
        if len(foundparts) > 0:
            self.rae_topic_string = foundparts[0]
        else:
            raise ValueError(MISSING_RAE_TARGET)

    def connect(self, broker: Text, port: int, connection: SessionConnectionType = SessionConnectionType.LOCAL_FAILOVER_TO_CLOUD) -> None:
        """
        Connect the underlying broker.

        The client should explicitly call mysession.destructor() to clean up.

        The connection is tried based on four possible options specified in the connection parameter.
        The default is LOCAL_FAILOVER_TO_CLOUD, which first attempts to connect directly to the configuration specified.
            If that fails, it will fail over to the cloud configuration, if available.
        The CLOUD_FAILOVER_TO_LOCAL is the inverse.
        The LOCAL_ONLY and CLOUD_ONLY options will only attempt to connect to those configurations.

        Connections can be the simple hostname/IP and port pair, or can be named configurations as specified in the
        kaiju_mqtt_py library documentation. The special case is the "cloud" which will need the downloaded certs.

        :param broker: The RAE host/ip or connection configuration to connect to.
        :param port: The port to connect to. The normal default is 1883, but this is not set by default.
        :param connection: The type of connection to make.
        :return: None
        """

        self._host_to_rae_name(broker)

        if broker == CLOUD_BROKER_NAME:
            raise ValueError("We already know how to connect to the cloud. You should specify the RAE or configuration name.")

        if connection == SessionConnectionType.LOCAL_FAILOVER_TO_CLOUD:
            try:
                self.kaiju.connect(broker, port)
            except (gaierror, Exception):
                # todo other errors - dns?
                try:
                    self.kaiju.connect(CLOUD_BROKER_NAME, port)
                    self.connected_to_cloud = True
                except (gaierror, Exception):
                    logger.error("The AWS IoT cloud broker did not respond.\nThis is most likely a network problem.")
                    return
        elif connection == SessionConnectionType.CLOUD_FAILOVER_TO_LOCAL:
            try:
                self.kaiju.connect(CLOUD_BROKER_NAME, port)
                self.connected_to_cloud = True
            except (gaierror, Exception):
                # todo other errors - timeout?
                self.kaiju.connect(broker, port)
        elif connection == SessionConnectionType.LOCAL_ONLY:
            self.kaiju.connect(broker, port)
        elif connection == SessionConnectionType.CLOUD_ONLY:
            self.kaiju.connect(CLOUD_BROKER_NAME, port)
            self.connected_to_cloud = True

    def subscribe(self, topic: Text, newfunc: Any, options_dict: Dict = None) -> None:
        """
        Subscribe to a topic with the underlying MQTT broker.

        This typically would be used to subscribe to the status of a test plan.

        The signature of the new function should be:
        def handle_updates(client, userdata, packet):
            ...

        This is the normal shape for a paho-mqtt topic message subscriber. The most interesting arg is packet.payload,
        of type dict. The packet.payload is a list of dicts. The dicts start out with the following keys:
        url, status, name logfile, step
        These will be populated with the current state of the test run. This will get called typically whenever one of
        the elements changes its value in the Automator module.

        :param topic:
        :param newfunc:
        :param options_dict:
        :return:
        """
        options = options_dict if options_dict else {"qos": 1, "timeoutMs": 15000}
        cleanup = self.kaiju.subscribe(topic, newfunc, options)

        self.cleanup_funcs.append(cleanup)

    def get_test_plan_for_device(self, device: DeviceIdentifier) -> Dict:
        """
        Request a test plan from the remote server.

        This is returned as a JSON dict.

        Example response:
        {"branch": "5.1",
        "testcases": [
                {"exec": "/tests/suite/file1.js?args"},
                {"exec": "/tests/suite/file2.js?args"},
                ...
            ],
        "sdkVersion": "ninja_6",
        }


        To run this plan, it needs to be put in the following structure:
        { "device_ip": "some_ip",
          "testplan" : <this object> }

        :param device: The DeviceIdentifier to use in the data section of the request.
        :return: The response from the Automator module as a dict.
        """
        # i'm making a request to a service on the RAE at topic test_runner/get_testplan
        topic = topicmaker(
            DestinationType.CLOUD if self.connected_to_cloud else DestinationType.RAE,
            DestinationType.RAE,
            TopicType.REQUESTERS_REQUEST_TOPIC,
            Session.automation_status_topic_pattern.format("get_testplan"),
            self.rae_topic_string,
        )
        response = self.kaiju.request(topic, device.as_json(), options={"qos": 1, "timeoutMs": 3 * 60 * 1000})
        return response

    @retry((MqttRetryableError,))
    def run_plan(self, plan) -> Dict:
        """
        Send a request to run a specified test plan.

        This will do a basic sanity check on the test plan for general shape before submitting, because I am a terrible
        typist. If there is a problem with the plan's format, SyntaxError will be raised.

        A request needs to be formed around the results of a call to get_test_plan_for_device before
        calling this. It should be shaped like this:
        { "device_ip": "some_ip",
          "testplan" : <test plan object from get_test_plan_for_device>}


        The plan will get a basic sanity check before being sent on. Errors will be surfaced as SyntaxError.

        :param plan: The plan to execute.
        :return: The response from the Automator module as a dict.
        """
        if not Request.sanity_check(plan):
            logger.critical("The request failed basic sanity checks.")
            raise SyntaxError("The request failed basic sanity checks.")
        topic = topicmaker(
            DestinationType.CLOUD if self.connected_to_cloud else DestinationType.RAE,
            DestinationType.RAE,
            TopicType.REQUESTERS_REQUEST_TOPIC,
            Session.automation_status_topic_pattern.format("run_tests"),
            self.rae_topic_string,
        )

        response = self.kaiju.request(topic, plan, {"qos": 1, "timeoutMs": 60 * 1000})
        # Detect and report on fail states
        if "body" in response and "message" in response["body"] and "Executing testplan on target." not in response["body"]["message"]:
            if "Device is currently busy" in response["body"]["message"]:
                # busy message looks similar to this:
                # {'status': 200,
                # 'body': {'status': 'running', 'message':
                #          'Device is currently busy running tests, request test cancellation or try again later'}}
                requested_device: Optional[DeviceIdentifier] = None

                # locate the device identifier in the request
                if "target" in plan:
                    if "esn" in plan["target"]:
                        requested_device = DeviceIdentifier(esn=plan["target"]["esn"])
                    elif "ip" in plan["target"]:
                        requested_device = DeviceIdentifier(ip=plan["target"]["ip"])
                    elif "serial" in plan["target"]:
                        requested_device = DeviceIdentifier(serial=plan["target"]["serial"])
                elif "device_ip" in plan:
                    requested_device = DeviceIdentifier(ip=plan["device_ip"])
                elif "device_esn" in plan:
                    requested_device = DeviceIdentifier(esn=plan["device_esn"])
                elif "device_serial" in plan:
                    requested_device = DeviceIdentifier(serial=plan["device_serial"])

                if requested_device is not None:
                    self.cancel_plan_for_device(requested_device)

                raise MqttRetryableError("The device thinks it was busy. Requesting a cancel of the current run.")

            elif "Failed to lookup" in response["body"]["message"]:
                """ The not-found-device message looks like this:
                {'status': 200, 'body':
                {'message': 'Failed to lookup device based on the data provided, please double check data,
                launch Netflix and try again', 'error': 'Error: Failed to lookup device based on the data provided,
                please double check data, launch Netflix and try again ... (stack trace)'}}
                """
                raise ValueError("The RAE does not recognize the device identifier:\n{}".format(response["body"]["message"]))

            raise ValueError("The automator rejected the request to run tests:\n{}".format(response["body"]["message"]))

        return response

    def cancel_plan_for_device(self, device) -> Dict:
        """
        Request that we cancel the tests for this device.

        :param device: Which device to cancel for.
        :return: dict with keys status and body. Status will be a typical HTTP error code.
        """
        topic = topicmaker(
            DestinationType.CLOUD if self.connected_to_cloud else DestinationType.RAE,
            DestinationType.RAE,
            TopicType.REQUEST,
            Session.automation_status_topic_pattern.format("cancel_tests"),
            self.rae_topic_string,
        )
        response = self.kaiju.request(topic, device.as_json())
        return response

    def destructor(self):
        """
        Cleanly shut down the KaijuMqtt object and disconnect.

        Some unsubscribe actions need to be performed on shutdown of the client. I'd suggest putting this in a finally:
        clause to prevent strange behaviors. It is safe to call this multiple times.

        :return:
        """
        [x() for x in self.cleanup_funcs]
        self.kaiju.close()

    def get_eyepatch_connected_esn_list(self) -> List[Text]:
        """
        Get the list of devices for which an eyepatch is connected.

        from v 1.1
        Abstracted due to the intent to change the implementation later.

        :return: list of strings, which are the ESNs with detected eyepatch configurations.
        """
        topic = topicmaker(
            DestinationType.CLOUD if self.connected_to_cloud else DestinationType.RAE,
            DestinationType.RAE,
            TopicType.REQUESTERS_REQUEST_TOPIC,
            "avaf/execute/peripheral.list",
            self.rae_topic_string,
        )

        reply: Dict = self.kaiju.request(topic, {"type": "eyepatch"})
        if "body" not in reply:
            raise ValueError("There was no body in the response to the peripheral list request.")
        if type(reply["body"]) is not list:
            raise ValueError("The peripheral list API did not include a list of peripherals.")
        returnme: List[Text] = [peripheral["esn"] for peripheral in reply["body"] if peripheral["esn"] != ""]
        return returnme

    def is_esn_connected_to_eyepatch(self, esn: Text) -> bool:
        """
        Convenience call to just find out if the ESN I'm interested in is in that list.

        from v 1.1
        Note that it makes a request to the RAE on every call, as there's no great way to determine cache status or
        valid duration.

        :param esn: The ESN of the device we are interested in. Note that this is not using the DeviceIdentifier.
        :return:
        """
        return esn in self.get_eyepatch_connected_esn_list()

    def status(self, **kwargs) -> Dict:
        """
        Get the state of in-memory automators.

        These are cleared any time the automator service restarts. The result object includes the most recent topic to
        subscribe to for the specified device.

        :param kwargs: device=DeviceIdentifier(...) - an optional device to attempt a match on
        :return:
        """
        device: DeviceIdentifier = kwargs.get("device", None)
        request: Dict = {}
        if device is not None:
            request.update(device.as_dict())
        topic = topicmaker(
            DestinationType.CLOUD if self.connected_to_cloud else DestinationType.RAE,
            DestinationType.RAE,
            TopicType.REQUESTERS_REQUEST_TOPIC,
            "test_runner/status",
            self.rae_topic_string,
        )
        return self.kaiju.request(topic, request, {"qos": 1, "timeoutMs": 15000})


class StatefulSession:
    """
    A simplified client that handles most of the boilerplate of monitoring testing.

    This object handles state of the connection to a KaijuMqtt agent, the device, and the test plan.

    This object also simplifies getting status updates. Any object that implements "handle_progress_update(payload)" and
    "handle_run_complete(packet)" can be appended to this.status_watchers to get updates as the run progresses.
    """

    def __init__(self, **kwargs):
        """
        Construct a new StatefulSession. Args are passed to the DeviceIdentifier constructor.

        :param kwargs: Passed unmodified to the DeviceIdentifier constructor. ex: esn=DEVICE_12345 or ip=192.168.144.49
        """
        self.connected: bool = False
        self.device: DeviceIdentifier = DeviceIdentifier(**kwargs)
        self.plan_request: Optional[Dict] = None
        self.session: Session = Session()
        self.status_watchers = []

    def connect(self, broker: Text, port: int, connection: SessionConnectionType = SessionConnectionType.LOCAL_FAILOVER_TO_CLOUD):
        """Connect the session to an MQTT broker."""
        self.session.connect(broker, port, connection)
        self.connected = True

    def get_test_plan(self):
        """Get the test plan and store it internally."""
        plan_response = self.session.get_test_plan_for_device(self.device)
        if "status" in plan_response and plan_response["status"] != 200:
            raise ValueError(REQUEST_STATUS_FAILED)
        if (
            "body" not in plan_response
            or "testcases" not in plan_response["body"]
            or not isinstance(plan_response["body"]["testcases"], list)
            or len(plan_response["body"]["testcases"]) < 1
        ):
            if "body" in plan_response and "error" in plan_response["body"]:
                raise ValueError(plan_response["body"]["error"])
            else:
                raise ValueError(INCOMPLETE_PLAN_REQUEST_ERROR)

        self.plan_request = self.device.as_dict()
        self.plan_request["testplan"] = plan_response["body"]

    def run_tests(self):
        """Start the test plan and update watchers in the status_watchers list."""
        if self.plan_request is None:
            self.get_test_plan()

        def receive_update(client, userdata, packet):
            """
            Broadcast received updates to watchers.

            :param client:
            :param userdata:
            :param packet:
            :return:
            """

            [watcher.handle_progress_update(packet.payload["results"]) for watcher in self.status_watchers]

            # we hand down the entire packet so the topic and payload can be inspected
            # when multiple devices are sending updates at once, this is how you tell which one is done during reporting
            if "running" in packet.payload and not packet.payload["running"]:
                [watcher.handle_run_complete(packet) for watcher in self.status_watchers]

        full_result = self.session.run_plan(self.plan_request)
        if full_result["status"] != 200:
            logger.error("The test plan run was not run:")
            logger.error(full_result)

        if full_result is None or "body" not in full_result or "resultTopic" not in full_result["body"]:
            raise ValueError(full_result["body"]["error"])
        else:
            # Subscribe to topic returned as “resultTopic” to get test result stream
            self.session.subscribe(full_result["body"]["resultTopic"], receive_update)

    def cancel(self):
        self.session.cancel_plan_for_device(self.device)

    def close(self):
        self.session.destructor()


@contextmanager
def stateful_session_mgr(**kwargs) -> Generator[StatefulSession, None, None]:
    """
    Conveniently makes and cleans up a StatefulSession.

    :param kwargs: rae (str), the broker to reach out to
    :return:
    """
    session = StatefulSession(**kwargs)
    try:
        if "rae" not in kwargs:
            raise ValueError("The stateful session manager call needs the keyword 'rae'.")
        session.connect(kwargs["rae"], 1883)  # we really don't have an alternate port, but you get it
        yield session
    finally:
        session.close()
