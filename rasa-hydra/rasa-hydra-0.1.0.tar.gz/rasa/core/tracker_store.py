import asyncio
import json
import logging
import os
import pickle
import typing
from typing import Iterator, Optional, Text, Iterable, Union

import itertools
import copy

# noinspection PyPep8Naming
import time

import opentracing

from rasa.core.actions.action import ACTION_LISTEN_NAME
from rasa.core.broker import EventChannel
from rasa.core.domain import Domain
from rasa.core.events import SlotSet
from rasa.core.trackers import ActionExecuted, DialogueStateTracker, EventVerbosity
from rasa.utils.common import class_from_module_path

if typing.TYPE_CHECKING:
    from sqlalchemy.engine.url import URL
    from sqlalchemy.engine import Engine


logger = logging.getLogger(__name__)


class TrackerStore(object):
    def __init__(
        self, domain: Optional[Domain], event_broker: Optional[EventChannel] = None
    ) -> None:
        self.domain = domain
        self.event_broker = event_broker
        self.max_event_history = None

    @staticmethod
    def find_tracker_store(domain, store=None, event_broker=None):
        if store is None or store.type is None:
            tracker_store = InMemoryTrackerStore(domain, event_broker=event_broker)
        elif store.type == "redis":
            tracker_store = RedisTrackerStore(
                domain=domain, host=store.url, event_broker=event_broker, **store.kwargs
            )
        elif store.type == "redis_cluster":
            tracker_store = RedisClusterTrackerStore(
                domain=domain, host=store.url, event_broker=event_broker, **store.kwargs
            )
        elif store.type == "mongod":
            tracker_store = MongoTrackerStore(
                domain=domain, host=store.url, event_broker=event_broker, **store.kwargs
            )
        elif store.type.lower() == "sql":
            tracker_store = SQLTrackerStore(
                domain=domain, host=store.url, event_broker=event_broker, **store.kwargs
            )
        else:
            tracker_store = TrackerStore.load_tracker_from_module_string(domain, store)

        logger.debug("Connected to {}.".format(tracker_store.__class__.__name__))
        return tracker_store

    @staticmethod
    def load_tracker_from_module_string(domain, store):
        custom_tracker = None
        try:
            custom_tracker = class_from_module_path(store.type)
        except (AttributeError, ImportError):
            logger.warning(
                "Store type '{}' not found. "
                "Using InMemoryTrackerStore instead".format(store.type)
            )

        if custom_tracker:
            return custom_tracker(domain=domain, url=store.url, **store.kwargs)
        else:
            return InMemoryTrackerStore(domain)

    async def get_or_create_tracker(self, sender_id, max_event_history=None):
        tracker = await self.retrieve(sender_id)
        self.max_event_history = max_event_history
        if tracker is None:
            tracker = await self.create_tracker(sender_id)
        return tracker

    def init_tracker(self, sender_id):
        if self.domain:
            return DialogueStateTracker(
                sender_id, self.domain.slots, max_event_history=self.max_event_history
            )
        else:
            return None

    async def create_tracker(self, sender_id, append_action_listen=True):
        """Creates a new tracker for the sender_id.

        The tracker is initially listening."""

        tracker = self.init_tracker(sender_id)
        if tracker:
            if append_action_listen:
                tracker.update(ActionExecuted(ACTION_LISTEN_NAME))
            await self.save(tracker)
        return tracker

    def save(self, tracker):
        raise NotImplementedError()

    def retrieve(self, sender_id: Text) -> Optional[DialogueStateTracker]:
        raise NotImplementedError()

    async def stream_events(self, tracker: DialogueStateTracker) -> None:
        with opentracing.tracer.start_active_span('kafka_publish_evt'):
            csi = tracker.get_slot('channelUserId')
            if csi:
                offset = await self.number_of_existing_events(tracker.sender_id)
                evts = tracker.events
                for evt in list(itertools.islice(evts, offset, len(evts))):
                    body = {"sender_id": tracker.sender_id}
                    body.update(evt.as_dict())
                    is_pii = tracker.get_slot('is_pii')
                    body["message_id"] = tracker.get_slot("messageId")

                    if body.get('event') == 'slot' and self.is_authenticate_state(tracker) and body.get('value') == 'pass':
                        tracker.update(SlotSet('is_pii', True))
                    elif is_pii and body.get('event') == 'user':
                        body['text'] = '{authentication}'

                    if body.get('event') == 'user' and tracker.current_state().get("active_form") and tracker.latest_message.intent.get('name') is None:
                        body['parse_data']['intent']['name'] = 'Test'
                        body['parse_data']['intent']['confidence'] = 1.0

                    if body.get('event') == 'bot':
                        body["prediction_error"] = tracker.get_slot('predictionError')
                        tracker.update(SlotSet('predictionError', False))

                    self.event_broker.publish(body)

    def is_authenticate_state(self, tracker):
        curr_state = tracker.current_state()
        active_form = curr_state.get('active_form')
        return active_form.get('name') == os.environ.get('AUTHENTICATION_STATE', 'authentication_form')

    async def number_of_existing_events(self, sender_id: Text) -> int:
        """Return number of stored events for a given sender id."""
        old_tracker = await self.retrieve(sender_id)
        return len(old_tracker.events) if old_tracker else 0

    def keys(self) -> Iterable[Text]:
        raise NotImplementedError()

    @staticmethod
    def serialise_tracker(tracker):
        with opentracing.tracer.start_active_span('serialise_tracker'):
            dialogue = tracker.as_dialogue()
            return pickle.dumps(dialogue)

    def deserialise_tracker(self, sender_id, _json) -> Optional[DialogueStateTracker]:
        with opentracing.tracer.start_active_span('deserialise_tracker'):
            dialogue = pickle.loads(_json)
            tracker = self.init_tracker(sender_id)
            if tracker:
                tracker.recreate_from_dialogue(dialogue)
                return tracker
            else:
                return None

    def get_channel_timeout(self, channel):
        timeouts = {
            "OMNI_VOICE_00001": 50,
            "OMNI_WEBCHAT_00001": 1200,
            "OMNI_DASHCHAT_00001": 60 * 60 * 2,
            "OMNI_IOSAPP_00001": 1200,
            "OMNI_REST_00001": 120,
        }
        return timeouts.get(channel)

    async def ping(self):
        return "ok"


