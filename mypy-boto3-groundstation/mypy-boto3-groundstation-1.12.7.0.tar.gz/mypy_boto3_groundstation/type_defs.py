"""
Main interface for groundstation service type definitions.

Usage::

    from mypy_boto3.groundstation.type_defs import ClientCancelContactResponseTypeDef

    data: ClientCancelContactResponseTypeDef = {...}
"""
from datetime import datetime
import sys
from typing import Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ClientCancelContactResponseTypeDef",
    "ClientCreateConfigConfigDataantennaDownlinkConfigspectrumConfigbandwidthTypeDef",
    "ClientCreateConfigConfigDataantennaDownlinkConfigspectrumConfigcenterFrequencyTypeDef",
    "ClientCreateConfigConfigDataantennaDownlinkConfigspectrumConfigTypeDef",
    "ClientCreateConfigConfigDataantennaDownlinkConfigTypeDef",
    "ClientCreateConfigConfigDataantennaDownlinkDemodDecodeConfigdecodeConfigTypeDef",
    "ClientCreateConfigConfigDataantennaDownlinkDemodDecodeConfigdemodulationConfigTypeDef",
    "ClientCreateConfigConfigDataantennaDownlinkDemodDecodeConfigspectrumConfigbandwidthTypeDef",
    "ClientCreateConfigConfigDataantennaDownlinkDemodDecodeConfigspectrumConfigcenterFrequencyTypeDef",
    "ClientCreateConfigConfigDataantennaDownlinkDemodDecodeConfigspectrumConfigTypeDef",
    "ClientCreateConfigConfigDataantennaDownlinkDemodDecodeConfigTypeDef",
    "ClientCreateConfigConfigDataantennaUplinkConfigspectrumConfigcenterFrequencyTypeDef",
    "ClientCreateConfigConfigDataantennaUplinkConfigspectrumConfigTypeDef",
    "ClientCreateConfigConfigDataantennaUplinkConfigtargetEirpTypeDef",
    "ClientCreateConfigConfigDataantennaUplinkConfigTypeDef",
    "ClientCreateConfigConfigDatadataflowEndpointConfigTypeDef",
    "ClientCreateConfigConfigDatatrackingConfigTypeDef",
    "ClientCreateConfigConfigDatauplinkEchoConfigTypeDef",
    "ClientCreateConfigConfigDataTypeDef",
    "ClientCreateConfigResponseTypeDef",
    "ClientCreateDataflowEndpointGroupEndpointDetailsendpointaddressTypeDef",
    "ClientCreateDataflowEndpointGroupEndpointDetailsendpointTypeDef",
    "ClientCreateDataflowEndpointGroupEndpointDetailssecurityDetailsTypeDef",
    "ClientCreateDataflowEndpointGroupEndpointDetailsTypeDef",
    "ClientCreateDataflowEndpointGroupResponseTypeDef",
    "ClientCreateMissionProfileResponseTypeDef",
    "ClientDeleteConfigResponseTypeDef",
    "ClientDeleteDataflowEndpointGroupResponseTypeDef",
    "ClientDeleteMissionProfileResponseTypeDef",
    "ClientDescribeContactResponsemaximumElevationTypeDef",
    "ClientDescribeContactResponseTypeDef",
    "ClientGetConfigResponseconfigDataantennaDownlinkConfigspectrumConfigbandwidthTypeDef",
    "ClientGetConfigResponseconfigDataantennaDownlinkConfigspectrumConfigcenterFrequencyTypeDef",
    "ClientGetConfigResponseconfigDataantennaDownlinkConfigspectrumConfigTypeDef",
    "ClientGetConfigResponseconfigDataantennaDownlinkConfigTypeDef",
    "ClientGetConfigResponseconfigDataantennaDownlinkDemodDecodeConfigdecodeConfigTypeDef",
    "ClientGetConfigResponseconfigDataantennaDownlinkDemodDecodeConfigdemodulationConfigTypeDef",
    "ClientGetConfigResponseconfigDataantennaDownlinkDemodDecodeConfigspectrumConfigbandwidthTypeDef",
    "ClientGetConfigResponseconfigDataantennaDownlinkDemodDecodeConfigspectrumConfigcenterFrequencyTypeDef",
    "ClientGetConfigResponseconfigDataantennaDownlinkDemodDecodeConfigspectrumConfigTypeDef",
    "ClientGetConfigResponseconfigDataantennaDownlinkDemodDecodeConfigTypeDef",
    "ClientGetConfigResponseconfigDataantennaUplinkConfigspectrumConfigcenterFrequencyTypeDef",
    "ClientGetConfigResponseconfigDataantennaUplinkConfigspectrumConfigTypeDef",
    "ClientGetConfigResponseconfigDataantennaUplinkConfigtargetEirpTypeDef",
    "ClientGetConfigResponseconfigDataantennaUplinkConfigTypeDef",
    "ClientGetConfigResponseconfigDatadataflowEndpointConfigTypeDef",
    "ClientGetConfigResponseconfigDatatrackingConfigTypeDef",
    "ClientGetConfigResponseconfigDatauplinkEchoConfigTypeDef",
    "ClientGetConfigResponseconfigDataTypeDef",
    "ClientGetConfigResponseTypeDef",
    "ClientGetDataflowEndpointGroupResponseendpointsDetailsendpointaddressTypeDef",
    "ClientGetDataflowEndpointGroupResponseendpointsDetailsendpointTypeDef",
    "ClientGetDataflowEndpointGroupResponseendpointsDetailssecurityDetailsTypeDef",
    "ClientGetDataflowEndpointGroupResponseendpointsDetailsTypeDef",
    "ClientGetDataflowEndpointGroupResponseTypeDef",
    "ClientGetMinuteUsageResponseTypeDef",
    "ClientGetMissionProfileResponseTypeDef",
    "ClientGetSatelliteResponseTypeDef",
    "ClientListConfigsResponseconfigListTypeDef",
    "ClientListConfigsResponseTypeDef",
    "ClientListContactsResponsecontactListmaximumElevationTypeDef",
    "ClientListContactsResponsecontactListTypeDef",
    "ClientListContactsResponseTypeDef",
    "ClientListDataflowEndpointGroupsResponsedataflowEndpointGroupListTypeDef",
    "ClientListDataflowEndpointGroupsResponseTypeDef",
    "ClientListGroundStationsResponsegroundStationListTypeDef",
    "ClientListGroundStationsResponseTypeDef",
    "ClientListMissionProfilesResponsemissionProfileListTypeDef",
    "ClientListMissionProfilesResponseTypeDef",
    "ClientListSatellitesResponsesatellitesTypeDef",
    "ClientListSatellitesResponseTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientReserveContactResponseTypeDef",
    "ClientUpdateConfigConfigDataantennaDownlinkConfigspectrumConfigbandwidthTypeDef",
    "ClientUpdateConfigConfigDataantennaDownlinkConfigspectrumConfigcenterFrequencyTypeDef",
    "ClientUpdateConfigConfigDataantennaDownlinkConfigspectrumConfigTypeDef",
    "ClientUpdateConfigConfigDataantennaDownlinkConfigTypeDef",
    "ClientUpdateConfigConfigDataantennaDownlinkDemodDecodeConfigdecodeConfigTypeDef",
    "ClientUpdateConfigConfigDataantennaDownlinkDemodDecodeConfigdemodulationConfigTypeDef",
    "ClientUpdateConfigConfigDataantennaDownlinkDemodDecodeConfigspectrumConfigbandwidthTypeDef",
    "ClientUpdateConfigConfigDataantennaDownlinkDemodDecodeConfigspectrumConfigcenterFrequencyTypeDef",
    "ClientUpdateConfigConfigDataantennaDownlinkDemodDecodeConfigspectrumConfigTypeDef",
    "ClientUpdateConfigConfigDataantennaDownlinkDemodDecodeConfigTypeDef",
    "ClientUpdateConfigConfigDataantennaUplinkConfigspectrumConfigcenterFrequencyTypeDef",
    "ClientUpdateConfigConfigDataantennaUplinkConfigspectrumConfigTypeDef",
    "ClientUpdateConfigConfigDataantennaUplinkConfigtargetEirpTypeDef",
    "ClientUpdateConfigConfigDataantennaUplinkConfigTypeDef",
    "ClientUpdateConfigConfigDatadataflowEndpointConfigTypeDef",
    "ClientUpdateConfigConfigDatatrackingConfigTypeDef",
    "ClientUpdateConfigConfigDatauplinkEchoConfigTypeDef",
    "ClientUpdateConfigConfigDataTypeDef",
    "ClientUpdateConfigResponseTypeDef",
    "ClientUpdateMissionProfileResponseTypeDef",
    "ConfigListItemTypeDef",
    "ListConfigsResponseTypeDef",
    "ElevationTypeDef",
    "ContactDataTypeDef",
    "ListContactsResponseTypeDef",
    "DataflowEndpointListItemTypeDef",
    "ListDataflowEndpointGroupsResponseTypeDef",
    "GroundStationDataTypeDef",
    "ListGroundStationsResponseTypeDef",
    "MissionProfileListItemTypeDef",
    "ListMissionProfilesResponseTypeDef",
    "SatelliteListItemTypeDef",
    "ListSatellitesResponseTypeDef",
    "PaginatorConfigTypeDef",
)

