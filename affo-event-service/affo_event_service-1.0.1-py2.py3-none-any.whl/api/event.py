import datetime

from affo_event_service.extensions import clickhouse
from affo_event_service.models.event import Event


def create(event):
    event_obj = Event(event_time=datetime.datetime.utcnow(), **event)
    clickhouse.insert([event_obj])

    return {}
