"""
Main interface for cur service.

Usage::

    import boto3
    from mypy_boto3.cur import (
        Client,
        CostandUsageReportServiceClient,
        DescribeReportDefinitionsPaginator,
        )

    session = boto3.Session()

    client: CostandUsageReportServiceClient = boto3.client("cur")
    session_client: CostandUsageReportServiceClient = session.client("cur")

    describe_report_definitions_paginator: DescribeReportDefinitionsPaginator = client.get_paginator("describe_report_definitions")
"""
from mypy_boto3_cur.client import (
    CostandUsageReportServiceClient,
    CostandUsageReportServiceClient as Client,
)
from mypy_boto3_cur.paginator import DescribeReportDefinitionsPaginator


__all__ = ("Client", "CostandUsageReportServiceClient", "DescribeReportDefinitionsPaginator")
