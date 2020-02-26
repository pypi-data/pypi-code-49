"""
Main interface for glacier service type definitions.

Usage::

    from mypy_boto3.glacier.type_defs import ArchiveCreationOutputTypeDef

    data: ArchiveCreationOutputTypeDef = {...}
"""
import sys
from typing import Dict, IO, List, Union
from botocore.response import StreamingBody

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ArchiveCreationOutputTypeDef",
    "ClientCompleteMultipartUploadResponseTypeDef",
    "ClientCreateVaultResponseTypeDef",
    "ClientDescribeJobResponseInventoryRetrievalParametersTypeDef",
    "ClientDescribeJobResponseOutputLocationS3AccessControlListGranteeTypeDef",
    "ClientDescribeJobResponseOutputLocationS3AccessControlListTypeDef",
    "ClientDescribeJobResponseOutputLocationS3EncryptionTypeDef",
    "ClientDescribeJobResponseOutputLocationS3TypeDef",
    "ClientDescribeJobResponseOutputLocationTypeDef",
    "ClientDescribeJobResponseSelectParametersInputSerializationcsvTypeDef",
    "ClientDescribeJobResponseSelectParametersInputSerializationTypeDef",
    "ClientDescribeJobResponseSelectParametersOutputSerializationcsvTypeDef",
    "ClientDescribeJobResponseSelectParametersOutputSerializationTypeDef",
    "ClientDescribeJobResponseSelectParametersTypeDef",
    "ClientDescribeJobResponseTypeDef",
    "ClientDescribeVaultResponseTypeDef",
    "ClientGetDataRetrievalPolicyResponsePolicyRulesTypeDef",
    "ClientGetDataRetrievalPolicyResponsePolicyTypeDef",
    "ClientGetDataRetrievalPolicyResponseTypeDef",
    "ClientGetJobOutputResponseTypeDef",
    "ClientGetVaultAccessPolicyResponsepolicyTypeDef",
    "ClientGetVaultAccessPolicyResponseTypeDef",
    "ClientGetVaultLockResponseTypeDef",
    "ClientGetVaultNotificationsResponsevaultNotificationConfigTypeDef",
    "ClientGetVaultNotificationsResponseTypeDef",
    "ClientInitiateJobJobParametersInventoryRetrievalParametersTypeDef",
    "ClientInitiateJobJobParametersOutputLocationS3AccessControlListGranteeTypeDef",
    "ClientInitiateJobJobParametersOutputLocationS3AccessControlListTypeDef",
    "ClientInitiateJobJobParametersOutputLocationS3EncryptionTypeDef",
    "ClientInitiateJobJobParametersOutputLocationS3TypeDef",
    "ClientInitiateJobJobParametersOutputLocationTypeDef",
    "ClientInitiateJobJobParametersSelectParametersInputSerializationcsvTypeDef",
    "ClientInitiateJobJobParametersSelectParametersInputSerializationTypeDef",
    "ClientInitiateJobJobParametersSelectParametersOutputSerializationcsvTypeDef",
    "ClientInitiateJobJobParametersSelectParametersOutputSerializationTypeDef",
    "ClientInitiateJobJobParametersSelectParametersTypeDef",
    "ClientInitiateJobJobParametersTypeDef",
    "ClientInitiateJobResponseTypeDef",
    "ClientInitiateMultipartUploadResponseTypeDef",
    "ClientInitiateVaultLockPolicyTypeDef",
    "ClientInitiateVaultLockResponseTypeDef",
    "ClientListJobsResponseJobListInventoryRetrievalParametersTypeDef",
    "ClientListJobsResponseJobListOutputLocationS3AccessControlListGranteeTypeDef",
    "ClientListJobsResponseJobListOutputLocationS3AccessControlListTypeDef",
    "ClientListJobsResponseJobListOutputLocationS3EncryptionTypeDef",
    "ClientListJobsResponseJobListOutputLocationS3TypeDef",
    "ClientListJobsResponseJobListOutputLocationTypeDef",
    "ClientListJobsResponseJobListSelectParametersInputSerializationcsvTypeDef",
    "ClientListJobsResponseJobListSelectParametersInputSerializationTypeDef",
    "ClientListJobsResponseJobListSelectParametersOutputSerializationcsvTypeDef",
    "ClientListJobsResponseJobListSelectParametersOutputSerializationTypeDef",
    "ClientListJobsResponseJobListSelectParametersTypeDef",
    "ClientListJobsResponseJobListTypeDef",
    "ClientListJobsResponseTypeDef",
    "ClientListMultipartUploadsResponseUploadsListTypeDef",
    "ClientListMultipartUploadsResponseTypeDef",
    "ClientListPartsResponsePartsTypeDef",
    "ClientListPartsResponseTypeDef",
    "ClientListProvisionedCapacityResponseProvisionedCapacityListTypeDef",
    "ClientListProvisionedCapacityResponseTypeDef",
    "ClientListTagsForVaultResponseTypeDef",
    "ClientListVaultsResponseVaultListTypeDef",
    "ClientListVaultsResponseTypeDef",
    "ClientPurchaseProvisionedCapacityResponseTypeDef",
    "ClientSetDataRetrievalPolicyPolicyRulesTypeDef",
    "ClientSetDataRetrievalPolicyPolicyTypeDef",
    "ClientSetVaultAccessPolicyPolicyTypeDef",
    "ClientSetVaultNotificationsVaultNotificationConfigTypeDef",
    "ClientUploadArchiveResponseTypeDef",
    "ClientUploadMultipartPartResponseTypeDef",
    "CreateVaultOutputTypeDef",
    "GetJobOutputOutputTypeDef",
    "InitiateJobOutputTypeDef",
    "InitiateMultipartUploadOutputTypeDef",
    "InventoryRetrievalJobInputTypeDef",
    "EncryptionTypeDef",
    "GranteeTypeDef",
    "GrantTypeDef",
    "S3LocationTypeDef",
    "OutputLocationTypeDef",
    "CSVInputTypeDef",
    "InputSerializationTypeDef",
    "CSVOutputTypeDef",
    "OutputSerializationTypeDef",
    "SelectParametersTypeDef",
    "JobParametersTypeDef",
    "InventoryRetrievalJobDescriptionTypeDef",
    "GlacierJobDescriptionTypeDef",
    "ListJobsOutputTypeDef",
    "UploadListElementTypeDef",
    "ListMultipartUploadsOutputTypeDef",
    "PartListElementTypeDef",
    "ListPartsOutputTypeDef",
    "DescribeVaultOutputTypeDef",
    "ListVaultsOutputTypeDef",
    "PaginatorConfigTypeDef",
    "UploadMultipartPartOutputTypeDef",
    "VaultNotificationConfigTypeDef",
    "WaiterConfigTypeDef",
)

