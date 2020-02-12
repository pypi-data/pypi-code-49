"""
Main interface for ses service client waiters.

Usage::

    import boto3
    from mypy_boto3.ses import (
        IdentityExistsWaiter,
    )

    client: SESClient = boto3.client("ses")

    identity_exists_waiter: IdentityExistsWaiter = client.get_waiter("identity_exists")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from typing import List, TYPE_CHECKING
from botocore.waiter import Waiter as Boto3Waiter
from mypy_boto3_ses.type_defs import WaiterConfigTypeDef


__all__ = ("IdentityExistsWaiter",)


class IdentityExistsWaiter(Boto3Waiter):
    """
    [Waiter.IdentityExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ses.html#SES.Waiter.IdentityExists)
    """

    def wait(self, Identities: List[str], WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [IdentityExists.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ses.html#SES.Waiter.IdentityExists.wait)
        """
