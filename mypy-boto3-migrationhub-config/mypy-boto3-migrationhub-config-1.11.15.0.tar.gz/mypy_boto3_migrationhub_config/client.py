"""
Main interface for migrationhub-config service client

Usage::

    import boto3
    from mypy_boto3.migrationhub_config import MigrationHubConfigClient

    session = boto3.Session()

    client: MigrationHubConfigClient = boto3.client("migrationhub-config")
    session_client: MigrationHubConfigClient = session.client("migrationhub-config")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from typing import Any, Dict, TYPE_CHECKING
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_migrationhub_config.client as client_scope
else:
    client_scope = object
from mypy_boto3_migrationhub_config.type_defs import (
    ClientCreateHomeRegionControlResponseTypeDef,
    ClientCreateHomeRegionControlTargetTypeDef,
    ClientDescribeHomeRegionControlsResponseTypeDef,
    ClientDescribeHomeRegionControlsTargetTypeDef,
    ClientGetHomeRegionResponseTypeDef,
)


__all__ = ("MigrationHubConfigClient",)


class MigrationHubConfigClient:
    """
    [MigrationHubConfig.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/migrationhub-config.html#MigrationHubConfig.Client)
    """

    exceptions: "client_scope.Exceptions"

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/migrationhub-config.html#MigrationHubConfig.Client.can_paginate)
        """

    def create_home_region_control(
        self,
        HomeRegion: str,
        Target: ClientCreateHomeRegionControlTargetTypeDef,
        DryRun: bool = None,
    ) -> ClientCreateHomeRegionControlResponseTypeDef:
        """
        [Client.create_home_region_control documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/migrationhub-config.html#MigrationHubConfig.Client.create_home_region_control)
        """

    def describe_home_region_controls(
        self,
        ControlId: str = None,
        HomeRegion: str = None,
        Target: ClientDescribeHomeRegionControlsTargetTypeDef = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientDescribeHomeRegionControlsResponseTypeDef:
        """
        [Client.describe_home_region_controls documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/migrationhub-config.html#MigrationHubConfig.Client.describe_home_region_controls)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/migrationhub-config.html#MigrationHubConfig.Client.generate_presigned_url)
        """

    def get_home_region(self, *args: Any, **kwargs: Any) -> ClientGetHomeRegionResponseTypeDef:
        """
        [Client.get_home_region documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/migrationhub-config.html#MigrationHubConfig.Client.get_home_region)
        """


class Exceptions:
    AccessDeniedException: Boto3ClientError
    ClientError: Boto3ClientError
    DryRunOperation: Boto3ClientError
    InternalServerError: Boto3ClientError
    InvalidInputException: Boto3ClientError
    ServiceUnavailableException: Boto3ClientError
