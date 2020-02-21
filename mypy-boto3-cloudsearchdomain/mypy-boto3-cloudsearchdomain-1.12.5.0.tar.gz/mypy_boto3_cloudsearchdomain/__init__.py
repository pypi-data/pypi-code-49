"""
Main interface for cloudsearchdomain service.

Usage::

    import boto3
    from mypy_boto3.cloudsearchdomain import (
        Client,
        CloudSearchDomainClient,
        )

    session = boto3.Session()

    client: CloudSearchDomainClient = boto3.client("cloudsearchdomain")
    session_client: CloudSearchDomainClient = session.client("cloudsearchdomain")
"""
from mypy_boto3_cloudsearchdomain.client import (
    CloudSearchDomainClient as Client,
    CloudSearchDomainClient,
)


__all__ = ("Client", "CloudSearchDomainClient")
