# coding=utf-8
from __future__ import unicode_literals

import calendar
import datetime
import logging
import os
import sys
import threading
import time
import traceback
from collections import defaultdict, namedtuple

import related
import six
import zmq
from dateutil.parser import parse

from om.message import Message, Topic
from om.utils.charset import CharsetConverter


class Category(object):
    BOOKED_DIGIMON = "booked-digimon"
    BOOKED_EMPLOYEE = "booked-employee"
    BOOKED_VISITOR = "booked-visitor"
    PERMANENT_DIGIMON = "permanent-digimon"
    PERMANENT_EMPLOYEE = "permanent-employee"
    FILLER_EMPLOYEE = "filler-employee"
    FILLER_DIGIMON = "filler-digimon"
    FILLER_VISITOR_BUTTON = "filler-visitor-button"
    FILLER_VISITOR_UNEXPECTED = "filler-visitor-unexpected"

    UNKNOWN_CATEGORY = "unknown-category"


@related.immutable
class AccessProperties(object):
    category = related.StringField(required=False, default=Category.FILLER_VISITOR_UNEXPECTED)
    recurrence = related.StringField(required=False, default="")
    duration = related.IntegerField(required=False, default=0)
    occupant_check = related.BooleanField(required=False, default=False)
    zone = related.StringField(required=False, default=None)


MediumEntry = namedtuple("MediumEntry", ["medium_id", "medium_type", "medium_payload"])


