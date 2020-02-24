"""
Main interface for storagegateway service type definitions.

Usage::

    from mypy_boto3.storagegateway.type_defs import ClientActivateGatewayResponseTypeDef

    data: ClientActivateGatewayResponseTypeDef = {...}
"""
from datetime import datetime
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
    "ClientActivateGatewayResponseTypeDef",
    "ClientActivateGatewayTagsTypeDef",
    "ClientAddCacheResponseTypeDef",
    "ClientAddTagsToResourceResponseTypeDef",
    "ClientAddTagsToResourceTagsTypeDef",
    "ClientAddUploadBufferResponseTypeDef",
    "ClientAddWorkingStorageResponseTypeDef",
    "ClientAssignTapePoolResponseTypeDef",
    "ClientAttachVolumeResponseTypeDef",
    "ClientCancelArchivalResponseTypeDef",
    "ClientCancelRetrievalResponseTypeDef",
    "ClientCreateCachedIscsiVolumeResponseTypeDef",
    "ClientCreateCachedIscsiVolumeTagsTypeDef",
    "ClientCreateNfsFileShareNFSFileShareDefaultsTypeDef",
    "ClientCreateNfsFileShareResponseTypeDef",
    "ClientCreateNfsFileShareTagsTypeDef",
    "ClientCreateSmbFileShareResponseTypeDef",
    "ClientCreateSmbFileShareTagsTypeDef",
    "ClientCreateSnapshotFromVolumeRecoveryPointResponseTypeDef",
    "ClientCreateSnapshotFromVolumeRecoveryPointTagsTypeDef",
    "ClientCreateSnapshotResponseTypeDef",
    "ClientCreateSnapshotTagsTypeDef",
    "ClientCreateStoredIscsiVolumeResponseTypeDef",
    "ClientCreateStoredIscsiVolumeTagsTypeDef",
    "ClientCreateTapeWithBarcodeResponseTypeDef",
    "ClientCreateTapeWithBarcodeTagsTypeDef",
    "ClientCreateTapesResponseTypeDef",
    "ClientCreateTapesTagsTypeDef",
    "ClientDeleteBandwidthRateLimitResponseTypeDef",
    "ClientDeleteChapCredentialsResponseTypeDef",
    "ClientDeleteFileShareResponseTypeDef",
    "ClientDeleteGatewayResponseTypeDef",
    "ClientDeleteSnapshotScheduleResponseTypeDef",
    "ClientDeleteTapeArchiveResponseTypeDef",
    "ClientDeleteTapeResponseTypeDef",
    "ClientDeleteVolumeResponseTypeDef",
    "ClientDescribeAvailabilityMonitorTestResponseTypeDef",
    "ClientDescribeBandwidthRateLimitResponseTypeDef",
    "ClientDescribeCacheResponseTypeDef",
    "ClientDescribeCachedIscsiVolumesResponseCachediSCSIVolumesVolumeiSCSIAttributesTypeDef",
    "ClientDescribeCachedIscsiVolumesResponseCachediSCSIVolumesTypeDef",
    "ClientDescribeCachedIscsiVolumesResponseTypeDef",
    "ClientDescribeChapCredentialsResponseChapCredentialsTypeDef",
    "ClientDescribeChapCredentialsResponseTypeDef",
    "ClientDescribeGatewayInformationResponseGatewayNetworkInterfacesTypeDef",
    "ClientDescribeGatewayInformationResponseTagsTypeDef",
    "ClientDescribeGatewayInformationResponseTypeDef",
    "ClientDescribeMaintenanceStartTimeResponseTypeDef",
    "ClientDescribeNfsFileSharesResponseNFSFileShareInfoListNFSFileShareDefaultsTypeDef",
    "ClientDescribeNfsFileSharesResponseNFSFileShareInfoListTagsTypeDef",
    "ClientDescribeNfsFileSharesResponseNFSFileShareInfoListTypeDef",
    "ClientDescribeNfsFileSharesResponseTypeDef",
    "ClientDescribeSmbFileSharesResponseSMBFileShareInfoListTagsTypeDef",
    "ClientDescribeSmbFileSharesResponseSMBFileShareInfoListTypeDef",
    "ClientDescribeSmbFileSharesResponseTypeDef",
    "ClientDescribeSmbSettingsResponseTypeDef",
    "ClientDescribeSnapshotScheduleResponseTagsTypeDef",
    "ClientDescribeSnapshotScheduleResponseTypeDef",
    "ClientDescribeStoredIscsiVolumesResponseStorediSCSIVolumesVolumeiSCSIAttributesTypeDef",
    "ClientDescribeStoredIscsiVolumesResponseStorediSCSIVolumesTypeDef",
    "ClientDescribeStoredIscsiVolumesResponseTypeDef",
    "ClientDescribeTapeArchivesResponseTapeArchivesTypeDef",
    "ClientDescribeTapeArchivesResponseTypeDef",
    "ClientDescribeTapeRecoveryPointsResponseTapeRecoveryPointInfosTypeDef",
    "ClientDescribeTapeRecoveryPointsResponseTypeDef",
    "ClientDescribeTapesResponseTapesTypeDef",
    "ClientDescribeTapesResponseTypeDef",
    "ClientDescribeUploadBufferResponseTypeDef",
    "ClientDescribeVtlDevicesResponseVTLDevicesDeviceiSCSIAttributesTypeDef",
    "ClientDescribeVtlDevicesResponseVTLDevicesTypeDef",
    "ClientDescribeVtlDevicesResponseTypeDef",
    "ClientDescribeWorkingStorageResponseTypeDef",
    "ClientDetachVolumeResponseTypeDef",
    "ClientDisableGatewayResponseTypeDef",
    "ClientJoinDomainResponseTypeDef",
    "ClientListFileSharesResponseFileShareInfoListTypeDef",
    "ClientListFileSharesResponseTypeDef",
    "ClientListGatewaysResponseGatewaysTypeDef",
    "ClientListGatewaysResponseTypeDef",
    "ClientListLocalDisksResponseDisksTypeDef",
    "ClientListLocalDisksResponseTypeDef",
    "ClientListTagsForResourceResponseTagsTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientListTapesResponseTapeInfosTypeDef",
    "ClientListTapesResponseTypeDef",
    "ClientListVolumeInitiatorsResponseTypeDef",
    "ClientListVolumeRecoveryPointsResponseVolumeRecoveryPointInfosTypeDef",
    "ClientListVolumeRecoveryPointsResponseTypeDef",
    "ClientListVolumesResponseVolumeInfosTypeDef",
    "ClientListVolumesResponseTypeDef",
    "ClientNotifyWhenUploadedResponseTypeDef",
    "ClientRefreshCacheResponseTypeDef",
    "ClientRemoveTagsFromResourceResponseTypeDef",
    "ClientResetCacheResponseTypeDef",
    "ClientRetrieveTapeArchiveResponseTypeDef",
    "ClientRetrieveTapeRecoveryPointResponseTypeDef",
    "ClientSetLocalConsolePasswordResponseTypeDef",
    "ClientSetSmbGuestPasswordResponseTypeDef",
    "ClientShutdownGatewayResponseTypeDef",
    "ClientStartAvailabilityMonitorTestResponseTypeDef",
    "ClientStartGatewayResponseTypeDef",
    "ClientUpdateBandwidthRateLimitResponseTypeDef",
    "ClientUpdateChapCredentialsResponseTypeDef",
    "ClientUpdateGatewayInformationResponseTypeDef",
    "ClientUpdateGatewaySoftwareNowResponseTypeDef",
    "ClientUpdateMaintenanceStartTimeResponseTypeDef",
    "ClientUpdateNfsFileShareNFSFileShareDefaultsTypeDef",
    "ClientUpdateNfsFileShareResponseTypeDef",
    "ClientUpdateSmbFileShareResponseTypeDef",
    "ClientUpdateSmbSecurityStrategyResponseTypeDef",
    "ClientUpdateSnapshotScheduleResponseTypeDef",
    "ClientUpdateSnapshotScheduleTagsTypeDef",
    "ClientUpdateVtlDeviceTypeResponseTypeDef",
    "TapeArchiveTypeDef",
    "DescribeTapeArchivesOutputTypeDef",
    "TapeRecoveryPointInfoTypeDef",
    "DescribeTapeRecoveryPointsOutputTypeDef",
    "TapeTypeDef",
    "DescribeTapesOutputTypeDef",
    "DeviceiSCSIAttributesTypeDef",
    "VTLDeviceTypeDef",
    "DescribeVTLDevicesOutputTypeDef",
    "FileShareInfoTypeDef",
    "ListFileSharesOutputTypeDef",
    "GatewayInfoTypeDef",
    "ListGatewaysOutputTypeDef",
    "TagTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "TapeInfoTypeDef",
    "ListTapesOutputTypeDef",
    "VolumeInfoTypeDef",
    "ListVolumesOutputTypeDef",
    "PaginatorConfigTypeDef",
)