ClientCancelContactResponseTypeDef = TypedDict(
    "ClientCancelContactResponseTypeDef", {"contactId": str}, total=False
)

_RequiredClientCreateConfigConfigDataantennaDownlinkConfigspectrumConfigbandwidthTypeDef = TypedDict(
    "_RequiredClientCreateConfigConfigDataantennaDownlinkConfigspectrumConfigbandwidthTypeDef",
    {"units": Literal["GHz", "MHz", "kHz"]},
)
_OptionalClientCreateConfigConfigDataantennaDownlinkConfigspectrumConfigbandwidthTypeDef = TypedDict(
    "_OptionalClientCreateConfigConfigDataantennaDownlinkConfigspectrumConfigbandwidthTypeDef",
    {"value": float},
    total=False,
)


class ClientCreateConfigConfigDataantennaDownlinkConfigspectrumConfigbandwidthTypeDef(
    _RequiredClientCreateConfigConfigDataantennaDownlinkConfigspectrumConfigbandwidthTypeDef,
    _OptionalClientCreateConfigConfigDataantennaDownlinkConfigspectrumConfigbandwidthTypeDef,
):
    pass


ClientCreateConfigConfigDataantennaDownlinkConfigspectrumConfigcenterFrequencyTypeDef = TypedDict(
    "ClientCreateConfigConfigDataantennaDownlinkConfigspectrumConfigcenterFrequencyTypeDef",
    {"units": Literal["GHz", "MHz", "kHz"], "value": float},
    total=False,
)

_RequiredClientCreateConfigConfigDataantennaDownlinkConfigspectrumConfigTypeDef = TypedDict(
    "_RequiredClientCreateConfigConfigDataantennaDownlinkConfigspectrumConfigTypeDef",
    {"bandwidth": ClientCreateConfigConfigDataantennaDownlinkConfigspectrumConfigbandwidthTypeDef},
)
_OptionalClientCreateConfigConfigDataantennaDownlinkConfigspectrumConfigTypeDef = TypedDict(
    "_OptionalClientCreateConfigConfigDataantennaDownlinkConfigspectrumConfigTypeDef",
    {
        "centerFrequency": ClientCreateConfigConfigDataantennaDownlinkConfigspectrumConfigcenterFrequencyTypeDef,
        "polarization": Literal["LEFT_HAND", "NONE", "RIGHT_HAND"],
    },
    total=False,
)


class ClientCreateConfigConfigDataantennaDownlinkConfigspectrumConfigTypeDef(
    _RequiredClientCreateConfigConfigDataantennaDownlinkConfigspectrumConfigTypeDef,
    _OptionalClientCreateConfigConfigDataantennaDownlinkConfigspectrumConfigTypeDef,
):
    pass


ClientCreateConfigConfigDataantennaDownlinkConfigTypeDef = TypedDict(
    "ClientCreateConfigConfigDataantennaDownlinkConfigTypeDef",
    {"spectrumConfig": ClientCreateConfigConfigDataantennaDownlinkConfigspectrumConfigTypeDef},
)

ClientCreateConfigConfigDataantennaDownlinkDemodDecodeConfigdecodeConfigTypeDef = TypedDict(
    "ClientCreateConfigConfigDataantennaDownlinkDemodDecodeConfigdecodeConfigTypeDef",
    {"unvalidatedJSON": str},
    total=False,
)

