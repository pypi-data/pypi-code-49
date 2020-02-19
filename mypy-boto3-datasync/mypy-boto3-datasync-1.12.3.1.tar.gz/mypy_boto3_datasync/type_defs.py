"""
Main interface for datasync service type definitions.

Usage::

    from mypy_boto3.datasync.type_defs import ClientCreateAgentResponseTypeDef

    data: ClientCreateAgentResponseTypeDef = {...}
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
    "ClientCreateAgentResponseTypeDef",
    "ClientCreateAgentTagsTypeDef",
    "ClientCreateLocationEfsEc2ConfigTypeDef",
    "ClientCreateLocationEfsResponseTypeDef",
    "ClientCreateLocationEfsTagsTypeDef",
    "ClientCreateLocationFsxWindowsResponseTypeDef",
    "ClientCreateLocationFsxWindowsTagsTypeDef",
    "ClientCreateLocationNfsMountOptionsTypeDef",
    "ClientCreateLocationNfsOnPremConfigTypeDef",
    "ClientCreateLocationNfsResponseTypeDef",
    "ClientCreateLocationNfsTagsTypeDef",
    "ClientCreateLocationS3ResponseTypeDef",
    "ClientCreateLocationS3S3ConfigTypeDef",
    "ClientCreateLocationS3TagsTypeDef",
    "ClientCreateLocationSmbMountOptionsTypeDef",
    "ClientCreateLocationSmbResponseTypeDef",
    "ClientCreateLocationSmbTagsTypeDef",
    "ClientCreateTaskExcludesTypeDef",
    "ClientCreateTaskOptionsTypeDef",
    "ClientCreateTaskResponseTypeDef",
    "ClientCreateTaskScheduleTypeDef",
    "ClientCreateTaskTagsTypeDef",
    "ClientDescribeAgentResponsePrivateLinkConfigTypeDef",
    "ClientDescribeAgentResponseTypeDef",
    "ClientDescribeLocationEfsResponseEc2ConfigTypeDef",
    "ClientDescribeLocationEfsResponseTypeDef",
    "ClientDescribeLocationFsxWindowsResponseTypeDef",
    "ClientDescribeLocationNfsResponseMountOptionsTypeDef",
    "ClientDescribeLocationNfsResponseOnPremConfigTypeDef",
    "ClientDescribeLocationNfsResponseTypeDef",
    "ClientDescribeLocationS3ResponseS3ConfigTypeDef",
    "ClientDescribeLocationS3ResponseTypeDef",
    "ClientDescribeLocationSmbResponseMountOptionsTypeDef",
    "ClientDescribeLocationSmbResponseTypeDef",
    "ClientDescribeTaskExecutionResponseExcludesTypeDef",
    "ClientDescribeTaskExecutionResponseIncludesTypeDef",
    "ClientDescribeTaskExecutionResponseOptionsTypeDef",
    "ClientDescribeTaskExecutionResponseResultTypeDef",
    "ClientDescribeTaskExecutionResponseTypeDef",
    "ClientDescribeTaskResponseExcludesTypeDef",
    "ClientDescribeTaskResponseOptionsTypeDef",
    "ClientDescribeTaskResponseScheduleTypeDef",
    "ClientDescribeTaskResponseTypeDef",
    "ClientListAgentsResponseAgentsTypeDef",
    "ClientListAgentsResponseTypeDef",
    "ClientListLocationsResponseLocationsTypeDef",
    "ClientListLocationsResponseTypeDef",
    "ClientListTagsForResourceResponseTagsTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientListTaskExecutionsResponseTaskExecutionsTypeDef",
    "ClientListTaskExecutionsResponseTypeDef",
    "ClientListTasksResponseTasksTypeDef",
    "ClientListTasksResponseTypeDef",
    "ClientStartTaskExecutionIncludesTypeDef",
    "ClientStartTaskExecutionOverrideOptionsTypeDef",
    "ClientStartTaskExecutionResponseTypeDef",
    "ClientTagResourceTagsTypeDef",
    "ClientUpdateTaskExcludesTypeDef",
    "ClientUpdateTaskOptionsTypeDef",
    "ClientUpdateTaskScheduleTypeDef",
    "AgentListEntryTypeDef",
    "ListAgentsResponseTypeDef",
    "LocationListEntryTypeDef",
    "ListLocationsResponseTypeDef",
    "TagListEntryTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "TaskExecutionListEntryTypeDef",
    "ListTaskExecutionsResponseTypeDef",
    "TaskListEntryTypeDef",
    "ListTasksResponseTypeDef",
    "PaginatorConfigTypeDef",
)

ClientCreateAgentResponseTypeDef = TypedDict(
    "ClientCreateAgentResponseTypeDef", {"AgentArn": str}, total=False
)

ClientCreateAgentTagsTypeDef = TypedDict(
    "ClientCreateAgentTagsTypeDef", {"Key": str, "Value": str}, total=False
)

_RequiredClientCreateLocationEfsEc2ConfigTypeDef = TypedDict(
    "_RequiredClientCreateLocationEfsEc2ConfigTypeDef", {"SubnetArn": str}
)
_OptionalClientCreateLocationEfsEc2ConfigTypeDef = TypedDict(
    "_OptionalClientCreateLocationEfsEc2ConfigTypeDef",
    {"SecurityGroupArns": List[str]},
    total=False,
)


class ClientCreateLocationEfsEc2ConfigTypeDef(
    _RequiredClientCreateLocationEfsEc2ConfigTypeDef,
    _OptionalClientCreateLocationEfsEc2ConfigTypeDef,
):
    pass


ClientCreateLocationEfsResponseTypeDef = TypedDict(
    "ClientCreateLocationEfsResponseTypeDef", {"LocationArn": str}, total=False
)

_RequiredClientCreateLocationEfsTagsTypeDef = TypedDict(
    "_RequiredClientCreateLocationEfsTagsTypeDef", {"Key": str}
)
_OptionalClientCreateLocationEfsTagsTypeDef = TypedDict(
    "_OptionalClientCreateLocationEfsTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateLocationEfsTagsTypeDef(
    _RequiredClientCreateLocationEfsTagsTypeDef, _OptionalClientCreateLocationEfsTagsTypeDef
):
    pass


ClientCreateLocationFsxWindowsResponseTypeDef = TypedDict(
    "ClientCreateLocationFsxWindowsResponseTypeDef", {"LocationArn": str}, total=False
)

_RequiredClientCreateLocationFsxWindowsTagsTypeDef = TypedDict(
    "_RequiredClientCreateLocationFsxWindowsTagsTypeDef", {"Key": str}
)
_OptionalClientCreateLocationFsxWindowsTagsTypeDef = TypedDict(
    "_OptionalClientCreateLocationFsxWindowsTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateLocationFsxWindowsTagsTypeDef(
    _RequiredClientCreateLocationFsxWindowsTagsTypeDef,
    _OptionalClientCreateLocationFsxWindowsTagsTypeDef,
):
    pass


ClientCreateLocationNfsMountOptionsTypeDef = TypedDict(
    "ClientCreateLocationNfsMountOptionsTypeDef",
    {"Version": Literal["AUTOMATIC", "NFS3", "NFS4_0", "NFS4_1"]},
    total=False,
)

ClientCreateLocationNfsOnPremConfigTypeDef = TypedDict(
    "ClientCreateLocationNfsOnPremConfigTypeDef", {"AgentArns": List[str]}
)

ClientCreateLocationNfsResponseTypeDef = TypedDict(
    "ClientCreateLocationNfsResponseTypeDef", {"LocationArn": str}, total=False
)

_RequiredClientCreateLocationNfsTagsTypeDef = TypedDict(
    "_RequiredClientCreateLocationNfsTagsTypeDef", {"Key": str}
)
_OptionalClientCreateLocationNfsTagsTypeDef = TypedDict(
    "_OptionalClientCreateLocationNfsTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateLocationNfsTagsTypeDef(
    _RequiredClientCreateLocationNfsTagsTypeDef, _OptionalClientCreateLocationNfsTagsTypeDef
):
    pass


ClientCreateLocationS3ResponseTypeDef = TypedDict(
    "ClientCreateLocationS3ResponseTypeDef", {"LocationArn": str}, total=False
)

ClientCreateLocationS3S3ConfigTypeDef = TypedDict(
    "ClientCreateLocationS3S3ConfigTypeDef", {"BucketAccessRoleArn": str}
)

_RequiredClientCreateLocationS3TagsTypeDef = TypedDict(
    "_RequiredClientCreateLocationS3TagsTypeDef", {"Key": str}
)
_OptionalClientCreateLocationS3TagsTypeDef = TypedDict(
    "_OptionalClientCreateLocationS3TagsTypeDef", {"Value": str}, total=False
)


class ClientCreateLocationS3TagsTypeDef(
    _RequiredClientCreateLocationS3TagsTypeDef, _OptionalClientCreateLocationS3TagsTypeDef
):
    pass


ClientCreateLocationSmbMountOptionsTypeDef = TypedDict(
    "ClientCreateLocationSmbMountOptionsTypeDef",
    {"Version": Literal["AUTOMATIC", "SMB2", "SMB3"]},
    total=False,
)

ClientCreateLocationSmbResponseTypeDef = TypedDict(
    "ClientCreateLocationSmbResponseTypeDef", {"LocationArn": str}, total=False
)

_RequiredClientCreateLocationSmbTagsTypeDef = TypedDict(
    "_RequiredClientCreateLocationSmbTagsTypeDef", {"Key": str}
)
_OptionalClientCreateLocationSmbTagsTypeDef = TypedDict(
    "_OptionalClientCreateLocationSmbTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateLocationSmbTagsTypeDef(
    _RequiredClientCreateLocationSmbTagsTypeDef, _OptionalClientCreateLocationSmbTagsTypeDef
):
    pass


ClientCreateTaskExcludesTypeDef = TypedDict(
    "ClientCreateTaskExcludesTypeDef", {"FilterType": str, "Value": str}, total=False
)

ClientCreateTaskOptionsTypeDef = TypedDict(
    "ClientCreateTaskOptionsTypeDef",
    {
        "VerifyMode": Literal["POINT_IN_TIME_CONSISTENT", "ONLY_FILES_TRANSFERRED", "NONE"],
        "OverwriteMode": Literal["ALWAYS", "NEVER"],
        "Atime": Literal["NONE", "BEST_EFFORT"],
        "Mtime": Literal["NONE", "PRESERVE"],
        "Uid": Literal["NONE", "INT_VALUE", "NAME", "BOTH"],
        "Gid": Literal["NONE", "INT_VALUE", "NAME", "BOTH"],
        "PreserveDeletedFiles": Literal["PRESERVE", "REMOVE"],
        "PreserveDevices": Literal["NONE", "PRESERVE"],
        "PosixPermissions": Literal["NONE", "PRESERVE"],
        "BytesPerSecond": int,
        "TaskQueueing": Literal["ENABLED", "DISABLED"],
        "LogLevel": Literal["OFF", "BASIC", "TRANSFER"],
    },
    total=False,
)

ClientCreateTaskResponseTypeDef = TypedDict(
    "ClientCreateTaskResponseTypeDef", {"TaskArn": str}, total=False
)

ClientCreateTaskScheduleTypeDef = TypedDict(
    "ClientCreateTaskScheduleTypeDef", {"ScheduleExpression": str}
)

_RequiredClientCreateTaskTagsTypeDef = TypedDict(
    "_RequiredClientCreateTaskTagsTypeDef", {"Key": str}
)
_OptionalClientCreateTaskTagsTypeDef = TypedDict(
    "_OptionalClientCreateTaskTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateTaskTagsTypeDef(
    _RequiredClientCreateTaskTagsTypeDef, _OptionalClientCreateTaskTagsTypeDef
):
    pass


ClientDescribeAgentResponsePrivateLinkConfigTypeDef = TypedDict(
    "ClientDescribeAgentResponsePrivateLinkConfigTypeDef",
    {
        "VpcEndpointId": str,
        "PrivateLinkEndpoint": str,
        "SubnetArns": List[str],
        "SecurityGroupArns": List[str],
    },
    total=False,
)

ClientDescribeAgentResponseTypeDef = TypedDict(
    "ClientDescribeAgentResponseTypeDef",
    {
        "AgentArn": str,
        "Name": str,
        "Status": Literal["ONLINE", "OFFLINE"],
        "LastConnectionTime": datetime,
        "CreationTime": datetime,
        "EndpointType": Literal["PUBLIC", "PRIVATE_LINK", "FIPS"],
        "PrivateLinkConfig": ClientDescribeAgentResponsePrivateLinkConfigTypeDef,
    },
    total=False,
)

ClientDescribeLocationEfsResponseEc2ConfigTypeDef = TypedDict(
    "ClientDescribeLocationEfsResponseEc2ConfigTypeDef",
    {"SubnetArn": str, "SecurityGroupArns": List[str]},
    total=False,
)

ClientDescribeLocationEfsResponseTypeDef = TypedDict(
    "ClientDescribeLocationEfsResponseTypeDef",
    {
        "LocationArn": str,
        "LocationUri": str,
        "Ec2Config": ClientDescribeLocationEfsResponseEc2ConfigTypeDef,
        "CreationTime": datetime,
    },
    total=False,
)

ClientDescribeLocationFsxWindowsResponseTypeDef = TypedDict(
    "ClientDescribeLocationFsxWindowsResponseTypeDef",
    {
        "LocationArn": str,
        "LocationUri": str,
        "SecurityGroupArns": List[str],
        "CreationTime": datetime,
        "User": str,
        "Domain": str,
    },
    total=False,
)

ClientDescribeLocationNfsResponseMountOptionsTypeDef = TypedDict(
    "ClientDescribeLocationNfsResponseMountOptionsTypeDef",
    {"Version": Literal["AUTOMATIC", "NFS3", "NFS4_0", "NFS4_1"]},
    total=False,
)

ClientDescribeLocationNfsResponseOnPremConfigTypeDef = TypedDict(
    "ClientDescribeLocationNfsResponseOnPremConfigTypeDef", {"AgentArns": List[str]}, total=False
)

ClientDescribeLocationNfsResponseTypeDef = TypedDict(
    "ClientDescribeLocationNfsResponseTypeDef",
    {
        "LocationArn": str,
        "LocationUri": str,
        "OnPremConfig": ClientDescribeLocationNfsResponseOnPremConfigTypeDef,
        "MountOptions": ClientDescribeLocationNfsResponseMountOptionsTypeDef,
        "CreationTime": datetime,
    },
    total=False,
)

ClientDescribeLocationS3ResponseS3ConfigTypeDef = TypedDict(
    "ClientDescribeLocationS3ResponseS3ConfigTypeDef", {"BucketAccessRoleArn": str}, total=False
)

ClientDescribeLocationS3ResponseTypeDef = TypedDict(
    "ClientDescribeLocationS3ResponseTypeDef",
    {
        "LocationArn": str,
        "LocationUri": str,
        "S3StorageClass": Literal[
            "STANDARD",
            "STANDARD_IA",
            "ONEZONE_IA",
            "INTELLIGENT_TIERING",
            "GLACIER",
            "DEEP_ARCHIVE",
        ],
        "S3Config": ClientDescribeLocationS3ResponseS3ConfigTypeDef,
        "CreationTime": datetime,
    },
    total=False,
)

ClientDescribeLocationSmbResponseMountOptionsTypeDef = TypedDict(
    "ClientDescribeLocationSmbResponseMountOptionsTypeDef",
    {"Version": Literal["AUTOMATIC", "SMB2", "SMB3"]},
    total=False,
)

ClientDescribeLocationSmbResponseTypeDef = TypedDict(
    "ClientDescribeLocationSmbResponseTypeDef",
    {
        "LocationArn": str,
        "LocationUri": str,
        "AgentArns": List[str],
        "User": str,
        "Domain": str,
        "MountOptions": ClientDescribeLocationSmbResponseMountOptionsTypeDef,
        "CreationTime": datetime,
    },
    total=False,
)

ClientDescribeTaskExecutionResponseExcludesTypeDef = TypedDict(
    "ClientDescribeTaskExecutionResponseExcludesTypeDef",
    {"FilterType": str, "Value": str},
    total=False,
)

ClientDescribeTaskExecutionResponseIncludesTypeDef = TypedDict(
    "ClientDescribeTaskExecutionResponseIncludesTypeDef",
    {"FilterType": str, "Value": str},
    total=False,
)

ClientDescribeTaskExecutionResponseOptionsTypeDef = TypedDict(
    "ClientDescribeTaskExecutionResponseOptionsTypeDef",
    {
        "VerifyMode": Literal["POINT_IN_TIME_CONSISTENT", "ONLY_FILES_TRANSFERRED", "NONE"],
        "OverwriteMode": Literal["ALWAYS", "NEVER"],
        "Atime": Literal["NONE", "BEST_EFFORT"],
        "Mtime": Literal["NONE", "PRESERVE"],
        "Uid": Literal["NONE", "INT_VALUE", "NAME", "BOTH"],
        "Gid": Literal["NONE", "INT_VALUE", "NAME", "BOTH"],
        "PreserveDeletedFiles": Literal["PRESERVE", "REMOVE"],
        "PreserveDevices": Literal["NONE", "PRESERVE"],
        "PosixPermissions": Literal["NONE", "PRESERVE"],
        "BytesPerSecond": int,
        "TaskQueueing": Literal["ENABLED", "DISABLED"],
        "LogLevel": Literal["OFF", "BASIC", "TRANSFER"],
    },
    total=False,
)

ClientDescribeTaskExecutionResponseResultTypeDef = TypedDict(
    "ClientDescribeTaskExecutionResponseResultTypeDef",
    {
        "PrepareDuration": int,
        "PrepareStatus": Literal["PENDING", "SUCCESS", "ERROR"],
        "TotalDuration": int,
        "TransferDuration": int,
        "TransferStatus": Literal["PENDING", "SUCCESS", "ERROR"],
        "VerifyDuration": int,
        "VerifyStatus": Literal["PENDING", "SUCCESS", "ERROR"],
        "ErrorCode": str,
        "ErrorDetail": str,
    },
    total=False,
)

ClientDescribeTaskExecutionResponseTypeDef = TypedDict(
    "ClientDescribeTaskExecutionResponseTypeDef",
    {
        "TaskExecutionArn": str,
        "Status": Literal[
            "QUEUED", "LAUNCHING", "PREPARING", "TRANSFERRING", "VERIFYING", "SUCCESS", "ERROR"
        ],
        "Options": ClientDescribeTaskExecutionResponseOptionsTypeDef,
        "Excludes": List[ClientDescribeTaskExecutionResponseExcludesTypeDef],
        "Includes": List[ClientDescribeTaskExecutionResponseIncludesTypeDef],
        "StartTime": datetime,
        "EstimatedFilesToTransfer": int,
        "EstimatedBytesToTransfer": int,
        "FilesTransferred": int,
        "BytesWritten": int,
        "BytesTransferred": int,
        "Result": ClientDescribeTaskExecutionResponseResultTypeDef,
    },
    total=False,
)

ClientDescribeTaskResponseExcludesTypeDef = TypedDict(
    "ClientDescribeTaskResponseExcludesTypeDef", {"FilterType": str, "Value": str}, total=False
)

ClientDescribeTaskResponseOptionsTypeDef = TypedDict(
    "ClientDescribeTaskResponseOptionsTypeDef",
    {
        "VerifyMode": Literal["POINT_IN_TIME_CONSISTENT", "ONLY_FILES_TRANSFERRED", "NONE"],
        "OverwriteMode": Literal["ALWAYS", "NEVER"],
        "Atime": Literal["NONE", "BEST_EFFORT"],
        "Mtime": Literal["NONE", "PRESERVE"],
        "Uid": Literal["NONE", "INT_VALUE", "NAME", "BOTH"],
        "Gid": Literal["NONE", "INT_VALUE", "NAME", "BOTH"],
        "PreserveDeletedFiles": Literal["PRESERVE", "REMOVE"],
        "PreserveDevices": Literal["NONE", "PRESERVE"],
        "PosixPermissions": Literal["NONE", "PRESERVE"],
        "BytesPerSecond": int,
        "TaskQueueing": Literal["ENABLED", "DISABLED"],
        "LogLevel": Literal["OFF", "BASIC", "TRANSFER"],
    },
    total=False,
)

ClientDescribeTaskResponseScheduleTypeDef = TypedDict(
    "ClientDescribeTaskResponseScheduleTypeDef", {"ScheduleExpression": str}, total=False
)

ClientDescribeTaskResponseTypeDef = TypedDict(
    "ClientDescribeTaskResponseTypeDef",
    {
        "TaskArn": str,
        "Status": Literal["AVAILABLE", "CREATING", "QUEUED", "RUNNING", "UNAVAILABLE"],
        "Name": str,
        "CurrentTaskExecutionArn": str,
        "SourceLocationArn": str,
        "DestinationLocationArn": str,
        "CloudWatchLogGroupArn": str,
        "SourceNetworkInterfaceArns": List[str],
        "DestinationNetworkInterfaceArns": List[str],
        "Options": ClientDescribeTaskResponseOptionsTypeDef,
        "Excludes": List[ClientDescribeTaskResponseExcludesTypeDef],
        "Schedule": ClientDescribeTaskResponseScheduleTypeDef,
        "ErrorCode": str,
        "ErrorDetail": str,
        "CreationTime": datetime,
    },
    total=False,
)

ClientListAgentsResponseAgentsTypeDef = TypedDict(
    "ClientListAgentsResponseAgentsTypeDef",
    {"AgentArn": str, "Name": str, "Status": Literal["ONLINE", "OFFLINE"]},
    total=False,
)

ClientListAgentsResponseTypeDef = TypedDict(
    "ClientListAgentsResponseTypeDef",
    {"Agents": List[ClientListAgentsResponseAgentsTypeDef], "NextToken": str},
    total=False,
)

ClientListLocationsResponseLocationsTypeDef = TypedDict(
    "ClientListLocationsResponseLocationsTypeDef",
    {"LocationArn": str, "LocationUri": str},
    total=False,
)

ClientListLocationsResponseTypeDef = TypedDict(
    "ClientListLocationsResponseTypeDef",
    {"Locations": List[ClientListLocationsResponseLocationsTypeDef], "NextToken": str},
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

ClientListTaskExecutionsResponseTaskExecutionsTypeDef = TypedDict(
    "ClientListTaskExecutionsResponseTaskExecutionsTypeDef",
    {
        "TaskExecutionArn": str,
        "Status": Literal[
            "QUEUED", "LAUNCHING", "PREPARING", "TRANSFERRING", "VERIFYING", "SUCCESS", "ERROR"
        ],
    },
    total=False,
)

ClientListTaskExecutionsResponseTypeDef = TypedDict(
    "ClientListTaskExecutionsResponseTypeDef",
    {
        "TaskExecutions": List[ClientListTaskExecutionsResponseTaskExecutionsTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientListTasksResponseTasksTypeDef = TypedDict(
    "ClientListTasksResponseTasksTypeDef",
    {
        "TaskArn": str,
        "Status": Literal["AVAILABLE", "CREATING", "QUEUED", "RUNNING", "UNAVAILABLE"],
        "Name": str,
    },
    total=False,
)

ClientListTasksResponseTypeDef = TypedDict(
    "ClientListTasksResponseTypeDef",
    {"Tasks": List[ClientListTasksResponseTasksTypeDef], "NextToken": str},
    total=False,
)

ClientStartTaskExecutionIncludesTypeDef = TypedDict(
    "ClientStartTaskExecutionIncludesTypeDef", {"FilterType": str, "Value": str}, total=False
)

ClientStartTaskExecutionOverrideOptionsTypeDef = TypedDict(
    "ClientStartTaskExecutionOverrideOptionsTypeDef",
    {
        "VerifyMode": Literal["POINT_IN_TIME_CONSISTENT", "ONLY_FILES_TRANSFERRED", "NONE"],
        "OverwriteMode": Literal["ALWAYS", "NEVER"],
        "Atime": Literal["NONE", "BEST_EFFORT"],
        "Mtime": Literal["NONE", "PRESERVE"],
        "Uid": Literal["NONE", "INT_VALUE", "NAME", "BOTH"],
        "Gid": Literal["NONE", "INT_VALUE", "NAME", "BOTH"],
        "PreserveDeletedFiles": Literal["PRESERVE", "REMOVE"],
        "PreserveDevices": Literal["NONE", "PRESERVE"],
        "PosixPermissions": Literal["NONE", "PRESERVE"],
        "BytesPerSecond": int,
        "TaskQueueing": Literal["ENABLED", "DISABLED"],
        "LogLevel": Literal["OFF", "BASIC", "TRANSFER"],
    },
    total=False,
)

ClientStartTaskExecutionResponseTypeDef = TypedDict(
    "ClientStartTaskExecutionResponseTypeDef", {"TaskExecutionArn": str}, total=False
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


ClientUpdateTaskExcludesTypeDef = TypedDict(
    "ClientUpdateTaskExcludesTypeDef", {"FilterType": str, "Value": str}, total=False
)

ClientUpdateTaskOptionsTypeDef = TypedDict(
    "ClientUpdateTaskOptionsTypeDef",
    {
        "VerifyMode": Literal["POINT_IN_TIME_CONSISTENT", "ONLY_FILES_TRANSFERRED", "NONE"],
        "OverwriteMode": Literal["ALWAYS", "NEVER"],
        "Atime": Literal["NONE", "BEST_EFFORT"],
        "Mtime": Literal["NONE", "PRESERVE"],
        "Uid": Literal["NONE", "INT_VALUE", "NAME", "BOTH"],
        "Gid": Literal["NONE", "INT_VALUE", "NAME", "BOTH"],
        "PreserveDeletedFiles": Literal["PRESERVE", "REMOVE"],
        "PreserveDevices": Literal["NONE", "PRESERVE"],
        "PosixPermissions": Literal["NONE", "PRESERVE"],
        "BytesPerSecond": int,
        "TaskQueueing": Literal["ENABLED", "DISABLED"],
        "LogLevel": Literal["OFF", "BASIC", "TRANSFER"],
    },
    total=False,
)

ClientUpdateTaskScheduleTypeDef = TypedDict(
    "ClientUpdateTaskScheduleTypeDef", {"ScheduleExpression": str}
)

AgentListEntryTypeDef = TypedDict(
    "AgentListEntryTypeDef",
    {"AgentArn": str, "Name": str, "Status": Literal["ONLINE", "OFFLINE"]},
    total=False,
)

ListAgentsResponseTypeDef = TypedDict(
    "ListAgentsResponseTypeDef",
    {"Agents": List[AgentListEntryTypeDef], "NextToken": str},
    total=False,
)

LocationListEntryTypeDef = TypedDict(
    "LocationListEntryTypeDef", {"LocationArn": str, "LocationUri": str}, total=False
)

ListLocationsResponseTypeDef = TypedDict(
    "ListLocationsResponseTypeDef",
    {"Locations": List[LocationListEntryTypeDef], "NextToken": str},
    total=False,
)

_RequiredTagListEntryTypeDef = TypedDict("_RequiredTagListEntryTypeDef", {"Key": str})
_OptionalTagListEntryTypeDef = TypedDict(
    "_OptionalTagListEntryTypeDef", {"Value": str}, total=False
)


class TagListEntryTypeDef(_RequiredTagListEntryTypeDef, _OptionalTagListEntryTypeDef):
    pass


ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {"Tags": List[TagListEntryTypeDef], "NextToken": str},
    total=False,
)

TaskExecutionListEntryTypeDef = TypedDict(
    "TaskExecutionListEntryTypeDef",
    {
        "TaskExecutionArn": str,
        "Status": Literal[
            "QUEUED", "LAUNCHING", "PREPARING", "TRANSFERRING", "VERIFYING", "SUCCESS", "ERROR"
        ],
    },
    total=False,
)

ListTaskExecutionsResponseTypeDef = TypedDict(
    "ListTaskExecutionsResponseTypeDef",
    {"TaskExecutions": List[TaskExecutionListEntryTypeDef], "NextToken": str},
    total=False,
)

TaskListEntryTypeDef = TypedDict(
    "TaskListEntryTypeDef",
    {
        "TaskArn": str,
        "Status": Literal["AVAILABLE", "CREATING", "QUEUED", "RUNNING", "UNAVAILABLE"],
        "Name": str,
    },
    total=False,
)

ListTasksResponseTypeDef = TypedDict(
    "ListTasksResponseTypeDef", {"Tasks": List[TaskListEntryTypeDef], "NextToken": str}, total=False
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)