ArchiveCreationOutputTypeDef = TypedDict(
    "ArchiveCreationOutputTypeDef",
    {"location": str, "checksum": str, "archiveId": str},
    total=False,
)

ClientCompleteMultipartUploadResponseTypeDef = TypedDict(
    "ClientCompleteMultipartUploadResponseTypeDef",
    {"location": str, "checksum": str, "archiveId": str},
    total=False,
)

ClientCreateVaultResponseTypeDef = TypedDict(
    "ClientCreateVaultResponseTypeDef", {"location": str}, total=False
)

ClientDescribeJobResponseInventoryRetrievalParametersTypeDef = TypedDict(
    "ClientDescribeJobResponseInventoryRetrievalParametersTypeDef",
    {"Format": str, "StartDate": str, "EndDate": str, "Limit": str, "Marker": str},
    total=False,
)

ClientDescribeJobResponseOutputLocationS3AccessControlListGranteeTypeDef = TypedDict(
    "ClientDescribeJobResponseOutputLocationS3AccessControlListGranteeTypeDef",
    {
        "Type": Literal["AmazonCustomerByEmail", "CanonicalUser", "Group"],
        "DisplayName": str,
        "URI": str,
        "ID": str,
        "EmailAddress": str,
    },
    total=False,
)

ClientDescribeJobResponseOutputLocationS3AccessControlListTypeDef = TypedDict(
    "ClientDescribeJobResponseOutputLocationS3AccessControlListTypeDef",
    {
        "Grantee": ClientDescribeJobResponseOutputLocationS3AccessControlListGranteeTypeDef,
        "Permission": Literal["FULL_CONTROL", "WRITE", "WRITE_ACP", "READ", "READ_ACP"],
    },
    total=False,
)

ClientDescribeJobResponseOutputLocationS3EncryptionTypeDef = TypedDict(
    "ClientDescribeJobResponseOutputLocationS3EncryptionTypeDef",
    {"EncryptionType": Literal["aws:kms", "AES256"], "KMSKeyId": str, "KMSContext": str},
    total=False,
)

ClientDescribeJobResponseOutputLocationS3TypeDef = TypedDict(
    "ClientDescribeJobResponseOutputLocationS3TypeDef",
    {
        "BucketName": str,
        "Prefix": str,
        "Encryption": ClientDescribeJobResponseOutputLocationS3EncryptionTypeDef,
        "CannedACL": Literal[
            "private",
            "public-read",
            "public-read-write",
            "aws-exec-read",
            "authenticated-read",
            "bucket-owner-read",
            "bucket-owner-full-control",
        ],
        "AccessControlList": List[
            ClientDescribeJobResponseOutputLocationS3AccessControlListTypeDef
        ],
        "Tagging": Dict[str, str],
        "UserMetadata": Dict[str, str],
        "StorageClass": Literal["STANDARD", "REDUCED_REDUNDANCY", "STANDARD_IA"],
    },
    total=False,
)

ClientDescribeJobResponseOutputLocationTypeDef = TypedDict(
    "ClientDescribeJobResponseOutputLocationTypeDef",
    {"S3": ClientDescribeJobResponseOutputLocationS3TypeDef},
    total=False,
)

