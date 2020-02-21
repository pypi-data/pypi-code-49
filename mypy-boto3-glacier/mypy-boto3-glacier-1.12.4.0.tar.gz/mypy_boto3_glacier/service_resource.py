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
from typing import Any, Dict, IO, List, TYPE_CHECKING, Type, TypeVar, Union
from boto3.resources.base import ServiceResource as Boto3ServiceResource
from boto3.resources.collection import ResourceCollection
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

_ServiceResourceVaultsCollectionType = TypeVar(
    "_ServiceResourceVaultsCollectionType", bound="ServiceResourceVaultsCollection"
)


class ServiceResourceVaultsCollection(ResourceCollection):
    """
    [ServiceResource.vaults documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.4/reference/services/glacier.html#Glacier.ServiceResource.vaults)
    """

    @classmethod
    def all(
        cls: Type[_ServiceResourceVaultsCollectionType],
    ) -> Type[_ServiceResourceVaultsCollectionType]:
        pass

    @classmethod
    def filter(
        cls: Type[_ServiceResourceVaultsCollectionType], marker: str = None, limit: str = None
    ) -> Type[_ServiceResourceVaultsCollectionType]:
        pass

    @classmethod
    def limit(
        cls: Type[_ServiceResourceVaultsCollectionType], count: int
    ) -> Type[_ServiceResourceVaultsCollectionType]:
        pass

    @classmethod
    def page_size(
        cls: Type[_ServiceResourceVaultsCollectionType], count: int
    ) -> Type[_ServiceResourceVaultsCollectionType]:
        pass

    @classmethod
    def pages(cls: Type[_ServiceResourceVaultsCollectionType]) -> List["Vault"]:
        pass


_AccountVaultsCollectionType = TypeVar(
    "_AccountVaultsCollectionType", bound="AccountVaultsCollection"
)


class AccountVaultsCollection(ResourceCollection):
    """
    [Account.vaults documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.4/reference/services/glacier.html#Glacier.Account.vaults)
    """

    @classmethod
    def all(cls: Type[_AccountVaultsCollectionType]) -> Type[_AccountVaultsCollectionType]:
        pass

    @classmethod
    def filter(
        cls: Type[_AccountVaultsCollectionType], marker: str = None, limit: str = None
    ) -> Type[_AccountVaultsCollectionType]:
        pass

    @classmethod
    def limit(
        cls: Type[_AccountVaultsCollectionType], count: int
    ) -> Type[_AccountVaultsCollectionType]:
        pass

    @classmethod
    def page_size(
        cls: Type[_AccountVaultsCollectionType], count: int
    ) -> Type[_AccountVaultsCollectionType]:
        pass

    @classmethod
    def pages(cls: Type[_AccountVaultsCollectionType]) -> List["Vault"]:
        pass


_VaultCompletedJobsCollectionType = TypeVar(
    "_VaultCompletedJobsCollectionType", bound="VaultCompletedJobsCollection"
)


class VaultCompletedJobsCollection(ResourceCollection):
    """
    [Vault.completed_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.4/reference/services/glacier.html#Glacier.Vault.completed_jobs)
    """

    @classmethod
    def all(
        cls: Type[_VaultCompletedJobsCollectionType],
    ) -> Type[_VaultCompletedJobsCollectionType]:
        pass

    @classmethod
    def filter(
        cls: Type[_VaultCompletedJobsCollectionType],
        limit: str = None,
        marker: str = None,
        statuscode: str = None,
        completed: str = None,
    ) -> Type[_VaultCompletedJobsCollectionType]:
        pass

    @classmethod
    def limit(
        cls: Type[_VaultCompletedJobsCollectionType], count: int
    ) -> Type[_VaultCompletedJobsCollectionType]:
        pass

    @classmethod
    def page_size(
        cls: Type[_VaultCompletedJobsCollectionType], count: int
    ) -> Type[_VaultCompletedJobsCollectionType]:
        pass

    @classmethod
    def pages(cls: Type[_VaultCompletedJobsCollectionType]) -> List["Job"]:
        pass