ClientActivateGatewayResponseTypeDef = TypedDict(
    "ClientActivateGatewayResponseTypeDef", {"GatewayARN": str}, total=False
)

ClientActivateGatewayTagsTypeDef = TypedDict(
    "ClientActivateGatewayTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientAddCacheResponseTypeDef = TypedDict(
    "ClientAddCacheResponseTypeDef", {"GatewayARN": str}, total=False
)

ClientAddTagsToResourceResponseTypeDef = TypedDict(
    "ClientAddTagsToResourceResponseTypeDef", {"ResourceARN": str}, total=False
)

ClientAddTagsToResourceTagsTypeDef = TypedDict(
    "ClientAddTagsToResourceTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientAddUploadBufferResponseTypeDef = TypedDict(
    "ClientAddUploadBufferResponseTypeDef", {"GatewayARN": str}, total=False
)

ClientAddWorkingStorageResponseTypeDef = TypedDict(
    "ClientAddWorkingStorageResponseTypeDef", {"GatewayARN": str}, total=False
)

ClientAssignTapePoolResponseTypeDef = TypedDict(
    "ClientAssignTapePoolResponseTypeDef", {"TapeARN": str}, total=False
)

ClientAttachVolumeResponseTypeDef = TypedDict(
    "ClientAttachVolumeResponseTypeDef", {"VolumeARN": str, "TargetARN": str}, total=False
)

ClientCancelArchivalResponseTypeDef = TypedDict(
    "ClientCancelArchivalResponseTypeDef", {"TapeARN": str}, total=False
)

ClientCancelRetrievalResponseTypeDef = TypedDict(
    "ClientCancelRetrievalResponseTypeDef", {"TapeARN": str}, total=False
)

ClientCreateCachedIscsiVolumeResponseTypeDef = TypedDict(
    "ClientCreateCachedIscsiVolumeResponseTypeDef",
    {"VolumeARN": str, "TargetARN": str},
    total=False,
)

ClientCreateCachedIscsiVolumeTagsTypeDef = TypedDict(
    "ClientCreateCachedIscsiVolumeTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreateNfsFileShareNFSFileShareDefaultsTypeDef = TypedDict(
    "ClientCreateNfsFileShareNFSFileShareDefaultsTypeDef",
    {"FileMode": str, "DirectoryMode": str, "GroupId": int, "OwnerId": int},
    total=False,
)

ClientCreateNfsFileShareResponseTypeDef = TypedDict(
    "ClientCreateNfsFileShareResponseTypeDef", {"FileShareARN": str}, total=False
)

