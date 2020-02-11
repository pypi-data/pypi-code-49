"""
Main interface for signer service client waiters.

Usage::

    import boto3
    from mypy_boto3.signer import (
        SuccessfulSigningJobWaiter,
    )

    client: SignerClient = boto3.client("signer")

    successful_signing_job_waiter: SuccessfulSigningJobWaiter = client.get_waiter("successful_signing_job")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from typing import TYPE_CHECKING
from botocore.waiter import Waiter as Boto3Waiter
from mypy_boto3_signer.type_defs import WaiterConfigTypeDef


__all__ = ("SuccessfulSigningJobWaiter",)


class SuccessfulSigningJobWaiter(Boto3Waiter):
    """
    [Waiter.SuccessfulSigningJob documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/signer.html#Signer.Waiter.SuccessfulSigningJob)
    """

    def wait(self, jobId: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [SuccessfulSigningJob.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/signer.html#Signer.Waiter.SuccessfulSigningJob.wait)
        """
