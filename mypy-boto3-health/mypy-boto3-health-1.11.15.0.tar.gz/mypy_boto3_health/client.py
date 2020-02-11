"""
Main interface for health service client

Usage::

    import boto3
    from mypy_boto3.health import HealthClient

    session = boto3.Session()

    client: HealthClient = boto3.client("health")
    session_client: HealthClient = session.client("health")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_health.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_health.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_health.type_defs import (
    ClientDescribeAffectedAccountsForOrganizationResponseTypeDef,
    ClientDescribeAffectedEntitiesFilterTypeDef,
    ClientDescribeAffectedEntitiesForOrganizationOrganizationEntityFiltersTypeDef,
    ClientDescribeAffectedEntitiesForOrganizationResponseTypeDef,
    ClientDescribeAffectedEntitiesResponseTypeDef,
    ClientDescribeEntityAggregatesResponseTypeDef,
    ClientDescribeEventAggregatesFilterTypeDef,
    ClientDescribeEventAggregatesResponseTypeDef,
    ClientDescribeEventDetailsForOrganizationOrganizationEventDetailFiltersTypeDef,
    ClientDescribeEventDetailsForOrganizationResponseTypeDef,
    ClientDescribeEventDetailsResponseTypeDef,
    ClientDescribeEventTypesFilterTypeDef,
    ClientDescribeEventTypesResponseTypeDef,
    ClientDescribeEventsFilterTypeDef,
    ClientDescribeEventsForOrganizationFilterTypeDef,
    ClientDescribeEventsForOrganizationResponseTypeDef,
    ClientDescribeEventsResponseTypeDef,
    ClientDescribeHealthServiceStatusForOrganizationResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("HealthClient",)


class HealthClient:
    """
    [Health.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/health.html#Health.Client)
    """

    exceptions: "client_scope.Exceptions"

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/health.html#Health.Client.can_paginate)
        """

    def describe_affected_accounts_for_organization(
        self, eventArn: str, nextToken: str = None, maxResults: int = None
    ) -> ClientDescribeAffectedAccountsForOrganizationResponseTypeDef:
        """
        [Client.describe_affected_accounts_for_organization documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/health.html#Health.Client.describe_affected_accounts_for_organization)
        """

    def describe_affected_entities(
        self,
        filter: ClientDescribeAffectedEntitiesFilterTypeDef,
        locale: str = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ClientDescribeAffectedEntitiesResponseTypeDef:
        """
        [Client.describe_affected_entities documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/health.html#Health.Client.describe_affected_entities)
        """

    def describe_affected_entities_for_organization(
        self,
        organizationEntityFilters: List[
            ClientDescribeAffectedEntitiesForOrganizationOrganizationEntityFiltersTypeDef
        ],
        locale: str = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ClientDescribeAffectedEntitiesForOrganizationResponseTypeDef:
        """
        [Client.describe_affected_entities_for_organization documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/health.html#Health.Client.describe_affected_entities_for_organization)
        """

    def describe_entity_aggregates(
        self, eventArns: List[str] = None
    ) -> ClientDescribeEntityAggregatesResponseTypeDef:
        """
        [Client.describe_entity_aggregates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/health.html#Health.Client.describe_entity_aggregates)
        """

    def describe_event_aggregates(
        self,
        aggregateField: str,
        filter: ClientDescribeEventAggregatesFilterTypeDef = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> ClientDescribeEventAggregatesResponseTypeDef:
        """
        [Client.describe_event_aggregates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/health.html#Health.Client.describe_event_aggregates)
        """

    def describe_event_details(
        self, eventArns: List[str], locale: str = None
    ) -> ClientDescribeEventDetailsResponseTypeDef:
        """
        [Client.describe_event_details documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/health.html#Health.Client.describe_event_details)
        """

    def describe_event_details_for_organization(
        self,
        organizationEventDetailFilters: List[
            ClientDescribeEventDetailsForOrganizationOrganizationEventDetailFiltersTypeDef
        ],
        locale: str = None,
    ) -> ClientDescribeEventDetailsForOrganizationResponseTypeDef:
        """
        [Client.describe_event_details_for_organization documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/health.html#Health.Client.describe_event_details_for_organization)
        """

    def describe_event_types(
        self,
        filter: ClientDescribeEventTypesFilterTypeDef = None,
        locale: str = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ClientDescribeEventTypesResponseTypeDef:
        """
        [Client.describe_event_types documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/health.html#Health.Client.describe_event_types)
        """

    def describe_events(
        self,
        filter: ClientDescribeEventsFilterTypeDef = None,
        nextToken: str = None,
        maxResults: int = None,
        locale: str = None,
    ) -> ClientDescribeEventsResponseTypeDef:
        """
        [Client.describe_events documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/health.html#Health.Client.describe_events)
        """

    def describe_events_for_organization(
        self,
        filter: ClientDescribeEventsForOrganizationFilterTypeDef = None,
        nextToken: str = None,
        maxResults: int = None,
        locale: str = None,
    ) -> ClientDescribeEventsForOrganizationResponseTypeDef:
        """
        [Client.describe_events_for_organization documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/health.html#Health.Client.describe_events_for_organization)
        """

    def describe_health_service_status_for_organization(
        self, *args: Any, **kwargs: Any
    ) -> ClientDescribeHealthServiceStatusForOrganizationResponseTypeDef:
        """
        [Client.describe_health_service_status_for_organization documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/health.html#Health.Client.describe_health_service_status_for_organization)
        """

    def disable_health_service_access_for_organization(self, *args: Any, **kwargs: Any) -> None:
        """
        [Client.disable_health_service_access_for_organization documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/health.html#Health.Client.disable_health_service_access_for_organization)
        """

    def enable_health_service_access_for_organization(self, *args: Any, **kwargs: Any) -> None:
        """
        [Client.enable_health_service_access_for_organization documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/health.html#Health.Client.enable_health_service_access_for_organization)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/health.html#Health.Client.generate_presigned_url)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_affected_accounts_for_organization"]
    ) -> "paginator_scope.DescribeAffectedAccountsForOrganizationPaginator":
        """
        [Paginator.DescribeAffectedAccountsForOrganization documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/health.html#Health.Paginator.DescribeAffectedAccountsForOrganization)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_affected_entities"]
    ) -> "paginator_scope.DescribeAffectedEntitiesPaginator":
        """
        [Paginator.DescribeAffectedEntities documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/health.html#Health.Paginator.DescribeAffectedEntities)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_affected_entities_for_organization"]
    ) -> "paginator_scope.DescribeAffectedEntitiesForOrganizationPaginator":
        """
        [Paginator.DescribeAffectedEntitiesForOrganization documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/health.html#Health.Paginator.DescribeAffectedEntitiesForOrganization)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_event_aggregates"]
    ) -> "paginator_scope.DescribeEventAggregatesPaginator":
        """
        [Paginator.DescribeEventAggregates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/health.html#Health.Paginator.DescribeEventAggregates)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_event_types"]
    ) -> "paginator_scope.DescribeEventTypesPaginator":
        """
        [Paginator.DescribeEventTypes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/health.html#Health.Paginator.DescribeEventTypes)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_events"]
    ) -> "paginator_scope.DescribeEventsPaginator":
        """
        [Paginator.DescribeEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/health.html#Health.Paginator.DescribeEvents)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_events_for_organization"]
    ) -> "paginator_scope.DescribeEventsForOrganizationPaginator":
        """
        [Paginator.DescribeEventsForOrganization documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/health.html#Health.Paginator.DescribeEventsForOrganization)
        """


class Exceptions:
    ClientError: Boto3ClientError
    ConcurrentModificationException: Boto3ClientError
    InvalidPaginationToken: Boto3ClientError
    UnsupportedLocale: Boto3ClientError
