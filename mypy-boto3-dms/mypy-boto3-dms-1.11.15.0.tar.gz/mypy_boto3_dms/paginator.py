"""
Main interface for dms service client paginators.

Usage::

    import boto3
    from mypy_boto3.dms import (
        DescribeCertificatesPaginator,
        DescribeConnectionsPaginator,
        DescribeEndpointTypesPaginator,
        DescribeEndpointsPaginator,
        DescribeEventSubscriptionsPaginator,
        DescribeEventsPaginator,
        DescribeOrderableReplicationInstancesPaginator,
        DescribeReplicationInstancesPaginator,
        DescribeReplicationSubnetGroupsPaginator,
        DescribeReplicationTaskAssessmentResultsPaginator,
        DescribeReplicationTasksPaginator,
        DescribeSchemasPaginator,
        DescribeTableStatisticsPaginator,
    )

    client: DatabaseMigrationServiceClient = boto3.client("dms")

    describe_certificates_paginator: DescribeCertificatesPaginator = client.get_paginator("describe_certificates")
    describe_connections_paginator: DescribeConnectionsPaginator = client.get_paginator("describe_connections")
    describe_endpoint_types_paginator: DescribeEndpointTypesPaginator = client.get_paginator("describe_endpoint_types")
    describe_endpoints_paginator: DescribeEndpointsPaginator = client.get_paginator("describe_endpoints")
    describe_event_subscriptions_paginator: DescribeEventSubscriptionsPaginator = client.get_paginator("describe_event_subscriptions")
    describe_events_paginator: DescribeEventsPaginator = client.get_paginator("describe_events")
    describe_orderable_replication_instances_paginator: DescribeOrderableReplicationInstancesPaginator = client.get_paginator("describe_orderable_replication_instances")
    describe_replication_instances_paginator: DescribeReplicationInstancesPaginator = client.get_paginator("describe_replication_instances")
    describe_replication_subnet_groups_paginator: DescribeReplicationSubnetGroupsPaginator = client.get_paginator("describe_replication_subnet_groups")
    describe_replication_task_assessment_results_paginator: DescribeReplicationTaskAssessmentResultsPaginator = client.get_paginator("describe_replication_task_assessment_results")
    describe_replication_tasks_paginator: DescribeReplicationTasksPaginator = client.get_paginator("describe_replication_tasks")
    describe_schemas_paginator: DescribeSchemasPaginator = client.get_paginator("describe_schemas")
    describe_table_statistics_paginator: DescribeTableStatisticsPaginator = client.get_paginator("describe_table_statistics")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from datetime import datetime
import sys
from typing import Generator, List, TYPE_CHECKING
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_dms.type_defs import (
    DescribeCertificatesResponseTypeDef,
    DescribeConnectionsResponseTypeDef,
    DescribeEndpointTypesResponseTypeDef,
    DescribeEndpointsResponseTypeDef,
    DescribeEventSubscriptionsResponseTypeDef,
    DescribeEventsResponseTypeDef,
    DescribeOrderableReplicationInstancesResponseTypeDef,
    DescribeReplicationInstancesResponseTypeDef,
    DescribeReplicationSubnetGroupsResponseTypeDef,
    DescribeReplicationTaskAssessmentResultsResponseTypeDef,
    DescribeReplicationTasksResponseTypeDef,
    DescribeSchemasResponseTypeDef,
    DescribeTableStatisticsResponseTypeDef,
    FilterTypeDef,
    PaginatorConfigTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "DescribeCertificatesPaginator",
    "DescribeConnectionsPaginator",
    "DescribeEndpointTypesPaginator",
    "DescribeEndpointsPaginator",
    "DescribeEventSubscriptionsPaginator",
    "DescribeEventsPaginator",
    "DescribeOrderableReplicationInstancesPaginator",
    "DescribeReplicationInstancesPaginator",
    "DescribeReplicationSubnetGroupsPaginator",
    "DescribeReplicationTaskAssessmentResultsPaginator",
    "DescribeReplicationTasksPaginator",
    "DescribeSchemasPaginator",
    "DescribeTableStatisticsPaginator",
)


class DescribeCertificatesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeCertificates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeCertificates)
    """

    def paginate(
        self, Filters: List[FilterTypeDef] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[DescribeCertificatesResponseTypeDef, None, None]:
        """
        [DescribeCertificates.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeCertificates.paginate)
        """


class DescribeConnectionsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeConnections documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeConnections)
    """

    def paginate(
        self, Filters: List[FilterTypeDef] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[DescribeConnectionsResponseTypeDef, None, None]:
        """
        [DescribeConnections.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeConnections.paginate)
        """


class DescribeEndpointTypesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeEndpointTypes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeEndpointTypes)
    """

    def paginate(
        self, Filters: List[FilterTypeDef] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[DescribeEndpointTypesResponseTypeDef, None, None]:
        """
        [DescribeEndpointTypes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeEndpointTypes.paginate)
        """


class DescribeEndpointsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeEndpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeEndpoints)
    """

    def paginate(
        self, Filters: List[FilterTypeDef] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[DescribeEndpointsResponseTypeDef, None, None]:
        """
        [DescribeEndpoints.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeEndpoints.paginate)
        """


class DescribeEventSubscriptionsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeEventSubscriptions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeEventSubscriptions)
    """

    def paginate(
        self,
        SubscriptionName: str = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeEventSubscriptionsResponseTypeDef, None, None]:
        """
        [DescribeEventSubscriptions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeEventSubscriptions.paginate)
        """


class DescribeEventsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeEvents)
    """

    def paginate(
        self,
        SourceIdentifier: str = None,
        SourceType: Literal["replication-instance"] = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        Duration: int = None,
        EventCategories: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeEventsResponseTypeDef, None, None]:
        """
        [DescribeEvents.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeEvents.paginate)
        """


class DescribeOrderableReplicationInstancesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeOrderableReplicationInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeOrderableReplicationInstances)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[DescribeOrderableReplicationInstancesResponseTypeDef, None, None]:
        """
        [DescribeOrderableReplicationInstances.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeOrderableReplicationInstances.paginate)
        """


class DescribeReplicationInstancesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeReplicationInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeReplicationInstances)
    """

    def paginate(
        self, Filters: List[FilterTypeDef] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[DescribeReplicationInstancesResponseTypeDef, None, None]:
        """
        [DescribeReplicationInstances.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeReplicationInstances.paginate)
        """


class DescribeReplicationSubnetGroupsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeReplicationSubnetGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeReplicationSubnetGroups)
    """

    def paginate(
        self, Filters: List[FilterTypeDef] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[DescribeReplicationSubnetGroupsResponseTypeDef, None, None]:
        """
        [DescribeReplicationSubnetGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeReplicationSubnetGroups.paginate)
        """


class DescribeReplicationTaskAssessmentResultsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeReplicationTaskAssessmentResults documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeReplicationTaskAssessmentResults)
    """

    def paginate(
        self, ReplicationTaskArn: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[DescribeReplicationTaskAssessmentResultsResponseTypeDef, None, None]:
        """
        [DescribeReplicationTaskAssessmentResults.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeReplicationTaskAssessmentResults.paginate)
        """


class DescribeReplicationTasksPaginator(Boto3Paginator):
    """
    [Paginator.DescribeReplicationTasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeReplicationTasks)
    """

    def paginate(
        self,
        Filters: List[FilterTypeDef] = None,
        WithoutSettings: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeReplicationTasksResponseTypeDef, None, None]:
        """
        [DescribeReplicationTasks.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeReplicationTasks.paginate)
        """


class DescribeSchemasPaginator(Boto3Paginator):
    """
    [Paginator.DescribeSchemas documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeSchemas)
    """

    def paginate(
        self, EndpointArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[DescribeSchemasResponseTypeDef, None, None]:
        """
        [DescribeSchemas.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeSchemas.paginate)
        """


class DescribeTableStatisticsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeTableStatistics documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeTableStatistics)
    """

    def paginate(
        self,
        ReplicationTaskArn: str,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeTableStatisticsResponseTypeDef, None, None]:
        """
        [DescribeTableStatistics.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeTableStatistics.paginate)
        """
