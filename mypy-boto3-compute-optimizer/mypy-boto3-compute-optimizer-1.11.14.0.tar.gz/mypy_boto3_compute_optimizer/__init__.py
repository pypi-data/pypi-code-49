"""
Main interface for compute-optimizer service.

Usage::

    import boto3
    from mypy_boto3.compute_optimizer import (
        Client,
        ComputeOptimizerClient,
        )

    session = boto3.Session()

    client: ComputeOptimizerClient = boto3.client("compute-optimizer")
    session_client: ComputeOptimizerClient = session.client("compute-optimizer")
"""
from mypy_boto3_compute_optimizer.client import (
    ComputeOptimizerClient,
    ComputeOptimizerClient as Client,
)


__all__ = ("Client", "ComputeOptimizerClient")
