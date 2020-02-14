"""
Main interface for mediatailor service type definitions.

Usage::

    from mypy_boto3.mediatailor.type_defs import ClientGetPlaybackConfigurationResponseCdnConfigurationTypeDef

    data: ClientGetPlaybackConfigurationResponseCdnConfigurationTypeDef = {...}
"""
import sys
from typing import Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ClientGetPlaybackConfigurationResponseCdnConfigurationTypeDef",
    "ClientGetPlaybackConfigurationResponseDashConfigurationTypeDef",
    "ClientGetPlaybackConfigurationResponseHlsConfigurationTypeDef",
    "ClientGetPlaybackConfigurationResponseLivePreRollConfigurationTypeDef",
    "ClientGetPlaybackConfigurationResponseTypeDef",
    "ClientListPlaybackConfigurationsResponseItemsCdnConfigurationTypeDef",
    "ClientListPlaybackConfigurationsResponseItemsDashConfigurationTypeDef",
    "ClientListPlaybackConfigurationsResponseItemsHlsConfigurationTypeDef",
    "ClientListPlaybackConfigurationsResponseItemsTypeDef",
    "ClientListPlaybackConfigurationsResponseTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientPutPlaybackConfigurationCdnConfigurationTypeDef",
    "ClientPutPlaybackConfigurationDashConfigurationTypeDef",
    "ClientPutPlaybackConfigurationLivePreRollConfigurationTypeDef",
    "ClientPutPlaybackConfigurationResponseCdnConfigurationTypeDef",
    "ClientPutPlaybackConfigurationResponseDashConfigurationTypeDef",
    "ClientPutPlaybackConfigurationResponseHlsConfigurationTypeDef",
    "ClientPutPlaybackConfigurationResponseLivePreRollConfigurationTypeDef",
    "ClientPutPlaybackConfigurationResponseTypeDef",
    "CdnConfigurationTypeDef",
    "DashConfigurationTypeDef",
    "HlsConfigurationTypeDef",
    "PlaybackConfigurationTypeDef",
    "ListPlaybackConfigurationsResponseTypeDef",
    "PaginatorConfigTypeDef",
)

ClientGetPlaybackConfigurationResponseCdnConfigurationTypeDef = TypedDict(
    "ClientGetPlaybackConfigurationResponseCdnConfigurationTypeDef",
    {"AdSegmentUrlPrefix": str, "ContentSegmentUrlPrefix": str},
    total=False,
)

ClientGetPlaybackConfigurationResponseDashConfigurationTypeDef = TypedDict(
    "ClientGetPlaybackConfigurationResponseDashConfigurationTypeDef",
    {
        "ManifestEndpointPrefix": str,
        "MpdLocation": str,
        "OriginManifestType": Literal["SINGLE_PERIOD", "MULTI_PERIOD"],
    },
    total=False,
)

ClientGetPlaybackConfigurationResponseHlsConfigurationTypeDef = TypedDict(
    "ClientGetPlaybackConfigurationResponseHlsConfigurationTypeDef",
    {"ManifestEndpointPrefix": str},
    total=False,
)

ClientGetPlaybackConfigurationResponseLivePreRollConfigurationTypeDef = TypedDict(
    "ClientGetPlaybackConfigurationResponseLivePreRollConfigurationTypeDef",
    {"AdDecisionServerUrl": str, "MaxDurationSeconds": int},
    total=False,
)

ClientGetPlaybackConfigurationResponseTypeDef = TypedDict(
    "ClientGetPlaybackConfigurationResponseTypeDef",
    {
        "AdDecisionServerUrl": str,
        "CdnConfiguration": ClientGetPlaybackConfigurationResponseCdnConfigurationTypeDef,
        "DashConfiguration": ClientGetPlaybackConfigurationResponseDashConfigurationTypeDef,
        "HlsConfiguration": ClientGetPlaybackConfigurationResponseHlsConfigurationTypeDef,
        "LivePreRollConfiguration": ClientGetPlaybackConfigurationResponseLivePreRollConfigurationTypeDef,
        "Name": str,
        "PlaybackConfigurationArn": str,
        "PlaybackEndpointPrefix": str,
        "SessionInitializationEndpointPrefix": str,
        "SlateAdUrl": str,
        "Tags": Dict[str, str],
        "TranscodeProfileName": str,
        "VideoContentSourceUrl": str,
    },
    total=False,
)

ClientListPlaybackConfigurationsResponseItemsCdnConfigurationTypeDef = TypedDict(
    "ClientListPlaybackConfigurationsResponseItemsCdnConfigurationTypeDef",
    {"AdSegmentUrlPrefix": str, "ContentSegmentUrlPrefix": str},
    total=False,
)

ClientListPlaybackConfigurationsResponseItemsDashConfigurationTypeDef = TypedDict(
    "ClientListPlaybackConfigurationsResponseItemsDashConfigurationTypeDef",
    {
        "ManifestEndpointPrefix": str,
        "MpdLocation": str,
        "OriginManifestType": Literal["SINGLE_PERIOD", "MULTI_PERIOD"],
    },
    total=False,
)

ClientListPlaybackConfigurationsResponseItemsHlsConfigurationTypeDef = TypedDict(
    "ClientListPlaybackConfigurationsResponseItemsHlsConfigurationTypeDef",
    {"ManifestEndpointPrefix": str},
    total=False,
)