ClientCreateNfsFileShareTagsTypeDef = TypedDict(
    "ClientCreateNfsFileShareTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreateSmbFileShareResponseTypeDef = TypedDict(
    "ClientCreateSmbFileShareResponseTypeDef", {"FileShareARN": str}, total=False
)

ClientCreateSmbFileShareTagsTypeDef = TypedDict(
    "ClientCreateSmbFileShareTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreateSnapshotFromVolumeRecoveryPointResponseTypeDef = TypedDict(
    "ClientCreateSnapshotFromVolumeRecoveryPointResponseTypeDef",
    {"SnapshotId": str, "VolumeARN": str, "VolumeRecoveryPointTime": str},
    total=False,
)

ClientCreateSnapshotFromVolumeRecoveryPointTagsTypeDef = TypedDict(
    "ClientCreateSnapshotFromVolumeRecoveryPointTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientCreateSnapshotResponseTypeDef = TypedDict(
    "ClientCreateSnapshotResponseTypeDef", {"VolumeARN": str, "SnapshotId": str}, total=False
)

ClientCreateSnapshotTagsTypeDef = TypedDict(
    "ClientCreateSnapshotTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreateStoredIscsiVolumeResponseTypeDef = TypedDict(
    "ClientCreateStoredIscsiVolumeResponseTypeDef",
    {"VolumeARN": str, "VolumeSizeInBytes": int, "TargetARN": str},
    total=False,
)

ClientCreateStoredIscsiVolumeTagsTypeDef = TypedDict(
    "ClientCreateStoredIscsiVolumeTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreateTapeWithBarcodeResponseTypeDef = TypedDict(
    "ClientCreateTapeWithBarcodeResponseTypeDef", {"TapeARN": str}, total=False
)

ClientCreateTapeWithBarcodeTagsTypeDef = TypedDict(
    "ClientCreateTapeWithBarcodeTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreateTapesResponseTypeDef = TypedDict(
    "ClientCreateTapesResponseTypeDef", {"TapeARNs": List[str]}, total=False
)

ClientCreateTapesTagsTypeDef = TypedDict(
    "ClientCreateTapesTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientDeleteBandwidthRateLimitResponseTypeDef = TypedDict(
    "ClientDeleteBandwidthRateLimitResponseTypeDef", {"GatewayARN": str}, total=False
)

ClientDeleteChapCredentialsResponseTypeDef = TypedDict(
    "ClientDeleteChapCredentialsResponseTypeDef",
    {"TargetARN": str, "InitiatorName": str},
    total=False,
)

ClientDeleteFileShareResponseTypeDef = TypedDict(
    "ClientDeleteFileShareResponseTypeDef", {"FileShareARN": str}, total=False
)

ClientDeleteGatewayResponseTypeDef = TypedDict(
    "ClientDeleteGatewayResponseTypeDef", {"GatewayARN": str}, total=False
)

ClientDeleteSnapshotScheduleResponseTypeDef = TypedDict(
    "ClientDeleteSnapshotScheduleResponseTypeDef", {"VolumeARN": str}, total=False
)

ClientDeleteTapeArchiveResponseTypeDef = TypedDict(
    "ClientDeleteTapeArchiveResponseTypeDef", {"TapeARN": str}, total=False
)

ClientDeleteTapeResponseTypeDef = TypedDict(
    "ClientDeleteTapeResponseTypeDef", {"TapeARN": str}, total=False
)

ClientDeleteVolumeResponseTypeDef = TypedDict(
    "ClientDeleteVolumeResponseTypeDef", {"VolumeARN": str}, total=False
)

ClientDescribeAvailabilityMonitorTestResponseTypeDef = TypedDict(
    "ClientDescribeAvailabilityMonitorTestResponseTypeDef",
    {"GatewayARN": str, "Status": Literal["COMPLETE", "FAILED", "PENDING"], "StartTime": datetime},
    total=False,
)

ClientDescribeBandwidthRateLimitResponseTypeDef = TypedDict(
    "ClientDescribeBandwidthRateLimitResponseTypeDef",
    {
        "GatewayARN": str,
        "AverageUploadRateLimitInBitsPerSec": int,
        "AverageDownloadRateLimitInBitsPerSec": int,
    },
    total=False,
)

ClientDescribeCacheResponseTypeDef = TypedDict(
    "ClientDescribeCacheResponseTypeDef",
    {
        "GatewayARN": str,
        "DiskIds": List[str],
        "CacheAllocatedInBytes": int,
        "CacheUsedPercentage": float,
        "CacheDirtyPercentage": float,
        "CacheHitPercentage": float,
        "CacheMissPercentage": float,
    },
    total=False,
)

ClientDescribeCachedIscsiVolumesResponseCachediSCSIVolumesVolumeiSCSIAttributesTypeDef = TypedDict(
    "ClientDescribeCachedIscsiVolumesResponseCachediSCSIVolumesVolumeiSCSIAttributesTypeDef",
    {
        "TargetARN": str,
        "NetworkInterfaceId": str,
        "NetworkInterfacePort": int,
        "LunNumber": int,
        "ChapEnabled": bool,
    },
    total=False,
)

ClientDescribeCachedIscsiVolumesResponseCachediSCSIVolumesTypeDef = TypedDict(
    "ClientDescribeCachedIscsiVolumesResponseCachediSCSIVolumesTypeDef",
    {
        "VolumeARN": str,
        "VolumeId": str,
        "VolumeType": str,
        "VolumeStatus": str,
        "VolumeAttachmentStatus": str,
        "VolumeSizeInBytes": int,
        "VolumeProgress": float,
        "SourceSnapshotId": str,
        "VolumeiSCSIAttributes": ClientDescribeCachedIscsiVolumesResponseCachediSCSIVolumesVolumeiSCSIAttributesTypeDef,
        "CreatedDate": datetime,
        "VolumeUsedInBytes": int,
        "KMSKey": str,
        "TargetName": str,
    },
    total=False,
)

