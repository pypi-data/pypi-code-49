"""
Main interface for kinesisvideo service.

Usage::

    import boto3
    from mypy_boto3.kinesisvideo import (
        Client,
        KinesisVideoClient,
        ListSignalingChannelsPaginator,
        ListStreamsPaginator,
        )

    session = boto3.Session()

    client: KinesisVideoClient = boto3.client("kinesisvideo")
    session_client: KinesisVideoClient = session.client("kinesisvideo")

    list_signaling_channels_paginator: ListSignalingChannelsPaginator = client.get_paginator("list_signaling_channels")
    list_streams_paginator: ListStreamsPaginator = client.get_paginator("list_streams")
"""
from mypy_boto3_kinesisvideo.client import KinesisVideoClient as Client, KinesisVideoClient
from mypy_boto3_kinesisvideo.paginator import ListSignalingChannelsPaginator, ListStreamsPaginator


__all__ = ("Client", "KinesisVideoClient", "ListSignalingChannelsPaginator", "ListStreamsPaginator")
