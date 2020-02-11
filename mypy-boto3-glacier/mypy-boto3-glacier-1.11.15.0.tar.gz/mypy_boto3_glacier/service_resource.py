"""
Main interface for glacier service ServiceResource

Usage::

    import boto3
    from mypy_boto3.glacier import GlacierServiceResource
    import mypy_boto3.glacier.service_resource as glacier_resources

    resource: GlacierServiceResource = boto3.resource("glacier")
    session_resource: GlacierServiceResource = session.resource("glacier")

    Account: glacier_resources.Account = resource.Account(...)
    ...
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from typing import Any, Dict, IO, List, TYPE_CHECKING, Union
from boto3.resources.base import ServiceResource as Boto3ServiceResource
from boto3.resources.collection import ResourceCollection

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_glacier.service_resource as service_resource_scope
else:
    service_resource_scope = object
from mypy_boto3_glacier.type_defs import (
    ArchiveCreationOutputTypeDef,
    CreateVaultOutputTypeDef,
    GetJobOutputOutputTypeDef,
    InitiateJobOutputTypeDef,
    InitiateMultipartUploadOutputTypeDef,
    JobParametersTypeDef,
    ListPartsOutputTypeDef,
    UploadMultipartPartOutputTypeDef,
    VaultNotificationConfigTypeDef,
)


__all__ = (
    "GlacierServiceResource",
    "Account",
    "Archive",
    "Job",
    "MultipartUpload",
    "Notification",
    "Vault",
    "ServiceResourceVaultsCollection",
    "AccountVaultsCollection",
    "VaultCompletedJobsCollection",
    "VaultFailedJobsCollection",
    "VaultJobsCollection",
    "VaultJobsInProgressCollection",
    "VaultMultipartUplaodsCollection",
    "VaultMultipartUploadsCollection",
    "VaultSucceededJobsCollection",
)


class GlacierServiceResource(Boto3ServiceResource):
    """
    [Glacier.ServiceResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glacier.html#Glacier.ServiceResource)
    """

    vaults: "service_resource_scope.ServiceResourceVaultsCollection"

    def Account(self, id: str) -> "service_resource_scope.Account":
        """
        [ServiceResource.Account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glacier.html#Glacier.ServiceResource.Account)
        """

    def Archive(
        self, account_id: str, vault_name: str, id: str
    ) -> "service_resource_scope.Archive":
        """
        [ServiceResource.Archive documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glacier.html#Glacier.ServiceResource.Archive)
        """

    def Job(self, account_id: str, vault_name: str, id: str) -> "service_resource_scope.Job":
        """
        [ServiceResource.Job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glacier.html#Glacier.ServiceResource.Job)
        """

    def MultipartUpload(
        self, account_id: str, vault_name: str, id: str
    ) -> "service_resource_scope.MultipartUpload":
        """
        [ServiceResource.MultipartUpload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glacier.html#Glacier.ServiceResource.MultipartUpload)
        """

    def Notification(
        self, account_id: str, vault_name: str
    ) -> "service_resource_scope.Notification":
        """
        [ServiceResource.Notification documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glacier.html#Glacier.ServiceResource.Notification)
        """

    def Vault(self, account_id: str, name: str) -> "service_resource_scope.Vault":
        """
        [ServiceResource.Vault documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glacier.html#Glacier.ServiceResource.Vault)
        """

    def create_vault(self, accountId: str, vaultName: str) -> CreateVaultOutputTypeDef:
        """
        [ServiceResource.create_vault documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glacier.html#Glacier.ServiceResource.create_vault)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [ServiceResource.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glacier.html#Glacier.ServiceResource.get_available_subresources)
        """


class Account(Boto3ServiceResource):
    """
    [Account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glacier.html#Glacier.ServiceResource.Account)
    """

    id: str
    vaults: "service_resource_scope.AccountVaultsCollection"

    def create_vault(self, vaultName: str) -> CreateVaultOutputTypeDef:
        """
        [Account.create_vault documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glacier.html#Glacier.Account.create_vault)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Account.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glacier.html#Glacier.Account.get_available_subresources)
        """


class Archive(Boto3ServiceResource):
    """
    [Archive documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glacier.html#Glacier.ServiceResource.Archive)
    """

    account_id: str
    vault_name: str
    id: str

    def delete(self) -> None:
        """
        [Archive.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glacier.html#Glacier.Archive.delete)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Archive.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glacier.html#Glacier.Archive.get_available_subresources)
        """

    def initiate_archive_retrieval(
        self, jobParameters: JobParametersTypeDef = None
    ) -> InitiateJobOutputTypeDef:
        """
        [Archive.initiate_archive_retrieval documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glacier.html#Glacier.Archive.initiate_archive_retrieval)
        """


class Job(Boto3ServiceResource):
    """
    [Job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glacier.html#Glacier.ServiceResource.Job)
    """

    job_id: str
    job_description: str
    action: str
    archive_id: str
    vault_arn: str
    creation_date: str
    completed: bool
    status_code: str
    status_message: str
    archive_size_in_bytes: int
    inventory_size_in_bytes: int
    sns_topic: str
    completion_date: str
    sha256_tree_hash: str
    archive_sha256_tree_hash: str
    retrieval_byte_range: str
    tier: str
    inventory_retrieval_parameters: Dict[str, Any]
    job_output_path: str
    select_parameters: Dict[str, Any]
    output_location: Dict[str, Any]
    account_id: str
    vault_name: str
    id: str

    def get_available_subresources(self) -> List[str]:
        """
        [Job.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glacier.html#Glacier.Job.get_available_subresources)
        """

    def get_output(self, range: str = None) -> GetJobOutputOutputTypeDef:
        """
        [Job.get_output documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glacier.html#Glacier.Job.get_output)
        """

    def load(self) -> None:
        """
        [Job.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glacier.html#Glacier.Job.load)
        """

    def reload(self) -> None:
        """
        [Job.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glacier.html#Glacier.Job.reload)
        """


class MultipartUpload(Boto3ServiceResource):
    """
    [MultipartUpload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glacier.html#Glacier.ServiceResource.MultipartUpload)
    """

    multipart_upload_id: str
    vault_arn: str
    archive_description: str
    part_size_in_bytes: int
    creation_date: str
    account_id: str
    vault_name: str
    id: str

    def abort(self) -> None:
        """
        [MultipartUpload.abort documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glacier.html#Glacier.MultipartUpload.abort)
        """

    def complete(
        self, archiveSize: str = None, checksum: str = None
    ) -> ArchiveCreationOutputTypeDef:
        """
        [MultipartUpload.complete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glacier.html#Glacier.MultipartUpload.complete)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [MultipartUpload.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glacier.html#Glacier.MultipartUpload.get_available_subresources)
        """

    def parts(self, marker: str = None, limit: str = None) -> ListPartsOutputTypeDef:
        """
        [MultipartUpload.parts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glacier.html#Glacier.MultipartUpload.parts)
        """

    def upload_part(
        self, checksum: str = None, range: str = None, body: Union[bytes, IO] = None
    ) -> UploadMultipartPartOutputTypeDef:
        """
        [MultipartUpload.upload_part documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glacier.html#Glacier.MultipartUpload.upload_part)
        """


class Notification(Boto3ServiceResource):
    """
    [Notification documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glacier.html#Glacier.ServiceResource.Notification)
    """

    sns_topic: str
    events: List[Any]
    account_id: str
    vault_name: str

    def delete(self) -> None:
        """
        [Notification.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glacier.html#Glacier.Notification.delete)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Notification.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glacier.html#Glacier.Notification.get_available_subresources)
        """

    def load(self) -> None:
        """
        [Notification.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glacier.html#Glacier.Notification.load)
        """

    def reload(self) -> None:
        """
        [Notification.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glacier.html#Glacier.Notification.reload)
        """

    def set(self, vaultNotificationConfig: VaultNotificationConfigTypeDef = None) -> None:
        """
        [Notification.set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glacier.html#Glacier.Notification.set)
        """


class Vault(Boto3ServiceResource):
    """
    [Vault documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glacier.html#Glacier.ServiceResource.Vault)
    """

    vault_arn: str
    vault_name: str
    creation_date: str
    last_inventory_date: str
    number_of_archives: int
    size_in_bytes: int
    account_id: str
    name: str
    completed_jobs: "service_resource_scope.VaultCompletedJobsCollection"
    failed_jobs: "service_resource_scope.VaultFailedJobsCollection"
    jobs: "service_resource_scope.VaultJobsCollection"
    jobs_in_progress: "service_resource_scope.VaultJobsInProgressCollection"
    multipart_uplaods: "service_resource_scope.VaultMultipartUplaodsCollection"
    multipart_uploads: "service_resource_scope.VaultMultipartUploadsCollection"
    succeeded_jobs: "service_resource_scope.VaultSucceededJobsCollection"

    def create(self) -> CreateVaultOutputTypeDef:
        """
        [Vault.create documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glacier.html#Glacier.Vault.create)
        """

    def delete(self) -> None:
        """
        [Vault.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glacier.html#Glacier.Vault.delete)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Vault.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glacier.html#Glacier.Vault.get_available_subresources)
        """

    def initiate_inventory_retrieval(
        self, jobParameters: JobParametersTypeDef = None
    ) -> InitiateJobOutputTypeDef:
        """
        [Vault.initiate_inventory_retrieval documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glacier.html#Glacier.Vault.initiate_inventory_retrieval)
        """

    def initiate_multipart_upload(
        self, archiveDescription: str = None, partSize: str = None
    ) -> InitiateMultipartUploadOutputTypeDef:
        """
        [Vault.initiate_multipart_upload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glacier.html#Glacier.Vault.initiate_multipart_upload)
        """

    def load(self) -> None:
        """
        [Vault.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glacier.html#Glacier.Vault.load)
        """

    def reload(self) -> None:
        """
        [Vault.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glacier.html#Glacier.Vault.reload)
        """

    def upload_archive(
        self, archiveDescription: str = None, checksum: str = None, body: Union[bytes, IO] = None
    ) -> ArchiveCreationOutputTypeDef:
        """
        [Vault.upload_archive documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glacier.html#Glacier.Vault.upload_archive)
        """


class ServiceResourceVaultsCollection(ResourceCollection):
    """
    [ServiceResource.vaults documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glacier.html#Glacier.ServiceResource.vaults)
    """

    @classmethod
    def all(cls) -> "service_resource_scope.ServiceResourceVaultsCollection":
        pass

    @classmethod
    def filter(
        cls, marker: str = None, limit: str = None
    ) -> "service_resource_scope.ServiceResourceVaultsCollection":
        pass

    @classmethod
    def limit(cls, count: int) -> "service_resource_scope.ServiceResourceVaultsCollection":
        pass

    @classmethod
    def page_size(cls, count: int) -> "service_resource_scope.ServiceResourceVaultsCollection":
        pass

    @classmethod
    def pages(cls) -> List["service_resource_scope.Vault"]:
        pass


class AccountVaultsCollection(ResourceCollection):
    """
    [Account.vaults documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glacier.html#Glacier.Account.vaults)
    """

    @classmethod
    def all(cls) -> "service_resource_scope.AccountVaultsCollection":
        pass

    @classmethod
    def filter(
        cls, marker: str = None, limit: str = None
    ) -> "service_resource_scope.AccountVaultsCollection":
        pass

    @classmethod
    def limit(cls, count: int) -> "service_resource_scope.AccountVaultsCollection":
        pass

    @classmethod
    def page_size(cls, count: int) -> "service_resource_scope.AccountVaultsCollection":
        pass

    @classmethod
    def pages(cls) -> List["service_resource_scope.Vault"]:
        pass


class VaultCompletedJobsCollection(ResourceCollection):
    """
    [Vault.completed_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glacier.html#Glacier.Vault.completed_jobs)
    """

    @classmethod
    def all(cls) -> "service_resource_scope.VaultCompletedJobsCollection":
        pass

    @classmethod
    def filter(
        cls, limit: str = None, marker: str = None, statuscode: str = None, completed: str = None
    ) -> "service_resource_scope.VaultCompletedJobsCollection":
        pass

    @classmethod
    def limit(cls, count: int) -> "service_resource_scope.VaultCompletedJobsCollection":
        pass

    @classmethod
    def page_size(cls, count: int) -> "service_resource_scope.VaultCompletedJobsCollection":
        pass

    @classmethod
    def pages(cls) -> List["service_resource_scope.Job"]:
        pass


class VaultFailedJobsCollection(ResourceCollection):
    """
    [Vault.failed_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glacier.html#Glacier.Vault.failed_jobs)
    """

    @classmethod
    def all(cls) -> "service_resource_scope.VaultFailedJobsCollection":
        pass

    @classmethod
    def filter(
        cls, limit: str = None, marker: str = None, statuscode: str = None, completed: str = None
    ) -> "service_resource_scope.VaultFailedJobsCollection":
        pass

    @classmethod
    def limit(cls, count: int) -> "service_resource_scope.VaultFailedJobsCollection":
        pass

    @classmethod
    def page_size(cls, count: int) -> "service_resource_scope.VaultFailedJobsCollection":
        pass

    @classmethod
    def pages(cls) -> List["service_resource_scope.Job"]:
        pass


class VaultJobsCollection(ResourceCollection):
    """
    [Vault.jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glacier.html#Glacier.Vault.jobs)
    """

    @classmethod
    def all(cls) -> "service_resource_scope.VaultJobsCollection":
        pass

    @classmethod
    def filter(
        cls, limit: str = None, marker: str = None, statuscode: str = None, completed: str = None
    ) -> "service_resource_scope.VaultJobsCollection":
        pass

    @classmethod
    def limit(cls, count: int) -> "service_resource_scope.VaultJobsCollection":
        pass

    @classmethod
    def page_size(cls, count: int) -> "service_resource_scope.VaultJobsCollection":
        pass

    @classmethod
    def pages(cls) -> List["service_resource_scope.Job"]:
        pass


class VaultJobsInProgressCollection(ResourceCollection):
    """
    [Vault.jobs_in_progress documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glacier.html#Glacier.Vault.jobs_in_progress)
    """

    @classmethod
    def all(cls) -> "service_resource_scope.VaultJobsInProgressCollection":
        pass

    @classmethod
    def filter(
        cls, limit: str = None, marker: str = None, statuscode: str = None, completed: str = None
    ) -> "service_resource_scope.VaultJobsInProgressCollection":
        pass

    @classmethod
    def limit(cls, count: int) -> "service_resource_scope.VaultJobsInProgressCollection":
        pass

    @classmethod
    def page_size(cls, count: int) -> "service_resource_scope.VaultJobsInProgressCollection":
        pass

    @classmethod
    def pages(cls) -> List["service_resource_scope.Job"]:
        pass


class VaultMultipartUplaodsCollection(ResourceCollection):
    """
    [Vault.multipart_uplaods documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glacier.html#Glacier.Vault.multipart_uplaods)
    """

    @classmethod
    def all(cls) -> "service_resource_scope.VaultMultipartUplaodsCollection":
        pass

    @classmethod
    def filter(
        cls, marker: str = None, limit: str = None
    ) -> "service_resource_scope.VaultMultipartUplaodsCollection":
        pass

    @classmethod
    def limit(cls, count: int) -> "service_resource_scope.VaultMultipartUplaodsCollection":
        pass

    @classmethod
    def page_size(cls, count: int) -> "service_resource_scope.VaultMultipartUplaodsCollection":
        pass

    @classmethod
    def pages(cls) -> List["service_resource_scope.MultipartUpload"]:
        pass


class VaultMultipartUploadsCollection(ResourceCollection):
    """
    [Vault.multipart_uploads documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glacier.html#Glacier.Vault.multipart_uploads)
    """

    @classmethod
    def all(cls) -> "service_resource_scope.VaultMultipartUploadsCollection":
        pass

    @classmethod
    def filter(
        cls, marker: str = None, limit: str = None
    ) -> "service_resource_scope.VaultMultipartUploadsCollection":
        pass

    @classmethod
    def limit(cls, count: int) -> "service_resource_scope.VaultMultipartUploadsCollection":
        pass

    @classmethod
    def page_size(cls, count: int) -> "service_resource_scope.VaultMultipartUploadsCollection":
        pass

    @classmethod
    def pages(cls) -> List["service_resource_scope.MultipartUpload"]:
        pass


class VaultSucceededJobsCollection(ResourceCollection):
    """
    [Vault.succeeded_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glacier.html#Glacier.Vault.succeeded_jobs)
    """

    @classmethod
    def all(cls) -> "service_resource_scope.VaultSucceededJobsCollection":
        pass

    @classmethod
    def filter(
        cls, limit: str = None, marker: str = None, statuscode: str = None, completed: str = None
    ) -> "service_resource_scope.VaultSucceededJobsCollection":
        pass

    @classmethod
    def limit(cls, count: int) -> "service_resource_scope.VaultSucceededJobsCollection":
        pass

    @classmethod
    def page_size(cls, count: int) -> "service_resource_scope.VaultSucceededJobsCollection":
        pass

    @classmethod
    def pages(cls) -> List["service_resource_scope.Job"]:
        pass
