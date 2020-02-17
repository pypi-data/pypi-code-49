"""
Main interface for acm service.

Usage::

    import boto3
    from mypy_boto3.acm import (
        ACMClient,
        CertificateValidatedWaiter,
        Client,
        ListCertificatesPaginator,
        )

    session = boto3.Session()

    client: ACMClient = boto3.client("acm")
    session_client: ACMClient = session.client("acm")

    certificate_validated_waiter: CertificateValidatedWaiter = client.get_waiter("certificate_validated")

    list_certificates_paginator: ListCertificatesPaginator = client.get_paginator("list_certificates")
"""
from mypy_boto3_acm.client import ACMClient, ACMClient as Client
from mypy_boto3_acm.paginator import ListCertificatesPaginator
from mypy_boto3_acm.waiter import CertificateValidatedWaiter


__all__ = ("ACMClient", "CertificateValidatedWaiter", "Client", "ListCertificatesPaginator")
