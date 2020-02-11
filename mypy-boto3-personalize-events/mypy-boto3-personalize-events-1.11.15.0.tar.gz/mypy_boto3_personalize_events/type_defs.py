"""
Main interface for personalize-events service type definitions.

Usage::

    from mypy_boto3.personalize_events.type_defs import ClientPutEventsEventListTypeDef

    data: ClientPutEventsEventListTypeDef = {...}
"""
from datetime import datetime
import sys

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = ("ClientPutEventsEventListTypeDef",)

ClientPutEventsEventListTypeDef = TypedDict(
    "ClientPutEventsEventListTypeDef",
    {"eventId": str, "eventType": str, "properties": str, "sentAt": datetime},
    total=False,
)