ClientDescribeJobResponseSelectParametersInputSerializationcsvTypeDef = TypedDict(
    "ClientDescribeJobResponseSelectParametersInputSerializationcsvTypeDef",
    {
        "FileHeaderInfo": Literal["USE", "IGNORE", "NONE"],
        "Comments": str,
        "QuoteEscapeCharacter": str,
        "RecordDelimiter": str,
        "FieldDelimiter": str,
        "QuoteCharacter": str,
    },
    total=False,
)

ClientDescribeJobResponseSelectParametersInputSerializationTypeDef = TypedDict(
    "ClientDescribeJobResponseSelectParametersInputSerializationTypeDef",
    {"csv": ClientDescribeJobResponseSelectParametersInputSerializationcsvTypeDef},
    total=False,
)

ClientDescribeJobResponseSelectParametersOutputSerializationcsvTypeDef = TypedDict(
    "ClientDescribeJobResponseSelectParametersOutputSerializationcsvTypeDef",
    {
        "QuoteFields": Literal["ALWAYS", "ASNEEDED"],
        "QuoteEscapeCharacter": str,
        "RecordDelimiter": str,
        "FieldDelimiter": str,
        "QuoteCharacter": str,
    },
    total=False,
)

ClientDescribeJobResponseSelectParametersOutputSerializationTypeDef = TypedDict(
    "ClientDescribeJobResponseSelectParametersOutputSerializationTypeDef",
    {"csv": ClientDescribeJobResponseSelectParametersOutputSerializationcsvTypeDef},
    total=False,
)

ClientDescribeJobResponseSelectParametersTypeDef = TypedDict(
    "ClientDescribeJobResponseSelectParametersTypeDef",
    {
        "InputSerialization": ClientDescribeJobResponseSelectParametersInputSerializationTypeDef,
        "ExpressionType": str,
        "Expression": str,
        "OutputSerialization": ClientDescribeJobResponseSelectParametersOutputSerializationTypeDef,
    },
    total=False,
)

ClientDescribeJobResponseTypeDef = TypedDict(
    "ClientDescribeJobResponseTypeDef",
    {
        "JobId": str,
        "JobDescription": str,
        "Action": Literal["ArchiveRetrieval", "InventoryRetrieval", "Select"],
        "ArchiveId": str,
        "VaultARN": str,
        "CreationDate": str,
        "Completed": bool,
        "StatusCode": Literal["InProgress", "Succeeded", "Failed"],
        "StatusMessage": str,
        "ArchiveSizeInBytes": int,
        "InventorySizeInBytes": int,
        "SNSTopic": str,
        "CompletionDate": str,
        "SHA256TreeHash": str,
        "ArchiveSHA256TreeHash": str,
        "RetrievalByteRange": str,
        "Tier": str,
        "InventoryRetrievalParameters": ClientDescribeJobResponseInventoryRetrievalParametersTypeDef,
        "JobOutputPath": str,
        "SelectParameters": ClientDescribeJobResponseSelectParametersTypeDef,
        "OutputLocation": ClientDescribeJobResponseOutputLocationTypeDef,
    },
    total=False,
)

ClientDescribeVaultResponseTypeDef = TypedDict(
    "ClientDescribeVaultResponseTypeDef",
    {
        "VaultARN": str,
        "VaultName": str,
        "CreationDate": str,
        "LastInventoryDate": str,
        "NumberOfArchives": int,
        "SizeInBytes": int,
    },
    total=False,
)

ClientGetDataRetrievalPolicyResponsePolicyRulesTypeDef = TypedDict(
    "ClientGetDataRetrievalPolicyResponsePolicyRulesTypeDef",
    {"Strategy": str, "BytesPerHour": int},
    total=False,
)

ClientGetDataRetrievalPolicyResponsePolicyTypeDef = TypedDict(
    "ClientGetDataRetrievalPolicyResponsePolicyTypeDef",
    {"Rules": List[ClientGetDataRetrievalPolicyResponsePolicyRulesTypeDef]},
    total=False,
)

ClientGetDataRetrievalPolicyResponseTypeDef = TypedDict(
    "ClientGetDataRetrievalPolicyResponseTypeDef",
    {"Policy": ClientGetDataRetrievalPolicyResponsePolicyTypeDef},
    total=False,
)

ClientGetJobOutputResponseTypeDef = TypedDict(
    "ClientGetJobOutputResponseTypeDef",
    {
        "body": StreamingBody,
        "checksum": str,
        "status": int,
        "contentRange": str,
        "acceptRanges": str,
        "contentType": str,
        "archiveDescription": str,
    },
    total=False,
)

ClientGetVaultAccessPolicyResponsepolicyTypeDef = TypedDict(
    "ClientGetVaultAccessPolicyResponsepolicyTypeDef", {"Policy": str}, total=False
)

ClientGetVaultAccessPolicyResponseTypeDef = TypedDict(
    "ClientGetVaultAccessPolicyResponseTypeDef",
    {"policy": ClientGetVaultAccessPolicyResponsepolicyTypeDef},
    total=False,
)