class InMemoryTrackerStore(TrackerStore):
    def __init__(
        self, domain: Domain, event_broker: Optional[EventChannel] = None
    ) -> None:
        self.store = {}
        super(InMemoryTrackerStore, self).__init__(domain, event_broker)

    async def save(self, tracker: DialogueStateTracker) -> None:
        if self.event_broker:
            await self.stream_events(tracker)
        serialised = InMemoryTrackerStore.serialise_tracker(tracker)
        self.store[tracker.sender_id] = serialised

    async def retrieve(self, sender_id: Text) -> Optional[DialogueStateTracker]:
        if sender_id in self.store:
            logger.debug("Recreating tracker for id '{}'".format(sender_id))
            return self.deserialise_tracker(sender_id, self.store[sender_id])
        else:
            logger.debug("Creating a new tracker for id '{}'.".format(sender_id))
            return None

    async def keys(self) -> Iterable[Text]:
        return self.store.keys()


class RedisTrackerStore(TrackerStore):
    async def keys(self) -> Iterable[Text]:
        return self.red.keys()

    def __init__(
        self,
        domain,
        host="localhost",
        port=6379,
        db=0,
        password=None,
        event_broker=None,
        record_exp=None,
    ):

        import redis

        self.red = redis.StrictRedis(host=host, port=port, db=db, password=password)
        self.record_exp = record_exp
        super(RedisTrackerStore, self).__init__(domain, event_broker)

    async def save(self, tracker, timeout=None):
        if self.event_broker:
            await self.stream_events(tracker)

        timeout = self.get_channel_timeout(tracker.get_latest_input_channel())

        if not timeout and self.record_exp:
            timeout = self.record_exp

        serialised_tracker = self.serialise_tracker(tracker)
        self.red.set(tracker.sender_id, serialised_tracker, ex=timeout)

    async def retrieve(self, sender_id):
        with opentracing.tracer.start_active_span('redis_retrieve') as scope:
            stored = self.red.get(sender_id)
            if stored is not None:
                return self.deserialise_tracker(sender_id, stored)
            else:
                return None


