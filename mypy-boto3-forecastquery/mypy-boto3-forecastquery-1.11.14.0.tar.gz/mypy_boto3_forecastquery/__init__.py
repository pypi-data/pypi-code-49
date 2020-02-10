"""
Main interface for forecastquery service.

Usage::

    import boto3
    from mypy_boto3.forecastquery import (
        Client,
        ForecastQueryServiceClient,
        )

    session = boto3.Session()

    client: ForecastQueryServiceClient = boto3.client("forecastquery")
    session_client: ForecastQueryServiceClient = session.client("forecastquery")
"""
from mypy_boto3_forecastquery.client import (
    ForecastQueryServiceClient,
    ForecastQueryServiceClient as Client,
)


__all__ = ("Client", "ForecastQueryServiceClient")