ClientCreateConfigConfigDataantennaDownlinkDemodDecodeConfigdemodulationConfigTypeDef = TypedDict(
    "ClientCreateConfigConfigDataantennaDownlinkDemodDecodeConfigdemodulationConfigTypeDef",
    {"unvalidatedJSON": str},
    total=False,
)

ClientCreateConfigConfigDataantennaDownlinkDemodDecodeConfigspectrumConfigbandwidthTypeDef = TypedDict(
    "ClientCreateConfigConfigDataantennaDownlinkDemodDecodeConfigspectrumConfigbandwidthTypeDef",
    {"units": Literal["GHz", "MHz", "kHz"], "value": float},
    total=False,
)

ClientCreateConfigConfigDataantennaDownlinkDemodDecodeConfigspectrumConfigcenterFrequencyTypeDef = TypedDict(
    "ClientCreateConfigConfigDataantennaDownlinkDemodDecodeConfigspectrumConfigcenterFrequencyTypeDef",
    {"units": Literal["GHz", "MHz", "kHz"], "value": float},
    total=False,
)

ClientCreateConfigConfigDataantennaDownlinkDemodDecodeConfigspectrumConfigTypeDef = TypedDict(
    "ClientCreateConfigConfigDataantennaDownlinkDemodDecodeConfigspectrumConfigTypeDef",
    {
        "bandwidth": ClientCreateConfigConfigDataantennaDownlinkDemodDecodeConfigspectrumConfigbandwidthTypeDef,
        "centerFrequency": ClientCreateConfigConfigDataantennaDownlinkDemodDecodeConfigspectrumConfigcenterFrequencyTypeDef,
        "polarization": Literal["LEFT_HAND", "NONE", "RIGHT_HAND"],
    },
    total=False,
)

ClientCreateConfigConfigDataantennaDownlinkDemodDecodeConfigTypeDef = TypedDict(
    "ClientCreateConfigConfigDataantennaDownlinkDemodDecodeConfigTypeDef",
    {
        "decodeConfig": ClientCreateConfigConfigDataantennaDownlinkDemodDecodeConfigdecodeConfigTypeDef,
        "demodulationConfig": ClientCreateConfigConfigDataantennaDownlinkDemodDecodeConfigdemodulationConfigTypeDef,
        "spectrumConfig": ClientCreateConfigConfigDataantennaDownlinkDemodDecodeConfigspectrumConfigTypeDef,
    },
    total=False,
)

ClientCreateConfigConfigDataantennaUplinkConfigspectrumConfigcenterFrequencyTypeDef = TypedDict(
    "ClientCreateConfigConfigDataantennaUplinkConfigspectrumConfigcenterFrequencyTypeDef",
    {"units": Literal["GHz", "MHz", "kHz"], "value": float},
    total=False,
)

ClientCreateConfigConfigDataantennaUplinkConfigspectrumConfigTypeDef = TypedDict(
    "ClientCreateConfigConfigDataantennaUplinkConfigspectrumConfigTypeDef",
    {
        "centerFrequency": ClientCreateConfigConfigDataantennaUplinkConfigspectrumConfigcenterFrequencyTypeDef,
        "polarization": Literal["LEFT_HAND", "NONE", "RIGHT_HAND"],
    },
    total=False,
)

ClientCreateConfigConfigDataantennaUplinkConfigtargetEirpTypeDef = TypedDict(
    "ClientCreateConfigConfigDataantennaUplinkConfigtargetEirpTypeDef",
    {"units": str, "value": float},
    total=False,
)

ClientCreateConfigConfigDataantennaUplinkConfigTypeDef = TypedDict(
    "ClientCreateConfigConfigDataantennaUplinkConfigTypeDef",
    {
        "spectrumConfig": ClientCreateConfigConfigDataantennaUplinkConfigspectrumConfigTypeDef,
        "targetEirp": ClientCreateConfigConfigDataantennaUplinkConfigtargetEirpTypeDef,
    },
    total=False,
)

ClientCreateConfigConfigDatadataflowEndpointConfigTypeDef = TypedDict(
    "ClientCreateConfigConfigDatadataflowEndpointConfigTypeDef",
    {"dataflowEndpointName": str, "dataflowEndpointRegion": str},
    total=False,
)

ClientCreateConfigConfigDatatrackingConfigTypeDef = TypedDict(
    "ClientCreateConfigConfigDatatrackingConfigTypeDef",
    {"autotrack": Literal["PREFERRED", "REMOVED", "REQUIRED"]},
    total=False,
)

ClientCreateConfigConfigDatauplinkEchoConfigTypeDef = TypedDict(
    "ClientCreateConfigConfigDatauplinkEchoConfigTypeDef",
    {"antennaUplinkConfigArn": str, "enabled": bool},
    total=False,
)

ClientCreateConfigConfigDataTypeDef = TypedDict(
    "ClientCreateConfigConfigDataTypeDef",
    {
        "antennaDownlinkConfig": ClientCreateConfigConfigDataantennaDownlinkConfigTypeDef,
        "antennaDownlinkDemodDecodeConfig": ClientCreateConfigConfigDataantennaDownlinkDemodDecodeConfigTypeDef,
        "antennaUplinkConfig": ClientCreateConfigConfigDataantennaUplinkConfigTypeDef,
        "dataflowEndpointConfig": ClientCreateConfigConfigDatadataflowEndpointConfigTypeDef,
        "trackingConfig": ClientCreateConfigConfigDatatrackingConfigTypeDef,
        "uplinkEchoConfig": ClientCreateConfigConfigDatauplinkEchoConfigTypeDef,
    },
    total=False,
)

ClientCreateConfigResponseTypeDef = TypedDict(
    "ClientCreateConfigResponseTypeDef",
    {
        "configArn": str,
        "configId": str,
        "configType": Literal[
            "antenna-downlink",
            "antenna-downlink-demod-decode",
            "antenna-uplink",
            "dataflow-endpoint",
            "tracking",
            "uplink-echo",
        ],
    },
    total=False,
)

_RequiredClientCreateDataflowEndpointGroupEndpointDetailsendpointaddressTypeDef = TypedDict(
    "_RequiredClientCreateDataflowEndpointGroupEndpointDetailsendpointaddressTypeDef", {"name": str}
)
_OptionalClientCreateDataflowEndpointGroupEndpointDetailsendpointaddressTypeDef = TypedDict(
    "_OptionalClientCreateDataflowEndpointGroupEndpointDetailsendpointaddressTypeDef",
    {"port": int},
    total=False,
)


