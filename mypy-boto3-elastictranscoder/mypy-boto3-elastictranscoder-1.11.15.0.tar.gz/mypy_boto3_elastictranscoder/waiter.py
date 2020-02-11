"""
Main interface for elastictranscoder service client waiters.

Usage::

    import boto3
    from mypy_boto3.elastictranscoder import (
        JobCompleteWaiter,
    )

    client: ElasticTranscoderClient = boto3.client("elastictranscoder")

    job_complete_waiter: JobCompleteWaiter = client.get_waiter("job_complete")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from typing import TYPE_CHECKING
from botocore.waiter import Waiter as Boto3Waiter
from mypy_boto3_elastictranscoder.type_defs import WaiterConfigTypeDef


__all__ = ("JobCompleteWaiter",)


class JobCompleteWaiter(Boto3Waiter):
    """
    [Waiter.JobComplete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elastictranscoder.html#ElasticTranscoder.Waiter.JobComplete)
    """

    def wait(self, Id: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [JobComplete.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elastictranscoder.html#ElasticTranscoder.Waiter.JobComplete.wait)
        """
