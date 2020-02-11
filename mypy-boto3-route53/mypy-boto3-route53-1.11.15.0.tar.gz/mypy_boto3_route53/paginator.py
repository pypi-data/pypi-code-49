"""
Main interface for route53 service client paginators.

Usage::

    import boto3
    from mypy_boto3.route53 import (
        ListHealthChecksPaginator,
        ListHostedZonesPaginator,
        ListQueryLoggingConfigsPaginator,
        ListResourceRecordSetsPaginator,
        ListVPCAssociationAuthorizationsPaginator,
    )

    client: Route53Client = boto3.client("route53")

    list_health_checks_paginator: ListHealthChecksPaginator = client.get_paginator("list_health_checks")
    list_hosted_zones_paginator: ListHostedZonesPaginator = client.get_paginator("list_hosted_zones")
    list_query_logging_configs_paginator: ListQueryLoggingConfigsPaginator = client.get_paginator("list_query_logging_configs")
    list_resource_record_sets_paginator: ListResourceRecordSetsPaginator = client.get_paginator("list_resource_record_sets")
    list_vpc_association_authorizations_paginator: ListVPCAssociationAuthorizationsPaginator = client.get_paginator("list_vpc_association_authorizations")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from typing import Generator, TYPE_CHECKING
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_route53.type_defs import (
    ListHealthChecksResponseTypeDef,
    ListHostedZonesResponseTypeDef,
    ListQueryLoggingConfigsResponseTypeDef,
    ListResourceRecordSetsResponseTypeDef,
    ListVPCAssociationAuthorizationsResponseTypeDef,
    PaginatorConfigTypeDef,
)


__all__ = (
    "ListHealthChecksPaginator",
    "ListHostedZonesPaginator",
    "ListQueryLoggingConfigsPaginator",
    "ListResourceRecordSetsPaginator",
    "ListVPCAssociationAuthorizationsPaginator",
)


class ListHealthChecksPaginator(Boto3Paginator):
    """
    [Paginator.ListHealthChecks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/route53.html#Route53.Paginator.ListHealthChecks)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListHealthChecksResponseTypeDef, None, None]:
        """
        [ListHealthChecks.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/route53.html#Route53.Paginator.ListHealthChecks.paginate)
        """


class ListHostedZonesPaginator(Boto3Paginator):
    """
    [Paginator.ListHostedZones documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/route53.html#Route53.Paginator.ListHostedZones)
    """

    def paginate(
        self, DelegationSetId: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListHostedZonesResponseTypeDef, None, None]:
        """
        [ListHostedZones.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/route53.html#Route53.Paginator.ListHostedZones.paginate)
        """


class ListQueryLoggingConfigsPaginator(Boto3Paginator):
    """
    [Paginator.ListQueryLoggingConfigs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/route53.html#Route53.Paginator.ListQueryLoggingConfigs)
    """

    def paginate(
        self, HostedZoneId: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListQueryLoggingConfigsResponseTypeDef, None, None]:
        """
        [ListQueryLoggingConfigs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/route53.html#Route53.Paginator.ListQueryLoggingConfigs.paginate)
        """


class ListResourceRecordSetsPaginator(Boto3Paginator):
    """
    [Paginator.ListResourceRecordSets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/route53.html#Route53.Paginator.ListResourceRecordSets)
    """

    def paginate(
        self, HostedZoneId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListResourceRecordSetsResponseTypeDef, None, None]:
        """
        [ListResourceRecordSets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/route53.html#Route53.Paginator.ListResourceRecordSets.paginate)
        """


class ListVPCAssociationAuthorizationsPaginator(Boto3Paginator):
    """
    [Paginator.ListVPCAssociationAuthorizations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/route53.html#Route53.Paginator.ListVPCAssociationAuthorizations)
    """

    def paginate(
        self,
        HostedZoneId: str,
        MaxResults: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListVPCAssociationAuthorizationsResponseTypeDef, None, None]:
        """
        [ListVPCAssociationAuthorizations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/route53.html#Route53.Paginator.ListVPCAssociationAuthorizations.paginate)
        """
