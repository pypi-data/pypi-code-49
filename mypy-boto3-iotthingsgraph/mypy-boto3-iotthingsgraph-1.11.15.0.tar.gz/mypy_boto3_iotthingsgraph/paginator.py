"""
Main interface for iotthingsgraph service client paginators.

Usage::

    import boto3
    from mypy_boto3.iotthingsgraph import (
        GetFlowTemplateRevisionsPaginator,
        GetSystemTemplateRevisionsPaginator,
        ListFlowExecutionMessagesPaginator,
        ListTagsForResourcePaginator,
        SearchEntitiesPaginator,
        SearchFlowExecutionsPaginator,
        SearchFlowTemplatesPaginator,
        SearchSystemInstancesPaginator,
        SearchSystemTemplatesPaginator,
        SearchThingsPaginator,
    )

    client: IoTThingsGraphClient = boto3.client("iotthingsgraph")

    get_flow_template_revisions_paginator: GetFlowTemplateRevisionsPaginator = client.get_paginator("get_flow_template_revisions")
    get_system_template_revisions_paginator: GetSystemTemplateRevisionsPaginator = client.get_paginator("get_system_template_revisions")
    list_flow_execution_messages_paginator: ListFlowExecutionMessagesPaginator = client.get_paginator("list_flow_execution_messages")
    list_tags_for_resource_paginator: ListTagsForResourcePaginator = client.get_paginator("list_tags_for_resource")
    search_entities_paginator: SearchEntitiesPaginator = client.get_paginator("search_entities")
    search_flow_executions_paginator: SearchFlowExecutionsPaginator = client.get_paginator("search_flow_executions")
    search_flow_templates_paginator: SearchFlowTemplatesPaginator = client.get_paginator("search_flow_templates")
    search_system_instances_paginator: SearchSystemInstancesPaginator = client.get_paginator("search_system_instances")
    search_system_templates_paginator: SearchSystemTemplatesPaginator = client.get_paginator("search_system_templates")
    search_things_paginator: SearchThingsPaginator = client.get_paginator("search_things")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from datetime import datetime
import sys
from typing import Generator, List, TYPE_CHECKING
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_iotthingsgraph.type_defs import (
    EntityFilterTypeDef,
    FlowTemplateFilterTypeDef,
    GetFlowTemplateRevisionsResponseTypeDef,
    GetSystemTemplateRevisionsResponseTypeDef,
    ListFlowExecutionMessagesResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    PaginatorConfigTypeDef,
    SearchEntitiesResponseTypeDef,
    SearchFlowExecutionsResponseTypeDef,
    SearchFlowTemplatesResponseTypeDef,
    SearchSystemInstancesResponseTypeDef,
    SearchSystemTemplatesResponseTypeDef,
    SearchThingsResponseTypeDef,
    SystemInstanceFilterTypeDef,
    SystemTemplateFilterTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "GetFlowTemplateRevisionsPaginator",
    "GetSystemTemplateRevisionsPaginator",
    "ListFlowExecutionMessagesPaginator",
    "ListTagsForResourcePaginator",
    "SearchEntitiesPaginator",
    "SearchFlowExecutionsPaginator",
    "SearchFlowTemplatesPaginator",
    "SearchSystemInstancesPaginator",
    "SearchSystemTemplatesPaginator",
    "SearchThingsPaginator",
)


class GetFlowTemplateRevisionsPaginator(Boto3Paginator):
    """
    [Paginator.GetFlowTemplateRevisions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.GetFlowTemplateRevisions)
    """

    def paginate(
        self, id: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[GetFlowTemplateRevisionsResponseTypeDef, None, None]:
        """
        [GetFlowTemplateRevisions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.GetFlowTemplateRevisions.paginate)
        """


class GetSystemTemplateRevisionsPaginator(Boto3Paginator):
    """
    [Paginator.GetSystemTemplateRevisions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.GetSystemTemplateRevisions)
    """

    def paginate(
        self, id: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[GetSystemTemplateRevisionsResponseTypeDef, None, None]:
        """
        [GetSystemTemplateRevisions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.GetSystemTemplateRevisions.paginate)
        """


class ListFlowExecutionMessagesPaginator(Boto3Paginator):
    """
    [Paginator.ListFlowExecutionMessages documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.ListFlowExecutionMessages)
    """

    def paginate(
        self, flowExecutionId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListFlowExecutionMessagesResponseTypeDef, None, None]:
        """
        [ListFlowExecutionMessages.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.ListFlowExecutionMessages.paginate)
        """


class ListTagsForResourcePaginator(Boto3Paginator):
    """
    [Paginator.ListTagsForResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.ListTagsForResource)
    """

    def paginate(
        self, resourceArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListTagsForResourceResponseTypeDef, None, None]:
        """
        [ListTagsForResource.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.ListTagsForResource.paginate)
        """


class SearchEntitiesPaginator(Boto3Paginator):
    """
    [Paginator.SearchEntities documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.SearchEntities)
    """

    def paginate(
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
        filters: List[EntityFilterTypeDef] = None,
        namespaceVersion: int = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[SearchEntitiesResponseTypeDef, None, None]:
        """
        [SearchEntities.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.SearchEntities.paginate)
        """


class SearchFlowExecutionsPaginator(Boto3Paginator):
    """
    [Paginator.SearchFlowExecutions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.SearchFlowExecutions)
    """

    def paginate(
        self,
        systemInstanceId: str,
        flowExecutionId: str = None,
        startTime: datetime = None,
        endTime: datetime = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[SearchFlowExecutionsResponseTypeDef, None, None]:
        """
        [SearchFlowExecutions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.SearchFlowExecutions.paginate)
        """


class SearchFlowTemplatesPaginator(Boto3Paginator):
    """
    [Paginator.SearchFlowTemplates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.SearchFlowTemplates)
    """

    def paginate(
        self,
        filters: List[FlowTemplateFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[SearchFlowTemplatesResponseTypeDef, None, None]:
        """
        [SearchFlowTemplates.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.SearchFlowTemplates.paginate)
        """


class SearchSystemInstancesPaginator(Boto3Paginator):
    """
    [Paginator.SearchSystemInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.SearchSystemInstances)
    """

    def paginate(
        self,
        filters: List[SystemInstanceFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[SearchSystemInstancesResponseTypeDef, None, None]:
        """
        [SearchSystemInstances.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.SearchSystemInstances.paginate)
        """


class SearchSystemTemplatesPaginator(Boto3Paginator):
    """
    [Paginator.SearchSystemTemplates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.SearchSystemTemplates)
    """

    def paginate(
        self,
        filters: List[SystemTemplateFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[SearchSystemTemplatesResponseTypeDef, None, None]:
        """
        [SearchSystemTemplates.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.SearchSystemTemplates.paginate)
        """


class SearchThingsPaginator(Boto3Paginator):
    """
    [Paginator.SearchThings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.SearchThings)
    """

    def paginate(
        self,
        entityId: str,
        namespaceVersion: int = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[SearchThingsResponseTypeDef, None, None]:
        """
        [SearchThings.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.SearchThings.paginate)
        """
