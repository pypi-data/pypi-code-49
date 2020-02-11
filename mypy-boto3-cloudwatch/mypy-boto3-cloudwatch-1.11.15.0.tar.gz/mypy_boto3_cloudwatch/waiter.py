"""
Main interface for cloudwatch service client waiters.

Usage::

    import boto3
    from mypy_boto3.cloudwatch import (
        AlarmExistsWaiter,
    )

    client: CloudWatchClient = boto3.client("cloudwatch")

    alarm_exists_waiter: AlarmExistsWaiter = client.get_waiter("alarm_exists")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import List, TYPE_CHECKING
from botocore.waiter import Waiter as Boto3Waiter
from mypy_boto3_cloudwatch.type_defs import WaiterConfigTypeDef

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("AlarmExistsWaiter",)


class AlarmExistsWaiter(Boto3Waiter):
    """
    [Waiter.AlarmExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudwatch.html#CloudWatch.Waiter.AlarmExists)
    """

    def wait(
        self,
        AlarmNames: List[str] = None,
        AlarmNamePrefix: str = None,
        StateValue: Literal["OK", "ALARM", "INSUFFICIENT_DATA"] = None,
        ActionPrefix: str = None,
        MaxRecords: int = None,
        NextToken: str = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [AlarmExists.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudwatch.html#CloudWatch.Waiter.AlarmExists.wait)
        """