ClientGetVaultLockResponseTypeDef = TypedDict(
    "ClientGetVaultLockResponseTypeDef",
    {"Policy": str, "State": str, "ExpirationDate": str, "CreationDate": str},
    total=False,
)

ClientGetVaultNotificationsResponsevaultNotificationConfigTypeDef = TypedDict(
    "ClientGetVaultNotificationsResponsevaultNotificationConfigTypeDef",
    {"SNSTopic": str, "Events": List[str]},
    total=False,
)

ClientGetVaultNotificationsResponseTypeDef = TypedDict(
    "ClientGetVaultNotificationsResponseTypeDef",
    {"vaultNotificationConfig": ClientGetVaultNotificationsResponsevaultNotificationConfigTypeDef},
    total=False,
)

ClientInitiateJobJobParametersInventoryRetrievalParametersTypeDef = TypedDict(
    "ClientInitiateJobJobParametersInventoryRetrievalParametersTypeDef",
    {"StartDate": str, "EndDate": str, "Limit": str, "Marker": str},
    total=False,
)

ClientInitiateJobJobParametersOutputLocationS3AccessControlListGranteeTypeDef = TypedDict(
    "ClientInitiateJobJobParametersOutputLocationS3AccessControlListGranteeTypeDef",
    {
        "Type": Literal["AmazonCustomerByEmail", "CanonicalUser", "Group"],
        "DisplayName": str,
        "URI": str,
        "ID": str,
        "EmailAddress": str,
    },
    total=False,
)

ClientInitiateJobJobParametersOutputLocationS3AccessControlListTypeDef = TypedDict(
    "ClientInitiateJobJobParametersOutputLocationS3AccessControlListTypeDef",
    {
        "Grantee": ClientInitiateJobJobParametersOutputLocationS3AccessControlListGranteeTypeDef,
        "Permission": Literal["FULL_CONTROL", "WRITE", "WRITE_ACP", "READ", "READ_ACP"],
    },
    total=False,
)

ClientInitiateJobJobParametersOutputLocationS3EncryptionTypeDef = TypedDict(
    "ClientInitiateJobJobParametersOutputLocationS3EncryptionTypeDef",
    {"EncryptionType": Literal["aws:kms", "AES256"], "KMSKeyId": str, "KMSContext": str},
    total=False,
)

ClientInitiateJobJobParametersOutputLocationS3TypeDef = TypedDict(
    "ClientInitiateJobJobParametersOutputLocationS3TypeDef",
    {
        "BucketName": str,
        "Prefix": str,
        "Encryption": ClientInitiateJobJobParametersOutputLocationS3EncryptionTypeDef,
        "CannedACL": Literal[
            "private",
            "public-read",
            "public-read-write",
            "aws-exec-read",
            "authenticated-read",
            "bucket-owner-read",
            "bucket-owner-full-control",
        ],
        "AccessControlList": List[
            ClientInitiateJobJobParametersOutputLocationS3AccessControlListTypeDef
        ],
        "Tagging": Dict[str, str],
        "UserMetadata": Dict[str, str],
        "StorageClass": Literal["STANDARD", "REDUCED_REDUNDANCY", "STANDARD_IA"],
    },
    total=False,
)

ClientInitiateJobJobParametersOutputLocationTypeDef = TypedDict(
    "ClientInitiateJobJobParametersOutputLocationTypeDef",
    {"S3": ClientInitiateJobJobParametersOutputLocationS3TypeDef},
    total=False,
)

ClientInitiateJobJobParametersSelectParametersInputSerializationcsvTypeDef = TypedDict(
    "ClientInitiateJobJobParametersSelectParametersInputSerializationcsvTypeDef",
    {
        "FileHeaderInfo": Literal["USE", "IGNORE", "NONE"],
        "Comments": str,
        "QuoteEscapeCharacter": str,
        "RecordDelimiter": str,
        "FieldDelimiter": str,
        "QuoteCharacter": str,
    },
    total=False,
)

ClientInitiateJobJobParametersSelectParametersInputSerializationTypeDef = TypedDict(
    "ClientInitiateJobJobParametersSelectParametersInputSerializationTypeDef",
    {"csv": ClientInitiateJobJobParametersSelectParametersInputSerializationcsvTypeDef},
    total=False,
)

ClientInitiateJobJobParametersSelectParametersOutputSerializationcsvTypeDef = TypedDict(
    "ClientInitiateJobJobParametersSelectParametersOutputSerializationcsvTypeDef",
    {
        "QuoteFields": Literal["ALWAYS", "ASNEEDED"],
        "QuoteEscapeCharacter": str,
        "RecordDelimiter": str,
        "FieldDelimiter": str,
        "QuoteCharacter": str,
    },
    total=False,
)

ClientInitiateJobJobParametersSelectParametersOutputSerializationTypeDef = TypedDict(
    "ClientInitiateJobJobParametersSelectParametersOutputSerializationTypeDef",
    {"csv": ClientInitiateJobJobParametersSelectParametersOutputSerializationcsvTypeDef},
    total=False,
)

