"""
Main interface for dynamodb service client

Usage::

    import boto3
    from mypy_boto3.dynamodb import DynamoDBClient

    session = boto3.Session()

    client: DynamoDBClient = boto3.client("dynamodb")
    session_client: DynamoDBClient = session.client("dynamodb")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from datetime import datetime
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_dynamodb.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_dynamodb.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_dynamodb.type_defs import (
    ClientBatchGetItemRequestItemsTypeDef,
    ClientBatchGetItemResponseTypeDef,
    ClientBatchWriteItemRequestItemsTypeDef,
    ClientBatchWriteItemResponseTypeDef,
    ClientCreateBackupResponseTypeDef,
    ClientCreateGlobalTableReplicationGroupTypeDef,
    ClientCreateGlobalTableResponseTypeDef,
    ClientCreateTableAttributeDefinitionsTypeDef,
    ClientCreateTableGlobalSecondaryIndexesTypeDef,
    ClientCreateTableKeySchemaTypeDef,
    ClientCreateTableLocalSecondaryIndexesTypeDef,
    ClientCreateTableProvisionedThroughputTypeDef,
    ClientCreateTableResponseTypeDef,
    ClientCreateTableSSESpecificationTypeDef,
    ClientCreateTableStreamSpecificationTypeDef,
    ClientCreateTableTagsTypeDef,
    ClientDeleteBackupResponseTypeDef,
    ClientDeleteItemExpectedTypeDef,
    ClientDeleteItemExpressionAttributeValuesTypeDef,
    ClientDeleteItemKeyTypeDef,
    ClientDeleteItemResponseTypeDef,
    ClientDeleteTableResponseTypeDef,
    ClientDescribeBackupResponseTypeDef,
    ClientDescribeContinuousBackupsResponseTypeDef,
    ClientDescribeContributorInsightsResponseTypeDef,
    ClientDescribeEndpointsResponseTypeDef,
    ClientDescribeGlobalTableResponseTypeDef,
    ClientDescribeGlobalTableSettingsResponseTypeDef,
    ClientDescribeLimitsResponseTypeDef,
    ClientDescribeTableReplicaAutoScalingResponseTypeDef,
    ClientDescribeTableResponseTypeDef,
    ClientDescribeTimeToLiveResponseTypeDef,
    ClientGetItemKeyTypeDef,
    ClientGetItemResponseTypeDef,
    ClientListBackupsResponseTypeDef,
    ClientListContributorInsightsResponseTypeDef,
    ClientListGlobalTablesResponseTypeDef,
    ClientListTablesResponseTypeDef,
    ClientListTagsOfResourceResponseTypeDef,
    ClientPutItemExpectedTypeDef,
    ClientPutItemExpressionAttributeValuesTypeDef,
    ClientPutItemItemTypeDef,
    ClientPutItemResponseTypeDef,
    ClientQueryExclusiveStartKeyTypeDef,
    ClientQueryExpressionAttributeValuesTypeDef,
    ClientQueryKeyConditionsTypeDef,
    ClientQueryQueryFilterTypeDef,
    ClientQueryResponseTypeDef,
    ClientRestoreTableFromBackupGlobalSecondaryIndexOverrideTypeDef,
    ClientRestoreTableFromBackupLocalSecondaryIndexOverrideTypeDef,
    ClientRestoreTableFromBackupProvisionedThroughputOverrideTypeDef,
    ClientRestoreTableFromBackupResponseTypeDef,
    ClientRestoreTableToPointInTimeGlobalSecondaryIndexOverrideTypeDef,
    ClientRestoreTableToPointInTimeLocalSecondaryIndexOverrideTypeDef,
    ClientRestoreTableToPointInTimeProvisionedThroughputOverrideTypeDef,
    ClientRestoreTableToPointInTimeResponseTypeDef,
    ClientScanExclusiveStartKeyTypeDef,
    ClientScanExpressionAttributeValuesTypeDef,
    ClientScanResponseTypeDef,
    ClientScanScanFilterTypeDef,
    ClientTagResourceTagsTypeDef,
    ClientTransactGetItemsResponseTypeDef,
    ClientTransactGetItemsTransactItemsTypeDef,
    ClientTransactWriteItemsResponseTypeDef,
    ClientTransactWriteItemsTransactItemsTypeDef,
    ClientUpdateContinuousBackupsPointInTimeRecoverySpecificationTypeDef,
    ClientUpdateContinuousBackupsResponseTypeDef,
    ClientUpdateContributorInsightsResponseTypeDef,
    ClientUpdateGlobalTableReplicaUpdatesTypeDef,
    ClientUpdateGlobalTableResponseTypeDef,
    ClientUpdateGlobalTableSettingsGlobalTableGlobalSecondaryIndexSettingsUpdateTypeDef,
    ClientUpdateGlobalTableSettingsGlobalTableProvisionedWriteCapacityAutoScalingSettingsUpdateTypeDef,
    ClientUpdateGlobalTableSettingsReplicaSettingsUpdateTypeDef,
    ClientUpdateGlobalTableSettingsResponseTypeDef,
    ClientUpdateItemAttributeUpdatesTypeDef,
    ClientUpdateItemExpectedTypeDef,
    ClientUpdateItemExpressionAttributeValuesTypeDef,
    ClientUpdateItemKeyTypeDef,
    ClientUpdateItemResponseTypeDef,
    ClientUpdateTableAttributeDefinitionsTypeDef,
    ClientUpdateTableGlobalSecondaryIndexUpdatesTypeDef,
    ClientUpdateTableProvisionedThroughputTypeDef,
    ClientUpdateTableReplicaAutoScalingGlobalSecondaryIndexUpdatesTypeDef,
    ClientUpdateTableReplicaAutoScalingProvisionedWriteCapacityAutoScalingUpdateTypeDef,
    ClientUpdateTableReplicaAutoScalingReplicaUpdatesTypeDef,
    ClientUpdateTableReplicaAutoScalingResponseTypeDef,
    ClientUpdateTableReplicaUpdatesTypeDef,
    ClientUpdateTableResponseTypeDef,
    ClientUpdateTableSSESpecificationTypeDef,
    ClientUpdateTableStreamSpecificationTypeDef,
    ClientUpdateTimeToLiveResponseTypeDef,
    ClientUpdateTimeToLiveTimeToLiveSpecificationTypeDef,
)

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_dynamodb.waiter as waiter_scope
else:
    waiter_scope = object
if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("DynamoDBClient",)


class DynamoDBClient:
    """
    [DynamoDB.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dynamodb.html#DynamoDB.Client)
    """

    exceptions: "client_scope.Exceptions"

    def batch_get_item(
        self,
        RequestItems: Dict[str, ClientBatchGetItemRequestItemsTypeDef],
        ReturnConsumedCapacity: Literal["INDEXES", "TOTAL", "NONE"] = None,
    ) -> ClientBatchGetItemResponseTypeDef:
        """
        [Client.batch_get_item documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dynamodb.html#DynamoDB.Client.batch_get_item)
        """

    def batch_write_item(
        self,
        RequestItems: Dict[str, List[ClientBatchWriteItemRequestItemsTypeDef]],
        ReturnConsumedCapacity: Literal["INDEXES", "TOTAL", "NONE"] = None,
        ReturnItemCollectionMetrics: Literal["SIZE", "NONE"] = None,
    ) -> ClientBatchWriteItemResponseTypeDef:
        """
        [Client.batch_write_item documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dynamodb.html#DynamoDB.Client.batch_write_item)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dynamodb.html#DynamoDB.Client.can_paginate)
        """

    def create_backup(self, TableName: str, BackupName: str) -> ClientCreateBackupResponseTypeDef:
        """
        [Client.create_backup documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dynamodb.html#DynamoDB.Client.create_backup)
        """

    def create_global_table(
        self,
        GlobalTableName: str,
        ReplicationGroup: List[ClientCreateGlobalTableReplicationGroupTypeDef],
    ) -> ClientCreateGlobalTableResponseTypeDef:
        """
        [Client.create_global_table documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dynamodb.html#DynamoDB.Client.create_global_table)
        """

    def create_table(
        self,
        AttributeDefinitions: List[ClientCreateTableAttributeDefinitionsTypeDef],
        TableName: str,
        KeySchema: List[ClientCreateTableKeySchemaTypeDef],
        LocalSecondaryIndexes: List[ClientCreateTableLocalSecondaryIndexesTypeDef] = None,
        GlobalSecondaryIndexes: List[ClientCreateTableGlobalSecondaryIndexesTypeDef] = None,
        BillingMode: Literal["PROVISIONED", "PAY_PER_REQUEST"] = None,
        ProvisionedThroughput: ClientCreateTableProvisionedThroughputTypeDef = None,
        StreamSpecification: ClientCreateTableStreamSpecificationTypeDef = None,
        SSESpecification: ClientCreateTableSSESpecificationTypeDef = None,
        Tags: List[ClientCreateTableTagsTypeDef] = None,
    ) -> ClientCreateTableResponseTypeDef:
        """
        [Client.create_table documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dynamodb.html#DynamoDB.Client.create_table)
        """

    def delete_backup(self, BackupArn: str) -> ClientDeleteBackupResponseTypeDef:
        """
        [Client.delete_backup documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dynamodb.html#DynamoDB.Client.delete_backup)
        """

    def delete_item(
        self,
        TableName: str,
        Key: Dict[str, ClientDeleteItemKeyTypeDef],
        Expected: Dict[str, ClientDeleteItemExpectedTypeDef] = None,
        ConditionalOperator: Literal["AND", "OR"] = None,
        ReturnValues: Literal["NONE", "ALL_OLD", "UPDATED_OLD", "ALL_NEW", "UPDATED_NEW"] = None,
        ReturnConsumedCapacity: Literal["INDEXES", "TOTAL", "NONE"] = None,
        ReturnItemCollectionMetrics: Literal["SIZE", "NONE"] = None,
        ConditionExpression: str = None,
        ExpressionAttributeNames: Dict[str, str] = None,
        ExpressionAttributeValues: Dict[
            str, ClientDeleteItemExpressionAttributeValuesTypeDef
        ] = None,
    ) -> ClientDeleteItemResponseTypeDef:
        """
        [Client.delete_item documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dynamodb.html#DynamoDB.Client.delete_item)
        """

    def delete_table(self, TableName: str) -> ClientDeleteTableResponseTypeDef:
        """
        [Client.delete_table documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dynamodb.html#DynamoDB.Client.delete_table)
        """

    def describe_backup(self, BackupArn: str) -> ClientDescribeBackupResponseTypeDef:
        """
        [Client.describe_backup documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dynamodb.html#DynamoDB.Client.describe_backup)
        """

    def describe_continuous_backups(
        self, TableName: str
    ) -> ClientDescribeContinuousBackupsResponseTypeDef:
        """
        [Client.describe_continuous_backups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dynamodb.html#DynamoDB.Client.describe_continuous_backups)
        """

    def describe_contributor_insights(
        self, TableName: str, IndexName: str = None
    ) -> ClientDescribeContributorInsightsResponseTypeDef:
        """
        [Client.describe_contributor_insights documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dynamodb.html#DynamoDB.Client.describe_contributor_insights)
        """

    def describe_endpoints(
        self, *args: Any, **kwargs: Any
    ) -> ClientDescribeEndpointsResponseTypeDef:
        """
        [Client.describe_endpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dynamodb.html#DynamoDB.Client.describe_endpoints)
        """

    def describe_global_table(
        self, GlobalTableName: str
    ) -> ClientDescribeGlobalTableResponseTypeDef:
        """
        [Client.describe_global_table documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dynamodb.html#DynamoDB.Client.describe_global_table)
        """

    def describe_global_table_settings(
        self, GlobalTableName: str
    ) -> ClientDescribeGlobalTableSettingsResponseTypeDef:
        """
        [Client.describe_global_table_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dynamodb.html#DynamoDB.Client.describe_global_table_settings)
        """

    def describe_limits(self, *args: Any, **kwargs: Any) -> ClientDescribeLimitsResponseTypeDef:
        """
        [Client.describe_limits documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dynamodb.html#DynamoDB.Client.describe_limits)
        """

    def describe_table(self, TableName: str) -> ClientDescribeTableResponseTypeDef:
        """
        [Client.describe_table documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dynamodb.html#DynamoDB.Client.describe_table)
        """

    def describe_table_replica_auto_scaling(
        self, TableName: str
    ) -> ClientDescribeTableReplicaAutoScalingResponseTypeDef:
        """
        [Client.describe_table_replica_auto_scaling documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dynamodb.html#DynamoDB.Client.describe_table_replica_auto_scaling)
        """

    def describe_time_to_live(self, TableName: str) -> ClientDescribeTimeToLiveResponseTypeDef:
        """
        [Client.describe_time_to_live documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dynamodb.html#DynamoDB.Client.describe_time_to_live)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dynamodb.html#DynamoDB.Client.generate_presigned_url)
        """

    def get_item(
        self,
        TableName: str,
        Key: Dict[str, ClientGetItemKeyTypeDef],
        AttributesToGet: List[str] = None,
        ConsistentRead: bool = None,
        ReturnConsumedCapacity: Literal["INDEXES", "TOTAL", "NONE"] = None,
        ProjectionExpression: str = None,
        ExpressionAttributeNames: Dict[str, str] = None,
    ) -> ClientGetItemResponseTypeDef:
        """
        [Client.get_item documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dynamodb.html#DynamoDB.Client.get_item)
        """

    def list_backups(
        self,
        TableName: str = None,
        Limit: int = None,
        TimeRangeLowerBound: datetime = None,
        TimeRangeUpperBound: datetime = None,
        ExclusiveStartBackupArn: str = None,
        BackupType: Literal["USER", "SYSTEM", "AWS_BACKUP", "ALL"] = None,
    ) -> ClientListBackupsResponseTypeDef:
        """
        [Client.list_backups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dynamodb.html#DynamoDB.Client.list_backups)
        """

    def list_contributor_insights(
        self, TableName: str = None, NextToken: str = None, MaxResults: int = None
    ) -> ClientListContributorInsightsResponseTypeDef:
        """
        [Client.list_contributor_insights documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dynamodb.html#DynamoDB.Client.list_contributor_insights)
        """

    def list_global_tables(
        self, ExclusiveStartGlobalTableName: str = None, Limit: int = None, RegionName: str = None
    ) -> ClientListGlobalTablesResponseTypeDef:
        """
        [Client.list_global_tables documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dynamodb.html#DynamoDB.Client.list_global_tables)
        """

    def list_tables(
        self, ExclusiveStartTableName: str = None, Limit: int = None
    ) -> ClientListTablesResponseTypeDef:
        """
        [Client.list_tables documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dynamodb.html#DynamoDB.Client.list_tables)
        """

    def list_tags_of_resource(
        self, ResourceArn: str, NextToken: str = None
    ) -> ClientListTagsOfResourceResponseTypeDef:
        """
        [Client.list_tags_of_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dynamodb.html#DynamoDB.Client.list_tags_of_resource)
        """

    def put_item(
        self,
        TableName: str,
        Item: Dict[str, ClientPutItemItemTypeDef],
        Expected: Dict[str, ClientPutItemExpectedTypeDef] = None,
        ReturnValues: Literal["NONE", "ALL_OLD", "UPDATED_OLD", "ALL_NEW", "UPDATED_NEW"] = None,
        ReturnConsumedCapacity: Literal["INDEXES", "TOTAL", "NONE"] = None,
        ReturnItemCollectionMetrics: Literal["SIZE", "NONE"] = None,
        ConditionalOperator: Literal["AND", "OR"] = None,
        ConditionExpression: str = None,
        ExpressionAttributeNames: Dict[str, str] = None,
        ExpressionAttributeValues: Dict[str, ClientPutItemExpressionAttributeValuesTypeDef] = None,
    ) -> ClientPutItemResponseTypeDef:
        """
        [Client.put_item documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dynamodb.html#DynamoDB.Client.put_item)
        """

    def query(
        self,
        TableName: str,
        IndexName: str = None,
        Select: Literal[
            "ALL_ATTRIBUTES", "ALL_PROJECTED_ATTRIBUTES", "SPECIFIC_ATTRIBUTES", "COUNT"
        ] = None,
        AttributesToGet: List[str] = None,
        Limit: int = None,
        ConsistentRead: bool = None,
        KeyConditions: Dict[str, ClientQueryKeyConditionsTypeDef] = None,
        QueryFilter: Dict[str, ClientQueryQueryFilterTypeDef] = None,
        ConditionalOperator: Literal["AND", "OR"] = None,
        ScanIndexForward: bool = None,
        ExclusiveStartKey: Dict[str, ClientQueryExclusiveStartKeyTypeDef] = None,
        ReturnConsumedCapacity: Literal["INDEXES", "TOTAL", "NONE"] = None,
        ProjectionExpression: str = None,
        FilterExpression: str = None,
        KeyConditionExpression: str = None,
        ExpressionAttributeNames: Dict[str, str] = None,
        ExpressionAttributeValues: Dict[str, ClientQueryExpressionAttributeValuesTypeDef] = None,
    ) -> ClientQueryResponseTypeDef:
        """
        [Client.query documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dynamodb.html#DynamoDB.Client.query)
        """

    def restore_table_from_backup(
        self,
        TargetTableName: str,
        BackupArn: str,
        BillingModeOverride: Literal["PROVISIONED", "PAY_PER_REQUEST"] = None,
        GlobalSecondaryIndexOverride: List[
            ClientRestoreTableFromBackupGlobalSecondaryIndexOverrideTypeDef
        ] = None,
        LocalSecondaryIndexOverride: List[
            ClientRestoreTableFromBackupLocalSecondaryIndexOverrideTypeDef
        ] = None,
        ProvisionedThroughputOverride: ClientRestoreTableFromBackupProvisionedThroughputOverrideTypeDef = None,
    ) -> ClientRestoreTableFromBackupResponseTypeDef:
        """
        [Client.restore_table_from_backup documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dynamodb.html#DynamoDB.Client.restore_table_from_backup)
        """

    def restore_table_to_point_in_time(
        self,
        SourceTableName: str,
        TargetTableName: str,
        UseLatestRestorableTime: bool = None,
        RestoreDateTime: datetime = None,
        BillingModeOverride: Literal["PROVISIONED", "PAY_PER_REQUEST"] = None,
        GlobalSecondaryIndexOverride: List[
            ClientRestoreTableToPointInTimeGlobalSecondaryIndexOverrideTypeDef
        ] = None,
        LocalSecondaryIndexOverride: List[
            ClientRestoreTableToPointInTimeLocalSecondaryIndexOverrideTypeDef
        ] = None,
        ProvisionedThroughputOverride: ClientRestoreTableToPointInTimeProvisionedThroughputOverrideTypeDef = None,
    ) -> ClientRestoreTableToPointInTimeResponseTypeDef:
        """
        [Client.restore_table_to_point_in_time documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dynamodb.html#DynamoDB.Client.restore_table_to_point_in_time)
        """

    def scan(
        self,
        TableName: str,
        IndexName: str = None,
        AttributesToGet: List[str] = None,
        Limit: int = None,
        Select: Literal[
            "ALL_ATTRIBUTES", "ALL_PROJECTED_ATTRIBUTES", "SPECIFIC_ATTRIBUTES", "COUNT"
        ] = None,
        ScanFilter: Dict[str, ClientScanScanFilterTypeDef] = None,
        ConditionalOperator: Literal["AND", "OR"] = None,
        ExclusiveStartKey: Dict[str, ClientScanExclusiveStartKeyTypeDef] = None,
        ReturnConsumedCapacity: Literal["INDEXES", "TOTAL", "NONE"] = None,
        TotalSegments: int = None,
        Segment: int = None,
        ProjectionExpression: str = None,
        FilterExpression: str = None,
        ExpressionAttributeNames: Dict[str, str] = None,
        ExpressionAttributeValues: Dict[str, ClientScanExpressionAttributeValuesTypeDef] = None,
        ConsistentRead: bool = None,
    ) -> ClientScanResponseTypeDef:
        """
        [Client.scan documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dynamodb.html#DynamoDB.Client.scan)
        """

    def tag_resource(self, ResourceArn: str, Tags: List[ClientTagResourceTagsTypeDef]) -> None:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dynamodb.html#DynamoDB.Client.tag_resource)
        """

    def transact_get_items(
        self,
        TransactItems: List[ClientTransactGetItemsTransactItemsTypeDef],
        ReturnConsumedCapacity: Literal["INDEXES", "TOTAL", "NONE"] = None,
    ) -> ClientTransactGetItemsResponseTypeDef:
        """
        [Client.transact_get_items documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dynamodb.html#DynamoDB.Client.transact_get_items)
        """

    def transact_write_items(
        self,
        TransactItems: List[ClientTransactWriteItemsTransactItemsTypeDef],
        ReturnConsumedCapacity: Literal["INDEXES", "TOTAL", "NONE"] = None,
        ReturnItemCollectionMetrics: Literal["SIZE", "NONE"] = None,
        ClientRequestToken: str = None,
    ) -> ClientTransactWriteItemsResponseTypeDef:
        """
        [Client.transact_write_items documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dynamodb.html#DynamoDB.Client.transact_write_items)
        """

    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> None:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dynamodb.html#DynamoDB.Client.untag_resource)
        """

    def update_continuous_backups(
        self,
        TableName: str,
        PointInTimeRecoverySpecification: ClientUpdateContinuousBackupsPointInTimeRecoverySpecificationTypeDef,
    ) -> ClientUpdateContinuousBackupsResponseTypeDef:
        """
        [Client.update_continuous_backups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dynamodb.html#DynamoDB.Client.update_continuous_backups)
        """

    def update_contributor_insights(
        self,
        TableName: str,
        ContributorInsightsAction: Literal["ENABLE", "DISABLE"],
        IndexName: str = None,
    ) -> ClientUpdateContributorInsightsResponseTypeDef:
        """
        [Client.update_contributor_insights documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dynamodb.html#DynamoDB.Client.update_contributor_insights)
        """

    def update_global_table(
        self,
        GlobalTableName: str,
        ReplicaUpdates: List[ClientUpdateGlobalTableReplicaUpdatesTypeDef],
    ) -> ClientUpdateGlobalTableResponseTypeDef:
        """
        [Client.update_global_table documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dynamodb.html#DynamoDB.Client.update_global_table)
        """

    def update_global_table_settings(
        self,
        GlobalTableName: str,
        GlobalTableBillingMode: Literal["PROVISIONED", "PAY_PER_REQUEST"] = None,
        GlobalTableProvisionedWriteCapacityUnits: int = None,
        GlobalTableProvisionedWriteCapacityAutoScalingSettingsUpdate: ClientUpdateGlobalTableSettingsGlobalTableProvisionedWriteCapacityAutoScalingSettingsUpdateTypeDef = None,
        GlobalTableGlobalSecondaryIndexSettingsUpdate: List[
            ClientUpdateGlobalTableSettingsGlobalTableGlobalSecondaryIndexSettingsUpdateTypeDef
        ] = None,
        ReplicaSettingsUpdate: List[
            ClientUpdateGlobalTableSettingsReplicaSettingsUpdateTypeDef
        ] = None,
    ) -> ClientUpdateGlobalTableSettingsResponseTypeDef:
        """
        [Client.update_global_table_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dynamodb.html#DynamoDB.Client.update_global_table_settings)
        """

    def update_item(
        self,
        TableName: str,
        Key: Dict[str, ClientUpdateItemKeyTypeDef],
        AttributeUpdates: Dict[str, ClientUpdateItemAttributeUpdatesTypeDef] = None,
        Expected: Dict[str, ClientUpdateItemExpectedTypeDef] = None,
        ConditionalOperator: Literal["AND", "OR"] = None,
        ReturnValues: Literal["NONE", "ALL_OLD", "UPDATED_OLD", "ALL_NEW", "UPDATED_NEW"] = None,
        ReturnConsumedCapacity: Literal["INDEXES", "TOTAL", "NONE"] = None,
        ReturnItemCollectionMetrics: Literal["SIZE", "NONE"] = None,
        UpdateExpression: str = None,
        ConditionExpression: str = None,
        ExpressionAttributeNames: Dict[str, str] = None,
        ExpressionAttributeValues: Dict[
            str, ClientUpdateItemExpressionAttributeValuesTypeDef
        ] = None,
    ) -> ClientUpdateItemResponseTypeDef:
        """
        [Client.update_item documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dynamodb.html#DynamoDB.Client.update_item)
        """

    def update_table(
        self,
        TableName: str,
        AttributeDefinitions: List[ClientUpdateTableAttributeDefinitionsTypeDef] = None,
        BillingMode: Literal["PROVISIONED", "PAY_PER_REQUEST"] = None,
        ProvisionedThroughput: ClientUpdateTableProvisionedThroughputTypeDef = None,
        GlobalSecondaryIndexUpdates: List[
            ClientUpdateTableGlobalSecondaryIndexUpdatesTypeDef
        ] = None,
        StreamSpecification: ClientUpdateTableStreamSpecificationTypeDef = None,
        SSESpecification: ClientUpdateTableSSESpecificationTypeDef = None,
        ReplicaUpdates: List[ClientUpdateTableReplicaUpdatesTypeDef] = None,
    ) -> ClientUpdateTableResponseTypeDef:
        """
        [Client.update_table documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dynamodb.html#DynamoDB.Client.update_table)
        """

    def update_table_replica_auto_scaling(
        self,
        TableName: str,
        GlobalSecondaryIndexUpdates: List[
            ClientUpdateTableReplicaAutoScalingGlobalSecondaryIndexUpdatesTypeDef
        ] = None,
        ProvisionedWriteCapacityAutoScalingUpdate: ClientUpdateTableReplicaAutoScalingProvisionedWriteCapacityAutoScalingUpdateTypeDef = None,
        ReplicaUpdates: List[ClientUpdateTableReplicaAutoScalingReplicaUpdatesTypeDef] = None,
    ) -> ClientUpdateTableReplicaAutoScalingResponseTypeDef:
        """
        [Client.update_table_replica_auto_scaling documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dynamodb.html#DynamoDB.Client.update_table_replica_auto_scaling)
        """

    def update_time_to_live(
        self,
        TableName: str,
        TimeToLiveSpecification: ClientUpdateTimeToLiveTimeToLiveSpecificationTypeDef,
    ) -> ClientUpdateTimeToLiveResponseTypeDef:
        """
        [Client.update_time_to_live documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dynamodb.html#DynamoDB.Client.update_time_to_live)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_backups"]
    ) -> "paginator_scope.ListBackupsPaginator":
        """
        [Paginator.ListBackups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dynamodb.html#DynamoDB.Paginator.ListBackups)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_tables"]
    ) -> "paginator_scope.ListTablesPaginator":
        """
        [Paginator.ListTables documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dynamodb.html#DynamoDB.Paginator.ListTables)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_tags_of_resource"]
    ) -> "paginator_scope.ListTagsOfResourcePaginator":
        """
        [Paginator.ListTagsOfResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dynamodb.html#DynamoDB.Paginator.ListTagsOfResource)
        """

    @overload
    def get_paginator(self, operation_name: Literal["query"]) -> "paginator_scope.QueryPaginator":
        """
        [Paginator.Query documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dynamodb.html#DynamoDB.Paginator.Query)
        """

    @overload
    def get_paginator(self, operation_name: Literal["scan"]) -> "paginator_scope.ScanPaginator":
        """
        [Paginator.Scan documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dynamodb.html#DynamoDB.Paginator.Scan)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["table_exists"]) -> "waiter_scope.TableExistsWaiter":
        """
        [Waiter.TableExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dynamodb.html#DynamoDB.Waiter.TableExists)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["table_not_exists"]
    ) -> "waiter_scope.TableNotExistsWaiter":
        """
        [Waiter.TableNotExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dynamodb.html#DynamoDB.Waiter.TableNotExists)
        """


class Exceptions:
    BackupInUseException: Boto3ClientError
    BackupNotFoundException: Boto3ClientError
    ClientError: Boto3ClientError
    ConditionalCheckFailedException: Boto3ClientError
    ContinuousBackupsUnavailableException: Boto3ClientError
    GlobalTableAlreadyExistsException: Boto3ClientError
    GlobalTableNotFoundException: Boto3ClientError
    IdempotentParameterMismatchException: Boto3ClientError
    IndexNotFoundException: Boto3ClientError
    InternalServerError: Boto3ClientError
    InvalidRestoreTimeException: Boto3ClientError
    ItemCollectionSizeLimitExceededException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    PointInTimeRecoveryUnavailableException: Boto3ClientError
    ProvisionedThroughputExceededException: Boto3ClientError
    ReplicaAlreadyExistsException: Boto3ClientError
    ReplicaNotFoundException: Boto3ClientError
    RequestLimitExceeded: Boto3ClientError
    ResourceInUseException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    TableAlreadyExistsException: Boto3ClientError
    TableInUseException: Boto3ClientError
    TableNotFoundException: Boto3ClientError
    TransactionCanceledException: Boto3ClientError
    TransactionConflictException: Boto3ClientError
    TransactionInProgressException: Boto3ClientError
