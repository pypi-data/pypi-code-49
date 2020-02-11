"""
Main interface for pi service type definitions.

Usage::

    from mypy_boto3.pi.type_defs import ClientDescribeDimensionKeysGroupByTypeDef

    data: ClientDescribeDimensionKeysGroupByTypeDef = {...}
"""
from datetime import datetime
import sys
from typing import Dict, List

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ClientDescribeDimensionKeysGroupByTypeDef",
    "ClientDescribeDimensionKeysPartitionByTypeDef",
    "ClientDescribeDimensionKeysResponseKeysTypeDef",
    "ClientDescribeDimensionKeysResponsePartitionKeysTypeDef",
    "ClientDescribeDimensionKeysResponseTypeDef",
    "ClientGetResourceMetricsMetricQueriesGroupByTypeDef",
    "ClientGetResourceMetricsMetricQueriesTypeDef",
    "ClientGetResourceMetricsResponseMetricListDataPointsTypeDef",
    "ClientGetResourceMetricsResponseMetricListKeyTypeDef",
    "ClientGetResourceMetricsResponseMetricListTypeDef",
    "ClientGetResourceMetricsResponseTypeDef",
)

_RequiredClientDescribeDimensionKeysGroupByTypeDef = TypedDict(
    "_RequiredClientDescribeDimensionKeysGroupByTypeDef", {"Group": str}
)
_OptionalClientDescribeDimensionKeysGroupByTypeDef = TypedDict(
    "_OptionalClientDescribeDimensionKeysGroupByTypeDef",
    {"Dimensions": List[str], "Limit": int},
    total=False,
)


class ClientDescribeDimensionKeysGroupByTypeDef(
    _RequiredClientDescribeDimensionKeysGroupByTypeDef,
    _OptionalClientDescribeDimensionKeysGroupByTypeDef,
):
    pass


_RequiredClientDescribeDimensionKeysPartitionByTypeDef = TypedDict(
    "_RequiredClientDescribeDimensionKeysPartitionByTypeDef", {"Group": str}
)
_OptionalClientDescribeDimensionKeysPartitionByTypeDef = TypedDict(
    "_OptionalClientDescribeDimensionKeysPartitionByTypeDef",
    {"Dimensions": List[str], "Limit": int},
    total=False,
)


class ClientDescribeDimensionKeysPartitionByTypeDef(
    _RequiredClientDescribeDimensionKeysPartitionByTypeDef,
    _OptionalClientDescribeDimensionKeysPartitionByTypeDef,
):
    pass


ClientDescribeDimensionKeysResponseKeysTypeDef = TypedDict(
    "ClientDescribeDimensionKeysResponseKeysTypeDef",
    {"Dimensions": Dict[str, str], "Total": float, "Partitions": List[float]},
    total=False,
)

ClientDescribeDimensionKeysResponsePartitionKeysTypeDef = TypedDict(
    "ClientDescribeDimensionKeysResponsePartitionKeysTypeDef",
    {"Dimensions": Dict[str, str]},
    total=False,
)

ClientDescribeDimensionKeysResponseTypeDef = TypedDict(
    "ClientDescribeDimensionKeysResponseTypeDef",
    {
        "AlignedStartTime": datetime,
        "AlignedEndTime": datetime,
        "PartitionKeys": List[ClientDescribeDimensionKeysResponsePartitionKeysTypeDef],
        "Keys": List[ClientDescribeDimensionKeysResponseKeysTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientGetResourceMetricsMetricQueriesGroupByTypeDef = TypedDict(
    "ClientGetResourceMetricsMetricQueriesGroupByTypeDef",
    {"Group": str, "Dimensions": List[str], "Limit": int},
    total=False,
)

_RequiredClientGetResourceMetricsMetricQueriesTypeDef = TypedDict(
    "_RequiredClientGetResourceMetricsMetricQueriesTypeDef", {"Metric": str}
)
_OptionalClientGetResourceMetricsMetricQueriesTypeDef = TypedDict(
    "_OptionalClientGetResourceMetricsMetricQueriesTypeDef",
    {"GroupBy": ClientGetResourceMetricsMetricQueriesGroupByTypeDef, "Filter": Dict[str, str]},
    total=False,
)


class ClientGetResourceMetricsMetricQueriesTypeDef(
    _RequiredClientGetResourceMetricsMetricQueriesTypeDef,
    _OptionalClientGetResourceMetricsMetricQueriesTypeDef,
):
    pass


ClientGetResourceMetricsResponseMetricListDataPointsTypeDef = TypedDict(
    "ClientGetResourceMetricsResponseMetricListDataPointsTypeDef",
    {"Timestamp": datetime, "Value": float},
    total=False,
)

ClientGetResourceMetricsResponseMetricListKeyTypeDef = TypedDict(
    "ClientGetResourceMetricsResponseMetricListKeyTypeDef",
    {"Metric": str, "Dimensions": Dict[str, str]},
    total=False,
)

ClientGetResourceMetricsResponseMetricListTypeDef = TypedDict(
    "ClientGetResourceMetricsResponseMetricListTypeDef",
    {
        "Key": ClientGetResourceMetricsResponseMetricListKeyTypeDef,
        "DataPoints": List[ClientGetResourceMetricsResponseMetricListDataPointsTypeDef],
    },
    total=False,
)

ClientGetResourceMetricsResponseTypeDef = TypedDict(
    "ClientGetResourceMetricsResponseTypeDef",
    {
        "AlignedStartTime": datetime,
        "AlignedEndTime": datetime,
        "Identifier": str,
        "MetricList": List[ClientGetResourceMetricsResponseMetricListTypeDef],
        "NextToken": str,
    },
    total=False,
)