_VaultFailedJobsCollectionType = TypeVar(
    "_VaultFailedJobsCollectionType", bound="VaultFailedJobsCollection"
)


class VaultFailedJobsCollection(ResourceCollection):
    """
    [Vault.failed_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.4/reference/services/glacier.html#Glacier.Vault.failed_jobs)
    """

    @classmethod
    def all(cls: Type[_VaultFailedJobsCollectionType]) -> Type[_VaultFailedJobsCollectionType]:
        pass

    @classmethod
    def filter(
        cls: Type[_VaultFailedJobsCollectionType],
        limit: str = None,
        marker: str = None,
        statuscode: str = None,
        completed: str = None,
    ) -> Type[_VaultFailedJobsCollectionType]:
        pass

    @classmethod
    def limit(
        cls: Type[_VaultFailedJobsCollectionType], count: int
    ) -> Type[_VaultFailedJobsCollectionType]:
        pass

    @classmethod
    def page_size(
        cls: Type[_VaultFailedJobsCollectionType], count: int
    ) -> Type[_VaultFailedJobsCollectionType]:
        pass

    @classmethod
    def pages(cls: Type[_VaultFailedJobsCollectionType]) -> List["Job"]:
        pass


_VaultJobsCollectionType = TypeVar("_VaultJobsCollectionType", bound="VaultJobsCollection")


class VaultJobsCollection(ResourceCollection):
    """
    [Vault.jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.4/reference/services/glacier.html#Glacier.Vault.jobs)
    """

    @classmethod
    def all(cls: Type[_VaultJobsCollectionType]) -> Type[_VaultJobsCollectionType]:
        pass

    @classmethod
    def filter(
        cls: Type[_VaultJobsCollectionType],
        limit: str = None,
        marker: str = None,
        statuscode: str = None,
        completed: str = None,
    ) -> Type[_VaultJobsCollectionType]:
        pass

    @classmethod
    def limit(cls: Type[_VaultJobsCollectionType], count: int) -> Type[_VaultJobsCollectionType]:
        pass

    @classmethod
    def page_size(
        cls: Type[_VaultJobsCollectionType], count: int
    ) -> Type[_VaultJobsCollectionType]:
        pass

    @classmethod
    def pages(cls: Type[_VaultJobsCollectionType]) -> List["Job"]:
        pass


_VaultJobsInProgressCollectionType = TypeVar(
    "_VaultJobsInProgressCollectionType", bound="VaultJobsInProgressCollection"
)


class VaultJobsInProgressCollection(ResourceCollection):
    """
    [Vault.jobs_in_progress documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.4/reference/services/glacier.html#Glacier.Vault.jobs_in_progress)
    """

    @classmethod
    def all(
        cls: Type[_VaultJobsInProgressCollectionType],
    ) -> Type[_VaultJobsInProgressCollectionType]:
        pass

    @classmethod
    def filter(
        cls: Type[_VaultJobsInProgressCollectionType],
        limit: str = None,
        marker: str = None,
        statuscode: str = None,
        completed: str = None,
    ) -> Type[_VaultJobsInProgressCollectionType]:
        pass

    @classmethod
    def limit(
        cls: Type[_VaultJobsInProgressCollectionType], count: int
    ) -> Type[_VaultJobsInProgressCollectionType]:
        pass

    @classmethod
    def page_size(
        cls: Type[_VaultJobsInProgressCollectionType], count: int
    ) -> Type[_VaultJobsInProgressCollectionType]:
        pass

    @classmethod
    def pages(cls: Type[_VaultJobsInProgressCollectionType]) -> List["Job"]:
        pass


_VaultMultipartUplaodsCollectionType = TypeVar(
    "_VaultMultipartUplaodsCollectionType", bound="VaultMultipartUplaodsCollection"
)


