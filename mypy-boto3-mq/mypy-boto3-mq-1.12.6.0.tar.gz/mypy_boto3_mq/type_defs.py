"""
Main interface for mq service type definitions.

Usage::

    from mypy_boto3.mq.type_defs import ClientCreateBrokerConfigurationTypeDef

    data: ClientCreateBrokerConfigurationTypeDef = {...}
"""
from datetime import datetime
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
    "ClientCreateBrokerConfigurationTypeDef",
    "ClientCreateBrokerEncryptionOptionsTypeDef",
    "ClientCreateBrokerLogsTypeDef",
    "ClientCreateBrokerMaintenanceWindowStartTimeTypeDef",
    "ClientCreateBrokerResponseTypeDef",
    "ClientCreateBrokerUsersTypeDef",
    "ClientCreateConfigurationResponseLatestRevisionTypeDef",
    "ClientCreateConfigurationResponseTypeDef",
    "ClientDeleteBrokerResponseTypeDef",
    "ClientDescribeBrokerEngineTypesResponseBrokerEngineTypesEngineVersionsTypeDef",
    "ClientDescribeBrokerEngineTypesResponseBrokerEngineTypesTypeDef",
    "ClientDescribeBrokerEngineTypesResponseTypeDef",
    "ClientDescribeBrokerInstanceOptionsResponseBrokerInstanceOptionsAvailabilityZonesTypeDef",
    "ClientDescribeBrokerInstanceOptionsResponseBrokerInstanceOptionsTypeDef",
    "ClientDescribeBrokerInstanceOptionsResponseTypeDef",
    "ClientDescribeBrokerResponseBrokerInstancesTypeDef",
    "ClientDescribeBrokerResponseConfigurationsCurrentTypeDef",
    "ClientDescribeBrokerResponseConfigurationsHistoryTypeDef",
    "ClientDescribeBrokerResponseConfigurationsPendingTypeDef",
    "ClientDescribeBrokerResponseConfigurationsTypeDef",
    "ClientDescribeBrokerResponseEncryptionOptionsTypeDef",
    "ClientDescribeBrokerResponseLogsPendingTypeDef",
    "ClientDescribeBrokerResponseLogsTypeDef",
    "ClientDescribeBrokerResponseMaintenanceWindowStartTimeTypeDef",
    "ClientDescribeBrokerResponseUsersTypeDef",
    "ClientDescribeBrokerResponseTypeDef",
    "ClientDescribeConfigurationResponseLatestRevisionTypeDef",
    "ClientDescribeConfigurationResponseTypeDef",
    "ClientDescribeConfigurationRevisionResponseTypeDef",
    "ClientDescribeUserResponsePendingTypeDef",
    "ClientDescribeUserResponseTypeDef",
    "ClientListBrokersResponseBrokerSummariesTypeDef",
    "ClientListBrokersResponseTypeDef",
    "ClientListConfigurationRevisionsResponseRevisionsTypeDef",
    "ClientListConfigurationRevisionsResponseTypeDef",
    "ClientListConfigurationsResponseConfigurationsLatestRevisionTypeDef",
    "ClientListConfigurationsResponseConfigurationsTypeDef",
    "ClientListConfigurationsResponseTypeDef",
    "ClientListTagsResponseTypeDef",
    "ClientListUsersResponseUsersTypeDef",
    "ClientListUsersResponseTypeDef",
    "ClientUpdateBrokerConfigurationTypeDef",
    "ClientUpdateBrokerLogsTypeDef",
    "ClientUpdateBrokerResponseConfigurationTypeDef",
    "ClientUpdateBrokerResponseLogsTypeDef",
    "ClientUpdateBrokerResponseTypeDef",
    "ClientUpdateConfigurationResponseLatestRevisionTypeDef",
    "ClientUpdateConfigurationResponseWarningsTypeDef",
    "ClientUpdateConfigurationResponseTypeDef",
    "BrokerSummaryTypeDef",
    "ListBrokersResponseTypeDef",
    "PaginatorConfigTypeDef",
)

ClientCreateBrokerConfigurationTypeDef = TypedDict(
    "ClientCreateBrokerConfigurationTypeDef", {"Id": str, "Revision": int}, total=False
)

