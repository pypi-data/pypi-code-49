"""
Main interface for qldb service client

Usage::

    import boto3
    from mypy_boto3.qldb import QLDBClient

    session = boto3.Session()

    client: QLDBClient = boto3.client("qldb")
    session_client: QLDBClient = session.client("qldb")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from datetime import datetime
from typing import Any, Dict, List, TYPE_CHECKING
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_qldb.client as client_scope
else:
    client_scope = object
from mypy_boto3_qldb.type_defs import (
    ClientCreateLedgerResponseTypeDef,
    ClientDescribeJournalS3ExportResponseTypeDef,
    ClientDescribeLedgerResponseTypeDef,
    ClientExportJournalToS3ResponseTypeDef,
    ClientExportJournalToS3S3ExportConfigurationTypeDef,
    ClientGetBlockBlockAddressTypeDef,
    ClientGetBlockDigestTipAddressTypeDef,
    ClientGetBlockResponseTypeDef,
    ClientGetDigestResponseTypeDef,
    ClientGetRevisionBlockAddressTypeDef,
    ClientGetRevisionDigestTipAddressTypeDef,
    ClientGetRevisionResponseTypeDef,
    ClientListJournalS3ExportsForLedgerResponseTypeDef,
    ClientListJournalS3ExportsResponseTypeDef,
    ClientListLedgersResponseTypeDef,
    ClientListTagsForResourceResponseTypeDef,
    ClientUpdateLedgerResponseTypeDef,
)


__all__ = ("QLDBClient",)


class QLDBClient:
    """
    [QLDB.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/qldb.html#QLDB.Client)
    """

    exceptions: "client_scope.Exceptions"

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/qldb.html#QLDB.Client.can_paginate)
        """

    def create_ledger(
        self,
        Name: str,
        PermissionsMode: str,
        Tags: Dict[str, str] = None,
        DeletionProtection: bool = None,
    ) -> ClientCreateLedgerResponseTypeDef:
        """
        [Client.create_ledger documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/qldb.html#QLDB.Client.create_ledger)
        """

    def delete_ledger(self, Name: str) -> None:
        """
        [Client.delete_ledger documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/qldb.html#QLDB.Client.delete_ledger)
        """

    def describe_journal_s3_export(
        self, Name: str, ExportId: str
    ) -> ClientDescribeJournalS3ExportResponseTypeDef:
        """
        [Client.describe_journal_s3_export documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/qldb.html#QLDB.Client.describe_journal_s3_export)
        """

    def describe_ledger(self, Name: str) -> ClientDescribeLedgerResponseTypeDef:
        """
        [Client.describe_ledger documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/qldb.html#QLDB.Client.describe_ledger)
        """

    def export_journal_to_s3(
        self,
        Name: str,
        InclusiveStartTime: datetime,
        ExclusiveEndTime: datetime,
        S3ExportConfiguration: ClientExportJournalToS3S3ExportConfigurationTypeDef,
        RoleArn: str,
    ) -> ClientExportJournalToS3ResponseTypeDef:
        """
        [Client.export_journal_to_s3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/qldb.html#QLDB.Client.export_journal_to_s3)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/qldb.html#QLDB.Client.generate_presigned_url)
        """

    def get_block(
        self,
        Name: str,
        BlockAddress: ClientGetBlockBlockAddressTypeDef,
        DigestTipAddress: ClientGetBlockDigestTipAddressTypeDef = None,
    ) -> ClientGetBlockResponseTypeDef:
        """
        [Client.get_block documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/qldb.html#QLDB.Client.get_block)
        """

    def get_digest(self, Name: str) -> ClientGetDigestResponseTypeDef:
        """
        [Client.get_digest documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/qldb.html#QLDB.Client.get_digest)
        """

    def get_revision(
        self,
        Name: str,
        BlockAddress: ClientGetRevisionBlockAddressTypeDef,
        DocumentId: str,
        DigestTipAddress: ClientGetRevisionDigestTipAddressTypeDef = None,
    ) -> ClientGetRevisionResponseTypeDef:
        """
        [Client.get_revision documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/qldb.html#QLDB.Client.get_revision)
        """

    def list_journal_s3_exports(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ClientListJournalS3ExportsResponseTypeDef:
        """
        [Client.list_journal_s3_exports documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/qldb.html#QLDB.Client.list_journal_s3_exports)
        """

    def list_journal_s3_exports_for_ledger(
        self, Name: str, MaxResults: int = None, NextToken: str = None
    ) -> ClientListJournalS3ExportsForLedgerResponseTypeDef:
        """
        [Client.list_journal_s3_exports_for_ledger documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/qldb.html#QLDB.Client.list_journal_s3_exports_for_ledger)
        """

    def list_ledgers(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ClientListLedgersResponseTypeDef:
        """
        [Client.list_ledgers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/qldb.html#QLDB.Client.list_ledgers)
        """

    def list_tags_for_resource(self, ResourceArn: str) -> ClientListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/qldb.html#QLDB.Client.list_tags_for_resource)
        """

    def tag_resource(self, ResourceArn: str, Tags: Dict[str, str]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/qldb.html#QLDB.Client.tag_resource)
        """

    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/qldb.html#QLDB.Client.untag_resource)
        """

    def update_ledger(
        self, Name: str, DeletionProtection: bool = None
    ) -> ClientUpdateLedgerResponseTypeDef:
        """
        [Client.update_ledger documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/qldb.html#QLDB.Client.update_ledger)
        """


class Exceptions:
    ClientError: Boto3ClientError
    InvalidParameterException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    ResourceAlreadyExistsException: Boto3ClientError
    ResourceInUseException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    ResourcePreconditionNotMetException: Boto3ClientError
