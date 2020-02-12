"""
Main interface for meteringmarketplace service type definitions.

Usage::

    from mypy_boto3.meteringmarketplace.type_defs import ClientBatchMeterUsageResponseResultsUsageRecordTypeDef

    data: ClientBatchMeterUsageResponseResultsUsageRecordTypeDef = {...}
"""
from datetime import datetime
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
    "ClientBatchMeterUsageResponseResultsUsageRecordTypeDef",
    "ClientBatchMeterUsageResponseResultsTypeDef",
    "ClientBatchMeterUsageResponseUnprocessedRecordsTypeDef",
    "ClientBatchMeterUsageResponseTypeDef",
    "ClientBatchMeterUsageUsageRecordsTypeDef",
    "ClientMeterUsageResponseTypeDef",
    "ClientRegisterUsageResponseTypeDef",
    "ClientResolveCustomerResponseTypeDef",
)

ClientBatchMeterUsageResponseResultsUsageRecordTypeDef = TypedDict(
    "ClientBatchMeterUsageResponseResultsUsageRecordTypeDef",
    {"Timestamp": datetime, "CustomerIdentifier": str, "Dimension": str, "Quantity": int},
    total=False,
)

ClientBatchMeterUsageResponseResultsTypeDef = TypedDict(
    "ClientBatchMeterUsageResponseResultsTypeDef",
    {
        "UsageRecord": ClientBatchMeterUsageResponseResultsUsageRecordTypeDef,
        "MeteringRecordId": str,
        "Status": Literal["Success", "CustomerNotSubscribed", "DuplicateRecord"],
    },
    total=False,
)

ClientBatchMeterUsageResponseUnprocessedRecordsTypeDef = TypedDict(
    "ClientBatchMeterUsageResponseUnprocessedRecordsTypeDef",
    {"Timestamp": datetime, "CustomerIdentifier": str, "Dimension": str, "Quantity": int},
    total=False,
)

ClientBatchMeterUsageResponseTypeDef = TypedDict(
    "ClientBatchMeterUsageResponseTypeDef",
    {
        "Results": List[ClientBatchMeterUsageResponseResultsTypeDef],
        "UnprocessedRecords": List[ClientBatchMeterUsageResponseUnprocessedRecordsTypeDef],
    },
    total=False,
)

_RequiredClientBatchMeterUsageUsageRecordsTypeDef = TypedDict(
    "_RequiredClientBatchMeterUsageUsageRecordsTypeDef", {"Timestamp": datetime}
)
_OptionalClientBatchMeterUsageUsageRecordsTypeDef = TypedDict(
    "_OptionalClientBatchMeterUsageUsageRecordsTypeDef",
    {"CustomerIdentifier": str, "Dimension": str, "Quantity": int},
    total=False,
)


class ClientBatchMeterUsageUsageRecordsTypeDef(
    _RequiredClientBatchMeterUsageUsageRecordsTypeDef,
    _OptionalClientBatchMeterUsageUsageRecordsTypeDef,
):
    pass


ClientMeterUsageResponseTypeDef = TypedDict(
    "ClientMeterUsageResponseTypeDef", {"MeteringRecordId": str}, total=False
)

ClientRegisterUsageResponseTypeDef = TypedDict(
    "ClientRegisterUsageResponseTypeDef",
    {"PublicKeyRotationTimestamp": datetime, "Signature": str},
    total=False,
)

ClientResolveCustomerResponseTypeDef = TypedDict(
    "ClientResolveCustomerResponseTypeDef",
    {"CustomerIdentifier": str, "ProductCode": str},
    total=False,
)
