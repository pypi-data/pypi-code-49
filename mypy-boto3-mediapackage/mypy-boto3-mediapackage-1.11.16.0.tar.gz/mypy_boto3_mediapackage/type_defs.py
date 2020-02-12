"""
Main interface for mediapackage service type definitions.

Usage::

    from mypy_boto3.mediapackage.type_defs import ClientCreateChannelResponseHlsIngestIngestEndpointsTypeDef

    data: ClientCreateChannelResponseHlsIngestIngestEndpointsTypeDef = {...}
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
    "ClientCreateChannelResponseHlsIngestIngestEndpointsTypeDef",
    "ClientCreateChannelResponseHlsIngestTypeDef",
    "ClientCreateChannelResponseTypeDef",
    "ClientCreateHarvestJobResponseS3DestinationTypeDef",
    "ClientCreateHarvestJobResponseTypeDef",
    "ClientCreateHarvestJobS3DestinationTypeDef",
    "ClientCreateOriginEndpointAuthorizationTypeDef",
    "ClientCreateOriginEndpointCmafPackageEncryptionSpekeKeyProviderTypeDef",
    "ClientCreateOriginEndpointCmafPackageEncryptionTypeDef",
    "ClientCreateOriginEndpointCmafPackageHlsManifestsTypeDef",
    "ClientCreateOriginEndpointCmafPackageStreamSelectionTypeDef",
    "ClientCreateOriginEndpointCmafPackageTypeDef",
    "ClientCreateOriginEndpointDashPackageEncryptionSpekeKeyProviderTypeDef",
    "ClientCreateOriginEndpointDashPackageEncryptionTypeDef",
    "ClientCreateOriginEndpointDashPackageStreamSelectionTypeDef",
    "ClientCreateOriginEndpointDashPackageTypeDef",
    "ClientCreateOriginEndpointHlsPackageEncryptionSpekeKeyProviderTypeDef",
    "ClientCreateOriginEndpointHlsPackageEncryptionTypeDef",
    "ClientCreateOriginEndpointHlsPackageStreamSelectionTypeDef",
    "ClientCreateOriginEndpointHlsPackageTypeDef",
    "ClientCreateOriginEndpointMssPackageEncryptionSpekeKeyProviderTypeDef",
    "ClientCreateOriginEndpointMssPackageEncryptionTypeDef",
    "ClientCreateOriginEndpointMssPackageStreamSelectionTypeDef",
    "ClientCreateOriginEndpointMssPackageTypeDef",
    "ClientCreateOriginEndpointResponseAuthorizationTypeDef",
    "ClientCreateOriginEndpointResponseCmafPackageEncryptionSpekeKeyProviderTypeDef",
    "ClientCreateOriginEndpointResponseCmafPackageEncryptionTypeDef",
    "ClientCreateOriginEndpointResponseCmafPackageHlsManifestsTypeDef",
    "ClientCreateOriginEndpointResponseCmafPackageStreamSelectionTypeDef",
    "ClientCreateOriginEndpointResponseCmafPackageTypeDef",
    "ClientCreateOriginEndpointResponseDashPackageEncryptionSpekeKeyProviderTypeDef",
    "ClientCreateOriginEndpointResponseDashPackageEncryptionTypeDef",
    "ClientCreateOriginEndpointResponseDashPackageStreamSelectionTypeDef",
    "ClientCreateOriginEndpointResponseDashPackageTypeDef",
    "ClientCreateOriginEndpointResponseHlsPackageEncryptionSpekeKeyProviderTypeDef",
    "ClientCreateOriginEndpointResponseHlsPackageEncryptionTypeDef",
    "ClientCreateOriginEndpointResponseHlsPackageStreamSelectionTypeDef",
    "ClientCreateOriginEndpointResponseHlsPackageTypeDef",
    "ClientCreateOriginEndpointResponseMssPackageEncryptionSpekeKeyProviderTypeDef",
    "ClientCreateOriginEndpointResponseMssPackageEncryptionTypeDef",
    "ClientCreateOriginEndpointResponseMssPackageStreamSelectionTypeDef",
    "ClientCreateOriginEndpointResponseMssPackageTypeDef",
    "ClientCreateOriginEndpointResponseTypeDef",
    "ClientDescribeChannelResponseHlsIngestIngestEndpointsTypeDef",
    "ClientDescribeChannelResponseHlsIngestTypeDef",
    "ClientDescribeChannelResponseTypeDef",
    "ClientDescribeHarvestJobResponseS3DestinationTypeDef",
    "ClientDescribeHarvestJobResponseTypeDef",
    "ClientDescribeOriginEndpointResponseAuthorizationTypeDef",
    "ClientDescribeOriginEndpointResponseCmafPackageEncryptionSpekeKeyProviderTypeDef",
    "ClientDescribeOriginEndpointResponseCmafPackageEncryptionTypeDef",
    "ClientDescribeOriginEndpointResponseCmafPackageHlsManifestsTypeDef",
    "ClientDescribeOriginEndpointResponseCmafPackageStreamSelectionTypeDef",
    "ClientDescribeOriginEndpointResponseCmafPackageTypeDef",
    "ClientDescribeOriginEndpointResponseDashPackageEncryptionSpekeKeyProviderTypeDef",
    "ClientDescribeOriginEndpointResponseDashPackageEncryptionTypeDef",
    "ClientDescribeOriginEndpointResponseDashPackageStreamSelectionTypeDef",
    "ClientDescribeOriginEndpointResponseDashPackageTypeDef",
    "ClientDescribeOriginEndpointResponseHlsPackageEncryptionSpekeKeyProviderTypeDef",
    "ClientDescribeOriginEndpointResponseHlsPackageEncryptionTypeDef",
    "ClientDescribeOriginEndpointResponseHlsPackageStreamSelectionTypeDef",
    "ClientDescribeOriginEndpointResponseHlsPackageTypeDef",
    "ClientDescribeOriginEndpointResponseMssPackageEncryptionSpekeKeyProviderTypeDef",
    "ClientDescribeOriginEndpointResponseMssPackageEncryptionTypeDef",
    "ClientDescribeOriginEndpointResponseMssPackageStreamSelectionTypeDef",
    "ClientDescribeOriginEndpointResponseMssPackageTypeDef",
    "ClientDescribeOriginEndpointResponseTypeDef",
    "ClientListChannelsResponseChannelsHlsIngestIngestEndpointsTypeDef",
    "ClientListChannelsResponseChannelsHlsIngestTypeDef",
    "ClientListChannelsResponseChannelsTypeDef",
    "ClientListChannelsResponseTypeDef",
    "ClientListHarvestJobsResponseHarvestJobsS3DestinationTypeDef",
    "ClientListHarvestJobsResponseHarvestJobsTypeDef",
    "ClientListHarvestJobsResponseTypeDef",
    "ClientListOriginEndpointsResponseOriginEndpointsAuthorizationTypeDef",
    "ClientListOriginEndpointsResponseOriginEndpointsCmafPackageEncryptionSpekeKeyProviderTypeDef",
    "ClientListOriginEndpointsResponseOriginEndpointsCmafPackageEncryptionTypeDef",
    "ClientListOriginEndpointsResponseOriginEndpointsCmafPackageHlsManifestsTypeDef",
    "ClientListOriginEndpointsResponseOriginEndpointsCmafPackageStreamSelectionTypeDef",
    "ClientListOriginEndpointsResponseOriginEndpointsCmafPackageTypeDef",
    "ClientListOriginEndpointsResponseOriginEndpointsDashPackageEncryptionSpekeKeyProviderTypeDef",
    "ClientListOriginEndpointsResponseOriginEndpointsDashPackageEncryptionTypeDef",
    "ClientListOriginEndpointsResponseOriginEndpointsDashPackageStreamSelectionTypeDef",
    "ClientListOriginEndpointsResponseOriginEndpointsDashPackageTypeDef",
    "ClientListOriginEndpointsResponseOriginEndpointsHlsPackageEncryptionSpekeKeyProviderTypeDef",
    "ClientListOriginEndpointsResponseOriginEndpointsHlsPackageEncryptionTypeDef",
    "ClientListOriginEndpointsResponseOriginEndpointsHlsPackageStreamSelectionTypeDef",
    "ClientListOriginEndpointsResponseOriginEndpointsHlsPackageTypeDef",
    "ClientListOriginEndpointsResponseOriginEndpointsMssPackageEncryptionSpekeKeyProviderTypeDef",
    "ClientListOriginEndpointsResponseOriginEndpointsMssPackageEncryptionTypeDef",
    "ClientListOriginEndpointsResponseOriginEndpointsMssPackageStreamSelectionTypeDef",
    "ClientListOriginEndpointsResponseOriginEndpointsMssPackageTypeDef",
    "ClientListOriginEndpointsResponseOriginEndpointsTypeDef",
    "ClientListOriginEndpointsResponseTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientRotateChannelCredentialsResponseHlsIngestIngestEndpointsTypeDef",
    "ClientRotateChannelCredentialsResponseHlsIngestTypeDef",
    "ClientRotateChannelCredentialsResponseTypeDef",
    "ClientRotateIngestEndpointCredentialsResponseHlsIngestIngestEndpointsTypeDef",
    "ClientRotateIngestEndpointCredentialsResponseHlsIngestTypeDef",
    "ClientRotateIngestEndpointCredentialsResponseTypeDef",
    "ClientUpdateChannelResponseHlsIngestIngestEndpointsTypeDef",
    "ClientUpdateChannelResponseHlsIngestTypeDef",
    "ClientUpdateChannelResponseTypeDef",
    "ClientUpdateOriginEndpointAuthorizationTypeDef",
    "ClientUpdateOriginEndpointCmafPackageEncryptionSpekeKeyProviderTypeDef",
    "ClientUpdateOriginEndpointCmafPackageEncryptionTypeDef",
    "ClientUpdateOriginEndpointCmafPackageHlsManifestsTypeDef",
    "ClientUpdateOriginEndpointCmafPackageStreamSelectionTypeDef",
    "ClientUpdateOriginEndpointCmafPackageTypeDef",
    "ClientUpdateOriginEndpointDashPackageEncryptionSpekeKeyProviderTypeDef",
    "ClientUpdateOriginEndpointDashPackageEncryptionTypeDef",
    "ClientUpdateOriginEndpointDashPackageStreamSelectionTypeDef",
    "ClientUpdateOriginEndpointDashPackageTypeDef",
    "ClientUpdateOriginEndpointHlsPackageEncryptionSpekeKeyProviderTypeDef",
    "ClientUpdateOriginEndpointHlsPackageEncryptionTypeDef",
    "ClientUpdateOriginEndpointHlsPackageStreamSelectionTypeDef",
    "ClientUpdateOriginEndpointHlsPackageTypeDef",
    "ClientUpdateOriginEndpointMssPackageEncryptionSpekeKeyProviderTypeDef",
    "ClientUpdateOriginEndpointMssPackageEncryptionTypeDef",
    "ClientUpdateOriginEndpointMssPackageStreamSelectionTypeDef",
    "ClientUpdateOriginEndpointMssPackageTypeDef",
    "ClientUpdateOriginEndpointResponseAuthorizationTypeDef",
    "ClientUpdateOriginEndpointResponseCmafPackageEncryptionSpekeKeyProviderTypeDef",
    "ClientUpdateOriginEndpointResponseCmafPackageEncryptionTypeDef",
    "ClientUpdateOriginEndpointResponseCmafPackageHlsManifestsTypeDef",
    "ClientUpdateOriginEndpointResponseCmafPackageStreamSelectionTypeDef",
    "ClientUpdateOriginEndpointResponseCmafPackageTypeDef",
    "ClientUpdateOriginEndpointResponseDashPackageEncryptionSpekeKeyProviderTypeDef",
    "ClientUpdateOriginEndpointResponseDashPackageEncryptionTypeDef",
    "ClientUpdateOriginEndpointResponseDashPackageStreamSelectionTypeDef",
    "ClientUpdateOriginEndpointResponseDashPackageTypeDef",
    "ClientUpdateOriginEndpointResponseHlsPackageEncryptionSpekeKeyProviderTypeDef",
    "ClientUpdateOriginEndpointResponseHlsPackageEncryptionTypeDef",
    "ClientUpdateOriginEndpointResponseHlsPackageStreamSelectionTypeDef",
    "ClientUpdateOriginEndpointResponseHlsPackageTypeDef",
    "ClientUpdateOriginEndpointResponseMssPackageEncryptionSpekeKeyProviderTypeDef",
    "ClientUpdateOriginEndpointResponseMssPackageEncryptionTypeDef",
    "ClientUpdateOriginEndpointResponseMssPackageStreamSelectionTypeDef",
    "ClientUpdateOriginEndpointResponseMssPackageTypeDef",
    "ClientUpdateOriginEndpointResponseTypeDef",
    "IngestEndpointTypeDef",
    "HlsIngestTypeDef",
    "ChannelTypeDef",
    "ListChannelsResponseTypeDef",
    "S3DestinationTypeDef",
    "HarvestJobTypeDef",
    "ListHarvestJobsResponseTypeDef",
    "AuthorizationTypeDef",
    "SpekeKeyProviderTypeDef",
    "CmafEncryptionTypeDef",
    "HlsManifestTypeDef",
    "StreamSelectionTypeDef",
    "CmafPackageTypeDef",
    "DashEncryptionTypeDef",
    "DashPackageTypeDef",
    "HlsEncryptionTypeDef",
    "HlsPackageTypeDef",
    "MssEncryptionTypeDef",
    "MssPackageTypeDef",
    "OriginEndpointTypeDef",
    "ListOriginEndpointsResponseTypeDef",
    "PaginatorConfigTypeDef",
)

ClientCreateChannelResponseHlsIngestIngestEndpointsTypeDef = TypedDict(
    "ClientCreateChannelResponseHlsIngestIngestEndpointsTypeDef",
    {"Id": str, "Password": str, "Url": str, "Username": str},
    total=False,
)

ClientCreateChannelResponseHlsIngestTypeDef = TypedDict(
    "ClientCreateChannelResponseHlsIngestTypeDef",
    {"IngestEndpoints": List[ClientCreateChannelResponseHlsIngestIngestEndpointsTypeDef]},
    total=False,
)

ClientCreateChannelResponseTypeDef = TypedDict(
    "ClientCreateChannelResponseTypeDef",
    {
        "Arn": str,
        "Description": str,
        "HlsIngest": ClientCreateChannelResponseHlsIngestTypeDef,
        "Id": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

ClientCreateHarvestJobResponseS3DestinationTypeDef = TypedDict(
    "ClientCreateHarvestJobResponseS3DestinationTypeDef",
    {"BucketName": str, "ManifestKey": str, "RoleArn": str},
    total=False,
)

ClientCreateHarvestJobResponseTypeDef = TypedDict(
    "ClientCreateHarvestJobResponseTypeDef",
    {
        "Arn": str,
        "ChannelId": str,
        "CreatedAt": str,
        "EndTime": str,
        "Id": str,
        "OriginEndpointId": str,
        "S3Destination": ClientCreateHarvestJobResponseS3DestinationTypeDef,
        "StartTime": str,
        "Status": Literal["IN_PROGRESS", "SUCCEEDED", "FAILED"],
    },
    total=False,
)

ClientCreateHarvestJobS3DestinationTypeDef = TypedDict(
    "ClientCreateHarvestJobS3DestinationTypeDef",
    {"BucketName": str, "ManifestKey": str, "RoleArn": str},
)

ClientCreateOriginEndpointAuthorizationTypeDef = TypedDict(
    "ClientCreateOriginEndpointAuthorizationTypeDef",
    {"CdnIdentifierSecret": str, "SecretsRoleArn": str},
)

_RequiredClientCreateOriginEndpointCmafPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "_RequiredClientCreateOriginEndpointCmafPackageEncryptionSpekeKeyProviderTypeDef",
    {"ResourceId": str, "RoleArn": str, "SystemIds": List[str]},
)
_OptionalClientCreateOriginEndpointCmafPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "_OptionalClientCreateOriginEndpointCmafPackageEncryptionSpekeKeyProviderTypeDef",
    {"CertificateArn": str, "Url": str},
    total=False,
)


class ClientCreateOriginEndpointCmafPackageEncryptionSpekeKeyProviderTypeDef(
    _RequiredClientCreateOriginEndpointCmafPackageEncryptionSpekeKeyProviderTypeDef,
    _OptionalClientCreateOriginEndpointCmafPackageEncryptionSpekeKeyProviderTypeDef,
):
    pass


_RequiredClientCreateOriginEndpointCmafPackageEncryptionTypeDef = TypedDict(
    "_RequiredClientCreateOriginEndpointCmafPackageEncryptionTypeDef",
    {"SpekeKeyProvider": ClientCreateOriginEndpointCmafPackageEncryptionSpekeKeyProviderTypeDef},
)
_OptionalClientCreateOriginEndpointCmafPackageEncryptionTypeDef = TypedDict(
    "_OptionalClientCreateOriginEndpointCmafPackageEncryptionTypeDef",
    {"KeyRotationIntervalSeconds": int},
    total=False,
)


class ClientCreateOriginEndpointCmafPackageEncryptionTypeDef(
    _RequiredClientCreateOriginEndpointCmafPackageEncryptionTypeDef,
    _OptionalClientCreateOriginEndpointCmafPackageEncryptionTypeDef,
):
    pass


ClientCreateOriginEndpointCmafPackageHlsManifestsTypeDef = TypedDict(
    "ClientCreateOriginEndpointCmafPackageHlsManifestsTypeDef",
    {
        "AdMarkers": Literal["NONE", "SCTE35_ENHANCED", "PASSTHROUGH"],
        "AdTriggers": List[
            Literal[
                "SPLICE_INSERT",
                "BREAK",
                "PROVIDER_ADVERTISEMENT",
                "DISTRIBUTOR_ADVERTISEMENT",
                "PROVIDER_PLACEMENT_OPPORTUNITY",
                "DISTRIBUTOR_PLACEMENT_OPPORTUNITY",
                "PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY",
                "DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY",
            ]
        ],
        "AdsOnDeliveryRestrictions": Literal["NONE", "RESTRICTED", "UNRESTRICTED", "BOTH"],
        "Id": str,
        "IncludeIframeOnlyStream": bool,
        "ManifestName": str,
        "PlaylistType": Literal["NONE", "EVENT", "VOD"],
        "PlaylistWindowSeconds": int,
        "ProgramDateTimeIntervalSeconds": int,
    },
    total=False,
)

ClientCreateOriginEndpointCmafPackageStreamSelectionTypeDef = TypedDict(
    "ClientCreateOriginEndpointCmafPackageStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)

ClientCreateOriginEndpointCmafPackageTypeDef = TypedDict(
    "ClientCreateOriginEndpointCmafPackageTypeDef",
    {
        "Encryption": ClientCreateOriginEndpointCmafPackageEncryptionTypeDef,
        "HlsManifests": List[ClientCreateOriginEndpointCmafPackageHlsManifestsTypeDef],
        "SegmentDurationSeconds": int,
        "SegmentPrefix": str,
        "StreamSelection": ClientCreateOriginEndpointCmafPackageStreamSelectionTypeDef,
    },
    total=False,
)

ClientCreateOriginEndpointDashPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "ClientCreateOriginEndpointDashPackageEncryptionSpekeKeyProviderTypeDef",
    {"CertificateArn": str, "ResourceId": str, "RoleArn": str, "SystemIds": List[str], "Url": str},
    total=False,
)

ClientCreateOriginEndpointDashPackageEncryptionTypeDef = TypedDict(
    "ClientCreateOriginEndpointDashPackageEncryptionTypeDef",
    {
        "KeyRotationIntervalSeconds": int,
        "SpekeKeyProvider": ClientCreateOriginEndpointDashPackageEncryptionSpekeKeyProviderTypeDef,
    },
    total=False,
)

ClientCreateOriginEndpointDashPackageStreamSelectionTypeDef = TypedDict(
    "ClientCreateOriginEndpointDashPackageStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)

ClientCreateOriginEndpointDashPackageTypeDef = TypedDict(
    "ClientCreateOriginEndpointDashPackageTypeDef",
    {
        "AdTriggers": List[
            Literal[
                "SPLICE_INSERT",
                "BREAK",
                "PROVIDER_ADVERTISEMENT",
                "DISTRIBUTOR_ADVERTISEMENT",
                "PROVIDER_PLACEMENT_OPPORTUNITY",
                "DISTRIBUTOR_PLACEMENT_OPPORTUNITY",
                "PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY",
                "DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY",
            ]
        ],
        "AdsOnDeliveryRestrictions": Literal["NONE", "RESTRICTED", "UNRESTRICTED", "BOTH"],
        "Encryption": ClientCreateOriginEndpointDashPackageEncryptionTypeDef,
        "ManifestLayout": Literal["FULL", "COMPACT"],
        "ManifestWindowSeconds": int,
        "MinBufferTimeSeconds": int,
        "MinUpdatePeriodSeconds": int,
        "PeriodTriggers": List[str],
        "Profile": Literal["NONE", "HBBTV_1_5"],
        "SegmentDurationSeconds": int,
        "SegmentTemplateFormat": Literal[
            "NUMBER_WITH_TIMELINE", "TIME_WITH_TIMELINE", "NUMBER_WITH_DURATION"
        ],
        "StreamSelection": ClientCreateOriginEndpointDashPackageStreamSelectionTypeDef,
        "SuggestedPresentationDelaySeconds": int,
    },
    total=False,
)

ClientCreateOriginEndpointHlsPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "ClientCreateOriginEndpointHlsPackageEncryptionSpekeKeyProviderTypeDef",
    {"CertificateArn": str, "ResourceId": str, "RoleArn": str, "SystemIds": List[str], "Url": str},
    total=False,
)

ClientCreateOriginEndpointHlsPackageEncryptionTypeDef = TypedDict(
    "ClientCreateOriginEndpointHlsPackageEncryptionTypeDef",
    {
        "ConstantInitializationVector": str,
        "EncryptionMethod": Literal["AES_128", "SAMPLE_AES"],
        "KeyRotationIntervalSeconds": int,
        "RepeatExtXKey": bool,
        "SpekeKeyProvider": ClientCreateOriginEndpointHlsPackageEncryptionSpekeKeyProviderTypeDef,
    },
    total=False,
)

ClientCreateOriginEndpointHlsPackageStreamSelectionTypeDef = TypedDict(
    "ClientCreateOriginEndpointHlsPackageStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)

ClientCreateOriginEndpointHlsPackageTypeDef = TypedDict(
    "ClientCreateOriginEndpointHlsPackageTypeDef",
    {
        "AdMarkers": Literal["NONE", "SCTE35_ENHANCED", "PASSTHROUGH"],
        "AdTriggers": List[
            Literal[
                "SPLICE_INSERT",
                "BREAK",
                "PROVIDER_ADVERTISEMENT",
                "DISTRIBUTOR_ADVERTISEMENT",
                "PROVIDER_PLACEMENT_OPPORTUNITY",
                "DISTRIBUTOR_PLACEMENT_OPPORTUNITY",
                "PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY",
                "DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY",
            ]
        ],
        "AdsOnDeliveryRestrictions": Literal["NONE", "RESTRICTED", "UNRESTRICTED", "BOTH"],
        "Encryption": ClientCreateOriginEndpointHlsPackageEncryptionTypeDef,
        "IncludeIframeOnlyStream": bool,
        "PlaylistType": Literal["NONE", "EVENT", "VOD"],
        "PlaylistWindowSeconds": int,
        "ProgramDateTimeIntervalSeconds": int,
        "SegmentDurationSeconds": int,
        "StreamSelection": ClientCreateOriginEndpointHlsPackageStreamSelectionTypeDef,
        "UseAudioRenditionGroup": bool,
    },
    total=False,
)

_RequiredClientCreateOriginEndpointMssPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "_RequiredClientCreateOriginEndpointMssPackageEncryptionSpekeKeyProviderTypeDef",
    {"ResourceId": str, "RoleArn": str, "SystemIds": List[str]},
)
_OptionalClientCreateOriginEndpointMssPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "_OptionalClientCreateOriginEndpointMssPackageEncryptionSpekeKeyProviderTypeDef",
    {"CertificateArn": str, "Url": str},
    total=False,
)


class ClientCreateOriginEndpointMssPackageEncryptionSpekeKeyProviderTypeDef(
    _RequiredClientCreateOriginEndpointMssPackageEncryptionSpekeKeyProviderTypeDef,
    _OptionalClientCreateOriginEndpointMssPackageEncryptionSpekeKeyProviderTypeDef,
):
    pass


ClientCreateOriginEndpointMssPackageEncryptionTypeDef = TypedDict(
    "ClientCreateOriginEndpointMssPackageEncryptionTypeDef",
    {"SpekeKeyProvider": ClientCreateOriginEndpointMssPackageEncryptionSpekeKeyProviderTypeDef},
)

ClientCreateOriginEndpointMssPackageStreamSelectionTypeDef = TypedDict(
    "ClientCreateOriginEndpointMssPackageStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)

ClientCreateOriginEndpointMssPackageTypeDef = TypedDict(
    "ClientCreateOriginEndpointMssPackageTypeDef",
    {
        "Encryption": ClientCreateOriginEndpointMssPackageEncryptionTypeDef,
        "ManifestWindowSeconds": int,
        "SegmentDurationSeconds": int,
        "StreamSelection": ClientCreateOriginEndpointMssPackageStreamSelectionTypeDef,
    },
    total=False,
)

ClientCreateOriginEndpointResponseAuthorizationTypeDef = TypedDict(
    "ClientCreateOriginEndpointResponseAuthorizationTypeDef",
    {"CdnIdentifierSecret": str, "SecretsRoleArn": str},
    total=False,
)

ClientCreateOriginEndpointResponseCmafPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "ClientCreateOriginEndpointResponseCmafPackageEncryptionSpekeKeyProviderTypeDef",
    {"CertificateArn": str, "ResourceId": str, "RoleArn": str, "SystemIds": List[str], "Url": str},
    total=False,
)

ClientCreateOriginEndpointResponseCmafPackageEncryptionTypeDef = TypedDict(
    "ClientCreateOriginEndpointResponseCmafPackageEncryptionTypeDef",
    {
        "KeyRotationIntervalSeconds": int,
        "SpekeKeyProvider": ClientCreateOriginEndpointResponseCmafPackageEncryptionSpekeKeyProviderTypeDef,
    },
    total=False,
)

ClientCreateOriginEndpointResponseCmafPackageHlsManifestsTypeDef = TypedDict(
    "ClientCreateOriginEndpointResponseCmafPackageHlsManifestsTypeDef",
    {
        "AdMarkers": Literal["NONE", "SCTE35_ENHANCED", "PASSTHROUGH"],
        "Id": str,
        "IncludeIframeOnlyStream": bool,
        "ManifestName": str,
        "PlaylistType": Literal["NONE", "EVENT", "VOD"],
        "PlaylistWindowSeconds": int,
        "ProgramDateTimeIntervalSeconds": int,
        "Url": str,
    },
    total=False,
)

ClientCreateOriginEndpointResponseCmafPackageStreamSelectionTypeDef = TypedDict(
    "ClientCreateOriginEndpointResponseCmafPackageStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)

ClientCreateOriginEndpointResponseCmafPackageTypeDef = TypedDict(
    "ClientCreateOriginEndpointResponseCmafPackageTypeDef",
    {
        "Encryption": ClientCreateOriginEndpointResponseCmafPackageEncryptionTypeDef,
        "HlsManifests": List[ClientCreateOriginEndpointResponseCmafPackageHlsManifestsTypeDef],
        "SegmentDurationSeconds": int,
        "SegmentPrefix": str,
        "StreamSelection": ClientCreateOriginEndpointResponseCmafPackageStreamSelectionTypeDef,
    },
    total=False,
)

ClientCreateOriginEndpointResponseDashPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "ClientCreateOriginEndpointResponseDashPackageEncryptionSpekeKeyProviderTypeDef",
    {"CertificateArn": str, "ResourceId": str, "RoleArn": str, "SystemIds": List[str], "Url": str},
    total=False,
)

ClientCreateOriginEndpointResponseDashPackageEncryptionTypeDef = TypedDict(
    "ClientCreateOriginEndpointResponseDashPackageEncryptionTypeDef",
    {
        "KeyRotationIntervalSeconds": int,
        "SpekeKeyProvider": ClientCreateOriginEndpointResponseDashPackageEncryptionSpekeKeyProviderTypeDef,
    },
    total=False,
)

ClientCreateOriginEndpointResponseDashPackageStreamSelectionTypeDef = TypedDict(
    "ClientCreateOriginEndpointResponseDashPackageStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)

ClientCreateOriginEndpointResponseDashPackageTypeDef = TypedDict(
    "ClientCreateOriginEndpointResponseDashPackageTypeDef",
    {
        "AdTriggers": List[
            Literal[
                "SPLICE_INSERT",
                "BREAK",
                "PROVIDER_ADVERTISEMENT",
                "DISTRIBUTOR_ADVERTISEMENT",
                "PROVIDER_PLACEMENT_OPPORTUNITY",
                "DISTRIBUTOR_PLACEMENT_OPPORTUNITY",
                "PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY",
                "DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY",
            ]
        ],
        "AdsOnDeliveryRestrictions": Literal["NONE", "RESTRICTED", "UNRESTRICTED", "BOTH"],
        "Encryption": ClientCreateOriginEndpointResponseDashPackageEncryptionTypeDef,
        "ManifestLayout": Literal["FULL", "COMPACT"],
        "ManifestWindowSeconds": int,
        "MinBufferTimeSeconds": int,
        "MinUpdatePeriodSeconds": int,
        "PeriodTriggers": List[str],
        "Profile": Literal["NONE", "HBBTV_1_5"],
        "SegmentDurationSeconds": int,
        "SegmentTemplateFormat": Literal[
            "NUMBER_WITH_TIMELINE", "TIME_WITH_TIMELINE", "NUMBER_WITH_DURATION"
        ],
        "StreamSelection": ClientCreateOriginEndpointResponseDashPackageStreamSelectionTypeDef,
        "SuggestedPresentationDelaySeconds": int,
    },
    total=False,
)

ClientCreateOriginEndpointResponseHlsPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "ClientCreateOriginEndpointResponseHlsPackageEncryptionSpekeKeyProviderTypeDef",
    {"CertificateArn": str, "ResourceId": str, "RoleArn": str, "SystemIds": List[str], "Url": str},
    total=False,
)

ClientCreateOriginEndpointResponseHlsPackageEncryptionTypeDef = TypedDict(
    "ClientCreateOriginEndpointResponseHlsPackageEncryptionTypeDef",
    {
        "ConstantInitializationVector": str,
        "EncryptionMethod": Literal["AES_128", "SAMPLE_AES"],
        "KeyRotationIntervalSeconds": int,
        "RepeatExtXKey": bool,
        "SpekeKeyProvider": ClientCreateOriginEndpointResponseHlsPackageEncryptionSpekeKeyProviderTypeDef,
    },
    total=False,
)

ClientCreateOriginEndpointResponseHlsPackageStreamSelectionTypeDef = TypedDict(
    "ClientCreateOriginEndpointResponseHlsPackageStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)

ClientCreateOriginEndpointResponseHlsPackageTypeDef = TypedDict(
    "ClientCreateOriginEndpointResponseHlsPackageTypeDef",
    {
        "AdMarkers": Literal["NONE", "SCTE35_ENHANCED", "PASSTHROUGH"],
        "AdTriggers": List[
            Literal[
                "SPLICE_INSERT",
                "BREAK",
                "PROVIDER_ADVERTISEMENT",
                "DISTRIBUTOR_ADVERTISEMENT",
                "PROVIDER_PLACEMENT_OPPORTUNITY",
                "DISTRIBUTOR_PLACEMENT_OPPORTUNITY",
                "PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY",
                "DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY",
            ]
        ],
        "AdsOnDeliveryRestrictions": Literal["NONE", "RESTRICTED", "UNRESTRICTED", "BOTH"],
        "Encryption": ClientCreateOriginEndpointResponseHlsPackageEncryptionTypeDef,
        "IncludeIframeOnlyStream": bool,
        "PlaylistType": Literal["NONE", "EVENT", "VOD"],
        "PlaylistWindowSeconds": int,
        "ProgramDateTimeIntervalSeconds": int,
        "SegmentDurationSeconds": int,
        "StreamSelection": ClientCreateOriginEndpointResponseHlsPackageStreamSelectionTypeDef,
        "UseAudioRenditionGroup": bool,
    },
    total=False,
)

ClientCreateOriginEndpointResponseMssPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "ClientCreateOriginEndpointResponseMssPackageEncryptionSpekeKeyProviderTypeDef",
    {"CertificateArn": str, "ResourceId": str, "RoleArn": str, "SystemIds": List[str], "Url": str},
    total=False,
)

ClientCreateOriginEndpointResponseMssPackageEncryptionTypeDef = TypedDict(
    "ClientCreateOriginEndpointResponseMssPackageEncryptionTypeDef",
    {
        "SpekeKeyProvider": ClientCreateOriginEndpointResponseMssPackageEncryptionSpekeKeyProviderTypeDef
    },
    total=False,
)

ClientCreateOriginEndpointResponseMssPackageStreamSelectionTypeDef = TypedDict(
    "ClientCreateOriginEndpointResponseMssPackageStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)

ClientCreateOriginEndpointResponseMssPackageTypeDef = TypedDict(
    "ClientCreateOriginEndpointResponseMssPackageTypeDef",
    {
        "Encryption": ClientCreateOriginEndpointResponseMssPackageEncryptionTypeDef,
        "ManifestWindowSeconds": int,
        "SegmentDurationSeconds": int,
        "StreamSelection": ClientCreateOriginEndpointResponseMssPackageStreamSelectionTypeDef,
    },
    total=False,
)

ClientCreateOriginEndpointResponseTypeDef = TypedDict(
    "ClientCreateOriginEndpointResponseTypeDef",
    {
        "Arn": str,
        "Authorization": ClientCreateOriginEndpointResponseAuthorizationTypeDef,
        "ChannelId": str,
        "CmafPackage": ClientCreateOriginEndpointResponseCmafPackageTypeDef,
        "DashPackage": ClientCreateOriginEndpointResponseDashPackageTypeDef,
        "Description": str,
        "HlsPackage": ClientCreateOriginEndpointResponseHlsPackageTypeDef,
        "Id": str,
        "ManifestName": str,
        "MssPackage": ClientCreateOriginEndpointResponseMssPackageTypeDef,
        "Origination": Literal["ALLOW", "DENY"],
        "StartoverWindowSeconds": int,
        "Tags": Dict[str, str],
        "TimeDelaySeconds": int,
        "Url": str,
        "Whitelist": List[str],
    },
    total=False,
)

ClientDescribeChannelResponseHlsIngestIngestEndpointsTypeDef = TypedDict(
    "ClientDescribeChannelResponseHlsIngestIngestEndpointsTypeDef",
    {"Id": str, "Password": str, "Url": str, "Username": str},
    total=False,
)

ClientDescribeChannelResponseHlsIngestTypeDef = TypedDict(
    "ClientDescribeChannelResponseHlsIngestTypeDef",
    {"IngestEndpoints": List[ClientDescribeChannelResponseHlsIngestIngestEndpointsTypeDef]},
    total=False,
)

ClientDescribeChannelResponseTypeDef = TypedDict(
    "ClientDescribeChannelResponseTypeDef",
    {
        "Arn": str,
        "Description": str,
        "HlsIngest": ClientDescribeChannelResponseHlsIngestTypeDef,
        "Id": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

ClientDescribeHarvestJobResponseS3DestinationTypeDef = TypedDict(
    "ClientDescribeHarvestJobResponseS3DestinationTypeDef",
    {"BucketName": str, "ManifestKey": str, "RoleArn": str},
    total=False,
)

ClientDescribeHarvestJobResponseTypeDef = TypedDict(
    "ClientDescribeHarvestJobResponseTypeDef",
    {
        "Arn": str,
        "ChannelId": str,
        "CreatedAt": str,
        "EndTime": str,
        "Id": str,
        "OriginEndpointId": str,
        "S3Destination": ClientDescribeHarvestJobResponseS3DestinationTypeDef,
        "StartTime": str,
        "Status": Literal["IN_PROGRESS", "SUCCEEDED", "FAILED"],
    },
    total=False,
)

ClientDescribeOriginEndpointResponseAuthorizationTypeDef = TypedDict(
    "ClientDescribeOriginEndpointResponseAuthorizationTypeDef",
    {"CdnIdentifierSecret": str, "SecretsRoleArn": str},
    total=False,
)

ClientDescribeOriginEndpointResponseCmafPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "ClientDescribeOriginEndpointResponseCmafPackageEncryptionSpekeKeyProviderTypeDef",
    {"CertificateArn": str, "ResourceId": str, "RoleArn": str, "SystemIds": List[str], "Url": str},
    total=False,
)

ClientDescribeOriginEndpointResponseCmafPackageEncryptionTypeDef = TypedDict(
    "ClientDescribeOriginEndpointResponseCmafPackageEncryptionTypeDef",
    {
        "KeyRotationIntervalSeconds": int,
        "SpekeKeyProvider": ClientDescribeOriginEndpointResponseCmafPackageEncryptionSpekeKeyProviderTypeDef,
    },
    total=False,
)

ClientDescribeOriginEndpointResponseCmafPackageHlsManifestsTypeDef = TypedDict(
    "ClientDescribeOriginEndpointResponseCmafPackageHlsManifestsTypeDef",
    {
        "AdMarkers": Literal["NONE", "SCTE35_ENHANCED", "PASSTHROUGH"],
        "Id": str,
        "IncludeIframeOnlyStream": bool,
        "ManifestName": str,
        "PlaylistType": Literal["NONE", "EVENT", "VOD"],
        "PlaylistWindowSeconds": int,
        "ProgramDateTimeIntervalSeconds": int,
        "Url": str,
    },
    total=False,
)

ClientDescribeOriginEndpointResponseCmafPackageStreamSelectionTypeDef = TypedDict(
    "ClientDescribeOriginEndpointResponseCmafPackageStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)

ClientDescribeOriginEndpointResponseCmafPackageTypeDef = TypedDict(
    "ClientDescribeOriginEndpointResponseCmafPackageTypeDef",
    {
        "Encryption": ClientDescribeOriginEndpointResponseCmafPackageEncryptionTypeDef,
        "HlsManifests": List[ClientDescribeOriginEndpointResponseCmafPackageHlsManifestsTypeDef],
        "SegmentDurationSeconds": int,
        "SegmentPrefix": str,
        "StreamSelection": ClientDescribeOriginEndpointResponseCmafPackageStreamSelectionTypeDef,
    },
    total=False,
)

ClientDescribeOriginEndpointResponseDashPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "ClientDescribeOriginEndpointResponseDashPackageEncryptionSpekeKeyProviderTypeDef",
    {"CertificateArn": str, "ResourceId": str, "RoleArn": str, "SystemIds": List[str], "Url": str},
    total=False,
)

ClientDescribeOriginEndpointResponseDashPackageEncryptionTypeDef = TypedDict(
    "ClientDescribeOriginEndpointResponseDashPackageEncryptionTypeDef",
    {
        "KeyRotationIntervalSeconds": int,
        "SpekeKeyProvider": ClientDescribeOriginEndpointResponseDashPackageEncryptionSpekeKeyProviderTypeDef,
    },
    total=False,
)

ClientDescribeOriginEndpointResponseDashPackageStreamSelectionTypeDef = TypedDict(
    "ClientDescribeOriginEndpointResponseDashPackageStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)

ClientDescribeOriginEndpointResponseDashPackageTypeDef = TypedDict(
    "ClientDescribeOriginEndpointResponseDashPackageTypeDef",
    {
        "AdTriggers": List[
            Literal[
                "SPLICE_INSERT",
                "BREAK",
                "PROVIDER_ADVERTISEMENT",
                "DISTRIBUTOR_ADVERTISEMENT",
                "PROVIDER_PLACEMENT_OPPORTUNITY",
                "DISTRIBUTOR_PLACEMENT_OPPORTUNITY",
                "PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY",
                "DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY",
            ]
        ],
        "AdsOnDeliveryRestrictions": Literal["NONE", "RESTRICTED", "UNRESTRICTED", "BOTH"],
        "Encryption": ClientDescribeOriginEndpointResponseDashPackageEncryptionTypeDef,
        "ManifestLayout": Literal["FULL", "COMPACT"],
        "ManifestWindowSeconds": int,
        "MinBufferTimeSeconds": int,
        "MinUpdatePeriodSeconds": int,
        "PeriodTriggers": List[str],
        "Profile": Literal["NONE", "HBBTV_1_5"],
        "SegmentDurationSeconds": int,
        "SegmentTemplateFormat": Literal[
            "NUMBER_WITH_TIMELINE", "TIME_WITH_TIMELINE", "NUMBER_WITH_DURATION"
        ],
        "StreamSelection": ClientDescribeOriginEndpointResponseDashPackageStreamSelectionTypeDef,
        "SuggestedPresentationDelaySeconds": int,
    },
    total=False,
)

ClientDescribeOriginEndpointResponseHlsPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "ClientDescribeOriginEndpointResponseHlsPackageEncryptionSpekeKeyProviderTypeDef",
    {"CertificateArn": str, "ResourceId": str, "RoleArn": str, "SystemIds": List[str], "Url": str},
    total=False,
)

ClientDescribeOriginEndpointResponseHlsPackageEncryptionTypeDef = TypedDict(
    "ClientDescribeOriginEndpointResponseHlsPackageEncryptionTypeDef",
    {
        "ConstantInitializationVector": str,
        "EncryptionMethod": Literal["AES_128", "SAMPLE_AES"],
        "KeyRotationIntervalSeconds": int,
        "RepeatExtXKey": bool,
        "SpekeKeyProvider": ClientDescribeOriginEndpointResponseHlsPackageEncryptionSpekeKeyProviderTypeDef,
    },
    total=False,
)

ClientDescribeOriginEndpointResponseHlsPackageStreamSelectionTypeDef = TypedDict(
    "ClientDescribeOriginEndpointResponseHlsPackageStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)

ClientDescribeOriginEndpointResponseHlsPackageTypeDef = TypedDict(
    "ClientDescribeOriginEndpointResponseHlsPackageTypeDef",
    {
        "AdMarkers": Literal["NONE", "SCTE35_ENHANCED", "PASSTHROUGH"],
        "AdTriggers": List[
            Literal[
                "SPLICE_INSERT",
                "BREAK",
                "PROVIDER_ADVERTISEMENT",
                "DISTRIBUTOR_ADVERTISEMENT",
                "PROVIDER_PLACEMENT_OPPORTUNITY",
                "DISTRIBUTOR_PLACEMENT_OPPORTUNITY",
                "PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY",
                "DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY",
            ]
        ],
        "AdsOnDeliveryRestrictions": Literal["NONE", "RESTRICTED", "UNRESTRICTED", "BOTH"],
        "Encryption": ClientDescribeOriginEndpointResponseHlsPackageEncryptionTypeDef,
        "IncludeIframeOnlyStream": bool,
        "PlaylistType": Literal["NONE", "EVENT", "VOD"],
        "PlaylistWindowSeconds": int,
        "ProgramDateTimeIntervalSeconds": int,
        "SegmentDurationSeconds": int,
        "StreamSelection": ClientDescribeOriginEndpointResponseHlsPackageStreamSelectionTypeDef,
        "UseAudioRenditionGroup": bool,
    },
    total=False,
)

ClientDescribeOriginEndpointResponseMssPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "ClientDescribeOriginEndpointResponseMssPackageEncryptionSpekeKeyProviderTypeDef",
    {"CertificateArn": str, "ResourceId": str, "RoleArn": str, "SystemIds": List[str], "Url": str},
    total=False,
)

ClientDescribeOriginEndpointResponseMssPackageEncryptionTypeDef = TypedDict(
    "ClientDescribeOriginEndpointResponseMssPackageEncryptionTypeDef",
    {
        "SpekeKeyProvider": ClientDescribeOriginEndpointResponseMssPackageEncryptionSpekeKeyProviderTypeDef
    },
    total=False,
)

ClientDescribeOriginEndpointResponseMssPackageStreamSelectionTypeDef = TypedDict(
    "ClientDescribeOriginEndpointResponseMssPackageStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)

ClientDescribeOriginEndpointResponseMssPackageTypeDef = TypedDict(
    "ClientDescribeOriginEndpointResponseMssPackageTypeDef",
    {
        "Encryption": ClientDescribeOriginEndpointResponseMssPackageEncryptionTypeDef,
        "ManifestWindowSeconds": int,
        "SegmentDurationSeconds": int,
        "StreamSelection": ClientDescribeOriginEndpointResponseMssPackageStreamSelectionTypeDef,
    },
    total=False,
)

ClientDescribeOriginEndpointResponseTypeDef = TypedDict(
    "ClientDescribeOriginEndpointResponseTypeDef",
    {
        "Arn": str,
        "Authorization": ClientDescribeOriginEndpointResponseAuthorizationTypeDef,
        "ChannelId": str,
        "CmafPackage": ClientDescribeOriginEndpointResponseCmafPackageTypeDef,
        "DashPackage": ClientDescribeOriginEndpointResponseDashPackageTypeDef,
        "Description": str,
        "HlsPackage": ClientDescribeOriginEndpointResponseHlsPackageTypeDef,
        "Id": str,
        "ManifestName": str,
        "MssPackage": ClientDescribeOriginEndpointResponseMssPackageTypeDef,
        "Origination": Literal["ALLOW", "DENY"],
        "StartoverWindowSeconds": int,
        "Tags": Dict[str, str],
        "TimeDelaySeconds": int,
        "Url": str,
        "Whitelist": List[str],
    },
    total=False,
)

ClientListChannelsResponseChannelsHlsIngestIngestEndpointsTypeDef = TypedDict(
    "ClientListChannelsResponseChannelsHlsIngestIngestEndpointsTypeDef",
    {"Id": str, "Password": str, "Url": str, "Username": str},
    total=False,
)

ClientListChannelsResponseChannelsHlsIngestTypeDef = TypedDict(
    "ClientListChannelsResponseChannelsHlsIngestTypeDef",
    {"IngestEndpoints": List[ClientListChannelsResponseChannelsHlsIngestIngestEndpointsTypeDef]},
    total=False,
)

ClientListChannelsResponseChannelsTypeDef = TypedDict(
    "ClientListChannelsResponseChannelsTypeDef",
    {
        "Arn": str,
        "Description": str,
        "HlsIngest": ClientListChannelsResponseChannelsHlsIngestTypeDef,
        "Id": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

ClientListChannelsResponseTypeDef = TypedDict(
    "ClientListChannelsResponseTypeDef",
    {"Channels": List[ClientListChannelsResponseChannelsTypeDef], "NextToken": str},
    total=False,
)

ClientListHarvestJobsResponseHarvestJobsS3DestinationTypeDef = TypedDict(
    "ClientListHarvestJobsResponseHarvestJobsS3DestinationTypeDef",
    {"BucketName": str, "ManifestKey": str, "RoleArn": str},
    total=False,
)

ClientListHarvestJobsResponseHarvestJobsTypeDef = TypedDict(
    "ClientListHarvestJobsResponseHarvestJobsTypeDef",
    {
        "Arn": str,
        "ChannelId": str,
        "CreatedAt": str,
        "EndTime": str,
        "Id": str,
        "OriginEndpointId": str,
        "S3Destination": ClientListHarvestJobsResponseHarvestJobsS3DestinationTypeDef,
        "StartTime": str,
        "Status": Literal["IN_PROGRESS", "SUCCEEDED", "FAILED"],
    },
    total=False,
)

ClientListHarvestJobsResponseTypeDef = TypedDict(
    "ClientListHarvestJobsResponseTypeDef",
    {"HarvestJobs": List[ClientListHarvestJobsResponseHarvestJobsTypeDef], "NextToken": str},
    total=False,
)

ClientListOriginEndpointsResponseOriginEndpointsAuthorizationTypeDef = TypedDict(
    "ClientListOriginEndpointsResponseOriginEndpointsAuthorizationTypeDef",
    {"CdnIdentifierSecret": str, "SecretsRoleArn": str},
    total=False,
)

ClientListOriginEndpointsResponseOriginEndpointsCmafPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "ClientListOriginEndpointsResponseOriginEndpointsCmafPackageEncryptionSpekeKeyProviderTypeDef",
    {"CertificateArn": str, "ResourceId": str, "RoleArn": str, "SystemIds": List[str], "Url": str},
    total=False,
)

ClientListOriginEndpointsResponseOriginEndpointsCmafPackageEncryptionTypeDef = TypedDict(
    "ClientListOriginEndpointsResponseOriginEndpointsCmafPackageEncryptionTypeDef",
    {
        "KeyRotationIntervalSeconds": int,
        "SpekeKeyProvider": ClientListOriginEndpointsResponseOriginEndpointsCmafPackageEncryptionSpekeKeyProviderTypeDef,
    },
    total=False,
)

ClientListOriginEndpointsResponseOriginEndpointsCmafPackageHlsManifestsTypeDef = TypedDict(
    "ClientListOriginEndpointsResponseOriginEndpointsCmafPackageHlsManifestsTypeDef",
    {
        "AdMarkers": Literal["NONE", "SCTE35_ENHANCED", "PASSTHROUGH"],
        "Id": str,
        "IncludeIframeOnlyStream": bool,
        "ManifestName": str,
        "PlaylistType": Literal["NONE", "EVENT", "VOD"],
        "PlaylistWindowSeconds": int,
        "ProgramDateTimeIntervalSeconds": int,
        "Url": str,
    },
    total=False,
)

ClientListOriginEndpointsResponseOriginEndpointsCmafPackageStreamSelectionTypeDef = TypedDict(
    "ClientListOriginEndpointsResponseOriginEndpointsCmafPackageStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)

ClientListOriginEndpointsResponseOriginEndpointsCmafPackageTypeDef = TypedDict(
    "ClientListOriginEndpointsResponseOriginEndpointsCmafPackageTypeDef",
    {
        "Encryption": ClientListOriginEndpointsResponseOriginEndpointsCmafPackageEncryptionTypeDef,
        "HlsManifests": List[
            ClientListOriginEndpointsResponseOriginEndpointsCmafPackageHlsManifestsTypeDef
        ],
        "SegmentDurationSeconds": int,
        "SegmentPrefix": str,
        "StreamSelection": ClientListOriginEndpointsResponseOriginEndpointsCmafPackageStreamSelectionTypeDef,
    },
    total=False,
)

ClientListOriginEndpointsResponseOriginEndpointsDashPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "ClientListOriginEndpointsResponseOriginEndpointsDashPackageEncryptionSpekeKeyProviderTypeDef",
    {"CertificateArn": str, "ResourceId": str, "RoleArn": str, "SystemIds": List[str], "Url": str},
    total=False,
)

ClientListOriginEndpointsResponseOriginEndpointsDashPackageEncryptionTypeDef = TypedDict(
    "ClientListOriginEndpointsResponseOriginEndpointsDashPackageEncryptionTypeDef",
    {
        "KeyRotationIntervalSeconds": int,
        "SpekeKeyProvider": ClientListOriginEndpointsResponseOriginEndpointsDashPackageEncryptionSpekeKeyProviderTypeDef,
    },
    total=False,
)

ClientListOriginEndpointsResponseOriginEndpointsDashPackageStreamSelectionTypeDef = TypedDict(
    "ClientListOriginEndpointsResponseOriginEndpointsDashPackageStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)

ClientListOriginEndpointsResponseOriginEndpointsDashPackageTypeDef = TypedDict(
    "ClientListOriginEndpointsResponseOriginEndpointsDashPackageTypeDef",
    {
        "AdTriggers": List[
            Literal[
                "SPLICE_INSERT",
                "BREAK",
                "PROVIDER_ADVERTISEMENT",
                "DISTRIBUTOR_ADVERTISEMENT",
                "PROVIDER_PLACEMENT_OPPORTUNITY",
                "DISTRIBUTOR_PLACEMENT_OPPORTUNITY",
                "PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY",
                "DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY",
            ]
        ],
        "AdsOnDeliveryRestrictions": Literal["NONE", "RESTRICTED", "UNRESTRICTED", "BOTH"],
        "Encryption": ClientListOriginEndpointsResponseOriginEndpointsDashPackageEncryptionTypeDef,
        "ManifestLayout": Literal["FULL", "COMPACT"],
        "ManifestWindowSeconds": int,
        "MinBufferTimeSeconds": int,
        "MinUpdatePeriodSeconds": int,
        "PeriodTriggers": List[str],
        "Profile": Literal["NONE", "HBBTV_1_5"],
        "SegmentDurationSeconds": int,
        "SegmentTemplateFormat": Literal[
            "NUMBER_WITH_TIMELINE", "TIME_WITH_TIMELINE", "NUMBER_WITH_DURATION"
        ],
        "StreamSelection": ClientListOriginEndpointsResponseOriginEndpointsDashPackageStreamSelectionTypeDef,
        "SuggestedPresentationDelaySeconds": int,
    },
    total=False,
)

ClientListOriginEndpointsResponseOriginEndpointsHlsPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "ClientListOriginEndpointsResponseOriginEndpointsHlsPackageEncryptionSpekeKeyProviderTypeDef",
    {"CertificateArn": str, "ResourceId": str, "RoleArn": str, "SystemIds": List[str], "Url": str},
    total=False,
)

ClientListOriginEndpointsResponseOriginEndpointsHlsPackageEncryptionTypeDef = TypedDict(
    "ClientListOriginEndpointsResponseOriginEndpointsHlsPackageEncryptionTypeDef",
    {
        "ConstantInitializationVector": str,
        "EncryptionMethod": Literal["AES_128", "SAMPLE_AES"],
        "KeyRotationIntervalSeconds": int,
        "RepeatExtXKey": bool,
        "SpekeKeyProvider": ClientListOriginEndpointsResponseOriginEndpointsHlsPackageEncryptionSpekeKeyProviderTypeDef,
    },
    total=False,
)

ClientListOriginEndpointsResponseOriginEndpointsHlsPackageStreamSelectionTypeDef = TypedDict(
    "ClientListOriginEndpointsResponseOriginEndpointsHlsPackageStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)

ClientListOriginEndpointsResponseOriginEndpointsHlsPackageTypeDef = TypedDict(
    "ClientListOriginEndpointsResponseOriginEndpointsHlsPackageTypeDef",
    {
        "AdMarkers": Literal["NONE", "SCTE35_ENHANCED", "PASSTHROUGH"],
        "AdTriggers": List[
            Literal[
                "SPLICE_INSERT",
                "BREAK",
                "PROVIDER_ADVERTISEMENT",
                "DISTRIBUTOR_ADVERTISEMENT",
                "PROVIDER_PLACEMENT_OPPORTUNITY",
                "DISTRIBUTOR_PLACEMENT_OPPORTUNITY",
                "PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY",
                "DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY",
            ]
        ],
        "AdsOnDeliveryRestrictions": Literal["NONE", "RESTRICTED", "UNRESTRICTED", "BOTH"],
        "Encryption": ClientListOriginEndpointsResponseOriginEndpointsHlsPackageEncryptionTypeDef,
        "IncludeIframeOnlyStream": bool,
        "PlaylistType": Literal["NONE", "EVENT", "VOD"],
        "PlaylistWindowSeconds": int,
        "ProgramDateTimeIntervalSeconds": int,
        "SegmentDurationSeconds": int,
        "StreamSelection": ClientListOriginEndpointsResponseOriginEndpointsHlsPackageStreamSelectionTypeDef,
        "UseAudioRenditionGroup": bool,
    },
    total=False,
)

ClientListOriginEndpointsResponseOriginEndpointsMssPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "ClientListOriginEndpointsResponseOriginEndpointsMssPackageEncryptionSpekeKeyProviderTypeDef",
    {"CertificateArn": str, "ResourceId": str, "RoleArn": str, "SystemIds": List[str], "Url": str},
    total=False,
)

ClientListOriginEndpointsResponseOriginEndpointsMssPackageEncryptionTypeDef = TypedDict(
    "ClientListOriginEndpointsResponseOriginEndpointsMssPackageEncryptionTypeDef",
    {
        "SpekeKeyProvider": ClientListOriginEndpointsResponseOriginEndpointsMssPackageEncryptionSpekeKeyProviderTypeDef
    },
    total=False,
)

ClientListOriginEndpointsResponseOriginEndpointsMssPackageStreamSelectionTypeDef = TypedDict(
    "ClientListOriginEndpointsResponseOriginEndpointsMssPackageStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)

ClientListOriginEndpointsResponseOriginEndpointsMssPackageTypeDef = TypedDict(
    "ClientListOriginEndpointsResponseOriginEndpointsMssPackageTypeDef",
    {
        "Encryption": ClientListOriginEndpointsResponseOriginEndpointsMssPackageEncryptionTypeDef,
        "ManifestWindowSeconds": int,
        "SegmentDurationSeconds": int,
        "StreamSelection": ClientListOriginEndpointsResponseOriginEndpointsMssPackageStreamSelectionTypeDef,
    },
    total=False,
)

ClientListOriginEndpointsResponseOriginEndpointsTypeDef = TypedDict(
    "ClientListOriginEndpointsResponseOriginEndpointsTypeDef",
    {
        "Arn": str,
        "Authorization": ClientListOriginEndpointsResponseOriginEndpointsAuthorizationTypeDef,
        "ChannelId": str,
        "CmafPackage": ClientListOriginEndpointsResponseOriginEndpointsCmafPackageTypeDef,
        "DashPackage": ClientListOriginEndpointsResponseOriginEndpointsDashPackageTypeDef,
        "Description": str,
        "HlsPackage": ClientListOriginEndpointsResponseOriginEndpointsHlsPackageTypeDef,
        "Id": str,
        "ManifestName": str,
        "MssPackage": ClientListOriginEndpointsResponseOriginEndpointsMssPackageTypeDef,
        "Origination": Literal["ALLOW", "DENY"],
        "StartoverWindowSeconds": int,
        "Tags": Dict[str, str],
        "TimeDelaySeconds": int,
        "Url": str,
        "Whitelist": List[str],
    },
    total=False,
)

ClientListOriginEndpointsResponseTypeDef = TypedDict(
    "ClientListOriginEndpointsResponseTypeDef",
    {
        "NextToken": str,
        "OriginEndpoints": List[ClientListOriginEndpointsResponseOriginEndpointsTypeDef],
    },
    total=False,
)

ClientListTagsForResourceResponseTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTypeDef", {"Tags": Dict[str, str]}, total=False
)

ClientRotateChannelCredentialsResponseHlsIngestIngestEndpointsTypeDef = TypedDict(
    "ClientRotateChannelCredentialsResponseHlsIngestIngestEndpointsTypeDef",
    {"Id": str, "Password": str, "Url": str, "Username": str},
    total=False,
)

ClientRotateChannelCredentialsResponseHlsIngestTypeDef = TypedDict(
    "ClientRotateChannelCredentialsResponseHlsIngestTypeDef",
    {
        "IngestEndpoints": List[
            ClientRotateChannelCredentialsResponseHlsIngestIngestEndpointsTypeDef
        ]
    },
    total=False,
)

ClientRotateChannelCredentialsResponseTypeDef = TypedDict(
    "ClientRotateChannelCredentialsResponseTypeDef",
    {
        "Arn": str,
        "Description": str,
        "HlsIngest": ClientRotateChannelCredentialsResponseHlsIngestTypeDef,
        "Id": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

ClientRotateIngestEndpointCredentialsResponseHlsIngestIngestEndpointsTypeDef = TypedDict(
    "ClientRotateIngestEndpointCredentialsResponseHlsIngestIngestEndpointsTypeDef",
    {"Id": str, "Password": str, "Url": str, "Username": str},
    total=False,
)

ClientRotateIngestEndpointCredentialsResponseHlsIngestTypeDef = TypedDict(
    "ClientRotateIngestEndpointCredentialsResponseHlsIngestTypeDef",
    {
        "IngestEndpoints": List[
            ClientRotateIngestEndpointCredentialsResponseHlsIngestIngestEndpointsTypeDef
        ]
    },
    total=False,
)

ClientRotateIngestEndpointCredentialsResponseTypeDef = TypedDict(
    "ClientRotateIngestEndpointCredentialsResponseTypeDef",
    {
        "Arn": str,
        "Description": str,
        "HlsIngest": ClientRotateIngestEndpointCredentialsResponseHlsIngestTypeDef,
        "Id": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

ClientUpdateChannelResponseHlsIngestIngestEndpointsTypeDef = TypedDict(
    "ClientUpdateChannelResponseHlsIngestIngestEndpointsTypeDef",
    {"Id": str, "Password": str, "Url": str, "Username": str},
    total=False,
)

ClientUpdateChannelResponseHlsIngestTypeDef = TypedDict(
    "ClientUpdateChannelResponseHlsIngestTypeDef",
    {"IngestEndpoints": List[ClientUpdateChannelResponseHlsIngestIngestEndpointsTypeDef]},
    total=False,
)

ClientUpdateChannelResponseTypeDef = TypedDict(
    "ClientUpdateChannelResponseTypeDef",
    {
        "Arn": str,
        "Description": str,
        "HlsIngest": ClientUpdateChannelResponseHlsIngestTypeDef,
        "Id": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

ClientUpdateOriginEndpointAuthorizationTypeDef = TypedDict(
    "ClientUpdateOriginEndpointAuthorizationTypeDef",
    {"CdnIdentifierSecret": str, "SecretsRoleArn": str},
)

_RequiredClientUpdateOriginEndpointCmafPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "_RequiredClientUpdateOriginEndpointCmafPackageEncryptionSpekeKeyProviderTypeDef",
    {"ResourceId": str, "RoleArn": str, "SystemIds": List[str]},
)
_OptionalClientUpdateOriginEndpointCmafPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "_OptionalClientUpdateOriginEndpointCmafPackageEncryptionSpekeKeyProviderTypeDef",
    {"CertificateArn": str, "Url": str},
    total=False,
)


class ClientUpdateOriginEndpointCmafPackageEncryptionSpekeKeyProviderTypeDef(
    _RequiredClientUpdateOriginEndpointCmafPackageEncryptionSpekeKeyProviderTypeDef,
    _OptionalClientUpdateOriginEndpointCmafPackageEncryptionSpekeKeyProviderTypeDef,
):
    pass


_RequiredClientUpdateOriginEndpointCmafPackageEncryptionTypeDef = TypedDict(
    "_RequiredClientUpdateOriginEndpointCmafPackageEncryptionTypeDef",
    {"SpekeKeyProvider": ClientUpdateOriginEndpointCmafPackageEncryptionSpekeKeyProviderTypeDef},
)
_OptionalClientUpdateOriginEndpointCmafPackageEncryptionTypeDef = TypedDict(
    "_OptionalClientUpdateOriginEndpointCmafPackageEncryptionTypeDef",
    {"KeyRotationIntervalSeconds": int},
    total=False,
)


class ClientUpdateOriginEndpointCmafPackageEncryptionTypeDef(
    _RequiredClientUpdateOriginEndpointCmafPackageEncryptionTypeDef,
    _OptionalClientUpdateOriginEndpointCmafPackageEncryptionTypeDef,
):
    pass


ClientUpdateOriginEndpointCmafPackageHlsManifestsTypeDef = TypedDict(
    "ClientUpdateOriginEndpointCmafPackageHlsManifestsTypeDef",
    {
        "AdMarkers": Literal["NONE", "SCTE35_ENHANCED", "PASSTHROUGH"],
        "AdTriggers": List[
            Literal[
                "SPLICE_INSERT",
                "BREAK",
                "PROVIDER_ADVERTISEMENT",
                "DISTRIBUTOR_ADVERTISEMENT",
                "PROVIDER_PLACEMENT_OPPORTUNITY",
                "DISTRIBUTOR_PLACEMENT_OPPORTUNITY",
                "PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY",
                "DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY",
            ]
        ],
        "AdsOnDeliveryRestrictions": Literal["NONE", "RESTRICTED", "UNRESTRICTED", "BOTH"],
        "Id": str,
        "IncludeIframeOnlyStream": bool,
        "ManifestName": str,
        "PlaylistType": Literal["NONE", "EVENT", "VOD"],
        "PlaylistWindowSeconds": int,
        "ProgramDateTimeIntervalSeconds": int,
    },
    total=False,
)

ClientUpdateOriginEndpointCmafPackageStreamSelectionTypeDef = TypedDict(
    "ClientUpdateOriginEndpointCmafPackageStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)

ClientUpdateOriginEndpointCmafPackageTypeDef = TypedDict(
    "ClientUpdateOriginEndpointCmafPackageTypeDef",
    {
        "Encryption": ClientUpdateOriginEndpointCmafPackageEncryptionTypeDef,
        "HlsManifests": List[ClientUpdateOriginEndpointCmafPackageHlsManifestsTypeDef],
        "SegmentDurationSeconds": int,
        "SegmentPrefix": str,
        "StreamSelection": ClientUpdateOriginEndpointCmafPackageStreamSelectionTypeDef,
    },
    total=False,
)

ClientUpdateOriginEndpointDashPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "ClientUpdateOriginEndpointDashPackageEncryptionSpekeKeyProviderTypeDef",
    {"CertificateArn": str, "ResourceId": str, "RoleArn": str, "SystemIds": List[str], "Url": str},
    total=False,
)

ClientUpdateOriginEndpointDashPackageEncryptionTypeDef = TypedDict(
    "ClientUpdateOriginEndpointDashPackageEncryptionTypeDef",
    {
        "KeyRotationIntervalSeconds": int,
        "SpekeKeyProvider": ClientUpdateOriginEndpointDashPackageEncryptionSpekeKeyProviderTypeDef,
    },
    total=False,
)

ClientUpdateOriginEndpointDashPackageStreamSelectionTypeDef = TypedDict(
    "ClientUpdateOriginEndpointDashPackageStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)

ClientUpdateOriginEndpointDashPackageTypeDef = TypedDict(
    "ClientUpdateOriginEndpointDashPackageTypeDef",
    {
        "AdTriggers": List[
            Literal[
                "SPLICE_INSERT",
                "BREAK",
                "PROVIDER_ADVERTISEMENT",
                "DISTRIBUTOR_ADVERTISEMENT",
                "PROVIDER_PLACEMENT_OPPORTUNITY",
                "DISTRIBUTOR_PLACEMENT_OPPORTUNITY",
                "PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY",
                "DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY",
            ]
        ],
        "AdsOnDeliveryRestrictions": Literal["NONE", "RESTRICTED", "UNRESTRICTED", "BOTH"],
        "Encryption": ClientUpdateOriginEndpointDashPackageEncryptionTypeDef,
        "ManifestLayout": Literal["FULL", "COMPACT"],
        "ManifestWindowSeconds": int,
        "MinBufferTimeSeconds": int,
        "MinUpdatePeriodSeconds": int,
        "PeriodTriggers": List[str],
        "Profile": Literal["NONE", "HBBTV_1_5"],
        "SegmentDurationSeconds": int,
        "SegmentTemplateFormat": Literal[
            "NUMBER_WITH_TIMELINE", "TIME_WITH_TIMELINE", "NUMBER_WITH_DURATION"
        ],
        "StreamSelection": ClientUpdateOriginEndpointDashPackageStreamSelectionTypeDef,
        "SuggestedPresentationDelaySeconds": int,
    },
    total=False,
)

ClientUpdateOriginEndpointHlsPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "ClientUpdateOriginEndpointHlsPackageEncryptionSpekeKeyProviderTypeDef",
    {"CertificateArn": str, "ResourceId": str, "RoleArn": str, "SystemIds": List[str], "Url": str},
    total=False,
)

ClientUpdateOriginEndpointHlsPackageEncryptionTypeDef = TypedDict(
    "ClientUpdateOriginEndpointHlsPackageEncryptionTypeDef",
    {
        "ConstantInitializationVector": str,
        "EncryptionMethod": Literal["AES_128", "SAMPLE_AES"],
        "KeyRotationIntervalSeconds": int,
        "RepeatExtXKey": bool,
        "SpekeKeyProvider": ClientUpdateOriginEndpointHlsPackageEncryptionSpekeKeyProviderTypeDef,
    },
    total=False,
)

ClientUpdateOriginEndpointHlsPackageStreamSelectionTypeDef = TypedDict(
    "ClientUpdateOriginEndpointHlsPackageStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)

ClientUpdateOriginEndpointHlsPackageTypeDef = TypedDict(
    "ClientUpdateOriginEndpointHlsPackageTypeDef",
    {
        "AdMarkers": Literal["NONE", "SCTE35_ENHANCED", "PASSTHROUGH"],
        "AdTriggers": List[
            Literal[
                "SPLICE_INSERT",
                "BREAK",
                "PROVIDER_ADVERTISEMENT",
                "DISTRIBUTOR_ADVERTISEMENT",
                "PROVIDER_PLACEMENT_OPPORTUNITY",
                "DISTRIBUTOR_PLACEMENT_OPPORTUNITY",
                "PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY",
                "DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY",
            ]
        ],
        "AdsOnDeliveryRestrictions": Literal["NONE", "RESTRICTED", "UNRESTRICTED", "BOTH"],
        "Encryption": ClientUpdateOriginEndpointHlsPackageEncryptionTypeDef,
        "IncludeIframeOnlyStream": bool,
        "PlaylistType": Literal["NONE", "EVENT", "VOD"],
        "PlaylistWindowSeconds": int,
        "ProgramDateTimeIntervalSeconds": int,
        "SegmentDurationSeconds": int,
        "StreamSelection": ClientUpdateOriginEndpointHlsPackageStreamSelectionTypeDef,
        "UseAudioRenditionGroup": bool,
    },
    total=False,
)

_RequiredClientUpdateOriginEndpointMssPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "_RequiredClientUpdateOriginEndpointMssPackageEncryptionSpekeKeyProviderTypeDef",
    {"ResourceId": str, "RoleArn": str, "SystemIds": List[str]},
)
_OptionalClientUpdateOriginEndpointMssPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "_OptionalClientUpdateOriginEndpointMssPackageEncryptionSpekeKeyProviderTypeDef",
    {"CertificateArn": str, "Url": str},
    total=False,
)


class ClientUpdateOriginEndpointMssPackageEncryptionSpekeKeyProviderTypeDef(
    _RequiredClientUpdateOriginEndpointMssPackageEncryptionSpekeKeyProviderTypeDef,
    _OptionalClientUpdateOriginEndpointMssPackageEncryptionSpekeKeyProviderTypeDef,
):
    pass


ClientUpdateOriginEndpointMssPackageEncryptionTypeDef = TypedDict(
    "ClientUpdateOriginEndpointMssPackageEncryptionTypeDef",
    {"SpekeKeyProvider": ClientUpdateOriginEndpointMssPackageEncryptionSpekeKeyProviderTypeDef},
)

ClientUpdateOriginEndpointMssPackageStreamSelectionTypeDef = TypedDict(
    "ClientUpdateOriginEndpointMssPackageStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)

ClientUpdateOriginEndpointMssPackageTypeDef = TypedDict(
    "ClientUpdateOriginEndpointMssPackageTypeDef",
    {
        "Encryption": ClientUpdateOriginEndpointMssPackageEncryptionTypeDef,
        "ManifestWindowSeconds": int,
        "SegmentDurationSeconds": int,
        "StreamSelection": ClientUpdateOriginEndpointMssPackageStreamSelectionTypeDef,
    },
    total=False,
)

ClientUpdateOriginEndpointResponseAuthorizationTypeDef = TypedDict(
    "ClientUpdateOriginEndpointResponseAuthorizationTypeDef",
    {"CdnIdentifierSecret": str, "SecretsRoleArn": str},
    total=False,
)

ClientUpdateOriginEndpointResponseCmafPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "ClientUpdateOriginEndpointResponseCmafPackageEncryptionSpekeKeyProviderTypeDef",
    {"CertificateArn": str, "ResourceId": str, "RoleArn": str, "SystemIds": List[str], "Url": str},
    total=False,
)

ClientUpdateOriginEndpointResponseCmafPackageEncryptionTypeDef = TypedDict(
    "ClientUpdateOriginEndpointResponseCmafPackageEncryptionTypeDef",
    {
        "KeyRotationIntervalSeconds": int,
        "SpekeKeyProvider": ClientUpdateOriginEndpointResponseCmafPackageEncryptionSpekeKeyProviderTypeDef,
    },
    total=False,
)

ClientUpdateOriginEndpointResponseCmafPackageHlsManifestsTypeDef = TypedDict(
    "ClientUpdateOriginEndpointResponseCmafPackageHlsManifestsTypeDef",
    {
        "AdMarkers": Literal["NONE", "SCTE35_ENHANCED", "PASSTHROUGH"],
        "Id": str,
        "IncludeIframeOnlyStream": bool,
        "ManifestName": str,
        "PlaylistType": Literal["NONE", "EVENT", "VOD"],
        "PlaylistWindowSeconds": int,
        "ProgramDateTimeIntervalSeconds": int,
        "Url": str,
    },
    total=False,
)

ClientUpdateOriginEndpointResponseCmafPackageStreamSelectionTypeDef = TypedDict(
    "ClientUpdateOriginEndpointResponseCmafPackageStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)

ClientUpdateOriginEndpointResponseCmafPackageTypeDef = TypedDict(
    "ClientUpdateOriginEndpointResponseCmafPackageTypeDef",
    {
        "Encryption": ClientUpdateOriginEndpointResponseCmafPackageEncryptionTypeDef,
        "HlsManifests": List[ClientUpdateOriginEndpointResponseCmafPackageHlsManifestsTypeDef],
        "SegmentDurationSeconds": int,
        "SegmentPrefix": str,
        "StreamSelection": ClientUpdateOriginEndpointResponseCmafPackageStreamSelectionTypeDef,
    },
    total=False,
)

ClientUpdateOriginEndpointResponseDashPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "ClientUpdateOriginEndpointResponseDashPackageEncryptionSpekeKeyProviderTypeDef",
    {"CertificateArn": str, "ResourceId": str, "RoleArn": str, "SystemIds": List[str], "Url": str},
    total=False,
)

ClientUpdateOriginEndpointResponseDashPackageEncryptionTypeDef = TypedDict(
    "ClientUpdateOriginEndpointResponseDashPackageEncryptionTypeDef",
    {
        "KeyRotationIntervalSeconds": int,
        "SpekeKeyProvider": ClientUpdateOriginEndpointResponseDashPackageEncryptionSpekeKeyProviderTypeDef,
    },
    total=False,
)

ClientUpdateOriginEndpointResponseDashPackageStreamSelectionTypeDef = TypedDict(
    "ClientUpdateOriginEndpointResponseDashPackageStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)

ClientUpdateOriginEndpointResponseDashPackageTypeDef = TypedDict(
    "ClientUpdateOriginEndpointResponseDashPackageTypeDef",
    {
        "AdTriggers": List[
            Literal[
                "SPLICE_INSERT",
                "BREAK",
                "PROVIDER_ADVERTISEMENT",
                "DISTRIBUTOR_ADVERTISEMENT",
                "PROVIDER_PLACEMENT_OPPORTUNITY",
                "DISTRIBUTOR_PLACEMENT_OPPORTUNITY",
                "PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY",
                "DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY",
            ]
        ],
        "AdsOnDeliveryRestrictions": Literal["NONE", "RESTRICTED", "UNRESTRICTED", "BOTH"],
        "Encryption": ClientUpdateOriginEndpointResponseDashPackageEncryptionTypeDef,
        "ManifestLayout": Literal["FULL", "COMPACT"],
        "ManifestWindowSeconds": int,
        "MinBufferTimeSeconds": int,
        "MinUpdatePeriodSeconds": int,
        "PeriodTriggers": List[str],
        "Profile": Literal["NONE", "HBBTV_1_5"],
        "SegmentDurationSeconds": int,
        "SegmentTemplateFormat": Literal[
            "NUMBER_WITH_TIMELINE", "TIME_WITH_TIMELINE", "NUMBER_WITH_DURATION"
        ],
        "StreamSelection": ClientUpdateOriginEndpointResponseDashPackageStreamSelectionTypeDef,
        "SuggestedPresentationDelaySeconds": int,
    },
    total=False,
)

ClientUpdateOriginEndpointResponseHlsPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "ClientUpdateOriginEndpointResponseHlsPackageEncryptionSpekeKeyProviderTypeDef",
    {"CertificateArn": str, "ResourceId": str, "RoleArn": str, "SystemIds": List[str], "Url": str},
    total=False,
)

ClientUpdateOriginEndpointResponseHlsPackageEncryptionTypeDef = TypedDict(
    "ClientUpdateOriginEndpointResponseHlsPackageEncryptionTypeDef",
    {
        "ConstantInitializationVector": str,
        "EncryptionMethod": Literal["AES_128", "SAMPLE_AES"],
        "KeyRotationIntervalSeconds": int,
        "RepeatExtXKey": bool,
        "SpekeKeyProvider": ClientUpdateOriginEndpointResponseHlsPackageEncryptionSpekeKeyProviderTypeDef,
    },
    total=False,
)

ClientUpdateOriginEndpointResponseHlsPackageStreamSelectionTypeDef = TypedDict(
    "ClientUpdateOriginEndpointResponseHlsPackageStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)

ClientUpdateOriginEndpointResponseHlsPackageTypeDef = TypedDict(
    "ClientUpdateOriginEndpointResponseHlsPackageTypeDef",
    {
        "AdMarkers": Literal["NONE", "SCTE35_ENHANCED", "PASSTHROUGH"],
        "AdTriggers": List[
            Literal[
                "SPLICE_INSERT",
                "BREAK",
                "PROVIDER_ADVERTISEMENT",
                "DISTRIBUTOR_ADVERTISEMENT",
                "PROVIDER_PLACEMENT_OPPORTUNITY",
                "DISTRIBUTOR_PLACEMENT_OPPORTUNITY",
                "PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY",
                "DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY",
            ]
        ],
        "AdsOnDeliveryRestrictions": Literal["NONE", "RESTRICTED", "UNRESTRICTED", "BOTH"],
        "Encryption": ClientUpdateOriginEndpointResponseHlsPackageEncryptionTypeDef,
        "IncludeIframeOnlyStream": bool,
        "PlaylistType": Literal["NONE", "EVENT", "VOD"],
        "PlaylistWindowSeconds": int,
        "ProgramDateTimeIntervalSeconds": int,
        "SegmentDurationSeconds": int,
        "StreamSelection": ClientUpdateOriginEndpointResponseHlsPackageStreamSelectionTypeDef,
        "UseAudioRenditionGroup": bool,
    },
    total=False,
)

ClientUpdateOriginEndpointResponseMssPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "ClientUpdateOriginEndpointResponseMssPackageEncryptionSpekeKeyProviderTypeDef",
    {"CertificateArn": str, "ResourceId": str, "RoleArn": str, "SystemIds": List[str], "Url": str},
    total=False,
)

ClientUpdateOriginEndpointResponseMssPackageEncryptionTypeDef = TypedDict(
    "ClientUpdateOriginEndpointResponseMssPackageEncryptionTypeDef",
    {
        "SpekeKeyProvider": ClientUpdateOriginEndpointResponseMssPackageEncryptionSpekeKeyProviderTypeDef
    },
    total=False,
)

ClientUpdateOriginEndpointResponseMssPackageStreamSelectionTypeDef = TypedDict(
    "ClientUpdateOriginEndpointResponseMssPackageStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)

ClientUpdateOriginEndpointResponseMssPackageTypeDef = TypedDict(
    "ClientUpdateOriginEndpointResponseMssPackageTypeDef",
    {
        "Encryption": ClientUpdateOriginEndpointResponseMssPackageEncryptionTypeDef,
        "ManifestWindowSeconds": int,
        "SegmentDurationSeconds": int,
        "StreamSelection": ClientUpdateOriginEndpointResponseMssPackageStreamSelectionTypeDef,
    },
    total=False,
)

ClientUpdateOriginEndpointResponseTypeDef = TypedDict(
    "ClientUpdateOriginEndpointResponseTypeDef",
    {
        "Arn": str,
        "Authorization": ClientUpdateOriginEndpointResponseAuthorizationTypeDef,
        "ChannelId": str,
        "CmafPackage": ClientUpdateOriginEndpointResponseCmafPackageTypeDef,
        "DashPackage": ClientUpdateOriginEndpointResponseDashPackageTypeDef,
        "Description": str,
        "HlsPackage": ClientUpdateOriginEndpointResponseHlsPackageTypeDef,
        "Id": str,
        "ManifestName": str,
        "MssPackage": ClientUpdateOriginEndpointResponseMssPackageTypeDef,
        "Origination": Literal["ALLOW", "DENY"],
        "StartoverWindowSeconds": int,
        "Tags": Dict[str, str],
        "TimeDelaySeconds": int,
        "Url": str,
        "Whitelist": List[str],
    },
    total=False,
)

IngestEndpointTypeDef = TypedDict(
    "IngestEndpointTypeDef", {"Id": str, "Password": str, "Url": str, "Username": str}, total=False
)

HlsIngestTypeDef = TypedDict(
    "HlsIngestTypeDef", {"IngestEndpoints": List[IngestEndpointTypeDef]}, total=False
)

ChannelTypeDef = TypedDict(
    "ChannelTypeDef",
    {
        "Arn": str,
        "Description": str,
        "HlsIngest": HlsIngestTypeDef,
        "Id": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

ListChannelsResponseTypeDef = TypedDict(
    "ListChannelsResponseTypeDef", {"Channels": List[ChannelTypeDef], "NextToken": str}, total=False
)

S3DestinationTypeDef = TypedDict(
    "S3DestinationTypeDef", {"BucketName": str, "ManifestKey": str, "RoleArn": str}
)

HarvestJobTypeDef = TypedDict(
    "HarvestJobTypeDef",
    {
        "Arn": str,
        "ChannelId": str,
        "CreatedAt": str,
        "EndTime": str,
        "Id": str,
        "OriginEndpointId": str,
        "S3Destination": S3DestinationTypeDef,
        "StartTime": str,
        "Status": Literal["IN_PROGRESS", "SUCCEEDED", "FAILED"],
    },
    total=False,
)

ListHarvestJobsResponseTypeDef = TypedDict(
    "ListHarvestJobsResponseTypeDef",
    {"HarvestJobs": List[HarvestJobTypeDef], "NextToken": str},
    total=False,
)

AuthorizationTypeDef = TypedDict(
    "AuthorizationTypeDef", {"CdnIdentifierSecret": str, "SecretsRoleArn": str}
)

_RequiredSpekeKeyProviderTypeDef = TypedDict(
    "_RequiredSpekeKeyProviderTypeDef",
    {"ResourceId": str, "RoleArn": str, "SystemIds": List[str], "Url": str},
)
_OptionalSpekeKeyProviderTypeDef = TypedDict(
    "_OptionalSpekeKeyProviderTypeDef", {"CertificateArn": str}, total=False
)


class SpekeKeyProviderTypeDef(_RequiredSpekeKeyProviderTypeDef, _OptionalSpekeKeyProviderTypeDef):
    pass


_RequiredCmafEncryptionTypeDef = TypedDict(
    "_RequiredCmafEncryptionTypeDef", {"SpekeKeyProvider": SpekeKeyProviderTypeDef}
)
_OptionalCmafEncryptionTypeDef = TypedDict(
    "_OptionalCmafEncryptionTypeDef", {"KeyRotationIntervalSeconds": int}, total=False
)


class CmafEncryptionTypeDef(_RequiredCmafEncryptionTypeDef, _OptionalCmafEncryptionTypeDef):
    pass


_RequiredHlsManifestTypeDef = TypedDict("_RequiredHlsManifestTypeDef", {"Id": str})
_OptionalHlsManifestTypeDef = TypedDict(
    "_OptionalHlsManifestTypeDef",
    {
        "AdMarkers": Literal["NONE", "SCTE35_ENHANCED", "PASSTHROUGH"],
        "IncludeIframeOnlyStream": bool,
        "ManifestName": str,
        "PlaylistType": Literal["NONE", "EVENT", "VOD"],
        "PlaylistWindowSeconds": int,
        "ProgramDateTimeIntervalSeconds": int,
        "Url": str,
    },
    total=False,
)


class HlsManifestTypeDef(_RequiredHlsManifestTypeDef, _OptionalHlsManifestTypeDef):
    pass


StreamSelectionTypeDef = TypedDict(
    "StreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)

CmafPackageTypeDef = TypedDict(
    "CmafPackageTypeDef",
    {
        "Encryption": CmafEncryptionTypeDef,
        "HlsManifests": List[HlsManifestTypeDef],
        "SegmentDurationSeconds": int,
        "SegmentPrefix": str,
        "StreamSelection": StreamSelectionTypeDef,
    },
    total=False,
)

_RequiredDashEncryptionTypeDef = TypedDict(
    "_RequiredDashEncryptionTypeDef", {"SpekeKeyProvider": SpekeKeyProviderTypeDef}
)
_OptionalDashEncryptionTypeDef = TypedDict(
    "_OptionalDashEncryptionTypeDef", {"KeyRotationIntervalSeconds": int}, total=False
)


class DashEncryptionTypeDef(_RequiredDashEncryptionTypeDef, _OptionalDashEncryptionTypeDef):
    pass


DashPackageTypeDef = TypedDict(
    "DashPackageTypeDef",
    {
        "AdTriggers": List[
            Literal[
                "SPLICE_INSERT",
                "BREAK",
                "PROVIDER_ADVERTISEMENT",
                "DISTRIBUTOR_ADVERTISEMENT",
                "PROVIDER_PLACEMENT_OPPORTUNITY",
                "DISTRIBUTOR_PLACEMENT_OPPORTUNITY",
                "PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY",
                "DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY",
            ]
        ],
        "AdsOnDeliveryRestrictions": Literal["NONE", "RESTRICTED", "UNRESTRICTED", "BOTH"],
        "Encryption": DashEncryptionTypeDef,
        "ManifestLayout": Literal["FULL", "COMPACT"],
        "ManifestWindowSeconds": int,
        "MinBufferTimeSeconds": int,
        "MinUpdatePeriodSeconds": int,
        "PeriodTriggers": List[Literal["ADS"]],
        "Profile": Literal["NONE", "HBBTV_1_5"],
        "SegmentDurationSeconds": int,
        "SegmentTemplateFormat": Literal[
            "NUMBER_WITH_TIMELINE", "TIME_WITH_TIMELINE", "NUMBER_WITH_DURATION"
        ],
        "StreamSelection": StreamSelectionTypeDef,
        "SuggestedPresentationDelaySeconds": int,
    },
    total=False,
)

_RequiredHlsEncryptionTypeDef = TypedDict(
    "_RequiredHlsEncryptionTypeDef", {"SpekeKeyProvider": SpekeKeyProviderTypeDef}
)
_OptionalHlsEncryptionTypeDef = TypedDict(
    "_OptionalHlsEncryptionTypeDef",
    {
        "ConstantInitializationVector": str,
        "EncryptionMethod": Literal["AES_128", "SAMPLE_AES"],
        "KeyRotationIntervalSeconds": int,
        "RepeatExtXKey": bool,
    },
    total=False,
)


class HlsEncryptionTypeDef(_RequiredHlsEncryptionTypeDef, _OptionalHlsEncryptionTypeDef):
    pass


HlsPackageTypeDef = TypedDict(
    "HlsPackageTypeDef",
    {
        "AdMarkers": Literal["NONE", "SCTE35_ENHANCED", "PASSTHROUGH"],
        "AdTriggers": List[
            Literal[
                "SPLICE_INSERT",
                "BREAK",
                "PROVIDER_ADVERTISEMENT",
                "DISTRIBUTOR_ADVERTISEMENT",
                "PROVIDER_PLACEMENT_OPPORTUNITY",
                "DISTRIBUTOR_PLACEMENT_OPPORTUNITY",
                "PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY",
                "DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY",
            ]
        ],
        "AdsOnDeliveryRestrictions": Literal["NONE", "RESTRICTED", "UNRESTRICTED", "BOTH"],
        "Encryption": HlsEncryptionTypeDef,
        "IncludeIframeOnlyStream": bool,
        "PlaylistType": Literal["NONE", "EVENT", "VOD"],
        "PlaylistWindowSeconds": int,
        "ProgramDateTimeIntervalSeconds": int,
        "SegmentDurationSeconds": int,
        "StreamSelection": StreamSelectionTypeDef,
        "UseAudioRenditionGroup": bool,
    },
    total=False,
)

MssEncryptionTypeDef = TypedDict(
    "MssEncryptionTypeDef", {"SpekeKeyProvider": SpekeKeyProviderTypeDef}
)

MssPackageTypeDef = TypedDict(
    "MssPackageTypeDef",
    {
        "Encryption": MssEncryptionTypeDef,
        "ManifestWindowSeconds": int,
        "SegmentDurationSeconds": int,
        "StreamSelection": StreamSelectionTypeDef,
    },
    total=False,
)

OriginEndpointTypeDef = TypedDict(
    "OriginEndpointTypeDef",
    {
        "Arn": str,
        "Authorization": AuthorizationTypeDef,
        "ChannelId": str,
        "CmafPackage": CmafPackageTypeDef,
        "DashPackage": DashPackageTypeDef,
        "Description": str,
        "HlsPackage": HlsPackageTypeDef,
        "Id": str,
        "ManifestName": str,
        "MssPackage": MssPackageTypeDef,
        "Origination": Literal["ALLOW", "DENY"],
        "StartoverWindowSeconds": int,
        "Tags": Dict[str, str],
        "TimeDelaySeconds": int,
        "Url": str,
        "Whitelist": List[str],
    },
    total=False,
)

ListOriginEndpointsResponseTypeDef = TypedDict(
    "ListOriginEndpointsResponseTypeDef",
    {"NextToken": str, "OriginEndpoints": List[OriginEndpointTypeDef]},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)
