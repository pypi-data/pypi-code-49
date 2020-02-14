import itertools
import logging
from typing import Text, Optional, List, Dict, Any

from rasa.core.actions.action import ACTION_LISTEN_NAME, ACTION_SESSION_START_NAME
from rasa.core.events import SessionStarted, ActionExecuted

logger = logging.getLogger(__name__)


def is_action_listen(event: Dict[Text, Any]) -> bool:
    """Determine whether the serialised `event` is an `action_listen`."""

    return event.get("name") == ACTION_LISTEN_NAME


def is_action_session_start(event: Dict[Text, Any]) -> bool:
    """Determine whether the serialised `event` is an `action_session_start`."""

    return event.get("name") == ACTION_SESSION_START_NAME


def remove_leading_action_session_start_from(tracker: Dict[Text, Any]) -> None:
    """Remove a leading `ACTION_SESSION_START` if present in `tracker`."""

    if tracker["events"] and is_action_session_start(tracker["events"][0]):
        tracker["events"] = tracker["events"][1:]


def index_of_session_start_sequence_end(events: List[Dict[Text, Any]]) -> Optional[int]:
    """Determine the index of the end of the session start sequence in `events`.

    A session start sequence is a sequence of

        [`action_session_start`, `session_started`, ..., `action_listen`],

    where '...' can be any list of events excluding `action_listen` events.

    Args:
        events: Serialised events to inspect.

    Returns:
        The index of the first `ACTION_LISTEN` after a session start sequence if
        present, `None` otherwise.
    """

    # there must be at least three events if `events` begins with a session start
    # sequence
    if len(events) < 3:
        return None

    # for this to be a session start, the first two events must be
    # `action_session_start` and `session_started`
    if not (
        events[0].get("name") == ACTION_SESSION_START_NAME
        and events[1].get("event") == SessionStarted.type_name
    ):
        return None

    # now there may be any number of events, but the session start sequence will end
    # with the first `ACTION_LISTEN`
    # start the enumeration at 2 as the first two events are
    # `action_session_start` and `session_started`
    return next(
        (i for i, event in enumerate(events[2:], 2) if is_action_listen(event)), None
    )


def remove_events_until_timestamp(
    events: List[Dict[Text, Any]], timestamp: float
) -> List[Dict[Text, Any]]:
    """Remove events with timestamps up to and including `timestamp`.

    Assumes `events` are sorted by timestamp.

    Args:
        events: List of events to inspect.
        timestamp: Maximum timestamp.

    Returns:
        Events with a timestamp greater than `timestamp`. An empty list if
        no events have a timestamp below and including `timestamp`.
    """

    return list(itertools.dropwhile(lambda x: x["timestamp"] <= timestamp, events))


def timestamp_of_session_start(events: List[Dict]) -> Optional[float]:
    """Return timestamp of first `ACTION_LISTEN` event if the tracker
    contains a session start sequence and only one `ACTION_LISTEN`."""

    end_of_session_start = index_of_session_start_sequence_end(events)

    if end_of_session_start is not None:
        return events[end_of_session_start]["timestamp"]

    return None


def timestamp_of_first_action_listen(events: List[Dict]) -> float:
    """Return timestamp of first tracker event if the tracker contains only one
    event that is an ACTION_LISTEN event, 0 otherwise."""

    if events and len(events) == 1:
        event = events[0]
        if (
            event["event"] == ActionExecuted.type_name
            and event["name"] == ACTION_LISTEN_NAME
        ):
            return event["timestamp"]

    return 0


def timestamp_of_conversation_start(events: List[Dict]) -> float:
    """Get the timestamp of the conversation start.

    A conversation start can either be defined by a single `ACTION_LISTEN` or by a
    session start sequence.

    A session start sequence is a sequence of

        [`action_session_start`, `session_started`, ..., `action_listen`],

    where '...' can be any list of events excluding `action_listen` events.


    Args:
        events: List of events to inspect.

    Returns:
        The timestamp of the conversation start.
    """

    session_start_timestamp = timestamp_of_session_start(events)

    if session_start_timestamp is not None:
        return session_start_timestamp

    return timestamp_of_first_action_listen(events)
