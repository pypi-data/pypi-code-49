"""
Main interface for s3control service type definitions.

Usage::

    from mypy_boto3.s3control.type_defs import ClientCreateAccessPointPublicAccessBlockConfigurationTypeDef

    data: ClientCreateAccessPointPublicAccessBlockConfigurationTypeDef = {...}
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
    "ClientCreateAccessPointPublicAccessBlockConfigurationTypeDef",
    "ClientCreateAccessPointVpcConfigurationTypeDef",
    "ClientCreateJobManifestLocationTypeDef",
    "ClientCreateJobManifestSpecTypeDef",
    "ClientCreateJobManifestTypeDef",
    "ClientCreateJobOperationLambdaInvokeTypeDef",
    "ClientCreateJobOperationS3InitiateRestoreObjectTypeDef",
    "ClientCreateJobOperationS3PutObjectAclAccessControlPolicyAccessControlListGrantsGranteeTypeDef",
    "ClientCreateJobOperationS3PutObjectAclAccessControlPolicyAccessControlListGrantsTypeDef",
    "ClientCreateJobOperationS3PutObjectAclAccessControlPolicyAccessControlListOwnerTypeDef",
    "ClientCreateJobOperationS3PutObjectAclAccessControlPolicyAccessControlListTypeDef",
    "ClientCreateJobOperationS3PutObjectAclAccessControlPolicyTypeDef",
    "ClientCreateJobOperationS3PutObjectAclTypeDef",
    "ClientCreateJobOperationS3PutObjectCopyAccessControlGrantsGranteeTypeDef",
    "ClientCreateJobOperationS3PutObjectCopyAccessControlGrantsTypeDef",
    "ClientCreateJobOperationS3PutObjectCopyNewObjectMetadataTypeDef",
    "ClientCreateJobOperationS3PutObjectCopyNewObjectTaggingTypeDef",
    "ClientCreateJobOperationS3PutObjectCopyTypeDef",
    "ClientCreateJobOperationS3PutObjectTaggingTagSetTypeDef",
    "ClientCreateJobOperationS3PutObjectTaggingTypeDef",
    "ClientCreateJobOperationTypeDef",
    "ClientCreateJobReportTypeDef",
    "ClientCreateJobResponseTypeDef",
    "ClientDescribeJobResponseJobFailureReasonsTypeDef",
    "ClientDescribeJobResponseJobManifestLocationTypeDef",
    "ClientDescribeJobResponseJobManifestSpecTypeDef",
    "ClientDescribeJobResponseJobManifestTypeDef",
    "ClientDescribeJobResponseJobOperationLambdaInvokeTypeDef",
    "ClientDescribeJobResponseJobOperationS3InitiateRestoreObjectTypeDef",
    "ClientDescribeJobResponseJobOperationS3PutObjectAclAccessControlPolicyAccessControlListGrantsGranteeTypeDef",
    "ClientDescribeJobResponseJobOperationS3PutObjectAclAccessControlPolicyAccessControlListGrantsTypeDef",
    "ClientDescribeJobResponseJobOperationS3PutObjectAclAccessControlPolicyAccessControlListOwnerTypeDef",
    "ClientDescribeJobResponseJobOperationS3PutObjectAclAccessControlPolicyAccessControlListTypeDef",
    "ClientDescribeJobResponseJobOperationS3PutObjectAclAccessControlPolicyTypeDef",
    "ClientDescribeJobResponseJobOperationS3PutObjectAclTypeDef",
    "ClientDescribeJobResponseJobOperationS3PutObjectCopyAccessControlGrantsGranteeTypeDef",
    "ClientDescribeJobResponseJobOperationS3PutObjectCopyAccessControlGrantsTypeDef",
    "ClientDescribeJobResponseJobOperationS3PutObjectCopyNewObjectMetadataTypeDef",
    "ClientDescribeJobResponseJobOperationS3PutObjectCopyNewObjectTaggingTypeDef",
    "ClientDescribeJobResponseJobOperationS3PutObjectCopyTypeDef",
    "ClientDescribeJobResponseJobOperationS3PutObjectTaggingTagSetTypeDef",
    "ClientDescribeJobResponseJobOperationS3PutObjectTaggingTypeDef",
    "ClientDescribeJobResponseJobOperationTypeDef",
    "ClientDescribeJobResponseJobProgressSummaryTypeDef",
    "ClientDescribeJobResponseJobReportTypeDef",
    "ClientDescribeJobResponseJobTypeDef",
    "ClientDescribeJobResponseTypeDef",
    "ClientGetAccessPointPolicyResponseTypeDef",
    "ClientGetAccessPointPolicyStatusResponsePolicyStatusTypeDef",
    "ClientGetAccessPointPolicyStatusResponseTypeDef",
    "ClientGetAccessPointResponsePublicAccessBlockConfigurationTypeDef",
    "ClientGetAccessPointResponseVpcConfigurationTypeDef",
    "ClientGetAccessPointResponseTypeDef",
    "ClientGetPublicAccessBlockResponsePublicAccessBlockConfigurationTypeDef",
    "ClientGetPublicAccessBlockResponseTypeDef",
    "ClientListAccessPointsResponseAccessPointListVpcConfigurationTypeDef",
    "ClientListAccessPointsResponseAccessPointListTypeDef",
    "ClientListAccessPointsResponseTypeDef",
    "ClientListJobsResponseJobsProgressSummaryTypeDef",
    "ClientListJobsResponseJobsTypeDef",
    "ClientListJobsResponseTypeDef",
    "ClientPutPublicAccessBlockPublicAccessBlockConfigurationTypeDef",
    "ClientUpdateJobPriorityResponseTypeDef",
    "ClientUpdateJobStatusResponseTypeDef",
)

ClientCreateAccessPointPublicAccessBlockConfigurationTypeDef = TypedDict(
    "ClientCreateAccessPointPublicAccessBlockConfigurationTypeDef",
    {
        "BlockPublicAcls": bool,
        "IgnorePublicAcls": bool,
        "BlockPublicPolicy": bool,
        "RestrictPublicBuckets": bool,
    },
    total=False,
)

ClientCreateAccessPointVpcConfigurationTypeDef = TypedDict(
    "ClientCreateAccessPointVpcConfigurationTypeDef", {"VpcId": str}
)

ClientCreateJobManifestLocationTypeDef = TypedDict(
    "ClientCreateJobManifestLocationTypeDef",
    {"ObjectArn": str, "ObjectVersionId": str, "ETag": str},
    total=False,
)

_RequiredClientCreateJobManifestSpecTypeDef = TypedDict(
    "_RequiredClientCreateJobManifestSpecTypeDef",
    {"Format": Literal["S3BatchOperations_CSV_20180820", "S3InventoryReport_CSV_20161130"]},
)
_OptionalClientCreateJobManifestSpecTypeDef = TypedDict(
    "_OptionalClientCreateJobManifestSpecTypeDef",
    {"Fields": List[Literal["Ignore", "Bucket", "Key", "VersionId"]]},
    total=False,
)


class ClientCreateJobManifestSpecTypeDef(
    _RequiredClientCreateJobManifestSpecTypeDef, _OptionalClientCreateJobManifestSpecTypeDef
):
    pass


_RequiredClientCreateJobManifestTypeDef = TypedDict(
    "_RequiredClientCreateJobManifestTypeDef", {"Spec": ClientCreateJobManifestSpecTypeDef}
)
_OptionalClientCreateJobManifestTypeDef = TypedDict(
    "_OptionalClientCreateJobManifestTypeDef",
    {"Location": ClientCreateJobManifestLocationTypeDef},
    total=False,
)


class ClientCreateJobManifestTypeDef(
    _RequiredClientCreateJobManifestTypeDef, _OptionalClientCreateJobManifestTypeDef
):
    pass


ClientCreateJobOperationLambdaInvokeTypeDef = TypedDict(
    "ClientCreateJobOperationLambdaInvokeTypeDef", {"FunctionArn": str}, total=False
)

ClientCreateJobOperationS3InitiateRestoreObjectTypeDef = TypedDict(
    "ClientCreateJobOperationS3InitiateRestoreObjectTypeDef",
    {"ExpirationInDays": int, "GlacierJobTier": Literal["BULK", "STANDARD"]},
    total=False,
)

ClientCreateJobOperationS3PutObjectAclAccessControlPolicyAccessControlListGrantsGranteeTypeDef = TypedDict(
    "ClientCreateJobOperationS3PutObjectAclAccessControlPolicyAccessControlListGrantsGranteeTypeDef",
    {"TypeIdentifier": Literal["id", "emailAddress", "uri"], "Identifier": str, "DisplayName": str},
    total=False,
)

ClientCreateJobOperationS3PutObjectAclAccessControlPolicyAccessControlListGrantsTypeDef = TypedDict(
    "ClientCreateJobOperationS3PutObjectAclAccessControlPolicyAccessControlListGrantsTypeDef",
    {
        "Grantee": ClientCreateJobOperationS3PutObjectAclAccessControlPolicyAccessControlListGrantsGranteeTypeDef,
        "Permission": Literal["FULL_CONTROL", "READ", "WRITE", "READ_ACP", "WRITE_ACP"],
    },
    total=False,
)

ClientCreateJobOperationS3PutObjectAclAccessControlPolicyAccessControlListOwnerTypeDef = TypedDict(
    "ClientCreateJobOperationS3PutObjectAclAccessControlPolicyAccessControlListOwnerTypeDef",
    {"ID": str, "DisplayName": str},
    total=False,
)

ClientCreateJobOperationS3PutObjectAclAccessControlPolicyAccessControlListTypeDef = TypedDict(
    "ClientCreateJobOperationS3PutObjectAclAccessControlPolicyAccessControlListTypeDef",
    {
        "Owner": ClientCreateJobOperationS3PutObjectAclAccessControlPolicyAccessControlListOwnerTypeDef,
        "Grants": List[
            ClientCreateJobOperationS3PutObjectAclAccessControlPolicyAccessControlListGrantsTypeDef
        ],
    },
    total=False,
)

ClientCreateJobOperationS3PutObjectAclAccessControlPolicyTypeDef = TypedDict(
    "ClientCreateJobOperationS3PutObjectAclAccessControlPolicyTypeDef",
    {
        "AccessControlList": ClientCreateJobOperationS3PutObjectAclAccessControlPolicyAccessControlListTypeDef,
        "CannedAccessControlList": Literal[
            "private",
            "public-read",
            "public-read-write",
            "aws-exec-read",
            "authenticated-read",
            "bucket-owner-read",
            "bucket-owner-full-control",
        ],
    },
    total=False,
)

ClientCreateJobOperationS3PutObjectAclTypeDef = TypedDict(
    "ClientCreateJobOperationS3PutObjectAclTypeDef",
    {"AccessControlPolicy": ClientCreateJobOperationS3PutObjectAclAccessControlPolicyTypeDef},
    total=False,
)

ClientCreateJobOperationS3PutObjectCopyAccessControlGrantsGranteeTypeDef = TypedDict(
    "ClientCreateJobOperationS3PutObjectCopyAccessControlGrantsGranteeTypeDef",
    {"TypeIdentifier": Literal["id", "emailAddress", "uri"], "Identifier": str, "DisplayName": str},
    total=False,
)

ClientCreateJobOperationS3PutObjectCopyAccessControlGrantsTypeDef = TypedDict(
    "ClientCreateJobOperationS3PutObjectCopyAccessControlGrantsTypeDef",
    {
        "Grantee": ClientCreateJobOperationS3PutObjectCopyAccessControlGrantsGranteeTypeDef,
        "Permission": Literal["FULL_CONTROL", "READ", "WRITE", "READ_ACP", "WRITE_ACP"],
    },
    total=False,
)

ClientCreateJobOperationS3PutObjectCopyNewObjectMetadataTypeDef = TypedDict(
    "ClientCreateJobOperationS3PutObjectCopyNewObjectMetadataTypeDef",
    {
        "CacheControl": str,
        "ContentDisposition": str,
        "ContentEncoding": str,
        "ContentLanguage": str,
        "UserMetadata": Dict[str, str],
        "ContentLength": int,
        "ContentMD5": str,
        "ContentType": str,
        "HttpExpiresDate": datetime,
        "RequesterCharged": bool,
        "SSEAlgorithm": Literal["AES256", "KMS"],
    },
    total=False,
)

ClientCreateJobOperationS3PutObjectCopyNewObjectTaggingTypeDef = TypedDict(
    "ClientCreateJobOperationS3PutObjectCopyNewObjectTaggingTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientCreateJobOperationS3PutObjectCopyTypeDef = TypedDict(
    "ClientCreateJobOperationS3PutObjectCopyTypeDef",
    {
        "TargetResource": str,
        "CannedAccessControlList": Literal[
            "private",
            "public-read",
            "public-read-write",
            "aws-exec-read",
            "authenticated-read",
            "bucket-owner-read",
            "bucket-owner-full-control",
        ],
        "AccessControlGrants": List[
            ClientCreateJobOperationS3PutObjectCopyAccessControlGrantsTypeDef
        ],
        "MetadataDirective": Literal["COPY", "REPLACE"],
        "ModifiedSinceConstraint": datetime,
        "NewObjectMetadata": ClientCreateJobOperationS3PutObjectCopyNewObjectMetadataTypeDef,
        "NewObjectTagging": List[ClientCreateJobOperationS3PutObjectCopyNewObjectTaggingTypeDef],
        "RedirectLocation": str,
        "RequesterPays": bool,
        "StorageClass": Literal[
            "STANDARD",
            "STANDARD_IA",
            "ONEZONE_IA",
            "GLACIER",
            "INTELLIGENT_TIERING",
            "DEEP_ARCHIVE",
        ],
        "UnModifiedSinceConstraint": datetime,
        "SSEAwsKmsKeyId": str,
        "TargetKeyPrefix": str,
        "ObjectLockLegalHoldStatus": Literal["OFF", "ON"],
        "ObjectLockMode": Literal["COMPLIANCE", "GOVERNANCE"],
        "ObjectLockRetainUntilDate": datetime,
    },
    total=False,
)

ClientCreateJobOperationS3PutObjectTaggingTagSetTypeDef = TypedDict(
    "ClientCreateJobOperationS3PutObjectTaggingTagSetTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientCreateJobOperationS3PutObjectTaggingTypeDef = TypedDict(
    "ClientCreateJobOperationS3PutObjectTaggingTypeDef",
    {"TagSet": List[ClientCreateJobOperationS3PutObjectTaggingTagSetTypeDef]},
    total=False,
)

ClientCreateJobOperationTypeDef = TypedDict(
    "ClientCreateJobOperationTypeDef",
    {
        "LambdaInvoke": ClientCreateJobOperationLambdaInvokeTypeDef,
        "S3PutObjectCopy": ClientCreateJobOperationS3PutObjectCopyTypeDef,
        "S3PutObjectAcl": ClientCreateJobOperationS3PutObjectAclTypeDef,
        "S3PutObjectTagging": ClientCreateJobOperationS3PutObjectTaggingTypeDef,
        "S3InitiateRestoreObject": ClientCreateJobOperationS3InitiateRestoreObjectTypeDef,
    },
    total=False,
)

ClientCreateJobReportTypeDef = TypedDict(
    "ClientCreateJobReportTypeDef",
    {
        "Bucket": str,
        "Format": str,
        "Enabled": bool,
        "Prefix": str,
        "ReportScope": Literal["AllTasks", "FailedTasksOnly"],
    },
    total=False,
)

ClientCreateJobResponseTypeDef = TypedDict(
    "ClientCreateJobResponseTypeDef", {"JobId": str}, total=False
)

ClientDescribeJobResponseJobFailureReasonsTypeDef = TypedDict(
    "ClientDescribeJobResponseJobFailureReasonsTypeDef",
    {"FailureCode": str, "FailureReason": str},
    total=False,
)

ClientDescribeJobResponseJobManifestLocationTypeDef = TypedDict(
    "ClientDescribeJobResponseJobManifestLocationTypeDef",
    {"ObjectArn": str, "ObjectVersionId": str, "ETag": str},
    total=False,
)

ClientDescribeJobResponseJobManifestSpecTypeDef = TypedDict(
    "ClientDescribeJobResponseJobManifestSpecTypeDef",
    {
        "Format": Literal["S3BatchOperations_CSV_20180820", "S3InventoryReport_CSV_20161130"],
        "Fields": List[Literal["Ignore", "Bucket", "Key", "VersionId"]],
    },
    total=False,
)

ClientDescribeJobResponseJobManifestTypeDef = TypedDict(
    "ClientDescribeJobResponseJobManifestTypeDef",
    {
        "Spec": ClientDescribeJobResponseJobManifestSpecTypeDef,
        "Location": ClientDescribeJobResponseJobManifestLocationTypeDef,
    },
    total=False,
)

ClientDescribeJobResponseJobOperationLambdaInvokeTypeDef = TypedDict(
    "ClientDescribeJobResponseJobOperationLambdaInvokeTypeDef", {"FunctionArn": str}, total=False
)

ClientDescribeJobResponseJobOperationS3InitiateRestoreObjectTypeDef = TypedDict(
    "ClientDescribeJobResponseJobOperationS3InitiateRestoreObjectTypeDef",
    {"ExpirationInDays": int, "GlacierJobTier": Literal["BULK", "STANDARD"]},
    total=False,
)

ClientDescribeJobResponseJobOperationS3PutObjectAclAccessControlPolicyAccessControlListGrantsGranteeTypeDef = TypedDict(
    "ClientDescribeJobResponseJobOperationS3PutObjectAclAccessControlPolicyAccessControlListGrantsGranteeTypeDef",
    {"TypeIdentifier": Literal["id", "emailAddress", "uri"], "Identifier": str, "DisplayName": str},
    total=False,
)

ClientDescribeJobResponseJobOperationS3PutObjectAclAccessControlPolicyAccessControlListGrantsTypeDef = TypedDict(
    "ClientDescribeJobResponseJobOperationS3PutObjectAclAccessControlPolicyAccessControlListGrantsTypeDef",
    {
        "Grantee": ClientDescribeJobResponseJobOperationS3PutObjectAclAccessControlPolicyAccessControlListGrantsGranteeTypeDef,
        "Permission": Literal["FULL_CONTROL", "READ", "WRITE", "READ_ACP", "WRITE_ACP"],
    },
    total=False,
)

ClientDescribeJobResponseJobOperationS3PutObjectAclAccessControlPolicyAccessControlListOwnerTypeDef = TypedDict(
    "ClientDescribeJobResponseJobOperationS3PutObjectAclAccessControlPolicyAccessControlListOwnerTypeDef",
    {"ID": str, "DisplayName": str},
    total=False,
)

ClientDescribeJobResponseJobOperationS3PutObjectAclAccessControlPolicyAccessControlListTypeDef = TypedDict(
    "ClientDescribeJobResponseJobOperationS3PutObjectAclAccessControlPolicyAccessControlListTypeDef",
    {
        "Owner": ClientDescribeJobResponseJobOperationS3PutObjectAclAccessControlPolicyAccessControlListOwnerTypeDef,
        "Grants": List[
            ClientDescribeJobResponseJobOperationS3PutObjectAclAccessControlPolicyAccessControlListGrantsTypeDef
        ],
    },
    total=False,
)

ClientDescribeJobResponseJobOperationS3PutObjectAclAccessControlPolicyTypeDef = TypedDict(
    "ClientDescribeJobResponseJobOperationS3PutObjectAclAccessControlPolicyTypeDef",
    {
        "AccessControlList": ClientDescribeJobResponseJobOperationS3PutObjectAclAccessControlPolicyAccessControlListTypeDef,
        "CannedAccessControlList": Literal[
            "private",
            "public-read",
            "public-read-write",
            "aws-exec-read",
            "authenticated-read",
            "bucket-owner-read",
            "bucket-owner-full-control",
        ],
    },
    total=False,
)

ClientDescribeJobResponseJobOperationS3PutObjectAclTypeDef = TypedDict(
    "ClientDescribeJobResponseJobOperationS3PutObjectAclTypeDef",
    {
        "AccessControlPolicy": ClientDescribeJobResponseJobOperationS3PutObjectAclAccessControlPolicyTypeDef
    },
    total=False,
)

ClientDescribeJobResponseJobOperationS3PutObjectCopyAccessControlGrantsGranteeTypeDef = TypedDict(
    "ClientDescribeJobResponseJobOperationS3PutObjectCopyAccessControlGrantsGranteeTypeDef",
    {"TypeIdentifier": Literal["id", "emailAddress", "uri"], "Identifier": str, "DisplayName": str},
    total=False,
)

ClientDescribeJobResponseJobOperationS3PutObjectCopyAccessControlGrantsTypeDef = TypedDict(
    "ClientDescribeJobResponseJobOperationS3PutObjectCopyAccessControlGrantsTypeDef",
    {
        "Grantee": ClientDescribeJobResponseJobOperationS3PutObjectCopyAccessControlGrantsGranteeTypeDef,
        "Permission": Literal["FULL_CONTROL", "READ", "WRITE", "READ_ACP", "WRITE_ACP"],
    },
    total=False,
)

ClientDescribeJobResponseJobOperationS3PutObjectCopyNewObjectMetadataTypeDef = TypedDict(
    "ClientDescribeJobResponseJobOperationS3PutObjectCopyNewObjectMetadataTypeDef",
    {
        "CacheControl": str,
        "ContentDisposition": str,
        "ContentEncoding": str,
        "ContentLanguage": str,
        "UserMetadata": Dict[str, str],
        "ContentLength": int,
        "ContentMD5": str,
        "ContentType": str,
        "HttpExpiresDate": datetime,
        "RequesterCharged": bool,
        "SSEAlgorithm": Literal["AES256", "KMS"],
    },
    total=False,
)

ClientDescribeJobResponseJobOperationS3PutObjectCopyNewObjectTaggingTypeDef = TypedDict(
    "ClientDescribeJobResponseJobOperationS3PutObjectCopyNewObjectTaggingTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientDescribeJobResponseJobOperationS3PutObjectCopyTypeDef = TypedDict(
    "ClientDescribeJobResponseJobOperationS3PutObjectCopyTypeDef",
    {
        "TargetResource": str,
        "CannedAccessControlList": Literal[
            "private",
            "public-read",
            "public-read-write",
            "aws-exec-read",
            "authenticated-read",
            "bucket-owner-read",
            "bucket-owner-full-control",
        ],
        "AccessControlGrants": List[
            ClientDescribeJobResponseJobOperationS3PutObjectCopyAccessControlGrantsTypeDef
        ],
        "MetadataDirective": Literal["COPY", "REPLACE"],
        "ModifiedSinceConstraint": datetime,
        "NewObjectMetadata": ClientDescribeJobResponseJobOperationS3PutObjectCopyNewObjectMetadataTypeDef,
        "NewObjectTagging": List[
            ClientDescribeJobResponseJobOperationS3PutObjectCopyNewObjectTaggingTypeDef
        ],
        "RedirectLocation": str,
        "RequesterPays": bool,
        "StorageClass": Literal[
            "STANDARD",
            "STANDARD_IA",
            "ONEZONE_IA",
            "GLACIER",
            "INTELLIGENT_TIERING",
            "DEEP_ARCHIVE",
        ],
        "UnModifiedSinceConstraint": datetime,
        "SSEAwsKmsKeyId": str,
        "TargetKeyPrefix": str,
        "ObjectLockLegalHoldStatus": Literal["OFF", "ON"],
        "ObjectLockMode": Literal["COMPLIANCE", "GOVERNANCE"],
        "ObjectLockRetainUntilDate": datetime,
    },
    total=False,
)

ClientDescribeJobResponseJobOperationS3PutObjectTaggingTagSetTypeDef = TypedDict(
    "ClientDescribeJobResponseJobOperationS3PutObjectTaggingTagSetTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientDescribeJobResponseJobOperationS3PutObjectTaggingTypeDef = TypedDict(
    "ClientDescribeJobResponseJobOperationS3PutObjectTaggingTypeDef",
    {"TagSet": List[ClientDescribeJobResponseJobOperationS3PutObjectTaggingTagSetTypeDef]},
    total=False,
)

ClientDescribeJobResponseJobOperationTypeDef = TypedDict(
    "ClientDescribeJobResponseJobOperationTypeDef",
    {
        "LambdaInvoke": ClientDescribeJobResponseJobOperationLambdaInvokeTypeDef,
        "S3PutObjectCopy": ClientDescribeJobResponseJobOperationS3PutObjectCopyTypeDef,
        "S3PutObjectAcl": ClientDescribeJobResponseJobOperationS3PutObjectAclTypeDef,
        "S3PutObjectTagging": ClientDescribeJobResponseJobOperationS3PutObjectTaggingTypeDef,
        "S3InitiateRestoreObject": ClientDescribeJobResponseJobOperationS3InitiateRestoreObjectTypeDef,
    },
    total=False,
)

ClientDescribeJobResponseJobProgressSummaryTypeDef = TypedDict(
    "ClientDescribeJobResponseJobProgressSummaryTypeDef",
    {"TotalNumberOfTasks": int, "NumberOfTasksSucceeded": int, "NumberOfTasksFailed": int},
    total=False,
)

ClientDescribeJobResponseJobReportTypeDef = TypedDict(
    "ClientDescribeJobResponseJobReportTypeDef",
    {
        "Bucket": str,
        "Format": str,
        "Enabled": bool,
        "Prefix": str,
        "ReportScope": Literal["AllTasks", "FailedTasksOnly"],
    },
    total=False,
)

ClientDescribeJobResponseJobTypeDef = TypedDict(
    "ClientDescribeJobResponseJobTypeDef",
    {
        "JobId": str,
        "ConfirmationRequired": bool,
        "Description": str,
        "JobArn": str,
        "Status": Literal[
            "Active",
            "Cancelled",
            "Cancelling",
            "Complete",
            "Completing",
            "Failed",
            "Failing",
            "New",
            "Paused",
            "Pausing",
            "Preparing",
            "Ready",
            "Suspended",
        ],
        "Manifest": ClientDescribeJobResponseJobManifestTypeDef,
        "Operation": ClientDescribeJobResponseJobOperationTypeDef,
        "Priority": int,
        "ProgressSummary": ClientDescribeJobResponseJobProgressSummaryTypeDef,
        "StatusUpdateReason": str,
        "FailureReasons": List[ClientDescribeJobResponseJobFailureReasonsTypeDef],
        "Report": ClientDescribeJobResponseJobReportTypeDef,
        "CreationTime": datetime,
        "TerminationDate": datetime,
        "RoleArn": str,
        "SuspendedDate": datetime,
        "SuspendedCause": str,
    },
    total=False,
)

ClientDescribeJobResponseTypeDef = TypedDict(
    "ClientDescribeJobResponseTypeDef", {"Job": ClientDescribeJobResponseJobTypeDef}, total=False
)

ClientGetAccessPointPolicyResponseTypeDef = TypedDict(
    "ClientGetAccessPointPolicyResponseTypeDef", {"Policy": str}, total=False
)

ClientGetAccessPointPolicyStatusResponsePolicyStatusTypeDef = TypedDict(
    "ClientGetAccessPointPolicyStatusResponsePolicyStatusTypeDef", {"IsPublic": bool}, total=False
)

ClientGetAccessPointPolicyStatusResponseTypeDef = TypedDict(
    "ClientGetAccessPointPolicyStatusResponseTypeDef",
    {"PolicyStatus": ClientGetAccessPointPolicyStatusResponsePolicyStatusTypeDef},
    total=False,
)

ClientGetAccessPointResponsePublicAccessBlockConfigurationTypeDef = TypedDict(
    "ClientGetAccessPointResponsePublicAccessBlockConfigurationTypeDef",
    {
        "BlockPublicAcls": bool,
        "IgnorePublicAcls": bool,
        "BlockPublicPolicy": bool,
        "RestrictPublicBuckets": bool,
    },
    total=False,
)

ClientGetAccessPointResponseVpcConfigurationTypeDef = TypedDict(
    "ClientGetAccessPointResponseVpcConfigurationTypeDef", {"VpcId": str}, total=False
)

ClientGetAccessPointResponseTypeDef = TypedDict(
    "ClientGetAccessPointResponseTypeDef",
    {
        "Name": str,
        "Bucket": str,
        "NetworkOrigin": Literal["Internet", "VPC"],
        "VpcConfiguration": ClientGetAccessPointResponseVpcConfigurationTypeDef,
        "PublicAccessBlockConfiguration": ClientGetAccessPointResponsePublicAccessBlockConfigurationTypeDef,
        "CreationDate": datetime,
    },
    total=False,
)

ClientGetPublicAccessBlockResponsePublicAccessBlockConfigurationTypeDef = TypedDict(
    "ClientGetPublicAccessBlockResponsePublicAccessBlockConfigurationTypeDef",
    {
        "BlockPublicAcls": bool,
        "IgnorePublicAcls": bool,
        "BlockPublicPolicy": bool,
        "RestrictPublicBuckets": bool,
    },
    total=False,
)

ClientGetPublicAccessBlockResponseTypeDef = TypedDict(
    "ClientGetPublicAccessBlockResponseTypeDef",
    {
        "PublicAccessBlockConfiguration": ClientGetPublicAccessBlockResponsePublicAccessBlockConfigurationTypeDef
    },
    total=False,
)

ClientListAccessPointsResponseAccessPointListVpcConfigurationTypeDef = TypedDict(
    "ClientListAccessPointsResponseAccessPointListVpcConfigurationTypeDef",
    {"VpcId": str},
    total=False,
)

ClientListAccessPointsResponseAccessPointListTypeDef = TypedDict(
    "ClientListAccessPointsResponseAccessPointListTypeDef",
    {
        "Name": str,
        "NetworkOrigin": Literal["Internet", "VPC"],
        "VpcConfiguration": ClientListAccessPointsResponseAccessPointListVpcConfigurationTypeDef,
        "Bucket": str,
    },
    total=False,
)

ClientListAccessPointsResponseTypeDef = TypedDict(
    "ClientListAccessPointsResponseTypeDef",
    {
        "AccessPointList": List[ClientListAccessPointsResponseAccessPointListTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientListJobsResponseJobsProgressSummaryTypeDef = TypedDict(
    "ClientListJobsResponseJobsProgressSummaryTypeDef",
    {"TotalNumberOfTasks": int, "NumberOfTasksSucceeded": int, "NumberOfTasksFailed": int},
    total=False,
)

ClientListJobsResponseJobsTypeDef = TypedDict(
    "ClientListJobsResponseJobsTypeDef",
    {
        "JobId": str,
        "Description": str,
        "Operation": Literal[
            "LambdaInvoke",
            "S3PutObjectCopy",
            "S3PutObjectAcl",
            "S3PutObjectTagging",
            "S3InitiateRestoreObject",
        ],
        "Priority": int,
        "Status": Literal[
            "Active",
            "Cancelled",
            "Cancelling",
            "Complete",
            "Completing",
            "Failed",
            "Failing",
            "New",
            "Paused",
            "Pausing",
            "Preparing",
            "Ready",
            "Suspended",
        ],
        "CreationTime": datetime,
        "TerminationDate": datetime,
        "ProgressSummary": ClientListJobsResponseJobsProgressSummaryTypeDef,
    },
    total=False,
)

ClientListJobsResponseTypeDef = TypedDict(
    "ClientListJobsResponseTypeDef",
    {"NextToken": str, "Jobs": List[ClientListJobsResponseJobsTypeDef]},
    total=False,
)

ClientPutPublicAccessBlockPublicAccessBlockConfigurationTypeDef = TypedDict(
    "ClientPutPublicAccessBlockPublicAccessBlockConfigurationTypeDef",
    {
        "BlockPublicAcls": bool,
        "IgnorePublicAcls": bool,
        "BlockPublicPolicy": bool,
        "RestrictPublicBuckets": bool,
    },
    total=False,
)

ClientUpdateJobPriorityResponseTypeDef = TypedDict(
    "ClientUpdateJobPriorityResponseTypeDef", {"JobId": str, "Priority": int}, total=False
)

ClientUpdateJobStatusResponseTypeDef = TypedDict(
    "ClientUpdateJobStatusResponseTypeDef",
    {
        "JobId": str,
        "Status": Literal[
            "Active",
            "Cancelled",
            "Cancelling",
            "Complete",
            "Completing",
            "Failed",
            "Failing",
            "New",
            "Paused",
            "Pausing",
            "Preparing",
            "Ready",
            "Suspended",
        ],
        "StatusUpdateReason": str,
    },
    total=False,
)