ClientInitiateJobJobParametersSelectParametersTypeDef = TypedDict(
    "ClientInitiateJobJobParametersSelectParametersTypeDef",
    {
        "InputSerialization": ClientInitiateJobJobParametersSelectParametersInputSerializationTypeDef,
        "ExpressionType": str,
        "Expression": str,
        "OutputSerialization": ClientInitiateJobJobParametersSelectParametersOutputSerializationTypeDef,
    },
    total=False,
)

ClientInitiateJobJobParametersTypeDef = TypedDict(
    "ClientInitiateJobJobParametersTypeDef",
    {
        "Format": str,
        "Type": str,
        "ArchiveId": str,
        "Description": str,
        "SNSTopic": str,
        "RetrievalByteRange": str,
        "Tier": str,
        "InventoryRetrievalParameters": ClientInitiateJobJobParametersInventoryRetrievalParametersTypeDef,
        "SelectParameters": ClientInitiateJobJobParametersSelectParametersTypeDef,
        "OutputLocation": ClientInitiateJobJobParametersOutputLocationTypeDef,
    },
    total=False,
)

ClientInitiateJobResponseTypeDef = TypedDict(
    "ClientInitiateJobResponseTypeDef",
    {"location": str, "jobId": str, "jobOutputPath": str},
    total=False,
)

ClientInitiateMultipartUploadResponseTypeDef = TypedDict(
    "ClientInitiateMultipartUploadResponseTypeDef", {"location": str, "uploadId": str}, total=False
)

ClientInitiateVaultLockPolicyTypeDef = TypedDict(
    "ClientInitiateVaultLockPolicyTypeDef", {"Policy": str}, total=False
)

ClientInitiateVaultLockResponseTypeDef = TypedDict(
    "ClientInitiateVaultLockResponseTypeDef", {"lockId": str}, total=False
)

ClientListJobsResponseJobListInventoryRetrievalParametersTypeDef = TypedDict(
    "ClientListJobsResponseJobListInventoryRetrievalParametersTypeDef",
    {"Format": str, "StartDate": str, "EndDate": str, "Limit": str, "Marker": str},
    total=False,
)

ClientListJobsResponseJobListOutputLocationS3AccessControlListGranteeTypeDef = TypedDict(
    "ClientListJobsResponseJobListOutputLocationS3AccessControlListGranteeTypeDef",
    {
        "Type": Literal["AmazonCustomerByEmail", "CanonicalUser", "Group"],
        "DisplayName": str,
        "URI": str,
        "ID": str,
        "EmailAddress": str,
    },
    total=False,
)

ClientListJobsResponseJobListOutputLocationS3AccessControlListTypeDef = TypedDict(
    "ClientListJobsResponseJobListOutputLocationS3AccessControlListTypeDef",
    {
        "Grantee": ClientListJobsResponseJobListOutputLocationS3AccessControlListGranteeTypeDef,
        "Permission": Literal["FULL_CONTROL", "WRITE", "WRITE_ACP", "READ", "READ_ACP"],
    },
    total=False,
)

ClientListJobsResponseJobListOutputLocationS3EncryptionTypeDef = TypedDict(
    "ClientListJobsResponseJobListOutputLocationS3EncryptionTypeDef",
    {"EncryptionType": Literal["aws:kms", "AES256"], "KMSKeyId": str, "KMSContext": str},
    total=False,
)

ClientListJobsResponseJobListOutputLocationS3TypeDef = TypedDict(
    "ClientListJobsResponseJobListOutputLocationS3TypeDef",
    {
        "BucketName": str,
        "Prefix": str,
        "Encryption": ClientListJobsResponseJobListOutputLocationS3EncryptionTypeDef,
        "CannedACL": Literal[
            "private",
            "public-read",
            "public-read-write",
            "aws-exec-read",
            "authenticated-read",
            "bucket-owner-read",
            "bucket-owner-full-control",
        ],
        "AccessControlList": List[
            ClientListJobsResponseJobListOutputLocationS3AccessControlListTypeDef
        ],
        "Tagging": Dict[str, str],
        "UserMetadata": Dict[str, str],
        "StorageClass": Literal["STANDARD", "REDUCED_REDUNDANCY", "STANDARD_IA"],
    },
    total=False,
)

ClientListJobsResponseJobListOutputLocationTypeDef = TypedDict(
    "ClientListJobsResponseJobListOutputLocationTypeDef",
    {"S3": ClientListJobsResponseJobListOutputLocationS3TypeDef},
    total=False,
)

ClientListJobsResponseJobListSelectParametersInputSerializationcsvTypeDef = TypedDict(
    "ClientListJobsResponseJobListSelectParametersInputSerializationcsvTypeDef",
    {
        "FileHeaderInfo": Literal["USE", "IGNORE", "NONE"],
        "Comments": str,
        "QuoteEscapeCharacter": str,
        "RecordDelimiter": str,
        "FieldDelimiter": str,
        "QuoteCharacter": str,
    },
    total=False,
)

