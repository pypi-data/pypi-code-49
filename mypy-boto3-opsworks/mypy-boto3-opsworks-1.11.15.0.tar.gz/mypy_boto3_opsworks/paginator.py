"""
Main interface for opsworks service client paginators.

Usage::

    import boto3
    from mypy_boto3.opsworks import (
        DescribeEcsClustersPaginator,
    )

    client: OpsWorksClient = boto3.client("opsworks")

    describe_ecs_clusters_paginator: DescribeEcsClustersPaginator = client.get_paginator("describe_ecs_clusters")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from typing import Generator, List, TYPE_CHECKING
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_opsworks.type_defs import DescribeEcsClustersResultTypeDef, PaginatorConfigTypeDef


__all__ = ("DescribeEcsClustersPaginator",)


class DescribeEcsClustersPaginator(Boto3Paginator):
    """
    [Paginator.DescribeEcsClusters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/opsworks.html#OpsWorks.Paginator.DescribeEcsClusters)
    """

    def paginate(
        self,
        EcsClusterArns: List[str] = None,
        StackId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeEcsClustersResultTypeDef, None, None]:
        """
        [DescribeEcsClusters.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/opsworks.html#OpsWorks.Paginator.DescribeEcsClusters.paginate)
        """
