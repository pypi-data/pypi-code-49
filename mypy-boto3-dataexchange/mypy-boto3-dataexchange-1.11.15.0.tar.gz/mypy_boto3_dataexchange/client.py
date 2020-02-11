"""
Main interface for dataexchange service client

Usage::

    import boto3
    from mypy_boto3.dataexchange import DataExchangeClient

    session = boto3.Session()

    client: DataExchangeClient = boto3.client("dataexchange")
    session_client: DataExchangeClient = session.client("dataexchange")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_dataexchange.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_dataexchange.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_dataexchange.type_defs import (
    ClientCreateDataSetResponseTypeDef,
    ClientCreateJobDetailsTypeDef,
    ClientCreateJobResponseTypeDef,
    ClientCreateRevisionResponseTypeDef,
    ClientGetAssetResponseTypeDef,
    ClientGetDataSetResponseTypeDef,
    ClientGetJobResponseTypeDef,
    ClientGetRevisionResponseTypeDef,
    ClientListDataSetRevisionsResponseTypeDef,
    ClientListDataSetsResponseTypeDef,
    ClientListJobsResponseTypeDef,
    ClientListRevisionAssetsResponseTypeDef,
    ClientListTagsForResourceResponseTypeDef,
    ClientUpdateAssetResponseTypeDef,
    ClientUpdateDataSetResponseTypeDef,
    ClientUpdateRevisionResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("DataExchangeClient",)


class DataExchangeClient:
    """
    [DataExchange.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dataexchange.html#DataExchange.Client)
    """

    exceptions: "client_scope.Exceptions"

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dataexchange.html#DataExchange.Client.can_paginate)
        """

    def cancel_job(self, JobId: str) -> None:
        """
        [Client.cancel_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dataexchange.html#DataExchange.Client.cancel_job)
        """

    def create_data_set(
        self, AssetType: str, Description: str, Name: str, Tags: Dict[str, str] = None
    ) -> ClientCreateDataSetResponseTypeDef:
        """
        [Client.create_data_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dataexchange.html#DataExchange.Client.create_data_set)
        """

    def create_job(
        self,
        Details: ClientCreateJobDetailsTypeDef,
        Type: Literal[
            "IMPORT_ASSETS_FROM_S3",
            "IMPORT_ASSET_FROM_SIGNED_URL",
            "EXPORT_ASSETS_TO_S3",
            "EXPORT_ASSET_TO_SIGNED_URL",
        ],
    ) -> ClientCreateJobResponseTypeDef:
        """
        [Client.create_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dataexchange.html#DataExchange.Client.create_job)
        """

    def create_revision(
        self, DataSetId: str, Comment: str = None, Tags: Dict[str, str] = None
    ) -> ClientCreateRevisionResponseTypeDef:
        """
        [Client.create_revision documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dataexchange.html#DataExchange.Client.create_revision)
        """

    def delete_asset(self, AssetId: str, DataSetId: str, RevisionId: str) -> None:
        """
        [Client.delete_asset documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dataexchange.html#DataExchange.Client.delete_asset)
        """

    def delete_data_set(self, DataSetId: str) -> None:
        """
        [Client.delete_data_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dataexchange.html#DataExchange.Client.delete_data_set)
        """

    def delete_revision(self, DataSetId: str, RevisionId: str) -> None:
        """
        [Client.delete_revision documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dataexchange.html#DataExchange.Client.delete_revision)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dataexchange.html#DataExchange.Client.generate_presigned_url)
        """

    def get_asset(
        self, AssetId: str, DataSetId: str, RevisionId: str
    ) -> ClientGetAssetResponseTypeDef:
        """
        [Client.get_asset documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dataexchange.html#DataExchange.Client.get_asset)
        """

    def get_data_set(self, DataSetId: str) -> ClientGetDataSetResponseTypeDef:
        """
        [Client.get_data_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dataexchange.html#DataExchange.Client.get_data_set)
        """

    def get_job(self, JobId: str) -> ClientGetJobResponseTypeDef:
        """
        [Client.get_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dataexchange.html#DataExchange.Client.get_job)
        """

    def get_revision(self, DataSetId: str, RevisionId: str) -> ClientGetRevisionResponseTypeDef:
        """
        [Client.get_revision documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dataexchange.html#DataExchange.Client.get_revision)
        """

    def list_data_set_revisions(
        self, DataSetId: str, MaxResults: int = None, NextToken: str = None
    ) -> ClientListDataSetRevisionsResponseTypeDef:
        """
        [Client.list_data_set_revisions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dataexchange.html#DataExchange.Client.list_data_set_revisions)
        """

    def list_data_sets(
        self, MaxResults: int = None, NextToken: str = None, Origin: str = None
    ) -> ClientListDataSetsResponseTypeDef:
        """
        [Client.list_data_sets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dataexchange.html#DataExchange.Client.list_data_sets)
        """

    def list_jobs(
        self,
        DataSetId: str = None,
        MaxResults: int = None,
        NextToken: str = None,
        RevisionId: str = None,
    ) -> ClientListJobsResponseTypeDef:
        """
        [Client.list_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dataexchange.html#DataExchange.Client.list_jobs)
        """

    def list_revision_assets(
        self, DataSetId: str, RevisionId: str, MaxResults: int = None, NextToken: str = None
    ) -> ClientListRevisionAssetsResponseTypeDef:
        """
        [Client.list_revision_assets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dataexchange.html#DataExchange.Client.list_revision_assets)
        """

    def list_tags_for_resource(self, ResourceArn: str) -> ClientListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dataexchange.html#DataExchange.Client.list_tags_for_resource)
        """

    def start_job(self, JobId: str) -> Dict[str, Any]:
        """
        [Client.start_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dataexchange.html#DataExchange.Client.start_job)
        """

    def tag_resource(self, ResourceArn: str, Tags: Dict[str, str]) -> None:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dataexchange.html#DataExchange.Client.tag_resource)
        """

    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> None:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dataexchange.html#DataExchange.Client.untag_resource)
        """

    def update_asset(
        self, AssetId: str, DataSetId: str, Name: str, RevisionId: str
    ) -> ClientUpdateAssetResponseTypeDef:
        """
        [Client.update_asset documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dataexchange.html#DataExchange.Client.update_asset)
        """

    def update_data_set(
        self, DataSetId: str, Description: str = None, Name: str = None
    ) -> ClientUpdateDataSetResponseTypeDef:
        """
        [Client.update_data_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dataexchange.html#DataExchange.Client.update_data_set)
        """

    def update_revision(
        self, DataSetId: str, RevisionId: str, Comment: str = None, Finalized: bool = None
    ) -> ClientUpdateRevisionResponseTypeDef:
        """
        [Client.update_revision documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dataexchange.html#DataExchange.Client.update_revision)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_data_set_revisions"]
    ) -> "paginator_scope.ListDataSetRevisionsPaginator":
        """
        [Paginator.ListDataSetRevisions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dataexchange.html#DataExchange.Paginator.ListDataSetRevisions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_data_sets"]
    ) -> "paginator_scope.ListDataSetsPaginator":
        """
        [Paginator.ListDataSets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dataexchange.html#DataExchange.Paginator.ListDataSets)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_jobs"]
    ) -> "paginator_scope.ListJobsPaginator":
        """
        [Paginator.ListJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dataexchange.html#DataExchange.Paginator.ListJobs)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_revision_assets"]
    ) -> "paginator_scope.ListRevisionAssetsPaginator":
        """
        [Paginator.ListRevisionAssets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dataexchange.html#DataExchange.Paginator.ListRevisionAssets)
        """


class Exceptions:
    AccessDeniedException: Boto3ClientError
    ClientError: Boto3ClientError
    ConflictException: Boto3ClientError
    InternalServerException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    ServiceLimitExceededException: Boto3ClientError
    ThrottlingException: Boto3ClientError
    ValidationException: Boto3ClientError