class RedisClusterTrackerStore(TrackerStore):
    async def keys(self) -> Iterable[Text]:
        return await self.red_cluster.keys()

    def __init__(
            self,
            domain,
            host="localhost",
            port=6379,
            event_broker=None,
            standalone_host="localhost",
            standalone_port=6379,
            record_exp=None,
    ):
        from aredis import StrictRedisCluster, StrictRedis, RedisClusterException

        try:
            max_connections = 32 * os.cpu_count()
            logger.info(f"Redis cluster connection info - {host}:{port}. Max connections: {max_connections}")
            self.red_cluster = StrictRedisCluster(host=host, port=port, max_connections=max_connections)
        except RedisClusterException as exp:
            logger.error(f"Unable to connect to Redis cluster, falling back to Redis standalone connection: {exp}")
            self.red_cluster = StrictRedis(host=standalone_host, port=standalone_port)

        self.record_exp = record_exp
        super(RedisClusterTrackerStore, self).__init__(domain, event_broker)

    async def save(self, tracker, timeout=None):
        with opentracing.tracer.start_active_span('redis_save'):
            if self.event_broker:
                await self.stream_events(tracker)

            timeout = self.get_channel_timeout(tracker.get_latest_input_channel())

            if not timeout and self.record_exp:
                timeout = self.record_exp

            serialised_tracker = self.serialise_tracker(tracker)
            async with await self.red_cluster.pipeline() as pipe:
                await pipe.set(tracker.sender_id, serialised_tracker, ex=timeout * 2)
                await pipe.set(f'sid_{tracker.sender_id}', '', ex=timeout)
                await pipe.execute()

    async def retrieve(self, sender_id):
        with opentracing.tracer.start_active_span('redis_retrieve'):
            stored = await self.red_cluster.get(sender_id)

            if stored is not None:
                return self.deserialise_tracker(sender_id, stored)
            else:
                return None

    async def delete(self, sender_id):
        await self.red_cluster.delete(sender_id)

    async def ping(self):
        return await self.red_cluster.ping()

    async def test_conn(self):
        return await self.red_cluster.setex("ping", 5, "")


class MongoTrackerStore(TrackerStore):
    def __init__(
        self,
        domain,
        host="mongodb://localhost:27017",
        db="rasa",
        username=None,
        password=None,
        auth_source="admin",
        collection="conversations",
        event_broker=None,
    ):
        from pymongo.database import Database
        from pymongo import MongoClient

        self.client = MongoClient(
            host,
            username=username,
            password=password,
            authSource=auth_source,
            # delay connect until process forking is done
            connect=False,
        )

        self.db = Database(self.client, db)
        self.collection = collection
        super(MongoTrackerStore, self).__init__(domain, event_broker)

        self._ensure_indices()

    @property
    def conversations(self):
        return self.db[self.collection]

    def _ensure_indices(self):
        self.conversations.create_index("sender_id")

    async def save(self, tracker, timeout=None):
        if self.event_broker:
            await self.stream_events(tracker)

        state = tracker.current_state(EventVerbosity.ALL)

        self.conversations.update_one(
            {"sender_id": tracker.sender_id}, {"$set": state}, upsert=True
        )

    async def retrieve(self, sender_id):
        stored = self.conversations.find_one({"sender_id": sender_id})

        # look for conversations which have used an `int` sender_id in the past
        # and update them.
        if stored is None and sender_id.isdigit():
            from pymongo import ReturnDocument

            stored = self.conversations.find_one_and_update(
                {"sender_id": int(sender_id)},
                {"$set": {"sender_id": str(sender_id)}},
                return_document=ReturnDocument.AFTER,
            )

        if stored is not None:
            if self.domain:
                return DialogueStateTracker.from_dict(
                    sender_id, stored.get("events"), self.domain.slots
                )
            else:
                logger.warning(
                    "Can't recreate tracker from mongo storage "
                    "because no domain is set. Returning `None` "
                    "instead."
                )
                return None
        else:
            return None

    async def keys(self) -> Iterable[Text]:
        return [c["sender_id"] for c in self.conversations.find()]


