"""
Main interface for cloudsearchdomain service type definitions.

Usage::

    from mypy_boto3.cloudsearchdomain.type_defs import ClientSearchResponsefacetsbucketsTypeDef

    data: ClientSearchResponsefacetsbucketsTypeDef = {...}
"""
import sys
from typing import Dict, List

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ClientSearchResponsefacetsbucketsTypeDef",
    "ClientSearchResponsefacetsTypeDef",
    "ClientSearchResponsehitshitTypeDef",
    "ClientSearchResponsehitsTypeDef",
    "ClientSearchResponsestatsTypeDef",
    "ClientSearchResponsestatusTypeDef",
    "ClientSearchResponseTypeDef",
    "ClientSuggestResponsestatusTypeDef",
    "ClientSuggestResponsesuggestsuggestionsTypeDef",
    "ClientSuggestResponsesuggestTypeDef",
    "ClientSuggestResponseTypeDef",
    "ClientUploadDocumentsResponsewarningsTypeDef",
    "ClientUploadDocumentsResponseTypeDef",
)

ClientSearchResponsefacetsbucketsTypeDef = TypedDict(
    "ClientSearchResponsefacetsbucketsTypeDef", {"value": str, "count": int}, total=False
)

ClientSearchResponsefacetsTypeDef = TypedDict(
    "ClientSearchResponsefacetsTypeDef",
    {"buckets": List[ClientSearchResponsefacetsbucketsTypeDef]},
    total=False,
)

ClientSearchResponsehitshitTypeDef = TypedDict(
    "ClientSearchResponsehitshitTypeDef",
    {
        "id": str,
        "fields": Dict[str, List[str]],
        "exprs": Dict[str, str],
        "highlights": Dict[str, str],
    },
    total=False,
)

ClientSearchResponsehitsTypeDef = TypedDict(
    "ClientSearchResponsehitsTypeDef",
    {"found": int, "start": int, "cursor": str, "hit": List[ClientSearchResponsehitshitTypeDef]},
    total=False,
)

ClientSearchResponsestatsTypeDef = TypedDict(
    "ClientSearchResponsestatsTypeDef",
    {
        "min": str,
        "max": str,
        "count": int,
        "missing": int,
        "sum": float,
        "sumOfSquares": float,
        "mean": str,
        "stddev": float,
    },
    total=False,
)

ClientSearchResponsestatusTypeDef = TypedDict(
    "ClientSearchResponsestatusTypeDef", {"timems": int, "rid": str}, total=False
)

ClientSearchResponseTypeDef = TypedDict(
    "ClientSearchResponseTypeDef",
    {
        "status": ClientSearchResponsestatusTypeDef,
        "hits": ClientSearchResponsehitsTypeDef,
        "facets": Dict[str, ClientSearchResponsefacetsTypeDef],
        "stats": Dict[str, ClientSearchResponsestatsTypeDef],
    },
    total=False,
)

ClientSuggestResponsestatusTypeDef = TypedDict(
    "ClientSuggestResponsestatusTypeDef", {"timems": int, "rid": str}, total=False
)

ClientSuggestResponsesuggestsuggestionsTypeDef = TypedDict(
    "ClientSuggestResponsesuggestsuggestionsTypeDef",
    {"suggestion": str, "score": int, "id": str},
    total=False,
)

ClientSuggestResponsesuggestTypeDef = TypedDict(
    "ClientSuggestResponsesuggestTypeDef",
    {
        "query": str,
        "found": int,
        "suggestions": List[ClientSuggestResponsesuggestsuggestionsTypeDef],
    },
    total=False,
)

ClientSuggestResponseTypeDef = TypedDict(
    "ClientSuggestResponseTypeDef",
    {"status": ClientSuggestResponsestatusTypeDef, "suggest": ClientSuggestResponsesuggestTypeDef},
    total=False,
)

ClientUploadDocumentsResponsewarningsTypeDef = TypedDict(
    "ClientUploadDocumentsResponsewarningsTypeDef", {"message": str}, total=False
)

ClientUploadDocumentsResponseTypeDef = TypedDict(
    "ClientUploadDocumentsResponseTypeDef",
    {
        "status": str,
        "adds": int,
        "deletes": int,
        "warnings": List[ClientUploadDocumentsResponsewarningsTypeDef],
    },
    total=False,
)
