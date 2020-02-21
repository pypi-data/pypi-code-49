"""
Main interface for sagemaker-runtime service.

Usage::

    import boto3
    from mypy_boto3.sagemaker_runtime import (
        Client,
        SageMakerRuntimeClient,
        )

    session = boto3.Session()

    client: SageMakerRuntimeClient = boto3.client("sagemaker-runtime")
    session_client: SageMakerRuntimeClient = session.client("sagemaker-runtime")
"""
from mypy_boto3_sagemaker_runtime.client import (
    SageMakerRuntimeClient,
    SageMakerRuntimeClient as Client,
)


__all__ = ("Client", "SageMakerRuntimeClient")
