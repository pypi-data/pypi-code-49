"""
Main interface for cognito-sync service type definitions.

Usage::

    from mypy_boto3.cognito_sync.type_defs import ClientBulkPublishResponseTypeDef

    data: ClientBulkPublishResponseTypeDef = {...}
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
    "ClientBulkPublishResponseTypeDef",
    "ClientDeleteDatasetResponseDatasetTypeDef",
    "ClientDeleteDatasetResponseTypeDef",
    "ClientDescribeDatasetResponseDatasetTypeDef",
    "ClientDescribeDatasetResponseTypeDef",
    "ClientDescribeIdentityPoolUsageResponseIdentityPoolUsageTypeDef",
    "ClientDescribeIdentityPoolUsageResponseTypeDef",
    "ClientDescribeIdentityUsageResponseIdentityUsageTypeDef",
    "ClientDescribeIdentityUsageResponseTypeDef",
    "ClientGetBulkPublishDetailsResponseTypeDef",
    "ClientGetCognitoEventsResponseTypeDef",
    "ClientGetIdentityPoolConfigurationResponseCognitoStreamsTypeDef",
    "ClientGetIdentityPoolConfigurationResponsePushSyncTypeDef",
    "ClientGetIdentityPoolConfigurationResponseTypeDef",
    "ClientListDatasetsResponseDatasetsTypeDef",
    "ClientListDatasetsResponseTypeDef",
    "ClientListIdentityPoolUsageResponseIdentityPoolUsagesTypeDef",
    "ClientListIdentityPoolUsageResponseTypeDef",
    "ClientListRecordsResponseRecordsTypeDef",
    "ClientListRecordsResponseTypeDef",
    "ClientRegisterDeviceResponseTypeDef",
    "ClientSetIdentityPoolConfigurationCognitoStreamsTypeDef",
    "ClientSetIdentityPoolConfigurationPushSyncTypeDef",
    "ClientSetIdentityPoolConfigurationResponseCognitoStreamsTypeDef",
    "ClientSetIdentityPoolConfigurationResponsePushSyncTypeDef",
    "ClientSetIdentityPoolConfigurationResponseTypeDef",
    "ClientUpdateRecordsRecordPatchesTypeDef",
    "ClientUpdateRecordsResponseRecordsTypeDef",
    "ClientUpdateRecordsResponseTypeDef",
)

ClientBulkPublishResponseTypeDef = TypedDict(
    "ClientBulkPublishResponseTypeDef", {"IdentityPoolId": str}, total=False
)

ClientDeleteDatasetResponseDatasetTypeDef = TypedDict(
    "ClientDeleteDatasetResponseDatasetTypeDef",
    {
        "IdentityId": str,
        "DatasetName": str,
        "CreationDate": datetime,
        "LastModifiedDate": datetime,
        "LastModifiedBy": str,
        "DataStorage": int,
        "NumRecords": int,
    },
    total=False,
)

ClientDeleteDatasetResponseTypeDef = TypedDict(
    "ClientDeleteDatasetResponseTypeDef",
    {"Dataset": ClientDeleteDatasetResponseDatasetTypeDef},
    total=False,
)

ClientDescribeDatasetResponseDatasetTypeDef = TypedDict(
    "ClientDescribeDatasetResponseDatasetTypeDef",
    {
        "IdentityId": str,
        "DatasetName": str,
        "CreationDate": datetime,
        "LastModifiedDate": datetime,
        "LastModifiedBy": str,
        "DataStorage": int,
        "NumRecords": int,
    },
    total=False,
)

ClientDescribeDatasetResponseTypeDef = TypedDict(
    "ClientDescribeDatasetResponseTypeDef",
    {"Dataset": ClientDescribeDatasetResponseDatasetTypeDef},
    total=False,
)

ClientDescribeIdentityPoolUsageResponseIdentityPoolUsageTypeDef = TypedDict(
    "ClientDescribeIdentityPoolUsageResponseIdentityPoolUsageTypeDef",
    {
        "IdentityPoolId": str,
        "SyncSessionsCount": int,
        "DataStorage": int,
        "LastModifiedDate": datetime,
    },
    total=False,
)

ClientDescribeIdentityPoolUsageResponseTypeDef = TypedDict(
    "ClientDescribeIdentityPoolUsageResponseTypeDef",
    {"IdentityPoolUsage": ClientDescribeIdentityPoolUsageResponseIdentityPoolUsageTypeDef},
    total=False,
)

ClientDescribeIdentityUsageResponseIdentityUsageTypeDef = TypedDict(
    "ClientDescribeIdentityUsageResponseIdentityUsageTypeDef",
    {
        "IdentityId": str,
        "IdentityPoolId": str,
        "LastModifiedDate": datetime,
        "DatasetCount": int,
        "DataStorage": int,
    },
    total=False,
)

ClientDescribeIdentityUsageResponseTypeDef = TypedDict(
    "ClientDescribeIdentityUsageResponseTypeDef",
    {"IdentityUsage": ClientDescribeIdentityUsageResponseIdentityUsageTypeDef},
    total=False,
)

ClientGetBulkPublishDetailsResponseTypeDef = TypedDict(
    "ClientGetBulkPublishDetailsResponseTypeDef",
    {
        "IdentityPoolId": str,
        "BulkPublishStartTime": datetime,
        "BulkPublishCompleteTime": datetime,
        "BulkPublishStatus": Literal["NOT_STARTED", "IN_PROGRESS", "FAILED", "SUCCEEDED"],
        "FailureMessage": str,
    },
    total=False,
)

ClientGetCognitoEventsResponseTypeDef = TypedDict(
    "ClientGetCognitoEventsResponseTypeDef", {"Events": Dict[str, str]}, total=False
)

ClientGetIdentityPoolConfigurationResponseCognitoStreamsTypeDef = TypedDict(
    "ClientGetIdentityPoolConfigurationResponseCognitoStreamsTypeDef",
    {"StreamName": str, "RoleArn": str, "StreamingStatus": Literal["ENABLED", "DISABLED"]},
    total=False,
)

ClientGetIdentityPoolConfigurationResponsePushSyncTypeDef = TypedDict(
    "ClientGetIdentityPoolConfigurationResponsePushSyncTypeDef",
    {"ApplicationArns": List[str], "RoleArn": str},
    total=False,
)

ClientGetIdentityPoolConfigurationResponseTypeDef = TypedDict(
    "ClientGetIdentityPoolConfigurationResponseTypeDef",
    {
        "IdentityPoolId": str,
        "PushSync": ClientGetIdentityPoolConfigurationResponsePushSyncTypeDef,
        "CognitoStreams": ClientGetIdentityPoolConfigurationResponseCognitoStreamsTypeDef,
    },
    total=False,
)

ClientListDatasetsResponseDatasetsTypeDef = TypedDict(
    "ClientListDatasetsResponseDatasetsTypeDef",
    {
        "IdentityId": str,
        "DatasetName": str,
        "CreationDate": datetime,
        "LastModifiedDate": datetime,
        "LastModifiedBy": str,
        "DataStorage": int,
        "NumRecords": int,
    },
    total=False,
)

ClientListDatasetsResponseTypeDef = TypedDict(
    "ClientListDatasetsResponseTypeDef",
    {"Datasets": List[ClientListDatasetsResponseDatasetsTypeDef], "Count": int, "NextToken": str},
    total=False,
)

ClientListIdentityPoolUsageResponseIdentityPoolUsagesTypeDef = TypedDict(
    "ClientListIdentityPoolUsageResponseIdentityPoolUsagesTypeDef",
    {
        "IdentityPoolId": str,
        "SyncSessionsCount": int,
        "DataStorage": int,
        "LastModifiedDate": datetime,
    },
    total=False,
)

ClientListIdentityPoolUsageResponseTypeDef = TypedDict(
    "ClientListIdentityPoolUsageResponseTypeDef",
    {
        "IdentityPoolUsages": List[ClientListIdentityPoolUsageResponseIdentityPoolUsagesTypeDef],
        "MaxResults": int,
        "Count": int,
        "NextToken": str,
    },
    total=False,
)

ClientListRecordsResponseRecordsTypeDef = TypedDict(
    "ClientListRecordsResponseRecordsTypeDef",
    {
        "Key": str,
        "Value": str,
        "SyncCount": int,
        "LastModifiedDate": datetime,
        "LastModifiedBy": str,
        "DeviceLastModifiedDate": datetime,
    },
    total=False,
)

ClientListRecordsResponseTypeDef = TypedDict(
    "ClientListRecordsResponseTypeDef",
    {
        "Records": List[ClientListRecordsResponseRecordsTypeDef],
        "NextToken": str,
        "Count": int,
        "DatasetSyncCount": int,
        "LastModifiedBy": str,
        "MergedDatasetNames": List[str],
        "DatasetExists": bool,
        "DatasetDeletedAfterRequestedSyncCount": bool,
        "SyncSessionToken": str,
    },
    total=False,
)

ClientRegisterDeviceResponseTypeDef = TypedDict(
    "ClientRegisterDeviceResponseTypeDef", {"DeviceId": str}, total=False
)

ClientSetIdentityPoolConfigurationCognitoStreamsTypeDef = TypedDict(
    "ClientSetIdentityPoolConfigurationCognitoStreamsTypeDef",
    {"StreamName": str, "RoleArn": str, "StreamingStatus": Literal["ENABLED", "DISABLED"]},
    total=False,
)

ClientSetIdentityPoolConfigurationPushSyncTypeDef = TypedDict(
    "ClientSetIdentityPoolConfigurationPushSyncTypeDef",
    {"ApplicationArns": List[str], "RoleArn": str},
    total=False,
)

ClientSetIdentityPoolConfigurationResponseCognitoStreamsTypeDef = TypedDict(
    "ClientSetIdentityPoolConfigurationResponseCognitoStreamsTypeDef",
    {"StreamName": str, "RoleArn": str, "StreamingStatus": Literal["ENABLED", "DISABLED"]},
    total=False,
)

ClientSetIdentityPoolConfigurationResponsePushSyncTypeDef = TypedDict(
    "ClientSetIdentityPoolConfigurationResponsePushSyncTypeDef",
    {"ApplicationArns": List[str], "RoleArn": str},
    total=False,
)

ClientSetIdentityPoolConfigurationResponseTypeDef = TypedDict(
    "ClientSetIdentityPoolConfigurationResponseTypeDef",
    {
        "IdentityPoolId": str,
        "PushSync": ClientSetIdentityPoolConfigurationResponsePushSyncTypeDef,
        "CognitoStreams": ClientSetIdentityPoolConfigurationResponseCognitoStreamsTypeDef,
    },
    total=False,
)

_RequiredClientUpdateRecordsRecordPatchesTypeDef = TypedDict(
    "_RequiredClientUpdateRecordsRecordPatchesTypeDef",
    {"Op": Literal["replace", "remove"], "Key": str, "SyncCount": int},
)
_OptionalClientUpdateRecordsRecordPatchesTypeDef = TypedDict(
    "_OptionalClientUpdateRecordsRecordPatchesTypeDef",
    {"Value": str, "DeviceLastModifiedDate": datetime},
    total=False,
)


class ClientUpdateRecordsRecordPatchesTypeDef(
    _RequiredClientUpdateRecordsRecordPatchesTypeDef,
    _OptionalClientUpdateRecordsRecordPatchesTypeDef,
):
    pass


ClientUpdateRecordsResponseRecordsTypeDef = TypedDict(
    "ClientUpdateRecordsResponseRecordsTypeDef",
    {
        "Key": str,
        "Value": str,
        "SyncCount": int,
        "LastModifiedDate": datetime,
        "LastModifiedBy": str,
        "DeviceLastModifiedDate": datetime,
    },
    total=False,
)

ClientUpdateRecordsResponseTypeDef = TypedDict(
    "ClientUpdateRecordsResponseTypeDef",
    {"Records": List[ClientUpdateRecordsResponseRecordsTypeDef]},
    total=False,
)
