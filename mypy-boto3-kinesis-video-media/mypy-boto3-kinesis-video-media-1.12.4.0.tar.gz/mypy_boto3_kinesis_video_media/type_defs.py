"""
Main interface for kinesis-video-media service type definitions.

Usage::

    from mypy_boto3.kinesis_video_media.type_defs import ClientGetMediaResponseTypeDef

    data: ClientGetMediaResponseTypeDef = {...}
"""
from datetime import datetime
import sys
from botocore.response import StreamingBody

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = ("ClientGetMediaResponseTypeDef", "ClientGetMediaStartSelectorTypeDef")

ClientGetMediaResponseTypeDef = TypedDict(
    "ClientGetMediaResponseTypeDef", {"ContentType": str, "Payload": StreamingBody}, total=False
)

_RequiredClientGetMediaStartSelectorTypeDef = TypedDict(
    "_RequiredClientGetMediaStartSelectorTypeDef",
    {
        "StartSelectorType": Literal[
            "FRAGMENT_NUMBER",
            "SERVER_TIMESTAMP",
            "PRODUCER_TIMESTAMP",
            "NOW",
            "EARLIEST",
            "CONTINUATION_TOKEN",
        ]
    },
)
_OptionalClientGetMediaStartSelectorTypeDef = TypedDict(
    "_OptionalClientGetMediaStartSelectorTypeDef",
    {"AfterFragmentNumber": str, "StartTimestamp": datetime, "ContinuationToken": str},
    total=False,
)


class ClientGetMediaStartSelectorTypeDef(
    _RequiredClientGetMediaStartSelectorTypeDef, _OptionalClientGetMediaStartSelectorTypeDef
):
    pass