class ClientCreateDataflowEndpointGroupEndpointDetailsendpointaddressTypeDef(
    _RequiredClientCreateDataflowEndpointGroupEndpointDetailsendpointaddressTypeDef,
    _OptionalClientCreateDataflowEndpointGroupEndpointDetailsendpointaddressTypeDef,
):
    pass


ClientCreateDataflowEndpointGroupEndpointDetailsendpointTypeDef = TypedDict(
    "ClientCreateDataflowEndpointGroupEndpointDetailsendpointTypeDef",
    {
        "address": ClientCreateDataflowEndpointGroupEndpointDetailsendpointaddressTypeDef,
        "name": str,
        "status": Literal["created", "creating", "deleted", "deleting", "failed"],
    },
    total=False,
)

ClientCreateDataflowEndpointGroupEndpointDetailssecurityDetailsTypeDef = TypedDict(
    "ClientCreateDataflowEndpointGroupEndpointDetailssecurityDetailsTypeDef",
    {"roleArn": str, "securityGroupIds": List[str], "subnetIds": List[str]},
    total=False,
)

ClientCreateDataflowEndpointGroupEndpointDetailsTypeDef = TypedDict(
    "ClientCreateDataflowEndpointGroupEndpointDetailsTypeDef",
    {
        "endpoint": ClientCreateDataflowEndpointGroupEndpointDetailsendpointTypeDef,
        "securityDetails": ClientCreateDataflowEndpointGroupEndpointDetailssecurityDetailsTypeDef,
    },
    total=False,
)

ClientCreateDataflowEndpointGroupResponseTypeDef = TypedDict(
    "ClientCreateDataflowEndpointGroupResponseTypeDef",
    {"dataflowEndpointGroupId": str},
    total=False,
)

ClientCreateMissionProfileResponseTypeDef = TypedDict(
    "ClientCreateMissionProfileResponseTypeDef", {"missionProfileId": str}, total=False
)

ClientDeleteConfigResponseTypeDef = TypedDict(
    "ClientDeleteConfigResponseTypeDef",
    {
        "configArn": str,
        "configId": str,
        "configType": Literal[
            "antenna-downlink",
            "antenna-downlink-demod-decode",
            "antenna-uplink",
            "dataflow-endpoint",
            "tracking",
            "uplink-echo",
        ],
    },
    total=False,
)

ClientDeleteDataflowEndpointGroupResponseTypeDef = TypedDict(
    "ClientDeleteDataflowEndpointGroupResponseTypeDef",
    {"dataflowEndpointGroupId": str},
    total=False,
)

ClientDeleteMissionProfileResponseTypeDef = TypedDict(
    "ClientDeleteMissionProfileResponseTypeDef", {"missionProfileId": str}, total=False
)

ClientDescribeContactResponsemaximumElevationTypeDef = TypedDict(
    "ClientDescribeContactResponsemaximumElevationTypeDef",
    {"unit": Literal["DEGREE_ANGLE", "RADIAN"], "value": float},
    total=False,
)

ClientDescribeContactResponseTypeDef = TypedDict(
    "ClientDescribeContactResponseTypeDef",
    {
        "contactId": str,
        "contactStatus": Literal[
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
        ],
        "endTime": datetime,
        "errorMessage": str,
        "groundStation": str,
        "maximumElevation": ClientDescribeContactResponsemaximumElevationTypeDef,
        "missionProfileArn": str,
        "postPassEndTime": datetime,
        "prePassStartTime": datetime,
        "region": str,
        "satelliteArn": str,
        "startTime": datetime,
        "tags": Dict[str, str],
    },
    total=False,
)

ClientGetConfigResponseconfigDataantennaDownlinkConfigspectrumConfigbandwidthTypeDef = TypedDict(
    "ClientGetConfigResponseconfigDataantennaDownlinkConfigspectrumConfigbandwidthTypeDef",
    {"units": Literal["GHz", "MHz", "kHz"], "value": float},
    total=False,
)

ClientGetConfigResponseconfigDataantennaDownlinkConfigspectrumConfigcenterFrequencyTypeDef = TypedDict(
    "ClientGetConfigResponseconfigDataantennaDownlinkConfigspectrumConfigcenterFrequencyTypeDef",
    {"units": Literal["GHz", "MHz", "kHz"], "value": float},
    total=False,
)

ClientGetConfigResponseconfigDataantennaDownlinkConfigspectrumConfigTypeDef = TypedDict(
    "ClientGetConfigResponseconfigDataantennaDownlinkConfigspectrumConfigTypeDef",
    {
        "bandwidth": ClientGetConfigResponseconfigDataantennaDownlinkConfigspectrumConfigbandwidthTypeDef,
        "centerFrequency": ClientGetConfigResponseconfigDataantennaDownlinkConfigspectrumConfigcenterFrequencyTypeDef,
        "polarization": Literal["LEFT_HAND", "NONE", "RIGHT_HAND"],
    },
    total=False,
)

ClientGetConfigResponseconfigDataantennaDownlinkConfigTypeDef = TypedDict(
    "ClientGetConfigResponseconfigDataantennaDownlinkConfigTypeDef",
    {"spectrumConfig": ClientGetConfigResponseconfigDataantennaDownlinkConfigspectrumConfigTypeDef},
    total=False,
)

ClientGetConfigResponseconfigDataantennaDownlinkDemodDecodeConfigdecodeConfigTypeDef = TypedDict(
    "ClientGetConfigResponseconfigDataantennaDownlinkDemodDecodeConfigdecodeConfigTypeDef",
    {"unvalidatedJSON": str},
    total=False,
)

ClientGetConfigResponseconfigDataantennaDownlinkDemodDecodeConfigdemodulationConfigTypeDef = TypedDict(
    "ClientGetConfigResponseconfigDataantennaDownlinkDemodDecodeConfigdemodulationConfigTypeDef",
    {"unvalidatedJSON": str},
    total=False,
)

ClientGetConfigResponseconfigDataantennaDownlinkDemodDecodeConfigspectrumConfigbandwidthTypeDef = TypedDict(
    "ClientGetConfigResponseconfigDataantennaDownlinkDemodDecodeConfigspectrumConfigbandwidthTypeDef",
    {"units": Literal["GHz", "MHz", "kHz"], "value": float},
    total=False,
)