ClientDescribeCachedIscsiVolumesResponseTypeDef = TypedDict(
    "ClientDescribeCachedIscsiVolumesResponseTypeDef",
    {"CachediSCSIVolumes": List[ClientDescribeCachedIscsiVolumesResponseCachediSCSIVolumesTypeDef]},
    total=False,
)

ClientDescribeChapCredentialsResponseChapCredentialsTypeDef = TypedDict(
    "ClientDescribeChapCredentialsResponseChapCredentialsTypeDef",
    {
        "TargetARN": str,
        "SecretToAuthenticateInitiator": str,
        "InitiatorName": str,
        "SecretToAuthenticateTarget": str,
    },
    total=False,
)

ClientDescribeChapCredentialsResponseTypeDef = TypedDict(
    "ClientDescribeChapCredentialsResponseTypeDef",
    {"ChapCredentials": List[ClientDescribeChapCredentialsResponseChapCredentialsTypeDef]},
    total=False,
)

ClientDescribeGatewayInformationResponseGatewayNetworkInterfacesTypeDef = TypedDict(
    "ClientDescribeGatewayInformationResponseGatewayNetworkInterfacesTypeDef",
    {"Ipv4Address": str, "MacAddress": str, "Ipv6Address": str},
    total=False,
)

ClientDescribeGatewayInformationResponseTagsTypeDef = TypedDict(
    "ClientDescribeGatewayInformationResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientDescribeGatewayInformationResponseTypeDef = TypedDict(
    "ClientDescribeGatewayInformationResponseTypeDef",
    {
        "GatewayARN": str,
        "GatewayId": str,
        "GatewayName": str,
        "GatewayTimezone": str,
        "GatewayState": str,
        "GatewayNetworkInterfaces": List[
            ClientDescribeGatewayInformationResponseGatewayNetworkInterfacesTypeDef
        ],
        "GatewayType": str,
        "NextUpdateAvailabilityDate": str,
        "LastSoftwareUpdate": str,
        "Ec2InstanceId": str,
        "Ec2InstanceRegion": str,
        "Tags": List[ClientDescribeGatewayInformationResponseTagsTypeDef],
        "VPCEndpoint": str,
        "CloudWatchLogGroupARN": str,
        "HostEnvironment": Literal["VMWARE", "HYPER-V", "EC2", "KVM", "OTHER"],
    },
    total=False,
)

ClientDescribeMaintenanceStartTimeResponseTypeDef = TypedDict(
    "ClientDescribeMaintenanceStartTimeResponseTypeDef",
    {
        "GatewayARN": str,
        "HourOfDay": int,
        "MinuteOfHour": int,
        "DayOfWeek": int,
        "DayOfMonth": int,
        "Timezone": str,
    },
    total=False,
)

ClientDescribeNfsFileSharesResponseNFSFileShareInfoListNFSFileShareDefaultsTypeDef = TypedDict(
    "ClientDescribeNfsFileSharesResponseNFSFileShareInfoListNFSFileShareDefaultsTypeDef",
    {"FileMode": str, "DirectoryMode": str, "GroupId": int, "OwnerId": int},
    total=False,
)

ClientDescribeNfsFileSharesResponseNFSFileShareInfoListTagsTypeDef = TypedDict(
    "ClientDescribeNfsFileSharesResponseNFSFileShareInfoListTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientDescribeNfsFileSharesResponseNFSFileShareInfoListTypeDef = TypedDict(
    "ClientDescribeNfsFileSharesResponseNFSFileShareInfoListTypeDef",
    {
        "NFSFileShareDefaults": ClientDescribeNfsFileSharesResponseNFSFileShareInfoListNFSFileShareDefaultsTypeDef,
        "FileShareARN": str,
        "FileShareId": str,
        "FileShareStatus": str,
        "GatewayARN": str,
        "KMSEncrypted": bool,
        "KMSKey": str,
        "Path": str,
        "Role": str,
        "LocationARN": str,
        "DefaultStorageClass": str,
        "ObjectACL": Literal[
            "private",
            "public-read",
            "public-read-write",
            "authenticated-read",
            "bucket-owner-read",
            "bucket-owner-full-control",
            "aws-exec-read",
        ],
        "ClientList": List[str],
        "Squash": str,
        "ReadOnly": bool,
        "GuessMIMETypeEnabled": bool,
        "RequesterPays": bool,
        "Tags": List[ClientDescribeNfsFileSharesResponseNFSFileShareInfoListTagsTypeDef],
    },
    total=False,
)

ClientDescribeNfsFileSharesResponseTypeDef = TypedDict(
    "ClientDescribeNfsFileSharesResponseTypeDef",
    {"NFSFileShareInfoList": List[ClientDescribeNfsFileSharesResponseNFSFileShareInfoListTypeDef]},
    total=False,
)

ClientDescribeSmbFileSharesResponseSMBFileShareInfoListTagsTypeDef = TypedDict(
    "ClientDescribeSmbFileSharesResponseSMBFileShareInfoListTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientDescribeSmbFileSharesResponseSMBFileShareInfoListTypeDef = TypedDict(
    "ClientDescribeSmbFileSharesResponseSMBFileShareInfoListTypeDef",
    {
        "FileShareARN": str,
        "FileShareId": str,
        "FileShareStatus": str,
        "GatewayARN": str,
        "KMSEncrypted": bool,
        "KMSKey": str,
        "Path": str,
        "Role": str,
        "LocationARN": str,
        "DefaultStorageClass": str,
        "ObjectACL": Literal[
            "private",
            "public-read",
            "public-read-write",
            "authenticated-read",
            "bucket-owner-read",
            "bucket-owner-full-control",
            "aws-exec-read",
        ],
        "ReadOnly": bool,
        "GuessMIMETypeEnabled": bool,
        "RequesterPays": bool,
        "SMBACLEnabled": bool,
        "AdminUserList": List[str],
        "ValidUserList": List[str],
        "InvalidUserList": List[str],
        "Authentication": str,
        "Tags": List[ClientDescribeSmbFileSharesResponseSMBFileShareInfoListTagsTypeDef],
    },
    total=False,
)

