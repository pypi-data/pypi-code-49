"""
Main interface for dynamodb service client waiters.

Usage::

    import boto3
    from mypy_boto3.dynamodb import (
        TableExistsWaiter,
        TableNotExistsWaiter,
    )

    client: DynamoDBClient = boto3.client("dynamodb")

    table_exists_waiter: TableExistsWaiter = client.get_waiter("table_exists")
    table_not_exists_waiter: TableNotExistsWaiter = client.get_waiter("table_not_exists")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from typing import TYPE_CHECKING
from botocore.waiter import Waiter as Boto3Waiter
from mypy_boto3_dynamodb.type_defs import WaiterConfigTypeDef


__all__ = ("TableExistsWaiter", "TableNotExistsWaiter")


class TableExistsWaiter(Boto3Waiter):
    """
    [Waiter.TableExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dynamodb.html#DynamoDB.Waiter.TableExists)
    """

    def wait(self, TableName: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [TableExists.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dynamodb.html#DynamoDB.Waiter.TableExists.wait)
        """


class TableNotExistsWaiter(Boto3Waiter):
    """
    [Waiter.TableNotExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dynamodb.html#DynamoDB.Waiter.TableNotExists)
    """

    def wait(self, TableName: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [TableNotExists.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dynamodb.html#DynamoDB.Waiter.TableNotExists.wait)
        """
