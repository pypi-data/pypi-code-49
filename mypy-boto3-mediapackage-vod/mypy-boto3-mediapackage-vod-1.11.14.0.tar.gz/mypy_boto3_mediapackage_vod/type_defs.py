"""
Main interface for mediapackage-vod service type definitions.

Usage::

    from mypy_boto3.mediapackage_vod.type_defs import ClientCreateAssetResponseEgressEndpointsTypeDef

    data: ClientCreateAssetResponseEgressEndpointsTypeDef = {...}
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
    "ClientCreateAssetResponseEgressEndpointsTypeDef",
    "ClientCreateAssetResponseTypeDef",
    "ClientCreatePackagingConfigurationCmafPackageEncryptionSpekeKeyProviderTypeDef",
    "ClientCreatePackagingConfigurationCmafPackageEncryptionTypeDef",
    "ClientCreatePackagingConfigurationCmafPackageHlsManifestsStreamSelectionTypeDef",
    "ClientCreatePackagingConfigurationCmafPackageHlsManifestsTypeDef",
    "ClientCreatePackagingConfigurationCmafPackageTypeDef",
    "ClientCreatePackagingConfigurationDashPackageDashManifestsStreamSelectionTypeDef",
    "ClientCreatePackagingConfigurationDashPackageDashManifestsTypeDef",
    "ClientCreatePackagingConfigurationDashPackageEncryptionSpekeKeyProviderTypeDef",
    "ClientCreatePackagingConfigurationDashPackageEncryptionTypeDef",
    "ClientCreatePackagingConfigurationDashPackageTypeDef",
    "ClientCreatePackagingConfigurationHlsPackageEncryptionSpekeKeyProviderTypeDef",
    "ClientCreatePackagingConfigurationHlsPackageEncryptionTypeDef",
    "ClientCreatePackagingConfigurationHlsPackageHlsManifestsStreamSelectionTypeDef",
    "ClientCreatePackagingConfigurationHlsPackageHlsManifestsTypeDef",
    "ClientCreatePackagingConfigurationHlsPackageTypeDef",
    "ClientCreatePackagingConfigurationMssPackageEncryptionSpekeKeyProviderTypeDef",
    "ClientCreatePackagingConfigurationMssPackageEncryptionTypeDef",
    "ClientCreatePackagingConfigurationMssPackageMssManifestsStreamSelectionTypeDef",
    "ClientCreatePackagingConfigurationMssPackageMssManifestsTypeDef",
    "ClientCreatePackagingConfigurationMssPackageTypeDef",
    "ClientCreatePackagingConfigurationResponseCmafPackageEncryptionSpekeKeyProviderTypeDef",
    "ClientCreatePackagingConfigurationResponseCmafPackageEncryptionTypeDef",
    "ClientCreatePackagingConfigurationResponseCmafPackageHlsManifestsStreamSelectionTypeDef",
    "ClientCreatePackagingConfigurationResponseCmafPackageHlsManifestsTypeDef",
    "ClientCreatePackagingConfigurationResponseCmafPackageTypeDef",
    "ClientCreatePackagingConfigurationResponseDashPackageDashManifestsStreamSelectionTypeDef",
    "ClientCreatePackagingConfigurationResponseDashPackageDashManifestsTypeDef",
    "ClientCreatePackagingConfigurationResponseDashPackageEncryptionSpekeKeyProviderTypeDef",
    "ClientCreatePackagingConfigurationResponseDashPackageEncryptionTypeDef",
    "ClientCreatePackagingConfigurationResponseDashPackageTypeDef",
    "ClientCreatePackagingConfigurationResponseHlsPackageEncryptionSpekeKeyProviderTypeDef",
    "ClientCreatePackagingConfigurationResponseHlsPackageEncryptionTypeDef",
    "ClientCreatePackagingConfigurationResponseHlsPackageHlsManifestsStreamSelectionTypeDef",
    "ClientCreatePackagingConfigurationResponseHlsPackageHlsManifestsTypeDef",
    "ClientCreatePackagingConfigurationResponseHlsPackageTypeDef",
    "ClientCreatePackagingConfigurationResponseMssPackageEncryptionSpekeKeyProviderTypeDef",
    "ClientCreatePackagingConfigurationResponseMssPackageEncryptionTypeDef",
    "ClientCreatePackagingConfigurationResponseMssPackageMssManifestsStreamSelectionTypeDef",
    "ClientCreatePackagingConfigurationResponseMssPackageMssManifestsTypeDef",
    "ClientCreatePackagingConfigurationResponseMssPackageTypeDef",
    "ClientCreatePackagingConfigurationResponseTypeDef",
    "ClientCreatePackagingGroupResponseTypeDef",
    "ClientDescribeAssetResponseEgressEndpointsTypeDef",
    "ClientDescribeAssetResponseTypeDef",
    "ClientDescribePackagingConfigurationResponseCmafPackageEncryptionSpekeKeyProviderTypeDef",
    "ClientDescribePackagingConfigurationResponseCmafPackageEncryptionTypeDef",
    "ClientDescribePackagingConfigurationResponseCmafPackageHlsManifestsStreamSelectionTypeDef",
    "ClientDescribePackagingConfigurationResponseCmafPackageHlsManifestsTypeDef",
    "ClientDescribePackagingConfigurationResponseCmafPackageTypeDef",
    "ClientDescribePackagingConfigurationResponseDashPackageDashManifestsStreamSelectionTypeDef",
    "ClientDescribePackagingConfigurationResponseDashPackageDashManifestsTypeDef",
    "ClientDescribePackagingConfigurationResponseDashPackageEncryptionSpekeKeyProviderTypeDef",
    "ClientDescribePackagingConfigurationResponseDashPackageEncryptionTypeDef",
    "ClientDescribePackagingConfigurationResponseDashPackageTypeDef",
    "ClientDescribePackagingConfigurationResponseHlsPackageEncryptionSpekeKeyProviderTypeDef",
    "ClientDescribePackagingConfigurationResponseHlsPackageEncryptionTypeDef",
    "ClientDescribePackagingConfigurationResponseHlsPackageHlsManifestsStreamSelectionTypeDef",
    "ClientDescribePackagingConfigurationResponseHlsPackageHlsManifestsTypeDef",
    "ClientDescribePackagingConfigurationResponseHlsPackageTypeDef",
    "ClientDescribePackagingConfigurationResponseMssPackageEncryptionSpekeKeyProviderTypeDef",
    "ClientDescribePackagingConfigurationResponseMssPackageEncryptionTypeDef",
    "ClientDescribePackagingConfigurationResponseMssPackageMssManifestsStreamSelectionTypeDef",
    "ClientDescribePackagingConfigurationResponseMssPackageMssManifestsTypeDef",
    "ClientDescribePackagingConfigurationResponseMssPackageTypeDef",
    "ClientDescribePackagingConfigurationResponseTypeDef",
    "ClientDescribePackagingGroupResponseTypeDef",
    "ClientListAssetsResponseAssetsTypeDef",
    "ClientListAssetsResponseTypeDef",
    "ClientListPackagingConfigurationsResponsePackagingConfigurationsCmafPackageEncryptionSpekeKeyProviderTypeDef",
    "ClientListPackagingConfigurationsResponsePackagingConfigurationsCmafPackageEncryptionTypeDef",
    "ClientListPackagingConfigurationsResponsePackagingConfigurationsCmafPackageHlsManifestsStreamSelectionTypeDef",
    "ClientListPackagingConfigurationsResponsePackagingConfigurationsCmafPackageHlsManifestsTypeDef",
    "ClientListPackagingConfigurationsResponsePackagingConfigurationsCmafPackageTypeDef",
    "ClientListPackagingConfigurationsResponsePackagingConfigurationsDashPackageDashManifestsStreamSelectionTypeDef",
    "ClientListPackagingConfigurationsResponsePackagingConfigurationsDashPackageDashManifestsTypeDef",
    "ClientListPackagingConfigurationsResponsePackagingConfigurationsDashPackageEncryptionSpekeKeyProviderTypeDef",
    "ClientListPackagingConfigurationsResponsePackagingConfigurationsDashPackageEncryptionTypeDef",
    "ClientListPackagingConfigurationsResponsePackagingConfigurationsDashPackageTypeDef",
    "ClientListPackagingConfigurationsResponsePackagingConfigurationsHlsPackageEncryptionSpekeKeyProviderTypeDef",
    "ClientListPackagingConfigurationsResponsePackagingConfigurationsHlsPackageEncryptionTypeDef",
    "ClientListPackagingConfigurationsResponsePackagingConfigurationsHlsPackageHlsManifestsStreamSelectionTypeDef",
    "ClientListPackagingConfigurationsResponsePackagingConfigurationsHlsPackageHlsManifestsTypeDef",
    "ClientListPackagingConfigurationsResponsePackagingConfigurationsHlsPackageTypeDef",
    "ClientListPackagingConfigurationsResponsePackagingConfigurationsMssPackageEncryptionSpekeKeyProviderTypeDef",
    "ClientListPackagingConfigurationsResponsePackagingConfigurationsMssPackageEncryptionTypeDef",
    "ClientListPackagingConfigurationsResponsePackagingConfigurationsMssPackageMssManifestsStreamSelectionTypeDef",
    "ClientListPackagingConfigurationsResponsePackagingConfigurationsMssPackageMssManifestsTypeDef",
    "ClientListPackagingConfigurationsResponsePackagingConfigurationsMssPackageTypeDef",
    "ClientListPackagingConfigurationsResponsePackagingConfigurationsTypeDef",
    "ClientListPackagingConfigurationsResponseTypeDef",
    "ClientListPackagingGroupsResponsePackagingGroupsTypeDef",
    "ClientListPackagingGroupsResponseTypeDef",
    "AssetShallowTypeDef",
    "ListAssetsResponseTypeDef",
    "SpekeKeyProviderTypeDef",
    "CmafEncryptionTypeDef",
    "StreamSelectionTypeDef",
    "HlsManifestTypeDef",
    "CmafPackageTypeDef",
    "DashEncryptionTypeDef",
    "DashManifestTypeDef",
    "DashPackageTypeDef",
    "HlsEncryptionTypeDef",
    "HlsPackageTypeDef",
    "MssEncryptionTypeDef",
    "MssManifestTypeDef",
    "MssPackageTypeDef",
    "PackagingConfigurationTypeDef",
    "ListPackagingConfigurationsResponseTypeDef",
    "PackagingGroupTypeDef",
    "ListPackagingGroupsResponseTypeDef",
    "PaginatorConfigTypeDef",
)

ClientCreateAssetResponseEgressEndpointsTypeDef = TypedDict(
    "ClientCreateAssetResponseEgressEndpointsTypeDef",
    {"PackagingConfigurationId": str, "Url": str},
    total=False,
)

ClientCreateAssetResponseTypeDef = TypedDict(
    "ClientCreateAssetResponseTypeDef",
    {
        "Arn": str,
        "CreatedAt": str,
        "EgressEndpoints": List[ClientCreateAssetResponseEgressEndpointsTypeDef],
        "Id": str,
        "PackagingGroupId": str,
        "ResourceId": str,
        "SourceArn": str,
        "SourceRoleArn": str,
    },
    total=False,
)

_RequiredClientCreatePackagingConfigurationCmafPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "_RequiredClientCreatePackagingConfigurationCmafPackageEncryptionSpekeKeyProviderTypeDef",
    {"RoleArn": str, "SystemIds": List[str]},
)
_OptionalClientCreatePackagingConfigurationCmafPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "_OptionalClientCreatePackagingConfigurationCmafPackageEncryptionSpekeKeyProviderTypeDef",
    {"Url": str},
    total=False,
)


class ClientCreatePackagingConfigurationCmafPackageEncryptionSpekeKeyProviderTypeDef(
    _RequiredClientCreatePackagingConfigurationCmafPackageEncryptionSpekeKeyProviderTypeDef,
    _OptionalClientCreatePackagingConfigurationCmafPackageEncryptionSpekeKeyProviderTypeDef,
):
    pass


ClientCreatePackagingConfigurationCmafPackageEncryptionTypeDef = TypedDict(
    "ClientCreatePackagingConfigurationCmafPackageEncryptionTypeDef",
    {
        "SpekeKeyProvider": ClientCreatePackagingConfigurationCmafPackageEncryptionSpekeKeyProviderTypeDef
    },
)

ClientCreatePackagingConfigurationCmafPackageHlsManifestsStreamSelectionTypeDef = TypedDict(
    "ClientCreatePackagingConfigurationCmafPackageHlsManifestsStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)

ClientCreatePackagingConfigurationCmafPackageHlsManifestsTypeDef = TypedDict(
    "ClientCreatePackagingConfigurationCmafPackageHlsManifestsTypeDef",
    {
        "AdMarkers": Literal["NONE", "SCTE35_ENHANCED", "PASSTHROUGH"],
        "IncludeIframeOnlyStream": bool,
        "ManifestName": str,
        "ProgramDateTimeIntervalSeconds": int,
        "RepeatExtXKey": bool,
        "StreamSelection": ClientCreatePackagingConfigurationCmafPackageHlsManifestsStreamSelectionTypeDef,
    },
    total=False,
)

ClientCreatePackagingConfigurationCmafPackageTypeDef = TypedDict(
    "ClientCreatePackagingConfigurationCmafPackageTypeDef",
    {
        "Encryption": ClientCreatePackagingConfigurationCmafPackageEncryptionTypeDef,
        "HlsManifests": List[ClientCreatePackagingConfigurationCmafPackageHlsManifestsTypeDef],
        "SegmentDurationSeconds": int,
    },
    total=False,
)

ClientCreatePackagingConfigurationDashPackageDashManifestsStreamSelectionTypeDef = TypedDict(
    "ClientCreatePackagingConfigurationDashPackageDashManifestsStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)

ClientCreatePackagingConfigurationDashPackageDashManifestsTypeDef = TypedDict(
    "ClientCreatePackagingConfigurationDashPackageDashManifestsTypeDef",
    {
        "ManifestName": str,
        "MinBufferTimeSeconds": int,
        "Profile": Literal["NONE", "HBBTV_1_5"],
        "StreamSelection": ClientCreatePackagingConfigurationDashPackageDashManifestsStreamSelectionTypeDef,
    },
    total=False,
)

ClientCreatePackagingConfigurationDashPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "ClientCreatePackagingConfigurationDashPackageEncryptionSpekeKeyProviderTypeDef",
    {"RoleArn": str, "SystemIds": List[str], "Url": str},
    total=False,
)

ClientCreatePackagingConfigurationDashPackageEncryptionTypeDef = TypedDict(
    "ClientCreatePackagingConfigurationDashPackageEncryptionTypeDef",
    {
        "SpekeKeyProvider": ClientCreatePackagingConfigurationDashPackageEncryptionSpekeKeyProviderTypeDef
    },
    total=False,
)

_RequiredClientCreatePackagingConfigurationDashPackageTypeDef = TypedDict(
    "_RequiredClientCreatePackagingConfigurationDashPackageTypeDef",
    {"DashManifests": List[ClientCreatePackagingConfigurationDashPackageDashManifestsTypeDef]},
)
_OptionalClientCreatePackagingConfigurationDashPackageTypeDef = TypedDict(
    "_OptionalClientCreatePackagingConfigurationDashPackageTypeDef",
    {
        "Encryption": ClientCreatePackagingConfigurationDashPackageEncryptionTypeDef,
        "SegmentDurationSeconds": int,
    },
    total=False,
)


class ClientCreatePackagingConfigurationDashPackageTypeDef(
    _RequiredClientCreatePackagingConfigurationDashPackageTypeDef,
    _OptionalClientCreatePackagingConfigurationDashPackageTypeDef,
):
    pass


_RequiredClientCreatePackagingConfigurationHlsPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "_RequiredClientCreatePackagingConfigurationHlsPackageEncryptionSpekeKeyProviderTypeDef",
    {"RoleArn": str, "SystemIds": List[str]},
)
_OptionalClientCreatePackagingConfigurationHlsPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "_OptionalClientCreatePackagingConfigurationHlsPackageEncryptionSpekeKeyProviderTypeDef",
    {"Url": str},
    total=False,
)


class ClientCreatePackagingConfigurationHlsPackageEncryptionSpekeKeyProviderTypeDef(
    _RequiredClientCreatePackagingConfigurationHlsPackageEncryptionSpekeKeyProviderTypeDef,
    _OptionalClientCreatePackagingConfigurationHlsPackageEncryptionSpekeKeyProviderTypeDef,
):
    pass


_RequiredClientCreatePackagingConfigurationHlsPackageEncryptionTypeDef = TypedDict(
    "_RequiredClientCreatePackagingConfigurationHlsPackageEncryptionTypeDef",
    {
        "SpekeKeyProvider": ClientCreatePackagingConfigurationHlsPackageEncryptionSpekeKeyProviderTypeDef
    },
)
_OptionalClientCreatePackagingConfigurationHlsPackageEncryptionTypeDef = TypedDict(
    "_OptionalClientCreatePackagingConfigurationHlsPackageEncryptionTypeDef",
    {"ConstantInitializationVector": str, "EncryptionMethod": Literal["AES_128", "SAMPLE_AES"]},
    total=False,
)


class ClientCreatePackagingConfigurationHlsPackageEncryptionTypeDef(
    _RequiredClientCreatePackagingConfigurationHlsPackageEncryptionTypeDef,
    _OptionalClientCreatePackagingConfigurationHlsPackageEncryptionTypeDef,
):
    pass


ClientCreatePackagingConfigurationHlsPackageHlsManifestsStreamSelectionTypeDef = TypedDict(
    "ClientCreatePackagingConfigurationHlsPackageHlsManifestsStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)

ClientCreatePackagingConfigurationHlsPackageHlsManifestsTypeDef = TypedDict(
    "ClientCreatePackagingConfigurationHlsPackageHlsManifestsTypeDef",
    {
        "AdMarkers": Literal["NONE", "SCTE35_ENHANCED", "PASSTHROUGH"],
        "IncludeIframeOnlyStream": bool,
        "ManifestName": str,
        "ProgramDateTimeIntervalSeconds": int,
        "RepeatExtXKey": bool,
        "StreamSelection": ClientCreatePackagingConfigurationHlsPackageHlsManifestsStreamSelectionTypeDef,
    },
    total=False,
)

ClientCreatePackagingConfigurationHlsPackageTypeDef = TypedDict(
    "ClientCreatePackagingConfigurationHlsPackageTypeDef",
    {
        "Encryption": ClientCreatePackagingConfigurationHlsPackageEncryptionTypeDef,
        "HlsManifests": List[ClientCreatePackagingConfigurationHlsPackageHlsManifestsTypeDef],
        "SegmentDurationSeconds": int,
        "UseAudioRenditionGroup": bool,
    },
    total=False,
)

_RequiredClientCreatePackagingConfigurationMssPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "_RequiredClientCreatePackagingConfigurationMssPackageEncryptionSpekeKeyProviderTypeDef",
    {"RoleArn": str, "SystemIds": List[str]},
)
_OptionalClientCreatePackagingConfigurationMssPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "_OptionalClientCreatePackagingConfigurationMssPackageEncryptionSpekeKeyProviderTypeDef",
    {"Url": str},
    total=False,
)


class ClientCreatePackagingConfigurationMssPackageEncryptionSpekeKeyProviderTypeDef(
    _RequiredClientCreatePackagingConfigurationMssPackageEncryptionSpekeKeyProviderTypeDef,
    _OptionalClientCreatePackagingConfigurationMssPackageEncryptionSpekeKeyProviderTypeDef,
):
    pass


ClientCreatePackagingConfigurationMssPackageEncryptionTypeDef = TypedDict(
    "ClientCreatePackagingConfigurationMssPackageEncryptionTypeDef",
    {
        "SpekeKeyProvider": ClientCreatePackagingConfigurationMssPackageEncryptionSpekeKeyProviderTypeDef
    },
)

ClientCreatePackagingConfigurationMssPackageMssManifestsStreamSelectionTypeDef = TypedDict(
    "ClientCreatePackagingConfigurationMssPackageMssManifestsStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)

ClientCreatePackagingConfigurationMssPackageMssManifestsTypeDef = TypedDict(
    "ClientCreatePackagingConfigurationMssPackageMssManifestsTypeDef",
    {
        "ManifestName": str,
        "StreamSelection": ClientCreatePackagingConfigurationMssPackageMssManifestsStreamSelectionTypeDef,
    },
    total=False,
)

ClientCreatePackagingConfigurationMssPackageTypeDef = TypedDict(
    "ClientCreatePackagingConfigurationMssPackageTypeDef",
    {
        "Encryption": ClientCreatePackagingConfigurationMssPackageEncryptionTypeDef,
        "MssManifests": List[ClientCreatePackagingConfigurationMssPackageMssManifestsTypeDef],
        "SegmentDurationSeconds": int,
    },
    total=False,
)

ClientCreatePackagingConfigurationResponseCmafPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "ClientCreatePackagingConfigurationResponseCmafPackageEncryptionSpekeKeyProviderTypeDef",
    {"RoleArn": str, "SystemIds": List[str], "Url": str},
    total=False,
)

ClientCreatePackagingConfigurationResponseCmafPackageEncryptionTypeDef = TypedDict(
    "ClientCreatePackagingConfigurationResponseCmafPackageEncryptionTypeDef",
    {
        "SpekeKeyProvider": ClientCreatePackagingConfigurationResponseCmafPackageEncryptionSpekeKeyProviderTypeDef
    },
    total=False,
)

ClientCreatePackagingConfigurationResponseCmafPackageHlsManifestsStreamSelectionTypeDef = TypedDict(
    "ClientCreatePackagingConfigurationResponseCmafPackageHlsManifestsStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)

ClientCreatePackagingConfigurationResponseCmafPackageHlsManifestsTypeDef = TypedDict(
    "ClientCreatePackagingConfigurationResponseCmafPackageHlsManifestsTypeDef",
    {
        "AdMarkers": Literal["NONE", "SCTE35_ENHANCED", "PASSTHROUGH"],
        "IncludeIframeOnlyStream": bool,
        "ManifestName": str,
        "ProgramDateTimeIntervalSeconds": int,
        "RepeatExtXKey": bool,
        "StreamSelection": ClientCreatePackagingConfigurationResponseCmafPackageHlsManifestsStreamSelectionTypeDef,
    },
    total=False,
)

ClientCreatePackagingConfigurationResponseCmafPackageTypeDef = TypedDict(
    "ClientCreatePackagingConfigurationResponseCmafPackageTypeDef",
    {
        "Encryption": ClientCreatePackagingConfigurationResponseCmafPackageEncryptionTypeDef,
        "HlsManifests": List[
            ClientCreatePackagingConfigurationResponseCmafPackageHlsManifestsTypeDef
        ],
        "SegmentDurationSeconds": int,
    },
    total=False,
)

ClientCreatePackagingConfigurationResponseDashPackageDashManifestsStreamSelectionTypeDef = TypedDict(
    "ClientCreatePackagingConfigurationResponseDashPackageDashManifestsStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)

ClientCreatePackagingConfigurationResponseDashPackageDashManifestsTypeDef = TypedDict(
    "ClientCreatePackagingConfigurationResponseDashPackageDashManifestsTypeDef",
    {
        "ManifestName": str,
        "MinBufferTimeSeconds": int,
        "Profile": Literal["NONE", "HBBTV_1_5"],
        "StreamSelection": ClientCreatePackagingConfigurationResponseDashPackageDashManifestsStreamSelectionTypeDef,
    },
    total=False,
)

ClientCreatePackagingConfigurationResponseDashPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "ClientCreatePackagingConfigurationResponseDashPackageEncryptionSpekeKeyProviderTypeDef",
    {"RoleArn": str, "SystemIds": List[str], "Url": str},
    total=False,
)

ClientCreatePackagingConfigurationResponseDashPackageEncryptionTypeDef = TypedDict(
    "ClientCreatePackagingConfigurationResponseDashPackageEncryptionTypeDef",
    {
        "SpekeKeyProvider": ClientCreatePackagingConfigurationResponseDashPackageEncryptionSpekeKeyProviderTypeDef
    },
    total=False,
)

ClientCreatePackagingConfigurationResponseDashPackageTypeDef = TypedDict(
    "ClientCreatePackagingConfigurationResponseDashPackageTypeDef",
    {
        "DashManifests": List[
            ClientCreatePackagingConfigurationResponseDashPackageDashManifestsTypeDef
        ],
        "Encryption": ClientCreatePackagingConfigurationResponseDashPackageEncryptionTypeDef,
        "SegmentDurationSeconds": int,
    },
    total=False,
)

ClientCreatePackagingConfigurationResponseHlsPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "ClientCreatePackagingConfigurationResponseHlsPackageEncryptionSpekeKeyProviderTypeDef",
    {"RoleArn": str, "SystemIds": List[str], "Url": str},
    total=False,
)

ClientCreatePackagingConfigurationResponseHlsPackageEncryptionTypeDef = TypedDict(
    "ClientCreatePackagingConfigurationResponseHlsPackageEncryptionTypeDef",
    {
        "ConstantInitializationVector": str,
        "EncryptionMethod": Literal["AES_128", "SAMPLE_AES"],
        "SpekeKeyProvider": ClientCreatePackagingConfigurationResponseHlsPackageEncryptionSpekeKeyProviderTypeDef,
    },
    total=False,
)

ClientCreatePackagingConfigurationResponseHlsPackageHlsManifestsStreamSelectionTypeDef = TypedDict(
    "ClientCreatePackagingConfigurationResponseHlsPackageHlsManifestsStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)

ClientCreatePackagingConfigurationResponseHlsPackageHlsManifestsTypeDef = TypedDict(
    "ClientCreatePackagingConfigurationResponseHlsPackageHlsManifestsTypeDef",
    {
        "AdMarkers": Literal["NONE", "SCTE35_ENHANCED", "PASSTHROUGH"],
        "IncludeIframeOnlyStream": bool,
        "ManifestName": str,
        "ProgramDateTimeIntervalSeconds": int,
        "RepeatExtXKey": bool,
        "StreamSelection": ClientCreatePackagingConfigurationResponseHlsPackageHlsManifestsStreamSelectionTypeDef,
    },
    total=False,
)

ClientCreatePackagingConfigurationResponseHlsPackageTypeDef = TypedDict(
    "ClientCreatePackagingConfigurationResponseHlsPackageTypeDef",
    {
        "Encryption": ClientCreatePackagingConfigurationResponseHlsPackageEncryptionTypeDef,
        "HlsManifests": List[
            ClientCreatePackagingConfigurationResponseHlsPackageHlsManifestsTypeDef
        ],
        "SegmentDurationSeconds": int,
        "UseAudioRenditionGroup": bool,
    },
    total=False,
)

ClientCreatePackagingConfigurationResponseMssPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "ClientCreatePackagingConfigurationResponseMssPackageEncryptionSpekeKeyProviderTypeDef",
    {"RoleArn": str, "SystemIds": List[str], "Url": str},
    total=False,
)

ClientCreatePackagingConfigurationResponseMssPackageEncryptionTypeDef = TypedDict(
    "ClientCreatePackagingConfigurationResponseMssPackageEncryptionTypeDef",
    {
        "SpekeKeyProvider": ClientCreatePackagingConfigurationResponseMssPackageEncryptionSpekeKeyProviderTypeDef
    },
    total=False,
)

ClientCreatePackagingConfigurationResponseMssPackageMssManifestsStreamSelectionTypeDef = TypedDict(
    "ClientCreatePackagingConfigurationResponseMssPackageMssManifestsStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)

ClientCreatePackagingConfigurationResponseMssPackageMssManifestsTypeDef = TypedDict(
    "ClientCreatePackagingConfigurationResponseMssPackageMssManifestsTypeDef",
    {
        "ManifestName": str,
        "StreamSelection": ClientCreatePackagingConfigurationResponseMssPackageMssManifestsStreamSelectionTypeDef,
    },
    total=False,
)

ClientCreatePackagingConfigurationResponseMssPackageTypeDef = TypedDict(
    "ClientCreatePackagingConfigurationResponseMssPackageTypeDef",
    {
        "Encryption": ClientCreatePackagingConfigurationResponseMssPackageEncryptionTypeDef,
        "MssManifests": List[
            ClientCreatePackagingConfigurationResponseMssPackageMssManifestsTypeDef
        ],
        "SegmentDurationSeconds": int,
    },
    total=False,
)

ClientCreatePackagingConfigurationResponseTypeDef = TypedDict(
    "ClientCreatePackagingConfigurationResponseTypeDef",
    {
        "Arn": str,
        "CmafPackage": ClientCreatePackagingConfigurationResponseCmafPackageTypeDef,
        "DashPackage": ClientCreatePackagingConfigurationResponseDashPackageTypeDef,
        "HlsPackage": ClientCreatePackagingConfigurationResponseHlsPackageTypeDef,
        "Id": str,
        "MssPackage": ClientCreatePackagingConfigurationResponseMssPackageTypeDef,
        "PackagingGroupId": str,
    },
    total=False,
)

ClientCreatePackagingGroupResponseTypeDef = TypedDict(
    "ClientCreatePackagingGroupResponseTypeDef",
    {"Arn": str, "DomainName": str, "Id": str},
    total=False,
)

ClientDescribeAssetResponseEgressEndpointsTypeDef = TypedDict(
    "ClientDescribeAssetResponseEgressEndpointsTypeDef",
    {"PackagingConfigurationId": str, "Url": str},
    total=False,
)

ClientDescribeAssetResponseTypeDef = TypedDict(
    "ClientDescribeAssetResponseTypeDef",
    {
        "Arn": str,
        "CreatedAt": str,
        "EgressEndpoints": List[ClientDescribeAssetResponseEgressEndpointsTypeDef],
        "Id": str,
        "PackagingGroupId": str,
        "ResourceId": str,
        "SourceArn": str,
        "SourceRoleArn": str,
    },
    total=False,
)

ClientDescribePackagingConfigurationResponseCmafPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "ClientDescribePackagingConfigurationResponseCmafPackageEncryptionSpekeKeyProviderTypeDef",
    {"RoleArn": str, "SystemIds": List[str], "Url": str},
    total=False,
)

ClientDescribePackagingConfigurationResponseCmafPackageEncryptionTypeDef = TypedDict(
    "ClientDescribePackagingConfigurationResponseCmafPackageEncryptionTypeDef",
    {
        "SpekeKeyProvider": ClientDescribePackagingConfigurationResponseCmafPackageEncryptionSpekeKeyProviderTypeDef
    },
    total=False,
)

ClientDescribePackagingConfigurationResponseCmafPackageHlsManifestsStreamSelectionTypeDef = TypedDict(
    "ClientDescribePackagingConfigurationResponseCmafPackageHlsManifestsStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)

ClientDescribePackagingConfigurationResponseCmafPackageHlsManifestsTypeDef = TypedDict(
    "ClientDescribePackagingConfigurationResponseCmafPackageHlsManifestsTypeDef",
    {
        "AdMarkers": Literal["NONE", "SCTE35_ENHANCED", "PASSTHROUGH"],
        "IncludeIframeOnlyStream": bool,
        "ManifestName": str,
        "ProgramDateTimeIntervalSeconds": int,
        "RepeatExtXKey": bool,
        "StreamSelection": ClientDescribePackagingConfigurationResponseCmafPackageHlsManifestsStreamSelectionTypeDef,
    },
    total=False,
)

ClientDescribePackagingConfigurationResponseCmafPackageTypeDef = TypedDict(
    "ClientDescribePackagingConfigurationResponseCmafPackageTypeDef",
    {
        "Encryption": ClientDescribePackagingConfigurationResponseCmafPackageEncryptionTypeDef,
        "HlsManifests": List[
            ClientDescribePackagingConfigurationResponseCmafPackageHlsManifestsTypeDef
        ],
        "SegmentDurationSeconds": int,
    },
    total=False,
)

ClientDescribePackagingConfigurationResponseDashPackageDashManifestsStreamSelectionTypeDef = TypedDict(
    "ClientDescribePackagingConfigurationResponseDashPackageDashManifestsStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)

ClientDescribePackagingConfigurationResponseDashPackageDashManifestsTypeDef = TypedDict(
    "ClientDescribePackagingConfigurationResponseDashPackageDashManifestsTypeDef",
    {
        "ManifestName": str,
        "MinBufferTimeSeconds": int,
        "Profile": Literal["NONE", "HBBTV_1_5"],
        "StreamSelection": ClientDescribePackagingConfigurationResponseDashPackageDashManifestsStreamSelectionTypeDef,
    },
    total=False,
)

ClientDescribePackagingConfigurationResponseDashPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "ClientDescribePackagingConfigurationResponseDashPackageEncryptionSpekeKeyProviderTypeDef",
    {"RoleArn": str, "SystemIds": List[str], "Url": str},
    total=False,
)

ClientDescribePackagingConfigurationResponseDashPackageEncryptionTypeDef = TypedDict(
    "ClientDescribePackagingConfigurationResponseDashPackageEncryptionTypeDef",
    {
        "SpekeKeyProvider": ClientDescribePackagingConfigurationResponseDashPackageEncryptionSpekeKeyProviderTypeDef
    },
    total=False,
)

ClientDescribePackagingConfigurationResponseDashPackageTypeDef = TypedDict(
    "ClientDescribePackagingConfigurationResponseDashPackageTypeDef",
    {
        "DashManifests": List[
            ClientDescribePackagingConfigurationResponseDashPackageDashManifestsTypeDef
        ],
        "Encryption": ClientDescribePackagingConfigurationResponseDashPackageEncryptionTypeDef,
        "SegmentDurationSeconds": int,
    },
    total=False,
)

ClientDescribePackagingConfigurationResponseHlsPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "ClientDescribePackagingConfigurationResponseHlsPackageEncryptionSpekeKeyProviderTypeDef",
    {"RoleArn": str, "SystemIds": List[str], "Url": str},
    total=False,
)

ClientDescribePackagingConfigurationResponseHlsPackageEncryptionTypeDef = TypedDict(
    "ClientDescribePackagingConfigurationResponseHlsPackageEncryptionTypeDef",
    {
        "ConstantInitializationVector": str,
        "EncryptionMethod": Literal["AES_128", "SAMPLE_AES"],
        "SpekeKeyProvider": ClientDescribePackagingConfigurationResponseHlsPackageEncryptionSpekeKeyProviderTypeDef,
    },
    total=False,
)

ClientDescribePackagingConfigurationResponseHlsPackageHlsManifestsStreamSelectionTypeDef = TypedDict(
    "ClientDescribePackagingConfigurationResponseHlsPackageHlsManifestsStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)

ClientDescribePackagingConfigurationResponseHlsPackageHlsManifestsTypeDef = TypedDict(
    "ClientDescribePackagingConfigurationResponseHlsPackageHlsManifestsTypeDef",
    {
        "AdMarkers": Literal["NONE", "SCTE35_ENHANCED", "PASSTHROUGH"],
        "IncludeIframeOnlyStream": bool,
        "ManifestName": str,
        "ProgramDateTimeIntervalSeconds": int,
        "RepeatExtXKey": bool,
        "StreamSelection": ClientDescribePackagingConfigurationResponseHlsPackageHlsManifestsStreamSelectionTypeDef,
    },
    total=False,
)

ClientDescribePackagingConfigurationResponseHlsPackageTypeDef = TypedDict(
    "ClientDescribePackagingConfigurationResponseHlsPackageTypeDef",
    {
        "Encryption": ClientDescribePackagingConfigurationResponseHlsPackageEncryptionTypeDef,
        "HlsManifests": List[
            ClientDescribePackagingConfigurationResponseHlsPackageHlsManifestsTypeDef
        ],
        "SegmentDurationSeconds": int,
        "UseAudioRenditionGroup": bool,
    },
    total=False,
)

ClientDescribePackagingConfigurationResponseMssPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "ClientDescribePackagingConfigurationResponseMssPackageEncryptionSpekeKeyProviderTypeDef",
    {"RoleArn": str, "SystemIds": List[str], "Url": str},
    total=False,
)

ClientDescribePackagingConfigurationResponseMssPackageEncryptionTypeDef = TypedDict(
    "ClientDescribePackagingConfigurationResponseMssPackageEncryptionTypeDef",
    {
        "SpekeKeyProvider": ClientDescribePackagingConfigurationResponseMssPackageEncryptionSpekeKeyProviderTypeDef
    },
    total=False,
)

ClientDescribePackagingConfigurationResponseMssPackageMssManifestsStreamSelectionTypeDef = TypedDict(
    "ClientDescribePackagingConfigurationResponseMssPackageMssManifestsStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)

ClientDescribePackagingConfigurationResponseMssPackageMssManifestsTypeDef = TypedDict(
    "ClientDescribePackagingConfigurationResponseMssPackageMssManifestsTypeDef",
    {
        "ManifestName": str,
        "StreamSelection": ClientDescribePackagingConfigurationResponseMssPackageMssManifestsStreamSelectionTypeDef,
    },
    total=False,
)

ClientDescribePackagingConfigurationResponseMssPackageTypeDef = TypedDict(
    "ClientDescribePackagingConfigurationResponseMssPackageTypeDef",
    {
        "Encryption": ClientDescribePackagingConfigurationResponseMssPackageEncryptionTypeDef,
        "MssManifests": List[
            ClientDescribePackagingConfigurationResponseMssPackageMssManifestsTypeDef
        ],
        "SegmentDurationSeconds": int,
    },
    total=False,
)

ClientDescribePackagingConfigurationResponseTypeDef = TypedDict(
    "ClientDescribePackagingConfigurationResponseTypeDef",
    {
        "Arn": str,
        "CmafPackage": ClientDescribePackagingConfigurationResponseCmafPackageTypeDef,
        "DashPackage": ClientDescribePackagingConfigurationResponseDashPackageTypeDef,
        "HlsPackage": ClientDescribePackagingConfigurationResponseHlsPackageTypeDef,
        "Id": str,
        "MssPackage": ClientDescribePackagingConfigurationResponseMssPackageTypeDef,
        "PackagingGroupId": str,
    },
    total=False,
)

ClientDescribePackagingGroupResponseTypeDef = TypedDict(
    "ClientDescribePackagingGroupResponseTypeDef",
    {"Arn": str, "DomainName": str, "Id": str},
    total=False,
)

ClientListAssetsResponseAssetsTypeDef = TypedDict(
    "ClientListAssetsResponseAssetsTypeDef",
    {
        "Arn": str,
        "CreatedAt": str,
        "Id": str,
        "PackagingGroupId": str,
        "ResourceId": str,
        "SourceArn": str,
        "SourceRoleArn": str,
    },
    total=False,
)

ClientListAssetsResponseTypeDef = TypedDict(
    "ClientListAssetsResponseTypeDef",
    {"Assets": List[ClientListAssetsResponseAssetsTypeDef], "NextToken": str},
    total=False,
)

ClientListPackagingConfigurationsResponsePackagingConfigurationsCmafPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "ClientListPackagingConfigurationsResponsePackagingConfigurationsCmafPackageEncryptionSpekeKeyProviderTypeDef",
    {"RoleArn": str, "SystemIds": List[str], "Url": str},
    total=False,
)

ClientListPackagingConfigurationsResponsePackagingConfigurationsCmafPackageEncryptionTypeDef = TypedDict(
    "ClientListPackagingConfigurationsResponsePackagingConfigurationsCmafPackageEncryptionTypeDef",
    {
        "SpekeKeyProvider": ClientListPackagingConfigurationsResponsePackagingConfigurationsCmafPackageEncryptionSpekeKeyProviderTypeDef
    },
    total=False,
)

ClientListPackagingConfigurationsResponsePackagingConfigurationsCmafPackageHlsManifestsStreamSelectionTypeDef = TypedDict(
    "ClientListPackagingConfigurationsResponsePackagingConfigurationsCmafPackageHlsManifestsStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)

ClientListPackagingConfigurationsResponsePackagingConfigurationsCmafPackageHlsManifestsTypeDef = TypedDict(
    "ClientListPackagingConfigurationsResponsePackagingConfigurationsCmafPackageHlsManifestsTypeDef",
    {
        "AdMarkers": Literal["NONE", "SCTE35_ENHANCED", "PASSTHROUGH"],
        "IncludeIframeOnlyStream": bool,
        "ManifestName": str,
        "ProgramDateTimeIntervalSeconds": int,
        "RepeatExtXKey": bool,
        "StreamSelection": ClientListPackagingConfigurationsResponsePackagingConfigurationsCmafPackageHlsManifestsStreamSelectionTypeDef,
    },
    total=False,
)

ClientListPackagingConfigurationsResponsePackagingConfigurationsCmafPackageTypeDef = TypedDict(
    "ClientListPackagingConfigurationsResponsePackagingConfigurationsCmafPackageTypeDef",
    {
        "Encryption": ClientListPackagingConfigurationsResponsePackagingConfigurationsCmafPackageEncryptionTypeDef,
        "HlsManifests": List[
            ClientListPackagingConfigurationsResponsePackagingConfigurationsCmafPackageHlsManifestsTypeDef
        ],
        "SegmentDurationSeconds": int,
    },
    total=False,
)

ClientListPackagingConfigurationsResponsePackagingConfigurationsDashPackageDashManifestsStreamSelectionTypeDef = TypedDict(
    "ClientListPackagingConfigurationsResponsePackagingConfigurationsDashPackageDashManifestsStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)

ClientListPackagingConfigurationsResponsePackagingConfigurationsDashPackageDashManifestsTypeDef = TypedDict(
    "ClientListPackagingConfigurationsResponsePackagingConfigurationsDashPackageDashManifestsTypeDef",
    {
        "ManifestName": str,
        "MinBufferTimeSeconds": int,
        "Profile": Literal["NONE", "HBBTV_1_5"],
        "StreamSelection": ClientListPackagingConfigurationsResponsePackagingConfigurationsDashPackageDashManifestsStreamSelectionTypeDef,
    },
    total=False,
)

ClientListPackagingConfigurationsResponsePackagingConfigurationsDashPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "ClientListPackagingConfigurationsResponsePackagingConfigurationsDashPackageEncryptionSpekeKeyProviderTypeDef",
    {"RoleArn": str, "SystemIds": List[str], "Url": str},
    total=False,
)

ClientListPackagingConfigurationsResponsePackagingConfigurationsDashPackageEncryptionTypeDef = TypedDict(
    "ClientListPackagingConfigurationsResponsePackagingConfigurationsDashPackageEncryptionTypeDef",
    {
        "SpekeKeyProvider": ClientListPackagingConfigurationsResponsePackagingConfigurationsDashPackageEncryptionSpekeKeyProviderTypeDef
    },
    total=False,
)

ClientListPackagingConfigurationsResponsePackagingConfigurationsDashPackageTypeDef = TypedDict(
    "ClientListPackagingConfigurationsResponsePackagingConfigurationsDashPackageTypeDef",
    {
        "DashManifests": List[
            ClientListPackagingConfigurationsResponsePackagingConfigurationsDashPackageDashManifestsTypeDef
        ],
        "Encryption": ClientListPackagingConfigurationsResponsePackagingConfigurationsDashPackageEncryptionTypeDef,
        "SegmentDurationSeconds": int,
    },
    total=False,
)

ClientListPackagingConfigurationsResponsePackagingConfigurationsHlsPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "ClientListPackagingConfigurationsResponsePackagingConfigurationsHlsPackageEncryptionSpekeKeyProviderTypeDef",
    {"RoleArn": str, "SystemIds": List[str], "Url": str},
    total=False,
)

ClientListPackagingConfigurationsResponsePackagingConfigurationsHlsPackageEncryptionTypeDef = TypedDict(
    "ClientListPackagingConfigurationsResponsePackagingConfigurationsHlsPackageEncryptionTypeDef",
    {
        "ConstantInitializationVector": str,
        "EncryptionMethod": Literal["AES_128", "SAMPLE_AES"],
        "SpekeKeyProvider": ClientListPackagingConfigurationsResponsePackagingConfigurationsHlsPackageEncryptionSpekeKeyProviderTypeDef,
    },
    total=False,
)

ClientListPackagingConfigurationsResponsePackagingConfigurationsHlsPackageHlsManifestsStreamSelectionTypeDef = TypedDict(
    "ClientListPackagingConfigurationsResponsePackagingConfigurationsHlsPackageHlsManifestsStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)

ClientListPackagingConfigurationsResponsePackagingConfigurationsHlsPackageHlsManifestsTypeDef = TypedDict(
    "ClientListPackagingConfigurationsResponsePackagingConfigurationsHlsPackageHlsManifestsTypeDef",
    {
        "AdMarkers": Literal["NONE", "SCTE35_ENHANCED", "PASSTHROUGH"],
        "IncludeIframeOnlyStream": bool,
        "ManifestName": str,
        "ProgramDateTimeIntervalSeconds": int,
        "RepeatExtXKey": bool,
        "StreamSelection": ClientListPackagingConfigurationsResponsePackagingConfigurationsHlsPackageHlsManifestsStreamSelectionTypeDef,
    },
    total=False,
)

ClientListPackagingConfigurationsResponsePackagingConfigurationsHlsPackageTypeDef = TypedDict(
    "ClientListPackagingConfigurationsResponsePackagingConfigurationsHlsPackageTypeDef",
    {
        "Encryption": ClientListPackagingConfigurationsResponsePackagingConfigurationsHlsPackageEncryptionTypeDef,
        "HlsManifests": List[
            ClientListPackagingConfigurationsResponsePackagingConfigurationsHlsPackageHlsManifestsTypeDef
        ],
        "SegmentDurationSeconds": int,
        "UseAudioRenditionGroup": bool,
    },
    total=False,
)

ClientListPackagingConfigurationsResponsePackagingConfigurationsMssPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "ClientListPackagingConfigurationsResponsePackagingConfigurationsMssPackageEncryptionSpekeKeyProviderTypeDef",
    {"RoleArn": str, "SystemIds": List[str], "Url": str},
    total=False,
)

ClientListPackagingConfigurationsResponsePackagingConfigurationsMssPackageEncryptionTypeDef = TypedDict(
    "ClientListPackagingConfigurationsResponsePackagingConfigurationsMssPackageEncryptionTypeDef",
    {
        "SpekeKeyProvider": ClientListPackagingConfigurationsResponsePackagingConfigurationsMssPackageEncryptionSpekeKeyProviderTypeDef
    },
    total=False,
)

ClientListPackagingConfigurationsResponsePackagingConfigurationsMssPackageMssManifestsStreamSelectionTypeDef = TypedDict(
    "ClientListPackagingConfigurationsResponsePackagingConfigurationsMssPackageMssManifestsStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)

ClientListPackagingConfigurationsResponsePackagingConfigurationsMssPackageMssManifestsTypeDef = TypedDict(
    "ClientListPackagingConfigurationsResponsePackagingConfigurationsMssPackageMssManifestsTypeDef",
    {
        "ManifestName": str,
        "StreamSelection": ClientListPackagingConfigurationsResponsePackagingConfigurationsMssPackageMssManifestsStreamSelectionTypeDef,
    },
    total=False,
)

ClientListPackagingConfigurationsResponsePackagingConfigurationsMssPackageTypeDef = TypedDict(
    "ClientListPackagingConfigurationsResponsePackagingConfigurationsMssPackageTypeDef",
    {
        "Encryption": ClientListPackagingConfigurationsResponsePackagingConfigurationsMssPackageEncryptionTypeDef,
        "MssManifests": List[
            ClientListPackagingConfigurationsResponsePackagingConfigurationsMssPackageMssManifestsTypeDef
        ],
        "SegmentDurationSeconds": int,
    },
    total=False,
)

ClientListPackagingConfigurationsResponsePackagingConfigurationsTypeDef = TypedDict(
    "ClientListPackagingConfigurationsResponsePackagingConfigurationsTypeDef",
    {
        "Arn": str,
        "CmafPackage": ClientListPackagingConfigurationsResponsePackagingConfigurationsCmafPackageTypeDef,
        "DashPackage": ClientListPackagingConfigurationsResponsePackagingConfigurationsDashPackageTypeDef,
        "HlsPackage": ClientListPackagingConfigurationsResponsePackagingConfigurationsHlsPackageTypeDef,
        "Id": str,
        "MssPackage": ClientListPackagingConfigurationsResponsePackagingConfigurationsMssPackageTypeDef,
        "PackagingGroupId": str,
    },
    total=False,
)

ClientListPackagingConfigurationsResponseTypeDef = TypedDict(
    "ClientListPackagingConfigurationsResponseTypeDef",
    {
        "NextToken": str,
        "PackagingConfigurations": List[
            ClientListPackagingConfigurationsResponsePackagingConfigurationsTypeDef
        ],
    },
    total=False,
)

ClientListPackagingGroupsResponsePackagingGroupsTypeDef = TypedDict(
    "ClientListPackagingGroupsResponsePackagingGroupsTypeDef",
    {"Arn": str, "DomainName": str, "Id": str},
    total=False,
)

ClientListPackagingGroupsResponseTypeDef = TypedDict(
    "ClientListPackagingGroupsResponseTypeDef",
    {
        "NextToken": str,
        "PackagingGroups": List[ClientListPackagingGroupsResponsePackagingGroupsTypeDef],
    },
    total=False,
)

AssetShallowTypeDef = TypedDict(
    "AssetShallowTypeDef",
    {
        "Arn": str,
        "CreatedAt": str,
        "Id": str,
        "PackagingGroupId": str,
        "ResourceId": str,
        "SourceArn": str,
        "SourceRoleArn": str,
    },
    total=False,
)

ListAssetsResponseTypeDef = TypedDict(
    "ListAssetsResponseTypeDef",
    {"Assets": List[AssetShallowTypeDef], "NextToken": str},
    total=False,
)

SpekeKeyProviderTypeDef = TypedDict(
    "SpekeKeyProviderTypeDef", {"RoleArn": str, "SystemIds": List[str], "Url": str}
)

CmafEncryptionTypeDef = TypedDict(
    "CmafEncryptionTypeDef", {"SpekeKeyProvider": SpekeKeyProviderTypeDef}
)

StreamSelectionTypeDef = TypedDict(
    "StreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)

HlsManifestTypeDef = TypedDict(
    "HlsManifestTypeDef",
    {
        "AdMarkers": Literal["NONE", "SCTE35_ENHANCED", "PASSTHROUGH"],
        "IncludeIframeOnlyStream": bool,
        "ManifestName": str,
        "ProgramDateTimeIntervalSeconds": int,
        "RepeatExtXKey": bool,
        "StreamSelection": StreamSelectionTypeDef,
    },
    total=False,
)

_RequiredCmafPackageTypeDef = TypedDict(
    "_RequiredCmafPackageTypeDef", {"HlsManifests": List[HlsManifestTypeDef]}
)
_OptionalCmafPackageTypeDef = TypedDict(
    "_OptionalCmafPackageTypeDef",
    {"Encryption": CmafEncryptionTypeDef, "SegmentDurationSeconds": int},
    total=False,
)


class CmafPackageTypeDef(_RequiredCmafPackageTypeDef, _OptionalCmafPackageTypeDef):
    pass


DashEncryptionTypeDef = TypedDict(
    "DashEncryptionTypeDef", {"SpekeKeyProvider": SpekeKeyProviderTypeDef}
)

DashManifestTypeDef = TypedDict(
    "DashManifestTypeDef",
    {
        "ManifestName": str,
        "MinBufferTimeSeconds": int,
        "Profile": Literal["NONE", "HBBTV_1_5"],
        "StreamSelection": StreamSelectionTypeDef,
    },
    total=False,
)

_RequiredDashPackageTypeDef = TypedDict(
    "_RequiredDashPackageTypeDef", {"DashManifests": List[DashManifestTypeDef]}
)
_OptionalDashPackageTypeDef = TypedDict(
    "_OptionalDashPackageTypeDef",
    {"Encryption": DashEncryptionTypeDef, "SegmentDurationSeconds": int},
    total=False,
)


class DashPackageTypeDef(_RequiredDashPackageTypeDef, _OptionalDashPackageTypeDef):
    pass


_RequiredHlsEncryptionTypeDef = TypedDict(
    "_RequiredHlsEncryptionTypeDef", {"SpekeKeyProvider": SpekeKeyProviderTypeDef}
)
_OptionalHlsEncryptionTypeDef = TypedDict(
    "_OptionalHlsEncryptionTypeDef",
    {"ConstantInitializationVector": str, "EncryptionMethod": Literal["AES_128", "SAMPLE_AES"]},
    total=False,
)


class HlsEncryptionTypeDef(_RequiredHlsEncryptionTypeDef, _OptionalHlsEncryptionTypeDef):
    pass


_RequiredHlsPackageTypeDef = TypedDict(
    "_RequiredHlsPackageTypeDef", {"HlsManifests": List[HlsManifestTypeDef]}
)
_OptionalHlsPackageTypeDef = TypedDict(
    "_OptionalHlsPackageTypeDef",
    {
        "Encryption": HlsEncryptionTypeDef,
        "SegmentDurationSeconds": int,
        "UseAudioRenditionGroup": bool,
    },
    total=False,
)


class HlsPackageTypeDef(_RequiredHlsPackageTypeDef, _OptionalHlsPackageTypeDef):
    pass


MssEncryptionTypeDef = TypedDict(
    "MssEncryptionTypeDef", {"SpekeKeyProvider": SpekeKeyProviderTypeDef}
)

MssManifestTypeDef = TypedDict(
    "MssManifestTypeDef",
    {"ManifestName": str, "StreamSelection": StreamSelectionTypeDef},
    total=False,
)

_RequiredMssPackageTypeDef = TypedDict(
    "_RequiredMssPackageTypeDef", {"MssManifests": List[MssManifestTypeDef]}
)
_OptionalMssPackageTypeDef = TypedDict(
    "_OptionalMssPackageTypeDef",
    {"Encryption": MssEncryptionTypeDef, "SegmentDurationSeconds": int},
    total=False,
)


class MssPackageTypeDef(_RequiredMssPackageTypeDef, _OptionalMssPackageTypeDef):
    pass


PackagingConfigurationTypeDef = TypedDict(
    "PackagingConfigurationTypeDef",
    {
        "Arn": str,
        "CmafPackage": CmafPackageTypeDef,
        "DashPackage": DashPackageTypeDef,
        "HlsPackage": HlsPackageTypeDef,
        "Id": str,
        "MssPackage": MssPackageTypeDef,
        "PackagingGroupId": str,
    },
    total=False,
)

ListPackagingConfigurationsResponseTypeDef = TypedDict(
    "ListPackagingConfigurationsResponseTypeDef",
    {"NextToken": str, "PackagingConfigurations": List[PackagingConfigurationTypeDef]},
    total=False,
)

PackagingGroupTypeDef = TypedDict(
    "PackagingGroupTypeDef", {"Arn": str, "DomainName": str, "Id": str}, total=False
)

ListPackagingGroupsResponseTypeDef = TypedDict(
    "ListPackagingGroupsResponseTypeDef",
    {"NextToken": str, "PackagingGroups": List[PackagingGroupTypeDef]},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)
