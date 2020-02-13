"""
Main interface for forecastquery service type definitions.

Usage::

    from mypy_boto3.forecastquery.type_defs import ClientQueryForecastResponseForecastPredictionsTypeDef

    data: ClientQueryForecastResponseForecastPredictionsTypeDef = {...}
"""
import sys
from typing import Dict, List

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ClientQueryForecastResponseForecastPredictionsTypeDef",
    "ClientQueryForecastResponseForecastTypeDef",
    "ClientQueryForecastResponseTypeDef",
)

ClientQueryForecastResponseForecastPredictionsTypeDef = TypedDict(
    "ClientQueryForecastResponseForecastPredictionsTypeDef",
    {"Timestamp": str, "Value": float},
    total=False,
)

ClientQueryForecastResponseForecastTypeDef = TypedDict(
    "ClientQueryForecastResponseForecastTypeDef",
    {"Predictions": Dict[str, List[ClientQueryForecastResponseForecastPredictionsTypeDef]]},
    total=False,
)

ClientQueryForecastResponseTypeDef = TypedDict(
    "ClientQueryForecastResponseTypeDef",
    {"Forecast": ClientQueryForecastResponseForecastTypeDef},
    total=False,
)
