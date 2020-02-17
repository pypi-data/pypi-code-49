import logging
import os
import sys
import threading
import time
import traceback
from collections import namedtuple
from uuid import uuid4

import sentry_sdk
import zmq

from om.message import Message

CallbackEntry = namedtuple("CallbackEntry", ["timestamp", "result"])


def channel_to_response_topic(channel):
    if hasattr(channel, "decode"):
        cpy = channel.decode("utf-8")
    else:
        cpy = channel
    topic = "rpc-rep-{}".format(cpy)
    if hasattr(topic, "encode"):
        return topic.encode("ascii")
    return topic


def channel_to_request_topic(channel):
    if hasattr(channel, "decode"):
        cpy = channel.decode("utf-8")
    else:
        cpy = channel
    topic = "rpc-req-{}".format(cpy)
    if hasattr(topic, "encode"):
        return topic.encode("ascii")
    return topic


class RPCClient(object):
    class RPCEntry(object):
        def __init__(self):
            self.timestamp = time.time()
            self.result = None

    def __init__(self, config, context=None, channels=None):
        if channels is None:
            channels = []
        context = context or zmq.Context()
        self.log = logging.getLogger("rcp-client")
        self.lock = threading.RLock()
        self.results = dict()
        self.name = config.NAME
        if hasattr(config, "RPC_CLIENT_SYNC_TIMEOUT"):
            self.sync_timeout = config.RPC_CLIENT_SYNC_TIMEOUT
        else:
            self.sync_timeout = 3.0
        self.sub = context.socket(zmq.SUB)
        self.sub.connect("tcp://{}:{}".format(config.BROKER_HOST, config.BROKER_PUB_PORT))
        self.channels = channels
        for channel in channels:
            topic = channel_to_response_topic(channel)
            self.log.info("subscribing to channel: {}".format(topic))
            self.sub.subscribe(topic)
        self.pub = context.socket(zmq.PUB)
        self.pub.connect("tcp://{}:{}".format(config.BROKER_HOST, config.BROKER_SUB_PORT))
        self.receiver = threading.Thread(target=self.recv_thread)
        self.receiver.setDaemon(True)
        self.receiver.start()

    def return_error(self, status):
        return {"status": status}

    def return_success(self, message):
        response = message.get("response", {})
        message.setdefault("status", "success")
        if isinstance(response, dict):
            message["status"] = response.get("status")
            response.pop("status", None)
        return message

    def cleanup_old_results(self):
        now = time.time()
        with self.lock:
            to_delete = []
            for rpc_id, entry in self.results.items():
                if now - entry.timestamp > 10:
                    to_delete.append(rpc_id)
            for rpc_id in to_delete:
                try:
                    del self.results[rpc_id]
                except KeyError:
                    pass

    def _call(self, channel, type, request):
        rpc_id = str(uuid4())
        message = Message(
            name=self.name,
            type=type,
            rpc_id=rpc_id,
            request=request,
        )
        message.to_socket(self.pub, channel_to_request_topic(channel))
        return rpc_id

    def call_async(self, channel, type, request):
        return self._call(channel, type, request)

    def call_sync(self, channel, type, request):
        self.log.warning("running in sync mode, this may cause delay")
        rpc_id = self.call_async(channel, type, request)
        if channel not in self.channels:
            self.log.error("called in sync mode, but no subscription on channel is present!", extra={
                "channel": channel,
                "subscriptions": str(self.channels)
            })
            return self.return_error("no_subscription_on_channel")
        with self.lock:
            self.results[rpc_id] = self.RPCEntry()
        # wait a little because service cannot answer instantly
        time.sleep(0.1)
        while True:
            with self.lock:
                entry = self.results.get(rpc_id)
            if entry.result:
                with self.lock:
                    self.results.pop(rpc_id, None)
                return self.return_success(entry.result)
            duration = (time.time() - entry.timestamp)
            if duration > self.sync_timeout:
                return self.return_error("timeout")
            time.sleep(self.sync_timeout / 5.0)

    def rpc(self, channel, type, request):
        result = self.call_sync(channel, type, request)
        return result.get("response") or {}

    def recv_thread(self):
        try:
            while True:
                topic, message = Message.from_socket(self.sub)
                rpc_id = message.get("rpc_id")
                with self.lock:
                    if rpc_id in self.results:
                        self.results[rpc_id].result = message
        except KeyboardInterrupt:
            pass
        except Exception as e:
            sentry_sdk.capture_exception(e)
            traceback.print_exc(file=sys.stderr)
            sys.stderr.flush()
            time.sleep(1)
            os._exit(1)