ClientDescribeSmbFileSharesResponseTypeDef = TypedDict(
    "ClientDescribeSmbFileSharesResponseTypeDef",
    {"SMBFileShareInfoList": List[ClientDescribeSmbFileSharesResponseSMBFileShareInfoListTypeDef]},
    total=False,
)

ClientDescribeSmbSettingsResponseTypeDef = TypedDict(
    "ClientDescribeSmbSettingsResponseTypeDef",
    {
        "GatewayARN": str,
        "DomainName": str,
        "ActiveDirectoryStatus": Literal[
            "ACCESS_DENIED",
            "DETACHED",
            "JOINED",
            "JOINING",
            "NETWORK_ERROR",
            "TIMEOUT",
            "UNKNOWN_ERROR",
        ],
        "SMBGuestPasswordSet": bool,
        "SMBSecurityStrategy": Literal[
            "ClientSpecified", "MandatorySigning", "MandatoryEncryption"
        ],
    },
    total=False,
)

ClientDescribeSnapshotScheduleResponseTagsTypeDef = TypedDict(
    "ClientDescribeSnapshotScheduleResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientDescribeSnapshotScheduleResponseTypeDef = TypedDict(
    "ClientDescribeSnapshotScheduleResponseTypeDef",
    {
        "VolumeARN": str,
        "StartAt": int,
        "RecurrenceInHours": int,
        "Description": str,
        "Timezone": str,
        "Tags": List[ClientDescribeSnapshotScheduleResponseTagsTypeDef],
    },
    total=False,
)

ClientDescribeStoredIscsiVolumesResponseStorediSCSIVolumesVolumeiSCSIAttributesTypeDef = TypedDict(
    "ClientDescribeStoredIscsiVolumesResponseStorediSCSIVolumesVolumeiSCSIAttributesTypeDef",
    {
        "TargetARN": str,
        "NetworkInterfaceId": str,
        "NetworkInterfacePort": int,
        "LunNumber": int,
        "ChapEnabled": bool,
    },
    total=False,
)

ClientDescribeStoredIscsiVolumesResponseStorediSCSIVolumesTypeDef = TypedDict(
    "ClientDescribeStoredIscsiVolumesResponseStorediSCSIVolumesTypeDef",
    {
        "VolumeARN": str,
        "VolumeId": str,
        "VolumeType": str,
        "VolumeStatus": str,
        "VolumeAttachmentStatus": str,
        "VolumeSizeInBytes": int,
        "VolumeProgress": float,
        "VolumeDiskId": str,
        "SourceSnapshotId": str,
        "PreservedExistingData": bool,
        "VolumeiSCSIAttributes": ClientDescribeStoredIscsiVolumesResponseStorediSCSIVolumesVolumeiSCSIAttributesTypeDef,
        "CreatedDate": datetime,
        "VolumeUsedInBytes": int,
        "KMSKey": str,
        "TargetName": str,
    },
    total=False,
)

ClientDescribeStoredIscsiVolumesResponseTypeDef = TypedDict(
    "ClientDescribeStoredIscsiVolumesResponseTypeDef",
    {"StorediSCSIVolumes": List[ClientDescribeStoredIscsiVolumesResponseStorediSCSIVolumesTypeDef]},
    total=False,
)

ClientDescribeTapeArchivesResponseTapeArchivesTypeDef = TypedDict(
    "ClientDescribeTapeArchivesResponseTapeArchivesTypeDef",
    {
        "TapeARN": str,
        "TapeBarcode": str,
        "TapeCreatedDate": datetime,
        "TapeSizeInBytes": int,
        "CompletionTime": datetime,
        "RetrievedTo": str,
        "TapeStatus": str,
        "TapeUsedInBytes": int,
        "KMSKey": str,
        "PoolId": str,
    },
    total=False,
)

ClientDescribeTapeArchivesResponseTypeDef = TypedDict(
    "ClientDescribeTapeArchivesResponseTypeDef",
    {"TapeArchives": List[ClientDescribeTapeArchivesResponseTapeArchivesTypeDef], "Marker": str},
    total=False,
)

ClientDescribeTapeRecoveryPointsResponseTapeRecoveryPointInfosTypeDef = TypedDict(
    "ClientDescribeTapeRecoveryPointsResponseTapeRecoveryPointInfosTypeDef",
    {"TapeARN": str, "TapeRecoveryPointTime": datetime, "TapeSizeInBytes": int, "TapeStatus": str},
    total=False,
)

ClientDescribeTapeRecoveryPointsResponseTypeDef = TypedDict(
    "ClientDescribeTapeRecoveryPointsResponseTypeDef",
    {
        "GatewayARN": str,
        "TapeRecoveryPointInfos": List[
            ClientDescribeTapeRecoveryPointsResponseTapeRecoveryPointInfosTypeDef
        ],
        "Marker": str,
    },
    total=False,
)

ClientDescribeTapesResponseTapesTypeDef = TypedDict(
    "ClientDescribeTapesResponseTapesTypeDef",
    {
        "TapeARN": str,
        "TapeBarcode": str,
        "TapeCreatedDate": datetime,
        "TapeSizeInBytes": int,
        "TapeStatus": str,
        "VTLDevice": str,
        "Progress": float,
        "TapeUsedInBytes": int,
        "KMSKey": str,
        "PoolId": str,
    },
    total=False,
)

