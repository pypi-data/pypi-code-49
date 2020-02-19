"""
Main interface for translate service.

Usage::

    import boto3
    from mypy_boto3.translate import (
        Client,
        ListTerminologiesPaginator,
        TranslateClient,
        )

    session = boto3.Session()

    client: TranslateClient = boto3.client("translate")
    session_client: TranslateClient = session.client("translate")

    list_terminologies_paginator: ListTerminologiesPaginator = client.get_paginator("list_terminologies")
"""
from mypy_boto3_translate.client import TranslateClient as Client, TranslateClient
from mypy_boto3_translate.paginator import ListTerminologiesPaginator


__all__ = ("Client", "ListTerminologiesPaginator", "TranslateClient")
