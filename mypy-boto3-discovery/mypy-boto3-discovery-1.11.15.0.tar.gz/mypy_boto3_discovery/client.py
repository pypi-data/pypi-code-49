"""
Main interface for discovery service client

Usage::

    import boto3
    from mypy_boto3.discovery import ApplicationDiscoveryServiceClient

    session = boto3.Session()

    client: ApplicationDiscoveryServiceClient = boto3.client("discovery")
    session_client: ApplicationDiscoveryServiceClient = session.client("discovery")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from datetime import datetime
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_discovery.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_discovery.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_discovery.type_defs import (
    ClientBatchDeleteImportDataResponseTypeDef,
    ClientCreateApplicationResponseTypeDef,
    ClientCreateTagsTagsTypeDef,
    ClientDeleteTagsTagsTypeDef,
    ClientDescribeAgentsFiltersTypeDef,
    ClientDescribeAgentsResponseTypeDef,
    ClientDescribeConfigurationsResponseTypeDef,
    ClientDescribeContinuousExportsResponseTypeDef,
    ClientDescribeExportConfigurationsResponseTypeDef,
    ClientDescribeExportTasksFiltersTypeDef,
    ClientDescribeExportTasksResponseTypeDef,
    ClientDescribeImportTasksFiltersTypeDef,
    ClientDescribeImportTasksResponseTypeDef,
    ClientDescribeTagsFiltersTypeDef,
    ClientDescribeTagsResponseTypeDef,
    ClientExportConfigurationsResponseTypeDef,
    ClientGetDiscoverySummaryResponseTypeDef,
    ClientListConfigurationsFiltersTypeDef,
    ClientListConfigurationsOrderByTypeDef,
    ClientListConfigurationsResponseTypeDef,
    ClientListServerNeighborsResponseTypeDef,
    ClientStartContinuousExportResponseTypeDef,
    ClientStartDataCollectionByAgentIdsResponseTypeDef,
    ClientStartExportTaskFiltersTypeDef,
    ClientStartExportTaskResponseTypeDef,
    ClientStartImportTaskResponseTypeDef,
    ClientStopContinuousExportResponseTypeDef,
    ClientStopDataCollectionByAgentIdsResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ApplicationDiscoveryServiceClient",)


class ApplicationDiscoveryServiceClient:
    """
    [ApplicationDiscoveryService.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/discovery.html#ApplicationDiscoveryService.Client)
    """

    exceptions: "client_scope.Exceptions"

    def associate_configuration_items_to_application(
        self, applicationConfigurationId: str, configurationIds: List[str]
    ) -> Dict[str, Any]:
        """
        [Client.associate_configuration_items_to_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/discovery.html#ApplicationDiscoveryService.Client.associate_configuration_items_to_application)
        """

    def batch_delete_import_data(
        self, importTaskIds: List[str]
    ) -> ClientBatchDeleteImportDataResponseTypeDef:
        """
        [Client.batch_delete_import_data documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/discovery.html#ApplicationDiscoveryService.Client.batch_delete_import_data)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/discovery.html#ApplicationDiscoveryService.Client.can_paginate)
        """

    def create_application(
        self, name: str, description: str = None
    ) -> ClientCreateApplicationResponseTypeDef:
        """
        [Client.create_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/discovery.html#ApplicationDiscoveryService.Client.create_application)
        """

    def create_tags(
        self, configurationIds: List[str], tags: List[ClientCreateTagsTagsTypeDef]
    ) -> Dict[str, Any]:
        """
        [Client.create_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/discovery.html#ApplicationDiscoveryService.Client.create_tags)
        """

    def delete_applications(self, configurationIds: List[str]) -> Dict[str, Any]:
        """
        [Client.delete_applications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/discovery.html#ApplicationDiscoveryService.Client.delete_applications)
        """

    def delete_tags(
        self, configurationIds: List[str], tags: List[ClientDeleteTagsTagsTypeDef] = None
    ) -> Dict[str, Any]:
        """
        [Client.delete_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/discovery.html#ApplicationDiscoveryService.Client.delete_tags)
        """

    def describe_agents(
        self,
        agentIds: List[str] = None,
        filters: List[ClientDescribeAgentsFiltersTypeDef] = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> ClientDescribeAgentsResponseTypeDef:
        """
        [Client.describe_agents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/discovery.html#ApplicationDiscoveryService.Client.describe_agents)
        """

    def describe_configurations(
        self, configurationIds: List[str]
    ) -> ClientDescribeConfigurationsResponseTypeDef:
        """
        [Client.describe_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/discovery.html#ApplicationDiscoveryService.Client.describe_configurations)
        """

    def describe_continuous_exports(
        self, exportIds: List[str] = None, maxResults: int = None, nextToken: str = None
    ) -> ClientDescribeContinuousExportsResponseTypeDef:
        """
        [Client.describe_continuous_exports documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/discovery.html#ApplicationDiscoveryService.Client.describe_continuous_exports)
        """

    def describe_export_configurations(
        self, exportIds: List[str] = None, maxResults: int = None, nextToken: str = None
    ) -> ClientDescribeExportConfigurationsResponseTypeDef:
        """
        [Client.describe_export_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/discovery.html#ApplicationDiscoveryService.Client.describe_export_configurations)
        """

    def describe_export_tasks(
        self,
        exportIds: List[str] = None,
        filters: List[ClientDescribeExportTasksFiltersTypeDef] = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> ClientDescribeExportTasksResponseTypeDef:
        """
        [Client.describe_export_tasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/discovery.html#ApplicationDiscoveryService.Client.describe_export_tasks)
        """

    def describe_import_tasks(
        self,
        filters: List[ClientDescribeImportTasksFiltersTypeDef] = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> ClientDescribeImportTasksResponseTypeDef:
        """
        [Client.describe_import_tasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/discovery.html#ApplicationDiscoveryService.Client.describe_import_tasks)
        """

    def describe_tags(
        self,
        filters: List[ClientDescribeTagsFiltersTypeDef] = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> ClientDescribeTagsResponseTypeDef:
        """
        [Client.describe_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/discovery.html#ApplicationDiscoveryService.Client.describe_tags)
        """

    def disassociate_configuration_items_from_application(
        self, applicationConfigurationId: str, configurationIds: List[str]
    ) -> Dict[str, Any]:
        """
        [Client.disassociate_configuration_items_from_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/discovery.html#ApplicationDiscoveryService.Client.disassociate_configuration_items_from_application)
        """

    def export_configurations(
        self, *args: Any, **kwargs: Any
    ) -> ClientExportConfigurationsResponseTypeDef:
        """
        [Client.export_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/discovery.html#ApplicationDiscoveryService.Client.export_configurations)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/discovery.html#ApplicationDiscoveryService.Client.generate_presigned_url)
        """

    def get_discovery_summary(
        self, *args: Any, **kwargs: Any
    ) -> ClientGetDiscoverySummaryResponseTypeDef:
        """
        [Client.get_discovery_summary documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/discovery.html#ApplicationDiscoveryService.Client.get_discovery_summary)
        """

    def list_configurations(
        self,
        configurationType: Literal["SERVER", "PROCESS", "CONNECTION", "APPLICATION"],
        filters: List[ClientListConfigurationsFiltersTypeDef] = None,
        maxResults: int = None,
        nextToken: str = None,
        orderBy: List[ClientListConfigurationsOrderByTypeDef] = None,
    ) -> ClientListConfigurationsResponseTypeDef:
        """
        [Client.list_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/discovery.html#ApplicationDiscoveryService.Client.list_configurations)
        """

    def list_server_neighbors(
        self,
        configurationId: str,
        portInformationNeeded: bool = None,
        neighborConfigurationIds: List[str] = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> ClientListServerNeighborsResponseTypeDef:
        """
        [Client.list_server_neighbors documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/discovery.html#ApplicationDiscoveryService.Client.list_server_neighbors)
        """

    def start_continuous_export(
        self, *args: Any, **kwargs: Any
    ) -> ClientStartContinuousExportResponseTypeDef:
        """
        [Client.start_continuous_export documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/discovery.html#ApplicationDiscoveryService.Client.start_continuous_export)
        """

    def start_data_collection_by_agent_ids(
        self, agentIds: List[str]
    ) -> ClientStartDataCollectionByAgentIdsResponseTypeDef:
        """
        [Client.start_data_collection_by_agent_ids documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/discovery.html#ApplicationDiscoveryService.Client.start_data_collection_by_agent_ids)
        """

    def start_export_task(
        self,
        exportDataFormat: List[Literal["CSV", "GRAPHML"]] = None,
        filters: List[ClientStartExportTaskFiltersTypeDef] = None,
        startTime: datetime = None,
        endTime: datetime = None,
    ) -> ClientStartExportTaskResponseTypeDef:
        """
        [Client.start_export_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/discovery.html#ApplicationDiscoveryService.Client.start_export_task)
        """

    def start_import_task(
        self, name: str, importUrl: str, clientRequestToken: str = None
    ) -> ClientStartImportTaskResponseTypeDef:
        """
        [Client.start_import_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/discovery.html#ApplicationDiscoveryService.Client.start_import_task)
        """

    def stop_continuous_export(self, exportId: str) -> ClientStopContinuousExportResponseTypeDef:
        """
        [Client.stop_continuous_export documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/discovery.html#ApplicationDiscoveryService.Client.stop_continuous_export)
        """

    def stop_data_collection_by_agent_ids(
        self, agentIds: List[str]
    ) -> ClientStopDataCollectionByAgentIdsResponseTypeDef:
        """
        [Client.stop_data_collection_by_agent_ids documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/discovery.html#ApplicationDiscoveryService.Client.stop_data_collection_by_agent_ids)
        """

    def update_application(
        self, configurationId: str, name: str = None, description: str = None
    ) -> Dict[str, Any]:
        """
        [Client.update_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/discovery.html#ApplicationDiscoveryService.Client.update_application)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_agents"]
    ) -> "paginator_scope.DescribeAgentsPaginator":
        """
        [Paginator.DescribeAgents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/discovery.html#ApplicationDiscoveryService.Paginator.DescribeAgents)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_continuous_exports"]
    ) -> "paginator_scope.DescribeContinuousExportsPaginator":
        """
        [Paginator.DescribeContinuousExports documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/discovery.html#ApplicationDiscoveryService.Paginator.DescribeContinuousExports)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_export_configurations"]
    ) -> "paginator_scope.DescribeExportConfigurationsPaginator":
        """
        [Paginator.DescribeExportConfigurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/discovery.html#ApplicationDiscoveryService.Paginator.DescribeExportConfigurations)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_export_tasks"]
    ) -> "paginator_scope.DescribeExportTasksPaginator":
        """
        [Paginator.DescribeExportTasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/discovery.html#ApplicationDiscoveryService.Paginator.DescribeExportTasks)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_tags"]
    ) -> "paginator_scope.DescribeTagsPaginator":
        """
        [Paginator.DescribeTags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/discovery.html#ApplicationDiscoveryService.Paginator.DescribeTags)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_configurations"]
    ) -> "paginator_scope.ListConfigurationsPaginator":
        """
        [Paginator.ListConfigurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/discovery.html#ApplicationDiscoveryService.Paginator.ListConfigurations)
        """


class Exceptions:
    AuthorizationErrorException: Boto3ClientError
    ClientError: Boto3ClientError
    ConflictErrorException: Boto3ClientError
    HomeRegionNotSetException: Boto3ClientError
    InvalidParameterException: Boto3ClientError
    InvalidParameterValueException: Boto3ClientError
    OperationNotPermittedException: Boto3ClientError
    ResourceInUseException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    ServerInternalErrorException: Boto3ClientError