ClientListJobsResponseJobListSelectParametersInputSerializationTypeDef = TypedDict(
    "ClientListJobsResponseJobListSelectParametersInputSerializationTypeDef",
    {"csv": ClientListJobsResponseJobListSelectParametersInputSerializationcsvTypeDef},
    total=False,
)

ClientListJobsResponseJobListSelectParametersOutputSerializationcsvTypeDef = TypedDict(
    "ClientListJobsResponseJobListSelectParametersOutputSerializationcsvTypeDef",
    {
        "QuoteFields": Literal["ALWAYS", "ASNEEDED"],
        "QuoteEscapeCharacter": str,
        "RecordDelimiter": str,
        "FieldDelimiter": str,
        "QuoteCharacter": str,
    },
    total=False,
)

ClientListJobsResponseJobListSelectParametersOutputSerializationTypeDef = TypedDict(
    "ClientListJobsResponseJobListSelectParametersOutputSerializationTypeDef",
    {"csv": ClientListJobsResponseJobListSelectParametersOutputSerializationcsvTypeDef},
    total=False,
)

ClientListJobsResponseJobListSelectParametersTypeDef = TypedDict(
    "ClientListJobsResponseJobListSelectParametersTypeDef",
    {
        "InputSerialization": ClientListJobsResponseJobListSelectParametersInputSerializationTypeDef,
        "ExpressionType": str,
        "Expression": str,
        "OutputSerialization": ClientListJobsResponseJobListSelectParametersOutputSerializationTypeDef,
    },
    total=False,
)

ClientListJobsResponseJobListTypeDef = TypedDict(
    "ClientListJobsResponseJobListTypeDef",
    {
        "JobId": str,
        "JobDescription": str,
        "Action": Literal["ArchiveRetrieval", "InventoryRetrieval", "Select"],
        "ArchiveId": str,
        "VaultARN": str,
        "CreationDate": str,
        "Completed": bool,
        "StatusCode": Literal["InProgress", "Succeeded", "Failed"],
        "StatusMessage": str,
        "ArchiveSizeInBytes": int,
        "InventorySizeInBytes": int,
        "SNSTopic": str,
        "CompletionDate": str,
        "SHA256TreeHash": str,
        "ArchiveSHA256TreeHash": str,
        "RetrievalByteRange": str,
        "Tier": str,
        "InventoryRetrievalParameters": ClientListJobsResponseJobListInventoryRetrievalParametersTypeDef,
        "JobOutputPath": str,
        "SelectParameters": ClientListJobsResponseJobListSelectParametersTypeDef,
        "OutputLocation": ClientListJobsResponseJobListOutputLocationTypeDef,
    },
    total=False,
)

ClientListJobsResponseTypeDef = TypedDict(
    "ClientListJobsResponseTypeDef",
    {"JobList": List[ClientListJobsResponseJobListTypeDef], "Marker": str},
    total=False,
)

ClientListMultipartUploadsResponseUploadsListTypeDef = TypedDict(
    "ClientListMultipartUploadsResponseUploadsListTypeDef",
    {
        "MultipartUploadId": str,
        "VaultARN": str,
        "ArchiveDescription": str,
        "PartSizeInBytes": int,
        "CreationDate": str,
    },
    total=False,
)

ClientListMultipartUploadsResponseTypeDef = TypedDict(
    "ClientListMultipartUploadsResponseTypeDef",
    {"UploadsList": List[ClientListMultipartUploadsResponseUploadsListTypeDef], "Marker": str},
    total=False,
)

ClientListPartsResponsePartsTypeDef = TypedDict(
    "ClientListPartsResponsePartsTypeDef", {"RangeInBytes": str, "SHA256TreeHash": str}, total=False
)

ClientListPartsResponseTypeDef = TypedDict(
    "ClientListPartsResponseTypeDef",
    {
        "MultipartUploadId": str,
        "VaultARN": str,
        "ArchiveDescription": str,
        "PartSizeInBytes": int,
        "CreationDate": str,
        "Parts": List[ClientListPartsResponsePartsTypeDef],
        "Marker": str,
    },
    total=False,
)

ClientListProvisionedCapacityResponseProvisionedCapacityListTypeDef = TypedDict(
    "ClientListProvisionedCapacityResponseProvisionedCapacityListTypeDef",
    {"CapacityId": str, "StartDate": str, "ExpirationDate": str},
    total=False,
)

ClientListProvisionedCapacityResponseTypeDef = TypedDict(
    "ClientListProvisionedCapacityResponseTypeDef",
    {
        "ProvisionedCapacityList": List[
            ClientListProvisionedCapacityResponseProvisionedCapacityListTypeDef
        ]
    },
    total=False,
)

ClientListTagsForVaultResponseTypeDef = TypedDict(
    "ClientListTagsForVaultResponseTypeDef", {"Tags": Dict[str, str]}, total=False
)

