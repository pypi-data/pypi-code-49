"""
Main interface for opsworkscm service client waiters.

Usage::

    import boto3
    from mypy_boto3.opsworkscm import (
        NodeAssociatedWaiter,
    )

    client: OpsWorksCMClient = boto3.client("opsworkscm")

    node_associated_waiter: NodeAssociatedWaiter = client.get_waiter("node_associated")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from typing import TYPE_CHECKING
from botocore.waiter import Waiter as Boto3Waiter
from mypy_boto3_opsworkscm.type_defs import WaiterConfigTypeDef


__all__ = ("NodeAssociatedWaiter",)


class NodeAssociatedWaiter(Boto3Waiter):
    """
    [Waiter.NodeAssociated documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/opsworkscm.html#OpsWorksCM.Waiter.NodeAssociated)
    """

    def wait(
        self,
        NodeAssociationStatusToken: str,
        ServerName: str,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [NodeAssociated.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/opsworkscm.html#OpsWorksCM.Waiter.NodeAssociated.wait)
        """