ClientListPlaybackConfigurationsResponseItemsTypeDef = TypedDict(
    "ClientListPlaybackConfigurationsResponseItemsTypeDef",
    {
        "AdDecisionServerUrl": str,
        "CdnConfiguration": ClientListPlaybackConfigurationsResponseItemsCdnConfigurationTypeDef,
        "DashConfiguration": ClientListPlaybackConfigurationsResponseItemsDashConfigurationTypeDef,
        "HlsConfiguration": ClientListPlaybackConfigurationsResponseItemsHlsConfigurationTypeDef,
        "Name": str,
        "PlaybackConfigurationArn": str,
        "PlaybackEndpointPrefix": str,
        "SessionInitializationEndpointPrefix": str,
        "SlateAdUrl": str,
        "Tags": Dict[str, str],
        "TranscodeProfileName": str,
        "VideoContentSourceUrl": str,
    },
    total=False,
)

ClientListPlaybackConfigurationsResponseTypeDef = TypedDict(
    "ClientListPlaybackConfigurationsResponseTypeDef",
    {"Items": List[ClientListPlaybackConfigurationsResponseItemsTypeDef], "NextToken": str},
    total=False,
)

ClientListTagsForResourceResponseTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTypeDef", {"Tags": Dict[str, str]}, total=False
)

ClientPutPlaybackConfigurationCdnConfigurationTypeDef = TypedDict(
    "ClientPutPlaybackConfigurationCdnConfigurationTypeDef",
    {"AdSegmentUrlPrefix": str, "ContentSegmentUrlPrefix": str},
    total=False,
)

ClientPutPlaybackConfigurationDashConfigurationTypeDef = TypedDict(
    "ClientPutPlaybackConfigurationDashConfigurationTypeDef",
    {"MpdLocation": str, "OriginManifestType": Literal["SINGLE_PERIOD", "MULTI_PERIOD"]},
    total=False,
)

ClientPutPlaybackConfigurationLivePreRollConfigurationTypeDef = TypedDict(
    "ClientPutPlaybackConfigurationLivePreRollConfigurationTypeDef",
    {"AdDecisionServerUrl": str, "MaxDurationSeconds": int},
    total=False,
)

ClientPutPlaybackConfigurationResponseCdnConfigurationTypeDef = TypedDict(
    "ClientPutPlaybackConfigurationResponseCdnConfigurationTypeDef",
    {"AdSegmentUrlPrefix": str, "ContentSegmentUrlPrefix": str},
    total=False,
)

ClientPutPlaybackConfigurationResponseDashConfigurationTypeDef = TypedDict(
    "ClientPutPlaybackConfigurationResponseDashConfigurationTypeDef",
    {
        "ManifestEndpointPrefix": str,
        "MpdLocation": str,
        "OriginManifestType": Literal["SINGLE_PERIOD", "MULTI_PERIOD"],
    },
    total=False,
)

ClientPutPlaybackConfigurationResponseHlsConfigurationTypeDef = TypedDict(
    "ClientPutPlaybackConfigurationResponseHlsConfigurationTypeDef",
    {"ManifestEndpointPrefix": str},
    total=False,
)

ClientPutPlaybackConfigurationResponseLivePreRollConfigurationTypeDef = TypedDict(
    "ClientPutPlaybackConfigurationResponseLivePreRollConfigurationTypeDef",
    {"AdDecisionServerUrl": str, "MaxDurationSeconds": int},
    total=False,
)

ClientPutPlaybackConfigurationResponseTypeDef = TypedDict(
    "ClientPutPlaybackConfigurationResponseTypeDef",
    {
        "AdDecisionServerUrl": str,
        "CdnConfiguration": ClientPutPlaybackConfigurationResponseCdnConfigurationTypeDef,
        "DashConfiguration": ClientPutPlaybackConfigurationResponseDashConfigurationTypeDef,
        "HlsConfiguration": ClientPutPlaybackConfigurationResponseHlsConfigurationTypeDef,
        "LivePreRollConfiguration": ClientPutPlaybackConfigurationResponseLivePreRollConfigurationTypeDef,
        "Name": str,
        "PlaybackConfigurationArn": str,
        "PlaybackEndpointPrefix": str,
        "SessionInitializationEndpointPrefix": str,
        "SlateAdUrl": str,
        "Tags": Dict[str, str],
        "TranscodeProfileName": str,
        "VideoContentSourceUrl": str,
    },
    total=False,
)

CdnConfigurationTypeDef = TypedDict(
    "CdnConfigurationTypeDef",
    {"AdSegmentUrlPrefix": str, "ContentSegmentUrlPrefix": str},
    total=False,
)

DashConfigurationTypeDef = TypedDict(
    "DashConfigurationTypeDef",
    {
        "ManifestEndpointPrefix": str,
        "MpdLocation": str,
        "OriginManifestType": Literal["SINGLE_PERIOD", "MULTI_PERIOD"],
    },
    total=False,
)

HlsConfigurationTypeDef = TypedDict(
    "HlsConfigurationTypeDef", {"ManifestEndpointPrefix": str}, total=False
)

PlaybackConfigurationTypeDef = TypedDict(
    "PlaybackConfigurationTypeDef",
    {
        "AdDecisionServerUrl": str,
        "CdnConfiguration": CdnConfigurationTypeDef,
        "DashConfiguration": DashConfigurationTypeDef,
        "HlsConfiguration": HlsConfigurationTypeDef,
        "Name": str,
        "PlaybackConfigurationArn": str,
        "PlaybackEndpointPrefix": str,
        "SessionInitializationEndpointPrefix": str,
        "SlateAdUrl": str,
        "Tags": Dict[str, str],
        "TranscodeProfileName": str,
        "VideoContentSourceUrl": str,
    },
    total=False,
)

ListPlaybackConfigurationsResponseTypeDef = TypedDict(
    "ListPlaybackConfigurationsResponseTypeDef",
    {"Items": List[PlaybackConfigurationTypeDef], "NextToken": str},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)
