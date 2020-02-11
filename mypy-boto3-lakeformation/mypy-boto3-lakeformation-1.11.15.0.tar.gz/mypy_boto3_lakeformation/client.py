"""
Main interface for lakeformation service client

Usage::

    import boto3
    from mypy_boto3.lakeformation import LakeFormationClient

    session = boto3.Session()

    client: LakeFormationClient = boto3.client("lakeformation")
    session_client: LakeFormationClient = session.client("lakeformation")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Any, Dict, List, TYPE_CHECKING
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_lakeformation.client as client_scope
else:
    client_scope = object
from mypy_boto3_lakeformation.type_defs import (
    ClientBatchGrantPermissionsEntriesTypeDef,
    ClientBatchGrantPermissionsResponseTypeDef,
    ClientBatchRevokePermissionsEntriesTypeDef,
    ClientBatchRevokePermissionsResponseTypeDef,
    ClientDescribeResourceResponseTypeDef,
    ClientGetDataLakeSettingsResponseTypeDef,
    ClientGetEffectivePermissionsForPathResponseTypeDef,
    ClientGrantPermissionsPrincipalTypeDef,
    ClientGrantPermissionsResourceTypeDef,
    ClientListPermissionsPrincipalTypeDef,
    ClientListPermissionsResourceTypeDef,
    ClientListPermissionsResponseTypeDef,
    ClientListResourcesFilterConditionListTypeDef,
    ClientListResourcesResponseTypeDef,
    ClientPutDataLakeSettingsDataLakeSettingsTypeDef,
    ClientRevokePermissionsPrincipalTypeDef,
    ClientRevokePermissionsResourceTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("LakeFormationClient",)


class LakeFormationClient:
    """
    [LakeFormation.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lakeformation.html#LakeFormation.Client)
    """

    exceptions: "client_scope.Exceptions"

    def batch_grant_permissions(
        self, Entries: List[ClientBatchGrantPermissionsEntriesTypeDef], CatalogId: str = None
    ) -> ClientBatchGrantPermissionsResponseTypeDef:
        """
        [Client.batch_grant_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lakeformation.html#LakeFormation.Client.batch_grant_permissions)
        """

    def batch_revoke_permissions(
        self, Entries: List[ClientBatchRevokePermissionsEntriesTypeDef], CatalogId: str = None
    ) -> ClientBatchRevokePermissionsResponseTypeDef:
        """
        [Client.batch_revoke_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lakeformation.html#LakeFormation.Client.batch_revoke_permissions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lakeformation.html#LakeFormation.Client.can_paginate)
        """

    def deregister_resource(self, ResourceArn: str) -> Dict[str, Any]:
        """
        [Client.deregister_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lakeformation.html#LakeFormation.Client.deregister_resource)
        """

    def describe_resource(self, ResourceArn: str) -> ClientDescribeResourceResponseTypeDef:
        """
        [Client.describe_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lakeformation.html#LakeFormation.Client.describe_resource)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lakeformation.html#LakeFormation.Client.generate_presigned_url)
        """

    def get_data_lake_settings(
        self, CatalogId: str = None
    ) -> ClientGetDataLakeSettingsResponseTypeDef:
        """
        [Client.get_data_lake_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lakeformation.html#LakeFormation.Client.get_data_lake_settings)
        """

    def get_effective_permissions_for_path(
        self, ResourceArn: str, CatalogId: str = None, NextToken: str = None, MaxResults: int = None
    ) -> ClientGetEffectivePermissionsForPathResponseTypeDef:
        """
        [Client.get_effective_permissions_for_path documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lakeformation.html#LakeFormation.Client.get_effective_permissions_for_path)
        """

    def grant_permissions(
        self,
        Principal: ClientGrantPermissionsPrincipalTypeDef,
        Resource: ClientGrantPermissionsResourceTypeDef,
        Permissions: List[
            Literal[
                "ALL",
                "SELECT",
                "ALTER",
                "DROP",
                "DELETE",
                "INSERT",
                "CREATE_DATABASE",
                "CREATE_TABLE",
                "DATA_LOCATION_ACCESS",
            ]
        ],
        CatalogId: str = None,
        PermissionsWithGrantOption: List[
            Literal[
                "ALL",
                "SELECT",
                "ALTER",
                "DROP",
                "DELETE",
                "INSERT",
                "CREATE_DATABASE",
                "CREATE_TABLE",
                "DATA_LOCATION_ACCESS",
            ]
        ] = None,
    ) -> Dict[str, Any]:
        """
        [Client.grant_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lakeformation.html#LakeFormation.Client.grant_permissions)
        """

    def list_permissions(
        self,
        CatalogId: str = None,
        Principal: ClientListPermissionsPrincipalTypeDef = None,
        ResourceType: Literal["CATALOG", "DATABASE", "TABLE", "DATA_LOCATION"] = None,
        Resource: ClientListPermissionsResourceTypeDef = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientListPermissionsResponseTypeDef:
        """
        [Client.list_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lakeformation.html#LakeFormation.Client.list_permissions)
        """

    def list_resources(
        self,
        FilterConditionList: List[ClientListResourcesFilterConditionListTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientListResourcesResponseTypeDef:
        """
        [Client.list_resources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lakeformation.html#LakeFormation.Client.list_resources)
        """

    def put_data_lake_settings(
        self,
        DataLakeSettings: ClientPutDataLakeSettingsDataLakeSettingsTypeDef,
        CatalogId: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.put_data_lake_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lakeformation.html#LakeFormation.Client.put_data_lake_settings)
        """

    def register_resource(
        self, ResourceArn: str, UseServiceLinkedRole: bool = None, RoleArn: str = None
    ) -> Dict[str, Any]:
        """
        [Client.register_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lakeformation.html#LakeFormation.Client.register_resource)
        """

    def revoke_permissions(
        self,
        Principal: ClientRevokePermissionsPrincipalTypeDef,
        Resource: ClientRevokePermissionsResourceTypeDef,
        Permissions: List[
            Literal[
                "ALL",
                "SELECT",
                "ALTER",
                "DROP",
                "DELETE",
                "INSERT",
                "CREATE_DATABASE",
                "CREATE_TABLE",
                "DATA_LOCATION_ACCESS",
            ]
        ],
        CatalogId: str = None,
        PermissionsWithGrantOption: List[
            Literal[
                "ALL",
                "SELECT",
                "ALTER",
                "DROP",
                "DELETE",
                "INSERT",
                "CREATE_DATABASE",
                "CREATE_TABLE",
                "DATA_LOCATION_ACCESS",
            ]
        ] = None,
    ) -> Dict[str, Any]:
        """
        [Client.revoke_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lakeformation.html#LakeFormation.Client.revoke_permissions)
        """

    def update_resource(self, RoleArn: str, ResourceArn: str) -> Dict[str, Any]:
        """
        [Client.update_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lakeformation.html#LakeFormation.Client.update_resource)
        """


class Exceptions:
    AlreadyExistsException: Boto3ClientError
    ClientError: Boto3ClientError
    ConcurrentModificationException: Boto3ClientError
    EntityNotFoundException: Boto3ClientError
    InternalServiceException: Boto3ClientError
    InvalidInputException: Boto3ClientError
    OperationTimeoutException: Boto3ClientError