class VaultMultipartUplaodsCollection(ResourceCollection):
    """
    [Vault.multipart_uplaods documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.4/reference/services/glacier.html#Glacier.Vault.multipart_uplaods)
    """

    @classmethod
    def all(
        cls: Type[_VaultMultipartUplaodsCollectionType],
    ) -> Type[_VaultMultipartUplaodsCollectionType]:
        pass

    @classmethod
    def filter(
        cls: Type[_VaultMultipartUplaodsCollectionType], marker: str = None, limit: str = None
    ) -> Type[_VaultMultipartUplaodsCollectionType]:
        pass

    @classmethod
    def limit(
        cls: Type[_VaultMultipartUplaodsCollectionType], count: int
    ) -> Type[_VaultMultipartUplaodsCollectionType]:
        pass

    @classmethod
    def page_size(
        cls: Type[_VaultMultipartUplaodsCollectionType], count: int
    ) -> Type[_VaultMultipartUplaodsCollectionType]:
        pass

    @classmethod
    def pages(cls: Type[_VaultMultipartUplaodsCollectionType]) -> List["MultipartUpload"]:
        pass


_VaultMultipartUploadsCollectionType = TypeVar(
    "_VaultMultipartUploadsCollectionType", bound="VaultMultipartUploadsCollection"
)


class VaultMultipartUploadsCollection(ResourceCollection):
    """
    [Vault.multipart_uploads documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.4/reference/services/glacier.html#Glacier.Vault.multipart_uploads)
    """

    @classmethod
    def all(
        cls: Type[_VaultMultipartUploadsCollectionType],
    ) -> Type[_VaultMultipartUploadsCollectionType]:
        pass

    @classmethod
    def filter(
        cls: Type[_VaultMultipartUploadsCollectionType], marker: str = None, limit: str = None
    ) -> Type[_VaultMultipartUploadsCollectionType]:
        pass

    @classmethod
    def limit(
        cls: Type[_VaultMultipartUploadsCollectionType], count: int
    ) -> Type[_VaultMultipartUploadsCollectionType]:
        pass

    @classmethod
    def page_size(
        cls: Type[_VaultMultipartUploadsCollectionType], count: int
    ) -> Type[_VaultMultipartUploadsCollectionType]:
        pass

    @classmethod
    def pages(cls: Type[_VaultMultipartUploadsCollectionType]) -> List["MultipartUpload"]:
        pass


_VaultSucceededJobsCollectionType = TypeVar(
    "_VaultSucceededJobsCollectionType", bound="VaultSucceededJobsCollection"
)


class VaultSucceededJobsCollection(ResourceCollection):
    """
    [Vault.succeeded_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.4/reference/services/glacier.html#Glacier.Vault.succeeded_jobs)
    """

    @classmethod
    def all(
        cls: Type[_VaultSucceededJobsCollectionType],
    ) -> Type[_VaultSucceededJobsCollectionType]:
        pass

    @classmethod
    def filter(
        cls: Type[_VaultSucceededJobsCollectionType],
        limit: str = None,
        marker: str = None,
        statuscode: str = None,
        completed: str = None,
    ) -> Type[_VaultSucceededJobsCollectionType]:
        pass

    @classmethod
    def limit(
        cls: Type[_VaultSucceededJobsCollectionType], count: int
    ) -> Type[_VaultSucceededJobsCollectionType]:
        pass

    @classmethod
    def page_size(
        cls: Type[_VaultSucceededJobsCollectionType], count: int
    ) -> Type[_VaultSucceededJobsCollectionType]:
        pass

    @classmethod
    def pages(cls: Type[_VaultSucceededJobsCollectionType]) -> List["Job"]:
        pass


_ArchiveType = TypeVar("_ArchiveType", bound="Archive")


class Archive(Boto3ServiceResource):
    """
    [Archive documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.4/reference/services/glacier.html#Glacier.ServiceResource.Archive)
    """

    account_id: str
    vault_name: str
    id: str

    def delete(self) -> None:
        """
        [Archive.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.4/reference/services/glacier.html#Glacier.Archive.delete)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Archive.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.4/reference/services/glacier.html#Glacier.Archive.get_available_subresources)
        """

    def initiate_archive_retrieval(
        self, jobParameters: JobParametersTypeDef = None
    ) -> InitiateJobOutputTypeDef:
        """
        [Archive.initiate_archive_retrieval documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.4/reference/services/glacier.html#Glacier.Archive.initiate_archive_retrieval)
        """


