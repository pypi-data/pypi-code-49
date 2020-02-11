"""
Main interface for emr service client paginators.

Usage::

    import boto3
    from mypy_boto3.emr import (
        ListBootstrapActionsPaginator,
        ListClustersPaginator,
        ListInstanceFleetsPaginator,
        ListInstanceGroupsPaginator,
        ListInstancesPaginator,
        ListSecurityConfigurationsPaginator,
        ListStepsPaginator,
    )

    client: EMRClient = boto3.client("emr")

    list_bootstrap_actions_paginator: ListBootstrapActionsPaginator = client.get_paginator("list_bootstrap_actions")
    list_clusters_paginator: ListClustersPaginator = client.get_paginator("list_clusters")
    list_instance_fleets_paginator: ListInstanceFleetsPaginator = client.get_paginator("list_instance_fleets")
    list_instance_groups_paginator: ListInstanceGroupsPaginator = client.get_paginator("list_instance_groups")
    list_instances_paginator: ListInstancesPaginator = client.get_paginator("list_instances")
    list_security_configurations_paginator: ListSecurityConfigurationsPaginator = client.get_paginator("list_security_configurations")
    list_steps_paginator: ListStepsPaginator = client.get_paginator("list_steps")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from datetime import datetime
import sys
from typing import Generator, List, TYPE_CHECKING
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_emr.type_defs import (
    ListBootstrapActionsOutputTypeDef,
    ListClustersOutputTypeDef,
    ListInstanceFleetsOutputTypeDef,
    ListInstanceGroupsOutputTypeDef,
    ListInstancesOutputTypeDef,
    ListSecurityConfigurationsOutputTypeDef,
    ListStepsOutputTypeDef,
    PaginatorConfigTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ListBootstrapActionsPaginator",
    "ListClustersPaginator",
    "ListInstanceFleetsPaginator",
    "ListInstanceGroupsPaginator",
    "ListInstancesPaginator",
    "ListSecurityConfigurationsPaginator",
    "ListStepsPaginator",
)


class ListBootstrapActionsPaginator(Boto3Paginator):
    """
    [Paginator.ListBootstrapActions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/emr.html#EMR.Paginator.ListBootstrapActions)
    """

    def paginate(
        self, ClusterId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListBootstrapActionsOutputTypeDef, None, None]:
        """
        [ListBootstrapActions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/emr.html#EMR.Paginator.ListBootstrapActions.paginate)
        """


class ListClustersPaginator(Boto3Paginator):
    """
    [Paginator.ListClusters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/emr.html#EMR.Paginator.ListClusters)
    """

    def paginate(
        self,
        CreatedAfter: datetime = None,
        CreatedBefore: datetime = None,
        ClusterStates: List[
            Literal[
                "STARTING",
                "BOOTSTRAPPING",
                "RUNNING",
                "WAITING",
                "TERMINATING",
                "TERMINATED",
                "TERMINATED_WITH_ERRORS",
            ]
        ] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListClustersOutputTypeDef, None, None]:
        """
        [ListClusters.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/emr.html#EMR.Paginator.ListClusters.paginate)
        """


class ListInstanceFleetsPaginator(Boto3Paginator):
    """
    [Paginator.ListInstanceFleets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/emr.html#EMR.Paginator.ListInstanceFleets)
    """

    def paginate(
        self, ClusterId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListInstanceFleetsOutputTypeDef, None, None]:
        """
        [ListInstanceFleets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/emr.html#EMR.Paginator.ListInstanceFleets.paginate)
        """


class ListInstanceGroupsPaginator(Boto3Paginator):
    """
    [Paginator.ListInstanceGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/emr.html#EMR.Paginator.ListInstanceGroups)
    """

    def paginate(
        self, ClusterId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListInstanceGroupsOutputTypeDef, None, None]:
        """
        [ListInstanceGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/emr.html#EMR.Paginator.ListInstanceGroups.paginate)
        """


class ListInstancesPaginator(Boto3Paginator):
    """
    [Paginator.ListInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/emr.html#EMR.Paginator.ListInstances)
    """

    def paginate(
        self,
        ClusterId: str,
        InstanceGroupId: str = None,
        InstanceGroupTypes: List[Literal["MASTER", "CORE", "TASK"]] = None,
        InstanceFleetId: str = None,
        InstanceFleetType: Literal["MASTER", "CORE", "TASK"] = None,
        InstanceStates: List[
            Literal[
                "AWAITING_FULFILLMENT", "PROVISIONING", "BOOTSTRAPPING", "RUNNING", "TERMINATED"
            ]
        ] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListInstancesOutputTypeDef, None, None]:
        """
        [ListInstances.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/emr.html#EMR.Paginator.ListInstances.paginate)
        """


class ListSecurityConfigurationsPaginator(Boto3Paginator):
    """
    [Paginator.ListSecurityConfigurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/emr.html#EMR.Paginator.ListSecurityConfigurations)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListSecurityConfigurationsOutputTypeDef, None, None]:
        """
        [ListSecurityConfigurations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/emr.html#EMR.Paginator.ListSecurityConfigurations.paginate)
        """


class ListStepsPaginator(Boto3Paginator):
    """
    [Paginator.ListSteps documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/emr.html#EMR.Paginator.ListSteps)
    """

    def paginate(
        self,
        ClusterId: str,
        StepStates: List[
            Literal[
                "PENDING",
                "CANCEL_PENDING",
                "RUNNING",
                "COMPLETED",
                "CANCELLED",
                "FAILED",
                "INTERRUPTED",
            ]
        ] = None,
        StepIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListStepsOutputTypeDef, None, None]:
        """
        [ListSteps.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/emr.html#EMR.Paginator.ListSteps.paginate)
        """