ClientDescribeTapesResponseTypeDef = TypedDict(
    "ClientDescribeTapesResponseTypeDef",
    {"Tapes": List[ClientDescribeTapesResponseTapesTypeDef], "Marker": str},
    total=False,
)

ClientDescribeUploadBufferResponseTypeDef = TypedDict(
    "ClientDescribeUploadBufferResponseTypeDef",
    {
        "GatewayARN": str,
        "DiskIds": List[str],
        "UploadBufferUsedInBytes": int,
        "UploadBufferAllocatedInBytes": int,
    },
    total=False,
)

ClientDescribeVtlDevicesResponseVTLDevicesDeviceiSCSIAttributesTypeDef = TypedDict(
    "ClientDescribeVtlDevicesResponseVTLDevicesDeviceiSCSIAttributesTypeDef",
    {"TargetARN": str, "NetworkInterfaceId": str, "NetworkInterfacePort": int, "ChapEnabled": bool},
    total=False,
)

ClientDescribeVtlDevicesResponseVTLDevicesTypeDef = TypedDict(
    "ClientDescribeVtlDevicesResponseVTLDevicesTypeDef",
    {
        "VTLDeviceARN": str,
        "VTLDeviceType": str,
        "VTLDeviceVendor": str,
        "VTLDeviceProductIdentifier": str,
        "DeviceiSCSIAttributes": ClientDescribeVtlDevicesResponseVTLDevicesDeviceiSCSIAttributesTypeDef,
    },
    total=False,
)

ClientDescribeVtlDevicesResponseTypeDef = TypedDict(
    "ClientDescribeVtlDevicesResponseTypeDef",
    {
        "GatewayARN": str,
        "VTLDevices": List[ClientDescribeVtlDevicesResponseVTLDevicesTypeDef],
        "Marker": str,
    },
    total=False,
)

ClientDescribeWorkingStorageResponseTypeDef = TypedDict(
    "ClientDescribeWorkingStorageResponseTypeDef",
    {
        "GatewayARN": str,
        "DiskIds": List[str],
        "WorkingStorageUsedInBytes": int,
        "WorkingStorageAllocatedInBytes": int,
    },
    total=False,
)

ClientDetachVolumeResponseTypeDef = TypedDict(
    "ClientDetachVolumeResponseTypeDef", {"VolumeARN": str}, total=False
)

ClientDisableGatewayResponseTypeDef = TypedDict(
    "ClientDisableGatewayResponseTypeDef", {"GatewayARN": str}, total=False
)

ClientJoinDomainResponseTypeDef = TypedDict(
    "ClientJoinDomainResponseTypeDef",
    {
        "GatewayARN": str,
        "ActiveDirectoryStatus": Literal[
            "ACCESS_DENIED",
            "DETACHED",
            "JOINED",
            "JOINING",
            "NETWORK_ERROR",
            "TIMEOUT",
            "UNKNOWN_ERROR",
        ],
    },
    total=False,
)

ClientListFileSharesResponseFileShareInfoListTypeDef = TypedDict(
    "ClientListFileSharesResponseFileShareInfoListTypeDef",
    {
        "FileShareType": Literal["NFS", "SMB"],
        "FileShareARN": str,
        "FileShareId": str,
        "FileShareStatus": str,
        "GatewayARN": str,
    },
    total=False,
)

ClientListFileSharesResponseTypeDef = TypedDict(
    "ClientListFileSharesResponseTypeDef",
    {
        "Marker": str,
        "NextMarker": str,
        "FileShareInfoList": List[ClientListFileSharesResponseFileShareInfoListTypeDef],
    },
    total=False,
)

ClientListGatewaysResponseGatewaysTypeDef = TypedDict(
    "ClientListGatewaysResponseGatewaysTypeDef",
    {
        "GatewayId": str,
        "GatewayARN": str,
        "GatewayType": str,
        "GatewayOperationalState": str,
        "GatewayName": str,
        "Ec2InstanceId": str,
        "Ec2InstanceRegion": str,
    },
    total=False,
)

ClientListGatewaysResponseTypeDef = TypedDict(
    "ClientListGatewaysResponseTypeDef",
    {"Gateways": List[ClientListGatewaysResponseGatewaysTypeDef], "Marker": str},
    total=False,
)

ClientListLocalDisksResponseDisksTypeDef = TypedDict(
    "ClientListLocalDisksResponseDisksTypeDef",
    {
        "DiskId": str,
        "DiskPath": str,
        "DiskNode": str,
        "DiskStatus": str,
        "DiskSizeInBytes": int,
        "DiskAllocationType": str,
        "DiskAllocationResource": str,
        "DiskAttributeList": List[str],
    },
    total=False,
)

ClientListLocalDisksResponseTypeDef = TypedDict(
    "ClientListLocalDisksResponseTypeDef",
    {"GatewayARN": str, "Disks": List[ClientListLocalDisksResponseDisksTypeDef]},
    total=False,
)

ClientListTagsForResourceResponseTagsTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientListTagsForResourceResponseTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTypeDef",
    {"ResourceARN": str, "Marker": str, "Tags": List[ClientListTagsForResourceResponseTagsTypeDef]},
    total=False,
)

ClientListTapesResponseTapeInfosTypeDef = TypedDict(
    "ClientListTapesResponseTapeInfosTypeDef",
    {
        "TapeARN": str,
        "TapeBarcode": str,
        "TapeSizeInBytes": int,
        "TapeStatus": str,
        "GatewayARN": str,
        "PoolId": str,
    },
    total=False,
)