_Archive = Archive


_JobType = TypeVar("_JobType", bound="Job")


class Job(Boto3ServiceResource):
    """
    [Job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.4/reference/services/glacier.html#Glacier.ServiceResource.Job)
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
        [Job.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.4/reference/services/glacier.html#Glacier.Job.get_available_subresources)
        """

    def get_output(self, range: str = None) -> GetJobOutputOutputTypeDef:
        """
        [Job.get_output documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.4/reference/services/glacier.html#Glacier.Job.get_output)
        """

    def load(self) -> None:
        """
        [Job.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.4/reference/services/glacier.html#Glacier.Job.load)
        """

    def reload(self) -> None:
        """
        [Job.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.4/reference/services/glacier.html#Glacier.Job.reload)
        """


_Job = Job


_MultipartUploadType = TypeVar("_MultipartUploadType", bound="MultipartUpload")


class MultipartUpload(Boto3ServiceResource):
    """
    [MultipartUpload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.4/reference/services/glacier.html#Glacier.ServiceResource.MultipartUpload)
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
        [MultipartUpload.abort documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.4/reference/services/glacier.html#Glacier.MultipartUpload.abort)
        """

    def complete(
        self, archiveSize: str = None, checksum: str = None
    ) -> ArchiveCreationOutputTypeDef:
        """
        [MultipartUpload.complete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.4/reference/services/glacier.html#Glacier.MultipartUpload.complete)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [MultipartUpload.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.4/reference/services/glacier.html#Glacier.MultipartUpload.get_available_subresources)
        """

    def parts(self, marker: str = None, limit: str = None) -> ListPartsOutputTypeDef:
        """
        [MultipartUpload.parts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.4/reference/services/glacier.html#Glacier.MultipartUpload.parts)
        """

    def upload_part(
        self, checksum: str = None, range: str = None, body: Union[bytes, IO] = None
    ) -> UploadMultipartPartOutputTypeDef:
        """
        [MultipartUpload.upload_part documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.4/reference/services/glacier.html#Glacier.MultipartUpload.upload_part)
        """


_MultipartUpload = MultipartUpload


_NotificationType = TypeVar("_NotificationType", bound="Notification")


class Notification(Boto3ServiceResource):
    """
    [Notification documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.4/reference/services/glacier.html#Glacier.ServiceResource.Notification)
    """

    sns_topic: str
    events: List[Any]
    account_id: str
    vault_name: str

    def delete(self) -> None:
        """
        [Notification.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.4/reference/services/glacier.html#Glacier.Notification.delete)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Notification.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.4/reference/services/glacier.html#Glacier.Notification.get_available_subresources)
        """

    def load(self) -> None:
        """
        [Notification.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.4/reference/services/glacier.html#Glacier.Notification.load)
        """

    def reload(self) -> None:
        """
        [Notification.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.4/reference/services/glacier.html#Glacier.Notification.reload)
        """

    def set(self, vaultNotificationConfig: VaultNotificationConfigTypeDef = None) -> None:
        """
        [Notification.set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.4/reference/services/glacier.html#Glacier.Notification.set)
        """


_Notification = Notification


_VaultType = TypeVar("_VaultType", bound="Vault")


