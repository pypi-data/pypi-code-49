"""
Main interface for connectparticipant service type definitions.

Usage::

    from mypy_boto3.connectparticipant.type_defs import ClientCreateParticipantConnectionResponseConnectionCredentialsTypeDef

    data: ClientCreateParticipantConnectionResponseConnectionCredentialsTypeDef = {...}
"""
import sys
from typing import List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ClientCreateParticipantConnectionResponseConnectionCredentialsTypeDef",
    "ClientCreateParticipantConnectionResponseWebsocketTypeDef",
    "ClientCreateParticipantConnectionResponseTypeDef",
    "ClientGetTranscriptResponseTranscriptTypeDef",
    "ClientGetTranscriptResponseTypeDef",
    "ClientGetTranscriptStartPositionTypeDef",
    "ClientSendEventResponseTypeDef",
    "ClientSendMessageResponseTypeDef",
)

ClientCreateParticipantConnectionResponseConnectionCredentialsTypeDef = TypedDict(
    "ClientCreateParticipantConnectionResponseConnectionCredentialsTypeDef",
    {"ConnectionToken": str, "Expiry": str},
    total=False,
)

ClientCreateParticipantConnectionResponseWebsocketTypeDef = TypedDict(
    "ClientCreateParticipantConnectionResponseWebsocketTypeDef",
    {"Url": str, "ConnectionExpiry": str},
    total=False,
)

ClientCreateParticipantConnectionResponseTypeDef = TypedDict(
    "ClientCreateParticipantConnectionResponseTypeDef",
    {
        "Websocket": ClientCreateParticipantConnectionResponseWebsocketTypeDef,
        "ConnectionCredentials": ClientCreateParticipantConnectionResponseConnectionCredentialsTypeDef,
    },
    total=False,
)

ClientGetTranscriptResponseTranscriptTypeDef = TypedDict(
    "ClientGetTranscriptResponseTranscriptTypeDef",
    {
        "AbsoluteTime": str,
        "Content": str,
        "ContentType": str,
        "Id": str,
        "Type": Literal["MESSAGE", "EVENT", "CONNECTION_ACK"],
        "ParticipantId": str,
        "DisplayName": str,
        "ParticipantRole": Literal["AGENT", "CUSTOMER", "SYSTEM"],
    },
    total=False,
)

ClientGetTranscriptResponseTypeDef = TypedDict(
    "ClientGetTranscriptResponseTypeDef",
    {
        "InitialContactId": str,
        "Transcript": List[ClientGetTranscriptResponseTranscriptTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientGetTranscriptStartPositionTypeDef = TypedDict(
    "ClientGetTranscriptStartPositionTypeDef",
    {"Id": str, "AbsoluteTime": str, "MostRecent": int},
    total=False,
)

ClientSendEventResponseTypeDef = TypedDict(
    "ClientSendEventResponseTypeDef", {"Id": str, "AbsoluteTime": str}, total=False
)

ClientSendMessageResponseTypeDef = TypedDict(
    "ClientSendMessageResponseTypeDef", {"Id": str, "AbsoluteTime": str}, total=False
)