ClientListVaultsResponseVaultListTypeDef = TypedDict(
    "ClientListVaultsResponseVaultListTypeDef",
    {
        "VaultARN": str,
        "VaultName": str,
        "CreationDate": str,
        "LastInventoryDate": str,
        "NumberOfArchives": int,
        "SizeInBytes": int,
    },
    total=False,
)

ClientListVaultsResponseTypeDef = TypedDict(
    "ClientListVaultsResponseTypeDef",
    {"VaultList": List[ClientListVaultsResponseVaultListTypeDef], "Marker": str},
    total=False,
)

ClientPurchaseProvisionedCapacityResponseTypeDef = TypedDict(
    "ClientPurchaseProvisionedCapacityResponseTypeDef", {"capacityId": str}, total=False
)

ClientSetDataRetrievalPolicyPolicyRulesTypeDef = TypedDict(
    "ClientSetDataRetrievalPolicyPolicyRulesTypeDef",
    {"Strategy": str, "BytesPerHour": int},
    total=False,
)

ClientSetDataRetrievalPolicyPolicyTypeDef = TypedDict(
    "ClientSetDataRetrievalPolicyPolicyTypeDef",
    {"Rules": List[ClientSetDataRetrievalPolicyPolicyRulesTypeDef]},
    total=False,
)

ClientSetVaultAccessPolicyPolicyTypeDef = TypedDict(
    "ClientSetVaultAccessPolicyPolicyTypeDef", {"Policy": str}, total=False
)

ClientSetVaultNotificationsVaultNotificationConfigTypeDef = TypedDict(
    "ClientSetVaultNotificationsVaultNotificationConfigTypeDef",
    {"SNSTopic": str, "Events": List[str]},
    total=False,
)

ClientUploadArchiveResponseTypeDef = TypedDict(
    "ClientUploadArchiveResponseTypeDef",
    {"location": str, "checksum": str, "archiveId": str},
    total=False,
)

ClientUploadMultipartPartResponseTypeDef = TypedDict(
    "ClientUploadMultipartPartResponseTypeDef", {"checksum": str}, total=False
)

CreateVaultOutputTypeDef = TypedDict("CreateVaultOutputTypeDef", {"location": str}, total=False)

GetJobOutputOutputTypeDef = TypedDict(
    "GetJobOutputOutputTypeDef",
    {
        "body": Union[bytes, IO],
        "checksum": str,
        "status": int,
        "contentRange": str,
        "acceptRanges": str,
        "contentType": str,
        "archiveDescription": str,
    },
    total=False,
)

InitiateJobOutputTypeDef = TypedDict(
    "InitiateJobOutputTypeDef", {"location": str, "jobId": str, "jobOutputPath": str}, total=False
)

InitiateMultipartUploadOutputTypeDef = TypedDict(
    "InitiateMultipartUploadOutputTypeDef", {"location": str, "uploadId": str}, total=False
)

InventoryRetrievalJobInputTypeDef = TypedDict(
    "InventoryRetrievalJobInputTypeDef",
    {"StartDate": str, "EndDate": str, "Limit": str, "Marker": str},
    total=False,
)

EncryptionTypeDef = TypedDict(
    "EncryptionTypeDef",
    {"EncryptionType": Literal["aws:kms", "AES256"], "KMSKeyId": str, "KMSContext": str},
    total=False,
)

_RequiredGranteeTypeDef = TypedDict(
    "_RequiredGranteeTypeDef", {"Type": Literal["AmazonCustomerByEmail", "CanonicalUser", "Group"]}
)
_OptionalGranteeTypeDef = TypedDict(
    "_OptionalGranteeTypeDef",
    {"DisplayName": str, "URI": str, "ID": str, "EmailAddress": str},
    total=False,
)


class GranteeTypeDef(_RequiredGranteeTypeDef, _OptionalGranteeTypeDef):
    pass


GrantTypeDef = TypedDict(
    "GrantTypeDef",
    {
        "Grantee": GranteeTypeDef,
        "Permission": Literal["FULL_CONTROL", "WRITE", "WRITE_ACP", "READ", "READ_ACP"],
    },
    total=False,
)

S3LocationTypeDef = TypedDict(
    "S3LocationTypeDef",
    {
        "BucketName": str,
        "Prefix": str,
        "Encryption": EncryptionTypeDef,
        "CannedACL": Literal[
            "private",
            "public-read",
            "public-read-write",
            "aws-exec-read",
            "authenticated-read",
            "bucket-owner-read",
            "bucket-owner-full-control",
        ],
        "AccessControlList": List[GrantTypeDef],
        "Tagging": Dict[str, str],
        "UserMetadata": Dict[str, str],
        "StorageClass": Literal["STANDARD", "REDUCED_REDUNDANCY", "STANDARD_IA"],
    },
    total=False,
)

OutputLocationTypeDef = TypedDict("OutputLocationTypeDef", {"S3": S3LocationTypeDef}, total=False)