_RequiredClientCreateBrokerEncryptionOptionsTypeDef = TypedDict(
    "_RequiredClientCreateBrokerEncryptionOptionsTypeDef", {"UseAwsOwnedKey": bool}
)
_OptionalClientCreateBrokerEncryptionOptionsTypeDef = TypedDict(
    "_OptionalClientCreateBrokerEncryptionOptionsTypeDef", {"KmsKeyId": str}, total=False
)


class ClientCreateBrokerEncryptionOptionsTypeDef(
    _RequiredClientCreateBrokerEncryptionOptionsTypeDef,
    _OptionalClientCreateBrokerEncryptionOptionsTypeDef,
):
    pass


ClientCreateBrokerLogsTypeDef = TypedDict(
    "ClientCreateBrokerLogsTypeDef", {"Audit": bool, "General": bool}, total=False
)

ClientCreateBrokerMaintenanceWindowStartTimeTypeDef = TypedDict(
    "ClientCreateBrokerMaintenanceWindowStartTimeTypeDef",
    {
        "DayOfWeek": Literal[
            "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"
        ],
        "TimeOfDay": str,
        "TimeZone": str,
    },
    total=False,
)

ClientCreateBrokerResponseTypeDef = TypedDict(
    "ClientCreateBrokerResponseTypeDef", {"BrokerArn": str, "BrokerId": str}, total=False
)

ClientCreateBrokerUsersTypeDef = TypedDict(
    "ClientCreateBrokerUsersTypeDef",
    {"ConsoleAccess": bool, "Groups": List[str], "Password": str, "Username": str},
    total=False,
)

ClientCreateConfigurationResponseLatestRevisionTypeDef = TypedDict(
    "ClientCreateConfigurationResponseLatestRevisionTypeDef",
    {"Created": datetime, "Description": str, "Revision": int},
    total=False,
)

ClientCreateConfigurationResponseTypeDef = TypedDict(
    "ClientCreateConfigurationResponseTypeDef",
    {
        "Arn": str,
        "Created": datetime,
        "Id": str,
        "LatestRevision": ClientCreateConfigurationResponseLatestRevisionTypeDef,
        "Name": str,
    },
    total=False,
)

ClientDeleteBrokerResponseTypeDef = TypedDict(
    "ClientDeleteBrokerResponseTypeDef", {"BrokerId": str}, total=False
)

ClientDescribeBrokerEngineTypesResponseBrokerEngineTypesEngineVersionsTypeDef = TypedDict(
    "ClientDescribeBrokerEngineTypesResponseBrokerEngineTypesEngineVersionsTypeDef",
    {"Name": str},
    total=False,
)

ClientDescribeBrokerEngineTypesResponseBrokerEngineTypesTypeDef = TypedDict(
    "ClientDescribeBrokerEngineTypesResponseBrokerEngineTypesTypeDef",
    {
        "EngineType": str,
        "EngineVersions": List[
            ClientDescribeBrokerEngineTypesResponseBrokerEngineTypesEngineVersionsTypeDef
        ],
    },
    total=False,
)

