"""
Main interface for mediatailor service client paginators.

Usage::

    import boto3
    from mypy_boto3.mediatailor import (
        ListPlaybackConfigurationsPaginator,
    )

    client: MediaTailorClient = boto3.client("mediatailor")

    list_playback_configurations_paginator: ListPlaybackConfigurationsPaginator = client.get_paginator("list_playback_configurations")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from typing import Generator, TYPE_CHECKING
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_mediatailor.type_defs import (
    ListPlaybackConfigurationsResponseTypeDef,
    PaginatorConfigTypeDef,
)


__all__ = ("ListPlaybackConfigurationsPaginator",)


class ListPlaybackConfigurationsPaginator(Boto3Paginator):
    """
    [Paginator.ListPlaybackConfigurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/mediatailor.html#MediaTailor.Paginator.ListPlaybackConfigurations)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListPlaybackConfigurationsResponseTypeDef, None, None]:
        """
        [ListPlaybackConfigurations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/mediatailor.html#MediaTailor.Paginator.ListPlaybackConfigurations.paginate)
        """