class ExternalAuthorizationProvider(object):
    USER_PREFIX = ""

    VALID_MEDIUM_TYPES = ["*"]
    VALID_REASONS = ["unknown_medium", "authority"]
    LAST_RESULT_CACHE_ENABLED = True

    PREPROCESS_MEDIUM = True

    def __init__(self, config):
        assert self.USER_PREFIX, ("please set USER_PREFIX")
        assert not all(x in self.USER_PREFIX for x in ("-", "_")), ("user prefix must not contain -, _")

        self.config = config
        self.context = zmq.Context()
        self.sub = self.context.socket(zmq.SUB)
        self.pub = self.context.socket(zmq.PUB)
        self.sub.connect("tcp://{}:{}".format(config.BROKER_HOST, config.BROKER_PUB_PORT))
        self.pub.connect("tcp://{}:{}".format(config.BROKER_HOST, config.BROKER_SUB_PORT))
        self.sub.subscribe(Topic.COUNT)
        self.sub.subscribe(Topic.ACCESS_REJECT)

        self.cache = defaultdict(tuple)

    def user_id_for_identifier(self, category, user_identifier):
        return "{}-{}_{}".format(self.USER_PREFIX, category, user_identifier)

    def process_reject_message(self, message):
        """
        decide if we want to process the specific reject message
        this default implementation only checks on authority and unknown_medium reasons and
        only if the user is on the loop if a loop is available

        :param message: the full access_reject message
        :return: true if we want to proceed, false otherwise
        """

        # if we have a presence loop we only check if the user is actually on the loop
        if message.get("has_presence_loop") and not message.get("on_presence_loop"):
            return False

        # only check for spefific decisions
        reason = message.get("reason")
        if reason not in self.VALID_REASONS:
            return False

        # only check for specific medium types, or all if it is set to wildcard (*)
        if "*" not in self.VALID_MEDIUM_TYPES and message.get("medium_type") not in self.VALID_MEDIUM_TYPES:
            return False

        return True

    def _convert_to_timestamp(self, dt):
        if dt is None:
            return None

        if isinstance(dt, six.string_types):
            dt = parse(dt)

        if isinstance(dt, datetime.datetime):
            dt = calendar.timegm(dt.timetuple())

        if isinstance(dt, float):
            dt = int(dt)

        if not isinstance(dt, six.integer_types):
            raise ValueError("cannot convert '{}' to timestamp".format(dt))

        return dt

    def unknown_access(self, user_id, user_category, category, zone=None):
        assert category in [Category.FILLER_VISITOR_UNEXPECTED, Category.FILLER_VISITOR_BUTTON]
        start = time.time()
        end = None
        return self.access(user_id, user_category, start, category, end, zone=zone)

    def access(self, user_id, user_category, start, category, end=None, recurrence=None, duration=0,
               occupant_check=False, zone=None):
        result = {
            "category": category,
            "start": self._convert_to_timestamp(start),
            "end": self._convert_to_timestamp(end),
            "user": self.user_id_for_identifier(user_category, user_id),
            "recurrence": recurrence,
            "duration": duration,
            "occupant_check": occupant_check,
        }

        if zone:
            result["zone"] = zone

        return result

    def report_conncetion_status(self, online, delay):
        pass

    def has_access(self, type, id, gate, direction, message, medium_payload=None):
        """
        this medium checks if current mediums has access to parking lot


        on success a dictionary will be returned with the following structure, where as medium can be optional
        {
            "access": {access} // access that matched or is generated (see ocpp)
            "medium": {id=medium id, type=medium type, access2=list of accesses, scheme...} // just like redis payload
        }

        else the function should return 'False' if medium is unknown

        :param type: medium_type
        :param id: medium_id
        :param gate: gate
        :param direction: direction
        :param message: reject message
        :param medium_payload: the medium payload from tracking
        :return: dict (success) or False (fail)
        """
        raise NotImplementedError()

    def check_in(self, user, medium_id, medium_type, timestamp, gate, direction, message):
        raise NotImplementedError()

    def check_out(self, user, medium_id, medium_type, timestamp, gate, direction, message):
        raise NotImplementedError()

    def preprocess_medium(self, medium_id, medium_type):
        if self.PREPROCESS_MEDIUM:
            if not hasattr(self, "charset"):
                self.charset = CharsetConverter.from_yaml(self.config.YAML.charset)
            if medium_type == "lpr":
                return self.charset.clean(medium_id)
        return medium_id

    def is_in_cache(self, id, type, gate):
        return self.cache[gate][:2] == (id, type)

    def get_cached_result(self, gate):
        return self.cache[gate][2]

    def set_cache(self, id, type, gate, result):
        self.cache[gate] = (id, type, result)

    def clear_cache(self, gate):
        try:
            del self.cache[gate]
        except KeyError:
            pass

    def _get_medium_entry_from_payload(self, payload, medium_type=None):
        if not medium_type:
            medium_type = payload.get("medium_type", "lpr")
        medium_id = self.preprocess_medium(payload.get("id"), medium_type)
        return MediumEntry(
            medium_id=medium_id, medium_type=medium_type, medium_payload=payload.get("medium_payload", {})
        )

    def _get_mediums_from_reject_message(self, message):
        mediums = []
        if "last_medium_events" in message:
            last_mediums_events = message.get("last_mediums_events", {})
            for medium_type in last_mediums_events.keys():
                medium_entry = self._get_medium_entry_from_payload(last_mediums_events[medium_type], medium_type)
                if medium_type == "lpr":
                    mediums.insert(1, medium_entry)
                else:
                    mediums.append(medium_entry)
        else:
            medium_entry = self._get_medium_entry_from_payload(message)
            mediums.append(medium_entry)
        return mediums

    def _handle_access_reject(self, message):
        if not self.process_reject_message(message):
            return

        gateway = message.get("gateway", {})
        gate, direction = gateway.get("gate"), gateway.get("direction")
        mediums = self._get_mediums_from_reject_message(message)
        for medium in mediums:
            # reset values
            result = False
            start = time.time()
            medium_id = medium.medium_id
            type = medium.medium_type
            if self.is_in_cache(medium_id, type, gate):
                logging.info("result for {} is in cache".format((medium_id, type, gate)))
                result = self.get_cached_result(gate)
            else:
                try:
                    # TODO get the matched medium id or rather the whole medium with all accesses
                    result = self.has_access(type, medium_id, gate, direction, message, medium.medium_payload)
                except Exception:
                    traceback.print_exc()
                    self.report_conncetion_status(False, time.time() - start)
                    self.clear_cache(gate)
                else:
                    self.report_conncetion_status(True, time.time() - start)
                    self.set_cache(medium_id, type, gate, result)

            if result is False:
                logging.info("id {} not allowed at {}".format(medium_id, gate))
            else:
                logging.info("id {} allowed at {}".format(medium_id, gate))
                result["id"] = medium_id
                message = Message(
                    name=self.config.NAME,
                    type="auth",
                    id=medium_id,
                    medium_type=type,
                    gateway=message.get("gateway"),
                    access=result.get("access", {}),
                    medium=result.get("medium", {}),
                )
                message.to_socket(self.pub, Topic.BACKEND)
                logging.debug("sending: {}".format(message))

    def _handle_count_in(self, message):
        if not message.get("user", "").startswith(self.USER_PREFIX):
            return

        gateway = message.get("gateway", {})
        start = time.time()
        try:
            res = self.check_in(
                user=message.get("user"),
                medium_id=message.get("id"),
                medium_type=message.get("medium_type"),
                timestamp=message.get("timestamp"),
                gate=gateway.get("gate"),
                direction=gateway.get("direction"),
                message=message
            )
        except Exception:
            traceback.print_exc()
            self.report_conncetion_status(False, time.time() - start)
            return False
        else:
            self.report_conncetion_status(True, time.time() - start)
            return res

    def _handle_count_out(self, message):
        if not message.get("user", "").startswith(self.USER_PREFIX):
            return

        if message.get("gateway", {}).get("gate") == "automatically_deleted":
            return

        gateway = message.get("gateway", {})
        start = time.time()
        try:
            res = self.check_out(
                user=message.get("user"),
                medium_id=message.get("id"),
                medium_type=message.get("medium_type"),
                timestamp=message.get("timestamp"),
                gate=gateway.get("gate"),
                direction=gateway.get("direction"),
                message=message
            )
        except Exception:
            traceback.print_exc()
            self.report_conncetion_status(False, time.time() - start)
            return False
        else:
            self.report_conncetion_status(True, time.time() - start)
            return res

    def run_as_thread(self):
        thread = threading.Thread(target=self._thread_wrapper)
        thread.setDaemon(True)
        thread.start()
        return thread

    def _thread_wrapper(self):
        try:
            self.run()
        except KeyboardInterrupt:
            pass
        except Exception as e:
            logging.error("exception in auth provider thread: {}".format(str(e)))
            traceback.print_exc(file=sys.stderr)
            sys.stderr.flush()
            time.sleep(0.1)
            os._exit(1)

    def run(self):
        while True:
            topic, message = Message.from_socket(self.sub)
            if topic == Topic.ACCESS_REJECT:
                self._handle_access_reject(message)
            elif topic == Topic.COUNT:
                direction = message.get("gateway", {}).get("direction")
                if direction == "in":
                    self._handle_count_in(message)
                elif direction == "out":
                    self._handle_count_out(message)
                else:
                    logging.error("unknown direction {} for message {}".format(direction, message))
