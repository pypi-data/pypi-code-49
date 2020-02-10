"""
Main interface for support service.

Usage::

    import boto3
    from mypy_boto3.support import (
        Client,
        DescribeCasesPaginator,
        DescribeCommunicationsPaginator,
        SupportClient,
        )

    session = boto3.Session()

    client: SupportClient = boto3.client("support")
    session_client: SupportClient = session.client("support")

    describe_cases_paginator: DescribeCasesPaginator = client.get_paginator("describe_cases")
    describe_communications_paginator: DescribeCommunicationsPaginator = client.get_paginator("describe_communications")
"""
from mypy_boto3_support.client import SupportClient as Client, SupportClient
from mypy_boto3_support.paginator import DescribeCasesPaginator, DescribeCommunicationsPaginator


__all__ = ("Client", "DescribeCasesPaginator", "DescribeCommunicationsPaginator", "SupportClient")
