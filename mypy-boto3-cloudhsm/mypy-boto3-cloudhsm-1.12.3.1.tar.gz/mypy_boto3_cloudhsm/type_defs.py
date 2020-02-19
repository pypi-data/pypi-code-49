"""
Main interface for cloudhsm service type definitions.

Usage::

    from mypy_boto3.cloudhsm.type_defs import ClientAddTagsToResourceResponseTypeDef

    data: ClientAddTagsToResourceResponseTypeDef = {...}
"""
import sys
from typing import List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ClientAddTagsToResourceResponseTypeDef",
    "ClientAddTagsToResourceTagListTypeDef",
    "ClientCreateHapgResponseTypeDef",
    "ClientCreateHsmResponseTypeDef",
    "ClientCreateLunaClientResponseTypeDef",
    "ClientDeleteHapgResponseTypeDef",
    "ClientDeleteHsmResponseTypeDef",
    "ClientDeleteLunaClientResponseTypeDef",
    "ClientDescribeHapgResponseTypeDef",
    "ClientDescribeHsmResponseTypeDef",
    "ClientDescribeLunaClientResponseTypeDef",
    "ClientGetConfigResponseTypeDef",
    "ClientListAvailableZonesResponseTypeDef",
    "ClientListHapgsResponseTypeDef",
    "ClientListHsmsResponseTypeDef",
    "ClientListLunaClientsResponseTypeDef",
    "ClientListTagsForResourceResponseTagListTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientModifyHapgResponseTypeDef",
    "ClientModifyHsmResponseTypeDef",
    "ClientModifyLunaClientResponseTypeDef",
    "ClientRemoveTagsFromResourceResponseTypeDef",
    "ListHapgsResponseTypeDef",
    "ListHsmsResponseTypeDef",
    "ListLunaClientsResponseTypeDef",
    "PaginatorConfigTypeDef",
)

ClientAddTagsToResourceResponseTypeDef = TypedDict(
    "ClientAddTagsToResourceResponseTypeDef", {"Status": str}, total=False
)

_RequiredClientAddTagsToResourceTagListTypeDef = TypedDict(
    "_RequiredClientAddTagsToResourceTagListTypeDef", {"Key": str}
)
_OptionalClientAddTagsToResourceTagListTypeDef = TypedDict(
    "_OptionalClientAddTagsToResourceTagListTypeDef", {"Value": str}, total=False
)


class ClientAddTagsToResourceTagListTypeDef(
    _RequiredClientAddTagsToResourceTagListTypeDef, _OptionalClientAddTagsToResourceTagListTypeDef
):
    pass


ClientCreateHapgResponseTypeDef = TypedDict(
    "ClientCreateHapgResponseTypeDef", {"HapgArn": str}, total=False
)

ClientCreateHsmResponseTypeDef = TypedDict(
    "ClientCreateHsmResponseTypeDef", {"HsmArn": str}, total=False
)

ClientCreateLunaClientResponseTypeDef = TypedDict(
    "ClientCreateLunaClientResponseTypeDef", {"ClientArn": str}, total=False
)

ClientDeleteHapgResponseTypeDef = TypedDict(
    "ClientDeleteHapgResponseTypeDef", {"Status": str}, total=False
)

ClientDeleteHsmResponseTypeDef = TypedDict(
    "ClientDeleteHsmResponseTypeDef", {"Status": str}, total=False
)

ClientDeleteLunaClientResponseTypeDef = TypedDict(
    "ClientDeleteLunaClientResponseTypeDef", {"Status": str}, total=False
)

ClientDescribeHapgResponseTypeDef = TypedDict(
    "ClientDescribeHapgResponseTypeDef",
    {
        "HapgArn": str,
        "HapgSerial": str,
        "HsmsLastActionFailed": List[str],
        "HsmsPendingDeletion": List[str],
        "HsmsPendingRegistration": List[str],
        "Label": str,
        "LastModifiedTimestamp": str,
        "PartitionSerialList": List[str],
        "State": Literal["READY", "UPDATING", "DEGRADED"],
    },
    total=False,
)