ClientListTapesResponseTypeDef = TypedDict(
    "ClientListTapesResponseTypeDef",
    {"TapeInfos": List[ClientListTapesResponseTapeInfosTypeDef], "Marker": str},
    total=False,
)

ClientListVolumeInitiatorsResponseTypeDef = TypedDict(
    "ClientListVolumeInitiatorsResponseTypeDef", {"Initiators": List[str]}, total=False
)

ClientListVolumeRecoveryPointsResponseVolumeRecoveryPointInfosTypeDef = TypedDict(
    "ClientListVolumeRecoveryPointsResponseVolumeRecoveryPointInfosTypeDef",
    {
        "VolumeARN": str,
        "VolumeSizeInBytes": int,
        "VolumeUsageInBytes": int,
        "VolumeRecoveryPointTime": str,
    },
    total=False,
)

ClientListVolumeRecoveryPointsResponseTypeDef = TypedDict(
    "ClientListVolumeRecoveryPointsResponseTypeDef",
    {
        "GatewayARN": str,
        "VolumeRecoveryPointInfos": List[
            ClientListVolumeRecoveryPointsResponseVolumeRecoveryPointInfosTypeDef
        ],
    },
    total=False,
)

ClientListVolumesResponseVolumeInfosTypeDef = TypedDict(
    "ClientListVolumesResponseVolumeInfosTypeDef",
    {
        "VolumeARN": str,
        "VolumeId": str,
        "GatewayARN": str,
        "GatewayId": str,
        "VolumeType": str,
        "VolumeSizeInBytes": int,
        "VolumeAttachmentStatus": str,
    },
    total=False,
)

ClientListVolumesResponseTypeDef = TypedDict(
    "ClientListVolumesResponseTypeDef",
    {
        "GatewayARN": str,
        "Marker": str,
        "VolumeInfos": List[ClientListVolumesResponseVolumeInfosTypeDef],
    },
    total=False,
)

ClientNotifyWhenUploadedResponseTypeDef = TypedDict(
    "ClientNotifyWhenUploadedResponseTypeDef",
    {"FileShareARN": str, "NotificationId": str},
    total=False,
)

ClientRefreshCacheResponseTypeDef = TypedDict(
    "ClientRefreshCacheResponseTypeDef", {"FileShareARN": str, "NotificationId": str}, total=False
)

ClientRemoveTagsFromResourceResponseTypeDef = TypedDict(
    "ClientRemoveTagsFromResourceResponseTypeDef", {"ResourceARN": str}, total=False
)

ClientResetCacheResponseTypeDef = TypedDict(
    "ClientResetCacheResponseTypeDef", {"GatewayARN": str}, total=False
)

ClientRetrieveTapeArchiveResponseTypeDef = TypedDict(
    "ClientRetrieveTapeArchiveResponseTypeDef", {"TapeARN": str}, total=False
)

ClientRetrieveTapeRecoveryPointResponseTypeDef = TypedDict(
    "ClientRetrieveTapeRecoveryPointResponseTypeDef", {"TapeARN": str}, total=False
)

ClientSetLocalConsolePasswordResponseTypeDef = TypedDict(
    "ClientSetLocalConsolePasswordResponseTypeDef", {"GatewayARN": str}, total=False
)

ClientSetSmbGuestPasswordResponseTypeDef = TypedDict(
    "ClientSetSmbGuestPasswordResponseTypeDef", {"GatewayARN": str}, total=False
)

ClientShutdownGatewayResponseTypeDef = TypedDict(
    "ClientShutdownGatewayResponseTypeDef", {"GatewayARN": str}, total=False
)

ClientStartAvailabilityMonitorTestResponseTypeDef = TypedDict(
    "ClientStartAvailabilityMonitorTestResponseTypeDef", {"GatewayARN": str}, total=False
)

ClientStartGatewayResponseTypeDef = TypedDict(
    "ClientStartGatewayResponseTypeDef", {"GatewayARN": str}, total=False
)

ClientUpdateBandwidthRateLimitResponseTypeDef = TypedDict(
    "ClientUpdateBandwidthRateLimitResponseTypeDef", {"GatewayARN": str}, total=False
)

ClientUpdateChapCredentialsResponseTypeDef = TypedDict(
    "ClientUpdateChapCredentialsResponseTypeDef",
    {"TargetARN": str, "InitiatorName": str},
    total=False,
)

ClientUpdateGatewayInformationResponseTypeDef = TypedDict(
    "ClientUpdateGatewayInformationResponseTypeDef",
    {"GatewayARN": str, "GatewayName": str},
    total=False,
)

ClientUpdateGatewaySoftwareNowResponseTypeDef = TypedDict(
    "ClientUpdateGatewaySoftwareNowResponseTypeDef", {"GatewayARN": str}, total=False
)

ClientUpdateMaintenanceStartTimeResponseTypeDef = TypedDict(
    "ClientUpdateMaintenanceStartTimeResponseTypeDef", {"GatewayARN": str}, total=False
)

ClientUpdateNfsFileShareNFSFileShareDefaultsTypeDef = TypedDict(
    "ClientUpdateNfsFileShareNFSFileShareDefaultsTypeDef",
    {"FileMode": str, "DirectoryMode": str, "GroupId": int, "OwnerId": int},
    total=False,
)

ClientUpdateNfsFileShareResponseTypeDef = TypedDict(
    "ClientUpdateNfsFileShareResponseTypeDef", {"FileShareARN": str}, total=False
)

ClientUpdateSmbFileShareResponseTypeDef = TypedDict(
    "ClientUpdateSmbFileShareResponseTypeDef", {"FileShareARN": str}, total=False
)

ClientUpdateSmbSecurityStrategyResponseTypeDef = TypedDict(
    "ClientUpdateSmbSecurityStrategyResponseTypeDef", {"GatewayARN": str}, total=False
)

