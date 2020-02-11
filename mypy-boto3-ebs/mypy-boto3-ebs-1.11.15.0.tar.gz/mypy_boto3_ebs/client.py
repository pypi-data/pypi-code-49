"""
Main interface for ebs service client

Usage::

    import boto3
    from mypy_boto3.ebs import EBSClient

    session = boto3.Session()

    client: EBSClient = boto3.client("ebs")
    session_client: EBSClient = session.client("ebs")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from typing import Any, Dict, TYPE_CHECKING
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_ebs.client as client_scope
else:
    client_scope = object
from mypy_boto3_ebs.type_defs import (
    ClientGetSnapshotBlockResponseTypeDef,
    ClientListChangedBlocksResponseTypeDef,
    ClientListSnapshotBlocksResponseTypeDef,
)


__all__ = ("EBSClient",)


class EBSClient:
    """
    [EBS.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ebs.html#EBS.Client)
    """

    exceptions: "client_scope.Exceptions"

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ebs.html#EBS.Client.can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ebs.html#EBS.Client.generate_presigned_url)
        """

    def get_snapshot_block(
        self, SnapshotId: str, BlockIndex: int, BlockToken: str
    ) -> ClientGetSnapshotBlockResponseTypeDef:
        """
        [Client.get_snapshot_block documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ebs.html#EBS.Client.get_snapshot_block)
        """

    def list_changed_blocks(
        self,
        SecondSnapshotId: str,
        FirstSnapshotId: str = None,
        NextToken: str = None,
        MaxResults: int = None,
        StartingBlockIndex: int = None,
    ) -> ClientListChangedBlocksResponseTypeDef:
        """
        [Client.list_changed_blocks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ebs.html#EBS.Client.list_changed_blocks)
        """

    def list_snapshot_blocks(
        self,
        SnapshotId: str,
        NextToken: str = None,
        MaxResults: int = None,
        StartingBlockIndex: int = None,
    ) -> ClientListSnapshotBlocksResponseTypeDef:
        """
        [Client.list_snapshot_blocks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ebs.html#EBS.Client.list_snapshot_blocks)
        """


class Exceptions:
    ClientError: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    ValidationException: Boto3ClientError
