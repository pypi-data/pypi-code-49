"""
Main interface for pinpoint-email service client paginators.

Usage::

    import boto3
    from mypy_boto3.pinpoint_email import (
        GetDedicatedIpsPaginator,
        ListConfigurationSetsPaginator,
        ListDedicatedIpPoolsPaginator,
        ListDeliverabilityTestReportsPaginator,
        ListEmailIdentitiesPaginator,
    )

    client: PinpointEmailClient = boto3.client("pinpoint-email")

    get_dedicated_ips_paginator: GetDedicatedIpsPaginator = client.get_paginator("get_dedicated_ips")
    list_configuration_sets_paginator: ListConfigurationSetsPaginator = client.get_paginator("list_configuration_sets")
    list_dedicated_ip_pools_paginator: ListDedicatedIpPoolsPaginator = client.get_paginator("list_dedicated_ip_pools")
    list_deliverability_test_reports_paginator: ListDeliverabilityTestReportsPaginator = client.get_paginator("list_deliverability_test_reports")
    list_email_identities_paginator: ListEmailIdentitiesPaginator = client.get_paginator("list_email_identities")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from typing import Generator, TYPE_CHECKING
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_pinpoint_email.type_defs import (
    GetDedicatedIpsResponseTypeDef,
    ListConfigurationSetsResponseTypeDef,
    ListDedicatedIpPoolsResponseTypeDef,
    ListDeliverabilityTestReportsResponseTypeDef,
    ListEmailIdentitiesResponseTypeDef,
    PaginatorConfigTypeDef,
)


__all__ = (
    "GetDedicatedIpsPaginator",
    "ListConfigurationSetsPaginator",
    "ListDedicatedIpPoolsPaginator",
    "ListDeliverabilityTestReportsPaginator",
    "ListEmailIdentitiesPaginator",
)


class GetDedicatedIpsPaginator(Boto3Paginator):
    """
    [Paginator.GetDedicatedIps documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/pinpoint-email.html#PinpointEmail.Paginator.GetDedicatedIps)
    """

    def paginate(
        self, PoolName: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[GetDedicatedIpsResponseTypeDef, None, None]:
        """
        [GetDedicatedIps.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/pinpoint-email.html#PinpointEmail.Paginator.GetDedicatedIps.paginate)
        """


class ListConfigurationSetsPaginator(Boto3Paginator):
    """
    [Paginator.ListConfigurationSets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/pinpoint-email.html#PinpointEmail.Paginator.ListConfigurationSets)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListConfigurationSetsResponseTypeDef, None, None]:
        """
        [ListConfigurationSets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/pinpoint-email.html#PinpointEmail.Paginator.ListConfigurationSets.paginate)
        """


class ListDedicatedIpPoolsPaginator(Boto3Paginator):
    """
    [Paginator.ListDedicatedIpPools documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/pinpoint-email.html#PinpointEmail.Paginator.ListDedicatedIpPools)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListDedicatedIpPoolsResponseTypeDef, None, None]:
        """
        [ListDedicatedIpPools.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/pinpoint-email.html#PinpointEmail.Paginator.ListDedicatedIpPools.paginate)
        """


class ListDeliverabilityTestReportsPaginator(Boto3Paginator):
    """
    [Paginator.ListDeliverabilityTestReports documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/pinpoint-email.html#PinpointEmail.Paginator.ListDeliverabilityTestReports)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListDeliverabilityTestReportsResponseTypeDef, None, None]:
        """
        [ListDeliverabilityTestReports.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/pinpoint-email.html#PinpointEmail.Paginator.ListDeliverabilityTestReports.paginate)
        """


class ListEmailIdentitiesPaginator(Boto3Paginator):
    """
    [Paginator.ListEmailIdentities documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/pinpoint-email.html#PinpointEmail.Paginator.ListEmailIdentities)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListEmailIdentitiesResponseTypeDef, None, None]:
        """
        [ListEmailIdentities.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/pinpoint-email.html#PinpointEmail.Paginator.ListEmailIdentities.paginate)
        """
