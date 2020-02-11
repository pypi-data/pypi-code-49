"""
Main interface for dynamodb service client paginators.

Usage::

    import boto3
    from mypy_boto3.dynamodb import (
        ListBackupsPaginator,
        ListTablesPaginator,
        ListTagsOfResourcePaginator,
        QueryPaginator,
        ScanPaginator,
    )

    client: DynamoDBClient = boto3.client("dynamodb")

    list_backups_paginator: ListBackupsPaginator = client.get_paginator("list_backups")
    list_tables_paginator: ListTablesPaginator = client.get_paginator("list_tables")
    list_tags_of_resource_paginator: ListTagsOfResourcePaginator = client.get_paginator("list_tags_of_resource")
    query_paginator: QueryPaginator = client.get_paginator("query")
    scan_paginator: ScanPaginator = client.get_paginator("scan")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from datetime import datetime
import sys
from typing import Dict, Generator, List, TYPE_CHECKING
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_dynamodb.type_defs import (
    AttributeValueTypeDef,
    ConditionTypeDef,
    ListBackupsOutputTypeDef,
    ListTablesOutputTypeDef,
    ListTagsOfResourceOutputTypeDef,
    PaginatorConfigTypeDef,
    QueryOutputTypeDef,
    ScanOutputTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ListBackupsPaginator",
    "ListTablesPaginator",
    "ListTagsOfResourcePaginator",
    "QueryPaginator",
    "ScanPaginator",
)


class ListBackupsPaginator(Boto3Paginator):
    """
    [Paginator.ListBackups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dynamodb.html#DynamoDB.Paginator.ListBackups)
    """

    def paginate(
        self,
        TableName: str = None,
        TimeRangeLowerBound: datetime = None,
        TimeRangeUpperBound: datetime = None,
        BackupType: Literal["USER", "SYSTEM", "AWS_BACKUP", "ALL"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListBackupsOutputTypeDef, None, None]:
        """
        [ListBackups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dynamodb.html#DynamoDB.Paginator.ListBackups.paginate)
        """


class ListTablesPaginator(Boto3Paginator):
    """
    [Paginator.ListTables documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dynamodb.html#DynamoDB.Paginator.ListTables)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListTablesOutputTypeDef, None, None]:
        """
        [ListTables.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dynamodb.html#DynamoDB.Paginator.ListTables.paginate)
        """


class ListTagsOfResourcePaginator(Boto3Paginator):
    """
    [Paginator.ListTagsOfResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dynamodb.html#DynamoDB.Paginator.ListTagsOfResource)
    """

    def paginate(
        self, ResourceArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListTagsOfResourceOutputTypeDef, None, None]:
        """
        [ListTagsOfResource.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dynamodb.html#DynamoDB.Paginator.ListTagsOfResource.paginate)
        """


class QueryPaginator(Boto3Paginator):
    """
    [Paginator.Query documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dynamodb.html#DynamoDB.Paginator.Query)
    """

    def paginate(
        self,
        TableName: str,
        IndexName: str = None,
        Select: Literal[
            "ALL_ATTRIBUTES", "ALL_PROJECTED_ATTRIBUTES", "SPECIFIC_ATTRIBUTES", "COUNT"
        ] = None,
        AttributesToGet: List[str] = None,
        ConsistentRead: bool = None,
        KeyConditions: Dict[str, ConditionTypeDef] = None,
        QueryFilter: Dict[str, ConditionTypeDef] = None,
        ConditionalOperator: Literal["AND", "OR"] = None,
        ScanIndexForward: bool = None,
        ReturnConsumedCapacity: Literal["INDEXES", "TOTAL", "NONE"] = None,
        ProjectionExpression: str = None,
        FilterExpression: str = None,
        KeyConditionExpression: str = None,
        ExpressionAttributeNames: Dict[str, str] = None,
        ExpressionAttributeValues: Dict[str, AttributeValueTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[QueryOutputTypeDef, None, None]:
        """
        [Query.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dynamodb.html#DynamoDB.Paginator.Query.paginate)
        """


class ScanPaginator(Boto3Paginator):
    """
    [Paginator.Scan documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dynamodb.html#DynamoDB.Paginator.Scan)
    """

    def paginate(
        self,
        TableName: str,
        IndexName: str = None,
        AttributesToGet: List[str] = None,
        Select: Literal[
            "ALL_ATTRIBUTES", "ALL_PROJECTED_ATTRIBUTES", "SPECIFIC_ATTRIBUTES", "COUNT"
        ] = None,
        ScanFilter: Dict[str, ConditionTypeDef] = None,
        ConditionalOperator: Literal["AND", "OR"] = None,
        ReturnConsumedCapacity: Literal["INDEXES", "TOTAL", "NONE"] = None,
        TotalSegments: int = None,
        Segment: int = None,
        ProjectionExpression: str = None,
        FilterExpression: str = None,
        ExpressionAttributeNames: Dict[str, str] = None,
        ExpressionAttributeValues: Dict[str, AttributeValueTypeDef] = None,
        ConsistentRead: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ScanOutputTypeDef, None, None]:
        """
        [Scan.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dynamodb.html#DynamoDB.Paginator.Scan.paginate)
        """
