import logging
from .event import PubSubError, Event
from .util import SessionExchange

log = logging.getLogger("beercraft")
log_msg = logging.getLogger("beercraft.messages")


class HubSingleton(type):
    _hub = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._hub:
            cls._hub[cls] = super(HubSingleton, cls).__call__(*args, **kwargs)

        return cls._hub[cls]


class Hub(metaclass=HubSingleton):
    def __init__(self):
        self._events = {}
        self._missing_topics = {}
        self.oid = SessionExchange()

    def add_topic(self, topic):
        """ A topic can only be added once and only
        has the one Event object mapped to it.
        """
        if not isinstance(topic, str):
            msg = "Topic argument must be a string! (Given: {0})"
            raise PubSubError(msg.format(topic))

        if not self.has(topic):
            self._events[topic] = Event(topic)

    def subscribe(self, subscriber, topic):

        if not callable(subscriber):
            msg = 'Subscriber ({0}) to topic "{1}" must be a callable.'
            raise PubSubError(msg.format(subscriber, topic))

        self.add_topic(topic)
        log.debug("subscribe {0} to {1}".format(subscriber, topic))
        self._events[topic] += subscriber

    def send_message(self, topic, **kwargs):
        if self.has(topic):
            try:
                log_msg.debug("calling {0} with {1}".format(topic, kwargs.keys()))
                event = self._events[topic]
                log.debug(event)
                event(**kwargs)
            except Exception as ex:  # pylint: disable=broad-except
                raise ex
        else:
            log.debug("{0} has no subscribers.".format(topic))
            self._missing_topics.setdefault(topic, 0)
            self._missing_topics[topic] += 1

    def mk_msg_func(self, topic, **kwargs):
        def _call():
            self.send_message(topic, **kwargs)

        return _call

    def has(self, topic):
        return topic in self._events

    def clear_all(self):
        self._events.clear()
        self._missing_topics.clear()
        self.oid.clear_all()

    def topic_list(self):
        return list(self._events.keys())

    def missing_topic_list(self):
        return list(self._missing_topics.keys())
