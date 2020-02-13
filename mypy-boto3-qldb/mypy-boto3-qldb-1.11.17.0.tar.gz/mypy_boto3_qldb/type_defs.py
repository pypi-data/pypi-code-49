"""
Main interface for qldb service type definitions.

Usage::

    from mypy_boto3.qldb.type_defs import ClientCreateLedgerResponseTypeDef

    data: ClientCreateLedgerResponseTypeDef = {...}
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
    "ClientCreateLedgerResponseTypeDef",
    "ClientDescribeJournalS3ExportResponseExportDescriptionS3ExportConfigurationEncryptionConfigurationTypeDef",
    "ClientDescribeJournalS3ExportResponseExportDescriptionS3ExportConfigurationTypeDef",
    "ClientDescribeJournalS3ExportResponseExportDescriptionTypeDef",
    "ClientDescribeJournalS3ExportResponseTypeDef",
    "ClientDescribeLedgerResponseTypeDef",
    "ClientExportJournalToS3ResponseTypeDef",
    "ClientExportJournalToS3S3ExportConfigurationEncryptionConfigurationTypeDef",
    "ClientExportJournalToS3S3ExportConfigurationTypeDef",
    "ClientGetBlockBlockAddressTypeDef",
    "ClientGetBlockDigestTipAddressTypeDef",
    "ClientGetBlockResponseBlockTypeDef",
    "ClientGetBlockResponseProofTypeDef",
    "ClientGetBlockResponseTypeDef",
    "ClientGetDigestResponseDigestTipAddressTypeDef",
    "ClientGetDigestResponseTypeDef",
    "ClientGetRevisionBlockAddressTypeDef",
    "ClientGetRevisionDigestTipAddressTypeDef",
    "ClientGetRevisionResponseProofTypeDef",
    "ClientGetRevisionResponseRevisionTypeDef",
    "ClientGetRevisionResponseTypeDef",
    "ClientListJournalS3ExportsForLedgerResponseJournalS3ExportsS3ExportConfigurationEncryptionConfigurationTypeDef",
    "ClientListJournalS3ExportsForLedgerResponseJournalS3ExportsS3ExportConfigurationTypeDef",
    "ClientListJournalS3ExportsForLedgerResponseJournalS3ExportsTypeDef",
    "ClientListJournalS3ExportsForLedgerResponseTypeDef",
    "ClientListJournalS3ExportsResponseJournalS3ExportsS3ExportConfigurationEncryptionConfigurationTypeDef",
    "ClientListJournalS3ExportsResponseJournalS3ExportsS3ExportConfigurationTypeDef",
    "ClientListJournalS3ExportsResponseJournalS3ExportsTypeDef",
    "ClientListJournalS3ExportsResponseTypeDef",
    "ClientListLedgersResponseLedgersTypeDef",
    "ClientListLedgersResponseTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientUpdateLedgerResponseTypeDef",
)

ClientCreateLedgerResponseTypeDef = TypedDict(
    "ClientCreateLedgerResponseTypeDef",
    {
        "Name": str,
        "Arn": str,
        "State": Literal["CREATING", "ACTIVE", "DELETING", "DELETED"],
        "CreationDateTime": datetime,
        "DeletionProtection": bool,
    },
    total=False,
)

ClientDescribeJournalS3ExportResponseExportDescriptionS3ExportConfigurationEncryptionConfigurationTypeDef = TypedDict(
    "ClientDescribeJournalS3ExportResponseExportDescriptionS3ExportConfigurationEncryptionConfigurationTypeDef",
    {"ObjectEncryptionType": Literal["SSE_KMS", "SSE_S3", "NO_ENCRYPTION"], "KmsKeyArn": str},
    total=False,
)

ClientDescribeJournalS3ExportResponseExportDescriptionS3ExportConfigurationTypeDef = TypedDict(
    "ClientDescribeJournalS3ExportResponseExportDescriptionS3ExportConfigurationTypeDef",
    {
        "Bucket": str,
        "Prefix": str,
        "EncryptionConfiguration": ClientDescribeJournalS3ExportResponseExportDescriptionS3ExportConfigurationEncryptionConfigurationTypeDef,
    },
    total=False,
)

ClientDescribeJournalS3ExportResponseExportDescriptionTypeDef = TypedDict(
    "ClientDescribeJournalS3ExportResponseExportDescriptionTypeDef",
    {
        "LedgerName": str,
        "ExportId": str,
        "ExportCreationTime": datetime,
        "Status": Literal["IN_PROGRESS", "COMPLETED", "CANCELLED"],
        "InclusiveStartTime": datetime,
        "ExclusiveEndTime": datetime,
        "S3ExportConfiguration": ClientDescribeJournalS3ExportResponseExportDescriptionS3ExportConfigurationTypeDef,
        "RoleArn": str,
    },
    total=False,
)

ClientDescribeJournalS3ExportResponseTypeDef = TypedDict(
    "ClientDescribeJournalS3ExportResponseTypeDef",
    {"ExportDescription": ClientDescribeJournalS3ExportResponseExportDescriptionTypeDef},
    total=False,
)

ClientDescribeLedgerResponseTypeDef = TypedDict(
    "ClientDescribeLedgerResponseTypeDef",
    {
        "Name": str,
        "Arn": str,
        "State": Literal["CREATING", "ACTIVE", "DELETING", "DELETED"],
        "CreationDateTime": datetime,
        "DeletionProtection": bool,
    },
    total=False,
)

ClientExportJournalToS3ResponseTypeDef = TypedDict(
    "ClientExportJournalToS3ResponseTypeDef", {"ExportId": str}, total=False
)

ClientExportJournalToS3S3ExportConfigurationEncryptionConfigurationTypeDef = TypedDict(
    "ClientExportJournalToS3S3ExportConfigurationEncryptionConfigurationTypeDef",
    {"ObjectEncryptionType": Literal["SSE_KMS", "SSE_S3", "NO_ENCRYPTION"], "KmsKeyArn": str},
    total=False,
)

_RequiredClientExportJournalToS3S3ExportConfigurationTypeDef = TypedDict(
    "_RequiredClientExportJournalToS3S3ExportConfigurationTypeDef", {"Bucket": str}
)
_OptionalClientExportJournalToS3S3ExportConfigurationTypeDef = TypedDict(
    "_OptionalClientExportJournalToS3S3ExportConfigurationTypeDef",
    {
        "Prefix": str,
        "EncryptionConfiguration": ClientExportJournalToS3S3ExportConfigurationEncryptionConfigurationTypeDef,
    },
    total=False,
)


class ClientExportJournalToS3S3ExportConfigurationTypeDef(
    _RequiredClientExportJournalToS3S3ExportConfigurationTypeDef,
    _OptionalClientExportJournalToS3S3ExportConfigurationTypeDef,
):
    pass


ClientGetBlockBlockAddressTypeDef = TypedDict(
    "ClientGetBlockBlockAddressTypeDef", {"IonText": str}, total=False
)

ClientGetBlockDigestTipAddressTypeDef = TypedDict(
    "ClientGetBlockDigestTipAddressTypeDef", {"IonText": str}, total=False
)

ClientGetBlockResponseBlockTypeDef = TypedDict(
    "ClientGetBlockResponseBlockTypeDef", {"IonText": str}, total=False
)

ClientGetBlockResponseProofTypeDef = TypedDict(
    "ClientGetBlockResponseProofTypeDef", {"IonText": str}, total=False
)

ClientGetBlockResponseTypeDef = TypedDict(
    "ClientGetBlockResponseTypeDef",
    {"Block": ClientGetBlockResponseBlockTypeDef, "Proof": ClientGetBlockResponseProofTypeDef},
    total=False,
)

ClientGetDigestResponseDigestTipAddressTypeDef = TypedDict(
    "ClientGetDigestResponseDigestTipAddressTypeDef", {"IonText": str}, total=False
)

ClientGetDigestResponseTypeDef = TypedDict(
    "ClientGetDigestResponseTypeDef",
    {"Digest": bytes, "DigestTipAddress": ClientGetDigestResponseDigestTipAddressTypeDef},
    total=False,
)

ClientGetRevisionBlockAddressTypeDef = TypedDict(
    "ClientGetRevisionBlockAddressTypeDef", {"IonText": str}, total=False
)

ClientGetRevisionDigestTipAddressTypeDef = TypedDict(
    "ClientGetRevisionDigestTipAddressTypeDef", {"IonText": str}, total=False
)

ClientGetRevisionResponseProofTypeDef = TypedDict(
    "ClientGetRevisionResponseProofTypeDef", {"IonText": str}, total=False
)

ClientGetRevisionResponseRevisionTypeDef = TypedDict(
    "ClientGetRevisionResponseRevisionTypeDef", {"IonText": str}, total=False
)

ClientGetRevisionResponseTypeDef = TypedDict(
    "ClientGetRevisionResponseTypeDef",
    {
        "Proof": ClientGetRevisionResponseProofTypeDef,
        "Revision": ClientGetRevisionResponseRevisionTypeDef,
    },
    total=False,
)

ClientListJournalS3ExportsForLedgerResponseJournalS3ExportsS3ExportConfigurationEncryptionConfigurationTypeDef = TypedDict(
    "ClientListJournalS3ExportsForLedgerResponseJournalS3ExportsS3ExportConfigurationEncryptionConfigurationTypeDef",
    {"ObjectEncryptionType": Literal["SSE_KMS", "SSE_S3", "NO_ENCRYPTION"], "KmsKeyArn": str},
    total=False,
)

ClientListJournalS3ExportsForLedgerResponseJournalS3ExportsS3ExportConfigurationTypeDef = TypedDict(
    "ClientListJournalS3ExportsForLedgerResponseJournalS3ExportsS3ExportConfigurationTypeDef",
    {
        "Bucket": str,
        "Prefix": str,
        "EncryptionConfiguration": ClientListJournalS3ExportsForLedgerResponseJournalS3ExportsS3ExportConfigurationEncryptionConfigurationTypeDef,
    },
    total=False,
)

ClientListJournalS3ExportsForLedgerResponseJournalS3ExportsTypeDef = TypedDict(
    "ClientListJournalS3ExportsForLedgerResponseJournalS3ExportsTypeDef",
    {
        "LedgerName": str,
        "ExportId": str,
        "ExportCreationTime": datetime,
        "Status": Literal["IN_PROGRESS", "COMPLETED", "CANCELLED"],
        "InclusiveStartTime": datetime,
        "ExclusiveEndTime": datetime,
        "S3ExportConfiguration": ClientListJournalS3ExportsForLedgerResponseJournalS3ExportsS3ExportConfigurationTypeDef,
        "RoleArn": str,
    },
    total=False,
)

ClientListJournalS3ExportsForLedgerResponseTypeDef = TypedDict(
    "ClientListJournalS3ExportsForLedgerResponseTypeDef",
    {
        "JournalS3Exports": List[
            ClientListJournalS3ExportsForLedgerResponseJournalS3ExportsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientListJournalS3ExportsResponseJournalS3ExportsS3ExportConfigurationEncryptionConfigurationTypeDef = TypedDict(
    "ClientListJournalS3ExportsResponseJournalS3ExportsS3ExportConfigurationEncryptionConfigurationTypeDef",
    {"ObjectEncryptionType": Literal["SSE_KMS", "SSE_S3", "NO_ENCRYPTION"], "KmsKeyArn": str},
    total=False,
)

ClientListJournalS3ExportsResponseJournalS3ExportsS3ExportConfigurationTypeDef = TypedDict(
    "ClientListJournalS3ExportsResponseJournalS3ExportsS3ExportConfigurationTypeDef",
    {
        "Bucket": str,
        "Prefix": str,
        "EncryptionConfiguration": ClientListJournalS3ExportsResponseJournalS3ExportsS3ExportConfigurationEncryptionConfigurationTypeDef,
    },
    total=False,
)

ClientListJournalS3ExportsResponseJournalS3ExportsTypeDef = TypedDict(
    "ClientListJournalS3ExportsResponseJournalS3ExportsTypeDef",
    {
        "LedgerName": str,
        "ExportId": str,
        "ExportCreationTime": datetime,
        "Status": Literal["IN_PROGRESS", "COMPLETED", "CANCELLED"],
        "InclusiveStartTime": datetime,
        "ExclusiveEndTime": datetime,
        "S3ExportConfiguration": ClientListJournalS3ExportsResponseJournalS3ExportsS3ExportConfigurationTypeDef,
        "RoleArn": str,
    },
    total=False,
)

ClientListJournalS3ExportsResponseTypeDef = TypedDict(
    "ClientListJournalS3ExportsResponseTypeDef",
    {
        "JournalS3Exports": List[ClientListJournalS3ExportsResponseJournalS3ExportsTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientListLedgersResponseLedgersTypeDef = TypedDict(
    "ClientListLedgersResponseLedgersTypeDef",
    {
        "Name": str,
        "State": Literal["CREATING", "ACTIVE", "DELETING", "DELETED"],
        "CreationDateTime": datetime,
    },
    total=False,
)

ClientListLedgersResponseTypeDef = TypedDict(
    "ClientListLedgersResponseTypeDef",
    {"Ledgers": List[ClientListLedgersResponseLedgersTypeDef], "NextToken": str},
    total=False,
)

ClientListTagsForResourceResponseTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTypeDef", {"Tags": Dict[str, str]}, total=False
)

ClientUpdateLedgerResponseTypeDef = TypedDict(
    "ClientUpdateLedgerResponseTypeDef",
    {
        "Name": str,
        "Arn": str,
        "State": Literal["CREATING", "ACTIVE", "DELETING", "DELETED"],
        "CreationDateTime": datetime,
        "DeletionProtection": bool,
    },
    total=False,
)
