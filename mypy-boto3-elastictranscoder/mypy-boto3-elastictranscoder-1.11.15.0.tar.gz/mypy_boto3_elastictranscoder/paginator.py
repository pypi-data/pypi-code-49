"""
Main interface for elastictranscoder service client paginators.

Usage::

    import boto3
    from mypy_boto3.elastictranscoder import (
        ListJobsByPipelinePaginator,
        ListJobsByStatusPaginator,
        ListPipelinesPaginator,
        ListPresetsPaginator,
    )

    client: ElasticTranscoderClient = boto3.client("elastictranscoder")

    list_jobs_by_pipeline_paginator: ListJobsByPipelinePaginator = client.get_paginator("list_jobs_by_pipeline")
    list_jobs_by_status_paginator: ListJobsByStatusPaginator = client.get_paginator("list_jobs_by_status")
    list_pipelines_paginator: ListPipelinesPaginator = client.get_paginator("list_pipelines")
    list_presets_paginator: ListPresetsPaginator = client.get_paginator("list_presets")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from typing import Generator, TYPE_CHECKING
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_elastictranscoder.type_defs import (
    ListJobsByPipelineResponseTypeDef,
    ListJobsByStatusResponseTypeDef,
    ListPipelinesResponseTypeDef,
    ListPresetsResponseTypeDef,
    PaginatorConfigTypeDef,
)


__all__ = (
    "ListJobsByPipelinePaginator",
    "ListJobsByStatusPaginator",
    "ListPipelinesPaginator",
    "ListPresetsPaginator",
)


class ListJobsByPipelinePaginator(Boto3Paginator):
    """
    [Paginator.ListJobsByPipeline documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elastictranscoder.html#ElasticTranscoder.Paginator.ListJobsByPipeline)
    """

    def paginate(
        self,
        PipelineId: str,
        Ascending: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListJobsByPipelineResponseTypeDef, None, None]:
        """
        [ListJobsByPipeline.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elastictranscoder.html#ElasticTranscoder.Paginator.ListJobsByPipeline.paginate)
        """


class ListJobsByStatusPaginator(Boto3Paginator):
    """
    [Paginator.ListJobsByStatus documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elastictranscoder.html#ElasticTranscoder.Paginator.ListJobsByStatus)
    """

    def paginate(
        self, Status: str, Ascending: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListJobsByStatusResponseTypeDef, None, None]:
        """
        [ListJobsByStatus.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elastictranscoder.html#ElasticTranscoder.Paginator.ListJobsByStatus.paginate)
        """


class ListPipelinesPaginator(Boto3Paginator):
    """
    [Paginator.ListPipelines documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elastictranscoder.html#ElasticTranscoder.Paginator.ListPipelines)
    """

    def paginate(
        self, Ascending: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListPipelinesResponseTypeDef, None, None]:
        """
        [ListPipelines.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elastictranscoder.html#ElasticTranscoder.Paginator.ListPipelines.paginate)
        """


class ListPresetsPaginator(Boto3Paginator):
    """
    [Paginator.ListPresets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elastictranscoder.html#ElasticTranscoder.Paginator.ListPresets)
    """

    def paginate(
        self, Ascending: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListPresetsResponseTypeDef, None, None]:
        """
        [ListPresets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elastictranscoder.html#ElasticTranscoder.Paginator.ListPresets.paginate)
        """
