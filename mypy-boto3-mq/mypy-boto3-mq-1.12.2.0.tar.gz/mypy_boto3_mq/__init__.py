"""
Main interface for mq service.

Usage::

    import boto3
    from mypy_boto3.mq import (
        Client,
        ListBrokersPaginator,
        MQClient,
        )

    session = boto3.Session()

    client: MQClient = boto3.client("mq")
    session_client: MQClient = session.client("mq")

    list_brokers_paginator: ListBrokersPaginator = client.get_paginator("list_brokers")
"""
from mypy_boto3_mq.client import MQClient, MQClient as Client
from mypy_boto3_mq.paginator import ListBrokersPaginator


__all__ = ("Client", "ListBrokersPaginator", "MQClient")
