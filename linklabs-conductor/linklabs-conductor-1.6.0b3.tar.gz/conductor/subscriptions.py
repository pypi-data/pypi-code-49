import logging
import json

from queue import Queue, Empty
from threading import Thread, Event

import requests
import websockets
import zmq

LOG = logging.getLogger(__name__)


class SubscriptionError(Exception):
    """
    Exception thrown when a subscription reaches a fatal state.
    """
    pass


class Subscription(Thread):
    """ Uplink Subscription for Conductor Subjects. """

    def __init__(self, uplink_subject, callback=None):
        """ Constructs a Conductor Subscription Thread.

        Args:
            uplink_subject(:class:`.UplinkSubject`): The Conductor Subject to
                subscribe the uplink messages for.
            callback(func): A function that will get called when messages are
                recieved. Takes the uplink message object as the only argument.

        Note:
            Will pass messages through the supplied callback when supplied.
            Otherwise, will be required to utilize the iterator,  or access
            the ul_queue attribute directly.

        Example:
            Using a Callback ::
                ap = u.get_access_point("xx:xx:xx:xx:xx:xx")
                def cb(msg):
                    print(msg)
                sub = Subscription(ap, cb)
                sub.start()
                sleep(15)
                sub.stop()

            Using an iterator ::
                ap = u.get_access_point("xx:xx:xx:xx:xx:xx")
                def cb(msg):
                    print(msg)
                sub = Subscription(ap)
                num_msgs = 0
                sub.start()
                for msg in sub.itr():
                    num_msgs += 1
                    print(msg)
                    if num_msgs >= 2:
                        break
                sub.stop()

        Returns:
            Subscription Thread.
        """
        Thread.__init__(self)
        self.stop_event = Event()
        self.subject = uplink_subject
        self.name = "{}-uplink_subscription".format(self.subject.subject_id)
        self.ul_queue = Queue()
        self.callback = callback

    def run(self):
        """ The Subscription Thread.

        Note:
            Not Implemented in base class.
        """
        raise SubscriptionError("Use a derived subscription class ({})!"
                                .format(self.__subclasses__()))

    def iter(self):
        """ Provides an iterator function to handle the live subscription in a
        blocking fashion.

        Yeilds:
            UplinkMessage
        """
        while not self.stop_event.is_set():
            try:
                yield self.ul_queue.get_nowait()
            except Empty:
                continue

    def stop(self):
        """ Kill the Subscription Thread. """
        self.stop_event.set()