ClientDescribeHsmResponseTypeDef = TypedDict(
    "ClientDescribeHsmResponseTypeDef",
    {
        "HsmArn": str,
        "Status": Literal[
            "PENDING", "RUNNING", "UPDATING", "SUSPENDED", "TERMINATING", "TERMINATED", "DEGRADED"
        ],
        "StatusDetails": str,
        "AvailabilityZone": str,
        "EniId": str,
        "EniIp": str,
        "SubscriptionType": str,
        "SubscriptionStartDate": str,
        "SubscriptionEndDate": str,
        "VpcId": str,
        "SubnetId": str,
        "IamRoleArn": str,
        "SerialNumber": str,
        "VendorName": str,
        "HsmType": str,
        "SoftwareVersion": str,
        "SshPublicKey": str,
        "SshKeyLastUpdated": str,
        "ServerCertUri": str,
        "ServerCertLastUpdated": str,
        "Partitions": List[str],
    },
    total=False,
)

ClientDescribeLunaClientResponseTypeDef = TypedDict(
    "ClientDescribeLunaClientResponseTypeDef",
    {
        "ClientArn": str,
        "Certificate": str,
        "CertificateFingerprint": str,
        "LastModifiedTimestamp": str,
        "Label": str,
    },
    total=False,
)

ClientGetConfigResponseTypeDef = TypedDict(
    "ClientGetConfigResponseTypeDef",
    {"ConfigType": str, "ConfigFile": str, "ConfigCred": str},
    total=False,
)

ClientListAvailableZonesResponseTypeDef = TypedDict(
    "ClientListAvailableZonesResponseTypeDef", {"AZList": List[str]}, total=False
)

ClientListHapgsResponseTypeDef = TypedDict(
    "ClientListHapgsResponseTypeDef", {"HapgList": List[str], "NextToken": str}, total=False
)

ClientListHsmsResponseTypeDef = TypedDict(
    "ClientListHsmsResponseTypeDef", {"HsmList": List[str], "NextToken": str}, total=False
)

ClientListLunaClientsResponseTypeDef = TypedDict(
    "ClientListLunaClientsResponseTypeDef", {"ClientList": List[str], "NextToken": str}, total=False
)

ClientListTagsForResourceResponseTagListTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTagListTypeDef", {"Key": str, "Value": str}, total=False
)

ClientListTagsForResourceResponseTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTypeDef",
    {"TagList": List[ClientListTagsForResourceResponseTagListTypeDef]},
    total=False,
)

ClientModifyHapgResponseTypeDef = TypedDict(
    "ClientModifyHapgResponseTypeDef", {"HapgArn": str}, total=False
)

ClientModifyHsmResponseTypeDef = TypedDict(
    "ClientModifyHsmResponseTypeDef", {"HsmArn": str}, total=False
)

ClientModifyLunaClientResponseTypeDef = TypedDict(
    "ClientModifyLunaClientResponseTypeDef", {"ClientArn": str}, total=False
)

ClientRemoveTagsFromResourceResponseTypeDef = TypedDict(
    "ClientRemoveTagsFromResourceResponseTypeDef", {"Status": str}, total=False
)

_RequiredListHapgsResponseTypeDef = TypedDict(
    "_RequiredListHapgsResponseTypeDef", {"HapgList": List[str]}
)
_OptionalListHapgsResponseTypeDef = TypedDict(
    "_OptionalListHapgsResponseTypeDef", {"NextToken": str}, total=False
)


class ListHapgsResponseTypeDef(
    _RequiredListHapgsResponseTypeDef, _OptionalListHapgsResponseTypeDef
):
    pass


ListHsmsResponseTypeDef = TypedDict(
    "ListHsmsResponseTypeDef", {"HsmList": List[str], "NextToken": str}, total=False
)

_RequiredListLunaClientsResponseTypeDef = TypedDict(
    "_RequiredListLunaClientsResponseTypeDef", {"ClientList": List[str]}
)
_OptionalListLunaClientsResponseTypeDef = TypedDict(
    "_OptionalListLunaClientsResponseTypeDef", {"NextToken": str}, total=False
)


class ListLunaClientsResponseTypeDef(
    _RequiredListLunaClientsResponseTypeDef, _OptionalListLunaClientsResponseTypeDef
):
    pass


PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)
