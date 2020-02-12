"""
Main interface for sagemaker-a2i-runtime service client paginators.

Usage::

    import boto3
    from mypy_boto3.sagemaker_a2i_runtime import (
        ListHumanLoopsPaginator,
    )

    client: AugmentedAIRuntimeClient = boto3.client("sagemaker-a2i-runtime")

    list_human_loops_paginator: ListHumanLoopsPaginator = client.get_paginator("list_human_loops")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from datetime import datetime
import sys
from typing import Generator, TYPE_CHECKING
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_sagemaker_a2i_runtime.type_defs import (
    ListHumanLoopsResponseTypeDef,
    PaginatorConfigTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ListHumanLoopsPaginator",)


class ListHumanLoopsPaginator(Boto3Paginator):
    """
    [Paginator.ListHumanLoops documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker-a2i-runtime.html#AugmentedAIRuntime.Paginator.ListHumanLoops)
    """

    def paginate(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListHumanLoopsResponseTypeDef, None, None]:
        """
        [ListHumanLoops.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker-a2i-runtime.html#AugmentedAIRuntime.Paginator.ListHumanLoops.paginate)
        """