class SQLTrackerStore(TrackerStore):
    """Store which can save and retrieve trackers from an SQL database."""

    from sqlalchemy.ext.declarative import declarative_base

    Base = declarative_base()

    class SQLEvent(Base):
        from sqlalchemy import Column, Integer, String, Float, Text

        __tablename__ = "events"

        id = Column(Integer, primary_key=True)
        sender_id = Column(String(255), nullable=False, index=True)
        type_name = Column(String(255), nullable=False)
        timestamp = Column(Float)
        intent_name = Column(String(255))
        action_name = Column(String(255))
        data = Column(Text)

    def __init__(
        self,
        domain: Optional[Domain] = None,
        dialect: Text = "sqlite",
        host: Optional[Text] = None,
        port: Optional[int] = None,
        db: Text = "rasa.db",
        username: Text = None,
        password: Text = None,
        event_broker: Optional[EventChannel] = None,
        login_db: Optional[Text] = None,
    ) -> None:
        import sqlalchemy
        from sqlalchemy.orm import sessionmaker
        from sqlalchemy import create_engine

        engine_url = self._get_db_url(
            dialect, host, port, db, username, password, login_db
        )
        logger.debug(
            "Attempting to connect to database " 'via "{}"'.format(repr(engine_url))
        )

        # Database might take a while to come up
        while True:
            try:
                self.engine = create_engine(engine_url)

                # if `login_db` has been provided, use current connection with
                # that database to create working database `db`
                if login_db:
                    self._create_database_and_update_engine(db, engine_url)

                try:
                    self.Base.metadata.create_all(self.engine)
                except (
                    sqlalchemy.exc.OperationalError,
                    sqlalchemy.exc.ProgrammingError,
                ) as e:
                    # Several Rasa services started in parallel may attempt to
                    # create tables at the same time. That is okay so long as
                    # the first services finishes the table creation.
                    logger.error("Could not create tables: {}".format(e))

                self.session = sessionmaker(bind=self.engine)()
                break
            except (
                sqlalchemy.exc.OperationalError,
                sqlalchemy.exc.IntegrityError,
            ) as e:

                logger.warning(e)
                sleep(5)

        logger.debug("Connection to SQL database '{}' successful".format(db))

        super(SQLTrackerStore, self).__init__(domain, event_broker)

    @staticmethod
    def _get_db_url(
        dialect: Text = "sqlite",
        host: Optional[Text] = None,
        port: Optional[int] = None,
        db: Text = "rasa.db",
        username: Text = None,
        password: Text = None,
        login_db: Optional[Text] = None,
    ) -> Union[Text, "URL"]:
        from urllib.parse import urlsplit
        from sqlalchemy.engine.url import URL

        # Users might specify a url in the host
        parsed = urlsplit(host or "")
        if parsed.scheme:
            return host

        if host:
            # add fake scheme to properly parse components
            parsed = urlsplit("schema://" + host)

            # users might include the port in the url
            port = parsed.port or port
            host = parsed.hostname or host

        return URL(
            dialect,
            username,
            password,
            host,
            port,
            database=login_db if login_db else db,
        )

    def _create_database_and_update_engine(self, db: Text, engine_url: "URL"):
        """Create databse `db` and update engine to reflect the updated
            `engine_url`."""

        from sqlalchemy import create_engine

        self._create_database(self.engine, db)
        engine_url.database = db
        self.engine = create_engine(engine_url)

    @staticmethod
    def _create_database(engine: "Engine", db: Text):
        """Create database `db` on `engine` if it does not exist."""

        import psycopg2

        conn = engine.connect()

        cursor = conn.connection.cursor()
        cursor.execute("COMMIT")
        cursor.execute(
            ("SELECT 1 FROM pg_catalog.pg_database WHERE datname = '{}'".format(db))
        )
        exists = cursor.fetchone()
        if not exists:
            try:
                cursor.execute("CREATE DATABASE {}".format(db))
            except psycopg2.IntegrityError as e:
                logger.error("Could not create database '{}': {}".format(db, e))

        cursor.close()
        conn.close()

    async def keys(self) -> Iterable[Text]:
        sender_ids = self.session.query(self.SQLEvent.sender_id).distinct().all()
        return [sender_id for (sender_id,) in sender_ids]

    async def retrieve(self, sender_id: Text) -> Optional[DialogueStateTracker]:
        """Create a tracker from all previously stored events."""

        query = self.session.query(self.SQLEvent)
        result = query.filter_by(sender_id=sender_id).all()
        events = [json.loads(event.data) for event in result]

        if self.domain and len(events) > 0:
            logger.debug("Recreating tracker from sender id '{}'".format(sender_id))

            return DialogueStateTracker.from_dict(sender_id, events, self.domain.slots)
        else:
            logger.debug(
                "Can't retrieve tracker matching"
                "sender id '{}' from SQL storage.  "
                "Returning `None` instead.".format(sender_id)
            )
            return None

    async def save(self, tracker: DialogueStateTracker) -> None:
        """Update database with events from the current conversation."""

        if self.event_broker:
            await self.stream_events(tracker)

        events = self._additional_events(tracker)  # only store recent events

        for event in events:
            data = event.as_dict()

            intent = data.get("parse_data", {}).get("intent", {}).get("name")
            action = data.get("name")
            timestamp = data.get("timestamp")

            # noinspection PyArgumentList
            self.session.add(
                self.SQLEvent(
                    sender_id=tracker.sender_id,
                    type_name=event.type_name,
                    timestamp=timestamp,
                    intent_name=intent,
                    action_name=action,
                    data=json.dumps(data),
                )
            )
        self.session.commit()

        logger.debug(
            "Tracker with sender_id '{}' "
            "stored to database".format(tracker.sender_id)
        )

    def number_of_existing_events(self, sender_id: Text) -> int:
        """Return number of stored events for a given sender id."""

        query = self.session.query(self.SQLEvent.sender_id)
        return query.filter_by(sender_id=sender_id).count() or 0

    def _additional_events(self, tracker: DialogueStateTracker) -> Iterator:
        """Return events from the tracker which aren't currently stored."""
        n_events = self.number_of_existing_events(tracker.sender_id)
        return itertools.islice(tracker.events, n_events, len(tracker.events))
