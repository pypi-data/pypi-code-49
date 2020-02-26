"""
Main interface for application-insights service.

Usage::

    import boto3
    from mypy_boto3.application_insights import (
        ApplicationInsightsClient,
        Client,
        )

    session = boto3.Session()

    client: ApplicationInsightsClient = boto3.client("application-insights")
    session_client: ApplicationInsightsClient = session.client("application-insights")
"""
from mypy_boto3_application_insights.client import (
    ApplicationInsightsClient,
    ApplicationInsightsClient as Client,
)


__all__ = ("ApplicationInsightsClient", "Client")
