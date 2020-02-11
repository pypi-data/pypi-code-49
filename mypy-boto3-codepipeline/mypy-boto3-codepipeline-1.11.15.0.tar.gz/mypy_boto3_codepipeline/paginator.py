"""
Main interface for codepipeline service client paginators.

Usage::

    import boto3
    from mypy_boto3.codepipeline import (
        ListActionExecutionsPaginator,
        ListActionTypesPaginator,
        ListPipelineExecutionsPaginator,
        ListPipelinesPaginator,
        ListTagsForResourcePaginator,
        ListWebhooksPaginator,
    )

    client: CodePipelineClient = boto3.client("codepipeline")

    list_action_executions_paginator: ListActionExecutionsPaginator = client.get_paginator("list_action_executions")
    list_action_types_paginator: ListActionTypesPaginator = client.get_paginator("list_action_types")
    list_pipeline_executions_paginator: ListPipelineExecutionsPaginator = client.get_paginator("list_pipeline_executions")
    list_pipelines_paginator: ListPipelinesPaginator = client.get_paginator("list_pipelines")
    list_tags_for_resource_paginator: ListTagsForResourcePaginator = client.get_paginator("list_tags_for_resource")
    list_webhooks_paginator: ListWebhooksPaginator = client.get_paginator("list_webhooks")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Generator, TYPE_CHECKING
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_codepipeline.type_defs import (
    ActionExecutionFilterTypeDef,
    ListActionExecutionsOutputTypeDef,
    ListActionTypesOutputTypeDef,
    ListPipelineExecutionsOutputTypeDef,
    ListPipelinesOutputTypeDef,
    ListTagsForResourceOutputTypeDef,
    ListWebhooksOutputTypeDef,
    PaginatorConfigTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ListActionExecutionsPaginator",
    "ListActionTypesPaginator",
    "ListPipelineExecutionsPaginator",
    "ListPipelinesPaginator",
    "ListTagsForResourcePaginator",
    "ListWebhooksPaginator",
)


class ListActionExecutionsPaginator(Boto3Paginator):
    """
    [Paginator.ListActionExecutions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codepipeline.html#CodePipeline.Paginator.ListActionExecutions)
    """

    def paginate(
        self,
        pipelineName: str,
        filter: ActionExecutionFilterTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListActionExecutionsOutputTypeDef, None, None]:
        """
        [ListActionExecutions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codepipeline.html#CodePipeline.Paginator.ListActionExecutions.paginate)
        """


class ListActionTypesPaginator(Boto3Paginator):
    """
    [Paginator.ListActionTypes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codepipeline.html#CodePipeline.Paginator.ListActionTypes)
    """

    def paginate(
        self,
        actionOwnerFilter: Literal["AWS", "ThirdParty", "Custom"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListActionTypesOutputTypeDef, None, None]:
        """
        [ListActionTypes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codepipeline.html#CodePipeline.Paginator.ListActionTypes.paginate)
        """


class ListPipelineExecutionsPaginator(Boto3Paginator):
    """
    [Paginator.ListPipelineExecutions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codepipeline.html#CodePipeline.Paginator.ListPipelineExecutions)
    """

    def paginate(
        self, pipelineName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListPipelineExecutionsOutputTypeDef, None, None]:
        """
        [ListPipelineExecutions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codepipeline.html#CodePipeline.Paginator.ListPipelineExecutions.paginate)
        """


class ListPipelinesPaginator(Boto3Paginator):
    """
    [Paginator.ListPipelines documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codepipeline.html#CodePipeline.Paginator.ListPipelines)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListPipelinesOutputTypeDef, None, None]:
        """
        [ListPipelines.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codepipeline.html#CodePipeline.Paginator.ListPipelines.paginate)
        """


class ListTagsForResourcePaginator(Boto3Paginator):
    """
    [Paginator.ListTagsForResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codepipeline.html#CodePipeline.Paginator.ListTagsForResource)
    """

    def paginate(
        self, resourceArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListTagsForResourceOutputTypeDef, None, None]:
        """
        [ListTagsForResource.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codepipeline.html#CodePipeline.Paginator.ListTagsForResource.paginate)
        """


class ListWebhooksPaginator(Boto3Paginator):
    """
    [Paginator.ListWebhooks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codepipeline.html#CodePipeline.Paginator.ListWebhooks)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListWebhooksOutputTypeDef, None, None]:
        """
        [ListWebhooks.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codepipeline.html#CodePipeline.Paginator.ListWebhooks.paginate)
        """
