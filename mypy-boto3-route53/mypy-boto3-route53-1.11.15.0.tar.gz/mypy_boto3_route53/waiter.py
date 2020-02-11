"""
Main interface for route53 service client waiters.

Usage::

    import boto3
    from mypy_boto3.route53 import (
        ResourceRecordSetsChangedWaiter,
    )

    client: Route53Client = boto3.client("route53")

    resource_record_sets_changed_waiter: ResourceRecordSetsChangedWaiter = client.get_waiter("resource_record_sets_changed")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from typing import TYPE_CHECKING
from botocore.waiter import Waiter as Boto3Waiter
from mypy_boto3_route53.type_defs import WaiterConfigTypeDef


__all__ = ("ResourceRecordSetsChangedWaiter",)


class ResourceRecordSetsChangedWaiter(Boto3Waiter):
    """
    [Waiter.ResourceRecordSetsChanged documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/route53.html#Route53.Waiter.ResourceRecordSetsChanged)
    """

    def wait(self, Id: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [ResourceRecordSetsChanged.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/route53.html#Route53.Waiter.ResourceRecordSetsChanged.wait)
        """
