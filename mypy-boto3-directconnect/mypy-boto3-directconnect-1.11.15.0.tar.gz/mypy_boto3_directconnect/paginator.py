"""
Main interface for directconnect service client paginators.

Usage::

    import boto3
    from mypy_boto3.directconnect import (
        DescribeDirectConnectGatewayAssociationsPaginator,
        DescribeDirectConnectGatewayAttachmentsPaginator,
        DescribeDirectConnectGatewaysPaginator,
    )

    client: DirectConnectClient = boto3.client("directconnect")

    describe_direct_connect_gateway_associations_paginator: DescribeDirectConnectGatewayAssociationsPaginator = client.get_paginator("describe_direct_connect_gateway_associations")
    describe_direct_connect_gateway_attachments_paginator: DescribeDirectConnectGatewayAttachmentsPaginator = client.get_paginator("describe_direct_connect_gateway_attachments")
    describe_direct_connect_gateways_paginator: DescribeDirectConnectGatewaysPaginator = client.get_paginator("describe_direct_connect_gateways")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from typing import Generator, TYPE_CHECKING
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_directconnect.type_defs import (
    DescribeDirectConnectGatewayAssociationsResultTypeDef,
    DescribeDirectConnectGatewayAttachmentsResultTypeDef,
    DescribeDirectConnectGatewaysResultTypeDef,
    PaginatorConfigTypeDef,
)


__all__ = (
    "DescribeDirectConnectGatewayAssociationsPaginator",
    "DescribeDirectConnectGatewayAttachmentsPaginator",
    "DescribeDirectConnectGatewaysPaginator",
)


class DescribeDirectConnectGatewayAssociationsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeDirectConnectGatewayAssociations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/directconnect.html#DirectConnect.Paginator.DescribeDirectConnectGatewayAssociations)
    """

    def paginate(
        self,
        associationId: str = None,
        associatedGatewayId: str = None,
        directConnectGatewayId: str = None,
        virtualGatewayId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeDirectConnectGatewayAssociationsResultTypeDef, None, None]:
        """
        [DescribeDirectConnectGatewayAssociations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/directconnect.html#DirectConnect.Paginator.DescribeDirectConnectGatewayAssociations.paginate)
        """


class DescribeDirectConnectGatewayAttachmentsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeDirectConnectGatewayAttachments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/directconnect.html#DirectConnect.Paginator.DescribeDirectConnectGatewayAttachments)
    """

    def paginate(
        self,
        directConnectGatewayId: str = None,
        virtualInterfaceId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeDirectConnectGatewayAttachmentsResultTypeDef, None, None]:
        """
        [DescribeDirectConnectGatewayAttachments.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/directconnect.html#DirectConnect.Paginator.DescribeDirectConnectGatewayAttachments.paginate)
        """


class DescribeDirectConnectGatewaysPaginator(Boto3Paginator):
    """
    [Paginator.DescribeDirectConnectGateways documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/directconnect.html#DirectConnect.Paginator.DescribeDirectConnectGateways)
    """

    def paginate(
        self, directConnectGatewayId: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[DescribeDirectConnectGatewaysResultTypeDef, None, None]:
        """
        [DescribeDirectConnectGateways.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/directconnect.html#DirectConnect.Paginator.DescribeDirectConnectGateways.paginate)
        """
