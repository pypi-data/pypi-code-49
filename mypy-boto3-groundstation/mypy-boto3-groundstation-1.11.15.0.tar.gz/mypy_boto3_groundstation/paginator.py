"""
Main interface for groundstation service client paginators.

Usage::

    import boto3
    from mypy_boto3.groundstation import (
        ListConfigsPaginator,
        ListContactsPaginator,
        ListDataflowEndpointGroupsPaginator,
        ListGroundStationsPaginator,
        ListMissionProfilesPaginator,
        ListSatellitesPaginator,
    )

    client: GroundStationClient = boto3.client("groundstation")

    list_configs_paginator: ListConfigsPaginator = client.get_paginator("list_configs")
    list_contacts_paginator: ListContactsPaginator = client.get_paginator("list_contacts")
    list_dataflow_endpoint_groups_paginator: ListDataflowEndpointGroupsPaginator = client.get_paginator("list_dataflow_endpoint_groups")
    list_ground_stations_paginator: ListGroundStationsPaginator = client.get_paginator("list_ground_stations")
    list_mission_profiles_paginator: ListMissionProfilesPaginator = client.get_paginator("list_mission_profiles")
    list_satellites_paginator: ListSatellitesPaginator = client.get_paginator("list_satellites")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from datetime import datetime
import sys
from typing import Generator, List, TYPE_CHECKING
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_groundstation.type_defs import (
    ListConfigsResponseTypeDef,
    ListContactsResponseTypeDef,
    ListDataflowEndpointGroupsResponseTypeDef,
    ListGroundStationsResponseTypeDef,
    ListMissionProfilesResponseTypeDef,
    ListSatellitesResponseTypeDef,
    PaginatorConfigTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ListConfigsPaginator",
    "ListContactsPaginator",
    "ListDataflowEndpointGroupsPaginator",
    "ListGroundStationsPaginator",
    "ListMissionProfilesPaginator",
    "ListSatellitesPaginator",
)


class ListConfigsPaginator(Boto3Paginator):
    """
    [Paginator.ListConfigs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/groundstation.html#GroundStation.Paginator.ListConfigs)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListConfigsResponseTypeDef, None, None]:
        """
        [ListConfigs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/groundstation.html#GroundStation.Paginator.ListConfigs.paginate)
        """


class ListContactsPaginator(Boto3Paginator):
    """
    [Paginator.ListContacts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/groundstation.html#GroundStation.Paginator.ListContacts)
    """

    def paginate(
        self,
        endTime: datetime,
        startTime: datetime,
        statusList: List[
            Literal[
                "AVAILABLE",
                "AWS_CANCELLED",
                "CANCELLED",
                "CANCELLING",
                "COMPLETED",
                "FAILED",
                "FAILED_TO_SCHEDULE",
                "PASS",
                "POSTPASS",
                "PREPASS",
                "SCHEDULED",
                "SCHEDULING",
            ]
        ],
        groundStation: str = None,
        missionProfileArn: str = None,
        satelliteArn: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListContactsResponseTypeDef, None, None]:
        """
        [ListContacts.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/groundstation.html#GroundStation.Paginator.ListContacts.paginate)
        """


class ListDataflowEndpointGroupsPaginator(Boto3Paginator):
    """
    [Paginator.ListDataflowEndpointGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/groundstation.html#GroundStation.Paginator.ListDataflowEndpointGroups)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListDataflowEndpointGroupsResponseTypeDef, None, None]:
        """
        [ListDataflowEndpointGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/groundstation.html#GroundStation.Paginator.ListDataflowEndpointGroups.paginate)
        """


class ListGroundStationsPaginator(Boto3Paginator):
    """
    [Paginator.ListGroundStations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/groundstation.html#GroundStation.Paginator.ListGroundStations)
    """

    def paginate(
        self, satelliteId: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListGroundStationsResponseTypeDef, None, None]:
        """
        [ListGroundStations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/groundstation.html#GroundStation.Paginator.ListGroundStations.paginate)
        """


class ListMissionProfilesPaginator(Boto3Paginator):
    """
    [Paginator.ListMissionProfiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/groundstation.html#GroundStation.Paginator.ListMissionProfiles)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListMissionProfilesResponseTypeDef, None, None]:
        """
        [ListMissionProfiles.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/groundstation.html#GroundStation.Paginator.ListMissionProfiles.paginate)
        """


class ListSatellitesPaginator(Boto3Paginator):
    """
    [Paginator.ListSatellites documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/groundstation.html#GroundStation.Paginator.ListSatellites)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListSatellitesResponseTypeDef, None, None]:
        """
        [ListSatellites.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/groundstation.html#GroundStation.Paginator.ListSatellites.paginate)
        """
