"""
Main interface for kinesis-video-archived-media service type definitions.

Usage::

    from mypy_boto3.kinesis_video_archived_media.type_defs import ClientGetDashStreamingSessionUrlDASHFragmentSelectorTimestampRangeTypeDef

    data: ClientGetDashStreamingSessionUrlDASHFragmentSelectorTimestampRangeTypeDef = {...}
"""
from datetime import datetime
import sys
from typing import List
from botocore.response import StreamingBody

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ClientGetDashStreamingSessionUrlDASHFragmentSelectorTimestampRangeTypeDef",
    "ClientGetDashStreamingSessionUrlDASHFragmentSelectorTypeDef",
    "ClientGetDashStreamingSessionUrlResponseTypeDef",
    "ClientGetHlsStreamingSessionUrlHLSFragmentSelectorTimestampRangeTypeDef",
    "ClientGetHlsStreamingSessionUrlHLSFragmentSelectorTypeDef",
    "ClientGetHlsStreamingSessionUrlResponseTypeDef",
    "ClientGetMediaForFragmentListResponseTypeDef",
    "ClientListFragmentsFragmentSelectorTimestampRangeTypeDef",
    "ClientListFragmentsFragmentSelectorTypeDef",
    "ClientListFragmentsResponseFragmentsTypeDef",
    "ClientListFragmentsResponseTypeDef",
    "TimestampRangeTypeDef",
    "FragmentSelectorTypeDef",
    "FragmentTypeDef",
    "ListFragmentsOutputTypeDef",
    "PaginatorConfigTypeDef",
)

ClientGetDashStreamingSessionUrlDASHFragmentSelectorTimestampRangeTypeDef = TypedDict(
    "ClientGetDashStreamingSessionUrlDASHFragmentSelectorTimestampRangeTypeDef",
    {"StartTimestamp": datetime, "EndTimestamp": datetime},
    total=False,
)

ClientGetDashStreamingSessionUrlDASHFragmentSelectorTypeDef = TypedDict(
    "ClientGetDashStreamingSessionUrlDASHFragmentSelectorTypeDef",
    {
        "FragmentSelectorType": Literal["PRODUCER_TIMESTAMP", "SERVER_TIMESTAMP"],
        "TimestampRange": ClientGetDashStreamingSessionUrlDASHFragmentSelectorTimestampRangeTypeDef,
    },
    total=False,
)

ClientGetDashStreamingSessionUrlResponseTypeDef = TypedDict(
    "ClientGetDashStreamingSessionUrlResponseTypeDef", {"DASHStreamingSessionURL": str}, total=False
)

ClientGetHlsStreamingSessionUrlHLSFragmentSelectorTimestampRangeTypeDef = TypedDict(
    "ClientGetHlsStreamingSessionUrlHLSFragmentSelectorTimestampRangeTypeDef",
    {"StartTimestamp": datetime, "EndTimestamp": datetime},
    total=False,
)

ClientGetHlsStreamingSessionUrlHLSFragmentSelectorTypeDef = TypedDict(
    "ClientGetHlsStreamingSessionUrlHLSFragmentSelectorTypeDef",
    {
        "FragmentSelectorType": Literal["PRODUCER_TIMESTAMP", "SERVER_TIMESTAMP"],
        "TimestampRange": ClientGetHlsStreamingSessionUrlHLSFragmentSelectorTimestampRangeTypeDef,
    },
    total=False,
)

ClientGetHlsStreamingSessionUrlResponseTypeDef = TypedDict(
    "ClientGetHlsStreamingSessionUrlResponseTypeDef", {"HLSStreamingSessionURL": str}, total=False
)

ClientGetMediaForFragmentListResponseTypeDef = TypedDict(
    "ClientGetMediaForFragmentListResponseTypeDef",
    {"ContentType": str, "Payload": StreamingBody},
    total=False,
)

ClientListFragmentsFragmentSelectorTimestampRangeTypeDef = TypedDict(
    "ClientListFragmentsFragmentSelectorTimestampRangeTypeDef",
    {"StartTimestamp": datetime, "EndTimestamp": datetime},
    total=False,
)

_RequiredClientListFragmentsFragmentSelectorTypeDef = TypedDict(
    "_RequiredClientListFragmentsFragmentSelectorTypeDef",
    {"FragmentSelectorType": Literal["PRODUCER_TIMESTAMP", "SERVER_TIMESTAMP"]},
)
_OptionalClientListFragmentsFragmentSelectorTypeDef = TypedDict(
    "_OptionalClientListFragmentsFragmentSelectorTypeDef",
    {"TimestampRange": ClientListFragmentsFragmentSelectorTimestampRangeTypeDef},
    total=False,
)


class ClientListFragmentsFragmentSelectorTypeDef(
    _RequiredClientListFragmentsFragmentSelectorTypeDef,
    _OptionalClientListFragmentsFragmentSelectorTypeDef,
):
    pass


ClientListFragmentsResponseFragmentsTypeDef = TypedDict(
    "ClientListFragmentsResponseFragmentsTypeDef",
    {
        "FragmentNumber": str,
        "FragmentSizeInBytes": int,
        "ProducerTimestamp": datetime,
        "ServerTimestamp": datetime,
        "FragmentLengthInMilliseconds": int,
    },
    total=False,
)

ClientListFragmentsResponseTypeDef = TypedDict(
    "ClientListFragmentsResponseTypeDef",
    {"Fragments": List[ClientListFragmentsResponseFragmentsTypeDef], "NextToken": str},
    total=False,
)

TimestampRangeTypeDef = TypedDict(
    "TimestampRangeTypeDef", {"StartTimestamp": datetime, "EndTimestamp": datetime}
)

FragmentSelectorTypeDef = TypedDict(
    "FragmentSelectorTypeDef",
    {
        "FragmentSelectorType": Literal["PRODUCER_TIMESTAMP", "SERVER_TIMESTAMP"],
        "TimestampRange": TimestampRangeTypeDef,
    },
)

FragmentTypeDef = TypedDict(
    "FragmentTypeDef",
    {
        "FragmentNumber": str,
        "FragmentSizeInBytes": int,
        "ProducerTimestamp": datetime,
        "ServerTimestamp": datetime,
        "FragmentLengthInMilliseconds": int,
    },
    total=False,
)

ListFragmentsOutputTypeDef = TypedDict(
    "ListFragmentsOutputTypeDef",
    {"Fragments": List[FragmentTypeDef], "NextToken": str},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)
