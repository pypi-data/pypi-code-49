"""
Main interface for s3 service ServiceResource

Usage::

    import boto3
    from mypy_boto3.s3 import S3ServiceResource
    import mypy_boto3.s3.service_resource as s3_resources

    resource: S3ServiceResource = boto3.resource("s3")
    session_resource: S3ServiceResource = session.resource("s3")

    Bucket: s3_resources.Bucket = resource.Bucket(...)
    ...
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from datetime import datetime
import sys
from typing import Any, Callable, Dict, IO, List, TYPE_CHECKING, Union
from boto3.resources.base import ServiceResource as Boto3ServiceResource
from boto3.resources.collection import ResourceCollection
from boto3.s3.transfer import TransferConfig
from botocore.client import BaseClient

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_s3.service_resource as service_resource_scope
else:
    service_resource_scope = object
from mypy_boto3_s3.type_defs import (
    AbortMultipartUploadOutputTypeDef,
    AccessControlPolicyTypeDef,
    BucketLifecycleConfigurationTypeDef,
    BucketLoggingStatusTypeDef,
    CORSConfigurationTypeDef,
    CompleteMultipartUploadOutputTypeDef,
    CompletedMultipartUploadTypeDef,
    CopyObjectOutputTypeDef,
    CopySourceTypeDef,
    CreateBucketConfigurationTypeDef,
    CreateBucketOutputTypeDef,
    CreateMultipartUploadOutputTypeDef,
    DeleteObjectOutputTypeDef,
    DeleteObjectsOutputTypeDef,
    DeleteTypeDef,
    GetObjectOutputTypeDef,
    HeadObjectOutputTypeDef,
    LifecycleConfigurationTypeDef,
    NotificationConfigurationTypeDef,
    PutObjectAclOutputTypeDef,
    PutObjectOutputTypeDef,
    RequestPaymentConfigurationTypeDef,
    RestoreObjectOutputTypeDef,
    RestoreRequestTypeDef,
    TaggingTypeDef,
    UploadPartCopyOutputTypeDef,
    UploadPartOutputTypeDef,
    VersioningConfigurationTypeDef,
    WebsiteConfigurationTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "S3ServiceResource",
    "Bucket",
    "BucketAcl",
    "BucketCors",
    "BucketLifecycle",
    "BucketLifecycleConfiguration",
    "BucketLogging",
    "BucketNotification",
    "BucketPolicy",
    "BucketRequestPayment",
    "BucketTagging",
    "BucketVersioning",
    "BucketWebsite",
    "MultipartUpload",
    "MultipartUploadPart",
    "Object",
    "ObjectAcl",
    "ObjectSummary",
    "ObjectVersion",
    "ServiceResourceBucketsCollection",
    "BucketMultipartUploadsCollection",
    "BucketObjectVersionsCollection",
    "BucketObjectsCollection",
    "MultipartUploadPartsCollection",
)


class S3ServiceResource(Boto3ServiceResource):
    """
    [S3.ServiceResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.ServiceResource)
    """

    buckets: "service_resource_scope.ServiceResourceBucketsCollection"

    def Bucket(self, name: str) -> "service_resource_scope.Bucket":
        """
        [ServiceResource.Bucket documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.ServiceResource.Bucket)
        """

    def BucketAcl(self, bucket_name: str) -> "service_resource_scope.BucketAcl":
        """
        [ServiceResource.BucketAcl documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.ServiceResource.BucketAcl)
        """

    def BucketCors(self, bucket_name: str) -> "service_resource_scope.BucketCors":
        """
        [ServiceResource.BucketCors documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.ServiceResource.BucketCors)
        """

    def BucketLifecycle(self, bucket_name: str) -> "service_resource_scope.BucketLifecycle":
        """
        [ServiceResource.BucketLifecycle documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.ServiceResource.BucketLifecycle)
        """

    def BucketLifecycleConfiguration(
        self, bucket_name: str
    ) -> "service_resource_scope.BucketLifecycleConfiguration":
        """
        [ServiceResource.BucketLifecycleConfiguration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.ServiceResource.BucketLifecycleConfiguration)
        """

    def BucketLogging(self, bucket_name: str) -> "service_resource_scope.BucketLogging":
        """
        [ServiceResource.BucketLogging documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.ServiceResource.BucketLogging)
        """

    def BucketNotification(self, bucket_name: str) -> "service_resource_scope.BucketNotification":
        """
        [ServiceResource.BucketNotification documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.ServiceResource.BucketNotification)
        """

    def BucketPolicy(self, bucket_name: str) -> "service_resource_scope.BucketPolicy":
        """
        [ServiceResource.BucketPolicy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.ServiceResource.BucketPolicy)
        """

    def BucketRequestPayment(
        self, bucket_name: str
    ) -> "service_resource_scope.BucketRequestPayment":
        """
        [ServiceResource.BucketRequestPayment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.ServiceResource.BucketRequestPayment)
        """

    def BucketTagging(self, bucket_name: str) -> "service_resource_scope.BucketTagging":
        """
        [ServiceResource.BucketTagging documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.ServiceResource.BucketTagging)
        """

    def BucketVersioning(self, bucket_name: str) -> "service_resource_scope.BucketVersioning":
        """
        [ServiceResource.BucketVersioning documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.ServiceResource.BucketVersioning)
        """

    def BucketWebsite(self, bucket_name: str) -> "service_resource_scope.BucketWebsite":
        """
        [ServiceResource.BucketWebsite documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.ServiceResource.BucketWebsite)
        """

    def MultipartUpload(
        self, bucket_name: str, object_key: str, id: str
    ) -> "service_resource_scope.MultipartUpload":
        """
        [ServiceResource.MultipartUpload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.ServiceResource.MultipartUpload)
        """

    def MultipartUploadPart(
        self, bucket_name: str, object_key: str, multipart_upload_id: str, part_number: str
    ) -> "service_resource_scope.MultipartUploadPart":
        """
        [ServiceResource.MultipartUploadPart documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.ServiceResource.MultipartUploadPart)
        """

    def Object(self, bucket_name: str, key: str) -> "service_resource_scope.Object":
        """
        [ServiceResource.Object documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.ServiceResource.Object)
        """

    def ObjectAcl(self, bucket_name: str, object_key: str) -> "service_resource_scope.ObjectAcl":
        """
        [ServiceResource.ObjectAcl documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.ServiceResource.ObjectAcl)
        """

    def ObjectSummary(self, bucket_name: str, key: str) -> "service_resource_scope.ObjectSummary":
        """
        [ServiceResource.ObjectSummary documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.ServiceResource.ObjectSummary)
        """

    def ObjectVersion(
        self, bucket_name: str, object_key: str, id: str
    ) -> "service_resource_scope.ObjectVersion":
        """
        [ServiceResource.ObjectVersion documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.ServiceResource.ObjectVersion)
        """

    def create_bucket(
        self,
        Bucket: str,
        ACL: Literal["private", "public-read", "public-read-write", "authenticated-read"] = None,
        CreateBucketConfiguration: CreateBucketConfigurationTypeDef = None,
        GrantFullControl: str = None,
        GrantRead: str = None,
        GrantReadACP: str = None,
        GrantWrite: str = None,
        GrantWriteACP: str = None,
        ObjectLockEnabledForBucket: bool = None,
    ) -> CreateBucketOutputTypeDef:
        """
        [ServiceResource.create_bucket documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.ServiceResource.create_bucket)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [ServiceResource.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.ServiceResource.get_available_subresources)
        """


class Bucket(Boto3ServiceResource):
    """
    [Bucket documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.ServiceResource.Bucket)
    """

    creation_date: datetime
    name: str
    multipart_uploads: "service_resource_scope.BucketMultipartUploadsCollection"
    object_versions: "service_resource_scope.BucketObjectVersionsCollection"
    objects: "service_resource_scope.BucketObjectsCollection"

    def copy(
        self,
        CopySource: CopySourceTypeDef,
        Key: str,
        ExtraArgs: Dict[str, Any] = None,
        Callback: Callable[..., Any] = None,
        SourceClient: BaseClient = None,
        Config: TransferConfig = None,
    ) -> None:
        """
        [Bucket.copy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.Bucket.copy)
        """

    def create(
        self,
        ACL: Literal["private", "public-read", "public-read-write", "authenticated-read"] = None,
        CreateBucketConfiguration: CreateBucketConfigurationTypeDef = None,
        GrantFullControl: str = None,
        GrantRead: str = None,
        GrantReadACP: str = None,
        GrantWrite: str = None,
        GrantWriteACP: str = None,
        ObjectLockEnabledForBucket: bool = None,
    ) -> CreateBucketOutputTypeDef:
        """
        [Bucket.create documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.Bucket.create)
        """

    def delete(self) -> None:
        """
        [Bucket.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.Bucket.delete)
        """

    def delete_objects(
        self,
        Delete: DeleteTypeDef,
        MFA: str = None,
        RequestPayer: Literal["requester"] = None,
        BypassGovernanceRetention: bool = None,
    ) -> DeleteObjectsOutputTypeDef:
        """
        [Bucket.delete_objects documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.Bucket.delete_objects)
        """

    def download_file(
        self,
        Key: str,
        Filename: str,
        ExtraArgs: Dict[str, Any] = None,
        Callback: Callable[..., Any] = None,
        Config: TransferConfig = None,
    ) -> None:
        """
        [Bucket.download_file documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.Bucket.download_file)
        """

    def download_fileobj(
        self,
        Key: str,
        Fileobj: IO[Any],
        ExtraArgs: Dict[str, Any] = None,
        Callback: Callable[..., Any] = None,
        Config: TransferConfig = None,
    ) -> None:
        """
        [Bucket.download_fileobj documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.Bucket.download_fileobj)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Bucket.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.Bucket.get_available_subresources)
        """

    def load(self) -> None:
        """
        [Bucket.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.Bucket.load)
        """

    def put_object(
        self,
        Key: str,
        ACL: Literal[
            "private",
            "public-read",
            "public-read-write",
            "authenticated-read",
            "aws-exec-read",
            "bucket-owner-read",
            "bucket-owner-full-control",
        ] = None,
        Body: Union[bytes, IO] = None,
        CacheControl: str = None,
        ContentDisposition: str = None,
        ContentEncoding: str = None,
        ContentLanguage: str = None,
        ContentLength: int = None,
        ContentMD5: str = None,
        ContentType: str = None,
        Expires: datetime = None,
        GrantFullControl: str = None,
        GrantRead: str = None,
        GrantReadACP: str = None,
        GrantWriteACP: str = None,
        Metadata: Dict[str, str] = None,
        ServerSideEncryption: Literal["AES256", "aws:kms"] = None,
        StorageClass: Literal[
            "STANDARD",
            "REDUCED_REDUNDANCY",
            "STANDARD_IA",
            "ONEZONE_IA",
            "INTELLIGENT_TIERING",
            "GLACIER",
            "DEEP_ARCHIVE",
        ] = None,
        WebsiteRedirectLocation: str = None,
        SSECustomerAlgorithm: str = None,
        SSECustomerKey: str = None,
        SSECustomerKeyMD5: str = None,
        SSEKMSKeyId: str = None,
        SSEKMSEncryptionContext: str = None,
        RequestPayer: Literal["requester"] = None,
        Tagging: str = None,
        ObjectLockMode: Literal["GOVERNANCE", "COMPLIANCE"] = None,
        ObjectLockRetainUntilDate: datetime = None,
        ObjectLockLegalHoldStatus: Literal["ON", "OFF"] = None,
    ) -> PutObjectOutputTypeDef:
        """
        [Bucket.put_object documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.Bucket.put_object)
        """

    def upload_file(
        self,
        Filename: str,
        Key: str,
        ExtraArgs: Dict[str, Any] = None,
        Callback: Callable[..., Any] = None,
        Config: TransferConfig = None,
    ) -> None:
        """
        [Bucket.upload_file documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.Bucket.upload_file)
        """

    def upload_fileobj(
        self,
        Fileobj: IO[Any],
        Key: str,
        ExtraArgs: Dict[str, Any] = None,
        Callback: Callable[..., Any] = None,
        Config: TransferConfig = None,
    ) -> None:
        """
        [Bucket.upload_fileobj documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.Bucket.upload_fileobj)
        """

    def wait_until_exists(self) -> None:
        """
        [Bucket.wait_until_exists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.Bucket.wait_until_exists)
        """

    def wait_until_not_exists(self) -> None:
        """
        [Bucket.wait_until_not_exists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.Bucket.wait_until_not_exists)
        """


class BucketAcl(Boto3ServiceResource):
    """
    [BucketAcl documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.ServiceResource.BucketAcl)
    """

    owner: Dict[str, Any]
    grants: List[Any]
    bucket_name: str

    def get_available_subresources(self) -> List[str]:
        """
        [BucketAcl.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.BucketAcl.get_available_subresources)
        """

    def load(self) -> None:
        """
        [BucketAcl.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.BucketAcl.load)
        """

    def put(
        self,
        ACL: Literal["private", "public-read", "public-read-write", "authenticated-read"] = None,
        AccessControlPolicy: AccessControlPolicyTypeDef = None,
        GrantFullControl: str = None,
        GrantRead: str = None,
        GrantReadACP: str = None,
        GrantWrite: str = None,
        GrantWriteACP: str = None,
    ) -> None:
        """
        [BucketAcl.put documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.BucketAcl.put)
        """

    def reload(self) -> None:
        """
        [BucketAcl.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.BucketAcl.reload)
        """


class BucketCors(Boto3ServiceResource):
    """
    [BucketCors documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.ServiceResource.BucketCors)
    """

    cors_rules: List[Any]
    bucket_name: str

    def delete(self) -> None:
        """
        [BucketCors.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.BucketCors.delete)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [BucketCors.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.BucketCors.get_available_subresources)
        """

    def load(self) -> None:
        """
        [BucketCors.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.BucketCors.load)
        """

    def put(self, CORSConfiguration: CORSConfigurationTypeDef) -> None:
        """
        [BucketCors.put documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.BucketCors.put)
        """

    def reload(self) -> None:
        """
        [BucketCors.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.BucketCors.reload)
        """


class BucketLifecycle(Boto3ServiceResource):
    """
    [BucketLifecycle documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.ServiceResource.BucketLifecycle)
    """

    rules: List[Any]
    bucket_name: str

    def delete(self) -> None:
        """
        [BucketLifecycle.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.BucketLifecycle.delete)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [BucketLifecycle.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.BucketLifecycle.get_available_subresources)
        """

    def load(self) -> None:
        """
        [BucketLifecycle.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.BucketLifecycle.load)
        """

    def put(self, LifecycleConfiguration: LifecycleConfigurationTypeDef = None) -> None:
        """
        [BucketLifecycle.put documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.BucketLifecycle.put)
        """

    def reload(self) -> None:
        """
        [BucketLifecycle.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.BucketLifecycle.reload)
        """


class BucketLifecycleConfiguration(Boto3ServiceResource):
    """
    [BucketLifecycleConfiguration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.ServiceResource.BucketLifecycleConfiguration)
    """

    rules: List[Any]
    bucket_name: str

    def delete(self) -> None:
        """
        [BucketLifecycleConfiguration.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.BucketLifecycleConfiguration.delete)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [BucketLifecycleConfiguration.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.BucketLifecycleConfiguration.get_available_subresources)
        """

    def load(self) -> None:
        """
        [BucketLifecycleConfiguration.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.BucketLifecycleConfiguration.load)
        """

    def put(self, LifecycleConfiguration: BucketLifecycleConfigurationTypeDef = None) -> None:
        """
        [BucketLifecycleConfiguration.put documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.BucketLifecycleConfiguration.put)
        """

    def reload(self) -> None:
        """
        [BucketLifecycleConfiguration.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.BucketLifecycleConfiguration.reload)
        """


class BucketLogging(Boto3ServiceResource):
    """
    [BucketLogging documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.ServiceResource.BucketLogging)
    """

    logging_enabled: Dict[str, Any]
    bucket_name: str

    def get_available_subresources(self) -> List[str]:
        """
        [BucketLogging.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.BucketLogging.get_available_subresources)
        """

    def load(self) -> None:
        """
        [BucketLogging.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.BucketLogging.load)
        """

    def put(self, BucketLoggingStatus: BucketLoggingStatusTypeDef) -> None:
        """
        [BucketLogging.put documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.BucketLogging.put)
        """

    def reload(self) -> None:
        """
        [BucketLogging.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.BucketLogging.reload)
        """


class BucketNotification(Boto3ServiceResource):
    """
    [BucketNotification documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.ServiceResource.BucketNotification)
    """

    topic_configurations: List[Any]
    queue_configurations: List[Any]
    lambda_function_configurations: List[Any]
    bucket_name: str

    def get_available_subresources(self) -> List[str]:
        """
        [BucketNotification.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.BucketNotification.get_available_subresources)
        """

    def load(self) -> None:
        """
        [BucketNotification.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.BucketNotification.load)
        """

    def put(self, NotificationConfiguration: NotificationConfigurationTypeDef) -> None:
        """
        [BucketNotification.put documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.BucketNotification.put)
        """

    def reload(self) -> None:
        """
        [BucketNotification.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.BucketNotification.reload)
        """


class BucketPolicy(Boto3ServiceResource):
    """
    [BucketPolicy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.ServiceResource.BucketPolicy)
    """

    policy: str
    bucket_name: str

    def delete(self) -> None:
        """
        [BucketPolicy.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.BucketPolicy.delete)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [BucketPolicy.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.BucketPolicy.get_available_subresources)
        """

    def load(self) -> None:
        """
        [BucketPolicy.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.BucketPolicy.load)
        """

    def put(self, Policy: str, ConfirmRemoveSelfBucketAccess: bool = None) -> None:
        """
        [BucketPolicy.put documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.BucketPolicy.put)
        """

    def reload(self) -> None:
        """
        [BucketPolicy.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.BucketPolicy.reload)
        """


class BucketRequestPayment(Boto3ServiceResource):
    """
    [BucketRequestPayment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.ServiceResource.BucketRequestPayment)
    """

    payer: str
    bucket_name: str

    def get_available_subresources(self) -> List[str]:
        """
        [BucketRequestPayment.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.BucketRequestPayment.get_available_subresources)
        """

    def load(self) -> None:
        """
        [BucketRequestPayment.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.BucketRequestPayment.load)
        """

    def put(self, RequestPaymentConfiguration: RequestPaymentConfigurationTypeDef) -> None:
        """
        [BucketRequestPayment.put documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.BucketRequestPayment.put)
        """

    def reload(self) -> None:
        """
        [BucketRequestPayment.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.BucketRequestPayment.reload)
        """


class BucketTagging(Boto3ServiceResource):
    """
    [BucketTagging documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.ServiceResource.BucketTagging)
    """

    tag_set: List[Any]
    bucket_name: str

    def delete(self) -> None:
        """
        [BucketTagging.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.BucketTagging.delete)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [BucketTagging.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.BucketTagging.get_available_subresources)
        """

    def load(self) -> None:
        """
        [BucketTagging.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.BucketTagging.load)
        """

    def put(self, Tagging: TaggingTypeDef) -> None:
        """
        [BucketTagging.put documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.BucketTagging.put)
        """

    def reload(self) -> None:
        """
        [BucketTagging.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.BucketTagging.reload)
        """


class BucketVersioning(Boto3ServiceResource):
    """
    [BucketVersioning documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.ServiceResource.BucketVersioning)
    """

    status: str
    mfa_delete: str
    bucket_name: str

    def enable(
        self, VersioningConfiguration: VersioningConfigurationTypeDef, MFA: str = None
    ) -> None:
        """
        [BucketVersioning.enable documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.BucketVersioning.enable)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [BucketVersioning.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.BucketVersioning.get_available_subresources)
        """

    def load(self) -> None:
        """
        [BucketVersioning.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.BucketVersioning.load)
        """

    def put(self, VersioningConfiguration: VersioningConfigurationTypeDef, MFA: str = None) -> None:
        """
        [BucketVersioning.put documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.BucketVersioning.put)
        """

    def reload(self) -> None:
        """
        [BucketVersioning.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.BucketVersioning.reload)
        """

    def suspend(
        self, VersioningConfiguration: VersioningConfigurationTypeDef, MFA: str = None
    ) -> None:
        """
        [BucketVersioning.suspend documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.BucketVersioning.suspend)
        """


class BucketWebsite(Boto3ServiceResource):
    """
    [BucketWebsite documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.ServiceResource.BucketWebsite)
    """

    redirect_all_requests_to: Dict[str, Any]
    index_document: Dict[str, Any]
    error_document: Dict[str, Any]
    routing_rules: List[Any]
    bucket_name: str

    def delete(self) -> None:
        """
        [BucketWebsite.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.BucketWebsite.delete)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [BucketWebsite.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.BucketWebsite.get_available_subresources)
        """

    def load(self) -> None:
        """
        [BucketWebsite.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.BucketWebsite.load)
        """

    def put(self, WebsiteConfiguration: WebsiteConfigurationTypeDef) -> None:
        """
        [BucketWebsite.put documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.BucketWebsite.put)
        """

    def reload(self) -> None:
        """
        [BucketWebsite.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.BucketWebsite.reload)
        """


class MultipartUpload(Boto3ServiceResource):
    """
    [MultipartUpload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.ServiceResource.MultipartUpload)
    """

    upload_id: str
    key: str
    initiated: datetime
    storage_class: str
    owner: Dict[str, Any]
    initiator: Dict[str, Any]
    bucket_name: str
    object_key: str
    id: str
    parts: "service_resource_scope.MultipartUploadPartsCollection"

    def abort(self, RequestPayer: Literal["requester"] = None) -> AbortMultipartUploadOutputTypeDef:
        """
        [MultipartUpload.abort documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.MultipartUpload.abort)
        """

    def complete(
        self,
        MultipartUpload: CompletedMultipartUploadTypeDef = None,
        RequestPayer: Literal["requester"] = None,
    ) -> CompleteMultipartUploadOutputTypeDef:
        """
        [MultipartUpload.complete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.MultipartUpload.complete)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [MultipartUpload.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.MultipartUpload.get_available_subresources)
        """


class MultipartUploadPart(Boto3ServiceResource):
    """
    [MultipartUploadPart documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.ServiceResource.MultipartUploadPart)
    """

    last_modified: datetime
    e_tag: str
    size: int
    bucket_name: str
    object_key: str
    multipart_upload_id: str
    part_number: str

    def copy_from(
        self,
        CopySource: str,
        CopySourceIfMatch: str = None,
        CopySourceIfModifiedSince: datetime = None,
        CopySourceIfNoneMatch: str = None,
        CopySourceIfUnmodifiedSince: datetime = None,
        CopySourceRange: str = None,
        SSECustomerAlgorithm: str = None,
        SSECustomerKey: str = None,
        SSECustomerKeyMD5: str = None,
        CopySourceSSECustomerAlgorithm: str = None,
        CopySourceSSECustomerKey: str = None,
        CopySourceSSECustomerKeyMD5: str = None,
        RequestPayer: Literal["requester"] = None,
    ) -> UploadPartCopyOutputTypeDef:
        """
        [MultipartUploadPart.copy_from documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.MultipartUploadPart.copy_from)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [MultipartUploadPart.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.MultipartUploadPart.get_available_subresources)
        """

    def upload(
        self,
        Body: Union[bytes, IO] = None,
        ContentLength: int = None,
        ContentMD5: str = None,
        SSECustomerAlgorithm: str = None,
        SSECustomerKey: str = None,
        SSECustomerKeyMD5: str = None,
        RequestPayer: Literal["requester"] = None,
    ) -> UploadPartOutputTypeDef:
        """
        [MultipartUploadPart.upload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.MultipartUploadPart.upload)
        """


class Object(Boto3ServiceResource):
    """
    [Object documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.ServiceResource.Object)
    """

    delete_marker: bool
    accept_ranges: str
    expiration: str
    restore: str
    last_modified: datetime
    content_length: int
    e_tag: str
    missing_meta: int
    version_id: str
    cache_control: str
    content_disposition: str
    content_encoding: str
    content_language: str
    content_type: str
    expires: datetime
    website_redirect_location: str
    server_side_encryption: str
    metadata: Dict[str, Any]
    sse_customer_algorithm: str
    sse_customer_key_md5: str
    ssekms_key_id: str
    storage_class: str
    request_charged: str
    replication_status: str
    parts_count: int
    object_lock_mode: str
    object_lock_retain_until_date: datetime
    object_lock_legal_hold_status: str
    bucket_name: str
    key: str

    def copy(
        self,
        CopySource: CopySourceTypeDef,
        ExtraArgs: Dict[str, Any] = None,
        Callback: Callable[..., Any] = None,
        SourceClient: BaseClient = None,
        Config: TransferConfig = None,
    ) -> None:
        """
        [Object.copy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.Object.copy)
        """

    def copy_from(
        self,
        CopySource: str,
        ACL: Literal[
            "private",
            "public-read",
            "public-read-write",
            "authenticated-read",
            "aws-exec-read",
            "bucket-owner-read",
            "bucket-owner-full-control",
        ] = None,
        CacheControl: str = None,
        ContentDisposition: str = None,
        ContentEncoding: str = None,
        ContentLanguage: str = None,
        ContentType: str = None,
        CopySourceIfMatch: str = None,
        CopySourceIfModifiedSince: datetime = None,
        CopySourceIfNoneMatch: str = None,
        CopySourceIfUnmodifiedSince: datetime = None,
        Expires: datetime = None,
        GrantFullControl: str = None,
        GrantRead: str = None,
        GrantReadACP: str = None,
        GrantWriteACP: str = None,
        Metadata: Dict[str, str] = None,
        MetadataDirective: Literal["COPY", "REPLACE"] = None,
        TaggingDirective: Literal["COPY", "REPLACE"] = None,
        ServerSideEncryption: Literal["AES256", "aws:kms"] = None,
        StorageClass: Literal[
            "STANDARD",
            "REDUCED_REDUNDANCY",
            "STANDARD_IA",
            "ONEZONE_IA",
            "INTELLIGENT_TIERING",
            "GLACIER",
            "DEEP_ARCHIVE",
        ] = None,
        WebsiteRedirectLocation: str = None,
        SSECustomerAlgorithm: str = None,
        SSECustomerKey: str = None,
        SSECustomerKeyMD5: str = None,
        SSEKMSKeyId: str = None,
        SSEKMSEncryptionContext: str = None,
        CopySourceSSECustomerAlgorithm: str = None,
        CopySourceSSECustomerKey: str = None,
        CopySourceSSECustomerKeyMD5: str = None,
        RequestPayer: Literal["requester"] = None,
        Tagging: str = None,
        ObjectLockMode: Literal["GOVERNANCE", "COMPLIANCE"] = None,
        ObjectLockRetainUntilDate: datetime = None,
        ObjectLockLegalHoldStatus: Literal["ON", "OFF"] = None,
    ) -> CopyObjectOutputTypeDef:
        """
        [Object.copy_from documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.Object.copy_from)
        """

    def delete(
        self,
        MFA: str = None,
        VersionId: str = None,
        RequestPayer: Literal["requester"] = None,
        BypassGovernanceRetention: bool = None,
    ) -> DeleteObjectOutputTypeDef:
        """
        [Object.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.Object.delete)
        """

    def download_file(
        self,
        Filename: str,
        ExtraArgs: Dict[str, Any] = None,
        Callback: Callable[..., Any] = None,
        Config: TransferConfig = None,
    ) -> None:
        """
        [Object.download_file documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.Object.download_file)
        """

    def download_fileobj(
        self,
        Fileobj: IO[Any],
        ExtraArgs: Dict[str, Any] = None,
        Callback: Callable[..., Any] = None,
        Config: TransferConfig = None,
    ) -> None:
        """
        [Object.download_fileobj documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.Object.download_fileobj)
        """

    def get(
        self,
        IfMatch: str = None,
        IfModifiedSince: datetime = None,
        IfNoneMatch: str = None,
        IfUnmodifiedSince: datetime = None,
        Range: str = None,
        ResponseCacheControl: str = None,
        ResponseContentDisposition: str = None,
        ResponseContentEncoding: str = None,
        ResponseContentLanguage: str = None,
        ResponseContentType: str = None,
        ResponseExpires: datetime = None,
        VersionId: str = None,
        SSECustomerAlgorithm: str = None,
        SSECustomerKey: str = None,
        SSECustomerKeyMD5: str = None,
        RequestPayer: Literal["requester"] = None,
        PartNumber: int = None,
    ) -> GetObjectOutputTypeDef:
        """
        [Object.get documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.Object.get)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Object.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.Object.get_available_subresources)
        """

    def initiate_multipart_upload(
        self,
        ACL: Literal[
            "private",
            "public-read",
            "public-read-write",
            "authenticated-read",
            "aws-exec-read",
            "bucket-owner-read",
            "bucket-owner-full-control",
        ] = None,
        CacheControl: str = None,
        ContentDisposition: str = None,
        ContentEncoding: str = None,
        ContentLanguage: str = None,
        ContentType: str = None,
        Expires: datetime = None,
        GrantFullControl: str = None,
        GrantRead: str = None,
        GrantReadACP: str = None,
        GrantWriteACP: str = None,
        Metadata: Dict[str, str] = None,
        ServerSideEncryption: Literal["AES256", "aws:kms"] = None,
        StorageClass: Literal[
            "STANDARD",
            "REDUCED_REDUNDANCY",
            "STANDARD_IA",
            "ONEZONE_IA",
            "INTELLIGENT_TIERING",
            "GLACIER",
            "DEEP_ARCHIVE",
        ] = None,
        WebsiteRedirectLocation: str = None,
        SSECustomerAlgorithm: str = None,
        SSECustomerKey: str = None,
        SSECustomerKeyMD5: str = None,
        SSEKMSKeyId: str = None,
        SSEKMSEncryptionContext: str = None,
        RequestPayer: Literal["requester"] = None,
        Tagging: str = None,
        ObjectLockMode: Literal["GOVERNANCE", "COMPLIANCE"] = None,
        ObjectLockRetainUntilDate: datetime = None,
        ObjectLockLegalHoldStatus: Literal["ON", "OFF"] = None,
    ) -> CreateMultipartUploadOutputTypeDef:
        """
        [Object.initiate_multipart_upload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.Object.initiate_multipart_upload)
        """

    def load(self) -> None:
        """
        [Object.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.Object.load)
        """

    def put(
        self,
        ACL: Literal[
            "private",
            "public-read",
            "public-read-write",
            "authenticated-read",
            "aws-exec-read",
            "bucket-owner-read",
            "bucket-owner-full-control",
        ] = None,
        Body: Union[bytes, IO] = None,
        CacheControl: str = None,
        ContentDisposition: str = None,
        ContentEncoding: str = None,
        ContentLanguage: str = None,
        ContentLength: int = None,
        ContentMD5: str = None,
        ContentType: str = None,
        Expires: datetime = None,
        GrantFullControl: str = None,
        GrantRead: str = None,
        GrantReadACP: str = None,
        GrantWriteACP: str = None,
        Metadata: Dict[str, str] = None,
        ServerSideEncryption: Literal["AES256", "aws:kms"] = None,
        StorageClass: Literal[
            "STANDARD",
            "REDUCED_REDUNDANCY",
            "STANDARD_IA",
            "ONEZONE_IA",
            "INTELLIGENT_TIERING",
            "GLACIER",
            "DEEP_ARCHIVE",
        ] = None,
        WebsiteRedirectLocation: str = None,
        SSECustomerAlgorithm: str = None,
        SSECustomerKey: str = None,
        SSECustomerKeyMD5: str = None,
        SSEKMSKeyId: str = None,
        SSEKMSEncryptionContext: str = None,
        RequestPayer: Literal["requester"] = None,
        Tagging: str = None,
        ObjectLockMode: Literal["GOVERNANCE", "COMPLIANCE"] = None,
        ObjectLockRetainUntilDate: datetime = None,
        ObjectLockLegalHoldStatus: Literal["ON", "OFF"] = None,
    ) -> PutObjectOutputTypeDef:
        """
        [Object.put documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.Object.put)
        """

    def reload(self) -> None:
        """
        [Object.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.Object.reload)
        """

    def restore_object(
        self,
        VersionId: str = None,
        RestoreRequest: RestoreRequestTypeDef = None,
        RequestPayer: Literal["requester"] = None,
    ) -> RestoreObjectOutputTypeDef:
        """
        [Object.restore_object documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.Object.restore_object)
        """

    def upload_file(
        self,
        Filename: str,
        ExtraArgs: Dict[str, Any] = None,
        Callback: Callable[..., Any] = None,
        Config: TransferConfig = None,
    ) -> None:
        """
        [Object.upload_file documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.Object.upload_file)
        """

    def upload_fileobj(
        self,
        Fileobj: IO[Any],
        ExtraArgs: Dict[str, Any] = None,
        Callback: Callable[..., Any] = None,
        Config: TransferConfig = None,
    ) -> None:
        """
        [Object.upload_fileobj documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.Object.upload_fileobj)
        """

    def wait_until_exists(self) -> None:
        """
        [Object.wait_until_exists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.Object.wait_until_exists)
        """

    def wait_until_not_exists(self) -> None:
        """
        [Object.wait_until_not_exists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.Object.wait_until_not_exists)
        """


class ObjectAcl(Boto3ServiceResource):
    """
    [ObjectAcl documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.ServiceResource.ObjectAcl)
    """

    owner: Dict[str, Any]
    grants: List[Any]
    request_charged: str
    bucket_name: str
    object_key: str

    def get_available_subresources(self) -> List[str]:
        """
        [ObjectAcl.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.ObjectAcl.get_available_subresources)
        """

    def load(self) -> None:
        """
        [ObjectAcl.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.ObjectAcl.load)
        """

    def put(
        self,
        ACL: Literal[
            "private",
            "public-read",
            "public-read-write",
            "authenticated-read",
            "aws-exec-read",
            "bucket-owner-read",
            "bucket-owner-full-control",
        ] = None,
        AccessControlPolicy: AccessControlPolicyTypeDef = None,
        GrantFullControl: str = None,
        GrantRead: str = None,
        GrantReadACP: str = None,
        GrantWrite: str = None,
        GrantWriteACP: str = None,
        RequestPayer: Literal["requester"] = None,
        VersionId: str = None,
    ) -> PutObjectAclOutputTypeDef:
        """
        [ObjectAcl.put documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.ObjectAcl.put)
        """

    def reload(self) -> None:
        """
        [ObjectAcl.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.ObjectAcl.reload)
        """


class ObjectSummary(Boto3ServiceResource):
    """
    [ObjectSummary documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.ServiceResource.ObjectSummary)
    """

    last_modified: datetime
    e_tag: str
    size: int
    storage_class: str
    owner: Dict[str, Any]
    bucket_name: str
    key: str

    def copy_from(
        self,
        CopySource: str,
        ACL: Literal[
            "private",
            "public-read",
            "public-read-write",
            "authenticated-read",
            "aws-exec-read",
            "bucket-owner-read",
            "bucket-owner-full-control",
        ] = None,
        CacheControl: str = None,
        ContentDisposition: str = None,
        ContentEncoding: str = None,
        ContentLanguage: str = None,
        ContentType: str = None,
        CopySourceIfMatch: str = None,
        CopySourceIfModifiedSince: datetime = None,
        CopySourceIfNoneMatch: str = None,
        CopySourceIfUnmodifiedSince: datetime = None,
        Expires: datetime = None,
        GrantFullControl: str = None,
        GrantRead: str = None,
        GrantReadACP: str = None,
        GrantWriteACP: str = None,
        Metadata: Dict[str, str] = None,
        MetadataDirective: Literal["COPY", "REPLACE"] = None,
        TaggingDirective: Literal["COPY", "REPLACE"] = None,
        ServerSideEncryption: Literal["AES256", "aws:kms"] = None,
        StorageClass: Literal[
            "STANDARD",
            "REDUCED_REDUNDANCY",
            "STANDARD_IA",
            "ONEZONE_IA",
            "INTELLIGENT_TIERING",
            "GLACIER",
            "DEEP_ARCHIVE",
        ] = None,
        WebsiteRedirectLocation: str = None,
        SSECustomerAlgorithm: str = None,
        SSECustomerKey: str = None,
        SSECustomerKeyMD5: str = None,
        SSEKMSKeyId: str = None,
        SSEKMSEncryptionContext: str = None,
        CopySourceSSECustomerAlgorithm: str = None,
        CopySourceSSECustomerKey: str = None,
        CopySourceSSECustomerKeyMD5: str = None,
        RequestPayer: Literal["requester"] = None,
        Tagging: str = None,
        ObjectLockMode: Literal["GOVERNANCE", "COMPLIANCE"] = None,
        ObjectLockRetainUntilDate: datetime = None,
        ObjectLockLegalHoldStatus: Literal["ON", "OFF"] = None,
    ) -> CopyObjectOutputTypeDef:
        """
        [ObjectSummary.copy_from documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.ObjectSummary.copy_from)
        """

    def delete(
        self,
        MFA: str = None,
        VersionId: str = None,
        RequestPayer: Literal["requester"] = None,
        BypassGovernanceRetention: bool = None,
    ) -> DeleteObjectOutputTypeDef:
        """
        [ObjectSummary.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.ObjectSummary.delete)
        """

    def get(
        self,
        IfMatch: str = None,
        IfModifiedSince: datetime = None,
        IfNoneMatch: str = None,
        IfUnmodifiedSince: datetime = None,
        Range: str = None,
        ResponseCacheControl: str = None,
        ResponseContentDisposition: str = None,
        ResponseContentEncoding: str = None,
        ResponseContentLanguage: str = None,
        ResponseContentType: str = None,
        ResponseExpires: datetime = None,
        VersionId: str = None,
        SSECustomerAlgorithm: str = None,
        SSECustomerKey: str = None,
        SSECustomerKeyMD5: str = None,
        RequestPayer: Literal["requester"] = None,
        PartNumber: int = None,
    ) -> GetObjectOutputTypeDef:
        """
        [ObjectSummary.get documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.ObjectSummary.get)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [ObjectSummary.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.ObjectSummary.get_available_subresources)
        """

    def initiate_multipart_upload(
        self,
        ACL: Literal[
            "private",
            "public-read",
            "public-read-write",
            "authenticated-read",
            "aws-exec-read",
            "bucket-owner-read",
            "bucket-owner-full-control",
        ] = None,
        CacheControl: str = None,
        ContentDisposition: str = None,
        ContentEncoding: str = None,
        ContentLanguage: str = None,
        ContentType: str = None,
        Expires: datetime = None,
        GrantFullControl: str = None,
        GrantRead: str = None,
        GrantReadACP: str = None,
        GrantWriteACP: str = None,
        Metadata: Dict[str, str] = None,
        ServerSideEncryption: Literal["AES256", "aws:kms"] = None,
        StorageClass: Literal[
            "STANDARD",
            "REDUCED_REDUNDANCY",
            "STANDARD_IA",
            "ONEZONE_IA",
            "INTELLIGENT_TIERING",
            "GLACIER",
            "DEEP_ARCHIVE",
        ] = None,
        WebsiteRedirectLocation: str = None,
        SSECustomerAlgorithm: str = None,
        SSECustomerKey: str = None,
        SSECustomerKeyMD5: str = None,
        SSEKMSKeyId: str = None,
        SSEKMSEncryptionContext: str = None,
        RequestPayer: Literal["requester"] = None,
        Tagging: str = None,
        ObjectLockMode: Literal["GOVERNANCE", "COMPLIANCE"] = None,
        ObjectLockRetainUntilDate: datetime = None,
        ObjectLockLegalHoldStatus: Literal["ON", "OFF"] = None,
    ) -> CreateMultipartUploadOutputTypeDef:
        """
        [ObjectSummary.initiate_multipart_upload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.ObjectSummary.initiate_multipart_upload)
        """

    def load(self) -> None:
        """
        [ObjectSummary.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.ObjectSummary.load)
        """

    def put(
        self,
        ACL: Literal[
            "private",
            "public-read",
            "public-read-write",
            "authenticated-read",
            "aws-exec-read",
            "bucket-owner-read",
            "bucket-owner-full-control",
        ] = None,
        Body: Union[bytes, IO] = None,
        CacheControl: str = None,
        ContentDisposition: str = None,
        ContentEncoding: str = None,
        ContentLanguage: str = None,
        ContentLength: int = None,
        ContentMD5: str = None,
        ContentType: str = None,
        Expires: datetime = None,
        GrantFullControl: str = None,
        GrantRead: str = None,
        GrantReadACP: str = None,
        GrantWriteACP: str = None,
        Metadata: Dict[str, str] = None,
        ServerSideEncryption: Literal["AES256", "aws:kms"] = None,
        StorageClass: Literal[
            "STANDARD",
            "REDUCED_REDUNDANCY",
            "STANDARD_IA",
            "ONEZONE_IA",
            "INTELLIGENT_TIERING",
            "GLACIER",
            "DEEP_ARCHIVE",
        ] = None,
        WebsiteRedirectLocation: str = None,
        SSECustomerAlgorithm: str = None,
        SSECustomerKey: str = None,
        SSECustomerKeyMD5: str = None,
        SSEKMSKeyId: str = None,
        SSEKMSEncryptionContext: str = None,
        RequestPayer: Literal["requester"] = None,
        Tagging: str = None,
        ObjectLockMode: Literal["GOVERNANCE", "COMPLIANCE"] = None,
        ObjectLockRetainUntilDate: datetime = None,
        ObjectLockLegalHoldStatus: Literal["ON", "OFF"] = None,
    ) -> PutObjectOutputTypeDef:
        """
        [ObjectSummary.put documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.ObjectSummary.put)
        """

    def restore_object(
        self,
        VersionId: str = None,
        RestoreRequest: RestoreRequestTypeDef = None,
        RequestPayer: Literal["requester"] = None,
    ) -> RestoreObjectOutputTypeDef:
        """
        [ObjectSummary.restore_object documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.ObjectSummary.restore_object)
        """

    def wait_until_exists(self) -> None:
        """
        [ObjectSummary.wait_until_exists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.ObjectSummary.wait_until_exists)
        """

    def wait_until_not_exists(self) -> None:
        """
        [ObjectSummary.wait_until_not_exists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.ObjectSummary.wait_until_not_exists)
        """


class ObjectVersion(Boto3ServiceResource):
    """
    [ObjectVersion documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.ServiceResource.ObjectVersion)
    """

    e_tag: str
    size: int
    storage_class: str
    key: str
    version_id: str
    is_latest: bool
    last_modified: datetime
    owner: Dict[str, Any]
    bucket_name: str
    object_key: str
    id: str

    def delete(
        self,
        MFA: str = None,
        RequestPayer: Literal["requester"] = None,
        BypassGovernanceRetention: bool = None,
    ) -> DeleteObjectOutputTypeDef:
        """
        [ObjectVersion.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.ObjectVersion.delete)
        """

    def get(
        self,
        IfMatch: str = None,
        IfModifiedSince: datetime = None,
        IfNoneMatch: str = None,
        IfUnmodifiedSince: datetime = None,
        Range: str = None,
        ResponseCacheControl: str = None,
        ResponseContentDisposition: str = None,
        ResponseContentEncoding: str = None,
        ResponseContentLanguage: str = None,
        ResponseContentType: str = None,
        ResponseExpires: datetime = None,
        SSECustomerAlgorithm: str = None,
        SSECustomerKey: str = None,
        SSECustomerKeyMD5: str = None,
        RequestPayer: Literal["requester"] = None,
        PartNumber: int = None,
    ) -> GetObjectOutputTypeDef:
        """
        [ObjectVersion.get documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.ObjectVersion.get)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [ObjectVersion.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.ObjectVersion.get_available_subresources)
        """

    def head(
        self,
        IfMatch: str = None,
        IfModifiedSince: datetime = None,
        IfNoneMatch: str = None,
        IfUnmodifiedSince: datetime = None,
        Range: str = None,
        SSECustomerAlgorithm: str = None,
        SSECustomerKey: str = None,
        SSECustomerKeyMD5: str = None,
        RequestPayer: Literal["requester"] = None,
        PartNumber: int = None,
    ) -> HeadObjectOutputTypeDef:
        """
        [ObjectVersion.head documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.ObjectVersion.head)
        """


class ServiceResourceBucketsCollection(ResourceCollection):
    """
    [ServiceResource.buckets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.ServiceResource.buckets)
    """

    @classmethod
    def all(cls) -> "service_resource_scope.ServiceResourceBucketsCollection":
        pass

    @classmethod
    def filter(cls) -> "service_resource_scope.ServiceResourceBucketsCollection":
        pass

    @classmethod
    def limit(cls, count: int) -> "service_resource_scope.ServiceResourceBucketsCollection":
        pass

    @classmethod
    def page_size(cls, count: int) -> "service_resource_scope.ServiceResourceBucketsCollection":
        pass

    @classmethod
    def pages(cls) -> List["service_resource_scope.Bucket"]:
        pass


class BucketMultipartUploadsCollection(ResourceCollection):
    """
    [Bucket.multipart_uploads documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.Bucket.multipart_uploads)
    """

    @classmethod
    def all(cls) -> "service_resource_scope.BucketMultipartUploadsCollection":
        pass

    @classmethod
    def filter(
        cls,
        Delimiter: str = None,
        EncodingType: Literal["url"] = None,
        KeyMarker: str = None,
        MaxUploads: int = None,
        Prefix: str = None,
        UploadIdMarker: str = None,
    ) -> "service_resource_scope.BucketMultipartUploadsCollection":
        pass

    @classmethod
    def limit(cls, count: int) -> "service_resource_scope.BucketMultipartUploadsCollection":
        pass

    @classmethod
    def page_size(cls, count: int) -> "service_resource_scope.BucketMultipartUploadsCollection":
        pass

    @classmethod
    def pages(cls) -> List["service_resource_scope.MultipartUpload"]:
        pass


class BucketObjectVersionsCollection(ResourceCollection):
    """
    [Bucket.object_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.Bucket.object_versions)
    """

    @classmethod
    def all(cls) -> "service_resource_scope.BucketObjectVersionsCollection":
        pass

    @classmethod
    def filter(
        cls,
        Delimiter: str = None,
        EncodingType: Literal["url"] = None,
        KeyMarker: str = None,
        MaxKeys: int = None,
        Prefix: str = None,
        VersionIdMarker: str = None,
    ) -> "service_resource_scope.BucketObjectVersionsCollection":
        pass

    @classmethod
    def delete(
        cls,
        MFA: str = None,
        RequestPayer: Literal["requester"] = None,
        BypassGovernanceRetention: bool = None,
    ) -> DeleteObjectsOutputTypeDef:
        pass

    @classmethod
    def limit(cls, count: int) -> "service_resource_scope.BucketObjectVersionsCollection":
        pass

    @classmethod
    def page_size(cls, count: int) -> "service_resource_scope.BucketObjectVersionsCollection":
        pass

    @classmethod
    def pages(cls) -> List["service_resource_scope.ObjectVersion"]:
        pass


class BucketObjectsCollection(ResourceCollection):
    """
    [Bucket.objects documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.Bucket.objects)
    """

    @classmethod
    def all(cls) -> "service_resource_scope.BucketObjectsCollection":
        pass

    @classmethod
    def filter(
        cls,
        Delimiter: str = None,
        EncodingType: Literal["url"] = None,
        Marker: str = None,
        MaxKeys: int = None,
        Prefix: str = None,
        RequestPayer: Literal["requester"] = None,
    ) -> "service_resource_scope.BucketObjectsCollection":
        pass

    @classmethod
    def delete(
        cls,
        MFA: str = None,
        RequestPayer: Literal["requester"] = None,
        BypassGovernanceRetention: bool = None,
    ) -> DeleteObjectsOutputTypeDef:
        pass

    @classmethod
    def limit(cls, count: int) -> "service_resource_scope.BucketObjectsCollection":
        pass

    @classmethod
    def page_size(cls, count: int) -> "service_resource_scope.BucketObjectsCollection":
        pass

    @classmethod
    def pages(cls) -> List["service_resource_scope.ObjectSummary"]:
        pass


class MultipartUploadPartsCollection(ResourceCollection):
    """
    [MultipartUpload.parts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/s3.html#S3.MultipartUpload.parts)
    """

    @classmethod
    def all(cls) -> "service_resource_scope.MultipartUploadPartsCollection":
        pass

    @classmethod
    def filter(
        cls,
        MaxParts: int = None,
        PartNumberMarker: int = None,
        RequestPayer: Literal["requester"] = None,
    ) -> "service_resource_scope.MultipartUploadPartsCollection":
        pass

    @classmethod
    def limit(cls, count: int) -> "service_resource_scope.MultipartUploadPartsCollection":
        pass

    @classmethod
    def page_size(cls, count: int) -> "service_resource_scope.MultipartUploadPartsCollection":
        pass

    @classmethod
    def pages(cls) -> List["service_resource_scope.MultipartUploadPart"]:
        pass