class RPCServer(object):
    @staticmethod
    def gateway_filter(gate=None, direction=None):
        def _filter(request, message, handler):
            gateway = request.get("gateway")
            if not gateway:
                return False
            return (not gate or gate == gateway.get("gate")) and \
                   (not direction or direction == gateway.get("direction"))

        return _filter

    def __init__(self, config, context=None):
        context = context or zmq.Context()
        self.name = config.NAME
        self.sub = context.socket(zmq.SUB)
        self.sub.connect("tcp://{}:{}".format(config.BROKER_HOST, config.BROKER_PUB_PORT))
        self.pub = context.socket(zmq.PUB)
        self.pub.connect("tcp://{}:{}".format(config.BROKER_HOST, config.BROKER_SUB_PORT))
        self.handlers = {}
        self.filters = []
        self.log = logging.getLogger("rpc")

    def add_filter(self, handler):
        self.filters.append(handler)

    def _thread_wrapper(self):
        try:
            self.run()
        except KeyboardInterrupt:
            pass
        except Exception as e:
            sentry_sdk.capture_exception()
            traceback.print_exc(file=sys.stderr)
            sys.stderr.flush()
            time.sleep(1)
            os._exit(1)

    def register_handler(self, channel, type, handler):
        """
        :param type: the request type, specify * to catch all types, in this case no other
                     handler will be run for the channel except for the wildcard handler
        :param handler: request handler of the form (request:dict, meta:dict) -> any
                        if the handler returns a dict which contains the key "status",
                        then the value of "status" will be used as the rpc response status.
                        There are no other reserved keys except "status".
        """
        self.log.debug("register handler {}:{} -> {}".format(channel, type, handler))
        channel = self._ascii(channel)
        type = self._ascii(type)
        self.sub.subscribe(channel_to_request_topic(channel))
        self.handlers[(channel, type)] = handler

    def _channel_from_topic(self, topic):
        return topic.split(b"-", 2)[-1]

    def _ascii(self, x):
        if hasattr(x, "encode"):
            return x.encode("ascii")
        else:
            return x

    def _handlers_handler(self):
        pass

    def should_process_message(self, request, message, handler):
        if self.filters:
            for filter in self.filters:
                if filter(request=request, message=message, handler=handler):
                    return True
            return False
        return True

    def find_handler(self, channel, type):
        channel = self._ascii(channel)
        type = self._ascii(type)
        if type == "_handlers":
            return self._handlers_handler
        else:
            return self.handlers.get((channel, b"*")) or self.handlers.get((channel, type))

    def run_as_thread(self):
        thread = threading.Thread(target=self._thread_wrapper)
        thread.setDaemon(True)
        thread.start()
        return thread

    def run(self):
        while True:
            topic, message = Message.from_socket(self.sub)
            channel = self._channel_from_topic(topic)
            request = message["request"]
            type = message["type"]
            del message["request"]
            message["channel"] = channel

            self.log.debug("processing request for {}:{} -> {}".format(topic, channel, request))
            handler = self.find_handler(channel, type)
            if handler:
                try:
                    if not self.should_process_message(request, message, handler):
                        continue
                except Exception as e:
                    sentry_sdk.capture_exception()
                    self.log.info("exception in filter {}:{}".format(channel, type))
                    continue

                try:
                    response = handler(request, message)
                except Exception as e:
                    sentry_sdk.capture_exception()
                    self.log.info("exception in handler {}:{}".format(channel, type))
                    response = {"status": "handler_error", "exception": str(e)}
            else:
                self.log.warning("no handler found for {}:{}".format(channel, type))
                continue

            self.log.debug("response: {}".format(response))
            result = Message(type=type, name=self.name)
            result["rpc_id"] = message["rpc_id"]
            result["response"] = response
            result.to_socket(self.pub, channel_to_response_topic(channel))