class ZeroMQSubscription(Subscription):
    """ ZeroMQ 2 Implementation for uplink events given an UplinkSubject.

    Note:
        Requires port-forwardding to the server running the subscription.
    """

    def __init__(self, uplink_subject, port=11101, callback=None):
        super(ZeroMQSubscription, self).__init__(uplink_subject, callback)
        self.event_count = 0
        self.published_event_count = 0
        self.subscription_id = None
        self.port = port

        # Instantiate ZMQ Objects.
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.REP)
        self.ip = requests.get("https://api.ipify.org").text

        # Initialize the ZMQ Socket.
        LOG.info("Binding endpoint {}...".format(self.endpoint))
        try:
            self.socket.bind("tcp://*:{}".format(self.port))
        except Exception as e:
            raise SubscriptionError("Could not bind port! {}".format(str(e)))

        # Issue Subscription Request
        self.url = "{}/data/{}/{}/{}/subscriptions".format(
            self.subject.client_edge_url, self.subject.uplink_type,
            self.subject.subject_name, self.subject.subject_id)
        data = {
            "channelRequest": {
                "type": "ZeroMQ2",
                "endpoint": self.endpoint,
            },
            "subscriptionProperties": {
                "filterProperties": []
            }
        }

        self.subscription_id = self.subject._post(self.url, json=data)["id"]
        LOG.info("Created subscription: {}".format(self.subscription_id))

    def run(self):
        LOG.info("Start subscription...")
        while not self.stop_event.is_set():
            if self.socket.closed:
                raise SubscriptionError("Socket Closed!")

            msg = self.socket.recv_json()
            msg_type = msg["messageType"]
            LOG.info("Recieved {} message!".format(msg_type))
            LOG.debug("RXed message: {}".format(msg))

            if msg_type == "remove" or msg_type == "Error":
                LOG.error(msg["headers"]["ClosedReason"])
                continue
            elif "event" not in msg or not msg["event"]:
                continue
            evt = msg["event"]
            self.event_count += 1
            if self.callback:
                self.callback(self.subject._build_msg(self.subject.session,
                                                      evt["uuid"],
                                                      self.subject.instance,
                                                      evt))
            else:
                self.ul_queue.put(evt)

            self._send_response(msg.get("uuid"))

    def _send_response(self, uuid):
        """ Sends an acknowledgement response.

        Args:
            uuid(int): The UUID of the recieved message.
        """
        attempt = 0
        response = {
            "requestId": uuid,
            "responseStatus": {"OK": None},
            "service": "Subscription",
            "method": "Subscription",
            "responseData": None
        }
        while attempt < 5:
            try:
                attempt += 1
                self.socket.send_json(response)
                self.published_event_count += 1
                return
            except zmq.error.ZMQError:
                continue
            LOG.error("Could not send response!")

    def _close_subscription(self, err=None):
        """ Sends a close notification to Conductor.

        Args:
            err(str): An error message will failing.
        """
        response = {
            "subscriptionId": self.subscription_id,
            "messageType": "UnsubscribeRequest" if not err else "Error",
            "headers": {
                "matchedEventCount": self.event_count,
                "ClosedReason": "Requested by user" if not err else err,
                "publishedEventCount": self.published_event_count,
            },
            "event": None
        }
        return self.socket.send_json(response)

    def stop(self):
        self.stop_event.set()
        self._close_subscription()

    @property
    def endpoint(self):
        """ The Endpoint is the protocol/address/port of the zmq server. """
        return "tcp://{}:{}".format(self.ip, self.port)


class WebsocketSubscription(Subscription):
    """ Websocket Implementation for uplink events given an UplinkSubject.

    Note:
        Conductor Proxies will break websocket implementation.
    """

    def __init__(self, uplink_subject, callback=None):
        """

        """
        super(WebsocketSubscription, self).__init__(uplink_subject, callback)

        # Issue Subscription Request
        self.url = "{}/data/{}/{}/{}/subscriptions".format(
            self.subject.client_edge_url, self.subject.uplink_type,
            self.subject.subject_name, self.subject.subject_id)
        data = {
            "channelRequest": {
                "type": "Websocket",
            },
            "subscriptionProperties": {
                "filterProperties": []
            }
        }

        # Manually post to acquire HTTPS Headers.
        resp = self.session.post(self.url, json=data)
        resp.raise_for_status()
        rep = resp.json()

        self.subscription_id = rep["id"]
        self.ws_url = rep["websocketUrl"]["href"]
        LOG.info("Created subscription: {}".format(self.subscription_id))

        # Initialize Websocket Connection
        self.websocket = None
        try:
            hdrs = resp.request.headers.items()
            self.websocket = websockets.connect(self.ws_url,
                                                ping_interval=None,
                                                ping_timeout=50.0,
                                                extra_headers=hdrs)
        except Exception as e:
            raise SubscriptionError("Could not connect to websocket! {}"
                                    .format(str(e)))

    def run(self):
        while not self.stop_event.is_set():
            if self.terminated:
                raise SubscriptionError("Websocket terminated!")

            msg = json.loads(str(self.websocket.recv()))
            obj = self.subject._build_msg(self.subject.session,
                                          msg.get("uuid"),
                                          self.subject.instance,
                                          msg)
            if self.callback:
                self.callback(msg)
            else:
                self.ul_queue.put(obj)

    @property
    def terminated(self):
        if self.websocket:
            return not self.websocket.open
        return True
