"""
Main interface for health service client paginators.

Usage::

    import boto3
    from mypy_boto3.health import (
        DescribeAffectedAccountsForOrganizationPaginator,
        DescribeAffectedEntitiesPaginator,
        DescribeAffectedEntitiesForOrganizationPaginator,
        DescribeEventAggregatesPaginator,
        DescribeEventTypesPaginator,
        DescribeEventsPaginator,
        DescribeEventsForOrganizationPaginator,
    )

    client: HealthClient = boto3.client("health")

    describe_affected_accounts_for_organization_paginator: DescribeAffectedAccountsForOrganizationPaginator = client.get_paginator("describe_affected_accounts_for_organization")
    describe_affected_entities_paginator: DescribeAffectedEntitiesPaginator = client.get_paginator("describe_affected_entities")
    describe_affected_entities_for_organization_paginator: DescribeAffectedEntitiesForOrganizationPaginator = client.get_paginator("describe_affected_entities_for_organization")
    describe_event_aggregates_paginator: DescribeEventAggregatesPaginator = client.get_paginator("describe_event_aggregates")
    describe_event_types_paginator: DescribeEventTypesPaginator = client.get_paginator("describe_event_types")
    describe_events_paginator: DescribeEventsPaginator = client.get_paginator("describe_events")
    describe_events_for_organization_paginator: DescribeEventsForOrganizationPaginator = client.get_paginator("describe_events_for_organization")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Generator, List, TYPE_CHECKING
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_health.type_defs import (
    DescribeAffectedAccountsForOrganizationResponseTypeDef,
    DescribeAffectedEntitiesForOrganizationResponseTypeDef,
    DescribeAffectedEntitiesResponseTypeDef,
    DescribeEventAggregatesResponseTypeDef,
    DescribeEventTypesResponseTypeDef,
    DescribeEventsForOrganizationResponseTypeDef,
    DescribeEventsResponseTypeDef,
    EntityFilterTypeDef,
    EventAccountFilterTypeDef,
    EventFilterTypeDef,
    EventTypeFilterTypeDef,
    OrganizationEventFilterTypeDef,
    PaginatorConfigTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "DescribeAffectedAccountsForOrganizationPaginator",
    "DescribeAffectedEntitiesPaginator",
    "DescribeAffectedEntitiesForOrganizationPaginator",
    "DescribeEventAggregatesPaginator",
    "DescribeEventTypesPaginator",
    "DescribeEventsPaginator",
    "DescribeEventsForOrganizationPaginator",
)


class DescribeAffectedAccountsForOrganizationPaginator(Boto3Paginator):
    """
    [Paginator.DescribeAffectedAccountsForOrganization documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/health.html#Health.Paginator.DescribeAffectedAccountsForOrganization)
    """

    def paginate(
        self, eventArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[DescribeAffectedAccountsForOrganizationResponseTypeDef, None, None]:
        """
        [DescribeAffectedAccountsForOrganization.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/health.html#Health.Paginator.DescribeAffectedAccountsForOrganization.paginate)
        """


class DescribeAffectedEntitiesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeAffectedEntities documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/health.html#Health.Paginator.DescribeAffectedEntities)
    """

    def paginate(
        self,
        filter: EntityFilterTypeDef,
        locale: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeAffectedEntitiesResponseTypeDef, None, None]:
        """
        [DescribeAffectedEntities.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/health.html#Health.Paginator.DescribeAffectedEntities.paginate)
        """


class DescribeAffectedEntitiesForOrganizationPaginator(Boto3Paginator):
    """
    [Paginator.DescribeAffectedEntitiesForOrganization documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/health.html#Health.Paginator.DescribeAffectedEntitiesForOrganization)
    """

    def paginate(
        self,
        organizationEntityFilters: List[EventAccountFilterTypeDef],
        locale: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeAffectedEntitiesForOrganizationResponseTypeDef, None, None]:
        """
        [DescribeAffectedEntitiesForOrganization.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/health.html#Health.Paginator.DescribeAffectedEntitiesForOrganization.paginate)
        """


class DescribeEventAggregatesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeEventAggregates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/health.html#Health.Paginator.DescribeEventAggregates)
    """

    def paginate(
        self,
        aggregateField: Literal["eventTypeCategory"],
        filter: EventFilterTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeEventAggregatesResponseTypeDef, None, None]:
        """
        [DescribeEventAggregates.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/health.html#Health.Paginator.DescribeEventAggregates.paginate)
        """


class DescribeEventTypesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeEventTypes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/health.html#Health.Paginator.DescribeEventTypes)
    """

    def paginate(
        self,
        filter: EventTypeFilterTypeDef = None,
        locale: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeEventTypesResponseTypeDef, None, None]:
        """
        [DescribeEventTypes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/health.html#Health.Paginator.DescribeEventTypes.paginate)
        """


class DescribeEventsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/health.html#Health.Paginator.DescribeEvents)
    """

    def paginate(
        self,
        filter: EventFilterTypeDef = None,
        locale: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeEventsResponseTypeDef, None, None]:
        """
        [DescribeEvents.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/health.html#Health.Paginator.DescribeEvents.paginate)
        """


class DescribeEventsForOrganizationPaginator(Boto3Paginator):
    """
    [Paginator.DescribeEventsForOrganization documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/health.html#Health.Paginator.DescribeEventsForOrganization)
    """

    def paginate(
        self,
        filter: OrganizationEventFilterTypeDef = None,
        locale: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeEventsForOrganizationResponseTypeDef, None, None]:
        """
        [DescribeEventsForOrganization.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/health.html#Health.Paginator.DescribeEventsForOrganization.paginate)
        """
