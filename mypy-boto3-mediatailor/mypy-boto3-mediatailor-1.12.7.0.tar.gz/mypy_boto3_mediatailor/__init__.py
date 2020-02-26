"""
Main interface for mediatailor service.

Usage::

    import boto3
    from mypy_boto3.mediatailor import (
        Client,
        ListPlaybackConfigurationsPaginator,
        MediaTailorClient,
        )

    session = boto3.Session()

    client: MediaTailorClient = boto3.client("mediatailor")
    session_client: MediaTailorClient = session.client("mediatailor")

    list_playback_configurations_paginator: ListPlaybackConfigurationsPaginator = client.get_paginator("list_playback_configurations")
"""
from mypy_boto3_mediatailor.client import MediaTailorClient, MediaTailorClient as Client
from mypy_boto3_mediatailor.paginator import ListPlaybackConfigurationsPaginator


__all__ = ("Client", "ListPlaybackConfigurationsPaginator", "MediaTailorClient")
