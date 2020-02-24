"""
Main interface for secretsmanager service.

Usage::

    import boto3
    from mypy_boto3.secretsmanager import (
        Client,
        ListSecretsPaginator,
        SecretsManagerClient,
        )

    session = boto3.Session()

    client: SecretsManagerClient = boto3.client("secretsmanager")
    session_client: SecretsManagerClient = session.client("secretsmanager")

    list_secrets_paginator: ListSecretsPaginator = client.get_paginator("list_secrets")
"""
from mypy_boto3_secretsmanager.client import SecretsManagerClient as Client, SecretsManagerClient
from mypy_boto3_secretsmanager.paginator import ListSecretsPaginator


__all__ = ("Client", "ListSecretsPaginator", "SecretsManagerClient")
