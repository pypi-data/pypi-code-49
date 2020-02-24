"""
Main interface for apigatewaymanagementapi service.

Usage::

    import boto3
    from mypy_boto3.apigatewaymanagementapi import (
        ApiGatewayManagementApiClient,
        Client,
        )

    session = boto3.Session()

    client: ApiGatewayManagementApiClient = boto3.client("apigatewaymanagementapi")
    session_client: ApiGatewayManagementApiClient = session.client("apigatewaymanagementapi")
"""
from mypy_boto3_apigatewaymanagementapi.client import (
    ApiGatewayManagementApiClient as Client,
    ApiGatewayManagementApiClient,
)


__all__ = ("ApiGatewayManagementApiClient", "Client")
