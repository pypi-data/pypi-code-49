"""
Main interface for iotthingsgraph service client

Usage::

    import boto3
    from mypy_boto3.iotthingsgraph import IoTThingsGraphClient

    session = boto3.Session()

    client: IoTThingsGraphClient = boto3.client("iotthingsgraph")
    session_client: IoTThingsGraphClient = session.client("iotthingsgraph")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from datetime import datetime
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_iotthingsgraph.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_iotthingsgraph.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_iotthingsgraph.type_defs import (
    ClientCreateFlowTemplateDefinitionTypeDef,
    ClientCreateFlowTemplateResponseTypeDef,
    ClientCreateSystemInstanceDefinitionTypeDef,
    ClientCreateSystemInstanceMetricsConfigurationTypeDef,
    ClientCreateSystemInstanceResponseTypeDef,
    ClientCreateSystemInstanceTagsTypeDef,
    ClientCreateSystemTemplateDefinitionTypeDef,
    ClientCreateSystemTemplateResponseTypeDef,
    ClientDeleteNamespaceResponseTypeDef,
    ClientDeploySystemInstanceResponseTypeDef,
    ClientDescribeNamespaceResponseTypeDef,
    ClientGetEntitiesResponseTypeDef,
    ClientGetFlowTemplateResponseTypeDef,
    ClientGetFlowTemplateRevisionsResponseTypeDef,
    ClientGetNamespaceDeletionStatusResponseTypeDef,
    ClientGetSystemInstanceResponseTypeDef,
    ClientGetSystemTemplateResponseTypeDef,
    ClientGetSystemTemplateRevisionsResponseTypeDef,
    ClientGetUploadStatusResponseTypeDef,
    ClientListFlowExecutionMessagesResponseTypeDef,
    ClientListTagsForResourceResponseTypeDef,
    ClientSearchEntitiesFiltersTypeDef,
    ClientSearchEntitiesResponseTypeDef,
    ClientSearchFlowExecutionsResponseTypeDef,
    ClientSearchFlowTemplatesFiltersTypeDef,
    ClientSearchFlowTemplatesResponseTypeDef,
    ClientSearchSystemInstancesFiltersTypeDef,
    ClientSearchSystemInstancesResponseTypeDef,
    ClientSearchSystemTemplatesFiltersTypeDef,
    ClientSearchSystemTemplatesResponseTypeDef,
    ClientSearchThingsResponseTypeDef,
    ClientTagResourceTagsTypeDef,
    ClientUndeploySystemInstanceResponseTypeDef,
    ClientUpdateFlowTemplateDefinitionTypeDef,
    ClientUpdateFlowTemplateResponseTypeDef,
    ClientUpdateSystemTemplateDefinitionTypeDef,
    ClientUpdateSystemTemplateResponseTypeDef,
    ClientUploadEntityDefinitionsDocumentTypeDef,
    ClientUploadEntityDefinitionsResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("IoTThingsGraphClient",)


class IoTThingsGraphClient:
    """
    [IoTThingsGraph.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iotthingsgraph.html#IoTThingsGraph.Client)
    """

    exceptions: "client_scope.Exceptions"

    def associate_entity_to_thing(
        self, thingName: str, entityId: str, namespaceVersion: int = None
    ) -> Dict[str, Any]:
        """
        [Client.associate_entity_to_thing documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.associate_entity_to_thing)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.can_paginate)
        """

    def create_flow_template(
        self,
        definition: ClientCreateFlowTemplateDefinitionTypeDef,
        compatibleNamespaceVersion: int = None,
    ) -> ClientCreateFlowTemplateResponseTypeDef:
        """
        [Client.create_flow_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.create_flow_template)
        """

    def create_system_instance(
        self,
        definition: ClientCreateSystemInstanceDefinitionTypeDef,
        target: Literal["GREENGRASS", "CLOUD"],
        tags: List[ClientCreateSystemInstanceTagsTypeDef] = None,
        greengrassGroupName: str = None,
        s3BucketName: str = None,
        metricsConfiguration: ClientCreateSystemInstanceMetricsConfigurationTypeDef = None,
        flowActionsRoleArn: str = None,
    ) -> ClientCreateSystemInstanceResponseTypeDef:
        """
        [Client.create_system_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.create_system_instance)
        """

    def create_system_template(
        self,
        definition: ClientCreateSystemTemplateDefinitionTypeDef,
        compatibleNamespaceVersion: int = None,
    ) -> ClientCreateSystemTemplateResponseTypeDef:
        """
        [Client.create_system_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.create_system_template)
        """

    def delete_flow_template(self, id: str) -> Dict[str, Any]:
        """
        [Client.delete_flow_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.delete_flow_template)
        """

    def delete_namespace(self, *args: Any, **kwargs: Any) -> ClientDeleteNamespaceResponseTypeDef:
        """
        [Client.delete_namespace documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.delete_namespace)
        """

    def delete_system_instance(self, id: str = None) -> Dict[str, Any]:
        """
        [Client.delete_system_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.delete_system_instance)
        """

    def delete_system_template(self, id: str) -> Dict[str, Any]:
        """
        [Client.delete_system_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.delete_system_template)
        """

    def deploy_system_instance(self, id: str = None) -> ClientDeploySystemInstanceResponseTypeDef:
        """
        [Client.deploy_system_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.deploy_system_instance)
        """

    def deprecate_flow_template(self, id: str) -> Dict[str, Any]:
        """
        [Client.deprecate_flow_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.deprecate_flow_template)
        """

    def deprecate_system_template(self, id: str) -> Dict[str, Any]:
        """
        [Client.deprecate_system_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.deprecate_system_template)
        """

    def describe_namespace(
        self, namespaceName: str = None
    ) -> ClientDescribeNamespaceResponseTypeDef:
        """
        [Client.describe_namespace documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.describe_namespace)
        """

    def dissociate_entity_from_thing(
        self,
        thingName: str,
        entityType: Literal[
            "DEVICE",
            "SERVICE",
            "DEVICE_MODEL",
            "CAPABILITY",
            "STATE",
            "ACTION",
            "EVENT",
            "PROPERTY",
            "MAPPING",
            "ENUM",
        ],
    ) -> Dict[str, Any]:
        """
        [Client.dissociate_entity_from_thing documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.dissociate_entity_from_thing)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.generate_presigned_url)
        """

    def get_entities(
        self, ids: List[str], namespaceVersion: int = None
    ) -> ClientGetEntitiesResponseTypeDef:
        """
        [Client.get_entities documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.get_entities)
        """

    def get_flow_template(
        self, id: str, revisionNumber: int = None
    ) -> ClientGetFlowTemplateResponseTypeDef:
        """
        [Client.get_flow_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.get_flow_template)
        """

    def get_flow_template_revisions(
        self, id: str, nextToken: str = None, maxResults: int = None
    ) -> ClientGetFlowTemplateRevisionsResponseTypeDef:
        """
        [Client.get_flow_template_revisions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.get_flow_template_revisions)
        """

    def get_namespace_deletion_status(
        self, *args: Any, **kwargs: Any
    ) -> ClientGetNamespaceDeletionStatusResponseTypeDef:
        """
        [Client.get_namespace_deletion_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.get_namespace_deletion_status)
        """

    def get_system_instance(self, id: str) -> ClientGetSystemInstanceResponseTypeDef:
        """
        [Client.get_system_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.get_system_instance)
        """

    def get_system_template(
        self, id: str, revisionNumber: int = None
    ) -> ClientGetSystemTemplateResponseTypeDef:
        """
        [Client.get_system_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.get_system_template)
        """

    def get_system_template_revisions(
        self, id: str, nextToken: str = None, maxResults: int = None
    ) -> ClientGetSystemTemplateRevisionsResponseTypeDef:
        """
        [Client.get_system_template_revisions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.get_system_template_revisions)
        """

    def get_upload_status(self, uploadId: str) -> ClientGetUploadStatusResponseTypeDef:
        """
        [Client.get_upload_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.get_upload_status)
        """

    def list_flow_execution_messages(
        self, flowExecutionId: str, nextToken: str = None, maxResults: int = None
    ) -> ClientListFlowExecutionMessagesResponseTypeDef:
        """
        [Client.list_flow_execution_messages documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.list_flow_execution_messages)
        """

    def list_tags_for_resource(
        self, resourceArn: str, maxResults: int = None, nextToken: str = None
    ) -> ClientListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.list_tags_for_resource)
        """

    def search_entities(
        self,
        entityTypes: List[
            Literal[
                "DEVICE",
                "SERVICE",
                "DEVICE_MODEL",
                "CAPABILITY",
                "STATE",
                "ACTION",
                "EVENT",
                "PROPERTY",
                "MAPPING",
                "ENUM",
            ]
        ],
        filters: List[ClientSearchEntitiesFiltersTypeDef] = None,
        nextToken: str = None,
        maxResults: int = None,
        namespaceVersion: int = None,
    ) -> ClientSearchEntitiesResponseTypeDef:
        """
        [Client.search_entities documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.search_entities)
        """

    def search_flow_executions(
        self,
        systemInstanceId: str,
        flowExecutionId: str = None,
        startTime: datetime = None,
        endTime: datetime = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ClientSearchFlowExecutionsResponseTypeDef:
        """
        [Client.search_flow_executions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.search_flow_executions)
        """

    def search_flow_templates(
        self,
        filters: List[ClientSearchFlowTemplatesFiltersTypeDef] = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ClientSearchFlowTemplatesResponseTypeDef:
        """
        [Client.search_flow_templates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.search_flow_templates)
        """

    def search_system_instances(
        self,
        filters: List[ClientSearchSystemInstancesFiltersTypeDef] = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ClientSearchSystemInstancesResponseTypeDef:
        """
        [Client.search_system_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.search_system_instances)
        """

    def search_system_templates(
        self,
        filters: List[ClientSearchSystemTemplatesFiltersTypeDef] = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ClientSearchSystemTemplatesResponseTypeDef:
        """
        [Client.search_system_templates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.search_system_templates)
        """

    def search_things(
        self,
        entityId: str,
        nextToken: str = None,
        maxResults: int = None,
        namespaceVersion: int = None,
    ) -> ClientSearchThingsResponseTypeDef:
        """
        [Client.search_things documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.search_things)
        """

    def tag_resource(
        self, resourceArn: str, tags: List[ClientTagResourceTagsTypeDef]
    ) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.tag_resource)
        """

    def undeploy_system_instance(
        self, id: str = None
    ) -> ClientUndeploySystemInstanceResponseTypeDef:
        """
        [Client.undeploy_system_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.undeploy_system_instance)
        """

    def untag_resource(self, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.untag_resource)
        """

    def update_flow_template(
        self,
        id: str,
        definition: ClientUpdateFlowTemplateDefinitionTypeDef,
        compatibleNamespaceVersion: int = None,
    ) -> ClientUpdateFlowTemplateResponseTypeDef:
        """
        [Client.update_flow_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.update_flow_template)
        """

    def update_system_template(
        self,
        id: str,
        definition: ClientUpdateSystemTemplateDefinitionTypeDef,
        compatibleNamespaceVersion: int = None,
    ) -> ClientUpdateSystemTemplateResponseTypeDef:
        """
        [Client.update_system_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.update_system_template)
        """

    def upload_entity_definitions(
        self,
        document: ClientUploadEntityDefinitionsDocumentTypeDef = None,
        syncWithPublicNamespace: bool = None,
        deprecateExistingEntities: bool = None,
    ) -> ClientUploadEntityDefinitionsResponseTypeDef:
        """
        [Client.upload_entity_definitions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.upload_entity_definitions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_flow_template_revisions"]
    ) -> "paginator_scope.GetFlowTemplateRevisionsPaginator":
        """
        [Paginator.GetFlowTemplateRevisions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.GetFlowTemplateRevisions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_system_template_revisions"]
    ) -> "paginator_scope.GetSystemTemplateRevisionsPaginator":
        """
        [Paginator.GetSystemTemplateRevisions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.GetSystemTemplateRevisions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_flow_execution_messages"]
    ) -> "paginator_scope.ListFlowExecutionMessagesPaginator":
        """
        [Paginator.ListFlowExecutionMessages documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.ListFlowExecutionMessages)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_tags_for_resource"]
    ) -> "paginator_scope.ListTagsForResourcePaginator":
        """
        [Paginator.ListTagsForResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.ListTagsForResource)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["search_entities"]
    ) -> "paginator_scope.SearchEntitiesPaginator":
        """
        [Paginator.SearchEntities documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.SearchEntities)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["search_flow_executions"]
    ) -> "paginator_scope.SearchFlowExecutionsPaginator":
        """
        [Paginator.SearchFlowExecutions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.SearchFlowExecutions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["search_flow_templates"]
    ) -> "paginator_scope.SearchFlowTemplatesPaginator":
        """
        [Paginator.SearchFlowTemplates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.SearchFlowTemplates)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["search_system_instances"]
    ) -> "paginator_scope.SearchSystemInstancesPaginator":
        """
        [Paginator.SearchSystemInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.SearchSystemInstances)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["search_system_templates"]
    ) -> "paginator_scope.SearchSystemTemplatesPaginator":
        """
        [Paginator.SearchSystemTemplates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.SearchSystemTemplates)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["search_things"]
    ) -> "paginator_scope.SearchThingsPaginator":
        """
        [Paginator.SearchThings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.SearchThings)
        """


class Exceptions:
    ClientError: Boto3ClientError
    InternalFailureException: Boto3ClientError
    InvalidRequestException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    ResourceAlreadyExistsException: Boto3ClientError
    ResourceInUseException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    ThrottlingException: Boto3ClientError
