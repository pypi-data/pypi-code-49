"""
Main interface for elastic-inference service.

Usage::

    import boto3
    from mypy_boto3.elastic_inference import (
        Client,
        ElasticInferenceClient,
        )

    session = boto3.Session()

    client: ElasticInferenceClient = boto3.client("elastic-inference")
    session_client: ElasticInferenceClient = session.client("elastic-inference")
"""
from mypy_boto3_elastic_inference.client import (
    ElasticInferenceClient,
    ElasticInferenceClient as Client,
)


__all__ = ("Client", "ElasticInferenceClient")