ClientGetConfigResponseconfigDataantennaDownlinkDemodDecodeConfigspectrumConfigcenterFrequencyTypeDef = TypedDict(
    "ClientGetConfigResponseconfigDataantennaDownlinkDemodDecodeConfigspectrumConfigcenterFrequencyTypeDef",
    {"units": Literal["GHz", "MHz", "kHz"], "value": float},
    total=False,
)

ClientGetConfigResponseconfigDataantennaDownlinkDemodDecodeConfigspectrumConfigTypeDef = TypedDict(
    "ClientGetConfigResponseconfigDataantennaDownlinkDemodDecodeConfigspectrumConfigTypeDef",
    {
        "bandwidth": ClientGetConfigResponseconfigDataantennaDownlinkDemodDecodeConfigspectrumConfigbandwidthTypeDef,
        "centerFrequency": ClientGetConfigResponseconfigDataantennaDownlinkDemodDecodeConfigspectrumConfigcenterFrequencyTypeDef,
        "polarization": Literal["LEFT_HAND", "NONE", "RIGHT_HAND"],
    },
    total=False,
)

ClientGetConfigResponseconfigDataantennaDownlinkDemodDecodeConfigTypeDef = TypedDict(
    "ClientGetConfigResponseconfigDataantennaDownlinkDemodDecodeConfigTypeDef",
    {
        "decodeConfig": ClientGetConfigResponseconfigDataantennaDownlinkDemodDecodeConfigdecodeConfigTypeDef,
        "demodulationConfig": ClientGetConfigResponseconfigDataantennaDownlinkDemodDecodeConfigdemodulationConfigTypeDef,
        "spectrumConfig": ClientGetConfigResponseconfigDataantennaDownlinkDemodDecodeConfigspectrumConfigTypeDef,
    },
    total=False,
)

ClientGetConfigResponseconfigDataantennaUplinkConfigspectrumConfigcenterFrequencyTypeDef = TypedDict(
    "ClientGetConfigResponseconfigDataantennaUplinkConfigspectrumConfigcenterFrequencyTypeDef",
    {"units": Literal["GHz", "MHz", "kHz"], "value": float},
    total=False,
)

ClientGetConfigResponseconfigDataantennaUplinkConfigspectrumConfigTypeDef = TypedDict(
    "ClientGetConfigResponseconfigDataantennaUplinkConfigspectrumConfigTypeDef",
    {
        "centerFrequency": ClientGetConfigResponseconfigDataantennaUplinkConfigspectrumConfigcenterFrequencyTypeDef,
        "polarization": Literal["LEFT_HAND", "NONE", "RIGHT_HAND"],
    },
    total=False,
)

ClientGetConfigResponseconfigDataantennaUplinkConfigtargetEirpTypeDef = TypedDict(
    "ClientGetConfigResponseconfigDataantennaUplinkConfigtargetEirpTypeDef",
    {"units": str, "value": float},
    total=False,
)

ClientGetConfigResponseconfigDataantennaUplinkConfigTypeDef = TypedDict(
    "ClientGetConfigResponseconfigDataantennaUplinkConfigTypeDef",
    {
        "spectrumConfig": ClientGetConfigResponseconfigDataantennaUplinkConfigspectrumConfigTypeDef,
        "targetEirp": ClientGetConfigResponseconfigDataantennaUplinkConfigtargetEirpTypeDef,
    },
    total=False,
)

ClientGetConfigResponseconfigDatadataflowEndpointConfigTypeDef = TypedDict(
    "ClientGetConfigResponseconfigDatadataflowEndpointConfigTypeDef",
    {"dataflowEndpointName": str, "dataflowEndpointRegion": str},
    total=False,
)

ClientGetConfigResponseconfigDatatrackingConfigTypeDef = TypedDict(
    "ClientGetConfigResponseconfigDatatrackingConfigTypeDef",
    {"autotrack": Literal["PREFERRED", "REMOVED", "REQUIRED"]},
    total=False,
)

ClientGetConfigResponseconfigDatauplinkEchoConfigTypeDef = TypedDict(
    "ClientGetConfigResponseconfigDatauplinkEchoConfigTypeDef",
    {"antennaUplinkConfigArn": str, "enabled": bool},
    total=False,
)

ClientGetConfigResponseconfigDataTypeDef = TypedDict(
    "ClientGetConfigResponseconfigDataTypeDef",
    {
        "antennaDownlinkConfig": ClientGetConfigResponseconfigDataantennaDownlinkConfigTypeDef,
        "antennaDownlinkDemodDecodeConfig": ClientGetConfigResponseconfigDataantennaDownlinkDemodDecodeConfigTypeDef,
        "antennaUplinkConfig": ClientGetConfigResponseconfigDataantennaUplinkConfigTypeDef,
        "dataflowEndpointConfig": ClientGetConfigResponseconfigDatadataflowEndpointConfigTypeDef,
        "trackingConfig": ClientGetConfigResponseconfigDatatrackingConfigTypeDef,
        "uplinkEchoConfig": ClientGetConfigResponseconfigDatauplinkEchoConfigTypeDef,
    },
    total=False,
)

ClientGetConfigResponseTypeDef = TypedDict(
    "ClientGetConfigResponseTypeDef",
    {
        "configArn": str,
        "configData": ClientGetConfigResponseconfigDataTypeDef,
        "configId": str,
        "configType": Literal[
            "antenna-downlink",
            "antenna-downlink-demod-decode",
            "antenna-uplink",
            "dataflow-endpoint",
            "tracking",
            "uplink-echo",
        ],
        "name": str,
        "tags": Dict[str, str],
    },
    total=False,
)

ClientGetDataflowEndpointGroupResponseendpointsDetailsendpointaddressTypeDef = TypedDict(
    "ClientGetDataflowEndpointGroupResponseendpointsDetailsendpointaddressTypeDef",
    {"name": str, "port": int},
    total=False,
)

ClientGetDataflowEndpointGroupResponseendpointsDetailsendpointTypeDef = TypedDict(
    "ClientGetDataflowEndpointGroupResponseendpointsDetailsendpointTypeDef",
    {
        "address": ClientGetDataflowEndpointGroupResponseendpointsDetailsendpointaddressTypeDef,
        "name": str,
        "status": Literal["created", "creating", "deleted", "deleting", "failed"],
    },
    total=False,
)

