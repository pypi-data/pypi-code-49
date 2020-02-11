"""
Main interface for groundstation service client

Usage::

    import boto3
    from mypy_boto3.groundstation import GroundStationClient

    session = boto3.Session()

    client: GroundStationClient = boto3.client("groundstation")
    session_client: GroundStationClient = session.client("groundstation")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from datetime import datetime
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_groundstation.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_groundstation.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_groundstation.type_defs import (
    ClientCancelContactResponseTypeDef,
    ClientCreateConfigConfigDataTypeDef,
    ClientCreateConfigResponseTypeDef,
    ClientCreateDataflowEndpointGroupEndpointDetailsTypeDef,
    ClientCreateDataflowEndpointGroupResponseTypeDef,
    ClientCreateMissionProfileResponseTypeDef,
    ClientDeleteConfigResponseTypeDef,
    ClientDeleteDataflowEndpointGroupResponseTypeDef,
    ClientDeleteMissionProfileResponseTypeDef,
    ClientDescribeContactResponseTypeDef,
    ClientGetConfigResponseTypeDef,
    ClientGetDataflowEndpointGroupResponseTypeDef,
    ClientGetMinuteUsageResponseTypeDef,
    ClientGetMissionProfileResponseTypeDef,
    ClientGetSatelliteResponseTypeDef,
    ClientListConfigsResponseTypeDef,
    ClientListContactsResponseTypeDef,
    ClientListDataflowEndpointGroupsResponseTypeDef,
    ClientListGroundStationsResponseTypeDef,
    ClientListMissionProfilesResponseTypeDef,
    ClientListSatellitesResponseTypeDef,
    ClientListTagsForResourceResponseTypeDef,
    ClientReserveContactResponseTypeDef,
    ClientUpdateConfigConfigDataTypeDef,
    ClientUpdateConfigResponseTypeDef,
    ClientUpdateMissionProfileResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("GroundStationClient",)


class GroundStationClient:
    """
    [GroundStation.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/groundstation.html#GroundStation.Client)
    """

    exceptions: "client_scope.Exceptions"

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/groundstation.html#GroundStation.Client.can_paginate)
        """

    def cancel_contact(self, contactId: str) -> ClientCancelContactResponseTypeDef:
        """
        [Client.cancel_contact documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/groundstation.html#GroundStation.Client.cancel_contact)
        """

    def create_config(
        self,
        configData: ClientCreateConfigConfigDataTypeDef,
        name: str,
        tags: Dict[str, str] = None,
    ) -> ClientCreateConfigResponseTypeDef:
        """
        [Client.create_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/groundstation.html#GroundStation.Client.create_config)
        """

    def create_dataflow_endpoint_group(
        self,
        endpointDetails: List[ClientCreateDataflowEndpointGroupEndpointDetailsTypeDef],
        tags: Dict[str, str] = None,
    ) -> ClientCreateDataflowEndpointGroupResponseTypeDef:
        """
        [Client.create_dataflow_endpoint_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/groundstation.html#GroundStation.Client.create_dataflow_endpoint_group)
        """

    def create_mission_profile(
        self,
        dataflowEdges: List[List[str]],
        minimumViableContactDurationSeconds: int,
        name: str,
        trackingConfigArn: str,
        contactPostPassDurationSeconds: int = None,
        contactPrePassDurationSeconds: int = None,
        tags: Dict[str, str] = None,
    ) -> ClientCreateMissionProfileResponseTypeDef:
        """
        [Client.create_mission_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/groundstation.html#GroundStation.Client.create_mission_profile)
        """

    def delete_config(
        self,
        configId: str,
        configType: Literal[
            "antenna-downlink",
            "antenna-downlink-demod-decode",
            "antenna-uplink",
            "dataflow-endpoint",
            "tracking",
            "uplink-echo",
        ],
    ) -> ClientDeleteConfigResponseTypeDef:
        """
        [Client.delete_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/groundstation.html#GroundStation.Client.delete_config)
        """

    def delete_dataflow_endpoint_group(
        self, dataflowEndpointGroupId: str
    ) -> ClientDeleteDataflowEndpointGroupResponseTypeDef:
        """
        [Client.delete_dataflow_endpoint_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/groundstation.html#GroundStation.Client.delete_dataflow_endpoint_group)
        """

    def delete_mission_profile(
        self, missionProfileId: str
    ) -> ClientDeleteMissionProfileResponseTypeDef:
        """
        [Client.delete_mission_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/groundstation.html#GroundStation.Client.delete_mission_profile)
        """

    def describe_contact(self, contactId: str) -> ClientDescribeContactResponseTypeDef:
        """
        [Client.describe_contact documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/groundstation.html#GroundStation.Client.describe_contact)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/groundstation.html#GroundStation.Client.generate_presigned_url)
        """

    def get_config(
        self,
        configId: str,
        configType: Literal[
            "antenna-downlink",
            "antenna-downlink-demod-decode",
            "antenna-uplink",
            "dataflow-endpoint",
            "tracking",
            "uplink-echo",
        ],
    ) -> ClientGetConfigResponseTypeDef:
        """
        [Client.get_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/groundstation.html#GroundStation.Client.get_config)
        """

    def get_dataflow_endpoint_group(
        self, dataflowEndpointGroupId: str
    ) -> ClientGetDataflowEndpointGroupResponseTypeDef:
        """
        [Client.get_dataflow_endpoint_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/groundstation.html#GroundStation.Client.get_dataflow_endpoint_group)
        """

    def get_minute_usage(self, month: int, year: int) -> ClientGetMinuteUsageResponseTypeDef:
        """
        [Client.get_minute_usage documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/groundstation.html#GroundStation.Client.get_minute_usage)
        """

    def get_mission_profile(self, missionProfileId: str) -> ClientGetMissionProfileResponseTypeDef:
        """
        [Client.get_mission_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/groundstation.html#GroundStation.Client.get_mission_profile)
        """

    def get_satellite(self, satelliteId: str) -> ClientGetSatelliteResponseTypeDef:
        """
        [Client.get_satellite documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/groundstation.html#GroundStation.Client.get_satellite)
        """

    def list_configs(
        self, maxResults: int = None, nextToken: str = None
    ) -> ClientListConfigsResponseTypeDef:
        """
        [Client.list_configs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/groundstation.html#GroundStation.Client.list_configs)
        """

    def list_contacts(
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
        maxResults: int = None,
        missionProfileArn: str = None,
        nextToken: str = None,
        satelliteArn: str = None,
    ) -> ClientListContactsResponseTypeDef:
        """
        [Client.list_contacts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/groundstation.html#GroundStation.Client.list_contacts)
        """

    def list_dataflow_endpoint_groups(
        self, maxResults: int = None, nextToken: str = None
    ) -> ClientListDataflowEndpointGroupsResponseTypeDef:
        """
        [Client.list_dataflow_endpoint_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/groundstation.html#GroundStation.Client.list_dataflow_endpoint_groups)
        """

    def list_ground_stations(
        self, maxResults: int = None, nextToken: str = None, satelliteId: str = None
    ) -> ClientListGroundStationsResponseTypeDef:
        """
        [Client.list_ground_stations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/groundstation.html#GroundStation.Client.list_ground_stations)
        """

    def list_mission_profiles(
        self, maxResults: int = None, nextToken: str = None
    ) -> ClientListMissionProfilesResponseTypeDef:
        """
        [Client.list_mission_profiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/groundstation.html#GroundStation.Client.list_mission_profiles)
        """

    def list_satellites(
        self, maxResults: int = None, nextToken: str = None
    ) -> ClientListSatellitesResponseTypeDef:
        """
        [Client.list_satellites documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/groundstation.html#GroundStation.Client.list_satellites)
        """

    def list_tags_for_resource(self, resourceArn: str) -> ClientListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/groundstation.html#GroundStation.Client.list_tags_for_resource)
        """

    def reserve_contact(
        self,
        endTime: datetime,
        groundStation: str,
        missionProfileArn: str,
        satelliteArn: str,
        startTime: datetime,
        tags: Dict[str, str] = None,
    ) -> ClientReserveContactResponseTypeDef:
        """
        [Client.reserve_contact documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/groundstation.html#GroundStation.Client.reserve_contact)
        """

    def tag_resource(self, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/groundstation.html#GroundStation.Client.tag_resource)
        """

    def untag_resource(self, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/groundstation.html#GroundStation.Client.untag_resource)
        """

    def update_config(
        self,
        configData: ClientUpdateConfigConfigDataTypeDef,
        configId: str,
        configType: Literal[
            "antenna-downlink",
            "antenna-downlink-demod-decode",
            "antenna-uplink",
            "dataflow-endpoint",
            "tracking",
            "uplink-echo",
        ],
        name: str,
    ) -> ClientUpdateConfigResponseTypeDef:
        """
        [Client.update_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/groundstation.html#GroundStation.Client.update_config)
        """

    def update_mission_profile(
        self,
        missionProfileId: str,
        contactPostPassDurationSeconds: int = None,
        contactPrePassDurationSeconds: int = None,
        dataflowEdges: List[List[str]] = None,
        minimumViableContactDurationSeconds: int = None,
        name: str = None,
        trackingConfigArn: str = None,
    ) -> ClientUpdateMissionProfileResponseTypeDef:
        """
        [Client.update_mission_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/groundstation.html#GroundStation.Client.update_mission_profile)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_configs"]
    ) -> "paginator_scope.ListConfigsPaginator":
        """
        [Paginator.ListConfigs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/groundstation.html#GroundStation.Paginator.ListConfigs)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_contacts"]
    ) -> "paginator_scope.ListContactsPaginator":
        """
        [Paginator.ListContacts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/groundstation.html#GroundStation.Paginator.ListContacts)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_dataflow_endpoint_groups"]
    ) -> "paginator_scope.ListDataflowEndpointGroupsPaginator":
        """
        [Paginator.ListDataflowEndpointGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/groundstation.html#GroundStation.Paginator.ListDataflowEndpointGroups)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_ground_stations"]
    ) -> "paginator_scope.ListGroundStationsPaginator":
        """
        [Paginator.ListGroundStations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/groundstation.html#GroundStation.Paginator.ListGroundStations)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_mission_profiles"]
    ) -> "paginator_scope.ListMissionProfilesPaginator":
        """
        [Paginator.ListMissionProfiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/groundstation.html#GroundStation.Paginator.ListMissionProfiles)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_satellites"]
    ) -> "paginator_scope.ListSatellitesPaginator":
        """
        [Paginator.ListSatellites documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/groundstation.html#GroundStation.Paginator.ListSatellites)
        """


class Exceptions:
    ClientError: Boto3ClientError
    DependencyException: Boto3ClientError
    InvalidParameterException: Boto3ClientError
    ResourceLimitExceededException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