ClientDescribeBrokerEngineTypesResponseTypeDef = TypedDict(
    "ClientDescribeBrokerEngineTypesResponseTypeDef",
    {
        "BrokerEngineTypes": List[ClientDescribeBrokerEngineTypesResponseBrokerEngineTypesTypeDef],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ClientDescribeBrokerInstanceOptionsResponseBrokerInstanceOptionsAvailabilityZonesTypeDef = TypedDict(
    "ClientDescribeBrokerInstanceOptionsResponseBrokerInstanceOptionsAvailabilityZonesTypeDef",
    {"Name": str},
    total=False,
)

ClientDescribeBrokerInstanceOptionsResponseBrokerInstanceOptionsTypeDef = TypedDict(
    "ClientDescribeBrokerInstanceOptionsResponseBrokerInstanceOptionsTypeDef",
    {
        "AvailabilityZones": List[
            ClientDescribeBrokerInstanceOptionsResponseBrokerInstanceOptionsAvailabilityZonesTypeDef
        ],
        "EngineType": str,
        "HostInstanceType": str,
        "StorageType": Literal["EBS", "EFS"],
        "SupportedDeploymentModes": List[Literal["SINGLE_INSTANCE", "ACTIVE_STANDBY_MULTI_AZ"]],
        "SupportedEngineVersions": List[str],
    },
    total=False,
)

ClientDescribeBrokerInstanceOptionsResponseTypeDef = TypedDict(
    "ClientDescribeBrokerInstanceOptionsResponseTypeDef",
    {
        "BrokerInstanceOptions": List[
            ClientDescribeBrokerInstanceOptionsResponseBrokerInstanceOptionsTypeDef
        ],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ClientDescribeBrokerResponseBrokerInstancesTypeDef = TypedDict(
    "ClientDescribeBrokerResponseBrokerInstancesTypeDef",
    {"ConsoleURL": str, "Endpoints": List[str], "IpAddress": str},
    total=False,
)

ClientDescribeBrokerResponseConfigurationsCurrentTypeDef = TypedDict(
    "ClientDescribeBrokerResponseConfigurationsCurrentTypeDef",
    {"Id": str, "Revision": int},
    total=False,
)

ClientDescribeBrokerResponseConfigurationsHistoryTypeDef = TypedDict(
    "ClientDescribeBrokerResponseConfigurationsHistoryTypeDef",
    {"Id": str, "Revision": int},
    total=False,
)

ClientDescribeBrokerResponseConfigurationsPendingTypeDef = TypedDict(
    "ClientDescribeBrokerResponseConfigurationsPendingTypeDef",
    {"Id": str, "Revision": int},
    total=False,
)

ClientDescribeBrokerResponseConfigurationsTypeDef = TypedDict(
    "ClientDescribeBrokerResponseConfigurationsTypeDef",
    {
        "Current": ClientDescribeBrokerResponseConfigurationsCurrentTypeDef,
        "History": List[ClientDescribeBrokerResponseConfigurationsHistoryTypeDef],
        "Pending": ClientDescribeBrokerResponseConfigurationsPendingTypeDef,
    },
    total=False,
)

ClientDescribeBrokerResponseEncryptionOptionsTypeDef = TypedDict(
    "ClientDescribeBrokerResponseEncryptionOptionsTypeDef",
    {"KmsKeyId": str, "UseAwsOwnedKey": bool},
    total=False,
)

ClientDescribeBrokerResponseLogsPendingTypeDef = TypedDict(
    "ClientDescribeBrokerResponseLogsPendingTypeDef", {"Audit": bool, "General": bool}, total=False
)

ClientDescribeBrokerResponseLogsTypeDef = TypedDict(
    "ClientDescribeBrokerResponseLogsTypeDef",
    {
        "Audit": bool,
        "AuditLogGroup": str,
        "General": bool,
        "GeneralLogGroup": str,
        "Pending": ClientDescribeBrokerResponseLogsPendingTypeDef,
    },
    total=False,
)

ClientDescribeBrokerResponseMaintenanceWindowStartTimeTypeDef = TypedDict(
    "ClientDescribeBrokerResponseMaintenanceWindowStartTimeTypeDef",
    {
        "DayOfWeek": Literal[
            "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"
        ],
        "TimeOfDay": str,
        "TimeZone": str,
    },
    total=False,
)

ClientDescribeBrokerResponseUsersTypeDef = TypedDict(
    "ClientDescribeBrokerResponseUsersTypeDef",
    {"PendingChange": Literal["CREATE", "UPDATE", "DELETE"], "Username": str},
    total=False,
)

ClientDescribeBrokerResponseTypeDef = TypedDict(
    "ClientDescribeBrokerResponseTypeDef",
    {
        "AutoMinorVersionUpgrade": bool,
        "BrokerArn": str,
        "BrokerId": str,
        "BrokerInstances": List[ClientDescribeBrokerResponseBrokerInstancesTypeDef],
        "BrokerName": str,
        "BrokerState": Literal[
            "CREATION_IN_PROGRESS",
            "CREATION_FAILED",
            "DELETION_IN_PROGRESS",
            "RUNNING",
            "REBOOT_IN_PROGRESS",
        ],
        "Configurations": ClientDescribeBrokerResponseConfigurationsTypeDef,
        "Created": datetime,
        "DeploymentMode": Literal["SINGLE_INSTANCE", "ACTIVE_STANDBY_MULTI_AZ"],
        "EncryptionOptions": ClientDescribeBrokerResponseEncryptionOptionsTypeDef,
        "EngineType": str,
        "EngineVersion": str,
        "HostInstanceType": str,
        "Logs": ClientDescribeBrokerResponseLogsTypeDef,
        "MaintenanceWindowStartTime": ClientDescribeBrokerResponseMaintenanceWindowStartTimeTypeDef,
        "PendingEngineVersion": str,
        "PendingHostInstanceType": str,
        "PendingSecurityGroups": List[str],
        "PubliclyAccessible": bool,
        "SecurityGroups": List[str],
        "StorageType": Literal["EBS", "EFS"],
        "SubnetIds": List[str],
        "Tags": Dict[str, str],
        "Users": List[ClientDescribeBrokerResponseUsersTypeDef],
    },
    total=False,
)

ClientDescribeConfigurationResponseLatestRevisionTypeDef = TypedDict(
    "ClientDescribeConfigurationResponseLatestRevisionTypeDef",
    {"Created": datetime, "Description": str, "Revision": int},
    total=False,
)

ClientDescribeConfigurationResponseTypeDef = TypedDict(
    "ClientDescribeConfigurationResponseTypeDef",
    {
        "Arn": str,
        "Created": datetime,
        "Description": str,
        "EngineType": str,
        "EngineVersion": str,
        "Id": str,
        "LatestRevision": ClientDescribeConfigurationResponseLatestRevisionTypeDef,
        "Name": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

ClientDescribeConfigurationRevisionResponseTypeDef = TypedDict(
    "ClientDescribeConfigurationRevisionResponseTypeDef",
    {"ConfigurationId": str, "Created": datetime, "Data": str, "Description": str},
    total=False,
)

ClientDescribeUserResponsePendingTypeDef = TypedDict(
    "ClientDescribeUserResponsePendingTypeDef",
    {
        "ConsoleAccess": bool,
        "Groups": List[str],
        "PendingChange": Literal["CREATE", "UPDATE", "DELETE"],
    },
    total=False,
)

ClientDescribeUserResponseTypeDef = TypedDict(
    "ClientDescribeUserResponseTypeDef",
    {
        "BrokerId": str,
        "ConsoleAccess": bool,
        "Groups": List[str],
        "Pending": ClientDescribeUserResponsePendingTypeDef,
        "Username": str,
    },
    total=False,
)

ClientListBrokersResponseBrokerSummariesTypeDef = TypedDict(
    "ClientListBrokersResponseBrokerSummariesTypeDef",
    {
        "BrokerArn": str,
        "BrokerId": str,
        "BrokerName": str,
        "BrokerState": Literal[
            "CREATION_IN_PROGRESS",
            "CREATION_FAILED",
            "DELETION_IN_PROGRESS",
            "RUNNING",
            "REBOOT_IN_PROGRESS",
        ],
        "Created": datetime,
        "DeploymentMode": Literal["SINGLE_INSTANCE", "ACTIVE_STANDBY_MULTI_AZ"],
        "HostInstanceType": str,
    },
    total=False,
)

ClientListBrokersResponseTypeDef = TypedDict(
    "ClientListBrokersResponseTypeDef",
    {"BrokerSummaries": List[ClientListBrokersResponseBrokerSummariesTypeDef], "NextToken": str},
    total=False,
)

ClientListConfigurationRevisionsResponseRevisionsTypeDef = TypedDict(
    "ClientListConfigurationRevisionsResponseRevisionsTypeDef",
    {"Created": datetime, "Description": str, "Revision": int},
    total=False,
)

ClientListConfigurationRevisionsResponseTypeDef = TypedDict(
    "ClientListConfigurationRevisionsResponseTypeDef",
    {
        "ConfigurationId": str,
        "MaxResults": int,
        "NextToken": str,
        "Revisions": List[ClientListConfigurationRevisionsResponseRevisionsTypeDef],
    },
    total=False,
)

ClientListConfigurationsResponseConfigurationsLatestRevisionTypeDef = TypedDict(
    "ClientListConfigurationsResponseConfigurationsLatestRevisionTypeDef",
    {"Created": datetime, "Description": str, "Revision": int},
    total=False,
)

ClientListConfigurationsResponseConfigurationsTypeDef = TypedDict(
    "ClientListConfigurationsResponseConfigurationsTypeDef",
    {
        "Arn": str,
        "Created": datetime,
        "Description": str,
        "EngineType": str,
        "EngineVersion": str,
        "Id": str,
        "LatestRevision": ClientListConfigurationsResponseConfigurationsLatestRevisionTypeDef,
        "Name": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

ClientListConfigurationsResponseTypeDef = TypedDict(
    "ClientListConfigurationsResponseTypeDef",
    {
        "Configurations": List[ClientListConfigurationsResponseConfigurationsTypeDef],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ClientListTagsResponseTypeDef = TypedDict(
    "ClientListTagsResponseTypeDef", {"Tags": Dict[str, str]}, total=False
)

ClientListUsersResponseUsersTypeDef = TypedDict(
    "ClientListUsersResponseUsersTypeDef",
    {"PendingChange": Literal["CREATE", "UPDATE", "DELETE"], "Username": str},
    total=False,
)

ClientListUsersResponseTypeDef = TypedDict(
    "ClientListUsersResponseTypeDef",
    {
        "BrokerId": str,
        "MaxResults": int,
        "NextToken": str,
        "Users": List[ClientListUsersResponseUsersTypeDef],
    },
    total=False,
)

ClientUpdateBrokerConfigurationTypeDef = TypedDict(
    "ClientUpdateBrokerConfigurationTypeDef", {"Id": str, "Revision": int}, total=False
)

ClientUpdateBrokerLogsTypeDef = TypedDict(
    "ClientUpdateBrokerLogsTypeDef", {"Audit": bool, "General": bool}, total=False
)

ClientUpdateBrokerResponseConfigurationTypeDef = TypedDict(
    "ClientUpdateBrokerResponseConfigurationTypeDef", {"Id": str, "Revision": int}, total=False
)

ClientUpdateBrokerResponseLogsTypeDef = TypedDict(
    "ClientUpdateBrokerResponseLogsTypeDef", {"Audit": bool, "General": bool}, total=False
)

ClientUpdateBrokerResponseTypeDef = TypedDict(
    "ClientUpdateBrokerResponseTypeDef",
    {
        "AutoMinorVersionUpgrade": bool,
        "BrokerId": str,
        "Configuration": ClientUpdateBrokerResponseConfigurationTypeDef,
        "EngineVersion": str,
        "HostInstanceType": str,
        "Logs": ClientUpdateBrokerResponseLogsTypeDef,
        "SecurityGroups": List[str],
    },
    total=False,
)

ClientUpdateConfigurationResponseLatestRevisionTypeDef = TypedDict(
    "ClientUpdateConfigurationResponseLatestRevisionTypeDef",
    {"Created": datetime, "Description": str, "Revision": int},
    total=False,
)

ClientUpdateConfigurationResponseWarningsTypeDef = TypedDict(
    "ClientUpdateConfigurationResponseWarningsTypeDef",
    {
        "AttributeName": str,
        "ElementName": str,
        "Reason": Literal[
            "DISALLOWED_ELEMENT_REMOVED",
            "DISALLOWED_ATTRIBUTE_REMOVED",
            "INVALID_ATTRIBUTE_VALUE_REMOVED",
        ],
    },
    total=False,
)

ClientUpdateConfigurationResponseTypeDef = TypedDict(
    "ClientUpdateConfigurationResponseTypeDef",
    {
        "Arn": str,
        "Created": datetime,
        "Id": str,
        "LatestRevision": ClientUpdateConfigurationResponseLatestRevisionTypeDef,
        "Name": str,
        "Warnings": List[ClientUpdateConfigurationResponseWarningsTypeDef],
    },
    total=False,
)

BrokerSummaryTypeDef = TypedDict(
    "BrokerSummaryTypeDef",
    {
        "BrokerArn": str,
        "BrokerId": str,
        "BrokerName": str,
        "BrokerState": Literal[
            "CREATION_IN_PROGRESS",
            "CREATION_FAILED",
            "DELETION_IN_PROGRESS",
            "RUNNING",
            "REBOOT_IN_PROGRESS",
        ],
        "Created": datetime,
        "DeploymentMode": Literal["SINGLE_INSTANCE", "ACTIVE_STANDBY_MULTI_AZ"],
        "HostInstanceType": str,
    },
    total=False,
)

ListBrokersResponseTypeDef = TypedDict(
    "ListBrokersResponseTypeDef",
    {"BrokerSummaries": List[BrokerSummaryTypeDef], "NextToken": str},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)
