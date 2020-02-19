"""
Main interface for efs service type definitions.

Usage::

    from mypy_boto3.efs.type_defs import ClientCreateAccessPointPosixUserTypeDef

    data: ClientCreateAccessPointPosixUserTypeDef = {...}
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
    "ClientCreateAccessPointPosixUserTypeDef",
    "ClientCreateAccessPointResponsePosixUserTypeDef",
    "ClientCreateAccessPointResponseRootDirectoryCreationInfoTypeDef",
    "ClientCreateAccessPointResponseRootDirectoryTypeDef",
    "ClientCreateAccessPointResponseTagsTypeDef",
    "ClientCreateAccessPointResponseTypeDef",
    "ClientCreateAccessPointRootDirectoryCreationInfoTypeDef",
    "ClientCreateAccessPointRootDirectoryTypeDef",
    "ClientCreateAccessPointTagsTypeDef",
    "ClientCreateFileSystemResponseSizeInBytesTypeDef",
    "ClientCreateFileSystemResponseTagsTypeDef",
    "ClientCreateFileSystemResponseTypeDef",
    "ClientCreateFileSystemTagsTypeDef",
    "ClientCreateMountTargetResponseTypeDef",
    "ClientCreateTagsTagsTypeDef",
    "ClientDescribeAccessPointsResponseAccessPointsPosixUserTypeDef",
    "ClientDescribeAccessPointsResponseAccessPointsRootDirectoryCreationInfoTypeDef",
    "ClientDescribeAccessPointsResponseAccessPointsRootDirectoryTypeDef",
    "ClientDescribeAccessPointsResponseAccessPointsTagsTypeDef",
    "ClientDescribeAccessPointsResponseAccessPointsTypeDef",
    "ClientDescribeAccessPointsResponseTypeDef",
    "ClientDescribeFileSystemPolicyResponseTypeDef",
    "ClientDescribeFileSystemsResponseFileSystemsSizeInBytesTypeDef",
    "ClientDescribeFileSystemsResponseFileSystemsTagsTypeDef",
    "ClientDescribeFileSystemsResponseFileSystemsTypeDef",
    "ClientDescribeFileSystemsResponseTypeDef",
    "ClientDescribeLifecycleConfigurationResponseLifecyclePoliciesTypeDef",
    "ClientDescribeLifecycleConfigurationResponseTypeDef",
    "ClientDescribeMountTargetSecurityGroupsResponseTypeDef",
    "ClientDescribeMountTargetsResponseMountTargetsTypeDef",
    "ClientDescribeMountTargetsResponseTypeDef",
    "ClientDescribeTagsResponseTagsTypeDef",
    "ClientDescribeTagsResponseTypeDef",
    "ClientListTagsForResourceResponseTagsTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientPutFileSystemPolicyResponseTypeDef",
    "ClientPutLifecycleConfigurationLifecyclePoliciesTypeDef",
    "ClientPutLifecycleConfigurationResponseLifecyclePoliciesTypeDef",
    "ClientPutLifecycleConfigurationResponseTypeDef",
    "ClientTagResourceTagsTypeDef",
    "ClientUpdateFileSystemResponseSizeInBytesTypeDef",
    "ClientUpdateFileSystemResponseTagsTypeDef",
    "ClientUpdateFileSystemResponseTypeDef",
    "FileSystemSizeTypeDef",
    "TagTypeDef",
    "FileSystemDescriptionTypeDef",
    "DescribeFileSystemsResponseTypeDef",
    "MountTargetDescriptionTypeDef",
    "DescribeMountTargetsResponseTypeDef",
    "DescribeTagsResponseTypeDef",
    "PaginatorConfigTypeDef",
)

_RequiredClientCreateAccessPointPosixUserTypeDef = TypedDict(
    "_RequiredClientCreateAccessPointPosixUserTypeDef", {"Uid": int}
)
_OptionalClientCreateAccessPointPosixUserTypeDef = TypedDict(
    "_OptionalClientCreateAccessPointPosixUserTypeDef",
    {"Gid": int, "SecondaryGids": List[int]},
    total=False,
)


class ClientCreateAccessPointPosixUserTypeDef(
    _RequiredClientCreateAccessPointPosixUserTypeDef,
    _OptionalClientCreateAccessPointPosixUserTypeDef,
):
    pass


ClientCreateAccessPointResponsePosixUserTypeDef = TypedDict(
    "ClientCreateAccessPointResponsePosixUserTypeDef",
    {"Uid": int, "Gid": int, "SecondaryGids": List[int]},
    total=False,
)

ClientCreateAccessPointResponseRootDirectoryCreationInfoTypeDef = TypedDict(
    "ClientCreateAccessPointResponseRootDirectoryCreationInfoTypeDef",
    {"OwnerUid": int, "OwnerGid": int, "Permissions": str},
    total=False,
)

ClientCreateAccessPointResponseRootDirectoryTypeDef = TypedDict(
    "ClientCreateAccessPointResponseRootDirectoryTypeDef",
    {"Path": str, "CreationInfo": ClientCreateAccessPointResponseRootDirectoryCreationInfoTypeDef},
    total=False,
)

ClientCreateAccessPointResponseTagsTypeDef = TypedDict(
    "ClientCreateAccessPointResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreateAccessPointResponseTypeDef = TypedDict(
    "ClientCreateAccessPointResponseTypeDef",
    {
        "ClientToken": str,
        "Name": str,
        "Tags": List[ClientCreateAccessPointResponseTagsTypeDef],
        "AccessPointId": str,
        "AccessPointArn": str,
        "FileSystemId": str,
        "PosixUser": ClientCreateAccessPointResponsePosixUserTypeDef,
        "RootDirectory": ClientCreateAccessPointResponseRootDirectoryTypeDef,
        "OwnerId": str,
        "LifeCycleState": Literal["creating", "available", "updating", "deleting", "deleted"],
    },
    total=False,
)

ClientCreateAccessPointRootDirectoryCreationInfoTypeDef = TypedDict(
    "ClientCreateAccessPointRootDirectoryCreationInfoTypeDef",
    {"OwnerUid": int, "OwnerGid": int, "Permissions": str},
    total=False,
)

ClientCreateAccessPointRootDirectoryTypeDef = TypedDict(
    "ClientCreateAccessPointRootDirectoryTypeDef",
    {"Path": str, "CreationInfo": ClientCreateAccessPointRootDirectoryCreationInfoTypeDef},
    total=False,
)

_RequiredClientCreateAccessPointTagsTypeDef = TypedDict(
    "_RequiredClientCreateAccessPointTagsTypeDef", {"Key": str}
)
_OptionalClientCreateAccessPointTagsTypeDef = TypedDict(
    "_OptionalClientCreateAccessPointTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateAccessPointTagsTypeDef(
    _RequiredClientCreateAccessPointTagsTypeDef, _OptionalClientCreateAccessPointTagsTypeDef
):
    pass


ClientCreateFileSystemResponseSizeInBytesTypeDef = TypedDict(
    "ClientCreateFileSystemResponseSizeInBytesTypeDef",
    {"Value": int, "Timestamp": datetime, "ValueInIA": int, "ValueInStandard": int},
    total=False,
)

ClientCreateFileSystemResponseTagsTypeDef = TypedDict(
    "ClientCreateFileSystemResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreateFileSystemResponseTypeDef = TypedDict(
    "ClientCreateFileSystemResponseTypeDef",
    {
        "OwnerId": str,
        "CreationToken": str,
        "FileSystemId": str,
        "CreationTime": datetime,
        "LifeCycleState": Literal["creating", "available", "updating", "deleting", "deleted"],
        "Name": str,
        "NumberOfMountTargets": int,
        "SizeInBytes": ClientCreateFileSystemResponseSizeInBytesTypeDef,
        "PerformanceMode": Literal["generalPurpose", "maxIO"],
        "Encrypted": bool,
        "KmsKeyId": str,
        "ThroughputMode": Literal["bursting", "provisioned"],
        "ProvisionedThroughputInMibps": float,
        "Tags": List[ClientCreateFileSystemResponseTagsTypeDef],
    },
    total=False,
)

_RequiredClientCreateFileSystemTagsTypeDef = TypedDict(
    "_RequiredClientCreateFileSystemTagsTypeDef", {"Key": str}
)
_OptionalClientCreateFileSystemTagsTypeDef = TypedDict(
    "_OptionalClientCreateFileSystemTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateFileSystemTagsTypeDef(
    _RequiredClientCreateFileSystemTagsTypeDef, _OptionalClientCreateFileSystemTagsTypeDef
):
    pass


ClientCreateMountTargetResponseTypeDef = TypedDict(
    "ClientCreateMountTargetResponseTypeDef",
    {
        "OwnerId": str,
        "MountTargetId": str,
        "FileSystemId": str,
        "SubnetId": str,
        "LifeCycleState": Literal["creating", "available", "updating", "deleting", "deleted"],
        "IpAddress": str,
        "NetworkInterfaceId": str,
        "AvailabilityZoneId": str,
        "AvailabilityZoneName": str,
    },
    total=False,
)

_RequiredClientCreateTagsTagsTypeDef = TypedDict(
    "_RequiredClientCreateTagsTagsTypeDef", {"Key": str}
)
_OptionalClientCreateTagsTagsTypeDef = TypedDict(
    "_OptionalClientCreateTagsTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateTagsTagsTypeDef(
    _RequiredClientCreateTagsTagsTypeDef, _OptionalClientCreateTagsTagsTypeDef
):
    pass


ClientDescribeAccessPointsResponseAccessPointsPosixUserTypeDef = TypedDict(
    "ClientDescribeAccessPointsResponseAccessPointsPosixUserTypeDef",
    {"Uid": int, "Gid": int, "SecondaryGids": List[int]},
    total=False,
)

ClientDescribeAccessPointsResponseAccessPointsRootDirectoryCreationInfoTypeDef = TypedDict(
    "ClientDescribeAccessPointsResponseAccessPointsRootDirectoryCreationInfoTypeDef",
    {"OwnerUid": int, "OwnerGid": int, "Permissions": str},
    total=False,
)

ClientDescribeAccessPointsResponseAccessPointsRootDirectoryTypeDef = TypedDict(
    "ClientDescribeAccessPointsResponseAccessPointsRootDirectoryTypeDef",
    {
        "Path": str,
        "CreationInfo": ClientDescribeAccessPointsResponseAccessPointsRootDirectoryCreationInfoTypeDef,
    },
    total=False,
)

ClientDescribeAccessPointsResponseAccessPointsTagsTypeDef = TypedDict(
    "ClientDescribeAccessPointsResponseAccessPointsTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientDescribeAccessPointsResponseAccessPointsTypeDef = TypedDict(
    "ClientDescribeAccessPointsResponseAccessPointsTypeDef",
    {
        "ClientToken": str,
        "Name": str,
        "Tags": List[ClientDescribeAccessPointsResponseAccessPointsTagsTypeDef],
        "AccessPointId": str,
        "AccessPointArn": str,
        "FileSystemId": str,
        "PosixUser": ClientDescribeAccessPointsResponseAccessPointsPosixUserTypeDef,
        "RootDirectory": ClientDescribeAccessPointsResponseAccessPointsRootDirectoryTypeDef,
        "OwnerId": str,
        "LifeCycleState": Literal["creating", "available", "updating", "deleting", "deleted"],
    },
    total=False,
)

ClientDescribeAccessPointsResponseTypeDef = TypedDict(
    "ClientDescribeAccessPointsResponseTypeDef",
    {"AccessPoints": List[ClientDescribeAccessPointsResponseAccessPointsTypeDef], "NextToken": str},
    total=False,
)

ClientDescribeFileSystemPolicyResponseTypeDef = TypedDict(
    "ClientDescribeFileSystemPolicyResponseTypeDef",
    {"FileSystemId": str, "Policy": str},
    total=False,
)

ClientDescribeFileSystemsResponseFileSystemsSizeInBytesTypeDef = TypedDict(
    "ClientDescribeFileSystemsResponseFileSystemsSizeInBytesTypeDef",
    {"Value": int, "Timestamp": datetime, "ValueInIA": int, "ValueInStandard": int},
    total=False,
)

ClientDescribeFileSystemsResponseFileSystemsTagsTypeDef = TypedDict(
    "ClientDescribeFileSystemsResponseFileSystemsTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientDescribeFileSystemsResponseFileSystemsTypeDef = TypedDict(
    "ClientDescribeFileSystemsResponseFileSystemsTypeDef",
    {
        "OwnerId": str,
        "CreationToken": str,
        "FileSystemId": str,
        "CreationTime": datetime,
        "LifeCycleState": Literal["creating", "available", "updating", "deleting", "deleted"],
        "Name": str,
        "NumberOfMountTargets": int,
        "SizeInBytes": ClientDescribeFileSystemsResponseFileSystemsSizeInBytesTypeDef,
        "PerformanceMode": Literal["generalPurpose", "maxIO"],
        "Encrypted": bool,
        "KmsKeyId": str,
        "ThroughputMode": Literal["bursting", "provisioned"],
        "ProvisionedThroughputInMibps": float,
        "Tags": List[ClientDescribeFileSystemsResponseFileSystemsTagsTypeDef],
    },
    total=False,
)

ClientDescribeFileSystemsResponseTypeDef = TypedDict(
    "ClientDescribeFileSystemsResponseTypeDef",
    {
        "Marker": str,
        "FileSystems": List[ClientDescribeFileSystemsResponseFileSystemsTypeDef],
        "NextMarker": str,
    },
    total=False,
)

ClientDescribeLifecycleConfigurationResponseLifecyclePoliciesTypeDef = TypedDict(
    "ClientDescribeLifecycleConfigurationResponseLifecyclePoliciesTypeDef",
    {
        "TransitionToIA": Literal[
            "AFTER_7_DAYS", "AFTER_14_DAYS", "AFTER_30_DAYS", "AFTER_60_DAYS", "AFTER_90_DAYS"
        ]
    },
    total=False,
)

ClientDescribeLifecycleConfigurationResponseTypeDef = TypedDict(
    "ClientDescribeLifecycleConfigurationResponseTypeDef",
    {
        "LifecyclePolicies": List[
            ClientDescribeLifecycleConfigurationResponseLifecyclePoliciesTypeDef
        ]
    },
    total=False,
)

ClientDescribeMountTargetSecurityGroupsResponseTypeDef = TypedDict(
    "ClientDescribeMountTargetSecurityGroupsResponseTypeDef",
    {"SecurityGroups": List[str]},
    total=False,
)

ClientDescribeMountTargetsResponseMountTargetsTypeDef = TypedDict(
    "ClientDescribeMountTargetsResponseMountTargetsTypeDef",
    {
        "OwnerId": str,
        "MountTargetId": str,
        "FileSystemId": str,
        "SubnetId": str,
        "LifeCycleState": Literal["creating", "available", "updating", "deleting", "deleted"],
        "IpAddress": str,
        "NetworkInterfaceId": str,
        "AvailabilityZoneId": str,
        "AvailabilityZoneName": str,
    },
    total=False,
)

ClientDescribeMountTargetsResponseTypeDef = TypedDict(
    "ClientDescribeMountTargetsResponseTypeDef",
    {
        "Marker": str,
        "MountTargets": List[ClientDescribeMountTargetsResponseMountTargetsTypeDef],
        "NextMarker": str,
    },
    total=False,
)

ClientDescribeTagsResponseTagsTypeDef = TypedDict(
    "ClientDescribeTagsResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientDescribeTagsResponseTypeDef = TypedDict(
    "ClientDescribeTagsResponseTypeDef",
    {"Marker": str, "Tags": List[ClientDescribeTagsResponseTagsTypeDef], "NextMarker": str},
    total=False,
)

ClientListTagsForResourceResponseTagsTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientListTagsForResourceResponseTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTypeDef",
    {"Tags": List[ClientListTagsForResourceResponseTagsTypeDef], "NextToken": str},
    total=False,
)

ClientPutFileSystemPolicyResponseTypeDef = TypedDict(
    "ClientPutFileSystemPolicyResponseTypeDef", {"FileSystemId": str, "Policy": str}, total=False
)

ClientPutLifecycleConfigurationLifecyclePoliciesTypeDef = TypedDict(
    "ClientPutLifecycleConfigurationLifecyclePoliciesTypeDef",
    {
        "TransitionToIA": Literal[
            "AFTER_7_DAYS", "AFTER_14_DAYS", "AFTER_30_DAYS", "AFTER_60_DAYS", "AFTER_90_DAYS"
        ]
    },
    total=False,
)

ClientPutLifecycleConfigurationResponseLifecyclePoliciesTypeDef = TypedDict(
    "ClientPutLifecycleConfigurationResponseLifecyclePoliciesTypeDef",
    {
        "TransitionToIA": Literal[
            "AFTER_7_DAYS", "AFTER_14_DAYS", "AFTER_30_DAYS", "AFTER_60_DAYS", "AFTER_90_DAYS"
        ]
    },
    total=False,
)

ClientPutLifecycleConfigurationResponseTypeDef = TypedDict(
    "ClientPutLifecycleConfigurationResponseTypeDef",
    {"LifecyclePolicies": List[ClientPutLifecycleConfigurationResponseLifecyclePoliciesTypeDef]},
    total=False,
)

_RequiredClientTagResourceTagsTypeDef = TypedDict(
    "_RequiredClientTagResourceTagsTypeDef", {"Key": str}
)
_OptionalClientTagResourceTagsTypeDef = TypedDict(
    "_OptionalClientTagResourceTagsTypeDef", {"Value": str}, total=False
)


class ClientTagResourceTagsTypeDef(
    _RequiredClientTagResourceTagsTypeDef, _OptionalClientTagResourceTagsTypeDef
):
    pass


ClientUpdateFileSystemResponseSizeInBytesTypeDef = TypedDict(
    "ClientUpdateFileSystemResponseSizeInBytesTypeDef",
    {"Value": int, "Timestamp": datetime, "ValueInIA": int, "ValueInStandard": int},
    total=False,
)

ClientUpdateFileSystemResponseTagsTypeDef = TypedDict(
    "ClientUpdateFileSystemResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientUpdateFileSystemResponseTypeDef = TypedDict(
    "ClientUpdateFileSystemResponseTypeDef",
    {
        "OwnerId": str,
        "CreationToken": str,
        "FileSystemId": str,
        "CreationTime": datetime,
        "LifeCycleState": Literal["creating", "available", "updating", "deleting", "deleted"],
        "Name": str,
        "NumberOfMountTargets": int,
        "SizeInBytes": ClientUpdateFileSystemResponseSizeInBytesTypeDef,
        "PerformanceMode": Literal["generalPurpose", "maxIO"],
        "Encrypted": bool,
        "KmsKeyId": str,
        "ThroughputMode": Literal["bursting", "provisioned"],
        "ProvisionedThroughputInMibps": float,
        "Tags": List[ClientUpdateFileSystemResponseTagsTypeDef],
    },
    total=False,
)

_RequiredFileSystemSizeTypeDef = TypedDict("_RequiredFileSystemSizeTypeDef", {"Value": int})
_OptionalFileSystemSizeTypeDef = TypedDict(
    "_OptionalFileSystemSizeTypeDef",
    {"Timestamp": datetime, "ValueInIA": int, "ValueInStandard": int},
    total=False,
)


class FileSystemSizeTypeDef(_RequiredFileSystemSizeTypeDef, _OptionalFileSystemSizeTypeDef):
    pass


TagTypeDef = TypedDict("TagTypeDef", {"Key": str, "Value": str})

_RequiredFileSystemDescriptionTypeDef = TypedDict(
    "_RequiredFileSystemDescriptionTypeDef",
    {
        "OwnerId": str,
        "CreationToken": str,
        "FileSystemId": str,
        "CreationTime": datetime,
        "LifeCycleState": Literal["creating", "available", "updating", "deleting", "deleted"],
        "NumberOfMountTargets": int,
        "SizeInBytes": FileSystemSizeTypeDef,
        "PerformanceMode": Literal["generalPurpose", "maxIO"],
        "Tags": List[TagTypeDef],
    },
)
_OptionalFileSystemDescriptionTypeDef = TypedDict(
    "_OptionalFileSystemDescriptionTypeDef",
    {
        "Name": str,
        "Encrypted": bool,
        "KmsKeyId": str,
        "ThroughputMode": Literal["bursting", "provisioned"],
        "ProvisionedThroughputInMibps": float,
    },
    total=False,
)


class FileSystemDescriptionTypeDef(
    _RequiredFileSystemDescriptionTypeDef, _OptionalFileSystemDescriptionTypeDef
):
    pass


DescribeFileSystemsResponseTypeDef = TypedDict(
    "DescribeFileSystemsResponseTypeDef",
    {"Marker": str, "FileSystems": List[FileSystemDescriptionTypeDef], "NextMarker": str},
    total=False,
)

_RequiredMountTargetDescriptionTypeDef = TypedDict(
    "_RequiredMountTargetDescriptionTypeDef",
    {
        "MountTargetId": str,
        "FileSystemId": str,
        "SubnetId": str,
        "LifeCycleState": Literal["creating", "available", "updating", "deleting", "deleted"],
    },
)
_OptionalMountTargetDescriptionTypeDef = TypedDict(
    "_OptionalMountTargetDescriptionTypeDef",
    {
        "OwnerId": str,
        "IpAddress": str,
        "NetworkInterfaceId": str,
        "AvailabilityZoneId": str,
        "AvailabilityZoneName": str,
    },
    total=False,
)


class MountTargetDescriptionTypeDef(
    _RequiredMountTargetDescriptionTypeDef, _OptionalMountTargetDescriptionTypeDef
):
    pass


DescribeMountTargetsResponseTypeDef = TypedDict(
    "DescribeMountTargetsResponseTypeDef",
    {"Marker": str, "MountTargets": List[MountTargetDescriptionTypeDef], "NextMarker": str},
    total=False,
)

_RequiredDescribeTagsResponseTypeDef = TypedDict(
    "_RequiredDescribeTagsResponseTypeDef", {"Tags": List[TagTypeDef]}
)
_OptionalDescribeTagsResponseTypeDef = TypedDict(
    "_OptionalDescribeTagsResponseTypeDef", {"Marker": str, "NextMarker": str}, total=False
)


class DescribeTagsResponseTypeDef(
    _RequiredDescribeTagsResponseTypeDef, _OptionalDescribeTagsResponseTypeDef
):
    pass


PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)
