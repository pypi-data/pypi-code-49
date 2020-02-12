"""
Main interface for medialive service client paginators.

Usage::

    import boto3
    from mypy_boto3.medialive import (
        DescribeSchedulePaginator,
        ListChannelsPaginator,
        ListInputSecurityGroupsPaginator,
        ListInputsPaginator,
        ListMultiplexProgramsPaginator,
        ListMultiplexesPaginator,
        ListOfferingsPaginator,
        ListReservationsPaginator,
    )

    client: MediaLiveClient = boto3.client("medialive")

    describe_schedule_paginator: DescribeSchedulePaginator = client.get_paginator("describe_schedule")
    list_channels_paginator: ListChannelsPaginator = client.get_paginator("list_channels")
    list_input_security_groups_paginator: ListInputSecurityGroupsPaginator = client.get_paginator("list_input_security_groups")
    list_inputs_paginator: ListInputsPaginator = client.get_paginator("list_inputs")
    list_multiplex_programs_paginator: ListMultiplexProgramsPaginator = client.get_paginator("list_multiplex_programs")
    list_multiplexes_paginator: ListMultiplexesPaginator = client.get_paginator("list_multiplexes")
    list_offerings_paginator: ListOfferingsPaginator = client.get_paginator("list_offerings")
    list_reservations_paginator: ListReservationsPaginator = client.get_paginator("list_reservations")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from typing import Generator, TYPE_CHECKING
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_medialive.type_defs import (
    DescribeScheduleResponseTypeDef,
    ListChannelsResponseTypeDef,
    ListInputSecurityGroupsResponseTypeDef,
    ListInputsResponseTypeDef,
    ListMultiplexProgramsResponseTypeDef,
    ListMultiplexesResponseTypeDef,
    ListOfferingsResponseTypeDef,
    ListReservationsResponseTypeDef,
    PaginatorConfigTypeDef,
)


__all__ = (
    "DescribeSchedulePaginator",
    "ListChannelsPaginator",
    "ListInputSecurityGroupsPaginator",
    "ListInputsPaginator",
    "ListMultiplexProgramsPaginator",
    "ListMultiplexesPaginator",
    "ListOfferingsPaginator",
    "ListReservationsPaginator",
)


class DescribeSchedulePaginator(Boto3Paginator):
    """
    [Paginator.DescribeSchedule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/medialive.html#MediaLive.Paginator.DescribeSchedule)
    """

    def paginate(
        self, ChannelId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[DescribeScheduleResponseTypeDef, None, None]:
        """
        [DescribeSchedule.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/medialive.html#MediaLive.Paginator.DescribeSchedule.paginate)
        """


class ListChannelsPaginator(Boto3Paginator):
    """
    [Paginator.ListChannels documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/medialive.html#MediaLive.Paginator.ListChannels)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListChannelsResponseTypeDef, None, None]:
        """
        [ListChannels.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/medialive.html#MediaLive.Paginator.ListChannels.paginate)
        """


class ListInputSecurityGroupsPaginator(Boto3Paginator):
    """
    [Paginator.ListInputSecurityGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/medialive.html#MediaLive.Paginator.ListInputSecurityGroups)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListInputSecurityGroupsResponseTypeDef, None, None]:
        """
        [ListInputSecurityGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/medialive.html#MediaLive.Paginator.ListInputSecurityGroups.paginate)
        """


class ListInputsPaginator(Boto3Paginator):
    """
    [Paginator.ListInputs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/medialive.html#MediaLive.Paginator.ListInputs)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListInputsResponseTypeDef, None, None]:
        """
        [ListInputs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/medialive.html#MediaLive.Paginator.ListInputs.paginate)
        """


class ListMultiplexProgramsPaginator(Boto3Paginator):
    """
    [Paginator.ListMultiplexPrograms documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/medialive.html#MediaLive.Paginator.ListMultiplexPrograms)
    """

    def paginate(
        self, MultiplexId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListMultiplexProgramsResponseTypeDef, None, None]:
        """
        [ListMultiplexPrograms.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/medialive.html#MediaLive.Paginator.ListMultiplexPrograms.paginate)
        """


class ListMultiplexesPaginator(Boto3Paginator):
    """
    [Paginator.ListMultiplexes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/medialive.html#MediaLive.Paginator.ListMultiplexes)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListMultiplexesResponseTypeDef, None, None]:
        """
        [ListMultiplexes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/medialive.html#MediaLive.Paginator.ListMultiplexes.paginate)
        """


class ListOfferingsPaginator(Boto3Paginator):
    """
    [Paginator.ListOfferings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/medialive.html#MediaLive.Paginator.ListOfferings)
    """

    def paginate(
        self,
        ChannelClass: str = None,
        ChannelConfiguration: str = None,
        Codec: str = None,
        Duration: str = None,
        MaximumBitrate: str = None,
        MaximumFramerate: str = None,
        Resolution: str = None,
        ResourceType: str = None,
        SpecialFeature: str = None,
        VideoQuality: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListOfferingsResponseTypeDef, None, None]:
        """
        [ListOfferings.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/medialive.html#MediaLive.Paginator.ListOfferings.paginate)
        """


class ListReservationsPaginator(Boto3Paginator):
    """
    [Paginator.ListReservations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/medialive.html#MediaLive.Paginator.ListReservations)
    """

    def paginate(
        self,
        ChannelClass: str = None,
        Codec: str = None,
        MaximumBitrate: str = None,
        MaximumFramerate: str = None,
        Resolution: str = None,
        ResourceType: str = None,
        SpecialFeature: str = None,
        VideoQuality: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListReservationsResponseTypeDef, None, None]:
        """
        [ListReservations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/medialive.html#MediaLive.Paginator.ListReservations.paginate)
        """