ClientGetDataflowEndpointGroupResponseendpointsDetailssecurityDetailsTypeDef = TypedDict(
    "ClientGetDataflowEndpointGroupResponseendpointsDetailssecurityDetailsTypeDef",
    {"roleArn": str, "securityGroupIds": List[str], "subnetIds": List[str]},
    total=False,
)

ClientGetDataflowEndpointGroupResponseendpointsDetailsTypeDef = TypedDict(
    "ClientGetDataflowEndpointGroupResponseendpointsDetailsTypeDef",
    {
        "endpoint": ClientGetDataflowEndpointGroupResponseendpointsDetailsendpointTypeDef,
        "securityDetails": ClientGetDataflowEndpointGroupResponseendpointsDetailssecurityDetailsTypeDef,
    },
    total=False,
)

ClientGetDataflowEndpointGroupResponseTypeDef = TypedDict(
    "ClientGetDataflowEndpointGroupResponseTypeDef",
    {
        "dataflowEndpointGroupArn": str,
        "dataflowEndpointGroupId": str,
        "endpointsDetails": List[ClientGetDataflowEndpointGroupResponseendpointsDetailsTypeDef],
        "tags": Dict[str, str],
    },
    total=False,
)

ClientGetMinuteUsageResponseTypeDef = TypedDict(
    "ClientGetMinuteUsageResponseTypeDef",
    {
        "estimatedMinutesRemaining": int,
        "isReservedMinutesCustomer": bool,
        "totalReservedMinuteAllocation": int,
        "totalScheduledMinutes": int,
        "upcomingMinutesScheduled": int,
    },
    total=False,
)

ClientGetMissionProfileResponseTypeDef = TypedDict(
    "ClientGetMissionProfileResponseTypeDef",
    {
        "contactPostPassDurationSeconds": int,
        "contactPrePassDurationSeconds": int,
        "dataflowEdges": List[List[str]],
        "minimumViableContactDurationSeconds": int,
        "missionProfileArn": str,
        "missionProfileId": str,
        "name": str,
        "region": str,
        "tags": Dict[str, str],
        "trackingConfigArn": str,
    },
    total=False,
)

ClientGetSatelliteResponseTypeDef = TypedDict(
    "ClientGetSatelliteResponseTypeDef",
    {"groundStations": List[str], "noradSatelliteID": int, "satelliteArn": str, "satelliteId": str},
    total=False,
)

ClientListConfigsResponseconfigListTypeDef = TypedDict(
    "ClientListConfigsResponseconfigListTypeDef",
    {
        "configArn": str,
        "configId": str,
        "configType": Literal[
            "antenna-downlink",
            "antenna-downlink-demod-decode",
            "antenna-uplink",
            "dataflow-endpoint",
            "tracking",
            "uplink-echo",
        ],
        "name": str,
    },
    total=False,
)

ClientListConfigsResponseTypeDef = TypedDict(
    "ClientListConfigsResponseTypeDef",
    {"configList": List[ClientListConfigsResponseconfigListTypeDef], "nextToken": str},
    total=False,
)

ClientListContactsResponsecontactListmaximumElevationTypeDef = TypedDict(
    "ClientListContactsResponsecontactListmaximumElevationTypeDef",
    {"unit": Literal["DEGREE_ANGLE", "RADIAN"], "value": float},
    total=False,
)

ClientListContactsResponsecontactListTypeDef = TypedDict(
    "ClientListContactsResponsecontactListTypeDef",
    {
        "contactId": str,
        "contactStatus": Literal[
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
        ],
        "endTime": datetime,
        "errorMessage": str,
        "groundStation": str,
        "maximumElevation": ClientListContactsResponsecontactListmaximumElevationTypeDef,
        "missionProfileArn": str,
        "postPassEndTime": datetime,
        "prePassStartTime": datetime,
        "region": str,
        "satelliteArn": str,
        "startTime": datetime,
        "tags": Dict[str, str],
    },
    total=False,
)

ClientListContactsResponseTypeDef = TypedDict(
    "ClientListContactsResponseTypeDef",
    {"contactList": List[ClientListContactsResponsecontactListTypeDef], "nextToken": str},
    total=False,
)

ClientListDataflowEndpointGroupsResponsedataflowEndpointGroupListTypeDef = TypedDict(
    "ClientListDataflowEndpointGroupsResponsedataflowEndpointGroupListTypeDef",
    {"dataflowEndpointGroupArn": str, "dataflowEndpointGroupId": str},
    total=False,
)

