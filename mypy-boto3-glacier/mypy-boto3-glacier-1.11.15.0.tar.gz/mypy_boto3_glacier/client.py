"""
Main interface for glacier service client

Usage::

    import boto3
    from mypy_boto3.glacier import GlacierClient

    session = boto3.Session()

    client: GlacierClient = boto3.client("glacier")
    session_client: GlacierClient = session.client("glacier")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Any, Dict, IO, List, TYPE_CHECKING, Union, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_glacier.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_glacier.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_glacier.type_defs import (
    ClientCompleteMultipartUploadResponseTypeDef,
    ClientCreateVaultResponseTypeDef,
    ClientDescribeJobResponseTypeDef,
    ClientDescribeVaultResponseTypeDef,
    ClientGetDataRetrievalPolicyResponseTypeDef,
    ClientGetJobOutputResponseTypeDef,
    ClientGetVaultAccessPolicyResponseTypeDef,
    ClientGetVaultLockResponseTypeDef,
    ClientGetVaultNotificationsResponseTypeDef,
    ClientInitiateJobJobParametersTypeDef,
    ClientInitiateJobResponseTypeDef,
    ClientInitiateMultipartUploadResponseTypeDef,
    ClientInitiateVaultLockPolicyTypeDef,
    ClientInitiateVaultLockResponseTypeDef,
    ClientListJobsResponseTypeDef,
    ClientListMultipartUploadsResponseTypeDef,
    ClientListPartsResponseTypeDef,
    ClientListProvisionedCapacityResponseTypeDef,
    ClientListTagsForVaultResponseTypeDef,
    ClientListVaultsResponseTypeDef,
    ClientPurchaseProvisionedCapacityResponseTypeDef,
    ClientSetDataRetrievalPolicyPolicyTypeDef,
    ClientSetVaultAccessPolicyPolicyTypeDef,
    ClientSetVaultNotificationsVaultNotificationConfigTypeDef,
    ClientUploadArchiveResponseTypeDef,
    ClientUploadMultipartPartResponseTypeDef,
)

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_glacier.waiter as waiter_scope
else:
    waiter_scope = object
if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("GlacierClient",)


class GlacierClient:
    """
    [Glacier.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glacier.html#Glacier.Client)
    """

    exceptions: "client_scope.Exceptions"

    def abort_multipart_upload(self, vaultName: str, uploadId: str, accountId: str = None) -> None:
        """
        [Client.abort_multipart_upload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glacier.html#Glacier.Client.abort_multipart_upload)
        """

    def abort_vault_lock(self, vaultName: str, accountId: str = None) -> None:
        """
        [Client.abort_vault_lock documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glacier.html#Glacier.Client.abort_vault_lock)
        """

    def add_tags_to_vault(
        self, vaultName: str, accountId: str = None, Tags: Dict[str, str] = None
    ) -> None:
        """
        [Client.add_tags_to_vault documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glacier.html#Glacier.Client.add_tags_to_vault)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glacier.html#Glacier.Client.can_paginate)
        """

    def complete_multipart_upload(
        self,
        vaultName: str,
        uploadId: str,
        accountId: str = None,
        archiveSize: str = None,
        checksum: str = None,
    ) -> ClientCompleteMultipartUploadResponseTypeDef:
        """
        [Client.complete_multipart_upload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glacier.html#Glacier.Client.complete_multipart_upload)
        """

    def complete_vault_lock(self, vaultName: str, lockId: str, accountId: str = None) -> None:
        """
        [Client.complete_vault_lock documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glacier.html#Glacier.Client.complete_vault_lock)
        """

    def create_vault(
        self, vaultName: str, accountId: str = None
    ) -> ClientCreateVaultResponseTypeDef:
        """
        [Client.create_vault documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glacier.html#Glacier.Client.create_vault)
        """

    def delete_archive(self, vaultName: str, archiveId: str, accountId: str = None) -> None:
        """
        [Client.delete_archive documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glacier.html#Glacier.Client.delete_archive)
        """

    def delete_vault(self, vaultName: str, accountId: str = None) -> None:
        """
        [Client.delete_vault documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glacier.html#Glacier.Client.delete_vault)
        """

    def delete_vault_access_policy(self, vaultName: str, accountId: str = None) -> None:
        """
        [Client.delete_vault_access_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glacier.html#Glacier.Client.delete_vault_access_policy)
        """

    def delete_vault_notifications(self, vaultName: str, accountId: str = None) -> None:
        """
        [Client.delete_vault_notifications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glacier.html#Glacier.Client.delete_vault_notifications)
        """

    def describe_job(
        self, vaultName: str, jobId: str, accountId: str = None
    ) -> ClientDescribeJobResponseTypeDef:
        """
        [Client.describe_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glacier.html#Glacier.Client.describe_job)
        """

    def describe_vault(
        self, vaultName: str, accountId: str = None
    ) -> ClientDescribeVaultResponseTypeDef:
        """
        [Client.describe_vault documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glacier.html#Glacier.Client.describe_vault)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glacier.html#Glacier.Client.generate_presigned_url)
        """

    def get_data_retrieval_policy(
        self, accountId: str = None
    ) -> ClientGetDataRetrievalPolicyResponseTypeDef:
        """
        [Client.get_data_retrieval_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glacier.html#Glacier.Client.get_data_retrieval_policy)
        """

    def get_job_output(
        self, vaultName: str, jobId: str, accountId: str = None, range: str = None
    ) -> ClientGetJobOutputResponseTypeDef:
        """
        [Client.get_job_output documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glacier.html#Glacier.Client.get_job_output)
        """

    def get_vault_access_policy(
        self, vaultName: str, accountId: str = None
    ) -> ClientGetVaultAccessPolicyResponseTypeDef:
        """
        [Client.get_vault_access_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glacier.html#Glacier.Client.get_vault_access_policy)
        """

    def get_vault_lock(
        self, vaultName: str, accountId: str = None
    ) -> ClientGetVaultLockResponseTypeDef:
        """
        [Client.get_vault_lock documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glacier.html#Glacier.Client.get_vault_lock)
        """

    def get_vault_notifications(
        self, vaultName: str, accountId: str = None
    ) -> ClientGetVaultNotificationsResponseTypeDef:
        """
        [Client.get_vault_notifications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glacier.html#Glacier.Client.get_vault_notifications)
        """

    def initiate_job(
        self,
        vaultName: str,
        accountId: str = None,
        jobParameters: ClientInitiateJobJobParametersTypeDef = None,
    ) -> ClientInitiateJobResponseTypeDef:
        """
        [Client.initiate_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glacier.html#Glacier.Client.initiate_job)
        """

    def initiate_multipart_upload(
        self,
        vaultName: str,
        accountId: str = None,
        archiveDescription: str = None,
        partSize: str = None,
    ) -> ClientInitiateMultipartUploadResponseTypeDef:
        """
        [Client.initiate_multipart_upload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glacier.html#Glacier.Client.initiate_multipart_upload)
        """

    def initiate_vault_lock(
        self,
        vaultName: str,
        accountId: str = None,
        policy: ClientInitiateVaultLockPolicyTypeDef = None,
    ) -> ClientInitiateVaultLockResponseTypeDef:
        """
        [Client.initiate_vault_lock documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glacier.html#Glacier.Client.initiate_vault_lock)
        """

    def list_jobs(
        self,
        vaultName: str,
        accountId: str = None,
        limit: str = None,
        marker: str = None,
        statuscode: str = None,
        completed: str = None,
    ) -> ClientListJobsResponseTypeDef:
        """
        [Client.list_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glacier.html#Glacier.Client.list_jobs)
        """

    def list_multipart_uploads(
        self, vaultName: str, accountId: str = None, marker: str = None, limit: str = None
    ) -> ClientListMultipartUploadsResponseTypeDef:
        """
        [Client.list_multipart_uploads documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glacier.html#Glacier.Client.list_multipart_uploads)
        """

    def list_parts(
        self,
        vaultName: str,
        uploadId: str,
        accountId: str = None,
        marker: str = None,
        limit: str = None,
    ) -> ClientListPartsResponseTypeDef:
        """
        [Client.list_parts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glacier.html#Glacier.Client.list_parts)
        """

    def list_provisioned_capacity(
        self, accountId: str = None
    ) -> ClientListProvisionedCapacityResponseTypeDef:
        """
        [Client.list_provisioned_capacity documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glacier.html#Glacier.Client.list_provisioned_capacity)
        """

    def list_tags_for_vault(
        self, vaultName: str, accountId: str = None
    ) -> ClientListTagsForVaultResponseTypeDef:
        """
        [Client.list_tags_for_vault documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glacier.html#Glacier.Client.list_tags_for_vault)
        """

    def list_vaults(
        self, accountId: str = None, marker: str = None, limit: str = None
    ) -> ClientListVaultsResponseTypeDef:
        """
        [Client.list_vaults documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glacier.html#Glacier.Client.list_vaults)
        """

    def purchase_provisioned_capacity(
        self, accountId: str = None
    ) -> ClientPurchaseProvisionedCapacityResponseTypeDef:
        """
        [Client.purchase_provisioned_capacity documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glacier.html#Glacier.Client.purchase_provisioned_capacity)
        """

    def remove_tags_from_vault(
        self, vaultName: str, accountId: str = None, TagKeys: List[str] = None
    ) -> None:
        """
        [Client.remove_tags_from_vault documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glacier.html#Glacier.Client.remove_tags_from_vault)
        """

    def set_data_retrieval_policy(
        self, accountId: str = None, Policy: ClientSetDataRetrievalPolicyPolicyTypeDef = None
    ) -> None:
        """
        [Client.set_data_retrieval_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glacier.html#Glacier.Client.set_data_retrieval_policy)
        """

    def set_vault_access_policy(
        self,
        vaultName: str,
        accountId: str = None,
        policy: ClientSetVaultAccessPolicyPolicyTypeDef = None,
    ) -> None:
        """
        [Client.set_vault_access_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glacier.html#Glacier.Client.set_vault_access_policy)
        """

    def set_vault_notifications(
        self,
        vaultName: str,
        accountId: str = None,
        vaultNotificationConfig: ClientSetVaultNotificationsVaultNotificationConfigTypeDef = None,
    ) -> None:
        """
        [Client.set_vault_notifications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glacier.html#Glacier.Client.set_vault_notifications)
        """

    def upload_archive(
        self,
        vaultName: str,
        accountId: str = None,
        archiveDescription: str = None,
        checksum: str = None,
        body: Union[bytes, IO] = None,
    ) -> ClientUploadArchiveResponseTypeDef:
        """
        [Client.upload_archive documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glacier.html#Glacier.Client.upload_archive)
        """

    def upload_multipart_part(
        self,
        vaultName: str,
        uploadId: str,
        accountId: str = None,
        checksum: str = None,
        range: str = None,
        body: Union[bytes, IO] = None,
    ) -> ClientUploadMultipartPartResponseTypeDef:
        """
        [Client.upload_multipart_part documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glacier.html#Glacier.Client.upload_multipart_part)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_jobs"]
    ) -> "paginator_scope.ListJobsPaginator":
        """
        [Paginator.ListJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glacier.html#Glacier.Paginator.ListJobs)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_multipart_uploads"]
    ) -> "paginator_scope.ListMultipartUploadsPaginator":
        """
        [Paginator.ListMultipartUploads documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glacier.html#Glacier.Paginator.ListMultipartUploads)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_parts"]
    ) -> "paginator_scope.ListPartsPaginator":
        """
        [Paginator.ListParts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glacier.html#Glacier.Paginator.ListParts)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_vaults"]
    ) -> "paginator_scope.ListVaultsPaginator":
        """
        [Paginator.ListVaults documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glacier.html#Glacier.Paginator.ListVaults)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["vault_exists"]) -> "waiter_scope.VaultExistsWaiter":
        """
        [Waiter.VaultExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glacier.html#Glacier.Waiter.VaultExists)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["vault_not_exists"]
    ) -> "waiter_scope.VaultNotExistsWaiter":
        """
        [Waiter.VaultNotExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glacier.html#Glacier.Waiter.VaultNotExists)
        """


class Exceptions:
    ClientError: Boto3ClientError
    InsufficientCapacityException: Boto3ClientError
    InvalidParameterValueException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    MissingParameterValueException: Boto3ClientError
    PolicyEnforcedException: Boto3ClientError
    RequestTimeoutException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    ServiceUnavailableException: Boto3ClientError
