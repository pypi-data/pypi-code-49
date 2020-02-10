"""
Main interface for cloudsearch service type definitions.

Usage::

    from mypy_boto3.cloudsearch.type_defs import ClientBuildSuggestersResponseTypeDef

    data: ClientBuildSuggestersResponseTypeDef = {...}
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
    "ClientBuildSuggestersResponseTypeDef",
    "ClientCreateDomainResponseDomainStatusDocServiceTypeDef",
    "ClientCreateDomainResponseDomainStatusLimitsTypeDef",
    "ClientCreateDomainResponseDomainStatusSearchServiceTypeDef",
    "ClientCreateDomainResponseDomainStatusTypeDef",
    "ClientCreateDomainResponseTypeDef",
    "ClientDefineAnalysisSchemeAnalysisSchemeAnalysisOptionsTypeDef",
    "ClientDefineAnalysisSchemeAnalysisSchemeTypeDef",
    "ClientDefineAnalysisSchemeResponseAnalysisSchemeOptionsAnalysisOptionsTypeDef",
    "ClientDefineAnalysisSchemeResponseAnalysisSchemeOptionsTypeDef",
    "ClientDefineAnalysisSchemeResponseAnalysisSchemeStatusTypeDef",
    "ClientDefineAnalysisSchemeResponseAnalysisSchemeTypeDef",
    "ClientDefineAnalysisSchemeResponseTypeDef",
    "ClientDefineExpressionExpressionTypeDef",
    "ClientDefineExpressionResponseExpressionOptionsTypeDef",
    "ClientDefineExpressionResponseExpressionStatusTypeDef",
    "ClientDefineExpressionResponseExpressionTypeDef",
    "ClientDefineExpressionResponseTypeDef",
    "ClientDefineIndexFieldIndexFieldDateArrayOptionsTypeDef",
    "ClientDefineIndexFieldIndexFieldDateOptionsTypeDef",
    "ClientDefineIndexFieldIndexFieldDoubleArrayOptionsTypeDef",
    "ClientDefineIndexFieldIndexFieldDoubleOptionsTypeDef",
    "ClientDefineIndexFieldIndexFieldIntArrayOptionsTypeDef",
    "ClientDefineIndexFieldIndexFieldIntOptionsTypeDef",
    "ClientDefineIndexFieldIndexFieldLatLonOptionsTypeDef",
    "ClientDefineIndexFieldIndexFieldLiteralArrayOptionsTypeDef",
    "ClientDefineIndexFieldIndexFieldLiteralOptionsTypeDef",
    "ClientDefineIndexFieldIndexFieldTextArrayOptionsTypeDef",
    "ClientDefineIndexFieldIndexFieldTextOptionsTypeDef",
    "ClientDefineIndexFieldIndexFieldTypeDef",
    "ClientDefineIndexFieldResponseIndexFieldOptionsDateArrayOptionsTypeDef",
    "ClientDefineIndexFieldResponseIndexFieldOptionsDateOptionsTypeDef",
    "ClientDefineIndexFieldResponseIndexFieldOptionsDoubleArrayOptionsTypeDef",
    "ClientDefineIndexFieldResponseIndexFieldOptionsDoubleOptionsTypeDef",
    "ClientDefineIndexFieldResponseIndexFieldOptionsIntArrayOptionsTypeDef",
    "ClientDefineIndexFieldResponseIndexFieldOptionsIntOptionsTypeDef",
    "ClientDefineIndexFieldResponseIndexFieldOptionsLatLonOptionsTypeDef",
    "ClientDefineIndexFieldResponseIndexFieldOptionsLiteralArrayOptionsTypeDef",
    "ClientDefineIndexFieldResponseIndexFieldOptionsLiteralOptionsTypeDef",
    "ClientDefineIndexFieldResponseIndexFieldOptionsTextArrayOptionsTypeDef",
    "ClientDefineIndexFieldResponseIndexFieldOptionsTextOptionsTypeDef",
    "ClientDefineIndexFieldResponseIndexFieldOptionsTypeDef",
    "ClientDefineIndexFieldResponseIndexFieldStatusTypeDef",
    "ClientDefineIndexFieldResponseIndexFieldTypeDef",
    "ClientDefineIndexFieldResponseTypeDef",
    "ClientDefineSuggesterResponseSuggesterOptionsDocumentSuggesterOptionsTypeDef",
    "ClientDefineSuggesterResponseSuggesterOptionsTypeDef",
    "ClientDefineSuggesterResponseSuggesterStatusTypeDef",
    "ClientDefineSuggesterResponseSuggesterTypeDef",
    "ClientDefineSuggesterResponseTypeDef",
    "ClientDefineSuggesterSuggesterDocumentSuggesterOptionsTypeDef",
    "ClientDefineSuggesterSuggesterTypeDef",
    "ClientDeleteAnalysisSchemeResponseAnalysisSchemeOptionsAnalysisOptionsTypeDef",
    "ClientDeleteAnalysisSchemeResponseAnalysisSchemeOptionsTypeDef",
    "ClientDeleteAnalysisSchemeResponseAnalysisSchemeStatusTypeDef",
    "ClientDeleteAnalysisSchemeResponseAnalysisSchemeTypeDef",
    "ClientDeleteAnalysisSchemeResponseTypeDef",
    "ClientDeleteDomainResponseDomainStatusDocServiceTypeDef",
    "ClientDeleteDomainResponseDomainStatusLimitsTypeDef",
    "ClientDeleteDomainResponseDomainStatusSearchServiceTypeDef",
    "ClientDeleteDomainResponseDomainStatusTypeDef",
    "ClientDeleteDomainResponseTypeDef",
    "ClientDeleteExpressionResponseExpressionOptionsTypeDef",
    "ClientDeleteExpressionResponseExpressionStatusTypeDef",
    "ClientDeleteExpressionResponseExpressionTypeDef",
    "ClientDeleteExpressionResponseTypeDef",
    "ClientDeleteIndexFieldResponseIndexFieldOptionsDateArrayOptionsTypeDef",
    "ClientDeleteIndexFieldResponseIndexFieldOptionsDateOptionsTypeDef",
    "ClientDeleteIndexFieldResponseIndexFieldOptionsDoubleArrayOptionsTypeDef",
    "ClientDeleteIndexFieldResponseIndexFieldOptionsDoubleOptionsTypeDef",
    "ClientDeleteIndexFieldResponseIndexFieldOptionsIntArrayOptionsTypeDef",
    "ClientDeleteIndexFieldResponseIndexFieldOptionsIntOptionsTypeDef",
    "ClientDeleteIndexFieldResponseIndexFieldOptionsLatLonOptionsTypeDef",
    "ClientDeleteIndexFieldResponseIndexFieldOptionsLiteralArrayOptionsTypeDef",
    "ClientDeleteIndexFieldResponseIndexFieldOptionsLiteralOptionsTypeDef",
    "ClientDeleteIndexFieldResponseIndexFieldOptionsTextArrayOptionsTypeDef",
    "ClientDeleteIndexFieldResponseIndexFieldOptionsTextOptionsTypeDef",
    "ClientDeleteIndexFieldResponseIndexFieldOptionsTypeDef",
    "ClientDeleteIndexFieldResponseIndexFieldStatusTypeDef",
    "ClientDeleteIndexFieldResponseIndexFieldTypeDef",
    "ClientDeleteIndexFieldResponseTypeDef",
    "ClientDeleteSuggesterResponseSuggesterOptionsDocumentSuggesterOptionsTypeDef",
    "ClientDeleteSuggesterResponseSuggesterOptionsTypeDef",
    "ClientDeleteSuggesterResponseSuggesterStatusTypeDef",
    "ClientDeleteSuggesterResponseSuggesterTypeDef",
    "ClientDeleteSuggesterResponseTypeDef",
    "ClientDescribeAnalysisSchemesResponseAnalysisSchemesOptionsAnalysisOptionsTypeDef",
    "ClientDescribeAnalysisSchemesResponseAnalysisSchemesOptionsTypeDef",
    "ClientDescribeAnalysisSchemesResponseAnalysisSchemesStatusTypeDef",
    "ClientDescribeAnalysisSchemesResponseAnalysisSchemesTypeDef",
    "ClientDescribeAnalysisSchemesResponseTypeDef",
    "ClientDescribeAvailabilityOptionsResponseAvailabilityOptionsStatusTypeDef",
    "ClientDescribeAvailabilityOptionsResponseAvailabilityOptionsTypeDef",
    "ClientDescribeAvailabilityOptionsResponseTypeDef",
    "ClientDescribeDomainEndpointOptionsResponseDomainEndpointOptionsOptionsTypeDef",
    "ClientDescribeDomainEndpointOptionsResponseDomainEndpointOptionsStatusTypeDef",
    "ClientDescribeDomainEndpointOptionsResponseDomainEndpointOptionsTypeDef",
    "ClientDescribeDomainEndpointOptionsResponseTypeDef",
    "ClientDescribeDomainsResponseDomainStatusListDocServiceTypeDef",
    "ClientDescribeDomainsResponseDomainStatusListLimitsTypeDef",
    "ClientDescribeDomainsResponseDomainStatusListSearchServiceTypeDef",
    "ClientDescribeDomainsResponseDomainStatusListTypeDef",
    "ClientDescribeDomainsResponseTypeDef",
    "ClientDescribeExpressionsResponseExpressionsOptionsTypeDef",
    "ClientDescribeExpressionsResponseExpressionsStatusTypeDef",
    "ClientDescribeExpressionsResponseExpressionsTypeDef",
    "ClientDescribeExpressionsResponseTypeDef",
    "ClientDescribeIndexFieldsResponseIndexFieldsOptionsDateArrayOptionsTypeDef",
    "ClientDescribeIndexFieldsResponseIndexFieldsOptionsDateOptionsTypeDef",
    "ClientDescribeIndexFieldsResponseIndexFieldsOptionsDoubleArrayOptionsTypeDef",
    "ClientDescribeIndexFieldsResponseIndexFieldsOptionsDoubleOptionsTypeDef",
    "ClientDescribeIndexFieldsResponseIndexFieldsOptionsIntArrayOptionsTypeDef",
    "ClientDescribeIndexFieldsResponseIndexFieldsOptionsIntOptionsTypeDef",
    "ClientDescribeIndexFieldsResponseIndexFieldsOptionsLatLonOptionsTypeDef",
    "ClientDescribeIndexFieldsResponseIndexFieldsOptionsLiteralArrayOptionsTypeDef",
    "ClientDescribeIndexFieldsResponseIndexFieldsOptionsLiteralOptionsTypeDef",
    "ClientDescribeIndexFieldsResponseIndexFieldsOptionsTextArrayOptionsTypeDef",
    "ClientDescribeIndexFieldsResponseIndexFieldsOptionsTextOptionsTypeDef",
    "ClientDescribeIndexFieldsResponseIndexFieldsOptionsTypeDef",
    "ClientDescribeIndexFieldsResponseIndexFieldsStatusTypeDef",
    "ClientDescribeIndexFieldsResponseIndexFieldsTypeDef",
    "ClientDescribeIndexFieldsResponseTypeDef",
    "ClientDescribeScalingParametersResponseScalingParametersOptionsTypeDef",
    "ClientDescribeScalingParametersResponseScalingParametersStatusTypeDef",
    "ClientDescribeScalingParametersResponseScalingParametersTypeDef",
    "ClientDescribeScalingParametersResponseTypeDef",
    "ClientDescribeServiceAccessPoliciesResponseAccessPoliciesStatusTypeDef",
    "ClientDescribeServiceAccessPoliciesResponseAccessPoliciesTypeDef",
    "ClientDescribeServiceAccessPoliciesResponseTypeDef",
    "ClientDescribeSuggestersResponseSuggestersOptionsDocumentSuggesterOptionsTypeDef",
    "ClientDescribeSuggestersResponseSuggestersOptionsTypeDef",
    "ClientDescribeSuggestersResponseSuggestersStatusTypeDef",
    "ClientDescribeSuggestersResponseSuggestersTypeDef",
    "ClientDescribeSuggestersResponseTypeDef",
    "ClientIndexDocumentsResponseTypeDef",
    "ClientListDomainNamesResponseTypeDef",
    "ClientUpdateAvailabilityOptionsResponseAvailabilityOptionsStatusTypeDef",
    "ClientUpdateAvailabilityOptionsResponseAvailabilityOptionsTypeDef",
    "ClientUpdateAvailabilityOptionsResponseTypeDef",
    "ClientUpdateDomainEndpointOptionsDomainEndpointOptionsTypeDef",
    "ClientUpdateDomainEndpointOptionsResponseDomainEndpointOptionsOptionsTypeDef",
    "ClientUpdateDomainEndpointOptionsResponseDomainEndpointOptionsStatusTypeDef",
    "ClientUpdateDomainEndpointOptionsResponseDomainEndpointOptionsTypeDef",
    "ClientUpdateDomainEndpointOptionsResponseTypeDef",
    "ClientUpdateScalingParametersResponseScalingParametersOptionsTypeDef",
    "ClientUpdateScalingParametersResponseScalingParametersStatusTypeDef",
    "ClientUpdateScalingParametersResponseScalingParametersTypeDef",
    "ClientUpdateScalingParametersResponseTypeDef",
    "ClientUpdateScalingParametersScalingParametersTypeDef",
    "ClientUpdateServiceAccessPoliciesResponseAccessPoliciesStatusTypeDef",
    "ClientUpdateServiceAccessPoliciesResponseAccessPoliciesTypeDef",
    "ClientUpdateServiceAccessPoliciesResponseTypeDef",
)

ClientBuildSuggestersResponseTypeDef = TypedDict(
    "ClientBuildSuggestersResponseTypeDef", {"FieldNames": List[str]}, total=False
)

ClientCreateDomainResponseDomainStatusDocServiceTypeDef = TypedDict(
    "ClientCreateDomainResponseDomainStatusDocServiceTypeDef", {"Endpoint": str}, total=False
)

ClientCreateDomainResponseDomainStatusLimitsTypeDef = TypedDict(
    "ClientCreateDomainResponseDomainStatusLimitsTypeDef",
    {"MaximumReplicationCount": int, "MaximumPartitionCount": int},
    total=False,
)

ClientCreateDomainResponseDomainStatusSearchServiceTypeDef = TypedDict(
    "ClientCreateDomainResponseDomainStatusSearchServiceTypeDef", {"Endpoint": str}, total=False
)

ClientCreateDomainResponseDomainStatusTypeDef = TypedDict(
    "ClientCreateDomainResponseDomainStatusTypeDef",
    {
        "DomainId": str,
        "DomainName": str,
        "ARN": str,
        "Created": bool,
        "Deleted": bool,
        "DocService": ClientCreateDomainResponseDomainStatusDocServiceTypeDef,
        "SearchService": ClientCreateDomainResponseDomainStatusSearchServiceTypeDef,
        "RequiresIndexDocuments": bool,
        "Processing": bool,
        "SearchInstanceType": str,
        "SearchPartitionCount": int,
        "SearchInstanceCount": int,
        "Limits": ClientCreateDomainResponseDomainStatusLimitsTypeDef,
    },
    total=False,
)

ClientCreateDomainResponseTypeDef = TypedDict(
    "ClientCreateDomainResponseTypeDef",
    {"DomainStatus": ClientCreateDomainResponseDomainStatusTypeDef},
    total=False,
)

ClientDefineAnalysisSchemeAnalysisSchemeAnalysisOptionsTypeDef = TypedDict(
    "ClientDefineAnalysisSchemeAnalysisSchemeAnalysisOptionsTypeDef",
    {
        "Synonyms": str,
        "Stopwords": str,
        "StemmingDictionary": str,
        "JapaneseTokenizationDictionary": str,
        "AlgorithmicStemming": Literal["none", "minimal", "light", "full"],
    },
    total=False,
)

_RequiredClientDefineAnalysisSchemeAnalysisSchemeTypeDef = TypedDict(
    "_RequiredClientDefineAnalysisSchemeAnalysisSchemeTypeDef", {"AnalysisSchemeName": str}
)
_OptionalClientDefineAnalysisSchemeAnalysisSchemeTypeDef = TypedDict(
    "_OptionalClientDefineAnalysisSchemeAnalysisSchemeTypeDef",
    {
        "AnalysisSchemeLanguage": Literal[
            "ar",
            "bg",
            "ca",
            "cs",
            "da",
            "de",
            "el",
            "en",
            "es",
            "eu",
            "fa",
            "fi",
            "fr",
            "ga",
            "gl",
            "he",
            "hi",
            "hu",
            "hy",
            "id",
            "it",
            "ja",
            "ko",
            "lv",
            "mul",
            "nl",
            "no",
            "pt",
            "ro",
            "ru",
            "sv",
            "th",
            "tr",
            "zh-Hans",
            "zh-Hant",
        ],
        "AnalysisOptions": ClientDefineAnalysisSchemeAnalysisSchemeAnalysisOptionsTypeDef,
    },
    total=False,
)


class ClientDefineAnalysisSchemeAnalysisSchemeTypeDef(
    _RequiredClientDefineAnalysisSchemeAnalysisSchemeTypeDef,
    _OptionalClientDefineAnalysisSchemeAnalysisSchemeTypeDef,
):
    pass


ClientDefineAnalysisSchemeResponseAnalysisSchemeOptionsAnalysisOptionsTypeDef = TypedDict(
    "ClientDefineAnalysisSchemeResponseAnalysisSchemeOptionsAnalysisOptionsTypeDef",
    {
        "Synonyms": str,
        "Stopwords": str,
        "StemmingDictionary": str,
        "JapaneseTokenizationDictionary": str,
        "AlgorithmicStemming": Literal["none", "minimal", "light", "full"],
    },
    total=False,
)

ClientDefineAnalysisSchemeResponseAnalysisSchemeOptionsTypeDef = TypedDict(
    "ClientDefineAnalysisSchemeResponseAnalysisSchemeOptionsTypeDef",
    {
        "AnalysisSchemeName": str,
        "AnalysisSchemeLanguage": Literal[
            "ar",
            "bg",
            "ca",
            "cs",
            "da",
            "de",
            "el",
            "en",
            "es",
            "eu",
            "fa",
            "fi",
            "fr",
            "ga",
            "gl",
            "he",
            "hi",
            "hu",
            "hy",
            "id",
            "it",
            "ja",
            "ko",
            "lv",
            "mul",
            "nl",
            "no",
            "pt",
            "ro",
            "ru",
            "sv",
            "th",
            "tr",
            "zh-Hans",
            "zh-Hant",
        ],
        "AnalysisOptions": ClientDefineAnalysisSchemeResponseAnalysisSchemeOptionsAnalysisOptionsTypeDef,
    },
    total=False,
)

ClientDefineAnalysisSchemeResponseAnalysisSchemeStatusTypeDef = TypedDict(
    "ClientDefineAnalysisSchemeResponseAnalysisSchemeStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": Literal["RequiresIndexDocuments", "Processing", "Active", "FailedToValidate"],
        "PendingDeletion": bool,
    },
    total=False,
)

ClientDefineAnalysisSchemeResponseAnalysisSchemeTypeDef = TypedDict(
    "ClientDefineAnalysisSchemeResponseAnalysisSchemeTypeDef",
    {
        "Options": ClientDefineAnalysisSchemeResponseAnalysisSchemeOptionsTypeDef,
        "Status": ClientDefineAnalysisSchemeResponseAnalysisSchemeStatusTypeDef,
    },
    total=False,
)

ClientDefineAnalysisSchemeResponseTypeDef = TypedDict(
    "ClientDefineAnalysisSchemeResponseTypeDef",
    {"AnalysisScheme": ClientDefineAnalysisSchemeResponseAnalysisSchemeTypeDef},
    total=False,
)

_RequiredClientDefineExpressionExpressionTypeDef = TypedDict(
    "_RequiredClientDefineExpressionExpressionTypeDef", {"ExpressionName": str}
)
_OptionalClientDefineExpressionExpressionTypeDef = TypedDict(
    "_OptionalClientDefineExpressionExpressionTypeDef", {"ExpressionValue": str}, total=False
)


class ClientDefineExpressionExpressionTypeDef(
    _RequiredClientDefineExpressionExpressionTypeDef,
    _OptionalClientDefineExpressionExpressionTypeDef,
):
    pass


ClientDefineExpressionResponseExpressionOptionsTypeDef = TypedDict(
    "ClientDefineExpressionResponseExpressionOptionsTypeDef",
    {"ExpressionName": str, "ExpressionValue": str},
    total=False,
)

ClientDefineExpressionResponseExpressionStatusTypeDef = TypedDict(
    "ClientDefineExpressionResponseExpressionStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": Literal["RequiresIndexDocuments", "Processing", "Active", "FailedToValidate"],
        "PendingDeletion": bool,
    },
    total=False,
)

ClientDefineExpressionResponseExpressionTypeDef = TypedDict(
    "ClientDefineExpressionResponseExpressionTypeDef",
    {
        "Options": ClientDefineExpressionResponseExpressionOptionsTypeDef,
        "Status": ClientDefineExpressionResponseExpressionStatusTypeDef,
    },
    total=False,
)

ClientDefineExpressionResponseTypeDef = TypedDict(
    "ClientDefineExpressionResponseTypeDef",
    {"Expression": ClientDefineExpressionResponseExpressionTypeDef},
    total=False,
)

ClientDefineIndexFieldIndexFieldDateArrayOptionsTypeDef = TypedDict(
    "ClientDefineIndexFieldIndexFieldDateArrayOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceFields": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
    },
    total=False,
)

ClientDefineIndexFieldIndexFieldDateOptionsTypeDef = TypedDict(
    "ClientDefineIndexFieldIndexFieldDateOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceField": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
        "SortEnabled": bool,
    },
    total=False,
)

ClientDefineIndexFieldIndexFieldDoubleArrayOptionsTypeDef = TypedDict(
    "ClientDefineIndexFieldIndexFieldDoubleArrayOptionsTypeDef",
    {
        "DefaultValue": float,
        "SourceFields": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
    },
    total=False,
)

ClientDefineIndexFieldIndexFieldDoubleOptionsTypeDef = TypedDict(
    "ClientDefineIndexFieldIndexFieldDoubleOptionsTypeDef",
    {
        "DefaultValue": float,
        "SourceField": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
        "SortEnabled": bool,
    },
    total=False,
)

ClientDefineIndexFieldIndexFieldIntArrayOptionsTypeDef = TypedDict(
    "ClientDefineIndexFieldIndexFieldIntArrayOptionsTypeDef",
    {
        "DefaultValue": int,
        "SourceFields": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
    },
    total=False,
)

ClientDefineIndexFieldIndexFieldIntOptionsTypeDef = TypedDict(
    "ClientDefineIndexFieldIndexFieldIntOptionsTypeDef",
    {
        "DefaultValue": int,
        "SourceField": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
        "SortEnabled": bool,
    },
    total=False,
)

ClientDefineIndexFieldIndexFieldLatLonOptionsTypeDef = TypedDict(
    "ClientDefineIndexFieldIndexFieldLatLonOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceField": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
        "SortEnabled": bool,
    },
    total=False,
)

ClientDefineIndexFieldIndexFieldLiteralArrayOptionsTypeDef = TypedDict(
    "ClientDefineIndexFieldIndexFieldLiteralArrayOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceFields": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
    },
    total=False,
)

ClientDefineIndexFieldIndexFieldLiteralOptionsTypeDef = TypedDict(
    "ClientDefineIndexFieldIndexFieldLiteralOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceField": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
        "SortEnabled": bool,
    },
    total=False,
)

ClientDefineIndexFieldIndexFieldTextArrayOptionsTypeDef = TypedDict(
    "ClientDefineIndexFieldIndexFieldTextArrayOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceFields": str,
        "ReturnEnabled": bool,
        "HighlightEnabled": bool,
        "AnalysisScheme": str,
    },
    total=False,
)

ClientDefineIndexFieldIndexFieldTextOptionsTypeDef = TypedDict(
    "ClientDefineIndexFieldIndexFieldTextOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceField": str,
        "ReturnEnabled": bool,
        "SortEnabled": bool,
        "HighlightEnabled": bool,
        "AnalysisScheme": str,
    },
    total=False,
)

_RequiredClientDefineIndexFieldIndexFieldTypeDef = TypedDict(
    "_RequiredClientDefineIndexFieldIndexFieldTypeDef", {"IndexFieldName": str}
)
_OptionalClientDefineIndexFieldIndexFieldTypeDef = TypedDict(
    "_OptionalClientDefineIndexFieldIndexFieldTypeDef",
    {
        "IndexFieldType": Literal[
            "int",
            "double",
            "literal",
            "text",
            "date",
            "latlon",
            "int-array",
            "double-array",
            "literal-array",
            "text-array",
            "date-array",
        ],
        "IntOptions": ClientDefineIndexFieldIndexFieldIntOptionsTypeDef,
        "DoubleOptions": ClientDefineIndexFieldIndexFieldDoubleOptionsTypeDef,
        "LiteralOptions": ClientDefineIndexFieldIndexFieldLiteralOptionsTypeDef,
        "TextOptions": ClientDefineIndexFieldIndexFieldTextOptionsTypeDef,
        "DateOptions": ClientDefineIndexFieldIndexFieldDateOptionsTypeDef,
        "LatLonOptions": ClientDefineIndexFieldIndexFieldLatLonOptionsTypeDef,
        "IntArrayOptions": ClientDefineIndexFieldIndexFieldIntArrayOptionsTypeDef,
        "DoubleArrayOptions": ClientDefineIndexFieldIndexFieldDoubleArrayOptionsTypeDef,
        "LiteralArrayOptions": ClientDefineIndexFieldIndexFieldLiteralArrayOptionsTypeDef,
        "TextArrayOptions": ClientDefineIndexFieldIndexFieldTextArrayOptionsTypeDef,
        "DateArrayOptions": ClientDefineIndexFieldIndexFieldDateArrayOptionsTypeDef,
    },
    total=False,
)


class ClientDefineIndexFieldIndexFieldTypeDef(
    _RequiredClientDefineIndexFieldIndexFieldTypeDef,
    _OptionalClientDefineIndexFieldIndexFieldTypeDef,
):
    pass


ClientDefineIndexFieldResponseIndexFieldOptionsDateArrayOptionsTypeDef = TypedDict(
    "ClientDefineIndexFieldResponseIndexFieldOptionsDateArrayOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceFields": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
    },
    total=False,
)

ClientDefineIndexFieldResponseIndexFieldOptionsDateOptionsTypeDef = TypedDict(
    "ClientDefineIndexFieldResponseIndexFieldOptionsDateOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceField": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
        "SortEnabled": bool,
    },
    total=False,
)

ClientDefineIndexFieldResponseIndexFieldOptionsDoubleArrayOptionsTypeDef = TypedDict(
    "ClientDefineIndexFieldResponseIndexFieldOptionsDoubleArrayOptionsTypeDef",
    {
        "DefaultValue": float,
        "SourceFields": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
    },
    total=False,
)

ClientDefineIndexFieldResponseIndexFieldOptionsDoubleOptionsTypeDef = TypedDict(
    "ClientDefineIndexFieldResponseIndexFieldOptionsDoubleOptionsTypeDef",
    {
        "DefaultValue": float,
        "SourceField": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
        "SortEnabled": bool,
    },
    total=False,
)

ClientDefineIndexFieldResponseIndexFieldOptionsIntArrayOptionsTypeDef = TypedDict(
    "ClientDefineIndexFieldResponseIndexFieldOptionsIntArrayOptionsTypeDef",
    {
        "DefaultValue": int,
        "SourceFields": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
    },
    total=False,
)

ClientDefineIndexFieldResponseIndexFieldOptionsIntOptionsTypeDef = TypedDict(
    "ClientDefineIndexFieldResponseIndexFieldOptionsIntOptionsTypeDef",
    {
        "DefaultValue": int,
        "SourceField": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
        "SortEnabled": bool,
    },
    total=False,
)

ClientDefineIndexFieldResponseIndexFieldOptionsLatLonOptionsTypeDef = TypedDict(
    "ClientDefineIndexFieldResponseIndexFieldOptionsLatLonOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceField": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
        "SortEnabled": bool,
    },
    total=False,
)

ClientDefineIndexFieldResponseIndexFieldOptionsLiteralArrayOptionsTypeDef = TypedDict(
    "ClientDefineIndexFieldResponseIndexFieldOptionsLiteralArrayOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceFields": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
    },
    total=False,
)

ClientDefineIndexFieldResponseIndexFieldOptionsLiteralOptionsTypeDef = TypedDict(
    "ClientDefineIndexFieldResponseIndexFieldOptionsLiteralOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceField": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
        "SortEnabled": bool,
    },
    total=False,
)

ClientDefineIndexFieldResponseIndexFieldOptionsTextArrayOptionsTypeDef = TypedDict(
    "ClientDefineIndexFieldResponseIndexFieldOptionsTextArrayOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceFields": str,
        "ReturnEnabled": bool,
        "HighlightEnabled": bool,
        "AnalysisScheme": str,
    },
    total=False,
)

ClientDefineIndexFieldResponseIndexFieldOptionsTextOptionsTypeDef = TypedDict(
    "ClientDefineIndexFieldResponseIndexFieldOptionsTextOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceField": str,
        "ReturnEnabled": bool,
        "SortEnabled": bool,
        "HighlightEnabled": bool,
        "AnalysisScheme": str,
    },
    total=False,
)

ClientDefineIndexFieldResponseIndexFieldOptionsTypeDef = TypedDict(
    "ClientDefineIndexFieldResponseIndexFieldOptionsTypeDef",
    {
        "IndexFieldName": str,
        "IndexFieldType": Literal[
            "int",
            "double",
            "literal",
            "text",
            "date",
            "latlon",
            "int-array",
            "double-array",
            "literal-array",
            "text-array",
            "date-array",
        ],
        "IntOptions": ClientDefineIndexFieldResponseIndexFieldOptionsIntOptionsTypeDef,
        "DoubleOptions": ClientDefineIndexFieldResponseIndexFieldOptionsDoubleOptionsTypeDef,
        "LiteralOptions": ClientDefineIndexFieldResponseIndexFieldOptionsLiteralOptionsTypeDef,
        "TextOptions": ClientDefineIndexFieldResponseIndexFieldOptionsTextOptionsTypeDef,
        "DateOptions": ClientDefineIndexFieldResponseIndexFieldOptionsDateOptionsTypeDef,
        "LatLonOptions": ClientDefineIndexFieldResponseIndexFieldOptionsLatLonOptionsTypeDef,
        "IntArrayOptions": ClientDefineIndexFieldResponseIndexFieldOptionsIntArrayOptionsTypeDef,
        "DoubleArrayOptions": ClientDefineIndexFieldResponseIndexFieldOptionsDoubleArrayOptionsTypeDef,
        "LiteralArrayOptions": ClientDefineIndexFieldResponseIndexFieldOptionsLiteralArrayOptionsTypeDef,
        "TextArrayOptions": ClientDefineIndexFieldResponseIndexFieldOptionsTextArrayOptionsTypeDef,
        "DateArrayOptions": ClientDefineIndexFieldResponseIndexFieldOptionsDateArrayOptionsTypeDef,
    },
    total=False,
)

ClientDefineIndexFieldResponseIndexFieldStatusTypeDef = TypedDict(
    "ClientDefineIndexFieldResponseIndexFieldStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": Literal["RequiresIndexDocuments", "Processing", "Active", "FailedToValidate"],
        "PendingDeletion": bool,
    },
    total=False,
)

ClientDefineIndexFieldResponseIndexFieldTypeDef = TypedDict(
    "ClientDefineIndexFieldResponseIndexFieldTypeDef",
    {
        "Options": ClientDefineIndexFieldResponseIndexFieldOptionsTypeDef,
        "Status": ClientDefineIndexFieldResponseIndexFieldStatusTypeDef,
    },
    total=False,
)

ClientDefineIndexFieldResponseTypeDef = TypedDict(
    "ClientDefineIndexFieldResponseTypeDef",
    {"IndexField": ClientDefineIndexFieldResponseIndexFieldTypeDef},
    total=False,
)

ClientDefineSuggesterResponseSuggesterOptionsDocumentSuggesterOptionsTypeDef = TypedDict(
    "ClientDefineSuggesterResponseSuggesterOptionsDocumentSuggesterOptionsTypeDef",
    {"SourceField": str, "FuzzyMatching": Literal["none", "low", "high"], "SortExpression": str},
    total=False,
)

ClientDefineSuggesterResponseSuggesterOptionsTypeDef = TypedDict(
    "ClientDefineSuggesterResponseSuggesterOptionsTypeDef",
    {
        "SuggesterName": str,
        "DocumentSuggesterOptions": ClientDefineSuggesterResponseSuggesterOptionsDocumentSuggesterOptionsTypeDef,
    },
    total=False,
)

ClientDefineSuggesterResponseSuggesterStatusTypeDef = TypedDict(
    "ClientDefineSuggesterResponseSuggesterStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": Literal["RequiresIndexDocuments", "Processing", "Active", "FailedToValidate"],
        "PendingDeletion": bool,
    },
    total=False,
)

ClientDefineSuggesterResponseSuggesterTypeDef = TypedDict(
    "ClientDefineSuggesterResponseSuggesterTypeDef",
    {
        "Options": ClientDefineSuggesterResponseSuggesterOptionsTypeDef,
        "Status": ClientDefineSuggesterResponseSuggesterStatusTypeDef,
    },
    total=False,
)

ClientDefineSuggesterResponseTypeDef = TypedDict(
    "ClientDefineSuggesterResponseTypeDef",
    {"Suggester": ClientDefineSuggesterResponseSuggesterTypeDef},
    total=False,
)

ClientDefineSuggesterSuggesterDocumentSuggesterOptionsTypeDef = TypedDict(
    "ClientDefineSuggesterSuggesterDocumentSuggesterOptionsTypeDef",
    {"SourceField": str, "FuzzyMatching": Literal["none", "low", "high"], "SortExpression": str},
    total=False,
)

_RequiredClientDefineSuggesterSuggesterTypeDef = TypedDict(
    "_RequiredClientDefineSuggesterSuggesterTypeDef", {"SuggesterName": str}
)
_OptionalClientDefineSuggesterSuggesterTypeDef = TypedDict(
    "_OptionalClientDefineSuggesterSuggesterTypeDef",
    {"DocumentSuggesterOptions": ClientDefineSuggesterSuggesterDocumentSuggesterOptionsTypeDef},
    total=False,
)


class ClientDefineSuggesterSuggesterTypeDef(
    _RequiredClientDefineSuggesterSuggesterTypeDef, _OptionalClientDefineSuggesterSuggesterTypeDef
):
    pass


ClientDeleteAnalysisSchemeResponseAnalysisSchemeOptionsAnalysisOptionsTypeDef = TypedDict(
    "ClientDeleteAnalysisSchemeResponseAnalysisSchemeOptionsAnalysisOptionsTypeDef",
    {
        "Synonyms": str,
        "Stopwords": str,
        "StemmingDictionary": str,
        "JapaneseTokenizationDictionary": str,
        "AlgorithmicStemming": Literal["none", "minimal", "light", "full"],
    },
    total=False,
)

ClientDeleteAnalysisSchemeResponseAnalysisSchemeOptionsTypeDef = TypedDict(
    "ClientDeleteAnalysisSchemeResponseAnalysisSchemeOptionsTypeDef",
    {
        "AnalysisSchemeName": str,
        "AnalysisSchemeLanguage": Literal[
            "ar",
            "bg",
            "ca",
            "cs",
            "da",
            "de",
            "el",
            "en",
            "es",
            "eu",
            "fa",
            "fi",
            "fr",
            "ga",
            "gl",
            "he",
            "hi",
            "hu",
            "hy",
            "id",
            "it",
            "ja",
            "ko",
            "lv",
            "mul",
            "nl",
            "no",
            "pt",
            "ro",
            "ru",
            "sv",
            "th",
            "tr",
            "zh-Hans",
            "zh-Hant",
        ],
        "AnalysisOptions": ClientDeleteAnalysisSchemeResponseAnalysisSchemeOptionsAnalysisOptionsTypeDef,
    },
    total=False,
)

ClientDeleteAnalysisSchemeResponseAnalysisSchemeStatusTypeDef = TypedDict(
    "ClientDeleteAnalysisSchemeResponseAnalysisSchemeStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": Literal["RequiresIndexDocuments", "Processing", "Active", "FailedToValidate"],
        "PendingDeletion": bool,
    },
    total=False,
)

ClientDeleteAnalysisSchemeResponseAnalysisSchemeTypeDef = TypedDict(
    "ClientDeleteAnalysisSchemeResponseAnalysisSchemeTypeDef",
    {
        "Options": ClientDeleteAnalysisSchemeResponseAnalysisSchemeOptionsTypeDef,
        "Status": ClientDeleteAnalysisSchemeResponseAnalysisSchemeStatusTypeDef,
    },
    total=False,
)

ClientDeleteAnalysisSchemeResponseTypeDef = TypedDict(
    "ClientDeleteAnalysisSchemeResponseTypeDef",
    {"AnalysisScheme": ClientDeleteAnalysisSchemeResponseAnalysisSchemeTypeDef},
    total=False,
)

ClientDeleteDomainResponseDomainStatusDocServiceTypeDef = TypedDict(
    "ClientDeleteDomainResponseDomainStatusDocServiceTypeDef", {"Endpoint": str}, total=False
)

ClientDeleteDomainResponseDomainStatusLimitsTypeDef = TypedDict(
    "ClientDeleteDomainResponseDomainStatusLimitsTypeDef",
    {"MaximumReplicationCount": int, "MaximumPartitionCount": int},
    total=False,
)

ClientDeleteDomainResponseDomainStatusSearchServiceTypeDef = TypedDict(
    "ClientDeleteDomainResponseDomainStatusSearchServiceTypeDef", {"Endpoint": str}, total=False
)

ClientDeleteDomainResponseDomainStatusTypeDef = TypedDict(
    "ClientDeleteDomainResponseDomainStatusTypeDef",
    {
        "DomainId": str,
        "DomainName": str,
        "ARN": str,
        "Created": bool,
        "Deleted": bool,
        "DocService": ClientDeleteDomainResponseDomainStatusDocServiceTypeDef,
        "SearchService": ClientDeleteDomainResponseDomainStatusSearchServiceTypeDef,
        "RequiresIndexDocuments": bool,
        "Processing": bool,
        "SearchInstanceType": str,
        "SearchPartitionCount": int,
        "SearchInstanceCount": int,
        "Limits": ClientDeleteDomainResponseDomainStatusLimitsTypeDef,
    },
    total=False,
)

ClientDeleteDomainResponseTypeDef = TypedDict(
    "ClientDeleteDomainResponseTypeDef",
    {"DomainStatus": ClientDeleteDomainResponseDomainStatusTypeDef},
    total=False,
)

ClientDeleteExpressionResponseExpressionOptionsTypeDef = TypedDict(
    "ClientDeleteExpressionResponseExpressionOptionsTypeDef",
    {"ExpressionName": str, "ExpressionValue": str},
    total=False,
)

ClientDeleteExpressionResponseExpressionStatusTypeDef = TypedDict(
    "ClientDeleteExpressionResponseExpressionStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": Literal["RequiresIndexDocuments", "Processing", "Active", "FailedToValidate"],
        "PendingDeletion": bool,
    },
    total=False,
)

ClientDeleteExpressionResponseExpressionTypeDef = TypedDict(
    "ClientDeleteExpressionResponseExpressionTypeDef",
    {
        "Options": ClientDeleteExpressionResponseExpressionOptionsTypeDef,
        "Status": ClientDeleteExpressionResponseExpressionStatusTypeDef,
    },
    total=False,
)

ClientDeleteExpressionResponseTypeDef = TypedDict(
    "ClientDeleteExpressionResponseTypeDef",
    {"Expression": ClientDeleteExpressionResponseExpressionTypeDef},
    total=False,
)

ClientDeleteIndexFieldResponseIndexFieldOptionsDateArrayOptionsTypeDef = TypedDict(
    "ClientDeleteIndexFieldResponseIndexFieldOptionsDateArrayOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceFields": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
    },
    total=False,
)

ClientDeleteIndexFieldResponseIndexFieldOptionsDateOptionsTypeDef = TypedDict(
    "ClientDeleteIndexFieldResponseIndexFieldOptionsDateOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceField": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
        "SortEnabled": bool,
    },
    total=False,
)

ClientDeleteIndexFieldResponseIndexFieldOptionsDoubleArrayOptionsTypeDef = TypedDict(
    "ClientDeleteIndexFieldResponseIndexFieldOptionsDoubleArrayOptionsTypeDef",
    {
        "DefaultValue": float,
        "SourceFields": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
    },
    total=False,
)

ClientDeleteIndexFieldResponseIndexFieldOptionsDoubleOptionsTypeDef = TypedDict(
    "ClientDeleteIndexFieldResponseIndexFieldOptionsDoubleOptionsTypeDef",
    {
        "DefaultValue": float,
        "SourceField": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
        "SortEnabled": bool,
    },
    total=False,
)

ClientDeleteIndexFieldResponseIndexFieldOptionsIntArrayOptionsTypeDef = TypedDict(
    "ClientDeleteIndexFieldResponseIndexFieldOptionsIntArrayOptionsTypeDef",
    {
        "DefaultValue": int,
        "SourceFields": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
    },
    total=False,
)

ClientDeleteIndexFieldResponseIndexFieldOptionsIntOptionsTypeDef = TypedDict(
    "ClientDeleteIndexFieldResponseIndexFieldOptionsIntOptionsTypeDef",
    {
        "DefaultValue": int,
        "SourceField": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
        "SortEnabled": bool,
    },
    total=False,
)

ClientDeleteIndexFieldResponseIndexFieldOptionsLatLonOptionsTypeDef = TypedDict(
    "ClientDeleteIndexFieldResponseIndexFieldOptionsLatLonOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceField": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
        "SortEnabled": bool,
    },
    total=False,
)

ClientDeleteIndexFieldResponseIndexFieldOptionsLiteralArrayOptionsTypeDef = TypedDict(
    "ClientDeleteIndexFieldResponseIndexFieldOptionsLiteralArrayOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceFields": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
    },
    total=False,
)

ClientDeleteIndexFieldResponseIndexFieldOptionsLiteralOptionsTypeDef = TypedDict(
    "ClientDeleteIndexFieldResponseIndexFieldOptionsLiteralOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceField": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
        "SortEnabled": bool,
    },
    total=False,
)

ClientDeleteIndexFieldResponseIndexFieldOptionsTextArrayOptionsTypeDef = TypedDict(
    "ClientDeleteIndexFieldResponseIndexFieldOptionsTextArrayOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceFields": str,
        "ReturnEnabled": bool,
        "HighlightEnabled": bool,
        "AnalysisScheme": str,
    },
    total=False,
)

ClientDeleteIndexFieldResponseIndexFieldOptionsTextOptionsTypeDef = TypedDict(
    "ClientDeleteIndexFieldResponseIndexFieldOptionsTextOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceField": str,
        "ReturnEnabled": bool,
        "SortEnabled": bool,
        "HighlightEnabled": bool,
        "AnalysisScheme": str,
    },
    total=False,
)

ClientDeleteIndexFieldResponseIndexFieldOptionsTypeDef = TypedDict(
    "ClientDeleteIndexFieldResponseIndexFieldOptionsTypeDef",
    {
        "IndexFieldName": str,
        "IndexFieldType": Literal[
            "int",
            "double",
            "literal",
            "text",
            "date",
            "latlon",
            "int-array",
            "double-array",
            "literal-array",
            "text-array",
            "date-array",
        ],
        "IntOptions": ClientDeleteIndexFieldResponseIndexFieldOptionsIntOptionsTypeDef,
        "DoubleOptions": ClientDeleteIndexFieldResponseIndexFieldOptionsDoubleOptionsTypeDef,
        "LiteralOptions": ClientDeleteIndexFieldResponseIndexFieldOptionsLiteralOptionsTypeDef,
        "TextOptions": ClientDeleteIndexFieldResponseIndexFieldOptionsTextOptionsTypeDef,
        "DateOptions": ClientDeleteIndexFieldResponseIndexFieldOptionsDateOptionsTypeDef,
        "LatLonOptions": ClientDeleteIndexFieldResponseIndexFieldOptionsLatLonOptionsTypeDef,
        "IntArrayOptions": ClientDeleteIndexFieldResponseIndexFieldOptionsIntArrayOptionsTypeDef,
        "DoubleArrayOptions": ClientDeleteIndexFieldResponseIndexFieldOptionsDoubleArrayOptionsTypeDef,
        "LiteralArrayOptions": ClientDeleteIndexFieldResponseIndexFieldOptionsLiteralArrayOptionsTypeDef,
        "TextArrayOptions": ClientDeleteIndexFieldResponseIndexFieldOptionsTextArrayOptionsTypeDef,
        "DateArrayOptions": ClientDeleteIndexFieldResponseIndexFieldOptionsDateArrayOptionsTypeDef,
    },
    total=False,
)

ClientDeleteIndexFieldResponseIndexFieldStatusTypeDef = TypedDict(
    "ClientDeleteIndexFieldResponseIndexFieldStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": Literal["RequiresIndexDocuments", "Processing", "Active", "FailedToValidate"],
        "PendingDeletion": bool,
    },
    total=False,
)

ClientDeleteIndexFieldResponseIndexFieldTypeDef = TypedDict(
    "ClientDeleteIndexFieldResponseIndexFieldTypeDef",
    {
        "Options": ClientDeleteIndexFieldResponseIndexFieldOptionsTypeDef,
        "Status": ClientDeleteIndexFieldResponseIndexFieldStatusTypeDef,
    },
    total=False,
)

ClientDeleteIndexFieldResponseTypeDef = TypedDict(
    "ClientDeleteIndexFieldResponseTypeDef",
    {"IndexField": ClientDeleteIndexFieldResponseIndexFieldTypeDef},
    total=False,
)

ClientDeleteSuggesterResponseSuggesterOptionsDocumentSuggesterOptionsTypeDef = TypedDict(
    "ClientDeleteSuggesterResponseSuggesterOptionsDocumentSuggesterOptionsTypeDef",
    {"SourceField": str, "FuzzyMatching": Literal["none", "low", "high"], "SortExpression": str},
    total=False,
)

ClientDeleteSuggesterResponseSuggesterOptionsTypeDef = TypedDict(
    "ClientDeleteSuggesterResponseSuggesterOptionsTypeDef",
    {
        "SuggesterName": str,
        "DocumentSuggesterOptions": ClientDeleteSuggesterResponseSuggesterOptionsDocumentSuggesterOptionsTypeDef,
    },
    total=False,
)

ClientDeleteSuggesterResponseSuggesterStatusTypeDef = TypedDict(
    "ClientDeleteSuggesterResponseSuggesterStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": Literal["RequiresIndexDocuments", "Processing", "Active", "FailedToValidate"],
        "PendingDeletion": bool,
    },
    total=False,
)

ClientDeleteSuggesterResponseSuggesterTypeDef = TypedDict(
    "ClientDeleteSuggesterResponseSuggesterTypeDef",
    {
        "Options": ClientDeleteSuggesterResponseSuggesterOptionsTypeDef,
        "Status": ClientDeleteSuggesterResponseSuggesterStatusTypeDef,
    },
    total=False,
)

ClientDeleteSuggesterResponseTypeDef = TypedDict(
    "ClientDeleteSuggesterResponseTypeDef",
    {"Suggester": ClientDeleteSuggesterResponseSuggesterTypeDef},
    total=False,
)

ClientDescribeAnalysisSchemesResponseAnalysisSchemesOptionsAnalysisOptionsTypeDef = TypedDict(
    "ClientDescribeAnalysisSchemesResponseAnalysisSchemesOptionsAnalysisOptionsTypeDef",
    {
        "Synonyms": str,
        "Stopwords": str,
        "StemmingDictionary": str,
        "JapaneseTokenizationDictionary": str,
        "AlgorithmicStemming": Literal["none", "minimal", "light", "full"],
    },
    total=False,
)

ClientDescribeAnalysisSchemesResponseAnalysisSchemesOptionsTypeDef = TypedDict(
    "ClientDescribeAnalysisSchemesResponseAnalysisSchemesOptionsTypeDef",
    {
        "AnalysisSchemeName": str,
        "AnalysisSchemeLanguage": Literal[
            "ar",
            "bg",
            "ca",
            "cs",
            "da",
            "de",
            "el",
            "en",
            "es",
            "eu",
            "fa",
            "fi",
            "fr",
            "ga",
            "gl",
            "he",
            "hi",
            "hu",
            "hy",
            "id",
            "it",
            "ja",
            "ko",
            "lv",
            "mul",
            "nl",
            "no",
            "pt",
            "ro",
            "ru",
            "sv",
            "th",
            "tr",
            "zh-Hans",
            "zh-Hant",
        ],
        "AnalysisOptions": ClientDescribeAnalysisSchemesResponseAnalysisSchemesOptionsAnalysisOptionsTypeDef,
    },
    total=False,
)

ClientDescribeAnalysisSchemesResponseAnalysisSchemesStatusTypeDef = TypedDict(
    "ClientDescribeAnalysisSchemesResponseAnalysisSchemesStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": Literal["RequiresIndexDocuments", "Processing", "Active", "FailedToValidate"],
        "PendingDeletion": bool,
    },
    total=False,
)

ClientDescribeAnalysisSchemesResponseAnalysisSchemesTypeDef = TypedDict(
    "ClientDescribeAnalysisSchemesResponseAnalysisSchemesTypeDef",
    {
        "Options": ClientDescribeAnalysisSchemesResponseAnalysisSchemesOptionsTypeDef,
        "Status": ClientDescribeAnalysisSchemesResponseAnalysisSchemesStatusTypeDef,
    },
    total=False,
)

ClientDescribeAnalysisSchemesResponseTypeDef = TypedDict(
    "ClientDescribeAnalysisSchemesResponseTypeDef",
    {"AnalysisSchemes": List[ClientDescribeAnalysisSchemesResponseAnalysisSchemesTypeDef]},
    total=False,
)

ClientDescribeAvailabilityOptionsResponseAvailabilityOptionsStatusTypeDef = TypedDict(
    "ClientDescribeAvailabilityOptionsResponseAvailabilityOptionsStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": Literal["RequiresIndexDocuments", "Processing", "Active", "FailedToValidate"],
        "PendingDeletion": bool,
    },
    total=False,
)

ClientDescribeAvailabilityOptionsResponseAvailabilityOptionsTypeDef = TypedDict(
    "ClientDescribeAvailabilityOptionsResponseAvailabilityOptionsTypeDef",
    {
        "Options": bool,
        "Status": ClientDescribeAvailabilityOptionsResponseAvailabilityOptionsStatusTypeDef,
    },
    total=False,
)

ClientDescribeAvailabilityOptionsResponseTypeDef = TypedDict(
    "ClientDescribeAvailabilityOptionsResponseTypeDef",
    {"AvailabilityOptions": ClientDescribeAvailabilityOptionsResponseAvailabilityOptionsTypeDef},
    total=False,
)

ClientDescribeDomainEndpointOptionsResponseDomainEndpointOptionsOptionsTypeDef = TypedDict(
    "ClientDescribeDomainEndpointOptionsResponseDomainEndpointOptionsOptionsTypeDef",
    {
        "EnforceHTTPS": bool,
        "TLSSecurityPolicy": Literal["Policy-Min-TLS-1-0-2019-07", "Policy-Min-TLS-1-2-2019-07"],
    },
    total=False,
)

ClientDescribeDomainEndpointOptionsResponseDomainEndpointOptionsStatusTypeDef = TypedDict(
    "ClientDescribeDomainEndpointOptionsResponseDomainEndpointOptionsStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": Literal["RequiresIndexDocuments", "Processing", "Active", "FailedToValidate"],
        "PendingDeletion": bool,
    },
    total=False,
)

ClientDescribeDomainEndpointOptionsResponseDomainEndpointOptionsTypeDef = TypedDict(
    "ClientDescribeDomainEndpointOptionsResponseDomainEndpointOptionsTypeDef",
    {
        "Options": ClientDescribeDomainEndpointOptionsResponseDomainEndpointOptionsOptionsTypeDef,
        "Status": ClientDescribeDomainEndpointOptionsResponseDomainEndpointOptionsStatusTypeDef,
    },
    total=False,
)

ClientDescribeDomainEndpointOptionsResponseTypeDef = TypedDict(
    "ClientDescribeDomainEndpointOptionsResponseTypeDef",
    {
        "DomainEndpointOptions": ClientDescribeDomainEndpointOptionsResponseDomainEndpointOptionsTypeDef
    },
    total=False,
)

ClientDescribeDomainsResponseDomainStatusListDocServiceTypeDef = TypedDict(
    "ClientDescribeDomainsResponseDomainStatusListDocServiceTypeDef", {"Endpoint": str}, total=False
)

ClientDescribeDomainsResponseDomainStatusListLimitsTypeDef = TypedDict(
    "ClientDescribeDomainsResponseDomainStatusListLimitsTypeDef",
    {"MaximumReplicationCount": int, "MaximumPartitionCount": int},
    total=False,
)

ClientDescribeDomainsResponseDomainStatusListSearchServiceTypeDef = TypedDict(
    "ClientDescribeDomainsResponseDomainStatusListSearchServiceTypeDef",
    {"Endpoint": str},
    total=False,
)

ClientDescribeDomainsResponseDomainStatusListTypeDef = TypedDict(
    "ClientDescribeDomainsResponseDomainStatusListTypeDef",
    {
        "DomainId": str,
        "DomainName": str,
        "ARN": str,
        "Created": bool,
        "Deleted": bool,
        "DocService": ClientDescribeDomainsResponseDomainStatusListDocServiceTypeDef,
        "SearchService": ClientDescribeDomainsResponseDomainStatusListSearchServiceTypeDef,
        "RequiresIndexDocuments": bool,
        "Processing": bool,
        "SearchInstanceType": str,
        "SearchPartitionCount": int,
        "SearchInstanceCount": int,
        "Limits": ClientDescribeDomainsResponseDomainStatusListLimitsTypeDef,
    },
    total=False,
)

ClientDescribeDomainsResponseTypeDef = TypedDict(
    "ClientDescribeDomainsResponseTypeDef",
    {"DomainStatusList": List[ClientDescribeDomainsResponseDomainStatusListTypeDef]},
    total=False,
)

ClientDescribeExpressionsResponseExpressionsOptionsTypeDef = TypedDict(
    "ClientDescribeExpressionsResponseExpressionsOptionsTypeDef",
    {"ExpressionName": str, "ExpressionValue": str},
    total=False,
)

ClientDescribeExpressionsResponseExpressionsStatusTypeDef = TypedDict(
    "ClientDescribeExpressionsResponseExpressionsStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": Literal["RequiresIndexDocuments", "Processing", "Active", "FailedToValidate"],
        "PendingDeletion": bool,
    },
    total=False,
)

ClientDescribeExpressionsResponseExpressionsTypeDef = TypedDict(
    "ClientDescribeExpressionsResponseExpressionsTypeDef",
    {
        "Options": ClientDescribeExpressionsResponseExpressionsOptionsTypeDef,
        "Status": ClientDescribeExpressionsResponseExpressionsStatusTypeDef,
    },
    total=False,
)

ClientDescribeExpressionsResponseTypeDef = TypedDict(
    "ClientDescribeExpressionsResponseTypeDef",
    {"Expressions": List[ClientDescribeExpressionsResponseExpressionsTypeDef]},
    total=False,
)

ClientDescribeIndexFieldsResponseIndexFieldsOptionsDateArrayOptionsTypeDef = TypedDict(
    "ClientDescribeIndexFieldsResponseIndexFieldsOptionsDateArrayOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceFields": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
    },
    total=False,
)

ClientDescribeIndexFieldsResponseIndexFieldsOptionsDateOptionsTypeDef = TypedDict(
    "ClientDescribeIndexFieldsResponseIndexFieldsOptionsDateOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceField": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
        "SortEnabled": bool,
    },
    total=False,
)

ClientDescribeIndexFieldsResponseIndexFieldsOptionsDoubleArrayOptionsTypeDef = TypedDict(
    "ClientDescribeIndexFieldsResponseIndexFieldsOptionsDoubleArrayOptionsTypeDef",
    {
        "DefaultValue": float,
        "SourceFields": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
    },
    total=False,
)

ClientDescribeIndexFieldsResponseIndexFieldsOptionsDoubleOptionsTypeDef = TypedDict(
    "ClientDescribeIndexFieldsResponseIndexFieldsOptionsDoubleOptionsTypeDef",
    {
        "DefaultValue": float,
        "SourceField": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
        "SortEnabled": bool,
    },
    total=False,
)

ClientDescribeIndexFieldsResponseIndexFieldsOptionsIntArrayOptionsTypeDef = TypedDict(
    "ClientDescribeIndexFieldsResponseIndexFieldsOptionsIntArrayOptionsTypeDef",
    {
        "DefaultValue": int,
        "SourceFields": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
    },
    total=False,
)

ClientDescribeIndexFieldsResponseIndexFieldsOptionsIntOptionsTypeDef = TypedDict(
    "ClientDescribeIndexFieldsResponseIndexFieldsOptionsIntOptionsTypeDef",
    {
        "DefaultValue": int,
        "SourceField": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
        "SortEnabled": bool,
    },
    total=False,
)

ClientDescribeIndexFieldsResponseIndexFieldsOptionsLatLonOptionsTypeDef = TypedDict(
    "ClientDescribeIndexFieldsResponseIndexFieldsOptionsLatLonOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceField": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
        "SortEnabled": bool,
    },
    total=False,
)

ClientDescribeIndexFieldsResponseIndexFieldsOptionsLiteralArrayOptionsTypeDef = TypedDict(
    "ClientDescribeIndexFieldsResponseIndexFieldsOptionsLiteralArrayOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceFields": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
    },
    total=False,
)

ClientDescribeIndexFieldsResponseIndexFieldsOptionsLiteralOptionsTypeDef = TypedDict(
    "ClientDescribeIndexFieldsResponseIndexFieldsOptionsLiteralOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceField": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
        "SortEnabled": bool,
    },
    total=False,
)

ClientDescribeIndexFieldsResponseIndexFieldsOptionsTextArrayOptionsTypeDef = TypedDict(
    "ClientDescribeIndexFieldsResponseIndexFieldsOptionsTextArrayOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceFields": str,
        "ReturnEnabled": bool,
        "HighlightEnabled": bool,
        "AnalysisScheme": str,
    },
    total=False,
)

ClientDescribeIndexFieldsResponseIndexFieldsOptionsTextOptionsTypeDef = TypedDict(
    "ClientDescribeIndexFieldsResponseIndexFieldsOptionsTextOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceField": str,
        "ReturnEnabled": bool,
        "SortEnabled": bool,
        "HighlightEnabled": bool,
        "AnalysisScheme": str,
    },
    total=False,
)

ClientDescribeIndexFieldsResponseIndexFieldsOptionsTypeDef = TypedDict(
    "ClientDescribeIndexFieldsResponseIndexFieldsOptionsTypeDef",
    {
        "IndexFieldName": str,
        "IndexFieldType": Literal[
            "int",
            "double",
            "literal",
            "text",
            "date",
            "latlon",
            "int-array",
            "double-array",
            "literal-array",
            "text-array",
            "date-array",
        ],
        "IntOptions": ClientDescribeIndexFieldsResponseIndexFieldsOptionsIntOptionsTypeDef,
        "DoubleOptions": ClientDescribeIndexFieldsResponseIndexFieldsOptionsDoubleOptionsTypeDef,
        "LiteralOptions": ClientDescribeIndexFieldsResponseIndexFieldsOptionsLiteralOptionsTypeDef,
        "TextOptions": ClientDescribeIndexFieldsResponseIndexFieldsOptionsTextOptionsTypeDef,
        "DateOptions": ClientDescribeIndexFieldsResponseIndexFieldsOptionsDateOptionsTypeDef,
        "LatLonOptions": ClientDescribeIndexFieldsResponseIndexFieldsOptionsLatLonOptionsTypeDef,
        "IntArrayOptions": ClientDescribeIndexFieldsResponseIndexFieldsOptionsIntArrayOptionsTypeDef,
        "DoubleArrayOptions": ClientDescribeIndexFieldsResponseIndexFieldsOptionsDoubleArrayOptionsTypeDef,
        "LiteralArrayOptions": ClientDescribeIndexFieldsResponseIndexFieldsOptionsLiteralArrayOptionsTypeDef,
        "TextArrayOptions": ClientDescribeIndexFieldsResponseIndexFieldsOptionsTextArrayOptionsTypeDef,
        "DateArrayOptions": ClientDescribeIndexFieldsResponseIndexFieldsOptionsDateArrayOptionsTypeDef,
    },
    total=False,
)

ClientDescribeIndexFieldsResponseIndexFieldsStatusTypeDef = TypedDict(
    "ClientDescribeIndexFieldsResponseIndexFieldsStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": Literal["RequiresIndexDocuments", "Processing", "Active", "FailedToValidate"],
        "PendingDeletion": bool,
    },
    total=False,
)

ClientDescribeIndexFieldsResponseIndexFieldsTypeDef = TypedDict(
    "ClientDescribeIndexFieldsResponseIndexFieldsTypeDef",
    {
        "Options": ClientDescribeIndexFieldsResponseIndexFieldsOptionsTypeDef,
        "Status": ClientDescribeIndexFieldsResponseIndexFieldsStatusTypeDef,
    },
    total=False,
)

ClientDescribeIndexFieldsResponseTypeDef = TypedDict(
    "ClientDescribeIndexFieldsResponseTypeDef",
    {"IndexFields": List[ClientDescribeIndexFieldsResponseIndexFieldsTypeDef]},
    total=False,
)

ClientDescribeScalingParametersResponseScalingParametersOptionsTypeDef = TypedDict(
    "ClientDescribeScalingParametersResponseScalingParametersOptionsTypeDef",
    {
        "DesiredInstanceType": Literal[
            "search.m1.small",
            "search.m1.large",
            "search.m2.xlarge",
            "search.m2.2xlarge",
            "search.m3.medium",
            "search.m3.large",
            "search.m3.xlarge",
            "search.m3.2xlarge",
        ],
        "DesiredReplicationCount": int,
        "DesiredPartitionCount": int,
    },
    total=False,
)

ClientDescribeScalingParametersResponseScalingParametersStatusTypeDef = TypedDict(
    "ClientDescribeScalingParametersResponseScalingParametersStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": Literal["RequiresIndexDocuments", "Processing", "Active", "FailedToValidate"],
        "PendingDeletion": bool,
    },
    total=False,
)

ClientDescribeScalingParametersResponseScalingParametersTypeDef = TypedDict(
    "ClientDescribeScalingParametersResponseScalingParametersTypeDef",
    {
        "Options": ClientDescribeScalingParametersResponseScalingParametersOptionsTypeDef,
        "Status": ClientDescribeScalingParametersResponseScalingParametersStatusTypeDef,
    },
    total=False,
)

ClientDescribeScalingParametersResponseTypeDef = TypedDict(
    "ClientDescribeScalingParametersResponseTypeDef",
    {"ScalingParameters": ClientDescribeScalingParametersResponseScalingParametersTypeDef},
    total=False,
)

ClientDescribeServiceAccessPoliciesResponseAccessPoliciesStatusTypeDef = TypedDict(
    "ClientDescribeServiceAccessPoliciesResponseAccessPoliciesStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": Literal["RequiresIndexDocuments", "Processing", "Active", "FailedToValidate"],
        "PendingDeletion": bool,
    },
    total=False,
)

ClientDescribeServiceAccessPoliciesResponseAccessPoliciesTypeDef = TypedDict(
    "ClientDescribeServiceAccessPoliciesResponseAccessPoliciesTypeDef",
    {
        "Options": str,
        "Status": ClientDescribeServiceAccessPoliciesResponseAccessPoliciesStatusTypeDef,
    },
    total=False,
)

ClientDescribeServiceAccessPoliciesResponseTypeDef = TypedDict(
    "ClientDescribeServiceAccessPoliciesResponseTypeDef",
    {"AccessPolicies": ClientDescribeServiceAccessPoliciesResponseAccessPoliciesTypeDef},
    total=False,
)

ClientDescribeSuggestersResponseSuggestersOptionsDocumentSuggesterOptionsTypeDef = TypedDict(
    "ClientDescribeSuggestersResponseSuggestersOptionsDocumentSuggesterOptionsTypeDef",
    {"SourceField": str, "FuzzyMatching": Literal["none", "low", "high"], "SortExpression": str},
    total=False,
)

ClientDescribeSuggestersResponseSuggestersOptionsTypeDef = TypedDict(
    "ClientDescribeSuggestersResponseSuggestersOptionsTypeDef",
    {
        "SuggesterName": str,
        "DocumentSuggesterOptions": ClientDescribeSuggestersResponseSuggestersOptionsDocumentSuggesterOptionsTypeDef,
    },
    total=False,
)

ClientDescribeSuggestersResponseSuggestersStatusTypeDef = TypedDict(
    "ClientDescribeSuggestersResponseSuggestersStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": Literal["RequiresIndexDocuments", "Processing", "Active", "FailedToValidate"],
        "PendingDeletion": bool,
    },
    total=False,
)

ClientDescribeSuggestersResponseSuggestersTypeDef = TypedDict(
    "ClientDescribeSuggestersResponseSuggestersTypeDef",
    {
        "Options": ClientDescribeSuggestersResponseSuggestersOptionsTypeDef,
        "Status": ClientDescribeSuggestersResponseSuggestersStatusTypeDef,
    },
    total=False,
)

ClientDescribeSuggestersResponseTypeDef = TypedDict(
    "ClientDescribeSuggestersResponseTypeDef",
    {"Suggesters": List[ClientDescribeSuggestersResponseSuggestersTypeDef]},
    total=False,
)

ClientIndexDocumentsResponseTypeDef = TypedDict(
    "ClientIndexDocumentsResponseTypeDef", {"FieldNames": List[str]}, total=False
)

ClientListDomainNamesResponseTypeDef = TypedDict(
    "ClientListDomainNamesResponseTypeDef", {"DomainNames": Dict[str, str]}, total=False
)

ClientUpdateAvailabilityOptionsResponseAvailabilityOptionsStatusTypeDef = TypedDict(
    "ClientUpdateAvailabilityOptionsResponseAvailabilityOptionsStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": Literal["RequiresIndexDocuments", "Processing", "Active", "FailedToValidate"],
        "PendingDeletion": bool,
    },
    total=False,
)

ClientUpdateAvailabilityOptionsResponseAvailabilityOptionsTypeDef = TypedDict(
    "ClientUpdateAvailabilityOptionsResponseAvailabilityOptionsTypeDef",
    {
        "Options": bool,
        "Status": ClientUpdateAvailabilityOptionsResponseAvailabilityOptionsStatusTypeDef,
    },
    total=False,
)

ClientUpdateAvailabilityOptionsResponseTypeDef = TypedDict(
    "ClientUpdateAvailabilityOptionsResponseTypeDef",
    {"AvailabilityOptions": ClientUpdateAvailabilityOptionsResponseAvailabilityOptionsTypeDef},
    total=False,
)

ClientUpdateDomainEndpointOptionsDomainEndpointOptionsTypeDef = TypedDict(
    "ClientUpdateDomainEndpointOptionsDomainEndpointOptionsTypeDef",
    {
        "EnforceHTTPS": bool,
        "TLSSecurityPolicy": Literal["Policy-Min-TLS-1-0-2019-07", "Policy-Min-TLS-1-2-2019-07"],
    },
    total=False,
)

ClientUpdateDomainEndpointOptionsResponseDomainEndpointOptionsOptionsTypeDef = TypedDict(
    "ClientUpdateDomainEndpointOptionsResponseDomainEndpointOptionsOptionsTypeDef",
    {
        "EnforceHTTPS": bool,
        "TLSSecurityPolicy": Literal["Policy-Min-TLS-1-0-2019-07", "Policy-Min-TLS-1-2-2019-07"],
    },
    total=False,
)

ClientUpdateDomainEndpointOptionsResponseDomainEndpointOptionsStatusTypeDef = TypedDict(
    "ClientUpdateDomainEndpointOptionsResponseDomainEndpointOptionsStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": Literal["RequiresIndexDocuments", "Processing", "Active", "FailedToValidate"],
        "PendingDeletion": bool,
    },
    total=False,
)

ClientUpdateDomainEndpointOptionsResponseDomainEndpointOptionsTypeDef = TypedDict(
    "ClientUpdateDomainEndpointOptionsResponseDomainEndpointOptionsTypeDef",
    {
        "Options": ClientUpdateDomainEndpointOptionsResponseDomainEndpointOptionsOptionsTypeDef,
        "Status": ClientUpdateDomainEndpointOptionsResponseDomainEndpointOptionsStatusTypeDef,
    },
    total=False,
)

ClientUpdateDomainEndpointOptionsResponseTypeDef = TypedDict(
    "ClientUpdateDomainEndpointOptionsResponseTypeDef",
    {
        "DomainEndpointOptions": ClientUpdateDomainEndpointOptionsResponseDomainEndpointOptionsTypeDef
    },
    total=False,
)

ClientUpdateScalingParametersResponseScalingParametersOptionsTypeDef = TypedDict(
    "ClientUpdateScalingParametersResponseScalingParametersOptionsTypeDef",
    {
        "DesiredInstanceType": Literal[
            "search.m1.small",
            "search.m1.large",
            "search.m2.xlarge",
            "search.m2.2xlarge",
            "search.m3.medium",
            "search.m3.large",
            "search.m3.xlarge",
            "search.m3.2xlarge",
        ],
        "DesiredReplicationCount": int,
        "DesiredPartitionCount": int,
    },
    total=False,
)

ClientUpdateScalingParametersResponseScalingParametersStatusTypeDef = TypedDict(
    "ClientUpdateScalingParametersResponseScalingParametersStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": Literal["RequiresIndexDocuments", "Processing", "Active", "FailedToValidate"],
        "PendingDeletion": bool,
    },
    total=False,
)

ClientUpdateScalingParametersResponseScalingParametersTypeDef = TypedDict(
    "ClientUpdateScalingParametersResponseScalingParametersTypeDef",
    {
        "Options": ClientUpdateScalingParametersResponseScalingParametersOptionsTypeDef,
        "Status": ClientUpdateScalingParametersResponseScalingParametersStatusTypeDef,
    },
    total=False,
)

ClientUpdateScalingParametersResponseTypeDef = TypedDict(
    "ClientUpdateScalingParametersResponseTypeDef",
    {"ScalingParameters": ClientUpdateScalingParametersResponseScalingParametersTypeDef},
    total=False,
)

ClientUpdateScalingParametersScalingParametersTypeDef = TypedDict(
    "ClientUpdateScalingParametersScalingParametersTypeDef",
    {
        "DesiredInstanceType": Literal[
            "search.m1.small",
            "search.m1.large",
            "search.m2.xlarge",
            "search.m2.2xlarge",
            "search.m3.medium",
            "search.m3.large",
            "search.m3.xlarge",
            "search.m3.2xlarge",
        ],
        "DesiredReplicationCount": int,
        "DesiredPartitionCount": int,
    },
    total=False,
)

ClientUpdateServiceAccessPoliciesResponseAccessPoliciesStatusTypeDef = TypedDict(
    "ClientUpdateServiceAccessPoliciesResponseAccessPoliciesStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": Literal["RequiresIndexDocuments", "Processing", "Active", "FailedToValidate"],
        "PendingDeletion": bool,
    },
    total=False,
)

ClientUpdateServiceAccessPoliciesResponseAccessPoliciesTypeDef = TypedDict(
    "ClientUpdateServiceAccessPoliciesResponseAccessPoliciesTypeDef",
    {
        "Options": str,
        "Status": ClientUpdateServiceAccessPoliciesResponseAccessPoliciesStatusTypeDef,
    },
    total=False,
)

ClientUpdateServiceAccessPoliciesResponseTypeDef = TypedDict(
    "ClientUpdateServiceAccessPoliciesResponseTypeDef",
    {"AccessPolicies": ClientUpdateServiceAccessPoliciesResponseAccessPoliciesTypeDef},
    total=False,
)
