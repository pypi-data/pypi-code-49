"""
Main interface for waf-regional service type definitions.

Usage::

    from mypy_boto3.waf_regional.type_defs import ClientCreateByteMatchSetResponseByteMatchSetByteMatchTuplesFieldToMatchTypeDef

    data: ClientCreateByteMatchSetResponseByteMatchSetByteMatchTuplesFieldToMatchTypeDef = {...}
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
    "ClientCreateByteMatchSetResponseByteMatchSetByteMatchTuplesFieldToMatchTypeDef",
    "ClientCreateByteMatchSetResponseByteMatchSetByteMatchTuplesTypeDef",
    "ClientCreateByteMatchSetResponseByteMatchSetTypeDef",
    "ClientCreateByteMatchSetResponseTypeDef",
    "ClientCreateGeoMatchSetResponseGeoMatchSetGeoMatchConstraintsTypeDef",
    "ClientCreateGeoMatchSetResponseGeoMatchSetTypeDef",
    "ClientCreateGeoMatchSetResponseTypeDef",
    "ClientCreateIpSetResponseIPSetIPSetDescriptorsTypeDef",
    "ClientCreateIpSetResponseIPSetTypeDef",
    "ClientCreateIpSetResponseTypeDef",
    "ClientCreateRateBasedRuleResponseRuleMatchPredicatesTypeDef",
    "ClientCreateRateBasedRuleResponseRuleTypeDef",
    "ClientCreateRateBasedRuleResponseTypeDef",
    "ClientCreateRateBasedRuleTagsTypeDef",
    "ClientCreateRegexMatchSetResponseRegexMatchSetRegexMatchTuplesFieldToMatchTypeDef",
    "ClientCreateRegexMatchSetResponseRegexMatchSetRegexMatchTuplesTypeDef",
    "ClientCreateRegexMatchSetResponseRegexMatchSetTypeDef",
    "ClientCreateRegexMatchSetResponseTypeDef",
    "ClientCreateRegexPatternSetResponseRegexPatternSetTypeDef",
    "ClientCreateRegexPatternSetResponseTypeDef",
    "ClientCreateRuleGroupResponseRuleGroupTypeDef",
    "ClientCreateRuleGroupResponseTypeDef",
    "ClientCreateRuleGroupTagsTypeDef",
    "ClientCreateRuleResponseRulePredicatesTypeDef",
    "ClientCreateRuleResponseRuleTypeDef",
    "ClientCreateRuleResponseTypeDef",
    "ClientCreateRuleTagsTypeDef",
    "ClientCreateSizeConstraintSetResponseSizeConstraintSetSizeConstraintsFieldToMatchTypeDef",
    "ClientCreateSizeConstraintSetResponseSizeConstraintSetSizeConstraintsTypeDef",
    "ClientCreateSizeConstraintSetResponseSizeConstraintSetTypeDef",
    "ClientCreateSizeConstraintSetResponseTypeDef",
    "ClientCreateSqlInjectionMatchSetResponseSqlInjectionMatchSetSqlInjectionMatchTuplesFieldToMatchTypeDef",
    "ClientCreateSqlInjectionMatchSetResponseSqlInjectionMatchSetSqlInjectionMatchTuplesTypeDef",
    "ClientCreateSqlInjectionMatchSetResponseSqlInjectionMatchSetTypeDef",
    "ClientCreateSqlInjectionMatchSetResponseTypeDef",
    "ClientCreateWebAclDefaultActionTypeDef",
    "ClientCreateWebAclResponseWebACLDefaultActionTypeDef",
    "ClientCreateWebAclResponseWebACLRulesActionTypeDef",
    "ClientCreateWebAclResponseWebACLRulesExcludedRulesTypeDef",
    "ClientCreateWebAclResponseWebACLRulesOverrideActionTypeDef",
    "ClientCreateWebAclResponseWebACLRulesTypeDef",
    "ClientCreateWebAclResponseWebACLTypeDef",
    "ClientCreateWebAclResponseTypeDef",
    "ClientCreateWebAclTagsTypeDef",
    "ClientCreateXssMatchSetResponseXssMatchSetXssMatchTuplesFieldToMatchTypeDef",
    "ClientCreateXssMatchSetResponseXssMatchSetXssMatchTuplesTypeDef",
    "ClientCreateXssMatchSetResponseXssMatchSetTypeDef",
    "ClientCreateXssMatchSetResponseTypeDef",
    "ClientDeleteByteMatchSetResponseTypeDef",
    "ClientDeleteGeoMatchSetResponseTypeDef",
    "ClientDeleteIpSetResponseTypeDef",
    "ClientDeleteRateBasedRuleResponseTypeDef",
    "ClientDeleteRegexMatchSetResponseTypeDef",
    "ClientDeleteRegexPatternSetResponseTypeDef",
    "ClientDeleteRuleGroupResponseTypeDef",
    "ClientDeleteRuleResponseTypeDef",
    "ClientDeleteSizeConstraintSetResponseTypeDef",
    "ClientDeleteSqlInjectionMatchSetResponseTypeDef",
    "ClientDeleteWebAclResponseTypeDef",
    "ClientDeleteXssMatchSetResponseTypeDef",
    "ClientGetByteMatchSetResponseByteMatchSetByteMatchTuplesFieldToMatchTypeDef",
    "ClientGetByteMatchSetResponseByteMatchSetByteMatchTuplesTypeDef",
    "ClientGetByteMatchSetResponseByteMatchSetTypeDef",
    "ClientGetByteMatchSetResponseTypeDef",
    "ClientGetChangeTokenResponseTypeDef",
    "ClientGetChangeTokenStatusResponseTypeDef",
    "ClientGetGeoMatchSetResponseGeoMatchSetGeoMatchConstraintsTypeDef",
    "ClientGetGeoMatchSetResponseGeoMatchSetTypeDef",
    "ClientGetGeoMatchSetResponseTypeDef",
    "ClientGetIpSetResponseIPSetIPSetDescriptorsTypeDef",
    "ClientGetIpSetResponseIPSetTypeDef",
    "ClientGetIpSetResponseTypeDef",
    "ClientGetLoggingConfigurationResponseLoggingConfigurationRedactedFieldsTypeDef",
    "ClientGetLoggingConfigurationResponseLoggingConfigurationTypeDef",
    "ClientGetLoggingConfigurationResponseTypeDef",
    "ClientGetPermissionPolicyResponseTypeDef",
    "ClientGetRateBasedRuleManagedKeysResponseTypeDef",
    "ClientGetRateBasedRuleResponseRuleMatchPredicatesTypeDef",
    "ClientGetRateBasedRuleResponseRuleTypeDef",
    "ClientGetRateBasedRuleResponseTypeDef",
    "ClientGetRegexMatchSetResponseRegexMatchSetRegexMatchTuplesFieldToMatchTypeDef",
    "ClientGetRegexMatchSetResponseRegexMatchSetRegexMatchTuplesTypeDef",
    "ClientGetRegexMatchSetResponseRegexMatchSetTypeDef",
    "ClientGetRegexMatchSetResponseTypeDef",
    "ClientGetRegexPatternSetResponseRegexPatternSetTypeDef",
    "ClientGetRegexPatternSetResponseTypeDef",
    "ClientGetRuleGroupResponseRuleGroupTypeDef",
    "ClientGetRuleGroupResponseTypeDef",
    "ClientGetRuleResponseRulePredicatesTypeDef",
    "ClientGetRuleResponseRuleTypeDef",
    "ClientGetRuleResponseTypeDef",
    "ClientGetSampledRequestsResponseSampledRequestsRequestHeadersTypeDef",
    "ClientGetSampledRequestsResponseSampledRequestsRequestTypeDef",
    "ClientGetSampledRequestsResponseSampledRequestsTypeDef",
    "ClientGetSampledRequestsResponseTimeWindowTypeDef",
    "ClientGetSampledRequestsResponseTypeDef",
    "ClientGetSampledRequestsTimeWindowTypeDef",
    "ClientGetSizeConstraintSetResponseSizeConstraintSetSizeConstraintsFieldToMatchTypeDef",
    "ClientGetSizeConstraintSetResponseSizeConstraintSetSizeConstraintsTypeDef",
    "ClientGetSizeConstraintSetResponseSizeConstraintSetTypeDef",
    "ClientGetSizeConstraintSetResponseTypeDef",
    "ClientGetSqlInjectionMatchSetResponseSqlInjectionMatchSetSqlInjectionMatchTuplesFieldToMatchTypeDef",
    "ClientGetSqlInjectionMatchSetResponseSqlInjectionMatchSetSqlInjectionMatchTuplesTypeDef",
    "ClientGetSqlInjectionMatchSetResponseSqlInjectionMatchSetTypeDef",
    "ClientGetSqlInjectionMatchSetResponseTypeDef",
    "ClientGetWebAclForResourceResponseWebACLSummaryTypeDef",
    "ClientGetWebAclForResourceResponseTypeDef",
    "ClientGetWebAclResponseWebACLDefaultActionTypeDef",
    "ClientGetWebAclResponseWebACLRulesActionTypeDef",
    "ClientGetWebAclResponseWebACLRulesExcludedRulesTypeDef",
    "ClientGetWebAclResponseWebACLRulesOverrideActionTypeDef",
    "ClientGetWebAclResponseWebACLRulesTypeDef",
    "ClientGetWebAclResponseWebACLTypeDef",
    "ClientGetWebAclResponseTypeDef",
    "ClientGetXssMatchSetResponseXssMatchSetXssMatchTuplesFieldToMatchTypeDef",
    "ClientGetXssMatchSetResponseXssMatchSetXssMatchTuplesTypeDef",
    "ClientGetXssMatchSetResponseXssMatchSetTypeDef",
    "ClientGetXssMatchSetResponseTypeDef",
    "ClientListActivatedRulesInRuleGroupResponseActivatedRulesActionTypeDef",
    "ClientListActivatedRulesInRuleGroupResponseActivatedRulesExcludedRulesTypeDef",
    "ClientListActivatedRulesInRuleGroupResponseActivatedRulesOverrideActionTypeDef",
    "ClientListActivatedRulesInRuleGroupResponseActivatedRulesTypeDef",
    "ClientListActivatedRulesInRuleGroupResponseTypeDef",
    "ClientListByteMatchSetsResponseByteMatchSetsTypeDef",
    "ClientListByteMatchSetsResponseTypeDef",
    "ClientListGeoMatchSetsResponseGeoMatchSetsTypeDef",
    "ClientListGeoMatchSetsResponseTypeDef",
    "ClientListIpSetsResponseIPSetsTypeDef",
    "ClientListIpSetsResponseTypeDef",
    "ClientListLoggingConfigurationsResponseLoggingConfigurationsRedactedFieldsTypeDef",
    "ClientListLoggingConfigurationsResponseLoggingConfigurationsTypeDef",
    "ClientListLoggingConfigurationsResponseTypeDef",
    "ClientListRateBasedRulesResponseRulesTypeDef",
    "ClientListRateBasedRulesResponseTypeDef",
    "ClientListRegexMatchSetsResponseRegexMatchSetsTypeDef",
    "ClientListRegexMatchSetsResponseTypeDef",
    "ClientListRegexPatternSetsResponseRegexPatternSetsTypeDef",
    "ClientListRegexPatternSetsResponseTypeDef",
    "ClientListResourcesForWebAclResponseTypeDef",
    "ClientListRuleGroupsResponseRuleGroupsTypeDef",
    "ClientListRuleGroupsResponseTypeDef",
    "ClientListRulesResponseRulesTypeDef",
    "ClientListRulesResponseTypeDef",
    "ClientListSizeConstraintSetsResponseSizeConstraintSetsTypeDef",
    "ClientListSizeConstraintSetsResponseTypeDef",
    "ClientListSqlInjectionMatchSetsResponseSqlInjectionMatchSetsTypeDef",
    "ClientListSqlInjectionMatchSetsResponseTypeDef",
    "ClientListSubscribedRuleGroupsResponseRuleGroupsTypeDef",
    "ClientListSubscribedRuleGroupsResponseTypeDef",
    "ClientListTagsForResourceResponseTagInfoForResourceTagListTypeDef",
    "ClientListTagsForResourceResponseTagInfoForResourceTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientListWebAclsResponseWebACLsTypeDef",
    "ClientListWebAclsResponseTypeDef",
    "ClientListXssMatchSetsResponseXssMatchSetsTypeDef",
    "ClientListXssMatchSetsResponseTypeDef",
    "ClientPutLoggingConfigurationLoggingConfigurationRedactedFieldsTypeDef",
    "ClientPutLoggingConfigurationLoggingConfigurationTypeDef",
    "ClientPutLoggingConfigurationResponseLoggingConfigurationRedactedFieldsTypeDef",
    "ClientPutLoggingConfigurationResponseLoggingConfigurationTypeDef",
    "ClientPutLoggingConfigurationResponseTypeDef",
    "ClientTagResourceTagsTypeDef",
    "ClientUpdateByteMatchSetResponseTypeDef",
    "ClientUpdateByteMatchSetUpdatesByteMatchTupleFieldToMatchTypeDef",
    "ClientUpdateByteMatchSetUpdatesByteMatchTupleTypeDef",
    "ClientUpdateByteMatchSetUpdatesTypeDef",
    "ClientUpdateGeoMatchSetResponseTypeDef",
    "ClientUpdateGeoMatchSetUpdatesGeoMatchConstraintTypeDef",
    "ClientUpdateGeoMatchSetUpdatesTypeDef",
    "ClientUpdateIpSetResponseTypeDef",
    "ClientUpdateIpSetUpdatesIPSetDescriptorTypeDef",
    "ClientUpdateIpSetUpdatesTypeDef",
    "ClientUpdateRateBasedRuleResponseTypeDef",
    "ClientUpdateRateBasedRuleUpdatesPredicateTypeDef",
    "ClientUpdateRateBasedRuleUpdatesTypeDef",
    "ClientUpdateRegexMatchSetResponseTypeDef",
    "ClientUpdateRegexMatchSetUpdatesRegexMatchTupleFieldToMatchTypeDef",
    "ClientUpdateRegexMatchSetUpdatesRegexMatchTupleTypeDef",
    "ClientUpdateRegexMatchSetUpdatesTypeDef",
    "ClientUpdateRegexPatternSetResponseTypeDef",
    "ClientUpdateRegexPatternSetUpdatesTypeDef",
    "ClientUpdateRuleGroupResponseTypeDef",
    "ClientUpdateRuleGroupUpdatesActivatedRuleActionTypeDef",
    "ClientUpdateRuleGroupUpdatesActivatedRuleExcludedRulesTypeDef",
    "ClientUpdateRuleGroupUpdatesActivatedRuleOverrideActionTypeDef",
    "ClientUpdateRuleGroupUpdatesActivatedRuleTypeDef",
    "ClientUpdateRuleGroupUpdatesTypeDef",
    "ClientUpdateRuleResponseTypeDef",
    "ClientUpdateRuleUpdatesPredicateTypeDef",
    "ClientUpdateRuleUpdatesTypeDef",
    "ClientUpdateSizeConstraintSetResponseTypeDef",
    "ClientUpdateSizeConstraintSetUpdatesSizeConstraintFieldToMatchTypeDef",
    "ClientUpdateSizeConstraintSetUpdatesSizeConstraintTypeDef",
    "ClientUpdateSizeConstraintSetUpdatesTypeDef",
    "ClientUpdateSqlInjectionMatchSetResponseTypeDef",
    "ClientUpdateSqlInjectionMatchSetUpdatesSqlInjectionMatchTupleFieldToMatchTypeDef",
    "ClientUpdateSqlInjectionMatchSetUpdatesSqlInjectionMatchTupleTypeDef",
    "ClientUpdateSqlInjectionMatchSetUpdatesTypeDef",
    "ClientUpdateWebAclDefaultActionTypeDef",
    "ClientUpdateWebAclResponseTypeDef",
    "ClientUpdateWebAclUpdatesActivatedRuleActionTypeDef",
    "ClientUpdateWebAclUpdatesActivatedRuleExcludedRulesTypeDef",
    "ClientUpdateWebAclUpdatesActivatedRuleOverrideActionTypeDef",
    "ClientUpdateWebAclUpdatesActivatedRuleTypeDef",
    "ClientUpdateWebAclUpdatesTypeDef",
    "ClientUpdateXssMatchSetResponseTypeDef",
    "ClientUpdateXssMatchSetUpdatesXssMatchTupleFieldToMatchTypeDef",
    "ClientUpdateXssMatchSetUpdatesXssMatchTupleTypeDef",
    "ClientUpdateXssMatchSetUpdatesTypeDef",
)

ClientCreateByteMatchSetResponseByteMatchSetByteMatchTuplesFieldToMatchTypeDef = TypedDict(
    "ClientCreateByteMatchSetResponseByteMatchSetByteMatchTuplesFieldToMatchTypeDef",
    {
        "Type": Literal[
            "URI", "QUERY_STRING", "HEADER", "METHOD", "BODY", "SINGLE_QUERY_ARG", "ALL_QUERY_ARGS"
        ],
        "Data": str,
    },
    total=False,
)

ClientCreateByteMatchSetResponseByteMatchSetByteMatchTuplesTypeDef = TypedDict(
    "ClientCreateByteMatchSetResponseByteMatchSetByteMatchTuplesTypeDef",
    {
        "FieldToMatch": ClientCreateByteMatchSetResponseByteMatchSetByteMatchTuplesFieldToMatchTypeDef,
        "TargetString": bytes,
        "TextTransformation": Literal[
            "NONE",
            "COMPRESS_WHITE_SPACE",
            "HTML_ENTITY_DECODE",
            "LOWERCASE",
            "CMD_LINE",
            "URL_DECODE",
        ],
        "PositionalConstraint": Literal[
            "EXACTLY", "STARTS_WITH", "ENDS_WITH", "CONTAINS", "CONTAINS_WORD"
        ],
    },
    total=False,
)

ClientCreateByteMatchSetResponseByteMatchSetTypeDef = TypedDict(
    "ClientCreateByteMatchSetResponseByteMatchSetTypeDef",
    {
        "ByteMatchSetId": str,
        "Name": str,
        "ByteMatchTuples": List[ClientCreateByteMatchSetResponseByteMatchSetByteMatchTuplesTypeDef],
    },
    total=False,
)

ClientCreateByteMatchSetResponseTypeDef = TypedDict(
    "ClientCreateByteMatchSetResponseTypeDef",
    {"ByteMatchSet": ClientCreateByteMatchSetResponseByteMatchSetTypeDef, "ChangeToken": str},
    total=False,
)

ClientCreateGeoMatchSetResponseGeoMatchSetGeoMatchConstraintsTypeDef = TypedDict(
    "ClientCreateGeoMatchSetResponseGeoMatchSetGeoMatchConstraintsTypeDef",
    {
        "Type": str,
        "Value": Literal[
            "AF",
            "AX",
            "AL",
            "DZ",
            "AS",
            "AD",
            "AO",
            "AI",
            "AQ",
            "AG",
            "AR",
            "AM",
            "AW",
            "AU",
            "AT",
            "AZ",
            "BS",
            "BH",
            "BD",
            "BB",
            "BY",
            "BE",
            "BZ",
            "BJ",
            "BM",
            "BT",
            "BO",
            "BQ",
            "BA",
            "BW",
            "BV",
            "BR",
            "IO",
            "BN",
            "BG",
            "BF",
            "BI",
            "KH",
            "CM",
            "CA",
            "CV",
            "KY",
            "CF",
            "TD",
            "CL",
            "CN",
            "CX",
            "CC",
            "CO",
            "KM",
            "CG",
            "CD",
            "CK",
            "CR",
            "CI",
            "HR",
            "CU",
            "CW",
            "CY",
            "CZ",
            "DK",
            "DJ",
            "DM",
            "DO",
            "EC",
            "EG",
            "SV",
            "GQ",
            "ER",
            "EE",
            "ET",
            "FK",
            "FO",
            "FJ",
            "FI",
            "FR",
            "GF",
            "PF",
            "TF",
            "GA",
            "GM",
            "GE",
            "DE",
            "GH",
            "GI",
            "GR",
            "GL",
            "GD",
            "GP",
            "GU",
            "GT",
            "GG",
            "GN",
            "GW",
            "GY",
            "HT",
            "HM",
            "VA",
            "HN",
            "HK",
            "HU",
            "IS",
            "IN",
            "ID",
            "IR",
            "IQ",
            "IE",
            "IM",
            "IL",
            "IT",
            "JM",
            "JP",
            "JE",
            "JO",
            "KZ",
            "KE",
            "KI",
            "KP",
            "KR",
            "KW",
            "KG",
            "LA",
            "LV",
            "LB",
            "LS",
            "LR",
            "LY",
            "LI",
            "LT",
            "LU",
            "MO",
            "MK",
            "MG",
            "MW",
            "MY",
            "MV",
            "ML",
            "MT",
            "MH",
            "MQ",
            "MR",
            "MU",
            "YT",
            "MX",
            "FM",
            "MD",
            "MC",
            "MN",
            "ME",
            "MS",
            "MA",
            "MZ",
            "MM",
            "NA",
            "NR",
            "NP",
            "NL",
            "NC",
            "NZ",
            "NI",
            "NE",
            "NG",
            "NU",
            "NF",
            "MP",
            "NO",
            "OM",
            "PK",
            "PW",
            "PS",
            "PA",
            "PG",
            "PY",
            "PE",
            "PH",
            "PN",
            "PL",
            "PT",
            "PR",
            "QA",
            "RE",
            "RO",
            "RU",
            "RW",
            "BL",
            "SH",
            "KN",
            "LC",
            "MF",
            "PM",
            "VC",
            "WS",
            "SM",
            "ST",
            "SA",
            "SN",
            "RS",
            "SC",
            "SL",
            "SG",
            "SX",
            "SK",
            "SI",
            "SB",
            "SO",
            "ZA",
            "GS",
            "SS",
            "ES",
            "LK",
            "SD",
            "SR",
            "SJ",
            "SZ",
            "SE",
            "CH",
            "SY",
            "TW",
            "TJ",
            "TZ",
            "TH",
            "TL",
            "TG",
            "TK",
            "TO",
            "TT",
            "TN",
            "TR",
            "TM",
            "TC",
            "TV",
            "UG",
            "UA",
            "AE",
            "GB",
            "US",
            "UM",
            "UY",
            "UZ",
            "VU",
            "VE",
            "VN",
            "VG",
            "VI",
            "WF",
            "EH",
            "YE",
            "ZM",
            "ZW",
        ],
    },
    total=False,
)

ClientCreateGeoMatchSetResponseGeoMatchSetTypeDef = TypedDict(
    "ClientCreateGeoMatchSetResponseGeoMatchSetTypeDef",
    {
        "GeoMatchSetId": str,
        "Name": str,
        "GeoMatchConstraints": List[
            ClientCreateGeoMatchSetResponseGeoMatchSetGeoMatchConstraintsTypeDef
        ],
    },
    total=False,
)

ClientCreateGeoMatchSetResponseTypeDef = TypedDict(
    "ClientCreateGeoMatchSetResponseTypeDef",
    {"GeoMatchSet": ClientCreateGeoMatchSetResponseGeoMatchSetTypeDef, "ChangeToken": str},
    total=False,
)

ClientCreateIpSetResponseIPSetIPSetDescriptorsTypeDef = TypedDict(
    "ClientCreateIpSetResponseIPSetIPSetDescriptorsTypeDef",
    {"Type": Literal["IPV4", "IPV6"], "Value": str},
    total=False,
)

ClientCreateIpSetResponseIPSetTypeDef = TypedDict(
    "ClientCreateIpSetResponseIPSetTypeDef",
    {
        "IPSetId": str,
        "Name": str,
        "IPSetDescriptors": List[ClientCreateIpSetResponseIPSetIPSetDescriptorsTypeDef],
    },
    total=False,
)

ClientCreateIpSetResponseTypeDef = TypedDict(
    "ClientCreateIpSetResponseTypeDef",
    {"IPSet": ClientCreateIpSetResponseIPSetTypeDef, "ChangeToken": str},
    total=False,
)

ClientCreateRateBasedRuleResponseRuleMatchPredicatesTypeDef = TypedDict(
    "ClientCreateRateBasedRuleResponseRuleMatchPredicatesTypeDef",
    {
        "Negated": bool,
        "Type": Literal[
            "IPMatch",
            "ByteMatch",
            "SqlInjectionMatch",
            "GeoMatch",
            "SizeConstraint",
            "XssMatch",
            "RegexMatch",
        ],
        "DataId": str,
    },
    total=False,
)

ClientCreateRateBasedRuleResponseRuleTypeDef = TypedDict(
    "ClientCreateRateBasedRuleResponseRuleTypeDef",
    {
        "RuleId": str,
        "Name": str,
        "MetricName": str,
        "MatchPredicates": List[ClientCreateRateBasedRuleResponseRuleMatchPredicatesTypeDef],
        "RateKey": str,
        "RateLimit": int,
    },
    total=False,
)

ClientCreateRateBasedRuleResponseTypeDef = TypedDict(
    "ClientCreateRateBasedRuleResponseTypeDef",
    {"Rule": ClientCreateRateBasedRuleResponseRuleTypeDef, "ChangeToken": str},
    total=False,
)

ClientCreateRateBasedRuleTagsTypeDef = TypedDict(
    "ClientCreateRateBasedRuleTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreateRegexMatchSetResponseRegexMatchSetRegexMatchTuplesFieldToMatchTypeDef = TypedDict(
    "ClientCreateRegexMatchSetResponseRegexMatchSetRegexMatchTuplesFieldToMatchTypeDef",
    {
        "Type": Literal[
            "URI", "QUERY_STRING", "HEADER", "METHOD", "BODY", "SINGLE_QUERY_ARG", "ALL_QUERY_ARGS"
        ],
        "Data": str,
    },
    total=False,
)

ClientCreateRegexMatchSetResponseRegexMatchSetRegexMatchTuplesTypeDef = TypedDict(
    "ClientCreateRegexMatchSetResponseRegexMatchSetRegexMatchTuplesTypeDef",
    {
        "FieldToMatch": ClientCreateRegexMatchSetResponseRegexMatchSetRegexMatchTuplesFieldToMatchTypeDef,
        "TextTransformation": Literal[
            "NONE",
            "COMPRESS_WHITE_SPACE",
            "HTML_ENTITY_DECODE",
            "LOWERCASE",
            "CMD_LINE",
            "URL_DECODE",
        ],
        "RegexPatternSetId": str,
    },
    total=False,
)

ClientCreateRegexMatchSetResponseRegexMatchSetTypeDef = TypedDict(
    "ClientCreateRegexMatchSetResponseRegexMatchSetTypeDef",
    {
        "RegexMatchSetId": str,
        "Name": str,
        "RegexMatchTuples": List[
            ClientCreateRegexMatchSetResponseRegexMatchSetRegexMatchTuplesTypeDef
        ],
    },
    total=False,
)

ClientCreateRegexMatchSetResponseTypeDef = TypedDict(
    "ClientCreateRegexMatchSetResponseTypeDef",
    {"RegexMatchSet": ClientCreateRegexMatchSetResponseRegexMatchSetTypeDef, "ChangeToken": str},
    total=False,
)

ClientCreateRegexPatternSetResponseRegexPatternSetTypeDef = TypedDict(
    "ClientCreateRegexPatternSetResponseRegexPatternSetTypeDef",
    {"RegexPatternSetId": str, "Name": str, "RegexPatternStrings": List[str]},
    total=False,
)

ClientCreateRegexPatternSetResponseTypeDef = TypedDict(
    "ClientCreateRegexPatternSetResponseTypeDef",
    {
        "RegexPatternSet": ClientCreateRegexPatternSetResponseRegexPatternSetTypeDef,
        "ChangeToken": str,
    },
    total=False,
)

ClientCreateRuleGroupResponseRuleGroupTypeDef = TypedDict(
    "ClientCreateRuleGroupResponseRuleGroupTypeDef",
    {"RuleGroupId": str, "Name": str, "MetricName": str},
    total=False,
)

ClientCreateRuleGroupResponseTypeDef = TypedDict(
    "ClientCreateRuleGroupResponseTypeDef",
    {"RuleGroup": ClientCreateRuleGroupResponseRuleGroupTypeDef, "ChangeToken": str},
    total=False,
)

ClientCreateRuleGroupTagsTypeDef = TypedDict(
    "ClientCreateRuleGroupTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreateRuleResponseRulePredicatesTypeDef = TypedDict(
    "ClientCreateRuleResponseRulePredicatesTypeDef",
    {
        "Negated": bool,
        "Type": Literal[
            "IPMatch",
            "ByteMatch",
            "SqlInjectionMatch",
            "GeoMatch",
            "SizeConstraint",
            "XssMatch",
            "RegexMatch",
        ],
        "DataId": str,
    },
    total=False,
)

ClientCreateRuleResponseRuleTypeDef = TypedDict(
    "ClientCreateRuleResponseRuleTypeDef",
    {
        "RuleId": str,
        "Name": str,
        "MetricName": str,
        "Predicates": List[ClientCreateRuleResponseRulePredicatesTypeDef],
    },
    total=False,
)

ClientCreateRuleResponseTypeDef = TypedDict(
    "ClientCreateRuleResponseTypeDef",
    {"Rule": ClientCreateRuleResponseRuleTypeDef, "ChangeToken": str},
    total=False,
)

ClientCreateRuleTagsTypeDef = TypedDict(
    "ClientCreateRuleTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreateSizeConstraintSetResponseSizeConstraintSetSizeConstraintsFieldToMatchTypeDef = TypedDict(
    "ClientCreateSizeConstraintSetResponseSizeConstraintSetSizeConstraintsFieldToMatchTypeDef",
    {
        "Type": Literal[
            "URI", "QUERY_STRING", "HEADER", "METHOD", "BODY", "SINGLE_QUERY_ARG", "ALL_QUERY_ARGS"
        ],
        "Data": str,
    },
    total=False,
)

ClientCreateSizeConstraintSetResponseSizeConstraintSetSizeConstraintsTypeDef = TypedDict(
    "ClientCreateSizeConstraintSetResponseSizeConstraintSetSizeConstraintsTypeDef",
    {
        "FieldToMatch": ClientCreateSizeConstraintSetResponseSizeConstraintSetSizeConstraintsFieldToMatchTypeDef,
        "TextTransformation": Literal[
            "NONE",
            "COMPRESS_WHITE_SPACE",
            "HTML_ENTITY_DECODE",
            "LOWERCASE",
            "CMD_LINE",
            "URL_DECODE",
        ],
        "ComparisonOperator": Literal["EQ", "NE", "LE", "LT", "GE", "GT"],
        "Size": int,
    },
    total=False,
)

ClientCreateSizeConstraintSetResponseSizeConstraintSetTypeDef = TypedDict(
    "ClientCreateSizeConstraintSetResponseSizeConstraintSetTypeDef",
    {
        "SizeConstraintSetId": str,
        "Name": str,
        "SizeConstraints": List[
            ClientCreateSizeConstraintSetResponseSizeConstraintSetSizeConstraintsTypeDef
        ],
    },
    total=False,
)

ClientCreateSizeConstraintSetResponseTypeDef = TypedDict(
    "ClientCreateSizeConstraintSetResponseTypeDef",
    {
        "SizeConstraintSet": ClientCreateSizeConstraintSetResponseSizeConstraintSetTypeDef,
        "ChangeToken": str,
    },
    total=False,
)

ClientCreateSqlInjectionMatchSetResponseSqlInjectionMatchSetSqlInjectionMatchTuplesFieldToMatchTypeDef = TypedDict(
    "ClientCreateSqlInjectionMatchSetResponseSqlInjectionMatchSetSqlInjectionMatchTuplesFieldToMatchTypeDef",
    {
        "Type": Literal[
            "URI", "QUERY_STRING", "HEADER", "METHOD", "BODY", "SINGLE_QUERY_ARG", "ALL_QUERY_ARGS"
        ],
        "Data": str,
    },
    total=False,
)

ClientCreateSqlInjectionMatchSetResponseSqlInjectionMatchSetSqlInjectionMatchTuplesTypeDef = TypedDict(
    "ClientCreateSqlInjectionMatchSetResponseSqlInjectionMatchSetSqlInjectionMatchTuplesTypeDef",
    {
        "FieldToMatch": ClientCreateSqlInjectionMatchSetResponseSqlInjectionMatchSetSqlInjectionMatchTuplesFieldToMatchTypeDef,
        "TextTransformation": Literal[
            "NONE",
            "COMPRESS_WHITE_SPACE",
            "HTML_ENTITY_DECODE",
            "LOWERCASE",
            "CMD_LINE",
            "URL_DECODE",
        ],
    },
    total=False,
)

ClientCreateSqlInjectionMatchSetResponseSqlInjectionMatchSetTypeDef = TypedDict(
    "ClientCreateSqlInjectionMatchSetResponseSqlInjectionMatchSetTypeDef",
    {
        "SqlInjectionMatchSetId": str,
        "Name": str,
        "SqlInjectionMatchTuples": List[
            ClientCreateSqlInjectionMatchSetResponseSqlInjectionMatchSetSqlInjectionMatchTuplesTypeDef
        ],
    },
    total=False,
)

ClientCreateSqlInjectionMatchSetResponseTypeDef = TypedDict(
    "ClientCreateSqlInjectionMatchSetResponseTypeDef",
    {
        "SqlInjectionMatchSet": ClientCreateSqlInjectionMatchSetResponseSqlInjectionMatchSetTypeDef,
        "ChangeToken": str,
    },
    total=False,
)

ClientCreateWebAclDefaultActionTypeDef = TypedDict(
    "ClientCreateWebAclDefaultActionTypeDef", {"Type": Literal["BLOCK", "ALLOW", "COUNT"]}
)

ClientCreateWebAclResponseWebACLDefaultActionTypeDef = TypedDict(
    "ClientCreateWebAclResponseWebACLDefaultActionTypeDef",
    {"Type": Literal["BLOCK", "ALLOW", "COUNT"]},
    total=False,
)

ClientCreateWebAclResponseWebACLRulesActionTypeDef = TypedDict(
    "ClientCreateWebAclResponseWebACLRulesActionTypeDef",
    {"Type": Literal["BLOCK", "ALLOW", "COUNT"]},
    total=False,
)

ClientCreateWebAclResponseWebACLRulesExcludedRulesTypeDef = TypedDict(
    "ClientCreateWebAclResponseWebACLRulesExcludedRulesTypeDef", {"RuleId": str}, total=False
)

ClientCreateWebAclResponseWebACLRulesOverrideActionTypeDef = TypedDict(
    "ClientCreateWebAclResponseWebACLRulesOverrideActionTypeDef",
    {"Type": Literal["NONE", "COUNT"]},
    total=False,
)

ClientCreateWebAclResponseWebACLRulesTypeDef = TypedDict(
    "ClientCreateWebAclResponseWebACLRulesTypeDef",
    {
        "Priority": int,
        "RuleId": str,
        "Action": ClientCreateWebAclResponseWebACLRulesActionTypeDef,
        "OverrideAction": ClientCreateWebAclResponseWebACLRulesOverrideActionTypeDef,
        "Type": Literal["REGULAR", "RATE_BASED", "GROUP"],
        "ExcludedRules": List[ClientCreateWebAclResponseWebACLRulesExcludedRulesTypeDef],
    },
    total=False,
)

ClientCreateWebAclResponseWebACLTypeDef = TypedDict(
    "ClientCreateWebAclResponseWebACLTypeDef",
    {
        "WebACLId": str,
        "Name": str,
        "MetricName": str,
        "DefaultAction": ClientCreateWebAclResponseWebACLDefaultActionTypeDef,
        "Rules": List[ClientCreateWebAclResponseWebACLRulesTypeDef],
        "WebACLArn": str,
    },
    total=False,
)

ClientCreateWebAclResponseTypeDef = TypedDict(
    "ClientCreateWebAclResponseTypeDef",
    {"WebACL": ClientCreateWebAclResponseWebACLTypeDef, "ChangeToken": str},
    total=False,
)

ClientCreateWebAclTagsTypeDef = TypedDict(
    "ClientCreateWebAclTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreateXssMatchSetResponseXssMatchSetXssMatchTuplesFieldToMatchTypeDef = TypedDict(
    "ClientCreateXssMatchSetResponseXssMatchSetXssMatchTuplesFieldToMatchTypeDef",
    {
        "Type": Literal[
            "URI", "QUERY_STRING", "HEADER", "METHOD", "BODY", "SINGLE_QUERY_ARG", "ALL_QUERY_ARGS"
        ],
        "Data": str,
    },
    total=False,
)

ClientCreateXssMatchSetResponseXssMatchSetXssMatchTuplesTypeDef = TypedDict(
    "ClientCreateXssMatchSetResponseXssMatchSetXssMatchTuplesTypeDef",
    {
        "FieldToMatch": ClientCreateXssMatchSetResponseXssMatchSetXssMatchTuplesFieldToMatchTypeDef,
        "TextTransformation": Literal[
            "NONE",
            "COMPRESS_WHITE_SPACE",
            "HTML_ENTITY_DECODE",
            "LOWERCASE",
            "CMD_LINE",
            "URL_DECODE",
        ],
    },
    total=False,
)

ClientCreateXssMatchSetResponseXssMatchSetTypeDef = TypedDict(
    "ClientCreateXssMatchSetResponseXssMatchSetTypeDef",
    {
        "XssMatchSetId": str,
        "Name": str,
        "XssMatchTuples": List[ClientCreateXssMatchSetResponseXssMatchSetXssMatchTuplesTypeDef],
    },
    total=False,
)

ClientCreateXssMatchSetResponseTypeDef = TypedDict(
    "ClientCreateXssMatchSetResponseTypeDef",
    {"XssMatchSet": ClientCreateXssMatchSetResponseXssMatchSetTypeDef, "ChangeToken": str},
    total=False,
)

ClientDeleteByteMatchSetResponseTypeDef = TypedDict(
    "ClientDeleteByteMatchSetResponseTypeDef", {"ChangeToken": str}, total=False
)

ClientDeleteGeoMatchSetResponseTypeDef = TypedDict(
    "ClientDeleteGeoMatchSetResponseTypeDef", {"ChangeToken": str}, total=False
)

ClientDeleteIpSetResponseTypeDef = TypedDict(
    "ClientDeleteIpSetResponseTypeDef", {"ChangeToken": str}, total=False
)

ClientDeleteRateBasedRuleResponseTypeDef = TypedDict(
    "ClientDeleteRateBasedRuleResponseTypeDef", {"ChangeToken": str}, total=False
)

ClientDeleteRegexMatchSetResponseTypeDef = TypedDict(
    "ClientDeleteRegexMatchSetResponseTypeDef", {"ChangeToken": str}, total=False
)

ClientDeleteRegexPatternSetResponseTypeDef = TypedDict(
    "ClientDeleteRegexPatternSetResponseTypeDef", {"ChangeToken": str}, total=False
)

ClientDeleteRuleGroupResponseTypeDef = TypedDict(
    "ClientDeleteRuleGroupResponseTypeDef", {"ChangeToken": str}, total=False
)

ClientDeleteRuleResponseTypeDef = TypedDict(
    "ClientDeleteRuleResponseTypeDef", {"ChangeToken": str}, total=False
)

ClientDeleteSizeConstraintSetResponseTypeDef = TypedDict(
    "ClientDeleteSizeConstraintSetResponseTypeDef", {"ChangeToken": str}, total=False
)

ClientDeleteSqlInjectionMatchSetResponseTypeDef = TypedDict(
    "ClientDeleteSqlInjectionMatchSetResponseTypeDef", {"ChangeToken": str}, total=False
)

ClientDeleteWebAclResponseTypeDef = TypedDict(
    "ClientDeleteWebAclResponseTypeDef", {"ChangeToken": str}, total=False
)

ClientDeleteXssMatchSetResponseTypeDef = TypedDict(
    "ClientDeleteXssMatchSetResponseTypeDef", {"ChangeToken": str}, total=False
)

ClientGetByteMatchSetResponseByteMatchSetByteMatchTuplesFieldToMatchTypeDef = TypedDict(
    "ClientGetByteMatchSetResponseByteMatchSetByteMatchTuplesFieldToMatchTypeDef",
    {
        "Type": Literal[
            "URI", "QUERY_STRING", "HEADER", "METHOD", "BODY", "SINGLE_QUERY_ARG", "ALL_QUERY_ARGS"
        ],
        "Data": str,
    },
    total=False,
)

ClientGetByteMatchSetResponseByteMatchSetByteMatchTuplesTypeDef = TypedDict(
    "ClientGetByteMatchSetResponseByteMatchSetByteMatchTuplesTypeDef",
    {
        "FieldToMatch": ClientGetByteMatchSetResponseByteMatchSetByteMatchTuplesFieldToMatchTypeDef,
        "TargetString": bytes,
        "TextTransformation": Literal[
            "NONE",
            "COMPRESS_WHITE_SPACE",
            "HTML_ENTITY_DECODE",
            "LOWERCASE",
            "CMD_LINE",
            "URL_DECODE",
        ],
        "PositionalConstraint": Literal[
            "EXACTLY", "STARTS_WITH", "ENDS_WITH", "CONTAINS", "CONTAINS_WORD"
        ],
    },
    total=False,
)

ClientGetByteMatchSetResponseByteMatchSetTypeDef = TypedDict(
    "ClientGetByteMatchSetResponseByteMatchSetTypeDef",
    {
        "ByteMatchSetId": str,
        "Name": str,
        "ByteMatchTuples": List[ClientGetByteMatchSetResponseByteMatchSetByteMatchTuplesTypeDef],
    },
    total=False,
)

ClientGetByteMatchSetResponseTypeDef = TypedDict(
    "ClientGetByteMatchSetResponseTypeDef",
    {"ByteMatchSet": ClientGetByteMatchSetResponseByteMatchSetTypeDef},
    total=False,
)

ClientGetChangeTokenResponseTypeDef = TypedDict(
    "ClientGetChangeTokenResponseTypeDef", {"ChangeToken": str}, total=False
)

ClientGetChangeTokenStatusResponseTypeDef = TypedDict(
    "ClientGetChangeTokenStatusResponseTypeDef",
    {"ChangeTokenStatus": Literal["PROVISIONED", "PENDING", "INSYNC"]},
    total=False,
)

ClientGetGeoMatchSetResponseGeoMatchSetGeoMatchConstraintsTypeDef = TypedDict(
    "ClientGetGeoMatchSetResponseGeoMatchSetGeoMatchConstraintsTypeDef",
    {
        "Type": str,
        "Value": Literal[
            "AF",
            "AX",
            "AL",
            "DZ",
            "AS",
            "AD",
            "AO",
            "AI",
            "AQ",
            "AG",
            "AR",
            "AM",
            "AW",
            "AU",
            "AT",
            "AZ",
            "BS",
            "BH",
            "BD",
            "BB",
            "BY",
            "BE",
            "BZ",
            "BJ",
            "BM",
            "BT",
            "BO",
            "BQ",
            "BA",
            "BW",
            "BV",
            "BR",
            "IO",
            "BN",
            "BG",
            "BF",
            "BI",
            "KH",
            "CM",
            "CA",
            "CV",
            "KY",
            "CF",
            "TD",
            "CL",
            "CN",
            "CX",
            "CC",
            "CO",
            "KM",
            "CG",
            "CD",
            "CK",
            "CR",
            "CI",
            "HR",
            "CU",
            "CW",
            "CY",
            "CZ",
            "DK",
            "DJ",
            "DM",
            "DO",
            "EC",
            "EG",
            "SV",
            "GQ",
            "ER",
            "EE",
            "ET",
            "FK",
            "FO",
            "FJ",
            "FI",
            "FR",
            "GF",
            "PF",
            "TF",
            "GA",
            "GM",
            "GE",
            "DE",
            "GH",
            "GI",
            "GR",
            "GL",
            "GD",
            "GP",
            "GU",
            "GT",
            "GG",
            "GN",
            "GW",
            "GY",
            "HT",
            "HM",
            "VA",
            "HN",
            "HK",
            "HU",
            "IS",
            "IN",
            "ID",
            "IR",
            "IQ",
            "IE",
            "IM",
            "IL",
            "IT",
            "JM",
            "JP",
            "JE",
            "JO",
            "KZ",
            "KE",
            "KI",
            "KP",
            "KR",
            "KW",
            "KG",
            "LA",
            "LV",
            "LB",
            "LS",
            "LR",
            "LY",
            "LI",
            "LT",
            "LU",
            "MO",
            "MK",
            "MG",
            "MW",
            "MY",
            "MV",
            "ML",
            "MT",
            "MH",
            "MQ",
            "MR",
            "MU",
            "YT",
            "MX",
            "FM",
            "MD",
            "MC",
            "MN",
            "ME",
            "MS",
            "MA",
            "MZ",
            "MM",
            "NA",
            "NR",
            "NP",
            "NL",
            "NC",
            "NZ",
            "NI",
            "NE",
            "NG",
            "NU",
            "NF",
            "MP",
            "NO",
            "OM",
            "PK",
            "PW",
            "PS",
            "PA",
            "PG",
            "PY",
            "PE",
            "PH",
            "PN",
            "PL",
            "PT",
            "PR",
            "QA",
            "RE",
            "RO",
            "RU",
            "RW",
            "BL",
            "SH",
            "KN",
            "LC",
            "MF",
            "PM",
            "VC",
            "WS",
            "SM",
            "ST",
            "SA",
            "SN",
            "RS",
            "SC",
            "SL",
            "SG",
            "SX",
            "SK",
            "SI",
            "SB",
            "SO",
            "ZA",
            "GS",
            "SS",
            "ES",
            "LK",
            "SD",
            "SR",
            "SJ",
            "SZ",
            "SE",
            "CH",
            "SY",
            "TW",
            "TJ",
            "TZ",
            "TH",
            "TL",
            "TG",
            "TK",
            "TO",
            "TT",
            "TN",
            "TR",
            "TM",
            "TC",
            "TV",
            "UG",
            "UA",
            "AE",
            "GB",
            "US",
            "UM",
            "UY",
            "UZ",
            "VU",
            "VE",
            "VN",
            "VG",
            "VI",
            "WF",
            "EH",
            "YE",
            "ZM",
            "ZW",
        ],
    },
    total=False,
)

ClientGetGeoMatchSetResponseGeoMatchSetTypeDef = TypedDict(
    "ClientGetGeoMatchSetResponseGeoMatchSetTypeDef",
    {
        "GeoMatchSetId": str,
        "Name": str,
        "GeoMatchConstraints": List[
            ClientGetGeoMatchSetResponseGeoMatchSetGeoMatchConstraintsTypeDef
        ],
    },
    total=False,
)

ClientGetGeoMatchSetResponseTypeDef = TypedDict(
    "ClientGetGeoMatchSetResponseTypeDef",
    {"GeoMatchSet": ClientGetGeoMatchSetResponseGeoMatchSetTypeDef},
    total=False,
)

ClientGetIpSetResponseIPSetIPSetDescriptorsTypeDef = TypedDict(
    "ClientGetIpSetResponseIPSetIPSetDescriptorsTypeDef",
    {"Type": Literal["IPV4", "IPV6"], "Value": str},
    total=False,
)

ClientGetIpSetResponseIPSetTypeDef = TypedDict(
    "ClientGetIpSetResponseIPSetTypeDef",
    {
        "IPSetId": str,
        "Name": str,
        "IPSetDescriptors": List[ClientGetIpSetResponseIPSetIPSetDescriptorsTypeDef],
    },
    total=False,
)

ClientGetIpSetResponseTypeDef = TypedDict(
    "ClientGetIpSetResponseTypeDef", {"IPSet": ClientGetIpSetResponseIPSetTypeDef}, total=False
)

ClientGetLoggingConfigurationResponseLoggingConfigurationRedactedFieldsTypeDef = TypedDict(
    "ClientGetLoggingConfigurationResponseLoggingConfigurationRedactedFieldsTypeDef",
    {
        "Type": Literal[
            "URI", "QUERY_STRING", "HEADER", "METHOD", "BODY", "SINGLE_QUERY_ARG", "ALL_QUERY_ARGS"
        ],
        "Data": str,
    },
    total=False,
)

ClientGetLoggingConfigurationResponseLoggingConfigurationTypeDef = TypedDict(
    "ClientGetLoggingConfigurationResponseLoggingConfigurationTypeDef",
    {
        "ResourceArn": str,
        "LogDestinationConfigs": List[str],
        "RedactedFields": List[
            ClientGetLoggingConfigurationResponseLoggingConfigurationRedactedFieldsTypeDef
        ],
    },
    total=False,
)

ClientGetLoggingConfigurationResponseTypeDef = TypedDict(
    "ClientGetLoggingConfigurationResponseTypeDef",
    {"LoggingConfiguration": ClientGetLoggingConfigurationResponseLoggingConfigurationTypeDef},
    total=False,
)

ClientGetPermissionPolicyResponseTypeDef = TypedDict(
    "ClientGetPermissionPolicyResponseTypeDef", {"Policy": str}, total=False
)

ClientGetRateBasedRuleManagedKeysResponseTypeDef = TypedDict(
    "ClientGetRateBasedRuleManagedKeysResponseTypeDef",
    {"ManagedKeys": List[str], "NextMarker": str},
    total=False,
)

ClientGetRateBasedRuleResponseRuleMatchPredicatesTypeDef = TypedDict(
    "ClientGetRateBasedRuleResponseRuleMatchPredicatesTypeDef",
    {
        "Negated": bool,
        "Type": Literal[
            "IPMatch",
            "ByteMatch",
            "SqlInjectionMatch",
            "GeoMatch",
            "SizeConstraint",
            "XssMatch",
            "RegexMatch",
        ],
        "DataId": str,
    },
    total=False,
)

ClientGetRateBasedRuleResponseRuleTypeDef = TypedDict(
    "ClientGetRateBasedRuleResponseRuleTypeDef",
    {
        "RuleId": str,
        "Name": str,
        "MetricName": str,
        "MatchPredicates": List[ClientGetRateBasedRuleResponseRuleMatchPredicatesTypeDef],
        "RateKey": str,
        "RateLimit": int,
    },
    total=False,
)

ClientGetRateBasedRuleResponseTypeDef = TypedDict(
    "ClientGetRateBasedRuleResponseTypeDef",
    {"Rule": ClientGetRateBasedRuleResponseRuleTypeDef},
    total=False,
)

ClientGetRegexMatchSetResponseRegexMatchSetRegexMatchTuplesFieldToMatchTypeDef = TypedDict(
    "ClientGetRegexMatchSetResponseRegexMatchSetRegexMatchTuplesFieldToMatchTypeDef",
    {
        "Type": Literal[
            "URI", "QUERY_STRING", "HEADER", "METHOD", "BODY", "SINGLE_QUERY_ARG", "ALL_QUERY_ARGS"
        ],
        "Data": str,
    },
    total=False,
)

ClientGetRegexMatchSetResponseRegexMatchSetRegexMatchTuplesTypeDef = TypedDict(
    "ClientGetRegexMatchSetResponseRegexMatchSetRegexMatchTuplesTypeDef",
    {
        "FieldToMatch": ClientGetRegexMatchSetResponseRegexMatchSetRegexMatchTuplesFieldToMatchTypeDef,
        "TextTransformation": Literal[
            "NONE",
            "COMPRESS_WHITE_SPACE",
            "HTML_ENTITY_DECODE",
            "LOWERCASE",
            "CMD_LINE",
            "URL_DECODE",
        ],
        "RegexPatternSetId": str,
    },
    total=False,
)

ClientGetRegexMatchSetResponseRegexMatchSetTypeDef = TypedDict(
    "ClientGetRegexMatchSetResponseRegexMatchSetTypeDef",
    {
        "RegexMatchSetId": str,
        "Name": str,
        "RegexMatchTuples": List[
            ClientGetRegexMatchSetResponseRegexMatchSetRegexMatchTuplesTypeDef
        ],
    },
    total=False,
)

ClientGetRegexMatchSetResponseTypeDef = TypedDict(
    "ClientGetRegexMatchSetResponseTypeDef",
    {"RegexMatchSet": ClientGetRegexMatchSetResponseRegexMatchSetTypeDef},
    total=False,
)

ClientGetRegexPatternSetResponseRegexPatternSetTypeDef = TypedDict(
    "ClientGetRegexPatternSetResponseRegexPatternSetTypeDef",
    {"RegexPatternSetId": str, "Name": str, "RegexPatternStrings": List[str]},
    total=False,
)

ClientGetRegexPatternSetResponseTypeDef = TypedDict(
    "ClientGetRegexPatternSetResponseTypeDef",
    {"RegexPatternSet": ClientGetRegexPatternSetResponseRegexPatternSetTypeDef},
    total=False,
)

ClientGetRuleGroupResponseRuleGroupTypeDef = TypedDict(
    "ClientGetRuleGroupResponseRuleGroupTypeDef",
    {"RuleGroupId": str, "Name": str, "MetricName": str},
    total=False,
)

ClientGetRuleGroupResponseTypeDef = TypedDict(
    "ClientGetRuleGroupResponseTypeDef",
    {"RuleGroup": ClientGetRuleGroupResponseRuleGroupTypeDef},
    total=False,
)

ClientGetRuleResponseRulePredicatesTypeDef = TypedDict(
    "ClientGetRuleResponseRulePredicatesTypeDef",
    {
        "Negated": bool,
        "Type": Literal[
            "IPMatch",
            "ByteMatch",
            "SqlInjectionMatch",
            "GeoMatch",
            "SizeConstraint",
            "XssMatch",
            "RegexMatch",
        ],
        "DataId": str,
    },
    total=False,
)

ClientGetRuleResponseRuleTypeDef = TypedDict(
    "ClientGetRuleResponseRuleTypeDef",
    {
        "RuleId": str,
        "Name": str,
        "MetricName": str,
        "Predicates": List[ClientGetRuleResponseRulePredicatesTypeDef],
    },
    total=False,
)

ClientGetRuleResponseTypeDef = TypedDict(
    "ClientGetRuleResponseTypeDef", {"Rule": ClientGetRuleResponseRuleTypeDef}, total=False
)

ClientGetSampledRequestsResponseSampledRequestsRequestHeadersTypeDef = TypedDict(
    "ClientGetSampledRequestsResponseSampledRequestsRequestHeadersTypeDef",
    {"Name": str, "Value": str},
    total=False,
)

ClientGetSampledRequestsResponseSampledRequestsRequestTypeDef = TypedDict(
    "ClientGetSampledRequestsResponseSampledRequestsRequestTypeDef",
    {
        "ClientIP": str,
        "Country": str,
        "URI": str,
        "Method": str,
        "HTTPVersion": str,
        "Headers": List[ClientGetSampledRequestsResponseSampledRequestsRequestHeadersTypeDef],
    },
    total=False,
)

ClientGetSampledRequestsResponseSampledRequestsTypeDef = TypedDict(
    "ClientGetSampledRequestsResponseSampledRequestsTypeDef",
    {
        "Request": ClientGetSampledRequestsResponseSampledRequestsRequestTypeDef,
        "Weight": int,
        "Timestamp": datetime,
        "Action": str,
        "RuleWithinRuleGroup": str,
    },
    total=False,
)

ClientGetSampledRequestsResponseTimeWindowTypeDef = TypedDict(
    "ClientGetSampledRequestsResponseTimeWindowTypeDef",
    {"StartTime": datetime, "EndTime": datetime},
    total=False,
)

ClientGetSampledRequestsResponseTypeDef = TypedDict(
    "ClientGetSampledRequestsResponseTypeDef",
    {
        "SampledRequests": List[ClientGetSampledRequestsResponseSampledRequestsTypeDef],
        "PopulationSize": int,
        "TimeWindow": ClientGetSampledRequestsResponseTimeWindowTypeDef,
    },
    total=False,
)

_RequiredClientGetSampledRequestsTimeWindowTypeDef = TypedDict(
    "_RequiredClientGetSampledRequestsTimeWindowTypeDef", {"StartTime": datetime}
)
_OptionalClientGetSampledRequestsTimeWindowTypeDef = TypedDict(
    "_OptionalClientGetSampledRequestsTimeWindowTypeDef", {"EndTime": datetime}, total=False
)


class ClientGetSampledRequestsTimeWindowTypeDef(
    _RequiredClientGetSampledRequestsTimeWindowTypeDef,
    _OptionalClientGetSampledRequestsTimeWindowTypeDef,
):
    pass


ClientGetSizeConstraintSetResponseSizeConstraintSetSizeConstraintsFieldToMatchTypeDef = TypedDict(
    "ClientGetSizeConstraintSetResponseSizeConstraintSetSizeConstraintsFieldToMatchTypeDef",
    {
        "Type": Literal[
            "URI", "QUERY_STRING", "HEADER", "METHOD", "BODY", "SINGLE_QUERY_ARG", "ALL_QUERY_ARGS"
        ],
        "Data": str,
    },
    total=False,
)

ClientGetSizeConstraintSetResponseSizeConstraintSetSizeConstraintsTypeDef = TypedDict(
    "ClientGetSizeConstraintSetResponseSizeConstraintSetSizeConstraintsTypeDef",
    {
        "FieldToMatch": ClientGetSizeConstraintSetResponseSizeConstraintSetSizeConstraintsFieldToMatchTypeDef,
        "TextTransformation": Literal[
            "NONE",
            "COMPRESS_WHITE_SPACE",
            "HTML_ENTITY_DECODE",
            "LOWERCASE",
            "CMD_LINE",
            "URL_DECODE",
        ],
        "ComparisonOperator": Literal["EQ", "NE", "LE", "LT", "GE", "GT"],
        "Size": int,
    },
    total=False,
)

ClientGetSizeConstraintSetResponseSizeConstraintSetTypeDef = TypedDict(
    "ClientGetSizeConstraintSetResponseSizeConstraintSetTypeDef",
    {
        "SizeConstraintSetId": str,
        "Name": str,
        "SizeConstraints": List[
            ClientGetSizeConstraintSetResponseSizeConstraintSetSizeConstraintsTypeDef
        ],
    },
    total=False,
)

ClientGetSizeConstraintSetResponseTypeDef = TypedDict(
    "ClientGetSizeConstraintSetResponseTypeDef",
    {"SizeConstraintSet": ClientGetSizeConstraintSetResponseSizeConstraintSetTypeDef},
    total=False,
)

ClientGetSqlInjectionMatchSetResponseSqlInjectionMatchSetSqlInjectionMatchTuplesFieldToMatchTypeDef = TypedDict(
    "ClientGetSqlInjectionMatchSetResponseSqlInjectionMatchSetSqlInjectionMatchTuplesFieldToMatchTypeDef",
    {
        "Type": Literal[
            "URI", "QUERY_STRING", "HEADER", "METHOD", "BODY", "SINGLE_QUERY_ARG", "ALL_QUERY_ARGS"
        ],
        "Data": str,
    },
    total=False,
)

ClientGetSqlInjectionMatchSetResponseSqlInjectionMatchSetSqlInjectionMatchTuplesTypeDef = TypedDict(
    "ClientGetSqlInjectionMatchSetResponseSqlInjectionMatchSetSqlInjectionMatchTuplesTypeDef",
    {
        "FieldToMatch": ClientGetSqlInjectionMatchSetResponseSqlInjectionMatchSetSqlInjectionMatchTuplesFieldToMatchTypeDef,
        "TextTransformation": Literal[
            "NONE",
            "COMPRESS_WHITE_SPACE",
            "HTML_ENTITY_DECODE",
            "LOWERCASE",
            "CMD_LINE",
            "URL_DECODE",
        ],
    },
    total=False,
)

ClientGetSqlInjectionMatchSetResponseSqlInjectionMatchSetTypeDef = TypedDict(
    "ClientGetSqlInjectionMatchSetResponseSqlInjectionMatchSetTypeDef",
    {
        "SqlInjectionMatchSetId": str,
        "Name": str,
        "SqlInjectionMatchTuples": List[
            ClientGetSqlInjectionMatchSetResponseSqlInjectionMatchSetSqlInjectionMatchTuplesTypeDef
        ],
    },
    total=False,
)

ClientGetSqlInjectionMatchSetResponseTypeDef = TypedDict(
    "ClientGetSqlInjectionMatchSetResponseTypeDef",
    {"SqlInjectionMatchSet": ClientGetSqlInjectionMatchSetResponseSqlInjectionMatchSetTypeDef},
    total=False,
)

ClientGetWebAclForResourceResponseWebACLSummaryTypeDef = TypedDict(
    "ClientGetWebAclForResourceResponseWebACLSummaryTypeDef",
    {"WebACLId": str, "Name": str},
    total=False,
)

ClientGetWebAclForResourceResponseTypeDef = TypedDict(
    "ClientGetWebAclForResourceResponseTypeDef",
    {"WebACLSummary": ClientGetWebAclForResourceResponseWebACLSummaryTypeDef},
    total=False,
)

ClientGetWebAclResponseWebACLDefaultActionTypeDef = TypedDict(
    "ClientGetWebAclResponseWebACLDefaultActionTypeDef",
    {"Type": Literal["BLOCK", "ALLOW", "COUNT"]},
    total=False,
)

ClientGetWebAclResponseWebACLRulesActionTypeDef = TypedDict(
    "ClientGetWebAclResponseWebACLRulesActionTypeDef",
    {"Type": Literal["BLOCK", "ALLOW", "COUNT"]},
    total=False,
)

ClientGetWebAclResponseWebACLRulesExcludedRulesTypeDef = TypedDict(
    "ClientGetWebAclResponseWebACLRulesExcludedRulesTypeDef", {"RuleId": str}, total=False
)

ClientGetWebAclResponseWebACLRulesOverrideActionTypeDef = TypedDict(
    "ClientGetWebAclResponseWebACLRulesOverrideActionTypeDef",
    {"Type": Literal["NONE", "COUNT"]},
    total=False,
)

ClientGetWebAclResponseWebACLRulesTypeDef = TypedDict(
    "ClientGetWebAclResponseWebACLRulesTypeDef",
    {
        "Priority": int,
        "RuleId": str,
        "Action": ClientGetWebAclResponseWebACLRulesActionTypeDef,
        "OverrideAction": ClientGetWebAclResponseWebACLRulesOverrideActionTypeDef,
        "Type": Literal["REGULAR", "RATE_BASED", "GROUP"],
        "ExcludedRules": List[ClientGetWebAclResponseWebACLRulesExcludedRulesTypeDef],
    },
    total=False,
)

ClientGetWebAclResponseWebACLTypeDef = TypedDict(
    "ClientGetWebAclResponseWebACLTypeDef",
    {
        "WebACLId": str,
        "Name": str,
        "MetricName": str,
        "DefaultAction": ClientGetWebAclResponseWebACLDefaultActionTypeDef,
        "Rules": List[ClientGetWebAclResponseWebACLRulesTypeDef],
        "WebACLArn": str,
    },
    total=False,
)

ClientGetWebAclResponseTypeDef = TypedDict(
    "ClientGetWebAclResponseTypeDef", {"WebACL": ClientGetWebAclResponseWebACLTypeDef}, total=False
)

ClientGetXssMatchSetResponseXssMatchSetXssMatchTuplesFieldToMatchTypeDef = TypedDict(
    "ClientGetXssMatchSetResponseXssMatchSetXssMatchTuplesFieldToMatchTypeDef",
    {
        "Type": Literal[
            "URI", "QUERY_STRING", "HEADER", "METHOD", "BODY", "SINGLE_QUERY_ARG", "ALL_QUERY_ARGS"
        ],
        "Data": str,
    },
    total=False,
)

ClientGetXssMatchSetResponseXssMatchSetXssMatchTuplesTypeDef = TypedDict(
    "ClientGetXssMatchSetResponseXssMatchSetXssMatchTuplesTypeDef",
    {
        "FieldToMatch": ClientGetXssMatchSetResponseXssMatchSetXssMatchTuplesFieldToMatchTypeDef,
        "TextTransformation": Literal[
            "NONE",
            "COMPRESS_WHITE_SPACE",
            "HTML_ENTITY_DECODE",
            "LOWERCASE",
            "CMD_LINE",
            "URL_DECODE",
        ],
    },
    total=False,
)

ClientGetXssMatchSetResponseXssMatchSetTypeDef = TypedDict(
    "ClientGetXssMatchSetResponseXssMatchSetTypeDef",
    {
        "XssMatchSetId": str,
        "Name": str,
        "XssMatchTuples": List[ClientGetXssMatchSetResponseXssMatchSetXssMatchTuplesTypeDef],
    },
    total=False,
)

ClientGetXssMatchSetResponseTypeDef = TypedDict(
    "ClientGetXssMatchSetResponseTypeDef",
    {"XssMatchSet": ClientGetXssMatchSetResponseXssMatchSetTypeDef},
    total=False,
)

ClientListActivatedRulesInRuleGroupResponseActivatedRulesActionTypeDef = TypedDict(
    "ClientListActivatedRulesInRuleGroupResponseActivatedRulesActionTypeDef",
    {"Type": Literal["BLOCK", "ALLOW", "COUNT"]},
    total=False,
)

ClientListActivatedRulesInRuleGroupResponseActivatedRulesExcludedRulesTypeDef = TypedDict(
    "ClientListActivatedRulesInRuleGroupResponseActivatedRulesExcludedRulesTypeDef",
    {"RuleId": str},
    total=False,
)

ClientListActivatedRulesInRuleGroupResponseActivatedRulesOverrideActionTypeDef = TypedDict(
    "ClientListActivatedRulesInRuleGroupResponseActivatedRulesOverrideActionTypeDef",
    {"Type": Literal["NONE", "COUNT"]},
    total=False,
)

ClientListActivatedRulesInRuleGroupResponseActivatedRulesTypeDef = TypedDict(
    "ClientListActivatedRulesInRuleGroupResponseActivatedRulesTypeDef",
    {
        "Priority": int,
        "RuleId": str,
        "Action": ClientListActivatedRulesInRuleGroupResponseActivatedRulesActionTypeDef,
        "OverrideAction": ClientListActivatedRulesInRuleGroupResponseActivatedRulesOverrideActionTypeDef,
        "Type": Literal["REGULAR", "RATE_BASED", "GROUP"],
        "ExcludedRules": List[
            ClientListActivatedRulesInRuleGroupResponseActivatedRulesExcludedRulesTypeDef
        ],
    },
    total=False,
)

ClientListActivatedRulesInRuleGroupResponseTypeDef = TypedDict(
    "ClientListActivatedRulesInRuleGroupResponseTypeDef",
    {
        "NextMarker": str,
        "ActivatedRules": List[ClientListActivatedRulesInRuleGroupResponseActivatedRulesTypeDef],
    },
    total=False,
)

ClientListByteMatchSetsResponseByteMatchSetsTypeDef = TypedDict(
    "ClientListByteMatchSetsResponseByteMatchSetsTypeDef",
    {"ByteMatchSetId": str, "Name": str},
    total=False,
)

ClientListByteMatchSetsResponseTypeDef = TypedDict(
    "ClientListByteMatchSetsResponseTypeDef",
    {"NextMarker": str, "ByteMatchSets": List[ClientListByteMatchSetsResponseByteMatchSetsTypeDef]},
    total=False,
)

ClientListGeoMatchSetsResponseGeoMatchSetsTypeDef = TypedDict(
    "ClientListGeoMatchSetsResponseGeoMatchSetsTypeDef",
    {"GeoMatchSetId": str, "Name": str},
    total=False,
)

ClientListGeoMatchSetsResponseTypeDef = TypedDict(
    "ClientListGeoMatchSetsResponseTypeDef",
    {"NextMarker": str, "GeoMatchSets": List[ClientListGeoMatchSetsResponseGeoMatchSetsTypeDef]},
    total=False,
)

ClientListIpSetsResponseIPSetsTypeDef = TypedDict(
    "ClientListIpSetsResponseIPSetsTypeDef", {"IPSetId": str, "Name": str}, total=False
)

ClientListIpSetsResponseTypeDef = TypedDict(
    "ClientListIpSetsResponseTypeDef",
    {"NextMarker": str, "IPSets": List[ClientListIpSetsResponseIPSetsTypeDef]},
    total=False,
)

ClientListLoggingConfigurationsResponseLoggingConfigurationsRedactedFieldsTypeDef = TypedDict(
    "ClientListLoggingConfigurationsResponseLoggingConfigurationsRedactedFieldsTypeDef",
    {
        "Type": Literal[
            "URI", "QUERY_STRING", "HEADER", "METHOD", "BODY", "SINGLE_QUERY_ARG", "ALL_QUERY_ARGS"
        ],
        "Data": str,
    },
    total=False,
)

ClientListLoggingConfigurationsResponseLoggingConfigurationsTypeDef = TypedDict(
    "ClientListLoggingConfigurationsResponseLoggingConfigurationsTypeDef",
    {
        "ResourceArn": str,
        "LogDestinationConfigs": List[str],
        "RedactedFields": List[
            ClientListLoggingConfigurationsResponseLoggingConfigurationsRedactedFieldsTypeDef
        ],
    },
    total=False,
)

ClientListLoggingConfigurationsResponseTypeDef = TypedDict(
    "ClientListLoggingConfigurationsResponseTypeDef",
    {
        "LoggingConfigurations": List[
            ClientListLoggingConfigurationsResponseLoggingConfigurationsTypeDef
        ],
        "NextMarker": str,
    },
    total=False,
)

ClientListRateBasedRulesResponseRulesTypeDef = TypedDict(
    "ClientListRateBasedRulesResponseRulesTypeDef", {"RuleId": str, "Name": str}, total=False
)

ClientListRateBasedRulesResponseTypeDef = TypedDict(
    "ClientListRateBasedRulesResponseTypeDef",
    {"NextMarker": str, "Rules": List[ClientListRateBasedRulesResponseRulesTypeDef]},
    total=False,
)

ClientListRegexMatchSetsResponseRegexMatchSetsTypeDef = TypedDict(
    "ClientListRegexMatchSetsResponseRegexMatchSetsTypeDef",
    {"RegexMatchSetId": str, "Name": str},
    total=False,
)

ClientListRegexMatchSetsResponseTypeDef = TypedDict(
    "ClientListRegexMatchSetsResponseTypeDef",
    {
        "NextMarker": str,
        "RegexMatchSets": List[ClientListRegexMatchSetsResponseRegexMatchSetsTypeDef],
    },
    total=False,
)

ClientListRegexPatternSetsResponseRegexPatternSetsTypeDef = TypedDict(
    "ClientListRegexPatternSetsResponseRegexPatternSetsTypeDef",
    {"RegexPatternSetId": str, "Name": str},
    total=False,
)

ClientListRegexPatternSetsResponseTypeDef = TypedDict(
    "ClientListRegexPatternSetsResponseTypeDef",
    {
        "NextMarker": str,
        "RegexPatternSets": List[ClientListRegexPatternSetsResponseRegexPatternSetsTypeDef],
    },
    total=False,
)

ClientListResourcesForWebAclResponseTypeDef = TypedDict(
    "ClientListResourcesForWebAclResponseTypeDef", {"ResourceArns": List[str]}, total=False
)

ClientListRuleGroupsResponseRuleGroupsTypeDef = TypedDict(
    "ClientListRuleGroupsResponseRuleGroupsTypeDef", {"RuleGroupId": str, "Name": str}, total=False
)

ClientListRuleGroupsResponseTypeDef = TypedDict(
    "ClientListRuleGroupsResponseTypeDef",
    {"NextMarker": str, "RuleGroups": List[ClientListRuleGroupsResponseRuleGroupsTypeDef]},
    total=False,
)

ClientListRulesResponseRulesTypeDef = TypedDict(
    "ClientListRulesResponseRulesTypeDef", {"RuleId": str, "Name": str}, total=False
)

ClientListRulesResponseTypeDef = TypedDict(
    "ClientListRulesResponseTypeDef",
    {"NextMarker": str, "Rules": List[ClientListRulesResponseRulesTypeDef]},
    total=False,
)

ClientListSizeConstraintSetsResponseSizeConstraintSetsTypeDef = TypedDict(
    "ClientListSizeConstraintSetsResponseSizeConstraintSetsTypeDef",
    {"SizeConstraintSetId": str, "Name": str},
    total=False,
)

ClientListSizeConstraintSetsResponseTypeDef = TypedDict(
    "ClientListSizeConstraintSetsResponseTypeDef",
    {
        "NextMarker": str,
        "SizeConstraintSets": List[ClientListSizeConstraintSetsResponseSizeConstraintSetsTypeDef],
    },
    total=False,
)

ClientListSqlInjectionMatchSetsResponseSqlInjectionMatchSetsTypeDef = TypedDict(
    "ClientListSqlInjectionMatchSetsResponseSqlInjectionMatchSetsTypeDef",
    {"SqlInjectionMatchSetId": str, "Name": str},
    total=False,
)

ClientListSqlInjectionMatchSetsResponseTypeDef = TypedDict(
    "ClientListSqlInjectionMatchSetsResponseTypeDef",
    {
        "NextMarker": str,
        "SqlInjectionMatchSets": List[
            ClientListSqlInjectionMatchSetsResponseSqlInjectionMatchSetsTypeDef
        ],
    },
    total=False,
)

ClientListSubscribedRuleGroupsResponseRuleGroupsTypeDef = TypedDict(
    "ClientListSubscribedRuleGroupsResponseRuleGroupsTypeDef",
    {"RuleGroupId": str, "Name": str, "MetricName": str},
    total=False,
)

ClientListSubscribedRuleGroupsResponseTypeDef = TypedDict(
    "ClientListSubscribedRuleGroupsResponseTypeDef",
    {
        "NextMarker": str,
        "RuleGroups": List[ClientListSubscribedRuleGroupsResponseRuleGroupsTypeDef],
    },
    total=False,
)

ClientListTagsForResourceResponseTagInfoForResourceTagListTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTagInfoForResourceTagListTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientListTagsForResourceResponseTagInfoForResourceTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTagInfoForResourceTypeDef",
    {
        "ResourceARN": str,
        "TagList": List[ClientListTagsForResourceResponseTagInfoForResourceTagListTypeDef],
    },
    total=False,
)

ClientListTagsForResourceResponseTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTypeDef",
    {
        "NextMarker": str,
        "TagInfoForResource": ClientListTagsForResourceResponseTagInfoForResourceTypeDef,
    },
    total=False,
)

ClientListWebAclsResponseWebACLsTypeDef = TypedDict(
    "ClientListWebAclsResponseWebACLsTypeDef", {"WebACLId": str, "Name": str}, total=False
)

ClientListWebAclsResponseTypeDef = TypedDict(
    "ClientListWebAclsResponseTypeDef",
    {"NextMarker": str, "WebACLs": List[ClientListWebAclsResponseWebACLsTypeDef]},
    total=False,
)

ClientListXssMatchSetsResponseXssMatchSetsTypeDef = TypedDict(
    "ClientListXssMatchSetsResponseXssMatchSetsTypeDef",
    {"XssMatchSetId": str, "Name": str},
    total=False,
)

ClientListXssMatchSetsResponseTypeDef = TypedDict(
    "ClientListXssMatchSetsResponseTypeDef",
    {"NextMarker": str, "XssMatchSets": List[ClientListXssMatchSetsResponseXssMatchSetsTypeDef]},
    total=False,
)

ClientPutLoggingConfigurationLoggingConfigurationRedactedFieldsTypeDef = TypedDict(
    "ClientPutLoggingConfigurationLoggingConfigurationRedactedFieldsTypeDef",
    {
        "Type": Literal[
            "URI", "QUERY_STRING", "HEADER", "METHOD", "BODY", "SINGLE_QUERY_ARG", "ALL_QUERY_ARGS"
        ],
        "Data": str,
    },
    total=False,
)

ClientPutLoggingConfigurationLoggingConfigurationTypeDef = TypedDict(
    "ClientPutLoggingConfigurationLoggingConfigurationTypeDef",
    {
        "ResourceArn": str,
        "LogDestinationConfigs": List[str],
        "RedactedFields": List[
            ClientPutLoggingConfigurationLoggingConfigurationRedactedFieldsTypeDef
        ],
    },
    total=False,
)

ClientPutLoggingConfigurationResponseLoggingConfigurationRedactedFieldsTypeDef = TypedDict(
    "ClientPutLoggingConfigurationResponseLoggingConfigurationRedactedFieldsTypeDef",
    {
        "Type": Literal[
            "URI", "QUERY_STRING", "HEADER", "METHOD", "BODY", "SINGLE_QUERY_ARG", "ALL_QUERY_ARGS"
        ],
        "Data": str,
    },
    total=False,
)

ClientPutLoggingConfigurationResponseLoggingConfigurationTypeDef = TypedDict(
    "ClientPutLoggingConfigurationResponseLoggingConfigurationTypeDef",
    {
        "ResourceArn": str,
        "LogDestinationConfigs": List[str],
        "RedactedFields": List[
            ClientPutLoggingConfigurationResponseLoggingConfigurationRedactedFieldsTypeDef
        ],
    },
    total=False,
)

ClientPutLoggingConfigurationResponseTypeDef = TypedDict(
    "ClientPutLoggingConfigurationResponseTypeDef",
    {"LoggingConfiguration": ClientPutLoggingConfigurationResponseLoggingConfigurationTypeDef},
    total=False,
)

ClientTagResourceTagsTypeDef = TypedDict(
    "ClientTagResourceTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientUpdateByteMatchSetResponseTypeDef = TypedDict(
    "ClientUpdateByteMatchSetResponseTypeDef", {"ChangeToken": str}, total=False
)

ClientUpdateByteMatchSetUpdatesByteMatchTupleFieldToMatchTypeDef = TypedDict(
    "ClientUpdateByteMatchSetUpdatesByteMatchTupleFieldToMatchTypeDef",
    {
        "Type": Literal[
            "URI", "QUERY_STRING", "HEADER", "METHOD", "BODY", "SINGLE_QUERY_ARG", "ALL_QUERY_ARGS"
        ],
        "Data": str,
    },
    total=False,
)

ClientUpdateByteMatchSetUpdatesByteMatchTupleTypeDef = TypedDict(
    "ClientUpdateByteMatchSetUpdatesByteMatchTupleTypeDef",
    {
        "FieldToMatch": ClientUpdateByteMatchSetUpdatesByteMatchTupleFieldToMatchTypeDef,
        "TargetString": bytes,
        "TextTransformation": Literal[
            "NONE",
            "COMPRESS_WHITE_SPACE",
            "HTML_ENTITY_DECODE",
            "LOWERCASE",
            "CMD_LINE",
            "URL_DECODE",
        ],
        "PositionalConstraint": Literal[
            "EXACTLY", "STARTS_WITH", "ENDS_WITH", "CONTAINS", "CONTAINS_WORD"
        ],
    },
    total=False,
)

_RequiredClientUpdateByteMatchSetUpdatesTypeDef = TypedDict(
    "_RequiredClientUpdateByteMatchSetUpdatesTypeDef", {"Action": Literal["INSERT", "DELETE"]}
)
_OptionalClientUpdateByteMatchSetUpdatesTypeDef = TypedDict(
    "_OptionalClientUpdateByteMatchSetUpdatesTypeDef",
    {"ByteMatchTuple": ClientUpdateByteMatchSetUpdatesByteMatchTupleTypeDef},
    total=False,
)


class ClientUpdateByteMatchSetUpdatesTypeDef(
    _RequiredClientUpdateByteMatchSetUpdatesTypeDef, _OptionalClientUpdateByteMatchSetUpdatesTypeDef
):
    pass


ClientUpdateGeoMatchSetResponseTypeDef = TypedDict(
    "ClientUpdateGeoMatchSetResponseTypeDef", {"ChangeToken": str}, total=False
)

ClientUpdateGeoMatchSetUpdatesGeoMatchConstraintTypeDef = TypedDict(
    "ClientUpdateGeoMatchSetUpdatesGeoMatchConstraintTypeDef",
    {
        "Type": str,
        "Value": Literal[
            "AF",
            "AX",
            "AL",
            "DZ",
            "AS",
            "AD",
            "AO",
            "AI",
            "AQ",
            "AG",
            "AR",
            "AM",
            "AW",
            "AU",
            "AT",
            "AZ",
            "BS",
            "BH",
            "BD",
            "BB",
            "BY",
            "BE",
            "BZ",
            "BJ",
            "BM",
            "BT",
            "BO",
            "BQ",
            "BA",
            "BW",
            "BV",
            "BR",
            "IO",
            "BN",
            "BG",
            "BF",
            "BI",
            "KH",
            "CM",
            "CA",
            "CV",
            "KY",
            "CF",
            "TD",
            "CL",
            "CN",
            "CX",
            "CC",
            "CO",
            "KM",
            "CG",
            "CD",
            "CK",
            "CR",
            "CI",
            "HR",
            "CU",
            "CW",
            "CY",
            "CZ",
            "DK",
            "DJ",
            "DM",
            "DO",
            "EC",
            "EG",
            "SV",
            "GQ",
            "ER",
            "EE",
            "ET",
            "FK",
            "FO",
            "FJ",
            "FI",
            "FR",
            "GF",
            "PF",
            "TF",
            "GA",
            "GM",
            "GE",
            "DE",
            "GH",
            "GI",
            "GR",
            "GL",
            "GD",
            "GP",
            "GU",
            "GT",
            "GG",
            "GN",
            "GW",
            "GY",
            "HT",
            "HM",
            "VA",
            "HN",
            "HK",
            "HU",
            "IS",
            "IN",
            "ID",
            "IR",
            "IQ",
            "IE",
            "IM",
            "IL",
            "IT",
            "JM",
            "JP",
            "JE",
            "JO",
            "KZ",
            "KE",
            "KI",
            "KP",
            "KR",
            "KW",
            "KG",
            "LA",
            "LV",
            "LB",
            "LS",
            "LR",
            "LY",
            "LI",
            "LT",
            "LU",
            "MO",
            "MK",
            "MG",
            "MW",
            "MY",
            "MV",
            "ML",
            "MT",
            "MH",
            "MQ",
            "MR",
            "MU",
            "YT",
            "MX",
            "FM",
            "MD",
            "MC",
            "MN",
            "ME",
            "MS",
            "MA",
            "MZ",
            "MM",
            "NA",
            "NR",
            "NP",
            "NL",
            "NC",
            "NZ",
            "NI",
            "NE",
            "NG",
            "NU",
            "NF",
            "MP",
            "NO",
            "OM",
            "PK",
            "PW",
            "PS",
            "PA",
            "PG",
            "PY",
            "PE",
            "PH",
            "PN",
            "PL",
            "PT",
            "PR",
            "QA",
            "RE",
            "RO",
            "RU",
            "RW",
            "BL",
            "SH",
            "KN",
            "LC",
            "MF",
            "PM",
            "VC",
            "WS",
            "SM",
            "ST",
            "SA",
            "SN",
            "RS",
            "SC",
            "SL",
            "SG",
            "SX",
            "SK",
            "SI",
            "SB",
            "SO",
            "ZA",
            "GS",
            "SS",
            "ES",
            "LK",
            "SD",
            "SR",
            "SJ",
            "SZ",
            "SE",
            "CH",
            "SY",
            "TW",
            "TJ",
            "TZ",
            "TH",
            "TL",
            "TG",
            "TK",
            "TO",
            "TT",
            "TN",
            "TR",
            "TM",
            "TC",
            "TV",
            "UG",
            "UA",
            "AE",
            "GB",
            "US",
            "UM",
            "UY",
            "UZ",
            "VU",
            "VE",
            "VN",
            "VG",
            "VI",
            "WF",
            "EH",
            "YE",
            "ZM",
            "ZW",
        ],
    },
    total=False,
)

_RequiredClientUpdateGeoMatchSetUpdatesTypeDef = TypedDict(
    "_RequiredClientUpdateGeoMatchSetUpdatesTypeDef", {"Action": Literal["INSERT", "DELETE"]}
)
_OptionalClientUpdateGeoMatchSetUpdatesTypeDef = TypedDict(
    "_OptionalClientUpdateGeoMatchSetUpdatesTypeDef",
    {"GeoMatchConstraint": ClientUpdateGeoMatchSetUpdatesGeoMatchConstraintTypeDef},
    total=False,
)


class ClientUpdateGeoMatchSetUpdatesTypeDef(
    _RequiredClientUpdateGeoMatchSetUpdatesTypeDef, _OptionalClientUpdateGeoMatchSetUpdatesTypeDef
):
    pass


ClientUpdateIpSetResponseTypeDef = TypedDict(
    "ClientUpdateIpSetResponseTypeDef", {"ChangeToken": str}, total=False
)

ClientUpdateIpSetUpdatesIPSetDescriptorTypeDef = TypedDict(
    "ClientUpdateIpSetUpdatesIPSetDescriptorTypeDef",
    {"Type": Literal["IPV4", "IPV6"], "Value": str},
    total=False,
)

_RequiredClientUpdateIpSetUpdatesTypeDef = TypedDict(
    "_RequiredClientUpdateIpSetUpdatesTypeDef", {"Action": Literal["INSERT", "DELETE"]}
)
_OptionalClientUpdateIpSetUpdatesTypeDef = TypedDict(
    "_OptionalClientUpdateIpSetUpdatesTypeDef",
    {"IPSetDescriptor": ClientUpdateIpSetUpdatesIPSetDescriptorTypeDef},
    total=False,
)


class ClientUpdateIpSetUpdatesTypeDef(
    _RequiredClientUpdateIpSetUpdatesTypeDef, _OptionalClientUpdateIpSetUpdatesTypeDef
):
    pass


ClientUpdateRateBasedRuleResponseTypeDef = TypedDict(
    "ClientUpdateRateBasedRuleResponseTypeDef", {"ChangeToken": str}, total=False
)

ClientUpdateRateBasedRuleUpdatesPredicateTypeDef = TypedDict(
    "ClientUpdateRateBasedRuleUpdatesPredicateTypeDef",
    {
        "Negated": bool,
        "Type": Literal[
            "IPMatch",
            "ByteMatch",
            "SqlInjectionMatch",
            "GeoMatch",
            "SizeConstraint",
            "XssMatch",
            "RegexMatch",
        ],
        "DataId": str,
    },
    total=False,
)

_RequiredClientUpdateRateBasedRuleUpdatesTypeDef = TypedDict(
    "_RequiredClientUpdateRateBasedRuleUpdatesTypeDef", {"Action": Literal["INSERT", "DELETE"]}
)
_OptionalClientUpdateRateBasedRuleUpdatesTypeDef = TypedDict(
    "_OptionalClientUpdateRateBasedRuleUpdatesTypeDef",
    {"Predicate": ClientUpdateRateBasedRuleUpdatesPredicateTypeDef},
    total=False,
)


class ClientUpdateRateBasedRuleUpdatesTypeDef(
    _RequiredClientUpdateRateBasedRuleUpdatesTypeDef,
    _OptionalClientUpdateRateBasedRuleUpdatesTypeDef,
):
    pass


ClientUpdateRegexMatchSetResponseTypeDef = TypedDict(
    "ClientUpdateRegexMatchSetResponseTypeDef", {"ChangeToken": str}, total=False
)

ClientUpdateRegexMatchSetUpdatesRegexMatchTupleFieldToMatchTypeDef = TypedDict(
    "ClientUpdateRegexMatchSetUpdatesRegexMatchTupleFieldToMatchTypeDef",
    {
        "Type": Literal[
            "URI", "QUERY_STRING", "HEADER", "METHOD", "BODY", "SINGLE_QUERY_ARG", "ALL_QUERY_ARGS"
        ],
        "Data": str,
    },
    total=False,
)

ClientUpdateRegexMatchSetUpdatesRegexMatchTupleTypeDef = TypedDict(
    "ClientUpdateRegexMatchSetUpdatesRegexMatchTupleTypeDef",
    {
        "FieldToMatch": ClientUpdateRegexMatchSetUpdatesRegexMatchTupleFieldToMatchTypeDef,
        "TextTransformation": Literal[
            "NONE",
            "COMPRESS_WHITE_SPACE",
            "HTML_ENTITY_DECODE",
            "LOWERCASE",
            "CMD_LINE",
            "URL_DECODE",
        ],
        "RegexPatternSetId": str,
    },
    total=False,
)

_RequiredClientUpdateRegexMatchSetUpdatesTypeDef = TypedDict(
    "_RequiredClientUpdateRegexMatchSetUpdatesTypeDef", {"Action": Literal["INSERT", "DELETE"]}
)
_OptionalClientUpdateRegexMatchSetUpdatesTypeDef = TypedDict(
    "_OptionalClientUpdateRegexMatchSetUpdatesTypeDef",
    {"RegexMatchTuple": ClientUpdateRegexMatchSetUpdatesRegexMatchTupleTypeDef},
    total=False,
)


class ClientUpdateRegexMatchSetUpdatesTypeDef(
    _RequiredClientUpdateRegexMatchSetUpdatesTypeDef,
    _OptionalClientUpdateRegexMatchSetUpdatesTypeDef,
):
    pass


ClientUpdateRegexPatternSetResponseTypeDef = TypedDict(
    "ClientUpdateRegexPatternSetResponseTypeDef", {"ChangeToken": str}, total=False
)

_RequiredClientUpdateRegexPatternSetUpdatesTypeDef = TypedDict(
    "_RequiredClientUpdateRegexPatternSetUpdatesTypeDef", {"Action": Literal["INSERT", "DELETE"]}
)
_OptionalClientUpdateRegexPatternSetUpdatesTypeDef = TypedDict(
    "_OptionalClientUpdateRegexPatternSetUpdatesTypeDef", {"RegexPatternString": str}, total=False
)


class ClientUpdateRegexPatternSetUpdatesTypeDef(
    _RequiredClientUpdateRegexPatternSetUpdatesTypeDef,
    _OptionalClientUpdateRegexPatternSetUpdatesTypeDef,
):
    pass


ClientUpdateRuleGroupResponseTypeDef = TypedDict(
    "ClientUpdateRuleGroupResponseTypeDef", {"ChangeToken": str}, total=False
)

ClientUpdateRuleGroupUpdatesActivatedRuleActionTypeDef = TypedDict(
    "ClientUpdateRuleGroupUpdatesActivatedRuleActionTypeDef",
    {"Type": Literal["BLOCK", "ALLOW", "COUNT"]},
    total=False,
)

ClientUpdateRuleGroupUpdatesActivatedRuleExcludedRulesTypeDef = TypedDict(
    "ClientUpdateRuleGroupUpdatesActivatedRuleExcludedRulesTypeDef", {"RuleId": str}, total=False
)

ClientUpdateRuleGroupUpdatesActivatedRuleOverrideActionTypeDef = TypedDict(
    "ClientUpdateRuleGroupUpdatesActivatedRuleOverrideActionTypeDef",
    {"Type": Literal["NONE", "COUNT"]},
    total=False,
)

ClientUpdateRuleGroupUpdatesActivatedRuleTypeDef = TypedDict(
    "ClientUpdateRuleGroupUpdatesActivatedRuleTypeDef",
    {
        "Priority": int,
        "RuleId": str,
        "Action": ClientUpdateRuleGroupUpdatesActivatedRuleActionTypeDef,
        "OverrideAction": ClientUpdateRuleGroupUpdatesActivatedRuleOverrideActionTypeDef,
        "Type": Literal["REGULAR", "RATE_BASED", "GROUP"],
        "ExcludedRules": List[ClientUpdateRuleGroupUpdatesActivatedRuleExcludedRulesTypeDef],
    },
    total=False,
)

ClientUpdateRuleGroupUpdatesTypeDef = TypedDict(
    "ClientUpdateRuleGroupUpdatesTypeDef",
    {
        "Action": Literal["INSERT", "DELETE"],
        "ActivatedRule": ClientUpdateRuleGroupUpdatesActivatedRuleTypeDef,
    },
    total=False,
)

ClientUpdateRuleResponseTypeDef = TypedDict(
    "ClientUpdateRuleResponseTypeDef", {"ChangeToken": str}, total=False
)

ClientUpdateRuleUpdatesPredicateTypeDef = TypedDict(
    "ClientUpdateRuleUpdatesPredicateTypeDef",
    {
        "Negated": bool,
        "Type": Literal[
            "IPMatch",
            "ByteMatch",
            "SqlInjectionMatch",
            "GeoMatch",
            "SizeConstraint",
            "XssMatch",
            "RegexMatch",
        ],
        "DataId": str,
    },
    total=False,
)

_RequiredClientUpdateRuleUpdatesTypeDef = TypedDict(
    "_RequiredClientUpdateRuleUpdatesTypeDef", {"Action": Literal["INSERT", "DELETE"]}
)
_OptionalClientUpdateRuleUpdatesTypeDef = TypedDict(
    "_OptionalClientUpdateRuleUpdatesTypeDef",
    {"Predicate": ClientUpdateRuleUpdatesPredicateTypeDef},
    total=False,
)


class ClientUpdateRuleUpdatesTypeDef(
    _RequiredClientUpdateRuleUpdatesTypeDef, _OptionalClientUpdateRuleUpdatesTypeDef
):
    pass


ClientUpdateSizeConstraintSetResponseTypeDef = TypedDict(
    "ClientUpdateSizeConstraintSetResponseTypeDef", {"ChangeToken": str}, total=False
)

ClientUpdateSizeConstraintSetUpdatesSizeConstraintFieldToMatchTypeDef = TypedDict(
    "ClientUpdateSizeConstraintSetUpdatesSizeConstraintFieldToMatchTypeDef",
    {
        "Type": Literal[
            "URI", "QUERY_STRING", "HEADER", "METHOD", "BODY", "SINGLE_QUERY_ARG", "ALL_QUERY_ARGS"
        ],
        "Data": str,
    },
    total=False,
)

ClientUpdateSizeConstraintSetUpdatesSizeConstraintTypeDef = TypedDict(
    "ClientUpdateSizeConstraintSetUpdatesSizeConstraintTypeDef",
    {
        "FieldToMatch": ClientUpdateSizeConstraintSetUpdatesSizeConstraintFieldToMatchTypeDef,
        "TextTransformation": Literal[
            "NONE",
            "COMPRESS_WHITE_SPACE",
            "HTML_ENTITY_DECODE",
            "LOWERCASE",
            "CMD_LINE",
            "URL_DECODE",
        ],
        "ComparisonOperator": Literal["EQ", "NE", "LE", "LT", "GE", "GT"],
        "Size": int,
    },
    total=False,
)

_RequiredClientUpdateSizeConstraintSetUpdatesTypeDef = TypedDict(
    "_RequiredClientUpdateSizeConstraintSetUpdatesTypeDef", {"Action": Literal["INSERT", "DELETE"]}
)
_OptionalClientUpdateSizeConstraintSetUpdatesTypeDef = TypedDict(
    "_OptionalClientUpdateSizeConstraintSetUpdatesTypeDef",
    {"SizeConstraint": ClientUpdateSizeConstraintSetUpdatesSizeConstraintTypeDef},
    total=False,
)


class ClientUpdateSizeConstraintSetUpdatesTypeDef(
    _RequiredClientUpdateSizeConstraintSetUpdatesTypeDef,
    _OptionalClientUpdateSizeConstraintSetUpdatesTypeDef,
):
    pass


ClientUpdateSqlInjectionMatchSetResponseTypeDef = TypedDict(
    "ClientUpdateSqlInjectionMatchSetResponseTypeDef", {"ChangeToken": str}, total=False
)

ClientUpdateSqlInjectionMatchSetUpdatesSqlInjectionMatchTupleFieldToMatchTypeDef = TypedDict(
    "ClientUpdateSqlInjectionMatchSetUpdatesSqlInjectionMatchTupleFieldToMatchTypeDef",
    {
        "Type": Literal[
            "URI", "QUERY_STRING", "HEADER", "METHOD", "BODY", "SINGLE_QUERY_ARG", "ALL_QUERY_ARGS"
        ],
        "Data": str,
    },
    total=False,
)

ClientUpdateSqlInjectionMatchSetUpdatesSqlInjectionMatchTupleTypeDef = TypedDict(
    "ClientUpdateSqlInjectionMatchSetUpdatesSqlInjectionMatchTupleTypeDef",
    {
        "FieldToMatch": ClientUpdateSqlInjectionMatchSetUpdatesSqlInjectionMatchTupleFieldToMatchTypeDef,
        "TextTransformation": Literal[
            "NONE",
            "COMPRESS_WHITE_SPACE",
            "HTML_ENTITY_DECODE",
            "LOWERCASE",
            "CMD_LINE",
            "URL_DECODE",
        ],
    },
    total=False,
)

_RequiredClientUpdateSqlInjectionMatchSetUpdatesTypeDef = TypedDict(
    "_RequiredClientUpdateSqlInjectionMatchSetUpdatesTypeDef",
    {"Action": Literal["INSERT", "DELETE"]},
)
_OptionalClientUpdateSqlInjectionMatchSetUpdatesTypeDef = TypedDict(
    "_OptionalClientUpdateSqlInjectionMatchSetUpdatesTypeDef",
    {
        "SqlInjectionMatchTuple": ClientUpdateSqlInjectionMatchSetUpdatesSqlInjectionMatchTupleTypeDef
    },
    total=False,
)


class ClientUpdateSqlInjectionMatchSetUpdatesTypeDef(
    _RequiredClientUpdateSqlInjectionMatchSetUpdatesTypeDef,
    _OptionalClientUpdateSqlInjectionMatchSetUpdatesTypeDef,
):
    pass


ClientUpdateWebAclDefaultActionTypeDef = TypedDict(
    "ClientUpdateWebAclDefaultActionTypeDef", {"Type": Literal["BLOCK", "ALLOW", "COUNT"]}
)

ClientUpdateWebAclResponseTypeDef = TypedDict(
    "ClientUpdateWebAclResponseTypeDef", {"ChangeToken": str}, total=False
)

ClientUpdateWebAclUpdatesActivatedRuleActionTypeDef = TypedDict(
    "ClientUpdateWebAclUpdatesActivatedRuleActionTypeDef",
    {"Type": Literal["BLOCK", "ALLOW", "COUNT"]},
    total=False,
)

ClientUpdateWebAclUpdatesActivatedRuleExcludedRulesTypeDef = TypedDict(
    "ClientUpdateWebAclUpdatesActivatedRuleExcludedRulesTypeDef", {"RuleId": str}, total=False
)

ClientUpdateWebAclUpdatesActivatedRuleOverrideActionTypeDef = TypedDict(
    "ClientUpdateWebAclUpdatesActivatedRuleOverrideActionTypeDef",
    {"Type": Literal["NONE", "COUNT"]},
    total=False,
)

ClientUpdateWebAclUpdatesActivatedRuleTypeDef = TypedDict(
    "ClientUpdateWebAclUpdatesActivatedRuleTypeDef",
    {
        "Priority": int,
        "RuleId": str,
        "Action": ClientUpdateWebAclUpdatesActivatedRuleActionTypeDef,
        "OverrideAction": ClientUpdateWebAclUpdatesActivatedRuleOverrideActionTypeDef,
        "Type": Literal["REGULAR", "RATE_BASED", "GROUP"],
        "ExcludedRules": List[ClientUpdateWebAclUpdatesActivatedRuleExcludedRulesTypeDef],
    },
    total=False,
)

_RequiredClientUpdateWebAclUpdatesTypeDef = TypedDict(
    "_RequiredClientUpdateWebAclUpdatesTypeDef", {"Action": Literal["INSERT", "DELETE"]}
)
_OptionalClientUpdateWebAclUpdatesTypeDef = TypedDict(
    "_OptionalClientUpdateWebAclUpdatesTypeDef",
    {"ActivatedRule": ClientUpdateWebAclUpdatesActivatedRuleTypeDef},
    total=False,
)


class ClientUpdateWebAclUpdatesTypeDef(
    _RequiredClientUpdateWebAclUpdatesTypeDef, _OptionalClientUpdateWebAclUpdatesTypeDef
):
    pass


ClientUpdateXssMatchSetResponseTypeDef = TypedDict(
    "ClientUpdateXssMatchSetResponseTypeDef", {"ChangeToken": str}, total=False
)

ClientUpdateXssMatchSetUpdatesXssMatchTupleFieldToMatchTypeDef = TypedDict(
    "ClientUpdateXssMatchSetUpdatesXssMatchTupleFieldToMatchTypeDef",
    {
        "Type": Literal[
            "URI", "QUERY_STRING", "HEADER", "METHOD", "BODY", "SINGLE_QUERY_ARG", "ALL_QUERY_ARGS"
        ],
        "Data": str,
    },
    total=False,
)

ClientUpdateXssMatchSetUpdatesXssMatchTupleTypeDef = TypedDict(
    "ClientUpdateXssMatchSetUpdatesXssMatchTupleTypeDef",
    {
        "FieldToMatch": ClientUpdateXssMatchSetUpdatesXssMatchTupleFieldToMatchTypeDef,
        "TextTransformation": Literal[
            "NONE",
            "COMPRESS_WHITE_SPACE",
            "HTML_ENTITY_DECODE",
            "LOWERCASE",
            "CMD_LINE",
            "URL_DECODE",
        ],
    },
    total=False,
)

_RequiredClientUpdateXssMatchSetUpdatesTypeDef = TypedDict(
    "_RequiredClientUpdateXssMatchSetUpdatesTypeDef", {"Action": Literal["INSERT", "DELETE"]}
)
_OptionalClientUpdateXssMatchSetUpdatesTypeDef = TypedDict(
    "_OptionalClientUpdateXssMatchSetUpdatesTypeDef",
    {"XssMatchTuple": ClientUpdateXssMatchSetUpdatesXssMatchTupleTypeDef},
    total=False,
)


class ClientUpdateXssMatchSetUpdatesTypeDef(
    _RequiredClientUpdateXssMatchSetUpdatesTypeDef, _OptionalClientUpdateXssMatchSetUpdatesTypeDef
):
    pass