ClientUpdateSnapshotScheduleResponseTypeDef = TypedDict(
    "ClientUpdateSnapshotScheduleResponseTypeDef", {"VolumeARN": str}, total=False
)

ClientUpdateSnapshotScheduleTagsTypeDef = TypedDict(
    "ClientUpdateSnapshotScheduleTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientUpdateVtlDeviceTypeResponseTypeDef = TypedDict(
    "ClientUpdateVtlDeviceTypeResponseTypeDef", {"VTLDeviceARN": str}, total=False
)

TapeArchiveTypeDef = TypedDict(
    "TapeArchiveTypeDef",
    {
        "TapeARN": str,
        "TapeBarcode": str,
        "TapeCreatedDate": datetime,
        "TapeSizeInBytes": int,
        "CompletionTime": datetime,
        "RetrievedTo": str,
        "TapeStatus": str,
        "TapeUsedInBytes": int,
        "KMSKey": str,
        "PoolId": str,
    },
    total=False,
)

DescribeTapeArchivesOutputTypeDef = TypedDict(
    "DescribeTapeArchivesOutputTypeDef",
    {"TapeArchives": List[TapeArchiveTypeDef], "Marker": str},
    total=False,
)

TapeRecoveryPointInfoTypeDef = TypedDict(
    "TapeRecoveryPointInfoTypeDef",
    {"TapeARN": str, "TapeRecoveryPointTime": datetime, "TapeSizeInBytes": int, "TapeStatus": str},
    total=False,
)

DescribeTapeRecoveryPointsOutputTypeDef = TypedDict(
    "DescribeTapeRecoveryPointsOutputTypeDef",
    {
        "GatewayARN": str,
        "TapeRecoveryPointInfos": List[TapeRecoveryPointInfoTypeDef],
        "Marker": str,
    },
    total=False,
)

TapeTypeDef = TypedDict(
    "TapeTypeDef",
    {
        "TapeARN": str,
        "TapeBarcode": str,
        "TapeCreatedDate": datetime,
        "TapeSizeInBytes": int,
        "TapeStatus": str,
        "VTLDevice": str,
        "Progress": float,
        "TapeUsedInBytes": int,
        "KMSKey": str,
        "PoolId": str,
    },
    total=False,
)

DescribeTapesOutputTypeDef = TypedDict(
    "DescribeTapesOutputTypeDef", {"Tapes": List[TapeTypeDef], "Marker": str}, total=False
)

DeviceiSCSIAttributesTypeDef = TypedDict(
    "DeviceiSCSIAttributesTypeDef",
    {"TargetARN": str, "NetworkInterfaceId": str, "NetworkInterfacePort": int, "ChapEnabled": bool},
    total=False,
)

VTLDeviceTypeDef = TypedDict(
    "VTLDeviceTypeDef",
    {
        "VTLDeviceARN": str,
        "VTLDeviceType": str,
        "VTLDeviceVendor": str,
        "VTLDeviceProductIdentifier": str,
        "DeviceiSCSIAttributes": DeviceiSCSIAttributesTypeDef,
    },
    total=False,
)

DescribeVTLDevicesOutputTypeDef = TypedDict(
    "DescribeVTLDevicesOutputTypeDef",
    {"GatewayARN": str, "VTLDevices": List[VTLDeviceTypeDef], "Marker": str},
    total=False,
)

FileShareInfoTypeDef = TypedDict(
    "FileShareInfoTypeDef",
    {
        "FileShareType": Literal["NFS", "SMB"],
        "FileShareARN": str,
        "FileShareId": str,
        "FileShareStatus": str,
        "GatewayARN": str,
    },
    total=False,
)

ListFileSharesOutputTypeDef = TypedDict(
    "ListFileSharesOutputTypeDef",
    {"Marker": str, "NextMarker": str, "FileShareInfoList": List[FileShareInfoTypeDef]},
    total=False,
)

GatewayInfoTypeDef = TypedDict(
    "GatewayInfoTypeDef",
    {
        "GatewayId": str,
        "GatewayARN": str,
        "GatewayType": str,
        "GatewayOperationalState": str,
        "GatewayName": str,
        "Ec2InstanceId": str,
        "Ec2InstanceRegion": str,
    },
    total=False,
)

ListGatewaysOutputTypeDef = TypedDict(
    "ListGatewaysOutputTypeDef", {"Gateways": List[GatewayInfoTypeDef], "Marker": str}, total=False
)

TagTypeDef = TypedDict("TagTypeDef", {"Key": str, "Value": str})

ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
    {"ResourceARN": str, "Marker": str, "Tags": List[TagTypeDef]},
    total=False,
)

TapeInfoTypeDef = TypedDict(
    "TapeInfoTypeDef",
    {
        "TapeARN": str,
        "TapeBarcode": str,
        "TapeSizeInBytes": int,
        "TapeStatus": str,
        "GatewayARN": str,
        "PoolId": str,
    },
    total=False,
)

ListTapesOutputTypeDef = TypedDict(
    "ListTapesOutputTypeDef", {"TapeInfos": List[TapeInfoTypeDef], "Marker": str}, total=False
)

VolumeInfoTypeDef = TypedDict(
    "VolumeInfoTypeDef",
    {
        "VolumeARN": str,
        "VolumeId": str,
        "GatewayARN": str,
        "GatewayId": str,
        "VolumeType": str,
        "VolumeSizeInBytes": int,
        "VolumeAttachmentStatus": str,
    },
    total=False,
)

ListVolumesOutputTypeDef = TypedDict(
    "ListVolumesOutputTypeDef",
    {"GatewayARN": str, "Marker": str, "VolumeInfos": List[VolumeInfoTypeDef]},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)