ClientListDataflowEndpointGroupsResponseTypeDef = TypedDict(
    "ClientListDataflowEndpointGroupsResponseTypeDef",
    {
        "dataflowEndpointGroupList": List[
            ClientListDataflowEndpointGroupsResponsedataflowEndpointGroupListTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)

ClientListGroundStationsResponsegroundStationListTypeDef = TypedDict(
    "ClientListGroundStationsResponsegroundStationListTypeDef",
    {"groundStationId": str, "groundStationName": str, "region": str},
    total=False,
)

ClientListGroundStationsResponseTypeDef = TypedDict(
    "ClientListGroundStationsResponseTypeDef",
    {
        "groundStationList": List[ClientListGroundStationsResponsegroundStationListTypeDef],
        "nextToken": str,
    },
    total=False,
)

ClientListMissionProfilesResponsemissionProfileListTypeDef = TypedDict(
    "ClientListMissionProfilesResponsemissionProfileListTypeDef",
    {"missionProfileArn": str, "missionProfileId": str, "name": str, "region": str},
    total=False,
)

ClientListMissionProfilesResponseTypeDef = TypedDict(
    "ClientListMissionProfilesResponseTypeDef",
    {
        "missionProfileList": List[ClientListMissionProfilesResponsemissionProfileListTypeDef],
        "nextToken": str,
    },
    total=False,
)

ClientListSatellitesResponsesatellitesTypeDef = TypedDict(
    "ClientListSatellitesResponsesatellitesTypeDef",
    {"groundStations": List[str], "noradSatelliteID": int, "satelliteArn": str, "satelliteId": str},
    total=False,
)

ClientListSatellitesResponseTypeDef = TypedDict(
    "ClientListSatellitesResponseTypeDef",
    {"nextToken": str, "satellites": List[ClientListSatellitesResponsesatellitesTypeDef]},
    total=False,
)

ClientListTagsForResourceResponseTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTypeDef", {"tags": Dict[str, str]}, total=False
)

ClientReserveContactResponseTypeDef = TypedDict(
    "ClientReserveContactResponseTypeDef", {"contactId": str}, total=False
)

_RequiredClientUpdateConfigConfigDataantennaDownlinkConfigspectrumConfigbandwidthTypeDef = TypedDict(
    "_RequiredClientUpdateConfigConfigDataantennaDownlinkConfigspectrumConfigbandwidthTypeDef",
    {"units": Literal["GHz", "MHz", "kHz"]},
)
_OptionalClientUpdateConfigConfigDataantennaDownlinkConfigspectrumConfigbandwidthTypeDef = TypedDict(
    "_OptionalClientUpdateConfigConfigDataantennaDownlinkConfigspectrumConfigbandwidthTypeDef",
    {"value": float},
    total=False,
)


class ClientUpdateConfigConfigDataantennaDownlinkConfigspectrumConfigbandwidthTypeDef(
    _RequiredClientUpdateConfigConfigDataantennaDownlinkConfigspectrumConfigbandwidthTypeDef,
    _OptionalClientUpdateConfigConfigDataantennaDownlinkConfigspectrumConfigbandwidthTypeDef,
):
    pass


ClientUpdateConfigConfigDataantennaDownlinkConfigspectrumConfigcenterFrequencyTypeDef = TypedDict(
    "ClientUpdateConfigConfigDataantennaDownlinkConfigspectrumConfigcenterFrequencyTypeDef",
    {"units": Literal["GHz", "MHz", "kHz"], "value": float},
    total=False,
)

_RequiredClientUpdateConfigConfigDataantennaDownlinkConfigspectrumConfigTypeDef = TypedDict(
    "_RequiredClientUpdateConfigConfigDataantennaDownlinkConfigspectrumConfigTypeDef",
    {"bandwidth": ClientUpdateConfigConfigDataantennaDownlinkConfigspectrumConfigbandwidthTypeDef},
)
_OptionalClientUpdateConfigConfigDataantennaDownlinkConfigspectrumConfigTypeDef = TypedDict(
    "_OptionalClientUpdateConfigConfigDataantennaDownlinkConfigspectrumConfigTypeDef",
    {
        "centerFrequency": ClientUpdateConfigConfigDataantennaDownlinkConfigspectrumConfigcenterFrequencyTypeDef,
        "polarization": Literal["LEFT_HAND", "NONE", "RIGHT_HAND"],
    },
    total=False,
)


class ClientUpdateConfigConfigDataantennaDownlinkConfigspectrumConfigTypeDef(
    _RequiredClientUpdateConfigConfigDataantennaDownlinkConfigspectrumConfigTypeDef,
    _OptionalClientUpdateConfigConfigDataantennaDownlinkConfigspectrumConfigTypeDef,
):
    pass


ClientUpdateConfigConfigDataantennaDownlinkConfigTypeDef = TypedDict(
    "ClientUpdateConfigConfigDataantennaDownlinkConfigTypeDef",
    {"spectrumConfig": ClientUpdateConfigConfigDataantennaDownlinkConfigspectrumConfigTypeDef},
)

ClientUpdateConfigConfigDataantennaDownlinkDemodDecodeConfigdecodeConfigTypeDef = TypedDict(
    "ClientUpdateConfigConfigDataantennaDownlinkDemodDecodeConfigdecodeConfigTypeDef",
    {"unvalidatedJSON": str},
    total=False,
)

ClientUpdateConfigConfigDataantennaDownlinkDemodDecodeConfigdemodulationConfigTypeDef = TypedDict(
    "ClientUpdateConfigConfigDataantennaDownlinkDemodDecodeConfigdemodulationConfigTypeDef",
    {"unvalidatedJSON": str},
    total=False,
)

ClientUpdateConfigConfigDataantennaDownlinkDemodDecodeConfigspectrumConfigbandwidthTypeDef = TypedDict(
    "ClientUpdateConfigConfigDataantennaDownlinkDemodDecodeConfigspectrumConfigbandwidthTypeDef",
    {"units": Literal["GHz", "MHz", "kHz"], "value": float},
    total=False,
)

ClientUpdateConfigConfigDataantennaDownlinkDemodDecodeConfigspectrumConfigcenterFrequencyTypeDef = TypedDict(
    "ClientUpdateConfigConfigDataantennaDownlinkDemodDecodeConfigspectrumConfigcenterFrequencyTypeDef",
    {"units": Literal["GHz", "MHz", "kHz"], "value": float},
    total=False,
)

ClientUpdateConfigConfigDataantennaDownlinkDemodDecodeConfigspectrumConfigTypeDef = TypedDict(
    "ClientUpdateConfigConfigDataantennaDownlinkDemodDecodeConfigspectrumConfigTypeDef",
    {
        "bandwidth": ClientUpdateConfigConfigDataantennaDownlinkDemodDecodeConfigspectrumConfigbandwidthTypeDef,
        "centerFrequency": ClientUpdateConfigConfigDataantennaDownlinkDemodDecodeConfigspectrumConfigcenterFrequencyTypeDef,
        "polarization": Literal["LEFT_HAND", "NONE", "RIGHT_HAND"],
    },
    total=False,
)

ClientUpdateConfigConfigDataantennaDownlinkDemodDecodeConfigTypeDef = TypedDict(
    "ClientUpdateConfigConfigDataantennaDownlinkDemodDecodeConfigTypeDef",
    {
        "decodeConfig": ClientUpdateConfigConfigDataantennaDownlinkDemodDecodeConfigdecodeConfigTypeDef,
        "demodulationConfig": ClientUpdateConfigConfigDataantennaDownlinkDemodDecodeConfigdemodulationConfigTypeDef,
        "spectrumConfig": ClientUpdateConfigConfigDataantennaDownlinkDemodDecodeConfigspectrumConfigTypeDef,
    },
    total=False,
)

ClientUpdateConfigConfigDataantennaUplinkConfigspectrumConfigcenterFrequencyTypeDef = TypedDict(
    "ClientUpdateConfigConfigDataantennaUplinkConfigspectrumConfigcenterFrequencyTypeDef",
    {"units": Literal["GHz", "MHz", "kHz"], "value": float},
    total=False,
)

ClientUpdateConfigConfigDataantennaUplinkConfigspectrumConfigTypeDef = TypedDict(
    "ClientUpdateConfigConfigDataantennaUplinkConfigspectrumConfigTypeDef",
    {
        "centerFrequency": ClientUpdateConfigConfigDataantennaUplinkConfigspectrumConfigcenterFrequencyTypeDef,
        "polarization": Literal["LEFT_HAND", "NONE", "RIGHT_HAND"],
    },
    total=False,
)

ClientUpdateConfigConfigDataantennaUplinkConfigtargetEirpTypeDef = TypedDict(
    "ClientUpdateConfigConfigDataantennaUplinkConfigtargetEirpTypeDef",
    {"units": str, "value": float},
    total=False,
)

ClientUpdateConfigConfigDataantennaUplinkConfigTypeDef = TypedDict(
    "ClientUpdateConfigConfigDataantennaUplinkConfigTypeDef",
    {
        "spectrumConfig": ClientUpdateConfigConfigDataantennaUplinkConfigspectrumConfigTypeDef,
        "targetEirp": ClientUpdateConfigConfigDataantennaUplinkConfigtargetEirpTypeDef,
    },
    total=False,
)

ClientUpdateConfigConfigDatadataflowEndpointConfigTypeDef = TypedDict(
    "ClientUpdateConfigConfigDatadataflowEndpointConfigTypeDef",
    {"dataflowEndpointName": str, "dataflowEndpointRegion": str},
    total=False,
)

ClientUpdateConfigConfigDatatrackingConfigTypeDef = TypedDict(
    "ClientUpdateConfigConfigDatatrackingConfigTypeDef",
    {"autotrack": Literal["PREFERRED", "REMOVED", "REQUIRED"]},
    total=False,
)

ClientUpdateConfigConfigDatauplinkEchoConfigTypeDef = TypedDict(
    "ClientUpdateConfigConfigDatauplinkEchoConfigTypeDef",
    {"antennaUplinkConfigArn": str, "enabled": bool},
    total=False,
)

ClientUpdateConfigConfigDataTypeDef = TypedDict(
    "ClientUpdateConfigConfigDataTypeDef",
    {
        "antennaDownlinkConfig": ClientUpdateConfigConfigDataantennaDownlinkConfigTypeDef,
        "antennaDownlinkDemodDecodeConfig": ClientUpdateConfigConfigDataantennaDownlinkDemodDecodeConfigTypeDef,
        "antennaUplinkConfig": ClientUpdateConfigConfigDataantennaUplinkConfigTypeDef,
        "dataflowEndpointConfig": ClientUpdateConfigConfigDatadataflowEndpointConfigTypeDef,
        "trackingConfig": ClientUpdateConfigConfigDatatrackingConfigTypeDef,
        "uplinkEchoConfig": ClientUpdateConfigConfigDatauplinkEchoConfigTypeDef,
    },
    total=False,
)

ClientUpdateConfigResponseTypeDef = TypedDict(
    "ClientUpdateConfigResponseTypeDef",
    {
        "configArn": str,
        "configId": str,
        "configType": Literal[
            "antenna-downlink",
            "antenna-downlink-demod-decode",
            "antenna-uplink",
            "dataflow-endpoint",
            "tracking",
            "uplink-echo",
        ],
    },
    total=False,
)

ClientUpdateMissionProfileResponseTypeDef = TypedDict(
    "ClientUpdateMissionProfileResponseTypeDef", {"missionProfileId": str}, total=False
)

ConfigListItemTypeDef = TypedDict(
    "ConfigListItemTypeDef",
    {
        "configArn": str,
        "configId": str,
        "configType": Literal[
            "antenna-downlink",
            "antenna-downlink-demod-decode",
            "antenna-uplink",
            "dataflow-endpoint",
            "tracking",
            "uplink-echo",
        ],
        "name": str,
    },
    total=False,
)

ListConfigsResponseTypeDef = TypedDict(
    "ListConfigsResponseTypeDef",
    {"configList": List[ConfigListItemTypeDef], "nextToken": str},
    total=False,
)

ElevationTypeDef = TypedDict(
    "ElevationTypeDef", {"unit": Literal["DEGREE_ANGLE", "RADIAN"], "value": float}
)

ContactDataTypeDef = TypedDict(
    "ContactDataTypeDef",
    {
        "contactId": str,
        "contactStatus": Literal[
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
        ],
        "endTime": datetime,
        "errorMessage": str,
        "groundStation": str,
        "maximumElevation": ElevationTypeDef,
        "missionProfileArn": str,
        "postPassEndTime": datetime,
        "prePassStartTime": datetime,
        "region": str,
        "satelliteArn": str,
        "startTime": datetime,
        "tags": Dict[str, str],
    },
    total=False,
)

ListContactsResponseTypeDef = TypedDict(
    "ListContactsResponseTypeDef",
    {"contactList": List[ContactDataTypeDef], "nextToken": str},
    total=False,
)

DataflowEndpointListItemTypeDef = TypedDict(
    "DataflowEndpointListItemTypeDef",
    {"dataflowEndpointGroupArn": str, "dataflowEndpointGroupId": str},
    total=False,
)

ListDataflowEndpointGroupsResponseTypeDef = TypedDict(
    "ListDataflowEndpointGroupsResponseTypeDef",
    {"dataflowEndpointGroupList": List[DataflowEndpointListItemTypeDef], "nextToken": str},
    total=False,
)

GroundStationDataTypeDef = TypedDict(
    "GroundStationDataTypeDef",
    {"groundStationId": str, "groundStationName": str, "region": str},
    total=False,
)

ListGroundStationsResponseTypeDef = TypedDict(
    "ListGroundStationsResponseTypeDef",
    {"groundStationList": List[GroundStationDataTypeDef], "nextToken": str},
    total=False,
)

MissionProfileListItemTypeDef = TypedDict(
    "MissionProfileListItemTypeDef",
    {"missionProfileArn": str, "missionProfileId": str, "name": str, "region": str},
    total=False,
)

ListMissionProfilesResponseTypeDef = TypedDict(
    "ListMissionProfilesResponseTypeDef",
    {"missionProfileList": List[MissionProfileListItemTypeDef], "nextToken": str},
    total=False,
)

SatelliteListItemTypeDef = TypedDict(
    "SatelliteListItemTypeDef",
    {"groundStations": List[str], "noradSatelliteID": int, "satelliteArn": str, "satelliteId": str},
    total=False,
)

ListSatellitesResponseTypeDef = TypedDict(
    "ListSatellitesResponseTypeDef",
    {"nextToken": str, "satellites": List[SatelliteListItemTypeDef]},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)