CSVInputTypeDef = TypedDict(
    "CSVInputTypeDef",
    {
        "FileHeaderInfo": Literal["USE", "IGNORE", "NONE"],
        "Comments": str,
        "QuoteEscapeCharacter": str,
        "RecordDelimiter": str,
        "FieldDelimiter": str,
        "QuoteCharacter": str,
    },
    total=False,
)

InputSerializationTypeDef = TypedDict(
    "InputSerializationTypeDef", {"csv": CSVInputTypeDef}, total=False
)

CSVOutputTypeDef = TypedDict(
    "CSVOutputTypeDef",
    {
        "QuoteFields": Literal["ALWAYS", "ASNEEDED"],
        "QuoteEscapeCharacter": str,
        "RecordDelimiter": str,
        "FieldDelimiter": str,
        "QuoteCharacter": str,
    },
    total=False,
)

OutputSerializationTypeDef = TypedDict(
    "OutputSerializationTypeDef", {"csv": CSVOutputTypeDef}, total=False
)

SelectParametersTypeDef = TypedDict(
    "SelectParametersTypeDef",
    {
        "InputSerialization": InputSerializationTypeDef,
        "ExpressionType": Literal["SQL"],
        "Expression": str,
        "OutputSerialization": OutputSerializationTypeDef,
    },
    total=False,
)

JobParametersTypeDef = TypedDict(
    "JobParametersTypeDef",
    {
        "Format": str,
        "Type": str,
        "ArchiveId": str,
        "Description": str,
        "SNSTopic": str,
        "RetrievalByteRange": str,
        "Tier": str,
        "InventoryRetrievalParameters": InventoryRetrievalJobInputTypeDef,
        "SelectParameters": SelectParametersTypeDef,
        "OutputLocation": OutputLocationTypeDef,
    },
    total=False,
)

InventoryRetrievalJobDescriptionTypeDef = TypedDict(
    "InventoryRetrievalJobDescriptionTypeDef",
    {"Format": str, "StartDate": str, "EndDate": str, "Limit": str, "Marker": str},
    total=False,
)

GlacierJobDescriptionTypeDef = TypedDict(
    "GlacierJobDescriptionTypeDef",
    {
        "JobId": str,
        "JobDescription": str,
        "Action": Literal["ArchiveRetrieval", "InventoryRetrieval", "Select"],
        "ArchiveId": str,
        "VaultARN": str,
        "CreationDate": str,
        "Completed": bool,
        "StatusCode": Literal["InProgress", "Succeeded", "Failed"],
        "StatusMessage": str,
        "ArchiveSizeInBytes": int,
        "InventorySizeInBytes": int,
        "SNSTopic": str,
        "CompletionDate": str,
        "SHA256TreeHash": str,
        "ArchiveSHA256TreeHash": str,
        "RetrievalByteRange": str,
        "Tier": str,
        "InventoryRetrievalParameters": InventoryRetrievalJobDescriptionTypeDef,
        "JobOutputPath": str,
        "SelectParameters": SelectParametersTypeDef,
        "OutputLocation": OutputLocationTypeDef,
    },
    total=False,
)

ListJobsOutputTypeDef = TypedDict(
    "ListJobsOutputTypeDef",
    {"JobList": List[GlacierJobDescriptionTypeDef], "Marker": str},
    total=False,
)

UploadListElementTypeDef = TypedDict(
    "UploadListElementTypeDef",
    {
        "MultipartUploadId": str,
        "VaultARN": str,
        "ArchiveDescription": str,
        "PartSizeInBytes": int,
        "CreationDate": str,
    },
    total=False,
)

ListMultipartUploadsOutputTypeDef = TypedDict(
    "ListMultipartUploadsOutputTypeDef",
    {"UploadsList": List[UploadListElementTypeDef], "Marker": str},
    total=False,
)

PartListElementTypeDef = TypedDict(
    "PartListElementTypeDef", {"RangeInBytes": str, "SHA256TreeHash": str}, total=False
)

ListPartsOutputTypeDef = TypedDict(
    "ListPartsOutputTypeDef",
    {
        "MultipartUploadId": str,
        "VaultARN": str,
        "ArchiveDescription": str,
        "PartSizeInBytes": int,
        "CreationDate": str,
        "Parts": List[PartListElementTypeDef],
        "Marker": str,
    },
    total=False,
)

DescribeVaultOutputTypeDef = TypedDict(
    "DescribeVaultOutputTypeDef",
    {
        "VaultARN": str,
        "VaultName": str,
        "CreationDate": str,
        "LastInventoryDate": str,
        "NumberOfArchives": int,
        "SizeInBytes": int,
    },
    total=False,
)

ListVaultsOutputTypeDef = TypedDict(
    "ListVaultsOutputTypeDef",
    {"VaultList": List[DescribeVaultOutputTypeDef], "Marker": str},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

UploadMultipartPartOutputTypeDef = TypedDict(
    "UploadMultipartPartOutputTypeDef", {"checksum": str}, total=False
)

VaultNotificationConfigTypeDef = TypedDict(
    "VaultNotificationConfigTypeDef", {"SNSTopic": str, "Events": List[str]}, total=False
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)