class Vault(Boto3ServiceResource):
    """
    [Vault documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.4/reference/services/glacier.html#Glacier.ServiceResource.Vault)
    """

    vault_arn: str
    vault_name: str
    creation_date: str
    last_inventory_date: str
    number_of_archives: int
    size_in_bytes: int
    account_id: str
    name: str
    completed_jobs: VaultCompletedJobsCollection
    failed_jobs: VaultFailedJobsCollection
    jobs: VaultJobsCollection
    jobs_in_progress: VaultJobsInProgressCollection
    multipart_uplaods: VaultMultipartUplaodsCollection
    multipart_uploads: VaultMultipartUploadsCollection
    succeeded_jobs: VaultSucceededJobsCollection

    def create(self) -> CreateVaultOutputTypeDef:
        """
        [Vault.create documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.4/reference/services/glacier.html#Glacier.Vault.create)
        """

    def delete(self) -> None:
        """
        [Vault.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.4/reference/services/glacier.html#Glacier.Vault.delete)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Vault.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.4/reference/services/glacier.html#Glacier.Vault.get_available_subresources)
        """

    def initiate_inventory_retrieval(
        self, jobParameters: JobParametersTypeDef = None
    ) -> InitiateJobOutputTypeDef:
        """
        [Vault.initiate_inventory_retrieval documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.4/reference/services/glacier.html#Glacier.Vault.initiate_inventory_retrieval)
        """

    def initiate_multipart_upload(
        self, archiveDescription: str = None, partSize: str = None
    ) -> InitiateMultipartUploadOutputTypeDef:
        """
        [Vault.initiate_multipart_upload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.4/reference/services/glacier.html#Glacier.Vault.initiate_multipart_upload)
        """

    def load(self) -> None:
        """
        [Vault.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.4/reference/services/glacier.html#Glacier.Vault.load)
        """

    def reload(self) -> None:
        """
        [Vault.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.4/reference/services/glacier.html#Glacier.Vault.reload)
        """

    def upload_archive(
        self, archiveDescription: str = None, checksum: str = None, body: Union[bytes, IO] = None
    ) -> ArchiveCreationOutputTypeDef:
        """
        [Vault.upload_archive documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.4/reference/services/glacier.html#Glacier.Vault.upload_archive)
        """


_Vault = Vault


_AccountType = TypeVar("_AccountType", bound="Account")


class Account(Boto3ServiceResource):
    """
    [Account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.4/reference/services/glacier.html#Glacier.ServiceResource.Account)
    """

    id: str
    vaults: AccountVaultsCollection

    def create_vault(self, vaultName: str) -> CreateVaultOutputTypeDef:
        """
        [Account.create_vault documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.4/reference/services/glacier.html#Glacier.Account.create_vault)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Account.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.4/reference/services/glacier.html#Glacier.Account.get_available_subresources)
        """


_Account = Account


class GlacierServiceResource(Boto3ServiceResource):
    """
    [Glacier.ServiceResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.4/reference/services/glacier.html#Glacier.ServiceResource)
    """

    vaults: ServiceResourceVaultsCollection

    def Account(self, id: str) -> _Account:
        """
        [ServiceResource.Account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.4/reference/services/glacier.html#Glacier.ServiceResource.Account)
        """

    def Archive(self, account_id: str, vault_name: str, id: str) -> _Archive:
        """
        [ServiceResource.Archive documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.4/reference/services/glacier.html#Glacier.ServiceResource.Archive)
        """

    def Job(self, account_id: str, vault_name: str, id: str) -> _Job:
        """
        [ServiceResource.Job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.4/reference/services/glacier.html#Glacier.ServiceResource.Job)
        """

    def MultipartUpload(self, account_id: str, vault_name: str, id: str) -> _MultipartUpload:
        """
        [ServiceResource.MultipartUpload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.4/reference/services/glacier.html#Glacier.ServiceResource.MultipartUpload)
        """

    def Notification(self, account_id: str, vault_name: str) -> _Notification:
        """
        [ServiceResource.Notification documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.4/reference/services/glacier.html#Glacier.ServiceResource.Notification)
        """

    def Vault(self, account_id: str, name: str) -> _Vault:
        """
        [ServiceResource.Vault documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.4/reference/services/glacier.html#Glacier.ServiceResource.Vault)
        """

    def create_vault(self, accountId: str, vaultName: str) -> CreateVaultOutputTypeDef:
        """
        [ServiceResource.create_vault documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.4/reference/services/glacier.html#Glacier.ServiceResource.create_vault)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [ServiceResource.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.4/reference/services/glacier.html#Glacier.ServiceResource.get_available_subresources)
        """
