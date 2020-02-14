"""
Main interface for wafv2 service type definitions.

Usage::

    from mypy_boto3.wafv2.type_defs import ClientCheckCapacityResponseTypeDef

    data: ClientCheckCapacityResponseTypeDef = {...}
"""
from datetime import datetime
import sys
from typing import Any, Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ClientCheckCapacityResponseTypeDef",
    "ClientCheckCapacityRulesActionTypeDef",
    "ClientCheckCapacityRulesOverrideActionTypeDef",
    "ClientCheckCapacityRulesStatementAndStatementTypeDef",
    "ClientCheckCapacityRulesStatementByteMatchStatementFieldToMatchSingleHeaderTypeDef",
    "ClientCheckCapacityRulesStatementByteMatchStatementFieldToMatchSingleQueryArgumentTypeDef",
    "ClientCheckCapacityRulesStatementByteMatchStatementFieldToMatchTypeDef",
    "ClientCheckCapacityRulesStatementByteMatchStatementTextTransformationsTypeDef",
    "ClientCheckCapacityRulesStatementByteMatchStatementTypeDef",
    "ClientCheckCapacityRulesStatementGeoMatchStatementTypeDef",
    "ClientCheckCapacityRulesStatementIPSetReferenceStatementTypeDef",
    "ClientCheckCapacityRulesStatementManagedRuleGroupStatementExcludedRulesTypeDef",
    "ClientCheckCapacityRulesStatementManagedRuleGroupStatementTypeDef",
    "ClientCheckCapacityRulesStatementNotStatementTypeDef",
    "ClientCheckCapacityRulesStatementOrStatementTypeDef",
    "ClientCheckCapacityRulesStatementRateBasedStatementTypeDef",
    "ClientCheckCapacityRulesStatementRegexPatternSetReferenceStatementFieldToMatchSingleHeaderTypeDef",
    "ClientCheckCapacityRulesStatementRegexPatternSetReferenceStatementFieldToMatchSingleQueryArgumentTypeDef",
    "ClientCheckCapacityRulesStatementRegexPatternSetReferenceStatementFieldToMatchTypeDef",
    "ClientCheckCapacityRulesStatementRegexPatternSetReferenceStatementTextTransformationsTypeDef",
    "ClientCheckCapacityRulesStatementRegexPatternSetReferenceStatementTypeDef",
    "ClientCheckCapacityRulesStatementRuleGroupReferenceStatementExcludedRulesTypeDef",
    "ClientCheckCapacityRulesStatementRuleGroupReferenceStatementTypeDef",
    "ClientCheckCapacityRulesStatementSizeConstraintStatementFieldToMatchSingleHeaderTypeDef",
    "ClientCheckCapacityRulesStatementSizeConstraintStatementFieldToMatchSingleQueryArgumentTypeDef",
    "ClientCheckCapacityRulesStatementSizeConstraintStatementFieldToMatchTypeDef",
    "ClientCheckCapacityRulesStatementSizeConstraintStatementTextTransformationsTypeDef",
    "ClientCheckCapacityRulesStatementSizeConstraintStatementTypeDef",
    "ClientCheckCapacityRulesStatementSqliMatchStatementFieldToMatchSingleHeaderTypeDef",
    "ClientCheckCapacityRulesStatementSqliMatchStatementFieldToMatchSingleQueryArgumentTypeDef",
    "ClientCheckCapacityRulesStatementSqliMatchStatementFieldToMatchTypeDef",
    "ClientCheckCapacityRulesStatementSqliMatchStatementTextTransformationsTypeDef",
    "ClientCheckCapacityRulesStatementSqliMatchStatementTypeDef",
    "ClientCheckCapacityRulesStatementXssMatchStatementFieldToMatchSingleHeaderTypeDef",
    "ClientCheckCapacityRulesStatementXssMatchStatementFieldToMatchSingleQueryArgumentTypeDef",
    "ClientCheckCapacityRulesStatementXssMatchStatementFieldToMatchTypeDef",
    "ClientCheckCapacityRulesStatementXssMatchStatementTextTransformationsTypeDef",
    "ClientCheckCapacityRulesStatementXssMatchStatementTypeDef",
    "ClientCheckCapacityRulesStatementTypeDef",
    "ClientCheckCapacityRulesVisibilityConfigTypeDef",
    "ClientCheckCapacityRulesTypeDef",
    "ClientCreateIpSetResponseSummaryTypeDef",
    "ClientCreateIpSetResponseTypeDef",
    "ClientCreateIpSetTagsTypeDef",
    "ClientCreateRegexPatternSetRegularExpressionListTypeDef",
    "ClientCreateRegexPatternSetResponseSummaryTypeDef",
    "ClientCreateRegexPatternSetResponseTypeDef",
    "ClientCreateRegexPatternSetTagsTypeDef",
    "ClientCreateRuleGroupResponseSummaryTypeDef",
    "ClientCreateRuleGroupResponseTypeDef",
    "ClientCreateRuleGroupRulesActionTypeDef",
    "ClientCreateRuleGroupRulesOverrideActionTypeDef",
    "ClientCreateRuleGroupRulesStatementAndStatementTypeDef",
    "ClientCreateRuleGroupRulesStatementByteMatchStatementFieldToMatchSingleHeaderTypeDef",
    "ClientCreateRuleGroupRulesStatementByteMatchStatementFieldToMatchSingleQueryArgumentTypeDef",
    "ClientCreateRuleGroupRulesStatementByteMatchStatementFieldToMatchTypeDef",
    "ClientCreateRuleGroupRulesStatementByteMatchStatementTextTransformationsTypeDef",
    "ClientCreateRuleGroupRulesStatementByteMatchStatementTypeDef",
    "ClientCreateRuleGroupRulesStatementGeoMatchStatementTypeDef",
    "ClientCreateRuleGroupRulesStatementIPSetReferenceStatementTypeDef",
    "ClientCreateRuleGroupRulesStatementManagedRuleGroupStatementExcludedRulesTypeDef",
    "ClientCreateRuleGroupRulesStatementManagedRuleGroupStatementTypeDef",
    "ClientCreateRuleGroupRulesStatementNotStatementTypeDef",
    "ClientCreateRuleGroupRulesStatementOrStatementTypeDef",
    "ClientCreateRuleGroupRulesStatementRateBasedStatementTypeDef",
    "ClientCreateRuleGroupRulesStatementRegexPatternSetReferenceStatementFieldToMatchSingleHeaderTypeDef",
    "ClientCreateRuleGroupRulesStatementRegexPatternSetReferenceStatementFieldToMatchSingleQueryArgumentTypeDef",
    "ClientCreateRuleGroupRulesStatementRegexPatternSetReferenceStatementFieldToMatchTypeDef",
    "ClientCreateRuleGroupRulesStatementRegexPatternSetReferenceStatementTextTransformationsTypeDef",
    "ClientCreateRuleGroupRulesStatementRegexPatternSetReferenceStatementTypeDef",
    "ClientCreateRuleGroupRulesStatementRuleGroupReferenceStatementExcludedRulesTypeDef",
    "ClientCreateRuleGroupRulesStatementRuleGroupReferenceStatementTypeDef",
    "ClientCreateRuleGroupRulesStatementSizeConstraintStatementFieldToMatchSingleHeaderTypeDef",
    "ClientCreateRuleGroupRulesStatementSizeConstraintStatementFieldToMatchSingleQueryArgumentTypeDef",
    "ClientCreateRuleGroupRulesStatementSizeConstraintStatementFieldToMatchTypeDef",
    "ClientCreateRuleGroupRulesStatementSizeConstraintStatementTextTransformationsTypeDef",
    "ClientCreateRuleGroupRulesStatementSizeConstraintStatementTypeDef",
    "ClientCreateRuleGroupRulesStatementSqliMatchStatementFieldToMatchSingleHeaderTypeDef",
    "ClientCreateRuleGroupRulesStatementSqliMatchStatementFieldToMatchSingleQueryArgumentTypeDef",
    "ClientCreateRuleGroupRulesStatementSqliMatchStatementFieldToMatchTypeDef",
    "ClientCreateRuleGroupRulesStatementSqliMatchStatementTextTransformationsTypeDef",
    "ClientCreateRuleGroupRulesStatementSqliMatchStatementTypeDef",
    "ClientCreateRuleGroupRulesStatementXssMatchStatementFieldToMatchSingleHeaderTypeDef",
    "ClientCreateRuleGroupRulesStatementXssMatchStatementFieldToMatchSingleQueryArgumentTypeDef",
    "ClientCreateRuleGroupRulesStatementXssMatchStatementFieldToMatchTypeDef",
    "ClientCreateRuleGroupRulesStatementXssMatchStatementTextTransformationsTypeDef",
    "ClientCreateRuleGroupRulesStatementXssMatchStatementTypeDef",
    "ClientCreateRuleGroupRulesStatementTypeDef",
    "ClientCreateRuleGroupRulesVisibilityConfigTypeDef",
    "ClientCreateRuleGroupRulesTypeDef",
    "ClientCreateRuleGroupTagsTypeDef",
    "ClientCreateRuleGroupVisibilityConfigTypeDef",
    "ClientCreateWebAclDefaultActionTypeDef",
    "ClientCreateWebAclResponseSummaryTypeDef",
    "ClientCreateWebAclResponseTypeDef",
    "ClientCreateWebAclRulesActionTypeDef",
    "ClientCreateWebAclRulesOverrideActionTypeDef",
    "ClientCreateWebAclRulesStatementAndStatementTypeDef",
    "ClientCreateWebAclRulesStatementByteMatchStatementFieldToMatchSingleHeaderTypeDef",
    "ClientCreateWebAclRulesStatementByteMatchStatementFieldToMatchSingleQueryArgumentTypeDef",
    "ClientCreateWebAclRulesStatementByteMatchStatementFieldToMatchTypeDef",
    "ClientCreateWebAclRulesStatementByteMatchStatementTextTransformationsTypeDef",
    "ClientCreateWebAclRulesStatementByteMatchStatementTypeDef",
    "ClientCreateWebAclRulesStatementGeoMatchStatementTypeDef",
    "ClientCreateWebAclRulesStatementIPSetReferenceStatementTypeDef",
    "ClientCreateWebAclRulesStatementManagedRuleGroupStatementExcludedRulesTypeDef",
    "ClientCreateWebAclRulesStatementManagedRuleGroupStatementTypeDef",
    "ClientCreateWebAclRulesStatementNotStatementTypeDef",
    "ClientCreateWebAclRulesStatementOrStatementTypeDef",
    "ClientCreateWebAclRulesStatementRateBasedStatementTypeDef",
    "ClientCreateWebAclRulesStatementRegexPatternSetReferenceStatementFieldToMatchSingleHeaderTypeDef",
    "ClientCreateWebAclRulesStatementRegexPatternSetReferenceStatementFieldToMatchSingleQueryArgumentTypeDef",
    "ClientCreateWebAclRulesStatementRegexPatternSetReferenceStatementFieldToMatchTypeDef",
    "ClientCreateWebAclRulesStatementRegexPatternSetReferenceStatementTextTransformationsTypeDef",
    "ClientCreateWebAclRulesStatementRegexPatternSetReferenceStatementTypeDef",
    "ClientCreateWebAclRulesStatementRuleGroupReferenceStatementExcludedRulesTypeDef",
    "ClientCreateWebAclRulesStatementRuleGroupReferenceStatementTypeDef",
    "ClientCreateWebAclRulesStatementSizeConstraintStatementFieldToMatchSingleHeaderTypeDef",
    "ClientCreateWebAclRulesStatementSizeConstraintStatementFieldToMatchSingleQueryArgumentTypeDef",
    "ClientCreateWebAclRulesStatementSizeConstraintStatementFieldToMatchTypeDef",
    "ClientCreateWebAclRulesStatementSizeConstraintStatementTextTransformationsTypeDef",
    "ClientCreateWebAclRulesStatementSizeConstraintStatementTypeDef",
    "ClientCreateWebAclRulesStatementSqliMatchStatementFieldToMatchSingleHeaderTypeDef",
    "ClientCreateWebAclRulesStatementSqliMatchStatementFieldToMatchSingleQueryArgumentTypeDef",
    "ClientCreateWebAclRulesStatementSqliMatchStatementFieldToMatchTypeDef",
    "ClientCreateWebAclRulesStatementSqliMatchStatementTextTransformationsTypeDef",
    "ClientCreateWebAclRulesStatementSqliMatchStatementTypeDef",
    "ClientCreateWebAclRulesStatementXssMatchStatementFieldToMatchSingleHeaderTypeDef",
    "ClientCreateWebAclRulesStatementXssMatchStatementFieldToMatchSingleQueryArgumentTypeDef",
    "ClientCreateWebAclRulesStatementXssMatchStatementFieldToMatchTypeDef",
    "ClientCreateWebAclRulesStatementXssMatchStatementTextTransformationsTypeDef",
    "ClientCreateWebAclRulesStatementXssMatchStatementTypeDef",
    "ClientCreateWebAclRulesStatementTypeDef",
    "ClientCreateWebAclRulesVisibilityConfigTypeDef",
    "ClientCreateWebAclRulesTypeDef",
    "ClientCreateWebAclTagsTypeDef",
    "ClientCreateWebAclVisibilityConfigTypeDef",
    "ClientDescribeManagedRuleGroupResponseRulesActionTypeDef",
    "ClientDescribeManagedRuleGroupResponseRulesTypeDef",
    "ClientDescribeManagedRuleGroupResponseTypeDef",
    "ClientGetIpSetResponseIPSetTypeDef",
    "ClientGetIpSetResponseTypeDef",
    "ClientGetLoggingConfigurationResponseLoggingConfigurationRedactedFieldsSingleHeaderTypeDef",
    "ClientGetLoggingConfigurationResponseLoggingConfigurationRedactedFieldsSingleQueryArgumentTypeDef",
    "ClientGetLoggingConfigurationResponseLoggingConfigurationRedactedFieldsTypeDef",
    "ClientGetLoggingConfigurationResponseLoggingConfigurationTypeDef",
    "ClientGetLoggingConfigurationResponseTypeDef",
    "ClientGetRateBasedStatementManagedKeysResponseManagedKeysIPV4TypeDef",
    "ClientGetRateBasedStatementManagedKeysResponseManagedKeysIPV6TypeDef",
    "ClientGetRateBasedStatementManagedKeysResponseTypeDef",
    "ClientGetRegexPatternSetResponseRegexPatternSetRegularExpressionListTypeDef",
    "ClientGetRegexPatternSetResponseRegexPatternSetTypeDef",
    "ClientGetRegexPatternSetResponseTypeDef",
    "ClientGetRuleGroupResponseRuleGroupRulesActionTypeDef",
    "ClientGetRuleGroupResponseRuleGroupRulesOverrideActionTypeDef",
    "ClientGetRuleGroupResponseRuleGroupRulesStatementAndStatementTypeDef",
    "ClientGetRuleGroupResponseRuleGroupRulesStatementByteMatchStatementFieldToMatchSingleHeaderTypeDef",
    "ClientGetRuleGroupResponseRuleGroupRulesStatementByteMatchStatementFieldToMatchSingleQueryArgumentTypeDef",
    "ClientGetRuleGroupResponseRuleGroupRulesStatementByteMatchStatementFieldToMatchTypeDef",
    "ClientGetRuleGroupResponseRuleGroupRulesStatementByteMatchStatementTextTransformationsTypeDef",
    "ClientGetRuleGroupResponseRuleGroupRulesStatementByteMatchStatementTypeDef",
    "ClientGetRuleGroupResponseRuleGroupRulesStatementGeoMatchStatementTypeDef",
    "ClientGetRuleGroupResponseRuleGroupRulesStatementIPSetReferenceStatementTypeDef",
    "ClientGetRuleGroupResponseRuleGroupRulesStatementManagedRuleGroupStatementExcludedRulesTypeDef",
    "ClientGetRuleGroupResponseRuleGroupRulesStatementManagedRuleGroupStatementTypeDef",
    "ClientGetRuleGroupResponseRuleGroupRulesStatementNotStatementTypeDef",
    "ClientGetRuleGroupResponseRuleGroupRulesStatementOrStatementTypeDef",
    "ClientGetRuleGroupResponseRuleGroupRulesStatementRateBasedStatementTypeDef",
    "ClientGetRuleGroupResponseRuleGroupRulesStatementRegexPatternSetReferenceStatementFieldToMatchSingleHeaderTypeDef",
    "ClientGetRuleGroupResponseRuleGroupRulesStatementRegexPatternSetReferenceStatementFieldToMatchSingleQueryArgumentTypeDef",
    "ClientGetRuleGroupResponseRuleGroupRulesStatementRegexPatternSetReferenceStatementFieldToMatchTypeDef",
    "ClientGetRuleGroupResponseRuleGroupRulesStatementRegexPatternSetReferenceStatementTextTransformationsTypeDef",
    "ClientGetRuleGroupResponseRuleGroupRulesStatementRegexPatternSetReferenceStatementTypeDef",
    "ClientGetRuleGroupResponseRuleGroupRulesStatementRuleGroupReferenceStatementExcludedRulesTypeDef",
    "ClientGetRuleGroupResponseRuleGroupRulesStatementRuleGroupReferenceStatementTypeDef",
    "ClientGetRuleGroupResponseRuleGroupRulesStatementSizeConstraintStatementFieldToMatchSingleHeaderTypeDef",
    "ClientGetRuleGroupResponseRuleGroupRulesStatementSizeConstraintStatementFieldToMatchSingleQueryArgumentTypeDef",
    "ClientGetRuleGroupResponseRuleGroupRulesStatementSizeConstraintStatementFieldToMatchTypeDef",
    "ClientGetRuleGroupResponseRuleGroupRulesStatementSizeConstraintStatementTextTransformationsTypeDef",
    "ClientGetRuleGroupResponseRuleGroupRulesStatementSizeConstraintStatementTypeDef",
    "ClientGetRuleGroupResponseRuleGroupRulesStatementSqliMatchStatementFieldToMatchSingleHeaderTypeDef",
    "ClientGetRuleGroupResponseRuleGroupRulesStatementSqliMatchStatementFieldToMatchSingleQueryArgumentTypeDef",
    "ClientGetRuleGroupResponseRuleGroupRulesStatementSqliMatchStatementFieldToMatchTypeDef",
    "ClientGetRuleGroupResponseRuleGroupRulesStatementSqliMatchStatementTextTransformationsTypeDef",
    "ClientGetRuleGroupResponseRuleGroupRulesStatementSqliMatchStatementTypeDef",
    "ClientGetRuleGroupResponseRuleGroupRulesStatementXssMatchStatementFieldToMatchSingleHeaderTypeDef",
    "ClientGetRuleGroupResponseRuleGroupRulesStatementXssMatchStatementFieldToMatchSingleQueryArgumentTypeDef",
    "ClientGetRuleGroupResponseRuleGroupRulesStatementXssMatchStatementFieldToMatchTypeDef",
    "ClientGetRuleGroupResponseRuleGroupRulesStatementXssMatchStatementTextTransformationsTypeDef",
    "ClientGetRuleGroupResponseRuleGroupRulesStatementXssMatchStatementTypeDef",
    "ClientGetRuleGroupResponseRuleGroupRulesStatementTypeDef",
    "ClientGetRuleGroupResponseRuleGroupRulesVisibilityConfigTypeDef",
    "ClientGetRuleGroupResponseRuleGroupRulesTypeDef",
    "ClientGetRuleGroupResponseRuleGroupVisibilityConfigTypeDef",
    "ClientGetRuleGroupResponseRuleGroupTypeDef",
    "ClientGetRuleGroupResponseTypeDef",
    "ClientGetSampledRequestsResponseSampledRequestsRequestHeadersTypeDef",
    "ClientGetSampledRequestsResponseSampledRequestsRequestTypeDef",
    "ClientGetSampledRequestsResponseSampledRequestsTypeDef",
    "ClientGetSampledRequestsResponseTimeWindowTypeDef",
    "ClientGetSampledRequestsResponseTypeDef",
    "ClientGetSampledRequestsTimeWindowTypeDef",
    "ClientGetWebAclForResourceResponseWebACLDefaultActionTypeDef",
    "ClientGetWebAclForResourceResponseWebACLRulesActionTypeDef",
    "ClientGetWebAclForResourceResponseWebACLRulesOverrideActionTypeDef",
    "ClientGetWebAclForResourceResponseWebACLRulesStatementAndStatementTypeDef",
    "ClientGetWebAclForResourceResponseWebACLRulesStatementByteMatchStatementFieldToMatchSingleHeaderTypeDef",
    "ClientGetWebAclForResourceResponseWebACLRulesStatementByteMatchStatementFieldToMatchSingleQueryArgumentTypeDef",
    "ClientGetWebAclForResourceResponseWebACLRulesStatementByteMatchStatementFieldToMatchTypeDef",
    "ClientGetWebAclForResourceResponseWebACLRulesStatementByteMatchStatementTextTransformationsTypeDef",
    "ClientGetWebAclForResourceResponseWebACLRulesStatementByteMatchStatementTypeDef",
    "ClientGetWebAclForResourceResponseWebACLRulesStatementGeoMatchStatementTypeDef",
    "ClientGetWebAclForResourceResponseWebACLRulesStatementIPSetReferenceStatementTypeDef",
    "ClientGetWebAclForResourceResponseWebACLRulesStatementManagedRuleGroupStatementExcludedRulesTypeDef",
    "ClientGetWebAclForResourceResponseWebACLRulesStatementManagedRuleGroupStatementTypeDef",
    "ClientGetWebAclForResourceResponseWebACLRulesStatementNotStatementTypeDef",
    "ClientGetWebAclForResourceResponseWebACLRulesStatementOrStatementTypeDef",
    "ClientGetWebAclForResourceResponseWebACLRulesStatementRateBasedStatementTypeDef",
    "ClientGetWebAclForResourceResponseWebACLRulesStatementRegexPatternSetReferenceStatementFieldToMatchSingleHeaderTypeDef",
    "ClientGetWebAclForResourceResponseWebACLRulesStatementRegexPatternSetReferenceStatementFieldToMatchSingleQueryArgumentTypeDef",
    "ClientGetWebAclForResourceResponseWebACLRulesStatementRegexPatternSetReferenceStatementFieldToMatchTypeDef",
    "ClientGetWebAclForResourceResponseWebACLRulesStatementRegexPatternSetReferenceStatementTextTransformationsTypeDef",
    "ClientGetWebAclForResourceResponseWebACLRulesStatementRegexPatternSetReferenceStatementTypeDef",
    "ClientGetWebAclForResourceResponseWebACLRulesStatementRuleGroupReferenceStatementExcludedRulesTypeDef",
    "ClientGetWebAclForResourceResponseWebACLRulesStatementRuleGroupReferenceStatementTypeDef",
    "ClientGetWebAclForResourceResponseWebACLRulesStatementSizeConstraintStatementFieldToMatchSingleHeaderTypeDef",
    "ClientGetWebAclForResourceResponseWebACLRulesStatementSizeConstraintStatementFieldToMatchSingleQueryArgumentTypeDef",
    "ClientGetWebAclForResourceResponseWebACLRulesStatementSizeConstraintStatementFieldToMatchTypeDef",
    "ClientGetWebAclForResourceResponseWebACLRulesStatementSizeConstraintStatementTextTransformationsTypeDef",
    "ClientGetWebAclForResourceResponseWebACLRulesStatementSizeConstraintStatementTypeDef",
    "ClientGetWebAclForResourceResponseWebACLRulesStatementSqliMatchStatementFieldToMatchSingleHeaderTypeDef",
    "ClientGetWebAclForResourceResponseWebACLRulesStatementSqliMatchStatementFieldToMatchSingleQueryArgumentTypeDef",
    "ClientGetWebAclForResourceResponseWebACLRulesStatementSqliMatchStatementFieldToMatchTypeDef",
    "ClientGetWebAclForResourceResponseWebACLRulesStatementSqliMatchStatementTextTransformationsTypeDef",
    "ClientGetWebAclForResourceResponseWebACLRulesStatementSqliMatchStatementTypeDef",
    "ClientGetWebAclForResourceResponseWebACLRulesStatementXssMatchStatementFieldToMatchSingleHeaderTypeDef",
    "ClientGetWebAclForResourceResponseWebACLRulesStatementXssMatchStatementFieldToMatchSingleQueryArgumentTypeDef",
    "ClientGetWebAclForResourceResponseWebACLRulesStatementXssMatchStatementFieldToMatchTypeDef",
    "ClientGetWebAclForResourceResponseWebACLRulesStatementXssMatchStatementTextTransformationsTypeDef",
    "ClientGetWebAclForResourceResponseWebACLRulesStatementXssMatchStatementTypeDef",
    "ClientGetWebAclForResourceResponseWebACLRulesStatementTypeDef",
    "ClientGetWebAclForResourceResponseWebACLRulesVisibilityConfigTypeDef",
    "ClientGetWebAclForResourceResponseWebACLRulesTypeDef",
    "ClientGetWebAclForResourceResponseWebACLVisibilityConfigTypeDef",
    "ClientGetWebAclForResourceResponseWebACLTypeDef",
    "ClientGetWebAclForResourceResponseTypeDef",
    "ClientGetWebAclResponseWebACLDefaultActionTypeDef",
    "ClientGetWebAclResponseWebACLRulesActionTypeDef",
    "ClientGetWebAclResponseWebACLRulesOverrideActionTypeDef",
    "ClientGetWebAclResponseWebACLRulesStatementAndStatementTypeDef",
    "ClientGetWebAclResponseWebACLRulesStatementByteMatchStatementFieldToMatchSingleHeaderTypeDef",
    "ClientGetWebAclResponseWebACLRulesStatementByteMatchStatementFieldToMatchSingleQueryArgumentTypeDef",
    "ClientGetWebAclResponseWebACLRulesStatementByteMatchStatementFieldToMatchTypeDef",
    "ClientGetWebAclResponseWebACLRulesStatementByteMatchStatementTextTransformationsTypeDef",
    "ClientGetWebAclResponseWebACLRulesStatementByteMatchStatementTypeDef",
    "ClientGetWebAclResponseWebACLRulesStatementGeoMatchStatementTypeDef",
    "ClientGetWebAclResponseWebACLRulesStatementIPSetReferenceStatementTypeDef",
    "ClientGetWebAclResponseWebACLRulesStatementManagedRuleGroupStatementExcludedRulesTypeDef",
    "ClientGetWebAclResponseWebACLRulesStatementManagedRuleGroupStatementTypeDef",
    "ClientGetWebAclResponseWebACLRulesStatementNotStatementTypeDef",
    "ClientGetWebAclResponseWebACLRulesStatementOrStatementTypeDef",
    "ClientGetWebAclResponseWebACLRulesStatementRateBasedStatementTypeDef",
    "ClientGetWebAclResponseWebACLRulesStatementRegexPatternSetReferenceStatementFieldToMatchSingleHeaderTypeDef",
    "ClientGetWebAclResponseWebACLRulesStatementRegexPatternSetReferenceStatementFieldToMatchSingleQueryArgumentTypeDef",
    "ClientGetWebAclResponseWebACLRulesStatementRegexPatternSetReferenceStatementFieldToMatchTypeDef",
    "ClientGetWebAclResponseWebACLRulesStatementRegexPatternSetReferenceStatementTextTransformationsTypeDef",
    "ClientGetWebAclResponseWebACLRulesStatementRegexPatternSetReferenceStatementTypeDef",
    "ClientGetWebAclResponseWebACLRulesStatementRuleGroupReferenceStatementExcludedRulesTypeDef",
    "ClientGetWebAclResponseWebACLRulesStatementRuleGroupReferenceStatementTypeDef",
    "ClientGetWebAclResponseWebACLRulesStatementSizeConstraintStatementFieldToMatchSingleHeaderTypeDef",
    "ClientGetWebAclResponseWebACLRulesStatementSizeConstraintStatementFieldToMatchSingleQueryArgumentTypeDef",
    "ClientGetWebAclResponseWebACLRulesStatementSizeConstraintStatementFieldToMatchTypeDef",
    "ClientGetWebAclResponseWebACLRulesStatementSizeConstraintStatementTextTransformationsTypeDef",
    "ClientGetWebAclResponseWebACLRulesStatementSizeConstraintStatementTypeDef",
    "ClientGetWebAclResponseWebACLRulesStatementSqliMatchStatementFieldToMatchSingleHeaderTypeDef",
    "ClientGetWebAclResponseWebACLRulesStatementSqliMatchStatementFieldToMatchSingleQueryArgumentTypeDef",
    "ClientGetWebAclResponseWebACLRulesStatementSqliMatchStatementFieldToMatchTypeDef",
    "ClientGetWebAclResponseWebACLRulesStatementSqliMatchStatementTextTransformationsTypeDef",
    "ClientGetWebAclResponseWebACLRulesStatementSqliMatchStatementTypeDef",
    "ClientGetWebAclResponseWebACLRulesStatementXssMatchStatementFieldToMatchSingleHeaderTypeDef",
    "ClientGetWebAclResponseWebACLRulesStatementXssMatchStatementFieldToMatchSingleQueryArgumentTypeDef",
    "ClientGetWebAclResponseWebACLRulesStatementXssMatchStatementFieldToMatchTypeDef",
    "ClientGetWebAclResponseWebACLRulesStatementXssMatchStatementTextTransformationsTypeDef",
    "ClientGetWebAclResponseWebACLRulesStatementXssMatchStatementTypeDef",
    "ClientGetWebAclResponseWebACLRulesStatementTypeDef",
    "ClientGetWebAclResponseWebACLRulesVisibilityConfigTypeDef",
    "ClientGetWebAclResponseWebACLRulesTypeDef",
    "ClientGetWebAclResponseWebACLVisibilityConfigTypeDef",
    "ClientGetWebAclResponseWebACLTypeDef",
    "ClientGetWebAclResponseTypeDef",
    "ClientListAvailableManagedRuleGroupsResponseManagedRuleGroupsTypeDef",
    "ClientListAvailableManagedRuleGroupsResponseTypeDef",
    "ClientListIpSetsResponseIPSetsTypeDef",
    "ClientListIpSetsResponseTypeDef",
    "ClientListLoggingConfigurationsResponseLoggingConfigurationsRedactedFieldsSingleHeaderTypeDef",
    "ClientListLoggingConfigurationsResponseLoggingConfigurationsRedactedFieldsSingleQueryArgumentTypeDef",
    "ClientListLoggingConfigurationsResponseLoggingConfigurationsRedactedFieldsTypeDef",
    "ClientListLoggingConfigurationsResponseLoggingConfigurationsTypeDef",
    "ClientListLoggingConfigurationsResponseTypeDef",
    "ClientListRegexPatternSetsResponseRegexPatternSetsTypeDef",
    "ClientListRegexPatternSetsResponseTypeDef",
    "ClientListResourcesForWebAclResponseTypeDef",
    "ClientListRuleGroupsResponseRuleGroupsTypeDef",
    "ClientListRuleGroupsResponseTypeDef",
    "ClientListTagsForResourceResponseTagInfoForResourceTagListTypeDef",
    "ClientListTagsForResourceResponseTagInfoForResourceTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientListWebAclsResponseWebACLsTypeDef",
    "ClientListWebAclsResponseTypeDef",
    "ClientPutLoggingConfigurationLoggingConfigurationRedactedFieldsSingleHeaderTypeDef",
    "ClientPutLoggingConfigurationLoggingConfigurationRedactedFieldsSingleQueryArgumentTypeDef",
    "ClientPutLoggingConfigurationLoggingConfigurationRedactedFieldsTypeDef",
    "ClientPutLoggingConfigurationLoggingConfigurationTypeDef",
    "ClientPutLoggingConfigurationResponseLoggingConfigurationRedactedFieldsSingleHeaderTypeDef",
    "ClientPutLoggingConfigurationResponseLoggingConfigurationRedactedFieldsSingleQueryArgumentTypeDef",
    "ClientPutLoggingConfigurationResponseLoggingConfigurationRedactedFieldsTypeDef",
    "ClientPutLoggingConfigurationResponseLoggingConfigurationTypeDef",
    "ClientPutLoggingConfigurationResponseTypeDef",
    "ClientTagResourceTagsTypeDef",
    "ClientUpdateIpSetResponseTypeDef",
    "ClientUpdateRegexPatternSetRegularExpressionListTypeDef",
    "ClientUpdateRegexPatternSetResponseTypeDef",
    "ClientUpdateRuleGroupResponseTypeDef",
    "ClientUpdateRuleGroupRulesActionTypeDef",
    "ClientUpdateRuleGroupRulesOverrideActionTypeDef",
    "ClientUpdateRuleGroupRulesStatementAndStatementTypeDef",
    "ClientUpdateRuleGroupRulesStatementByteMatchStatementFieldToMatchSingleHeaderTypeDef",
    "ClientUpdateRuleGroupRulesStatementByteMatchStatementFieldToMatchSingleQueryArgumentTypeDef",
    "ClientUpdateRuleGroupRulesStatementByteMatchStatementFieldToMatchTypeDef",
    "ClientUpdateRuleGroupRulesStatementByteMatchStatementTextTransformationsTypeDef",
    "ClientUpdateRuleGroupRulesStatementByteMatchStatementTypeDef",
    "ClientUpdateRuleGroupRulesStatementGeoMatchStatementTypeDef",
    "ClientUpdateRuleGroupRulesStatementIPSetReferenceStatementTypeDef",
    "ClientUpdateRuleGroupRulesStatementManagedRuleGroupStatementExcludedRulesTypeDef",
    "ClientUpdateRuleGroupRulesStatementManagedRuleGroupStatementTypeDef",
    "ClientUpdateRuleGroupRulesStatementNotStatementTypeDef",
    "ClientUpdateRuleGroupRulesStatementOrStatementTypeDef",
    "ClientUpdateRuleGroupRulesStatementRateBasedStatementTypeDef",
    "ClientUpdateRuleGroupRulesStatementRegexPatternSetReferenceStatementFieldToMatchSingleHeaderTypeDef",
    "ClientUpdateRuleGroupRulesStatementRegexPatternSetReferenceStatementFieldToMatchSingleQueryArgumentTypeDef",
    "ClientUpdateRuleGroupRulesStatementRegexPatternSetReferenceStatementFieldToMatchTypeDef",
    "ClientUpdateRuleGroupRulesStatementRegexPatternSetReferenceStatementTextTransformationsTypeDef",
    "ClientUpdateRuleGroupRulesStatementRegexPatternSetReferenceStatementTypeDef",
    "ClientUpdateRuleGroupRulesStatementRuleGroupReferenceStatementExcludedRulesTypeDef",
    "ClientUpdateRuleGroupRulesStatementRuleGroupReferenceStatementTypeDef",
    "ClientUpdateRuleGroupRulesStatementSizeConstraintStatementFieldToMatchSingleHeaderTypeDef",
    "ClientUpdateRuleGroupRulesStatementSizeConstraintStatementFieldToMatchSingleQueryArgumentTypeDef",
    "ClientUpdateRuleGroupRulesStatementSizeConstraintStatementFieldToMatchTypeDef",
    "ClientUpdateRuleGroupRulesStatementSizeConstraintStatementTextTransformationsTypeDef",
    "ClientUpdateRuleGroupRulesStatementSizeConstraintStatementTypeDef",
    "ClientUpdateRuleGroupRulesStatementSqliMatchStatementFieldToMatchSingleHeaderTypeDef",
    "ClientUpdateRuleGroupRulesStatementSqliMatchStatementFieldToMatchSingleQueryArgumentTypeDef",
    "ClientUpdateRuleGroupRulesStatementSqliMatchStatementFieldToMatchTypeDef",
    "ClientUpdateRuleGroupRulesStatementSqliMatchStatementTextTransformationsTypeDef",
    "ClientUpdateRuleGroupRulesStatementSqliMatchStatementTypeDef",
    "ClientUpdateRuleGroupRulesStatementXssMatchStatementFieldToMatchSingleHeaderTypeDef",
    "ClientUpdateRuleGroupRulesStatementXssMatchStatementFieldToMatchSingleQueryArgumentTypeDef",
    "ClientUpdateRuleGroupRulesStatementXssMatchStatementFieldToMatchTypeDef",
    "ClientUpdateRuleGroupRulesStatementXssMatchStatementTextTransformationsTypeDef",
    "ClientUpdateRuleGroupRulesStatementXssMatchStatementTypeDef",
    "ClientUpdateRuleGroupRulesStatementTypeDef",
    "ClientUpdateRuleGroupRulesVisibilityConfigTypeDef",
    "ClientUpdateRuleGroupRulesTypeDef",
    "ClientUpdateRuleGroupVisibilityConfigTypeDef",
    "ClientUpdateWebAclDefaultActionTypeDef",
    "ClientUpdateWebAclResponseTypeDef",
    "ClientUpdateWebAclRulesActionTypeDef",
    "ClientUpdateWebAclRulesOverrideActionTypeDef",
    "ClientUpdateWebAclRulesStatementAndStatementTypeDef",
    "ClientUpdateWebAclRulesStatementByteMatchStatementFieldToMatchSingleHeaderTypeDef",
    "ClientUpdateWebAclRulesStatementByteMatchStatementFieldToMatchSingleQueryArgumentTypeDef",
    "ClientUpdateWebAclRulesStatementByteMatchStatementFieldToMatchTypeDef",
    "ClientUpdateWebAclRulesStatementByteMatchStatementTextTransformationsTypeDef",
    "ClientUpdateWebAclRulesStatementByteMatchStatementTypeDef",
    "ClientUpdateWebAclRulesStatementGeoMatchStatementTypeDef",
    "ClientUpdateWebAclRulesStatementIPSetReferenceStatementTypeDef",
    "ClientUpdateWebAclRulesStatementManagedRuleGroupStatementExcludedRulesTypeDef",
    "ClientUpdateWebAclRulesStatementManagedRuleGroupStatementTypeDef",
    "ClientUpdateWebAclRulesStatementNotStatementTypeDef",
    "ClientUpdateWebAclRulesStatementOrStatementTypeDef",
    "ClientUpdateWebAclRulesStatementRateBasedStatementTypeDef",
    "ClientUpdateWebAclRulesStatementRegexPatternSetReferenceStatementFieldToMatchSingleHeaderTypeDef",
    "ClientUpdateWebAclRulesStatementRegexPatternSetReferenceStatementFieldToMatchSingleQueryArgumentTypeDef",
    "ClientUpdateWebAclRulesStatementRegexPatternSetReferenceStatementFieldToMatchTypeDef",
    "ClientUpdateWebAclRulesStatementRegexPatternSetReferenceStatementTextTransformationsTypeDef",
    "ClientUpdateWebAclRulesStatementRegexPatternSetReferenceStatementTypeDef",
    "ClientUpdateWebAclRulesStatementRuleGroupReferenceStatementExcludedRulesTypeDef",
    "ClientUpdateWebAclRulesStatementRuleGroupReferenceStatementTypeDef",
    "ClientUpdateWebAclRulesStatementSizeConstraintStatementFieldToMatchSingleHeaderTypeDef",
    "ClientUpdateWebAclRulesStatementSizeConstraintStatementFieldToMatchSingleQueryArgumentTypeDef",
    "ClientUpdateWebAclRulesStatementSizeConstraintStatementFieldToMatchTypeDef",
    "ClientUpdateWebAclRulesStatementSizeConstraintStatementTextTransformationsTypeDef",
    "ClientUpdateWebAclRulesStatementSizeConstraintStatementTypeDef",
    "ClientUpdateWebAclRulesStatementSqliMatchStatementFieldToMatchSingleHeaderTypeDef",
    "ClientUpdateWebAclRulesStatementSqliMatchStatementFieldToMatchSingleQueryArgumentTypeDef",
    "ClientUpdateWebAclRulesStatementSqliMatchStatementFieldToMatchTypeDef",
    "ClientUpdateWebAclRulesStatementSqliMatchStatementTextTransformationsTypeDef",
    "ClientUpdateWebAclRulesStatementSqliMatchStatementTypeDef",
    "ClientUpdateWebAclRulesStatementXssMatchStatementFieldToMatchSingleHeaderTypeDef",
    "ClientUpdateWebAclRulesStatementXssMatchStatementFieldToMatchSingleQueryArgumentTypeDef",
    "ClientUpdateWebAclRulesStatementXssMatchStatementFieldToMatchTypeDef",
    "ClientUpdateWebAclRulesStatementXssMatchStatementTextTransformationsTypeDef",
    "ClientUpdateWebAclRulesStatementXssMatchStatementTypeDef",
    "ClientUpdateWebAclRulesStatementTypeDef",
    "ClientUpdateWebAclRulesVisibilityConfigTypeDef",
    "ClientUpdateWebAclRulesTypeDef",
    "ClientUpdateWebAclVisibilityConfigTypeDef",
)

ClientCheckCapacityResponseTypeDef = TypedDict(
    "ClientCheckCapacityResponseTypeDef", {"Capacity": int}, total=False
)

ClientCheckCapacityRulesActionTypeDef = TypedDict(
    "ClientCheckCapacityRulesActionTypeDef",
    {"Block": Dict[str, Any], "Allow": Dict[str, Any], "Count": Dict[str, Any]},
    total=False,
)

ClientCheckCapacityRulesOverrideActionTypeDef = TypedDict(
    "ClientCheckCapacityRulesOverrideActionTypeDef",
    {"Count": Dict[str, Any], "None": Dict[str, Any]},
    total=False,
)

ClientCheckCapacityRulesStatementAndStatementTypeDef = TypedDict(
    "ClientCheckCapacityRulesStatementAndStatementTypeDef", {"Statements": List[Any]}, total=False
)

ClientCheckCapacityRulesStatementByteMatchStatementFieldToMatchSingleHeaderTypeDef = TypedDict(
    "ClientCheckCapacityRulesStatementByteMatchStatementFieldToMatchSingleHeaderTypeDef",
    {"Name": str},
    total=False,
)

ClientCheckCapacityRulesStatementByteMatchStatementFieldToMatchSingleQueryArgumentTypeDef = TypedDict(
    "ClientCheckCapacityRulesStatementByteMatchStatementFieldToMatchSingleQueryArgumentTypeDef",
    {"Name": str},
    total=False,
)

ClientCheckCapacityRulesStatementByteMatchStatementFieldToMatchTypeDef = TypedDict(
    "ClientCheckCapacityRulesStatementByteMatchStatementFieldToMatchTypeDef",
    {
        "SingleHeader": ClientCheckCapacityRulesStatementByteMatchStatementFieldToMatchSingleHeaderTypeDef,
        "SingleQueryArgument": ClientCheckCapacityRulesStatementByteMatchStatementFieldToMatchSingleQueryArgumentTypeDef,
        "AllQueryArguments": Dict[str, Any],
        "UriPath": Dict[str, Any],
        "QueryString": Dict[str, Any],
        "Body": Dict[str, Any],
        "Method": Dict[str, Any],
    },
    total=False,
)

ClientCheckCapacityRulesStatementByteMatchStatementTextTransformationsTypeDef = TypedDict(
    "ClientCheckCapacityRulesStatementByteMatchStatementTextTransformationsTypeDef",
    {
        "Priority": int,
        "Type": Literal[
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

ClientCheckCapacityRulesStatementByteMatchStatementTypeDef = TypedDict(
    "ClientCheckCapacityRulesStatementByteMatchStatementTypeDef",
    {
        "SearchString": bytes,
        "FieldToMatch": ClientCheckCapacityRulesStatementByteMatchStatementFieldToMatchTypeDef,
        "TextTransformations": List[
            ClientCheckCapacityRulesStatementByteMatchStatementTextTransformationsTypeDef
        ],
        "PositionalConstraint": Literal[
            "EXACTLY", "STARTS_WITH", "ENDS_WITH", "CONTAINS", "CONTAINS_WORD"
        ],
    },
    total=False,
)

ClientCheckCapacityRulesStatementGeoMatchStatementTypeDef = TypedDict(
    "ClientCheckCapacityRulesStatementGeoMatchStatementTypeDef",
    {
        "CountryCodes": List[
            Literal[
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
            ]
        ]
    },
    total=False,
)

ClientCheckCapacityRulesStatementIPSetReferenceStatementTypeDef = TypedDict(
    "ClientCheckCapacityRulesStatementIPSetReferenceStatementTypeDef", {"ARN": str}, total=False
)

ClientCheckCapacityRulesStatementManagedRuleGroupStatementExcludedRulesTypeDef = TypedDict(
    "ClientCheckCapacityRulesStatementManagedRuleGroupStatementExcludedRulesTypeDef",
    {"Name": str},
    total=False,
)

ClientCheckCapacityRulesStatementManagedRuleGroupStatementTypeDef = TypedDict(
    "ClientCheckCapacityRulesStatementManagedRuleGroupStatementTypeDef",
    {
        "VendorName": str,
        "Name": str,
        "ExcludedRules": List[
            ClientCheckCapacityRulesStatementManagedRuleGroupStatementExcludedRulesTypeDef
        ],
    },
    total=False,
)

ClientCheckCapacityRulesStatementNotStatementTypeDef = TypedDict(
    "ClientCheckCapacityRulesStatementNotStatementTypeDef", {"Statement": Any}, total=False
)

ClientCheckCapacityRulesStatementOrStatementTypeDef = TypedDict(
    "ClientCheckCapacityRulesStatementOrStatementTypeDef", {"Statements": List[Any]}, total=False
)

ClientCheckCapacityRulesStatementRateBasedStatementTypeDef = TypedDict(
    "ClientCheckCapacityRulesStatementRateBasedStatementTypeDef",
    {"Limit": int, "AggregateKeyType": str, "ScopeDownStatement": Any},
    total=False,
)

ClientCheckCapacityRulesStatementRegexPatternSetReferenceStatementFieldToMatchSingleHeaderTypeDef = TypedDict(
    "ClientCheckCapacityRulesStatementRegexPatternSetReferenceStatementFieldToMatchSingleHeaderTypeDef",
    {"Name": str},
    total=False,
)

ClientCheckCapacityRulesStatementRegexPatternSetReferenceStatementFieldToMatchSingleQueryArgumentTypeDef = TypedDict(
    "ClientCheckCapacityRulesStatementRegexPatternSetReferenceStatementFieldToMatchSingleQueryArgumentTypeDef",
    {"Name": str},
    total=False,
)

ClientCheckCapacityRulesStatementRegexPatternSetReferenceStatementFieldToMatchTypeDef = TypedDict(
    "ClientCheckCapacityRulesStatementRegexPatternSetReferenceStatementFieldToMatchTypeDef",
    {
        "SingleHeader": ClientCheckCapacityRulesStatementRegexPatternSetReferenceStatementFieldToMatchSingleHeaderTypeDef,
        "SingleQueryArgument": ClientCheckCapacityRulesStatementRegexPatternSetReferenceStatementFieldToMatchSingleQueryArgumentTypeDef,
        "AllQueryArguments": Dict[str, Any],
        "UriPath": Dict[str, Any],
        "QueryString": Dict[str, Any],
        "Body": Dict[str, Any],
        "Method": Dict[str, Any],
    },
    total=False,
)

ClientCheckCapacityRulesStatementRegexPatternSetReferenceStatementTextTransformationsTypeDef = TypedDict(
    "ClientCheckCapacityRulesStatementRegexPatternSetReferenceStatementTextTransformationsTypeDef",
    {
        "Priority": int,
        "Type": Literal[
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

ClientCheckCapacityRulesStatementRegexPatternSetReferenceStatementTypeDef = TypedDict(
    "ClientCheckCapacityRulesStatementRegexPatternSetReferenceStatementTypeDef",
    {
        "ARN": str,
        "FieldToMatch": ClientCheckCapacityRulesStatementRegexPatternSetReferenceStatementFieldToMatchTypeDef,
        "TextTransformations": List[
            ClientCheckCapacityRulesStatementRegexPatternSetReferenceStatementTextTransformationsTypeDef
        ],
    },
    total=False,
)

ClientCheckCapacityRulesStatementRuleGroupReferenceStatementExcludedRulesTypeDef = TypedDict(
    "ClientCheckCapacityRulesStatementRuleGroupReferenceStatementExcludedRulesTypeDef",
    {"Name": str},
    total=False,
)

ClientCheckCapacityRulesStatementRuleGroupReferenceStatementTypeDef = TypedDict(
    "ClientCheckCapacityRulesStatementRuleGroupReferenceStatementTypeDef",
    {
        "ARN": str,
        "ExcludedRules": List[
            ClientCheckCapacityRulesStatementRuleGroupReferenceStatementExcludedRulesTypeDef
        ],
    },
    total=False,
)

ClientCheckCapacityRulesStatementSizeConstraintStatementFieldToMatchSingleHeaderTypeDef = TypedDict(
    "ClientCheckCapacityRulesStatementSizeConstraintStatementFieldToMatchSingleHeaderTypeDef",
    {"Name": str},
    total=False,
)

ClientCheckCapacityRulesStatementSizeConstraintStatementFieldToMatchSingleQueryArgumentTypeDef = TypedDict(
    "ClientCheckCapacityRulesStatementSizeConstraintStatementFieldToMatchSingleQueryArgumentTypeDef",
    {"Name": str},
    total=False,
)

ClientCheckCapacityRulesStatementSizeConstraintStatementFieldToMatchTypeDef = TypedDict(
    "ClientCheckCapacityRulesStatementSizeConstraintStatementFieldToMatchTypeDef",
    {
        "SingleHeader": ClientCheckCapacityRulesStatementSizeConstraintStatementFieldToMatchSingleHeaderTypeDef,
        "SingleQueryArgument": ClientCheckCapacityRulesStatementSizeConstraintStatementFieldToMatchSingleQueryArgumentTypeDef,
        "AllQueryArguments": Dict[str, Any],
        "UriPath": Dict[str, Any],
        "QueryString": Dict[str, Any],
        "Body": Dict[str, Any],
        "Method": Dict[str, Any],
    },
    total=False,
)

ClientCheckCapacityRulesStatementSizeConstraintStatementTextTransformationsTypeDef = TypedDict(
    "ClientCheckCapacityRulesStatementSizeConstraintStatementTextTransformationsTypeDef",
    {
        "Priority": int,
        "Type": Literal[
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

ClientCheckCapacityRulesStatementSizeConstraintStatementTypeDef = TypedDict(
    "ClientCheckCapacityRulesStatementSizeConstraintStatementTypeDef",
    {
        "FieldToMatch": ClientCheckCapacityRulesStatementSizeConstraintStatementFieldToMatchTypeDef,
        "ComparisonOperator": Literal["EQ", "NE", "LE", "LT", "GE", "GT"],
        "Size": int,
        "TextTransformations": List[
            ClientCheckCapacityRulesStatementSizeConstraintStatementTextTransformationsTypeDef
        ],
    },
    total=False,
)

ClientCheckCapacityRulesStatementSqliMatchStatementFieldToMatchSingleHeaderTypeDef = TypedDict(
    "ClientCheckCapacityRulesStatementSqliMatchStatementFieldToMatchSingleHeaderTypeDef",
    {"Name": str},
    total=False,
)

ClientCheckCapacityRulesStatementSqliMatchStatementFieldToMatchSingleQueryArgumentTypeDef = TypedDict(
    "ClientCheckCapacityRulesStatementSqliMatchStatementFieldToMatchSingleQueryArgumentTypeDef",
    {"Name": str},
    total=False,
)

ClientCheckCapacityRulesStatementSqliMatchStatementFieldToMatchTypeDef = TypedDict(
    "ClientCheckCapacityRulesStatementSqliMatchStatementFieldToMatchTypeDef",
    {
        "SingleHeader": ClientCheckCapacityRulesStatementSqliMatchStatementFieldToMatchSingleHeaderTypeDef,
        "SingleQueryArgument": ClientCheckCapacityRulesStatementSqliMatchStatementFieldToMatchSingleQueryArgumentTypeDef,
        "AllQueryArguments": Dict[str, Any],
        "UriPath": Dict[str, Any],
        "QueryString": Dict[str, Any],
        "Body": Dict[str, Any],
        "Method": Dict[str, Any],
    },
    total=False,
)

ClientCheckCapacityRulesStatementSqliMatchStatementTextTransformationsTypeDef = TypedDict(
    "ClientCheckCapacityRulesStatementSqliMatchStatementTextTransformationsTypeDef",
    {
        "Priority": int,
        "Type": Literal[
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

ClientCheckCapacityRulesStatementSqliMatchStatementTypeDef = TypedDict(
    "ClientCheckCapacityRulesStatementSqliMatchStatementTypeDef",
    {
        "FieldToMatch": ClientCheckCapacityRulesStatementSqliMatchStatementFieldToMatchTypeDef,
        "TextTransformations": List[
            ClientCheckCapacityRulesStatementSqliMatchStatementTextTransformationsTypeDef
        ],
    },
    total=False,
)

ClientCheckCapacityRulesStatementXssMatchStatementFieldToMatchSingleHeaderTypeDef = TypedDict(
    "ClientCheckCapacityRulesStatementXssMatchStatementFieldToMatchSingleHeaderTypeDef",
    {"Name": str},
    total=False,
)

ClientCheckCapacityRulesStatementXssMatchStatementFieldToMatchSingleQueryArgumentTypeDef = TypedDict(
    "ClientCheckCapacityRulesStatementXssMatchStatementFieldToMatchSingleQueryArgumentTypeDef",
    {"Name": str},
    total=False,
)

ClientCheckCapacityRulesStatementXssMatchStatementFieldToMatchTypeDef = TypedDict(
    "ClientCheckCapacityRulesStatementXssMatchStatementFieldToMatchTypeDef",
    {
        "SingleHeader": ClientCheckCapacityRulesStatementXssMatchStatementFieldToMatchSingleHeaderTypeDef,
        "SingleQueryArgument": ClientCheckCapacityRulesStatementXssMatchStatementFieldToMatchSingleQueryArgumentTypeDef,
        "AllQueryArguments": Dict[str, Any],
        "UriPath": Dict[str, Any],
        "QueryString": Dict[str, Any],
        "Body": Dict[str, Any],
        "Method": Dict[str, Any],
    },
    total=False,
)

ClientCheckCapacityRulesStatementXssMatchStatementTextTransformationsTypeDef = TypedDict(
    "ClientCheckCapacityRulesStatementXssMatchStatementTextTransformationsTypeDef",
    {
        "Priority": int,
        "Type": Literal[
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

ClientCheckCapacityRulesStatementXssMatchStatementTypeDef = TypedDict(
    "ClientCheckCapacityRulesStatementXssMatchStatementTypeDef",
    {
        "FieldToMatch": ClientCheckCapacityRulesStatementXssMatchStatementFieldToMatchTypeDef,
        "TextTransformations": List[
            ClientCheckCapacityRulesStatementXssMatchStatementTextTransformationsTypeDef
        ],
    },
    total=False,
)

ClientCheckCapacityRulesStatementTypeDef = TypedDict(
    "ClientCheckCapacityRulesStatementTypeDef",
    {
        "ByteMatchStatement": ClientCheckCapacityRulesStatementByteMatchStatementTypeDef,
        "SqliMatchStatement": ClientCheckCapacityRulesStatementSqliMatchStatementTypeDef,
        "XssMatchStatement": ClientCheckCapacityRulesStatementXssMatchStatementTypeDef,
        "SizeConstraintStatement": ClientCheckCapacityRulesStatementSizeConstraintStatementTypeDef,
        "GeoMatchStatement": ClientCheckCapacityRulesStatementGeoMatchStatementTypeDef,
        "RuleGroupReferenceStatement": ClientCheckCapacityRulesStatementRuleGroupReferenceStatementTypeDef,
        "IPSetReferenceStatement": ClientCheckCapacityRulesStatementIPSetReferenceStatementTypeDef,
        "RegexPatternSetReferenceStatement": ClientCheckCapacityRulesStatementRegexPatternSetReferenceStatementTypeDef,
        "RateBasedStatement": ClientCheckCapacityRulesStatementRateBasedStatementTypeDef,
        "AndStatement": ClientCheckCapacityRulesStatementAndStatementTypeDef,
        "OrStatement": ClientCheckCapacityRulesStatementOrStatementTypeDef,
        "NotStatement": ClientCheckCapacityRulesStatementNotStatementTypeDef,
        "ManagedRuleGroupStatement": ClientCheckCapacityRulesStatementManagedRuleGroupStatementTypeDef,
    },
    total=False,
)

ClientCheckCapacityRulesVisibilityConfigTypeDef = TypedDict(
    "ClientCheckCapacityRulesVisibilityConfigTypeDef",
    {"SampledRequestsEnabled": bool, "CloudWatchMetricsEnabled": bool, "MetricName": str},
    total=False,
)

ClientCheckCapacityRulesTypeDef = TypedDict(
    "ClientCheckCapacityRulesTypeDef",
    {
        "Name": str,
        "Priority": int,
        "Statement": ClientCheckCapacityRulesStatementTypeDef,
        "Action": ClientCheckCapacityRulesActionTypeDef,
        "OverrideAction": ClientCheckCapacityRulesOverrideActionTypeDef,
        "VisibilityConfig": ClientCheckCapacityRulesVisibilityConfigTypeDef,
    },
    total=False,
)

ClientCreateIpSetResponseSummaryTypeDef = TypedDict(
    "ClientCreateIpSetResponseSummaryTypeDef",
    {"Name": str, "Id": str, "Description": str, "LockToken": str, "ARN": str},
    total=False,
)

ClientCreateIpSetResponseTypeDef = TypedDict(
    "ClientCreateIpSetResponseTypeDef",
    {"Summary": ClientCreateIpSetResponseSummaryTypeDef},
    total=False,
)

ClientCreateIpSetTagsTypeDef = TypedDict(
    "ClientCreateIpSetTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreateRegexPatternSetRegularExpressionListTypeDef = TypedDict(
    "ClientCreateRegexPatternSetRegularExpressionListTypeDef", {"RegexString": str}, total=False
)

ClientCreateRegexPatternSetResponseSummaryTypeDef = TypedDict(
    "ClientCreateRegexPatternSetResponseSummaryTypeDef",
    {"Name": str, "Id": str, "Description": str, "LockToken": str, "ARN": str},
    total=False,
)

ClientCreateRegexPatternSetResponseTypeDef = TypedDict(
    "ClientCreateRegexPatternSetResponseTypeDef",
    {"Summary": ClientCreateRegexPatternSetResponseSummaryTypeDef},
    total=False,
)

ClientCreateRegexPatternSetTagsTypeDef = TypedDict(
    "ClientCreateRegexPatternSetTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreateRuleGroupResponseSummaryTypeDef = TypedDict(
    "ClientCreateRuleGroupResponseSummaryTypeDef",
    {"Name": str, "Id": str, "Description": str, "LockToken": str, "ARN": str},
    total=False,
)

ClientCreateRuleGroupResponseTypeDef = TypedDict(
    "ClientCreateRuleGroupResponseTypeDef",
    {"Summary": ClientCreateRuleGroupResponseSummaryTypeDef},
    total=False,
)

ClientCreateRuleGroupRulesActionTypeDef = TypedDict(
    "ClientCreateRuleGroupRulesActionTypeDef",
    {"Block": Dict[str, Any], "Allow": Dict[str, Any], "Count": Dict[str, Any]},
    total=False,
)

ClientCreateRuleGroupRulesOverrideActionTypeDef = TypedDict(
    "ClientCreateRuleGroupRulesOverrideActionTypeDef",
    {"Count": Dict[str, Any], "None": Dict[str, Any]},
    total=False,
)

ClientCreateRuleGroupRulesStatementAndStatementTypeDef = TypedDict(
    "ClientCreateRuleGroupRulesStatementAndStatementTypeDef", {"Statements": List[Any]}, total=False
)

ClientCreateRuleGroupRulesStatementByteMatchStatementFieldToMatchSingleHeaderTypeDef = TypedDict(
    "ClientCreateRuleGroupRulesStatementByteMatchStatementFieldToMatchSingleHeaderTypeDef",
    {"Name": str},
    total=False,
)

ClientCreateRuleGroupRulesStatementByteMatchStatementFieldToMatchSingleQueryArgumentTypeDef = TypedDict(
    "ClientCreateRuleGroupRulesStatementByteMatchStatementFieldToMatchSingleQueryArgumentTypeDef",
    {"Name": str},
    total=False,
)

ClientCreateRuleGroupRulesStatementByteMatchStatementFieldToMatchTypeDef = TypedDict(
    "ClientCreateRuleGroupRulesStatementByteMatchStatementFieldToMatchTypeDef",
    {
        "SingleHeader": ClientCreateRuleGroupRulesStatementByteMatchStatementFieldToMatchSingleHeaderTypeDef,
        "SingleQueryArgument": ClientCreateRuleGroupRulesStatementByteMatchStatementFieldToMatchSingleQueryArgumentTypeDef,
        "AllQueryArguments": Dict[str, Any],
        "UriPath": Dict[str, Any],
        "QueryString": Dict[str, Any],
        "Body": Dict[str, Any],
        "Method": Dict[str, Any],
    },
    total=False,
)

ClientCreateRuleGroupRulesStatementByteMatchStatementTextTransformationsTypeDef = TypedDict(
    "ClientCreateRuleGroupRulesStatementByteMatchStatementTextTransformationsTypeDef",
    {
        "Priority": int,
        "Type": Literal[
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

ClientCreateRuleGroupRulesStatementByteMatchStatementTypeDef = TypedDict(
    "ClientCreateRuleGroupRulesStatementByteMatchStatementTypeDef",
    {
        "SearchString": bytes,
        "FieldToMatch": ClientCreateRuleGroupRulesStatementByteMatchStatementFieldToMatchTypeDef,
        "TextTransformations": List[
            ClientCreateRuleGroupRulesStatementByteMatchStatementTextTransformationsTypeDef
        ],
        "PositionalConstraint": Literal[
            "EXACTLY", "STARTS_WITH", "ENDS_WITH", "CONTAINS", "CONTAINS_WORD"
        ],
    },
    total=False,
)

ClientCreateRuleGroupRulesStatementGeoMatchStatementTypeDef = TypedDict(
    "ClientCreateRuleGroupRulesStatementGeoMatchStatementTypeDef",
    {
        "CountryCodes": List[
            Literal[
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
            ]
        ]
    },
    total=False,
)

ClientCreateRuleGroupRulesStatementIPSetReferenceStatementTypeDef = TypedDict(
    "ClientCreateRuleGroupRulesStatementIPSetReferenceStatementTypeDef", {"ARN": str}, total=False
)

ClientCreateRuleGroupRulesStatementManagedRuleGroupStatementExcludedRulesTypeDef = TypedDict(
    "ClientCreateRuleGroupRulesStatementManagedRuleGroupStatementExcludedRulesTypeDef",
    {"Name": str},
    total=False,
)

ClientCreateRuleGroupRulesStatementManagedRuleGroupStatementTypeDef = TypedDict(
    "ClientCreateRuleGroupRulesStatementManagedRuleGroupStatementTypeDef",
    {
        "VendorName": str,
        "Name": str,
        "ExcludedRules": List[
            ClientCreateRuleGroupRulesStatementManagedRuleGroupStatementExcludedRulesTypeDef
        ],
    },
    total=False,
)

ClientCreateRuleGroupRulesStatementNotStatementTypeDef = TypedDict(
    "ClientCreateRuleGroupRulesStatementNotStatementTypeDef", {"Statement": Any}, total=False
)

ClientCreateRuleGroupRulesStatementOrStatementTypeDef = TypedDict(
    "ClientCreateRuleGroupRulesStatementOrStatementTypeDef", {"Statements": List[Any]}, total=False
)

ClientCreateRuleGroupRulesStatementRateBasedStatementTypeDef = TypedDict(
    "ClientCreateRuleGroupRulesStatementRateBasedStatementTypeDef",
    {"Limit": int, "AggregateKeyType": str, "ScopeDownStatement": Any},
    total=False,
)

ClientCreateRuleGroupRulesStatementRegexPatternSetReferenceStatementFieldToMatchSingleHeaderTypeDef = TypedDict(
    "ClientCreateRuleGroupRulesStatementRegexPatternSetReferenceStatementFieldToMatchSingleHeaderTypeDef",
    {"Name": str},
    total=False,
)

ClientCreateRuleGroupRulesStatementRegexPatternSetReferenceStatementFieldToMatchSingleQueryArgumentTypeDef = TypedDict(
    "ClientCreateRuleGroupRulesStatementRegexPatternSetReferenceStatementFieldToMatchSingleQueryArgumentTypeDef",
    {"Name": str},
    total=False,
)

ClientCreateRuleGroupRulesStatementRegexPatternSetReferenceStatementFieldToMatchTypeDef = TypedDict(
    "ClientCreateRuleGroupRulesStatementRegexPatternSetReferenceStatementFieldToMatchTypeDef",
    {
        "SingleHeader": ClientCreateRuleGroupRulesStatementRegexPatternSetReferenceStatementFieldToMatchSingleHeaderTypeDef,
        "SingleQueryArgument": ClientCreateRuleGroupRulesStatementRegexPatternSetReferenceStatementFieldToMatchSingleQueryArgumentTypeDef,
        "AllQueryArguments": Dict[str, Any],
        "UriPath": Dict[str, Any],
        "QueryString": Dict[str, Any],
        "Body": Dict[str, Any],
        "Method": Dict[str, Any],
    },
    total=False,
)

ClientCreateRuleGroupRulesStatementRegexPatternSetReferenceStatementTextTransformationsTypeDef = TypedDict(
    "ClientCreateRuleGroupRulesStatementRegexPatternSetReferenceStatementTextTransformationsTypeDef",
    {
        "Priority": int,
        "Type": Literal[
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

ClientCreateRuleGroupRulesStatementRegexPatternSetReferenceStatementTypeDef = TypedDict(
    "ClientCreateRuleGroupRulesStatementRegexPatternSetReferenceStatementTypeDef",
    {
        "ARN": str,
        "FieldToMatch": ClientCreateRuleGroupRulesStatementRegexPatternSetReferenceStatementFieldToMatchTypeDef,
        "TextTransformations": List[
            ClientCreateRuleGroupRulesStatementRegexPatternSetReferenceStatementTextTransformationsTypeDef
        ],
    },
    total=False,
)

ClientCreateRuleGroupRulesStatementRuleGroupReferenceStatementExcludedRulesTypeDef = TypedDict(
    "ClientCreateRuleGroupRulesStatementRuleGroupReferenceStatementExcludedRulesTypeDef",
    {"Name": str},
    total=False,
)

ClientCreateRuleGroupRulesStatementRuleGroupReferenceStatementTypeDef = TypedDict(
    "ClientCreateRuleGroupRulesStatementRuleGroupReferenceStatementTypeDef",
    {
        "ARN": str,
        "ExcludedRules": List[
            ClientCreateRuleGroupRulesStatementRuleGroupReferenceStatementExcludedRulesTypeDef
        ],
    },
    total=False,
)

ClientCreateRuleGroupRulesStatementSizeConstraintStatementFieldToMatchSingleHeaderTypeDef = TypedDict(
    "ClientCreateRuleGroupRulesStatementSizeConstraintStatementFieldToMatchSingleHeaderTypeDef",
    {"Name": str},
    total=False,
)

ClientCreateRuleGroupRulesStatementSizeConstraintStatementFieldToMatchSingleQueryArgumentTypeDef = TypedDict(
    "ClientCreateRuleGroupRulesStatementSizeConstraintStatementFieldToMatchSingleQueryArgumentTypeDef",
    {"Name": str},
    total=False,
)

ClientCreateRuleGroupRulesStatementSizeConstraintStatementFieldToMatchTypeDef = TypedDict(
    "ClientCreateRuleGroupRulesStatementSizeConstraintStatementFieldToMatchTypeDef",
    {
        "SingleHeader": ClientCreateRuleGroupRulesStatementSizeConstraintStatementFieldToMatchSingleHeaderTypeDef,
        "SingleQueryArgument": ClientCreateRuleGroupRulesStatementSizeConstraintStatementFieldToMatchSingleQueryArgumentTypeDef,
        "AllQueryArguments": Dict[str, Any],
        "UriPath": Dict[str, Any],
        "QueryString": Dict[str, Any],
        "Body": Dict[str, Any],
        "Method": Dict[str, Any],
    },
    total=False,
)

ClientCreateRuleGroupRulesStatementSizeConstraintStatementTextTransformationsTypeDef = TypedDict(
    "ClientCreateRuleGroupRulesStatementSizeConstraintStatementTextTransformationsTypeDef",
    {
        "Priority": int,
        "Type": Literal[
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

ClientCreateRuleGroupRulesStatementSizeConstraintStatementTypeDef = TypedDict(
    "ClientCreateRuleGroupRulesStatementSizeConstraintStatementTypeDef",
    {
        "FieldToMatch": ClientCreateRuleGroupRulesStatementSizeConstraintStatementFieldToMatchTypeDef,
        "ComparisonOperator": Literal["EQ", "NE", "LE", "LT", "GE", "GT"],
        "Size": int,
        "TextTransformations": List[
            ClientCreateRuleGroupRulesStatementSizeConstraintStatementTextTransformationsTypeDef
        ],
    },
    total=False,
)

ClientCreateRuleGroupRulesStatementSqliMatchStatementFieldToMatchSingleHeaderTypeDef = TypedDict(
    "ClientCreateRuleGroupRulesStatementSqliMatchStatementFieldToMatchSingleHeaderTypeDef",
    {"Name": str},
    total=False,
)

ClientCreateRuleGroupRulesStatementSqliMatchStatementFieldToMatchSingleQueryArgumentTypeDef = TypedDict(
    "ClientCreateRuleGroupRulesStatementSqliMatchStatementFieldToMatchSingleQueryArgumentTypeDef",
    {"Name": str},
    total=False,
)

ClientCreateRuleGroupRulesStatementSqliMatchStatementFieldToMatchTypeDef = TypedDict(
    "ClientCreateRuleGroupRulesStatementSqliMatchStatementFieldToMatchTypeDef",
    {
        "SingleHeader": ClientCreateRuleGroupRulesStatementSqliMatchStatementFieldToMatchSingleHeaderTypeDef,
        "SingleQueryArgument": ClientCreateRuleGroupRulesStatementSqliMatchStatementFieldToMatchSingleQueryArgumentTypeDef,
        "AllQueryArguments": Dict[str, Any],
        "UriPath": Dict[str, Any],
        "QueryString": Dict[str, Any],
        "Body": Dict[str, Any],
        "Method": Dict[str, Any],
    },
    total=False,
)

ClientCreateRuleGroupRulesStatementSqliMatchStatementTextTransformationsTypeDef = TypedDict(
    "ClientCreateRuleGroupRulesStatementSqliMatchStatementTextTransformationsTypeDef",
    {
        "Priority": int,
        "Type": Literal[
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

ClientCreateRuleGroupRulesStatementSqliMatchStatementTypeDef = TypedDict(
    "ClientCreateRuleGroupRulesStatementSqliMatchStatementTypeDef",
    {
        "FieldToMatch": ClientCreateRuleGroupRulesStatementSqliMatchStatementFieldToMatchTypeDef,
        "TextTransformations": List[
            ClientCreateRuleGroupRulesStatementSqliMatchStatementTextTransformationsTypeDef
        ],
    },
    total=False,
)

ClientCreateRuleGroupRulesStatementXssMatchStatementFieldToMatchSingleHeaderTypeDef = TypedDict(
    "ClientCreateRuleGroupRulesStatementXssMatchStatementFieldToMatchSingleHeaderTypeDef",
    {"Name": str},
    total=False,
)

ClientCreateRuleGroupRulesStatementXssMatchStatementFieldToMatchSingleQueryArgumentTypeDef = TypedDict(
    "ClientCreateRuleGroupRulesStatementXssMatchStatementFieldToMatchSingleQueryArgumentTypeDef",
    {"Name": str},
    total=False,
)

ClientCreateRuleGroupRulesStatementXssMatchStatementFieldToMatchTypeDef = TypedDict(
    "ClientCreateRuleGroupRulesStatementXssMatchStatementFieldToMatchTypeDef",
    {
        "SingleHeader": ClientCreateRuleGroupRulesStatementXssMatchStatementFieldToMatchSingleHeaderTypeDef,
        "SingleQueryArgument": ClientCreateRuleGroupRulesStatementXssMatchStatementFieldToMatchSingleQueryArgumentTypeDef,
        "AllQueryArguments": Dict[str, Any],
        "UriPath": Dict[str, Any],
        "QueryString": Dict[str, Any],
        "Body": Dict[str, Any],
        "Method": Dict[str, Any],
    },
    total=False,
)

ClientCreateRuleGroupRulesStatementXssMatchStatementTextTransformationsTypeDef = TypedDict(
    "ClientCreateRuleGroupRulesStatementXssMatchStatementTextTransformationsTypeDef",
    {
        "Priority": int,
        "Type": Literal[
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

ClientCreateRuleGroupRulesStatementXssMatchStatementTypeDef = TypedDict(
    "ClientCreateRuleGroupRulesStatementXssMatchStatementTypeDef",
    {
        "FieldToMatch": ClientCreateRuleGroupRulesStatementXssMatchStatementFieldToMatchTypeDef,
        "TextTransformations": List[
            ClientCreateRuleGroupRulesStatementXssMatchStatementTextTransformationsTypeDef
        ],
    },
    total=False,
)

ClientCreateRuleGroupRulesStatementTypeDef = TypedDict(
    "ClientCreateRuleGroupRulesStatementTypeDef",
    {
        "ByteMatchStatement": ClientCreateRuleGroupRulesStatementByteMatchStatementTypeDef,
        "SqliMatchStatement": ClientCreateRuleGroupRulesStatementSqliMatchStatementTypeDef,
        "XssMatchStatement": ClientCreateRuleGroupRulesStatementXssMatchStatementTypeDef,
        "SizeConstraintStatement": ClientCreateRuleGroupRulesStatementSizeConstraintStatementTypeDef,
        "GeoMatchStatement": ClientCreateRuleGroupRulesStatementGeoMatchStatementTypeDef,
        "RuleGroupReferenceStatement": ClientCreateRuleGroupRulesStatementRuleGroupReferenceStatementTypeDef,
        "IPSetReferenceStatement": ClientCreateRuleGroupRulesStatementIPSetReferenceStatementTypeDef,
        "RegexPatternSetReferenceStatement": ClientCreateRuleGroupRulesStatementRegexPatternSetReferenceStatementTypeDef,
        "RateBasedStatement": ClientCreateRuleGroupRulesStatementRateBasedStatementTypeDef,
        "AndStatement": ClientCreateRuleGroupRulesStatementAndStatementTypeDef,
        "OrStatement": ClientCreateRuleGroupRulesStatementOrStatementTypeDef,
        "NotStatement": ClientCreateRuleGroupRulesStatementNotStatementTypeDef,
        "ManagedRuleGroupStatement": ClientCreateRuleGroupRulesStatementManagedRuleGroupStatementTypeDef,
    },
    total=False,
)

ClientCreateRuleGroupRulesVisibilityConfigTypeDef = TypedDict(
    "ClientCreateRuleGroupRulesVisibilityConfigTypeDef",
    {"SampledRequestsEnabled": bool, "CloudWatchMetricsEnabled": bool, "MetricName": str},
    total=False,
)

ClientCreateRuleGroupRulesTypeDef = TypedDict(
    "ClientCreateRuleGroupRulesTypeDef",
    {
        "Name": str,
        "Priority": int,
        "Statement": ClientCreateRuleGroupRulesStatementTypeDef,
        "Action": ClientCreateRuleGroupRulesActionTypeDef,
        "OverrideAction": ClientCreateRuleGroupRulesOverrideActionTypeDef,
        "VisibilityConfig": ClientCreateRuleGroupRulesVisibilityConfigTypeDef,
    },
    total=False,
)

ClientCreateRuleGroupTagsTypeDef = TypedDict(
    "ClientCreateRuleGroupTagsTypeDef", {"Key": str, "Value": str}, total=False
)

_RequiredClientCreateRuleGroupVisibilityConfigTypeDef = TypedDict(
    "_RequiredClientCreateRuleGroupVisibilityConfigTypeDef", {"SampledRequestsEnabled": bool}
)
_OptionalClientCreateRuleGroupVisibilityConfigTypeDef = TypedDict(
    "_OptionalClientCreateRuleGroupVisibilityConfigTypeDef",
    {"CloudWatchMetricsEnabled": bool, "MetricName": str},
    total=False,
)


class ClientCreateRuleGroupVisibilityConfigTypeDef(
    _RequiredClientCreateRuleGroupVisibilityConfigTypeDef,
    _OptionalClientCreateRuleGroupVisibilityConfigTypeDef,
):
    pass


ClientCreateWebAclDefaultActionTypeDef = TypedDict(
    "ClientCreateWebAclDefaultActionTypeDef",
    {"Block": Dict[str, Any], "Allow": Dict[str, Any]},
    total=False,
)

ClientCreateWebAclResponseSummaryTypeDef = TypedDict(
    "ClientCreateWebAclResponseSummaryTypeDef",
    {"Name": str, "Id": str, "Description": str, "LockToken": str, "ARN": str},
    total=False,
)

ClientCreateWebAclResponseTypeDef = TypedDict(
    "ClientCreateWebAclResponseTypeDef",
    {"Summary": ClientCreateWebAclResponseSummaryTypeDef},
    total=False,
)

ClientCreateWebAclRulesActionTypeDef = TypedDict(
    "ClientCreateWebAclRulesActionTypeDef",
    {"Block": Dict[str, Any], "Allow": Dict[str, Any], "Count": Dict[str, Any]},
    total=False,
)

ClientCreateWebAclRulesOverrideActionTypeDef = TypedDict(
    "ClientCreateWebAclRulesOverrideActionTypeDef",
    {"Count": Dict[str, Any], "None": Dict[str, Any]},
    total=False,
)

ClientCreateWebAclRulesStatementAndStatementTypeDef = TypedDict(
    "ClientCreateWebAclRulesStatementAndStatementTypeDef", {"Statements": List[Any]}, total=False
)

ClientCreateWebAclRulesStatementByteMatchStatementFieldToMatchSingleHeaderTypeDef = TypedDict(
    "ClientCreateWebAclRulesStatementByteMatchStatementFieldToMatchSingleHeaderTypeDef",
    {"Name": str},
    total=False,
)

ClientCreateWebAclRulesStatementByteMatchStatementFieldToMatchSingleQueryArgumentTypeDef = TypedDict(
    "ClientCreateWebAclRulesStatementByteMatchStatementFieldToMatchSingleQueryArgumentTypeDef",
    {"Name": str},
    total=False,
)

ClientCreateWebAclRulesStatementByteMatchStatementFieldToMatchTypeDef = TypedDict(
    "ClientCreateWebAclRulesStatementByteMatchStatementFieldToMatchTypeDef",
    {
        "SingleHeader": ClientCreateWebAclRulesStatementByteMatchStatementFieldToMatchSingleHeaderTypeDef,
        "SingleQueryArgument": ClientCreateWebAclRulesStatementByteMatchStatementFieldToMatchSingleQueryArgumentTypeDef,
        "AllQueryArguments": Dict[str, Any],
        "UriPath": Dict[str, Any],
        "QueryString": Dict[str, Any],
        "Body": Dict[str, Any],
        "Method": Dict[str, Any],
    },
    total=False,
)

ClientCreateWebAclRulesStatementByteMatchStatementTextTransformationsTypeDef = TypedDict(
    "ClientCreateWebAclRulesStatementByteMatchStatementTextTransformationsTypeDef",
    {
        "Priority": int,
        "Type": Literal[
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

ClientCreateWebAclRulesStatementByteMatchStatementTypeDef = TypedDict(
    "ClientCreateWebAclRulesStatementByteMatchStatementTypeDef",
    {
        "SearchString": bytes,
        "FieldToMatch": ClientCreateWebAclRulesStatementByteMatchStatementFieldToMatchTypeDef,
        "TextTransformations": List[
            ClientCreateWebAclRulesStatementByteMatchStatementTextTransformationsTypeDef
        ],
        "PositionalConstraint": Literal[
            "EXACTLY", "STARTS_WITH", "ENDS_WITH", "CONTAINS", "CONTAINS_WORD"
        ],
    },
    total=False,
)

ClientCreateWebAclRulesStatementGeoMatchStatementTypeDef = TypedDict(
    "ClientCreateWebAclRulesStatementGeoMatchStatementTypeDef",
    {
        "CountryCodes": List[
            Literal[
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
            ]
        ]
    },
    total=False,
)

ClientCreateWebAclRulesStatementIPSetReferenceStatementTypeDef = TypedDict(
    "ClientCreateWebAclRulesStatementIPSetReferenceStatementTypeDef", {"ARN": str}, total=False
)

ClientCreateWebAclRulesStatementManagedRuleGroupStatementExcludedRulesTypeDef = TypedDict(
    "ClientCreateWebAclRulesStatementManagedRuleGroupStatementExcludedRulesTypeDef",
    {"Name": str},
    total=False,
)

ClientCreateWebAclRulesStatementManagedRuleGroupStatementTypeDef = TypedDict(
    "ClientCreateWebAclRulesStatementManagedRuleGroupStatementTypeDef",
    {
        "VendorName": str,
        "Name": str,
        "ExcludedRules": List[
            ClientCreateWebAclRulesStatementManagedRuleGroupStatementExcludedRulesTypeDef
        ],
    },
    total=False,
)

ClientCreateWebAclRulesStatementNotStatementTypeDef = TypedDict(
    "ClientCreateWebAclRulesStatementNotStatementTypeDef", {"Statement": Any}, total=False
)

ClientCreateWebAclRulesStatementOrStatementTypeDef = TypedDict(
    "ClientCreateWebAclRulesStatementOrStatementTypeDef", {"Statements": List[Any]}, total=False
)

ClientCreateWebAclRulesStatementRateBasedStatementTypeDef = TypedDict(
    "ClientCreateWebAclRulesStatementRateBasedStatementTypeDef",
    {"Limit": int, "AggregateKeyType": str, "ScopeDownStatement": Any},
    total=False,
)

ClientCreateWebAclRulesStatementRegexPatternSetReferenceStatementFieldToMatchSingleHeaderTypeDef = TypedDict(
    "ClientCreateWebAclRulesStatementRegexPatternSetReferenceStatementFieldToMatchSingleHeaderTypeDef",
    {"Name": str},
    total=False,
)

ClientCreateWebAclRulesStatementRegexPatternSetReferenceStatementFieldToMatchSingleQueryArgumentTypeDef = TypedDict(
    "ClientCreateWebAclRulesStatementRegexPatternSetReferenceStatementFieldToMatchSingleQueryArgumentTypeDef",
    {"Name": str},
    total=False,
)

ClientCreateWebAclRulesStatementRegexPatternSetReferenceStatementFieldToMatchTypeDef = TypedDict(
    "ClientCreateWebAclRulesStatementRegexPatternSetReferenceStatementFieldToMatchTypeDef",
    {
        "SingleHeader": ClientCreateWebAclRulesStatementRegexPatternSetReferenceStatementFieldToMatchSingleHeaderTypeDef,
        "SingleQueryArgument": ClientCreateWebAclRulesStatementRegexPatternSetReferenceStatementFieldToMatchSingleQueryArgumentTypeDef,
        "AllQueryArguments": Dict[str, Any],
        "UriPath": Dict[str, Any],
        "QueryString": Dict[str, Any],
        "Body": Dict[str, Any],
        "Method": Dict[str, Any],
    },
    total=False,
)

ClientCreateWebAclRulesStatementRegexPatternSetReferenceStatementTextTransformationsTypeDef = TypedDict(
    "ClientCreateWebAclRulesStatementRegexPatternSetReferenceStatementTextTransformationsTypeDef",
    {
        "Priority": int,
        "Type": Literal[
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

ClientCreateWebAclRulesStatementRegexPatternSetReferenceStatementTypeDef = TypedDict(
    "ClientCreateWebAclRulesStatementRegexPatternSetReferenceStatementTypeDef",
    {
        "ARN": str,
        "FieldToMatch": ClientCreateWebAclRulesStatementRegexPatternSetReferenceStatementFieldToMatchTypeDef,
        "TextTransformations": List[
            ClientCreateWebAclRulesStatementRegexPatternSetReferenceStatementTextTransformationsTypeDef
        ],
    },
    total=False,
)

ClientCreateWebAclRulesStatementRuleGroupReferenceStatementExcludedRulesTypeDef = TypedDict(
    "ClientCreateWebAclRulesStatementRuleGroupReferenceStatementExcludedRulesTypeDef",
    {"Name": str},
    total=False,
)

ClientCreateWebAclRulesStatementRuleGroupReferenceStatementTypeDef = TypedDict(
    "ClientCreateWebAclRulesStatementRuleGroupReferenceStatementTypeDef",
    {
        "ARN": str,
        "ExcludedRules": List[
            ClientCreateWebAclRulesStatementRuleGroupReferenceStatementExcludedRulesTypeDef
        ],
    },
    total=False,
)

ClientCreateWebAclRulesStatementSizeConstraintStatementFieldToMatchSingleHeaderTypeDef = TypedDict(
    "ClientCreateWebAclRulesStatementSizeConstraintStatementFieldToMatchSingleHeaderTypeDef",
    {"Name": str},
    total=False,
)

ClientCreateWebAclRulesStatementSizeConstraintStatementFieldToMatchSingleQueryArgumentTypeDef = TypedDict(
    "ClientCreateWebAclRulesStatementSizeConstraintStatementFieldToMatchSingleQueryArgumentTypeDef",
    {"Name": str},
    total=False,
)

ClientCreateWebAclRulesStatementSizeConstraintStatementFieldToMatchTypeDef = TypedDict(
    "ClientCreateWebAclRulesStatementSizeConstraintStatementFieldToMatchTypeDef",
    {
        "SingleHeader": ClientCreateWebAclRulesStatementSizeConstraintStatementFieldToMatchSingleHeaderTypeDef,
        "SingleQueryArgument": ClientCreateWebAclRulesStatementSizeConstraintStatementFieldToMatchSingleQueryArgumentTypeDef,
        "AllQueryArguments": Dict[str, Any],
        "UriPath": Dict[str, Any],
        "QueryString": Dict[str, Any],
        "Body": Dict[str, Any],
        "Method": Dict[str, Any],
    },
    total=False,
)

ClientCreateWebAclRulesStatementSizeConstraintStatementTextTransformationsTypeDef = TypedDict(
    "ClientCreateWebAclRulesStatementSizeConstraintStatementTextTransformationsTypeDef",
    {
        "Priority": int,
        "Type": Literal[
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

ClientCreateWebAclRulesStatementSizeConstraintStatementTypeDef = TypedDict(
    "ClientCreateWebAclRulesStatementSizeConstraintStatementTypeDef",
    {
        "FieldToMatch": ClientCreateWebAclRulesStatementSizeConstraintStatementFieldToMatchTypeDef,
        "ComparisonOperator": Literal["EQ", "NE", "LE", "LT", "GE", "GT"],
        "Size": int,
        "TextTransformations": List[
            ClientCreateWebAclRulesStatementSizeConstraintStatementTextTransformationsTypeDef
        ],
    },
    total=False,
)

ClientCreateWebAclRulesStatementSqliMatchStatementFieldToMatchSingleHeaderTypeDef = TypedDict(
    "ClientCreateWebAclRulesStatementSqliMatchStatementFieldToMatchSingleHeaderTypeDef",
    {"Name": str},
    total=False,
)

ClientCreateWebAclRulesStatementSqliMatchStatementFieldToMatchSingleQueryArgumentTypeDef = TypedDict(
    "ClientCreateWebAclRulesStatementSqliMatchStatementFieldToMatchSingleQueryArgumentTypeDef",
    {"Name": str},
    total=False,
)

ClientCreateWebAclRulesStatementSqliMatchStatementFieldToMatchTypeDef = TypedDict(
    "ClientCreateWebAclRulesStatementSqliMatchStatementFieldToMatchTypeDef",
    {
        "SingleHeader": ClientCreateWebAclRulesStatementSqliMatchStatementFieldToMatchSingleHeaderTypeDef,
        "SingleQueryArgument": ClientCreateWebAclRulesStatementSqliMatchStatementFieldToMatchSingleQueryArgumentTypeDef,
        "AllQueryArguments": Dict[str, Any],
        "UriPath": Dict[str, Any],
        "QueryString": Dict[str, Any],
        "Body": Dict[str, Any],
        "Method": Dict[str, Any],
    },
    total=False,
)

ClientCreateWebAclRulesStatementSqliMatchStatementTextTransformationsTypeDef = TypedDict(
    "ClientCreateWebAclRulesStatementSqliMatchStatementTextTransformationsTypeDef",
    {
        "Priority": int,
        "Type": Literal[
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

ClientCreateWebAclRulesStatementSqliMatchStatementTypeDef = TypedDict(
    "ClientCreateWebAclRulesStatementSqliMatchStatementTypeDef",
    {
        "FieldToMatch": ClientCreateWebAclRulesStatementSqliMatchStatementFieldToMatchTypeDef,
        "TextTransformations": List[
            ClientCreateWebAclRulesStatementSqliMatchStatementTextTransformationsTypeDef
        ],
    },
    total=False,
)

ClientCreateWebAclRulesStatementXssMatchStatementFieldToMatchSingleHeaderTypeDef = TypedDict(
    "ClientCreateWebAclRulesStatementXssMatchStatementFieldToMatchSingleHeaderTypeDef",
    {"Name": str},
    total=False,
)

ClientCreateWebAclRulesStatementXssMatchStatementFieldToMatchSingleQueryArgumentTypeDef = TypedDict(
    "ClientCreateWebAclRulesStatementXssMatchStatementFieldToMatchSingleQueryArgumentTypeDef",
    {"Name": str},
    total=False,
)

ClientCreateWebAclRulesStatementXssMatchStatementFieldToMatchTypeDef = TypedDict(
    "ClientCreateWebAclRulesStatementXssMatchStatementFieldToMatchTypeDef",
    {
        "SingleHeader": ClientCreateWebAclRulesStatementXssMatchStatementFieldToMatchSingleHeaderTypeDef,
        "SingleQueryArgument": ClientCreateWebAclRulesStatementXssMatchStatementFieldToMatchSingleQueryArgumentTypeDef,
        "AllQueryArguments": Dict[str, Any],
        "UriPath": Dict[str, Any],
        "QueryString": Dict[str, Any],
        "Body": Dict[str, Any],
        "Method": Dict[str, Any],
    },
    total=False,
)

ClientCreateWebAclRulesStatementXssMatchStatementTextTransformationsTypeDef = TypedDict(
    "ClientCreateWebAclRulesStatementXssMatchStatementTextTransformationsTypeDef",
    {
        "Priority": int,
        "Type": Literal[
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

ClientCreateWebAclRulesStatementXssMatchStatementTypeDef = TypedDict(
    "ClientCreateWebAclRulesStatementXssMatchStatementTypeDef",
    {
        "FieldToMatch": ClientCreateWebAclRulesStatementXssMatchStatementFieldToMatchTypeDef,
        "TextTransformations": List[
            ClientCreateWebAclRulesStatementXssMatchStatementTextTransformationsTypeDef
        ],
    },
    total=False,
)

ClientCreateWebAclRulesStatementTypeDef = TypedDict(
    "ClientCreateWebAclRulesStatementTypeDef",
    {
        "ByteMatchStatement": ClientCreateWebAclRulesStatementByteMatchStatementTypeDef,
        "SqliMatchStatement": ClientCreateWebAclRulesStatementSqliMatchStatementTypeDef,
        "XssMatchStatement": ClientCreateWebAclRulesStatementXssMatchStatementTypeDef,
        "SizeConstraintStatement": ClientCreateWebAclRulesStatementSizeConstraintStatementTypeDef,
        "GeoMatchStatement": ClientCreateWebAclRulesStatementGeoMatchStatementTypeDef,
        "RuleGroupReferenceStatement": ClientCreateWebAclRulesStatementRuleGroupReferenceStatementTypeDef,
        "IPSetReferenceStatement": ClientCreateWebAclRulesStatementIPSetReferenceStatementTypeDef,
        "RegexPatternSetReferenceStatement": ClientCreateWebAclRulesStatementRegexPatternSetReferenceStatementTypeDef,
        "RateBasedStatement": ClientCreateWebAclRulesStatementRateBasedStatementTypeDef,
        "AndStatement": ClientCreateWebAclRulesStatementAndStatementTypeDef,
        "OrStatement": ClientCreateWebAclRulesStatementOrStatementTypeDef,
        "NotStatement": ClientCreateWebAclRulesStatementNotStatementTypeDef,
        "ManagedRuleGroupStatement": ClientCreateWebAclRulesStatementManagedRuleGroupStatementTypeDef,
    },
    total=False,
)

ClientCreateWebAclRulesVisibilityConfigTypeDef = TypedDict(
    "ClientCreateWebAclRulesVisibilityConfigTypeDef",
    {"SampledRequestsEnabled": bool, "CloudWatchMetricsEnabled": bool, "MetricName": str},
    total=False,
)

ClientCreateWebAclRulesTypeDef = TypedDict(
    "ClientCreateWebAclRulesTypeDef",
    {
        "Name": str,
        "Priority": int,
        "Statement": ClientCreateWebAclRulesStatementTypeDef,
        "Action": ClientCreateWebAclRulesActionTypeDef,
        "OverrideAction": ClientCreateWebAclRulesOverrideActionTypeDef,
        "VisibilityConfig": ClientCreateWebAclRulesVisibilityConfigTypeDef,
    },
    total=False,
)

ClientCreateWebAclTagsTypeDef = TypedDict(
    "ClientCreateWebAclTagsTypeDef", {"Key": str, "Value": str}, total=False
)

_RequiredClientCreateWebAclVisibilityConfigTypeDef = TypedDict(
    "_RequiredClientCreateWebAclVisibilityConfigTypeDef", {"SampledRequestsEnabled": bool}
)
_OptionalClientCreateWebAclVisibilityConfigTypeDef = TypedDict(
    "_OptionalClientCreateWebAclVisibilityConfigTypeDef",
    {"CloudWatchMetricsEnabled": bool, "MetricName": str},
    total=False,
)


class ClientCreateWebAclVisibilityConfigTypeDef(
    _RequiredClientCreateWebAclVisibilityConfigTypeDef,
    _OptionalClientCreateWebAclVisibilityConfigTypeDef,
):
    pass


ClientDescribeManagedRuleGroupResponseRulesActionTypeDef = TypedDict(
    "ClientDescribeManagedRuleGroupResponseRulesActionTypeDef",
    {"Block": Dict[str, Any], "Allow": Dict[str, Any], "Count": Dict[str, Any]},
    total=False,
)

ClientDescribeManagedRuleGroupResponseRulesTypeDef = TypedDict(
    "ClientDescribeManagedRuleGroupResponseRulesTypeDef",
    {"Name": str, "Action": ClientDescribeManagedRuleGroupResponseRulesActionTypeDef},
    total=False,
)

ClientDescribeManagedRuleGroupResponseTypeDef = TypedDict(
    "ClientDescribeManagedRuleGroupResponseTypeDef",
    {"Capacity": int, "Rules": List[ClientDescribeManagedRuleGroupResponseRulesTypeDef]},
    total=False,
)

ClientGetIpSetResponseIPSetTypeDef = TypedDict(
    "ClientGetIpSetResponseIPSetTypeDef",
    {
        "Name": str,
        "Id": str,
        "ARN": str,
        "Description": str,
        "IPAddressVersion": Literal["IPV4", "IPV6"],
        "Addresses": List[str],
    },
    total=False,
)

ClientGetIpSetResponseTypeDef = TypedDict(
    "ClientGetIpSetResponseTypeDef",
    {"IPSet": ClientGetIpSetResponseIPSetTypeDef, "LockToken": str},
    total=False,
)

ClientGetLoggingConfigurationResponseLoggingConfigurationRedactedFieldsSingleHeaderTypeDef = TypedDict(
    "ClientGetLoggingConfigurationResponseLoggingConfigurationRedactedFieldsSingleHeaderTypeDef",
    {"Name": str},
    total=False,
)

ClientGetLoggingConfigurationResponseLoggingConfigurationRedactedFieldsSingleQueryArgumentTypeDef = TypedDict(
    "ClientGetLoggingConfigurationResponseLoggingConfigurationRedactedFieldsSingleQueryArgumentTypeDef",
    {"Name": str},
    total=False,
)

ClientGetLoggingConfigurationResponseLoggingConfigurationRedactedFieldsTypeDef = TypedDict(
    "ClientGetLoggingConfigurationResponseLoggingConfigurationRedactedFieldsTypeDef",
    {
        "SingleHeader": ClientGetLoggingConfigurationResponseLoggingConfigurationRedactedFieldsSingleHeaderTypeDef,
        "SingleQueryArgument": ClientGetLoggingConfigurationResponseLoggingConfigurationRedactedFieldsSingleQueryArgumentTypeDef,
        "AllQueryArguments": Dict[str, Any],
        "UriPath": Dict[str, Any],
        "QueryString": Dict[str, Any],
        "Body": Dict[str, Any],
        "Method": Dict[str, Any],
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

ClientGetRateBasedStatementManagedKeysResponseManagedKeysIPV4TypeDef = TypedDict(
    "ClientGetRateBasedStatementManagedKeysResponseManagedKeysIPV4TypeDef",
    {"IPAddressVersion": Literal["IPV4", "IPV6"], "Addresses": List[str]},
    total=False,
)

ClientGetRateBasedStatementManagedKeysResponseManagedKeysIPV6TypeDef = TypedDict(
    "ClientGetRateBasedStatementManagedKeysResponseManagedKeysIPV6TypeDef",
    {"IPAddressVersion": Literal["IPV4", "IPV6"], "Addresses": List[str]},
    total=False,
)

ClientGetRateBasedStatementManagedKeysResponseTypeDef = TypedDict(
    "ClientGetRateBasedStatementManagedKeysResponseTypeDef",
    {
        "ManagedKeysIPV4": ClientGetRateBasedStatementManagedKeysResponseManagedKeysIPV4TypeDef,
        "ManagedKeysIPV6": ClientGetRateBasedStatementManagedKeysResponseManagedKeysIPV6TypeDef,
    },
    total=False,
)

ClientGetRegexPatternSetResponseRegexPatternSetRegularExpressionListTypeDef = TypedDict(
    "ClientGetRegexPatternSetResponseRegexPatternSetRegularExpressionListTypeDef",
    {"RegexString": str},
    total=False,
)

ClientGetRegexPatternSetResponseRegexPatternSetTypeDef = TypedDict(
    "ClientGetRegexPatternSetResponseRegexPatternSetTypeDef",
    {
        "Name": str,
        "Id": str,
        "ARN": str,
        "Description": str,
        "RegularExpressionList": List[
            ClientGetRegexPatternSetResponseRegexPatternSetRegularExpressionListTypeDef
        ],
    },
    total=False,
)

ClientGetRegexPatternSetResponseTypeDef = TypedDict(
    "ClientGetRegexPatternSetResponseTypeDef",
    {"RegexPatternSet": ClientGetRegexPatternSetResponseRegexPatternSetTypeDef, "LockToken": str},
    total=False,
)

ClientGetRuleGroupResponseRuleGroupRulesActionTypeDef = TypedDict(
    "ClientGetRuleGroupResponseRuleGroupRulesActionTypeDef",
    {"Block": Dict[str, Any], "Allow": Dict[str, Any], "Count": Dict[str, Any]},
    total=False,
)

ClientGetRuleGroupResponseRuleGroupRulesOverrideActionTypeDef = TypedDict(
    "ClientGetRuleGroupResponseRuleGroupRulesOverrideActionTypeDef",
    {"Count": Dict[str, Any], "None": Dict[str, Any]},
    total=False,
)

ClientGetRuleGroupResponseRuleGroupRulesStatementAndStatementTypeDef = TypedDict(
    "ClientGetRuleGroupResponseRuleGroupRulesStatementAndStatementTypeDef",
    {"Statements": List[Any]},
    total=False,
)

ClientGetRuleGroupResponseRuleGroupRulesStatementByteMatchStatementFieldToMatchSingleHeaderTypeDef = TypedDict(
    "ClientGetRuleGroupResponseRuleGroupRulesStatementByteMatchStatementFieldToMatchSingleHeaderTypeDef",
    {"Name": str},
    total=False,
)

ClientGetRuleGroupResponseRuleGroupRulesStatementByteMatchStatementFieldToMatchSingleQueryArgumentTypeDef = TypedDict(
    "ClientGetRuleGroupResponseRuleGroupRulesStatementByteMatchStatementFieldToMatchSingleQueryArgumentTypeDef",
    {"Name": str},
    total=False,
)

ClientGetRuleGroupResponseRuleGroupRulesStatementByteMatchStatementFieldToMatchTypeDef = TypedDict(
    "ClientGetRuleGroupResponseRuleGroupRulesStatementByteMatchStatementFieldToMatchTypeDef",
    {
        "SingleHeader": ClientGetRuleGroupResponseRuleGroupRulesStatementByteMatchStatementFieldToMatchSingleHeaderTypeDef,
        "SingleQueryArgument": ClientGetRuleGroupResponseRuleGroupRulesStatementByteMatchStatementFieldToMatchSingleQueryArgumentTypeDef,
        "AllQueryArguments": Dict[str, Any],
        "UriPath": Dict[str, Any],
        "QueryString": Dict[str, Any],
        "Body": Dict[str, Any],
        "Method": Dict[str, Any],
    },
    total=False,
)

ClientGetRuleGroupResponseRuleGroupRulesStatementByteMatchStatementTextTransformationsTypeDef = TypedDict(
    "ClientGetRuleGroupResponseRuleGroupRulesStatementByteMatchStatementTextTransformationsTypeDef",
    {
        "Priority": int,
        "Type": Literal[
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

ClientGetRuleGroupResponseRuleGroupRulesStatementByteMatchStatementTypeDef = TypedDict(
    "ClientGetRuleGroupResponseRuleGroupRulesStatementByteMatchStatementTypeDef",
    {
        "SearchString": bytes,
        "FieldToMatch": ClientGetRuleGroupResponseRuleGroupRulesStatementByteMatchStatementFieldToMatchTypeDef,
        "TextTransformations": List[
            ClientGetRuleGroupResponseRuleGroupRulesStatementByteMatchStatementTextTransformationsTypeDef
        ],
        "PositionalConstraint": Literal[
            "EXACTLY", "STARTS_WITH", "ENDS_WITH", "CONTAINS", "CONTAINS_WORD"
        ],
    },
    total=False,
)

ClientGetRuleGroupResponseRuleGroupRulesStatementGeoMatchStatementTypeDef = TypedDict(
    "ClientGetRuleGroupResponseRuleGroupRulesStatementGeoMatchStatementTypeDef",
    {
        "CountryCodes": List[
            Literal[
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
            ]
        ]
    },
    total=False,
)

ClientGetRuleGroupResponseRuleGroupRulesStatementIPSetReferenceStatementTypeDef = TypedDict(
    "ClientGetRuleGroupResponseRuleGroupRulesStatementIPSetReferenceStatementTypeDef",
    {"ARN": str},
    total=False,
)

ClientGetRuleGroupResponseRuleGroupRulesStatementManagedRuleGroupStatementExcludedRulesTypeDef = TypedDict(
    "ClientGetRuleGroupResponseRuleGroupRulesStatementManagedRuleGroupStatementExcludedRulesTypeDef",
    {"Name": str},
    total=False,
)

ClientGetRuleGroupResponseRuleGroupRulesStatementManagedRuleGroupStatementTypeDef = TypedDict(
    "ClientGetRuleGroupResponseRuleGroupRulesStatementManagedRuleGroupStatementTypeDef",
    {
        "VendorName": str,
        "Name": str,
        "ExcludedRules": List[
            ClientGetRuleGroupResponseRuleGroupRulesStatementManagedRuleGroupStatementExcludedRulesTypeDef
        ],
    },
    total=False,
)

ClientGetRuleGroupResponseRuleGroupRulesStatementNotStatementTypeDef = TypedDict(
    "ClientGetRuleGroupResponseRuleGroupRulesStatementNotStatementTypeDef",
    {"Statement": Any},
    total=False,
)

ClientGetRuleGroupResponseRuleGroupRulesStatementOrStatementTypeDef = TypedDict(
    "ClientGetRuleGroupResponseRuleGroupRulesStatementOrStatementTypeDef",
    {"Statements": List[Any]},
    total=False,
)

ClientGetRuleGroupResponseRuleGroupRulesStatementRateBasedStatementTypeDef = TypedDict(
    "ClientGetRuleGroupResponseRuleGroupRulesStatementRateBasedStatementTypeDef",
    {"Limit": int, "AggregateKeyType": str, "ScopeDownStatement": Any},
    total=False,
)

ClientGetRuleGroupResponseRuleGroupRulesStatementRegexPatternSetReferenceStatementFieldToMatchSingleHeaderTypeDef = TypedDict(
    "ClientGetRuleGroupResponseRuleGroupRulesStatementRegexPatternSetReferenceStatementFieldToMatchSingleHeaderTypeDef",
    {"Name": str},
    total=False,
)

ClientGetRuleGroupResponseRuleGroupRulesStatementRegexPatternSetReferenceStatementFieldToMatchSingleQueryArgumentTypeDef = TypedDict(
    "ClientGetRuleGroupResponseRuleGroupRulesStatementRegexPatternSetReferenceStatementFieldToMatchSingleQueryArgumentTypeDef",
    {"Name": str},
    total=False,
)

ClientGetRuleGroupResponseRuleGroupRulesStatementRegexPatternSetReferenceStatementFieldToMatchTypeDef = TypedDict(
    "ClientGetRuleGroupResponseRuleGroupRulesStatementRegexPatternSetReferenceStatementFieldToMatchTypeDef",
    {
        "SingleHeader": ClientGetRuleGroupResponseRuleGroupRulesStatementRegexPatternSetReferenceStatementFieldToMatchSingleHeaderTypeDef,
        "SingleQueryArgument": ClientGetRuleGroupResponseRuleGroupRulesStatementRegexPatternSetReferenceStatementFieldToMatchSingleQueryArgumentTypeDef,
        "AllQueryArguments": Dict[str, Any],
        "UriPath": Dict[str, Any],
        "QueryString": Dict[str, Any],
        "Body": Dict[str, Any],
        "Method": Dict[str, Any],
    },
    total=False,
)

ClientGetRuleGroupResponseRuleGroupRulesStatementRegexPatternSetReferenceStatementTextTransformationsTypeDef = TypedDict(
    "ClientGetRuleGroupResponseRuleGroupRulesStatementRegexPatternSetReferenceStatementTextTransformationsTypeDef",
    {
        "Priority": int,
        "Type": Literal[
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

ClientGetRuleGroupResponseRuleGroupRulesStatementRegexPatternSetReferenceStatementTypeDef = TypedDict(
    "ClientGetRuleGroupResponseRuleGroupRulesStatementRegexPatternSetReferenceStatementTypeDef",
    {
        "ARN": str,
        "FieldToMatch": ClientGetRuleGroupResponseRuleGroupRulesStatementRegexPatternSetReferenceStatementFieldToMatchTypeDef,
        "TextTransformations": List[
            ClientGetRuleGroupResponseRuleGroupRulesStatementRegexPatternSetReferenceStatementTextTransformationsTypeDef
        ],
    },
    total=False,
)

ClientGetRuleGroupResponseRuleGroupRulesStatementRuleGroupReferenceStatementExcludedRulesTypeDef = TypedDict(
    "ClientGetRuleGroupResponseRuleGroupRulesStatementRuleGroupReferenceStatementExcludedRulesTypeDef",
    {"Name": str},
    total=False,
)

ClientGetRuleGroupResponseRuleGroupRulesStatementRuleGroupReferenceStatementTypeDef = TypedDict(
    "ClientGetRuleGroupResponseRuleGroupRulesStatementRuleGroupReferenceStatementTypeDef",
    {
        "ARN": str,
        "ExcludedRules": List[
            ClientGetRuleGroupResponseRuleGroupRulesStatementRuleGroupReferenceStatementExcludedRulesTypeDef
        ],
    },
    total=False,
)

ClientGetRuleGroupResponseRuleGroupRulesStatementSizeConstraintStatementFieldToMatchSingleHeaderTypeDef = TypedDict(
    "ClientGetRuleGroupResponseRuleGroupRulesStatementSizeConstraintStatementFieldToMatchSingleHeaderTypeDef",
    {"Name": str},
    total=False,
)

ClientGetRuleGroupResponseRuleGroupRulesStatementSizeConstraintStatementFieldToMatchSingleQueryArgumentTypeDef = TypedDict(
    "ClientGetRuleGroupResponseRuleGroupRulesStatementSizeConstraintStatementFieldToMatchSingleQueryArgumentTypeDef",
    {"Name": str},
    total=False,
)

ClientGetRuleGroupResponseRuleGroupRulesStatementSizeConstraintStatementFieldToMatchTypeDef = TypedDict(
    "ClientGetRuleGroupResponseRuleGroupRulesStatementSizeConstraintStatementFieldToMatchTypeDef",
    {
        "SingleHeader": ClientGetRuleGroupResponseRuleGroupRulesStatementSizeConstraintStatementFieldToMatchSingleHeaderTypeDef,
        "SingleQueryArgument": ClientGetRuleGroupResponseRuleGroupRulesStatementSizeConstraintStatementFieldToMatchSingleQueryArgumentTypeDef,
        "AllQueryArguments": Dict[str, Any],
        "UriPath": Dict[str, Any],
        "QueryString": Dict[str, Any],
        "Body": Dict[str, Any],
        "Method": Dict[str, Any],
    },
    total=False,
)

ClientGetRuleGroupResponseRuleGroupRulesStatementSizeConstraintStatementTextTransformationsTypeDef = TypedDict(
    "ClientGetRuleGroupResponseRuleGroupRulesStatementSizeConstraintStatementTextTransformationsTypeDef",
    {
        "Priority": int,
        "Type": Literal[
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

ClientGetRuleGroupResponseRuleGroupRulesStatementSizeConstraintStatementTypeDef = TypedDict(
    "ClientGetRuleGroupResponseRuleGroupRulesStatementSizeConstraintStatementTypeDef",
    {
        "FieldToMatch": ClientGetRuleGroupResponseRuleGroupRulesStatementSizeConstraintStatementFieldToMatchTypeDef,
        "ComparisonOperator": Literal["EQ", "NE", "LE", "LT", "GE", "GT"],
        "Size": int,
        "TextTransformations": List[
            ClientGetRuleGroupResponseRuleGroupRulesStatementSizeConstraintStatementTextTransformationsTypeDef
        ],
    },
    total=False,
)

ClientGetRuleGroupResponseRuleGroupRulesStatementSqliMatchStatementFieldToMatchSingleHeaderTypeDef = TypedDict(
    "ClientGetRuleGroupResponseRuleGroupRulesStatementSqliMatchStatementFieldToMatchSingleHeaderTypeDef",
    {"Name": str},
    total=False,
)

ClientGetRuleGroupResponseRuleGroupRulesStatementSqliMatchStatementFieldToMatchSingleQueryArgumentTypeDef = TypedDict(
    "ClientGetRuleGroupResponseRuleGroupRulesStatementSqliMatchStatementFieldToMatchSingleQueryArgumentTypeDef",
    {"Name": str},
    total=False,
)

ClientGetRuleGroupResponseRuleGroupRulesStatementSqliMatchStatementFieldToMatchTypeDef = TypedDict(
    "ClientGetRuleGroupResponseRuleGroupRulesStatementSqliMatchStatementFieldToMatchTypeDef",
    {
        "SingleHeader": ClientGetRuleGroupResponseRuleGroupRulesStatementSqliMatchStatementFieldToMatchSingleHeaderTypeDef,
        "SingleQueryArgument": ClientGetRuleGroupResponseRuleGroupRulesStatementSqliMatchStatementFieldToMatchSingleQueryArgumentTypeDef,
        "AllQueryArguments": Dict[str, Any],
        "UriPath": Dict[str, Any],
        "QueryString": Dict[str, Any],
        "Body": Dict[str, Any],
        "Method": Dict[str, Any],
    },
    total=False,
)

ClientGetRuleGroupResponseRuleGroupRulesStatementSqliMatchStatementTextTransformationsTypeDef = TypedDict(
    "ClientGetRuleGroupResponseRuleGroupRulesStatementSqliMatchStatementTextTransformationsTypeDef",
    {
        "Priority": int,
        "Type": Literal[
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

ClientGetRuleGroupResponseRuleGroupRulesStatementSqliMatchStatementTypeDef = TypedDict(
    "ClientGetRuleGroupResponseRuleGroupRulesStatementSqliMatchStatementTypeDef",
    {
        "FieldToMatch": ClientGetRuleGroupResponseRuleGroupRulesStatementSqliMatchStatementFieldToMatchTypeDef,
        "TextTransformations": List[
            ClientGetRuleGroupResponseRuleGroupRulesStatementSqliMatchStatementTextTransformationsTypeDef
        ],
    },
    total=False,
)

ClientGetRuleGroupResponseRuleGroupRulesStatementXssMatchStatementFieldToMatchSingleHeaderTypeDef = TypedDict(
    "ClientGetRuleGroupResponseRuleGroupRulesStatementXssMatchStatementFieldToMatchSingleHeaderTypeDef",
    {"Name": str},
    total=False,
)

ClientGetRuleGroupResponseRuleGroupRulesStatementXssMatchStatementFieldToMatchSingleQueryArgumentTypeDef = TypedDict(
    "ClientGetRuleGroupResponseRuleGroupRulesStatementXssMatchStatementFieldToMatchSingleQueryArgumentTypeDef",
    {"Name": str},
    total=False,
)

ClientGetRuleGroupResponseRuleGroupRulesStatementXssMatchStatementFieldToMatchTypeDef = TypedDict(
    "ClientGetRuleGroupResponseRuleGroupRulesStatementXssMatchStatementFieldToMatchTypeDef",
    {
        "SingleHeader": ClientGetRuleGroupResponseRuleGroupRulesStatementXssMatchStatementFieldToMatchSingleHeaderTypeDef,
        "SingleQueryArgument": ClientGetRuleGroupResponseRuleGroupRulesStatementXssMatchStatementFieldToMatchSingleQueryArgumentTypeDef,
        "AllQueryArguments": Dict[str, Any],
        "UriPath": Dict[str, Any],
        "QueryString": Dict[str, Any],
        "Body": Dict[str, Any],
        "Method": Dict[str, Any],
    },
    total=False,
)

ClientGetRuleGroupResponseRuleGroupRulesStatementXssMatchStatementTextTransformationsTypeDef = TypedDict(
    "ClientGetRuleGroupResponseRuleGroupRulesStatementXssMatchStatementTextTransformationsTypeDef",
    {
        "Priority": int,
        "Type": Literal[
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

ClientGetRuleGroupResponseRuleGroupRulesStatementXssMatchStatementTypeDef = TypedDict(
    "ClientGetRuleGroupResponseRuleGroupRulesStatementXssMatchStatementTypeDef",
    {
        "FieldToMatch": ClientGetRuleGroupResponseRuleGroupRulesStatementXssMatchStatementFieldToMatchTypeDef,
        "TextTransformations": List[
            ClientGetRuleGroupResponseRuleGroupRulesStatementXssMatchStatementTextTransformationsTypeDef
        ],
    },
    total=False,
)

ClientGetRuleGroupResponseRuleGroupRulesStatementTypeDef = TypedDict(
    "ClientGetRuleGroupResponseRuleGroupRulesStatementTypeDef",
    {
        "ByteMatchStatement": ClientGetRuleGroupResponseRuleGroupRulesStatementByteMatchStatementTypeDef,
        "SqliMatchStatement": ClientGetRuleGroupResponseRuleGroupRulesStatementSqliMatchStatementTypeDef,
        "XssMatchStatement": ClientGetRuleGroupResponseRuleGroupRulesStatementXssMatchStatementTypeDef,
        "SizeConstraintStatement": ClientGetRuleGroupResponseRuleGroupRulesStatementSizeConstraintStatementTypeDef,
        "GeoMatchStatement": ClientGetRuleGroupResponseRuleGroupRulesStatementGeoMatchStatementTypeDef,
        "RuleGroupReferenceStatement": ClientGetRuleGroupResponseRuleGroupRulesStatementRuleGroupReferenceStatementTypeDef,
        "IPSetReferenceStatement": ClientGetRuleGroupResponseRuleGroupRulesStatementIPSetReferenceStatementTypeDef,
        "RegexPatternSetReferenceStatement": ClientGetRuleGroupResponseRuleGroupRulesStatementRegexPatternSetReferenceStatementTypeDef,
        "RateBasedStatement": ClientGetRuleGroupResponseRuleGroupRulesStatementRateBasedStatementTypeDef,
        "AndStatement": ClientGetRuleGroupResponseRuleGroupRulesStatementAndStatementTypeDef,
        "OrStatement": ClientGetRuleGroupResponseRuleGroupRulesStatementOrStatementTypeDef,
        "NotStatement": ClientGetRuleGroupResponseRuleGroupRulesStatementNotStatementTypeDef,
        "ManagedRuleGroupStatement": ClientGetRuleGroupResponseRuleGroupRulesStatementManagedRuleGroupStatementTypeDef,
    },
    total=False,
)

ClientGetRuleGroupResponseRuleGroupRulesVisibilityConfigTypeDef = TypedDict(
    "ClientGetRuleGroupResponseRuleGroupRulesVisibilityConfigTypeDef",
    {"SampledRequestsEnabled": bool, "CloudWatchMetricsEnabled": bool, "MetricName": str},
    total=False,
)

ClientGetRuleGroupResponseRuleGroupRulesTypeDef = TypedDict(
    "ClientGetRuleGroupResponseRuleGroupRulesTypeDef",
    {
        "Name": str,
        "Priority": int,
        "Statement": ClientGetRuleGroupResponseRuleGroupRulesStatementTypeDef,
        "Action": ClientGetRuleGroupResponseRuleGroupRulesActionTypeDef,
        "OverrideAction": ClientGetRuleGroupResponseRuleGroupRulesOverrideActionTypeDef,
        "VisibilityConfig": ClientGetRuleGroupResponseRuleGroupRulesVisibilityConfigTypeDef,
    },
    total=False,
)

ClientGetRuleGroupResponseRuleGroupVisibilityConfigTypeDef = TypedDict(
    "ClientGetRuleGroupResponseRuleGroupVisibilityConfigTypeDef",
    {"SampledRequestsEnabled": bool, "CloudWatchMetricsEnabled": bool, "MetricName": str},
    total=False,
)

ClientGetRuleGroupResponseRuleGroupTypeDef = TypedDict(
    "ClientGetRuleGroupResponseRuleGroupTypeDef",
    {
        "Name": str,
        "Id": str,
        "Capacity": int,
        "ARN": str,
        "Description": str,
        "Rules": List[ClientGetRuleGroupResponseRuleGroupRulesTypeDef],
        "VisibilityConfig": ClientGetRuleGroupResponseRuleGroupVisibilityConfigTypeDef,
    },
    total=False,
)

ClientGetRuleGroupResponseTypeDef = TypedDict(
    "ClientGetRuleGroupResponseTypeDef",
    {"RuleGroup": ClientGetRuleGroupResponseRuleGroupTypeDef, "LockToken": str},
    total=False,
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
        "RuleNameWithinRuleGroup": str,
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


ClientGetWebAclForResourceResponseWebACLDefaultActionTypeDef = TypedDict(
    "ClientGetWebAclForResourceResponseWebACLDefaultActionTypeDef",
    {"Block": Dict[str, Any], "Allow": Dict[str, Any]},
    total=False,
)

ClientGetWebAclForResourceResponseWebACLRulesActionTypeDef = TypedDict(
    "ClientGetWebAclForResourceResponseWebACLRulesActionTypeDef",
    {"Block": Dict[str, Any], "Allow": Dict[str, Any], "Count": Dict[str, Any]},
    total=False,
)

ClientGetWebAclForResourceResponseWebACLRulesOverrideActionTypeDef = TypedDict(
    "ClientGetWebAclForResourceResponseWebACLRulesOverrideActionTypeDef",
    {"Count": Dict[str, Any], "None": Dict[str, Any]},
    total=False,
)

ClientGetWebAclForResourceResponseWebACLRulesStatementAndStatementTypeDef = TypedDict(
    "ClientGetWebAclForResourceResponseWebACLRulesStatementAndStatementTypeDef",
    {"Statements": List[Any]},
    total=False,
)

ClientGetWebAclForResourceResponseWebACLRulesStatementByteMatchStatementFieldToMatchSingleHeaderTypeDef = TypedDict(
    "ClientGetWebAclForResourceResponseWebACLRulesStatementByteMatchStatementFieldToMatchSingleHeaderTypeDef",
    {"Name": str},
    total=False,
)

ClientGetWebAclForResourceResponseWebACLRulesStatementByteMatchStatementFieldToMatchSingleQueryArgumentTypeDef = TypedDict(
    "ClientGetWebAclForResourceResponseWebACLRulesStatementByteMatchStatementFieldToMatchSingleQueryArgumentTypeDef",
    {"Name": str},
    total=False,
)

ClientGetWebAclForResourceResponseWebACLRulesStatementByteMatchStatementFieldToMatchTypeDef = TypedDict(
    "ClientGetWebAclForResourceResponseWebACLRulesStatementByteMatchStatementFieldToMatchTypeDef",
    {
        "SingleHeader": ClientGetWebAclForResourceResponseWebACLRulesStatementByteMatchStatementFieldToMatchSingleHeaderTypeDef,
        "SingleQueryArgument": ClientGetWebAclForResourceResponseWebACLRulesStatementByteMatchStatementFieldToMatchSingleQueryArgumentTypeDef,
        "AllQueryArguments": Dict[str, Any],
        "UriPath": Dict[str, Any],
        "QueryString": Dict[str, Any],
        "Body": Dict[str, Any],
        "Method": Dict[str, Any],
    },
    total=False,
)

ClientGetWebAclForResourceResponseWebACLRulesStatementByteMatchStatementTextTransformationsTypeDef = TypedDict(
    "ClientGetWebAclForResourceResponseWebACLRulesStatementByteMatchStatementTextTransformationsTypeDef",
    {
        "Priority": int,
        "Type": Literal[
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

ClientGetWebAclForResourceResponseWebACLRulesStatementByteMatchStatementTypeDef = TypedDict(
    "ClientGetWebAclForResourceResponseWebACLRulesStatementByteMatchStatementTypeDef",
    {
        "SearchString": bytes,
        "FieldToMatch": ClientGetWebAclForResourceResponseWebACLRulesStatementByteMatchStatementFieldToMatchTypeDef,
        "TextTransformations": List[
            ClientGetWebAclForResourceResponseWebACLRulesStatementByteMatchStatementTextTransformationsTypeDef
        ],
        "PositionalConstraint": Literal[
            "EXACTLY", "STARTS_WITH", "ENDS_WITH", "CONTAINS", "CONTAINS_WORD"
        ],
    },
    total=False,
)

ClientGetWebAclForResourceResponseWebACLRulesStatementGeoMatchStatementTypeDef = TypedDict(
    "ClientGetWebAclForResourceResponseWebACLRulesStatementGeoMatchStatementTypeDef",
    {
        "CountryCodes": List[
            Literal[
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
            ]
        ]
    },
    total=False,
)

ClientGetWebAclForResourceResponseWebACLRulesStatementIPSetReferenceStatementTypeDef = TypedDict(
    "ClientGetWebAclForResourceResponseWebACLRulesStatementIPSetReferenceStatementTypeDef",
    {"ARN": str},
    total=False,
)

ClientGetWebAclForResourceResponseWebACLRulesStatementManagedRuleGroupStatementExcludedRulesTypeDef = TypedDict(
    "ClientGetWebAclForResourceResponseWebACLRulesStatementManagedRuleGroupStatementExcludedRulesTypeDef",
    {"Name": str},
    total=False,
)

ClientGetWebAclForResourceResponseWebACLRulesStatementManagedRuleGroupStatementTypeDef = TypedDict(
    "ClientGetWebAclForResourceResponseWebACLRulesStatementManagedRuleGroupStatementTypeDef",
    {
        "VendorName": str,
        "Name": str,
        "ExcludedRules": List[
            ClientGetWebAclForResourceResponseWebACLRulesStatementManagedRuleGroupStatementExcludedRulesTypeDef
        ],
    },
    total=False,
)

ClientGetWebAclForResourceResponseWebACLRulesStatementNotStatementTypeDef = TypedDict(
    "ClientGetWebAclForResourceResponseWebACLRulesStatementNotStatementTypeDef",
    {"Statement": Any},
    total=False,
)

ClientGetWebAclForResourceResponseWebACLRulesStatementOrStatementTypeDef = TypedDict(
    "ClientGetWebAclForResourceResponseWebACLRulesStatementOrStatementTypeDef",
    {"Statements": List[Any]},
    total=False,
)

ClientGetWebAclForResourceResponseWebACLRulesStatementRateBasedStatementTypeDef = TypedDict(
    "ClientGetWebAclForResourceResponseWebACLRulesStatementRateBasedStatementTypeDef",
    {"Limit": int, "AggregateKeyType": str, "ScopeDownStatement": Any},
    total=False,
)

ClientGetWebAclForResourceResponseWebACLRulesStatementRegexPatternSetReferenceStatementFieldToMatchSingleHeaderTypeDef = TypedDict(
    "ClientGetWebAclForResourceResponseWebACLRulesStatementRegexPatternSetReferenceStatementFieldToMatchSingleHeaderTypeDef",
    {"Name": str},
    total=False,
)

ClientGetWebAclForResourceResponseWebACLRulesStatementRegexPatternSetReferenceStatementFieldToMatchSingleQueryArgumentTypeDef = TypedDict(
    "ClientGetWebAclForResourceResponseWebACLRulesStatementRegexPatternSetReferenceStatementFieldToMatchSingleQueryArgumentTypeDef",
    {"Name": str},
    total=False,
)

ClientGetWebAclForResourceResponseWebACLRulesStatementRegexPatternSetReferenceStatementFieldToMatchTypeDef = TypedDict(
    "ClientGetWebAclForResourceResponseWebACLRulesStatementRegexPatternSetReferenceStatementFieldToMatchTypeDef",
    {
        "SingleHeader": ClientGetWebAclForResourceResponseWebACLRulesStatementRegexPatternSetReferenceStatementFieldToMatchSingleHeaderTypeDef,
        "SingleQueryArgument": ClientGetWebAclForResourceResponseWebACLRulesStatementRegexPatternSetReferenceStatementFieldToMatchSingleQueryArgumentTypeDef,
        "AllQueryArguments": Dict[str, Any],
        "UriPath": Dict[str, Any],
        "QueryString": Dict[str, Any],
        "Body": Dict[str, Any],
        "Method": Dict[str, Any],
    },
    total=False,
)

ClientGetWebAclForResourceResponseWebACLRulesStatementRegexPatternSetReferenceStatementTextTransformationsTypeDef = TypedDict(
    "ClientGetWebAclForResourceResponseWebACLRulesStatementRegexPatternSetReferenceStatementTextTransformationsTypeDef",
    {
        "Priority": int,
        "Type": Literal[
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

ClientGetWebAclForResourceResponseWebACLRulesStatementRegexPatternSetReferenceStatementTypeDef = TypedDict(
    "ClientGetWebAclForResourceResponseWebACLRulesStatementRegexPatternSetReferenceStatementTypeDef",
    {
        "ARN": str,
        "FieldToMatch": ClientGetWebAclForResourceResponseWebACLRulesStatementRegexPatternSetReferenceStatementFieldToMatchTypeDef,
        "TextTransformations": List[
            ClientGetWebAclForResourceResponseWebACLRulesStatementRegexPatternSetReferenceStatementTextTransformationsTypeDef
        ],
    },
    total=False,
)

ClientGetWebAclForResourceResponseWebACLRulesStatementRuleGroupReferenceStatementExcludedRulesTypeDef = TypedDict(
    "ClientGetWebAclForResourceResponseWebACLRulesStatementRuleGroupReferenceStatementExcludedRulesTypeDef",
    {"Name": str},
    total=False,
)

ClientGetWebAclForResourceResponseWebACLRulesStatementRuleGroupReferenceStatementTypeDef = TypedDict(
    "ClientGetWebAclForResourceResponseWebACLRulesStatementRuleGroupReferenceStatementTypeDef",
    {
        "ARN": str,
        "ExcludedRules": List[
            ClientGetWebAclForResourceResponseWebACLRulesStatementRuleGroupReferenceStatementExcludedRulesTypeDef
        ],
    },
    total=False,
)

ClientGetWebAclForResourceResponseWebACLRulesStatementSizeConstraintStatementFieldToMatchSingleHeaderTypeDef = TypedDict(
    "ClientGetWebAclForResourceResponseWebACLRulesStatementSizeConstraintStatementFieldToMatchSingleHeaderTypeDef",
    {"Name": str},
    total=False,
)

ClientGetWebAclForResourceResponseWebACLRulesStatementSizeConstraintStatementFieldToMatchSingleQueryArgumentTypeDef = TypedDict(
    "ClientGetWebAclForResourceResponseWebACLRulesStatementSizeConstraintStatementFieldToMatchSingleQueryArgumentTypeDef",
    {"Name": str},
    total=False,
)

ClientGetWebAclForResourceResponseWebACLRulesStatementSizeConstraintStatementFieldToMatchTypeDef = TypedDict(
    "ClientGetWebAclForResourceResponseWebACLRulesStatementSizeConstraintStatementFieldToMatchTypeDef",
    {
        "SingleHeader": ClientGetWebAclForResourceResponseWebACLRulesStatementSizeConstraintStatementFieldToMatchSingleHeaderTypeDef,
        "SingleQueryArgument": ClientGetWebAclForResourceResponseWebACLRulesStatementSizeConstraintStatementFieldToMatchSingleQueryArgumentTypeDef,
        "AllQueryArguments": Dict[str, Any],
        "UriPath": Dict[str, Any],
        "QueryString": Dict[str, Any],
        "Body": Dict[str, Any],
        "Method": Dict[str, Any],
    },
    total=False,
)

ClientGetWebAclForResourceResponseWebACLRulesStatementSizeConstraintStatementTextTransformationsTypeDef = TypedDict(
    "ClientGetWebAclForResourceResponseWebACLRulesStatementSizeConstraintStatementTextTransformationsTypeDef",
    {
        "Priority": int,
        "Type": Literal[
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

ClientGetWebAclForResourceResponseWebACLRulesStatementSizeConstraintStatementTypeDef = TypedDict(
    "ClientGetWebAclForResourceResponseWebACLRulesStatementSizeConstraintStatementTypeDef",
    {
        "FieldToMatch": ClientGetWebAclForResourceResponseWebACLRulesStatementSizeConstraintStatementFieldToMatchTypeDef,
        "ComparisonOperator": Literal["EQ", "NE", "LE", "LT", "GE", "GT"],
        "Size": int,
        "TextTransformations": List[
            ClientGetWebAclForResourceResponseWebACLRulesStatementSizeConstraintStatementTextTransformationsTypeDef
        ],
    },
    total=False,
)

ClientGetWebAclForResourceResponseWebACLRulesStatementSqliMatchStatementFieldToMatchSingleHeaderTypeDef = TypedDict(
    "ClientGetWebAclForResourceResponseWebACLRulesStatementSqliMatchStatementFieldToMatchSingleHeaderTypeDef",
    {"Name": str},
    total=False,
)

ClientGetWebAclForResourceResponseWebACLRulesStatementSqliMatchStatementFieldToMatchSingleQueryArgumentTypeDef = TypedDict(
    "ClientGetWebAclForResourceResponseWebACLRulesStatementSqliMatchStatementFieldToMatchSingleQueryArgumentTypeDef",
    {"Name": str},
    total=False,
)

ClientGetWebAclForResourceResponseWebACLRulesStatementSqliMatchStatementFieldToMatchTypeDef = TypedDict(
    "ClientGetWebAclForResourceResponseWebACLRulesStatementSqliMatchStatementFieldToMatchTypeDef",
    {
        "SingleHeader": ClientGetWebAclForResourceResponseWebACLRulesStatementSqliMatchStatementFieldToMatchSingleHeaderTypeDef,
        "SingleQueryArgument": ClientGetWebAclForResourceResponseWebACLRulesStatementSqliMatchStatementFieldToMatchSingleQueryArgumentTypeDef,
        "AllQueryArguments": Dict[str, Any],
        "UriPath": Dict[str, Any],
        "QueryString": Dict[str, Any],
        "Body": Dict[str, Any],
        "Method": Dict[str, Any],
    },
    total=False,
)

ClientGetWebAclForResourceResponseWebACLRulesStatementSqliMatchStatementTextTransformationsTypeDef = TypedDict(
    "ClientGetWebAclForResourceResponseWebACLRulesStatementSqliMatchStatementTextTransformationsTypeDef",
    {
        "Priority": int,
        "Type": Literal[
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

ClientGetWebAclForResourceResponseWebACLRulesStatementSqliMatchStatementTypeDef = TypedDict(
    "ClientGetWebAclForResourceResponseWebACLRulesStatementSqliMatchStatementTypeDef",
    {
        "FieldToMatch": ClientGetWebAclForResourceResponseWebACLRulesStatementSqliMatchStatementFieldToMatchTypeDef,
        "TextTransformations": List[
            ClientGetWebAclForResourceResponseWebACLRulesStatementSqliMatchStatementTextTransformationsTypeDef
        ],
    },
    total=False,
)

ClientGetWebAclForResourceResponseWebACLRulesStatementXssMatchStatementFieldToMatchSingleHeaderTypeDef = TypedDict(
    "ClientGetWebAclForResourceResponseWebACLRulesStatementXssMatchStatementFieldToMatchSingleHeaderTypeDef",
    {"Name": str},
    total=False,
)

ClientGetWebAclForResourceResponseWebACLRulesStatementXssMatchStatementFieldToMatchSingleQueryArgumentTypeDef = TypedDict(
    "ClientGetWebAclForResourceResponseWebACLRulesStatementXssMatchStatementFieldToMatchSingleQueryArgumentTypeDef",
    {"Name": str},
    total=False,
)

ClientGetWebAclForResourceResponseWebACLRulesStatementXssMatchStatementFieldToMatchTypeDef = TypedDict(
    "ClientGetWebAclForResourceResponseWebACLRulesStatementXssMatchStatementFieldToMatchTypeDef",
    {
        "SingleHeader": ClientGetWebAclForResourceResponseWebACLRulesStatementXssMatchStatementFieldToMatchSingleHeaderTypeDef,
        "SingleQueryArgument": ClientGetWebAclForResourceResponseWebACLRulesStatementXssMatchStatementFieldToMatchSingleQueryArgumentTypeDef,
        "AllQueryArguments": Dict[str, Any],
        "UriPath": Dict[str, Any],
        "QueryString": Dict[str, Any],
        "Body": Dict[str, Any],
        "Method": Dict[str, Any],
    },
    total=False,
)

ClientGetWebAclForResourceResponseWebACLRulesStatementXssMatchStatementTextTransformationsTypeDef = TypedDict(
    "ClientGetWebAclForResourceResponseWebACLRulesStatementXssMatchStatementTextTransformationsTypeDef",
    {
        "Priority": int,
        "Type": Literal[
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

ClientGetWebAclForResourceResponseWebACLRulesStatementXssMatchStatementTypeDef = TypedDict(
    "ClientGetWebAclForResourceResponseWebACLRulesStatementXssMatchStatementTypeDef",
    {
        "FieldToMatch": ClientGetWebAclForResourceResponseWebACLRulesStatementXssMatchStatementFieldToMatchTypeDef,
        "TextTransformations": List[
            ClientGetWebAclForResourceResponseWebACLRulesStatementXssMatchStatementTextTransformationsTypeDef
        ],
    },
    total=False,
)

ClientGetWebAclForResourceResponseWebACLRulesStatementTypeDef = TypedDict(
    "ClientGetWebAclForResourceResponseWebACLRulesStatementTypeDef",
    {
        "ByteMatchStatement": ClientGetWebAclForResourceResponseWebACLRulesStatementByteMatchStatementTypeDef,
        "SqliMatchStatement": ClientGetWebAclForResourceResponseWebACLRulesStatementSqliMatchStatementTypeDef,
        "XssMatchStatement": ClientGetWebAclForResourceResponseWebACLRulesStatementXssMatchStatementTypeDef,
        "SizeConstraintStatement": ClientGetWebAclForResourceResponseWebACLRulesStatementSizeConstraintStatementTypeDef,
        "GeoMatchStatement": ClientGetWebAclForResourceResponseWebACLRulesStatementGeoMatchStatementTypeDef,
        "RuleGroupReferenceStatement": ClientGetWebAclForResourceResponseWebACLRulesStatementRuleGroupReferenceStatementTypeDef,
        "IPSetReferenceStatement": ClientGetWebAclForResourceResponseWebACLRulesStatementIPSetReferenceStatementTypeDef,
        "RegexPatternSetReferenceStatement": ClientGetWebAclForResourceResponseWebACLRulesStatementRegexPatternSetReferenceStatementTypeDef,
        "RateBasedStatement": ClientGetWebAclForResourceResponseWebACLRulesStatementRateBasedStatementTypeDef,
        "AndStatement": ClientGetWebAclForResourceResponseWebACLRulesStatementAndStatementTypeDef,
        "OrStatement": ClientGetWebAclForResourceResponseWebACLRulesStatementOrStatementTypeDef,
        "NotStatement": ClientGetWebAclForResourceResponseWebACLRulesStatementNotStatementTypeDef,
        "ManagedRuleGroupStatement": ClientGetWebAclForResourceResponseWebACLRulesStatementManagedRuleGroupStatementTypeDef,
    },
    total=False,
)

ClientGetWebAclForResourceResponseWebACLRulesVisibilityConfigTypeDef = TypedDict(
    "ClientGetWebAclForResourceResponseWebACLRulesVisibilityConfigTypeDef",
    {"SampledRequestsEnabled": bool, "CloudWatchMetricsEnabled": bool, "MetricName": str},
    total=False,
)

ClientGetWebAclForResourceResponseWebACLRulesTypeDef = TypedDict(
    "ClientGetWebAclForResourceResponseWebACLRulesTypeDef",
    {
        "Name": str,
        "Priority": int,
        "Statement": ClientGetWebAclForResourceResponseWebACLRulesStatementTypeDef,
        "Action": ClientGetWebAclForResourceResponseWebACLRulesActionTypeDef,
        "OverrideAction": ClientGetWebAclForResourceResponseWebACLRulesOverrideActionTypeDef,
        "VisibilityConfig": ClientGetWebAclForResourceResponseWebACLRulesVisibilityConfigTypeDef,
    },
    total=False,
)

ClientGetWebAclForResourceResponseWebACLVisibilityConfigTypeDef = TypedDict(
    "ClientGetWebAclForResourceResponseWebACLVisibilityConfigTypeDef",
    {"SampledRequestsEnabled": bool, "CloudWatchMetricsEnabled": bool, "MetricName": str},
    total=False,
)

ClientGetWebAclForResourceResponseWebACLTypeDef = TypedDict(
    "ClientGetWebAclForResourceResponseWebACLTypeDef",
    {
        "Name": str,
        "Id": str,
        "ARN": str,
        "DefaultAction": ClientGetWebAclForResourceResponseWebACLDefaultActionTypeDef,
        "Description": str,
        "Rules": List[ClientGetWebAclForResourceResponseWebACLRulesTypeDef],
        "VisibilityConfig": ClientGetWebAclForResourceResponseWebACLVisibilityConfigTypeDef,
        "Capacity": int,
    },
    total=False,
)

ClientGetWebAclForResourceResponseTypeDef = TypedDict(
    "ClientGetWebAclForResourceResponseTypeDef",
    {"WebACL": ClientGetWebAclForResourceResponseWebACLTypeDef},
    total=False,
)

ClientGetWebAclResponseWebACLDefaultActionTypeDef = TypedDict(
    "ClientGetWebAclResponseWebACLDefaultActionTypeDef",
    {"Block": Dict[str, Any], "Allow": Dict[str, Any]},
    total=False,
)

ClientGetWebAclResponseWebACLRulesActionTypeDef = TypedDict(
    "ClientGetWebAclResponseWebACLRulesActionTypeDef",
    {"Block": Dict[str, Any], "Allow": Dict[str, Any], "Count": Dict[str, Any]},
    total=False,
)

ClientGetWebAclResponseWebACLRulesOverrideActionTypeDef = TypedDict(
    "ClientGetWebAclResponseWebACLRulesOverrideActionTypeDef",
    {"Count": Dict[str, Any], "None": Dict[str, Any]},
    total=False,
)

ClientGetWebAclResponseWebACLRulesStatementAndStatementTypeDef = TypedDict(
    "ClientGetWebAclResponseWebACLRulesStatementAndStatementTypeDef",
    {"Statements": List[Any]},
    total=False,
)

ClientGetWebAclResponseWebACLRulesStatementByteMatchStatementFieldToMatchSingleHeaderTypeDef = TypedDict(
    "ClientGetWebAclResponseWebACLRulesStatementByteMatchStatementFieldToMatchSingleHeaderTypeDef",
    {"Name": str},
    total=False,
)

ClientGetWebAclResponseWebACLRulesStatementByteMatchStatementFieldToMatchSingleQueryArgumentTypeDef = TypedDict(
    "ClientGetWebAclResponseWebACLRulesStatementByteMatchStatementFieldToMatchSingleQueryArgumentTypeDef",
    {"Name": str},
    total=False,
)

ClientGetWebAclResponseWebACLRulesStatementByteMatchStatementFieldToMatchTypeDef = TypedDict(
    "ClientGetWebAclResponseWebACLRulesStatementByteMatchStatementFieldToMatchTypeDef",
    {
        "SingleHeader": ClientGetWebAclResponseWebACLRulesStatementByteMatchStatementFieldToMatchSingleHeaderTypeDef,
        "SingleQueryArgument": ClientGetWebAclResponseWebACLRulesStatementByteMatchStatementFieldToMatchSingleQueryArgumentTypeDef,
        "AllQueryArguments": Dict[str, Any],
        "UriPath": Dict[str, Any],
        "QueryString": Dict[str, Any],
        "Body": Dict[str, Any],
        "Method": Dict[str, Any],
    },
    total=False,
)

ClientGetWebAclResponseWebACLRulesStatementByteMatchStatementTextTransformationsTypeDef = TypedDict(
    "ClientGetWebAclResponseWebACLRulesStatementByteMatchStatementTextTransformationsTypeDef",
    {
        "Priority": int,
        "Type": Literal[
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

ClientGetWebAclResponseWebACLRulesStatementByteMatchStatementTypeDef = TypedDict(
    "ClientGetWebAclResponseWebACLRulesStatementByteMatchStatementTypeDef",
    {
        "SearchString": bytes,
        "FieldToMatch": ClientGetWebAclResponseWebACLRulesStatementByteMatchStatementFieldToMatchTypeDef,
        "TextTransformations": List[
            ClientGetWebAclResponseWebACLRulesStatementByteMatchStatementTextTransformationsTypeDef
        ],
        "PositionalConstraint": Literal[
            "EXACTLY", "STARTS_WITH", "ENDS_WITH", "CONTAINS", "CONTAINS_WORD"
        ],
    },
    total=False,
)

ClientGetWebAclResponseWebACLRulesStatementGeoMatchStatementTypeDef = TypedDict(
    "ClientGetWebAclResponseWebACLRulesStatementGeoMatchStatementTypeDef",
    {
        "CountryCodes": List[
            Literal[
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
            ]
        ]
    },
    total=False,
)

ClientGetWebAclResponseWebACLRulesStatementIPSetReferenceStatementTypeDef = TypedDict(
    "ClientGetWebAclResponseWebACLRulesStatementIPSetReferenceStatementTypeDef",
    {"ARN": str},
    total=False,
)

ClientGetWebAclResponseWebACLRulesStatementManagedRuleGroupStatementExcludedRulesTypeDef = TypedDict(
    "ClientGetWebAclResponseWebACLRulesStatementManagedRuleGroupStatementExcludedRulesTypeDef",
    {"Name": str},
    total=False,
)

ClientGetWebAclResponseWebACLRulesStatementManagedRuleGroupStatementTypeDef = TypedDict(
    "ClientGetWebAclResponseWebACLRulesStatementManagedRuleGroupStatementTypeDef",
    {
        "VendorName": str,
        "Name": str,
        "ExcludedRules": List[
            ClientGetWebAclResponseWebACLRulesStatementManagedRuleGroupStatementExcludedRulesTypeDef
        ],
    },
    total=False,
)

ClientGetWebAclResponseWebACLRulesStatementNotStatementTypeDef = TypedDict(
    "ClientGetWebAclResponseWebACLRulesStatementNotStatementTypeDef",
    {"Statement": Any},
    total=False,
)

ClientGetWebAclResponseWebACLRulesStatementOrStatementTypeDef = TypedDict(
    "ClientGetWebAclResponseWebACLRulesStatementOrStatementTypeDef",
    {"Statements": List[Any]},
    total=False,
)

ClientGetWebAclResponseWebACLRulesStatementRateBasedStatementTypeDef = TypedDict(
    "ClientGetWebAclResponseWebACLRulesStatementRateBasedStatementTypeDef",
    {"Limit": int, "AggregateKeyType": str, "ScopeDownStatement": Any},
    total=False,
)

ClientGetWebAclResponseWebACLRulesStatementRegexPatternSetReferenceStatementFieldToMatchSingleHeaderTypeDef = TypedDict(
    "ClientGetWebAclResponseWebACLRulesStatementRegexPatternSetReferenceStatementFieldToMatchSingleHeaderTypeDef",
    {"Name": str},
    total=False,
)

ClientGetWebAclResponseWebACLRulesStatementRegexPatternSetReferenceStatementFieldToMatchSingleQueryArgumentTypeDef = TypedDict(
    "ClientGetWebAclResponseWebACLRulesStatementRegexPatternSetReferenceStatementFieldToMatchSingleQueryArgumentTypeDef",
    {"Name": str},
    total=False,
)

ClientGetWebAclResponseWebACLRulesStatementRegexPatternSetReferenceStatementFieldToMatchTypeDef = TypedDict(
    "ClientGetWebAclResponseWebACLRulesStatementRegexPatternSetReferenceStatementFieldToMatchTypeDef",
    {
        "SingleHeader": ClientGetWebAclResponseWebACLRulesStatementRegexPatternSetReferenceStatementFieldToMatchSingleHeaderTypeDef,
        "SingleQueryArgument": ClientGetWebAclResponseWebACLRulesStatementRegexPatternSetReferenceStatementFieldToMatchSingleQueryArgumentTypeDef,
        "AllQueryArguments": Dict[str, Any],
        "UriPath": Dict[str, Any],
        "QueryString": Dict[str, Any],
        "Body": Dict[str, Any],
        "Method": Dict[str, Any],
    },
    total=False,
)

ClientGetWebAclResponseWebACLRulesStatementRegexPatternSetReferenceStatementTextTransformationsTypeDef = TypedDict(
    "ClientGetWebAclResponseWebACLRulesStatementRegexPatternSetReferenceStatementTextTransformationsTypeDef",
    {
        "Priority": int,
        "Type": Literal[
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

ClientGetWebAclResponseWebACLRulesStatementRegexPatternSetReferenceStatementTypeDef = TypedDict(
    "ClientGetWebAclResponseWebACLRulesStatementRegexPatternSetReferenceStatementTypeDef",
    {
        "ARN": str,
        "FieldToMatch": ClientGetWebAclResponseWebACLRulesStatementRegexPatternSetReferenceStatementFieldToMatchTypeDef,
        "TextTransformations": List[
            ClientGetWebAclResponseWebACLRulesStatementRegexPatternSetReferenceStatementTextTransformationsTypeDef
        ],
    },
    total=False,
)

ClientGetWebAclResponseWebACLRulesStatementRuleGroupReferenceStatementExcludedRulesTypeDef = TypedDict(
    "ClientGetWebAclResponseWebACLRulesStatementRuleGroupReferenceStatementExcludedRulesTypeDef",
    {"Name": str},
    total=False,
)

ClientGetWebAclResponseWebACLRulesStatementRuleGroupReferenceStatementTypeDef = TypedDict(
    "ClientGetWebAclResponseWebACLRulesStatementRuleGroupReferenceStatementTypeDef",
    {
        "ARN": str,
        "ExcludedRules": List[
            ClientGetWebAclResponseWebACLRulesStatementRuleGroupReferenceStatementExcludedRulesTypeDef
        ],
    },
    total=False,
)

ClientGetWebAclResponseWebACLRulesStatementSizeConstraintStatementFieldToMatchSingleHeaderTypeDef = TypedDict(
    "ClientGetWebAclResponseWebACLRulesStatementSizeConstraintStatementFieldToMatchSingleHeaderTypeDef",
    {"Name": str},
    total=False,
)

ClientGetWebAclResponseWebACLRulesStatementSizeConstraintStatementFieldToMatchSingleQueryArgumentTypeDef = TypedDict(
    "ClientGetWebAclResponseWebACLRulesStatementSizeConstraintStatementFieldToMatchSingleQueryArgumentTypeDef",
    {"Name": str},
    total=False,
)

ClientGetWebAclResponseWebACLRulesStatementSizeConstraintStatementFieldToMatchTypeDef = TypedDict(
    "ClientGetWebAclResponseWebACLRulesStatementSizeConstraintStatementFieldToMatchTypeDef",
    {
        "SingleHeader": ClientGetWebAclResponseWebACLRulesStatementSizeConstraintStatementFieldToMatchSingleHeaderTypeDef,
        "SingleQueryArgument": ClientGetWebAclResponseWebACLRulesStatementSizeConstraintStatementFieldToMatchSingleQueryArgumentTypeDef,
        "AllQueryArguments": Dict[str, Any],
        "UriPath": Dict[str, Any],
        "QueryString": Dict[str, Any],
        "Body": Dict[str, Any],
        "Method": Dict[str, Any],
    },
    total=False,
)

ClientGetWebAclResponseWebACLRulesStatementSizeConstraintStatementTextTransformationsTypeDef = TypedDict(
    "ClientGetWebAclResponseWebACLRulesStatementSizeConstraintStatementTextTransformationsTypeDef",
    {
        "Priority": int,
        "Type": Literal[
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

ClientGetWebAclResponseWebACLRulesStatementSizeConstraintStatementTypeDef = TypedDict(
    "ClientGetWebAclResponseWebACLRulesStatementSizeConstraintStatementTypeDef",
    {
        "FieldToMatch": ClientGetWebAclResponseWebACLRulesStatementSizeConstraintStatementFieldToMatchTypeDef,
        "ComparisonOperator": Literal["EQ", "NE", "LE", "LT", "GE", "GT"],
        "Size": int,
        "TextTransformations": List[
            ClientGetWebAclResponseWebACLRulesStatementSizeConstraintStatementTextTransformationsTypeDef
        ],
    },
    total=False,
)

ClientGetWebAclResponseWebACLRulesStatementSqliMatchStatementFieldToMatchSingleHeaderTypeDef = TypedDict(
    "ClientGetWebAclResponseWebACLRulesStatementSqliMatchStatementFieldToMatchSingleHeaderTypeDef",
    {"Name": str},
    total=False,
)

ClientGetWebAclResponseWebACLRulesStatementSqliMatchStatementFieldToMatchSingleQueryArgumentTypeDef = TypedDict(
    "ClientGetWebAclResponseWebACLRulesStatementSqliMatchStatementFieldToMatchSingleQueryArgumentTypeDef",
    {"Name": str},
    total=False,
)

ClientGetWebAclResponseWebACLRulesStatementSqliMatchStatementFieldToMatchTypeDef = TypedDict(
    "ClientGetWebAclResponseWebACLRulesStatementSqliMatchStatementFieldToMatchTypeDef",
    {
        "SingleHeader": ClientGetWebAclResponseWebACLRulesStatementSqliMatchStatementFieldToMatchSingleHeaderTypeDef,
        "SingleQueryArgument": ClientGetWebAclResponseWebACLRulesStatementSqliMatchStatementFieldToMatchSingleQueryArgumentTypeDef,
        "AllQueryArguments": Dict[str, Any],
        "UriPath": Dict[str, Any],
        "QueryString": Dict[str, Any],
        "Body": Dict[str, Any],
        "Method": Dict[str, Any],
    },
    total=False,
)

ClientGetWebAclResponseWebACLRulesStatementSqliMatchStatementTextTransformationsTypeDef = TypedDict(
    "ClientGetWebAclResponseWebACLRulesStatementSqliMatchStatementTextTransformationsTypeDef",
    {
        "Priority": int,
        "Type": Literal[
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

ClientGetWebAclResponseWebACLRulesStatementSqliMatchStatementTypeDef = TypedDict(
    "ClientGetWebAclResponseWebACLRulesStatementSqliMatchStatementTypeDef",
    {
        "FieldToMatch": ClientGetWebAclResponseWebACLRulesStatementSqliMatchStatementFieldToMatchTypeDef,
        "TextTransformations": List[
            ClientGetWebAclResponseWebACLRulesStatementSqliMatchStatementTextTransformationsTypeDef
        ],
    },
    total=False,
)

ClientGetWebAclResponseWebACLRulesStatementXssMatchStatementFieldToMatchSingleHeaderTypeDef = TypedDict(
    "ClientGetWebAclResponseWebACLRulesStatementXssMatchStatementFieldToMatchSingleHeaderTypeDef",
    {"Name": str},
    total=False,
)

ClientGetWebAclResponseWebACLRulesStatementXssMatchStatementFieldToMatchSingleQueryArgumentTypeDef = TypedDict(
    "ClientGetWebAclResponseWebACLRulesStatementXssMatchStatementFieldToMatchSingleQueryArgumentTypeDef",
    {"Name": str},
    total=False,
)

ClientGetWebAclResponseWebACLRulesStatementXssMatchStatementFieldToMatchTypeDef = TypedDict(
    "ClientGetWebAclResponseWebACLRulesStatementXssMatchStatementFieldToMatchTypeDef",
    {
        "SingleHeader": ClientGetWebAclResponseWebACLRulesStatementXssMatchStatementFieldToMatchSingleHeaderTypeDef,
        "SingleQueryArgument": ClientGetWebAclResponseWebACLRulesStatementXssMatchStatementFieldToMatchSingleQueryArgumentTypeDef,
        "AllQueryArguments": Dict[str, Any],
        "UriPath": Dict[str, Any],
        "QueryString": Dict[str, Any],
        "Body": Dict[str, Any],
        "Method": Dict[str, Any],
    },
    total=False,
)

ClientGetWebAclResponseWebACLRulesStatementXssMatchStatementTextTransformationsTypeDef = TypedDict(
    "ClientGetWebAclResponseWebACLRulesStatementXssMatchStatementTextTransformationsTypeDef",
    {
        "Priority": int,
        "Type": Literal[
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

ClientGetWebAclResponseWebACLRulesStatementXssMatchStatementTypeDef = TypedDict(
    "ClientGetWebAclResponseWebACLRulesStatementXssMatchStatementTypeDef",
    {
        "FieldToMatch": ClientGetWebAclResponseWebACLRulesStatementXssMatchStatementFieldToMatchTypeDef,
        "TextTransformations": List[
            ClientGetWebAclResponseWebACLRulesStatementXssMatchStatementTextTransformationsTypeDef
        ],
    },
    total=False,
)

ClientGetWebAclResponseWebACLRulesStatementTypeDef = TypedDict(
    "ClientGetWebAclResponseWebACLRulesStatementTypeDef",
    {
        "ByteMatchStatement": ClientGetWebAclResponseWebACLRulesStatementByteMatchStatementTypeDef,
        "SqliMatchStatement": ClientGetWebAclResponseWebACLRulesStatementSqliMatchStatementTypeDef,
        "XssMatchStatement": ClientGetWebAclResponseWebACLRulesStatementXssMatchStatementTypeDef,
        "SizeConstraintStatement": ClientGetWebAclResponseWebACLRulesStatementSizeConstraintStatementTypeDef,
        "GeoMatchStatement": ClientGetWebAclResponseWebACLRulesStatementGeoMatchStatementTypeDef,
        "RuleGroupReferenceStatement": ClientGetWebAclResponseWebACLRulesStatementRuleGroupReferenceStatementTypeDef,
        "IPSetReferenceStatement": ClientGetWebAclResponseWebACLRulesStatementIPSetReferenceStatementTypeDef,
        "RegexPatternSetReferenceStatement": ClientGetWebAclResponseWebACLRulesStatementRegexPatternSetReferenceStatementTypeDef,
        "RateBasedStatement": ClientGetWebAclResponseWebACLRulesStatementRateBasedStatementTypeDef,
        "AndStatement": ClientGetWebAclResponseWebACLRulesStatementAndStatementTypeDef,
        "OrStatement": ClientGetWebAclResponseWebACLRulesStatementOrStatementTypeDef,
        "NotStatement": ClientGetWebAclResponseWebACLRulesStatementNotStatementTypeDef,
        "ManagedRuleGroupStatement": ClientGetWebAclResponseWebACLRulesStatementManagedRuleGroupStatementTypeDef,
    },
    total=False,
)

ClientGetWebAclResponseWebACLRulesVisibilityConfigTypeDef = TypedDict(
    "ClientGetWebAclResponseWebACLRulesVisibilityConfigTypeDef",
    {"SampledRequestsEnabled": bool, "CloudWatchMetricsEnabled": bool, "MetricName": str},
    total=False,
)

ClientGetWebAclResponseWebACLRulesTypeDef = TypedDict(
    "ClientGetWebAclResponseWebACLRulesTypeDef",
    {
        "Name": str,
        "Priority": int,
        "Statement": ClientGetWebAclResponseWebACLRulesStatementTypeDef,
        "Action": ClientGetWebAclResponseWebACLRulesActionTypeDef,
        "OverrideAction": ClientGetWebAclResponseWebACLRulesOverrideActionTypeDef,
        "VisibilityConfig": ClientGetWebAclResponseWebACLRulesVisibilityConfigTypeDef,
    },
    total=False,
)

ClientGetWebAclResponseWebACLVisibilityConfigTypeDef = TypedDict(
    "ClientGetWebAclResponseWebACLVisibilityConfigTypeDef",
    {"SampledRequestsEnabled": bool, "CloudWatchMetricsEnabled": bool, "MetricName": str},
    total=False,
)

ClientGetWebAclResponseWebACLTypeDef = TypedDict(
    "ClientGetWebAclResponseWebACLTypeDef",
    {
        "Name": str,
        "Id": str,
        "ARN": str,
        "DefaultAction": ClientGetWebAclResponseWebACLDefaultActionTypeDef,
        "Description": str,
        "Rules": List[ClientGetWebAclResponseWebACLRulesTypeDef],
        "VisibilityConfig": ClientGetWebAclResponseWebACLVisibilityConfigTypeDef,
        "Capacity": int,
    },
    total=False,
)

ClientGetWebAclResponseTypeDef = TypedDict(
    "ClientGetWebAclResponseTypeDef",
    {"WebACL": ClientGetWebAclResponseWebACLTypeDef, "LockToken": str},
    total=False,
)

ClientListAvailableManagedRuleGroupsResponseManagedRuleGroupsTypeDef = TypedDict(
    "ClientListAvailableManagedRuleGroupsResponseManagedRuleGroupsTypeDef",
    {"VendorName": str, "Name": str, "Description": str},
    total=False,
)

ClientListAvailableManagedRuleGroupsResponseTypeDef = TypedDict(
    "ClientListAvailableManagedRuleGroupsResponseTypeDef",
    {
        "NextMarker": str,
        "ManagedRuleGroups": List[
            ClientListAvailableManagedRuleGroupsResponseManagedRuleGroupsTypeDef
        ],
    },
    total=False,
)

ClientListIpSetsResponseIPSetsTypeDef = TypedDict(
    "ClientListIpSetsResponseIPSetsTypeDef",
    {"Name": str, "Id": str, "Description": str, "LockToken": str, "ARN": str},
    total=False,
)

ClientListIpSetsResponseTypeDef = TypedDict(
    "ClientListIpSetsResponseTypeDef",
    {"NextMarker": str, "IPSets": List[ClientListIpSetsResponseIPSetsTypeDef]},
    total=False,
)

ClientListLoggingConfigurationsResponseLoggingConfigurationsRedactedFieldsSingleHeaderTypeDef = TypedDict(
    "ClientListLoggingConfigurationsResponseLoggingConfigurationsRedactedFieldsSingleHeaderTypeDef",
    {"Name": str},
    total=False,
)

ClientListLoggingConfigurationsResponseLoggingConfigurationsRedactedFieldsSingleQueryArgumentTypeDef = TypedDict(
    "ClientListLoggingConfigurationsResponseLoggingConfigurationsRedactedFieldsSingleQueryArgumentTypeDef",
    {"Name": str},
    total=False,
)

ClientListLoggingConfigurationsResponseLoggingConfigurationsRedactedFieldsTypeDef = TypedDict(
    "ClientListLoggingConfigurationsResponseLoggingConfigurationsRedactedFieldsTypeDef",
    {
        "SingleHeader": ClientListLoggingConfigurationsResponseLoggingConfigurationsRedactedFieldsSingleHeaderTypeDef,
        "SingleQueryArgument": ClientListLoggingConfigurationsResponseLoggingConfigurationsRedactedFieldsSingleQueryArgumentTypeDef,
        "AllQueryArguments": Dict[str, Any],
        "UriPath": Dict[str, Any],
        "QueryString": Dict[str, Any],
        "Body": Dict[str, Any],
        "Method": Dict[str, Any],
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

ClientListRegexPatternSetsResponseRegexPatternSetsTypeDef = TypedDict(
    "ClientListRegexPatternSetsResponseRegexPatternSetsTypeDef",
    {"Name": str, "Id": str, "Description": str, "LockToken": str, "ARN": str},
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
    "ClientListRuleGroupsResponseRuleGroupsTypeDef",
    {"Name": str, "Id": str, "Description": str, "LockToken": str, "ARN": str},
    total=False,
)

ClientListRuleGroupsResponseTypeDef = TypedDict(
    "ClientListRuleGroupsResponseTypeDef",
    {"NextMarker": str, "RuleGroups": List[ClientListRuleGroupsResponseRuleGroupsTypeDef]},
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
    "ClientListWebAclsResponseWebACLsTypeDef",
    {"Name": str, "Id": str, "Description": str, "LockToken": str, "ARN": str},
    total=False,
)

ClientListWebAclsResponseTypeDef = TypedDict(
    "ClientListWebAclsResponseTypeDef",
    {"NextMarker": str, "WebACLs": List[ClientListWebAclsResponseWebACLsTypeDef]},
    total=False,
)

ClientPutLoggingConfigurationLoggingConfigurationRedactedFieldsSingleHeaderTypeDef = TypedDict(
    "ClientPutLoggingConfigurationLoggingConfigurationRedactedFieldsSingleHeaderTypeDef",
    {"Name": str},
    total=False,
)

ClientPutLoggingConfigurationLoggingConfigurationRedactedFieldsSingleQueryArgumentTypeDef = TypedDict(
    "ClientPutLoggingConfigurationLoggingConfigurationRedactedFieldsSingleQueryArgumentTypeDef",
    {"Name": str},
    total=False,
)

ClientPutLoggingConfigurationLoggingConfigurationRedactedFieldsTypeDef = TypedDict(
    "ClientPutLoggingConfigurationLoggingConfigurationRedactedFieldsTypeDef",
    {
        "SingleHeader": ClientPutLoggingConfigurationLoggingConfigurationRedactedFieldsSingleHeaderTypeDef,
        "SingleQueryArgument": ClientPutLoggingConfigurationLoggingConfigurationRedactedFieldsSingleQueryArgumentTypeDef,
        "AllQueryArguments": Dict[str, Any],
        "UriPath": Dict[str, Any],
        "QueryString": Dict[str, Any],
        "Body": Dict[str, Any],
        "Method": Dict[str, Any],
    },
    total=False,
)

_RequiredClientPutLoggingConfigurationLoggingConfigurationTypeDef = TypedDict(
    "_RequiredClientPutLoggingConfigurationLoggingConfigurationTypeDef", {"ResourceArn": str}
)
_OptionalClientPutLoggingConfigurationLoggingConfigurationTypeDef = TypedDict(
    "_OptionalClientPutLoggingConfigurationLoggingConfigurationTypeDef",
    {
        "LogDestinationConfigs": List[str],
        "RedactedFields": List[
            ClientPutLoggingConfigurationLoggingConfigurationRedactedFieldsTypeDef
        ],
    },
    total=False,
)


class ClientPutLoggingConfigurationLoggingConfigurationTypeDef(
    _RequiredClientPutLoggingConfigurationLoggingConfigurationTypeDef,
    _OptionalClientPutLoggingConfigurationLoggingConfigurationTypeDef,
):
    pass


ClientPutLoggingConfigurationResponseLoggingConfigurationRedactedFieldsSingleHeaderTypeDef = TypedDict(
    "ClientPutLoggingConfigurationResponseLoggingConfigurationRedactedFieldsSingleHeaderTypeDef",
    {"Name": str},
    total=False,
)

ClientPutLoggingConfigurationResponseLoggingConfigurationRedactedFieldsSingleQueryArgumentTypeDef = TypedDict(
    "ClientPutLoggingConfigurationResponseLoggingConfigurationRedactedFieldsSingleQueryArgumentTypeDef",
    {"Name": str},
    total=False,
)

ClientPutLoggingConfigurationResponseLoggingConfigurationRedactedFieldsTypeDef = TypedDict(
    "ClientPutLoggingConfigurationResponseLoggingConfigurationRedactedFieldsTypeDef",
    {
        "SingleHeader": ClientPutLoggingConfigurationResponseLoggingConfigurationRedactedFieldsSingleHeaderTypeDef,
        "SingleQueryArgument": ClientPutLoggingConfigurationResponseLoggingConfigurationRedactedFieldsSingleQueryArgumentTypeDef,
        "AllQueryArguments": Dict[str, Any],
        "UriPath": Dict[str, Any],
        "QueryString": Dict[str, Any],
        "Body": Dict[str, Any],
        "Method": Dict[str, Any],
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

ClientUpdateIpSetResponseTypeDef = TypedDict(
    "ClientUpdateIpSetResponseTypeDef", {"NextLockToken": str}, total=False
)

ClientUpdateRegexPatternSetRegularExpressionListTypeDef = TypedDict(
    "ClientUpdateRegexPatternSetRegularExpressionListTypeDef", {"RegexString": str}, total=False
)

ClientUpdateRegexPatternSetResponseTypeDef = TypedDict(
    "ClientUpdateRegexPatternSetResponseTypeDef", {"NextLockToken": str}, total=False
)

ClientUpdateRuleGroupResponseTypeDef = TypedDict(
    "ClientUpdateRuleGroupResponseTypeDef", {"NextLockToken": str}, total=False
)

ClientUpdateRuleGroupRulesActionTypeDef = TypedDict(
    "ClientUpdateRuleGroupRulesActionTypeDef",
    {"Block": Dict[str, Any], "Allow": Dict[str, Any], "Count": Dict[str, Any]},
    total=False,
)

ClientUpdateRuleGroupRulesOverrideActionTypeDef = TypedDict(
    "ClientUpdateRuleGroupRulesOverrideActionTypeDef",
    {"Count": Dict[str, Any], "None": Dict[str, Any]},
    total=False,
)

ClientUpdateRuleGroupRulesStatementAndStatementTypeDef = TypedDict(
    "ClientUpdateRuleGroupRulesStatementAndStatementTypeDef", {"Statements": List[Any]}, total=False
)

ClientUpdateRuleGroupRulesStatementByteMatchStatementFieldToMatchSingleHeaderTypeDef = TypedDict(
    "ClientUpdateRuleGroupRulesStatementByteMatchStatementFieldToMatchSingleHeaderTypeDef",
    {"Name": str},
    total=False,
)

ClientUpdateRuleGroupRulesStatementByteMatchStatementFieldToMatchSingleQueryArgumentTypeDef = TypedDict(
    "ClientUpdateRuleGroupRulesStatementByteMatchStatementFieldToMatchSingleQueryArgumentTypeDef",
    {"Name": str},
    total=False,
)

ClientUpdateRuleGroupRulesStatementByteMatchStatementFieldToMatchTypeDef = TypedDict(
    "ClientUpdateRuleGroupRulesStatementByteMatchStatementFieldToMatchTypeDef",
    {
        "SingleHeader": ClientUpdateRuleGroupRulesStatementByteMatchStatementFieldToMatchSingleHeaderTypeDef,
        "SingleQueryArgument": ClientUpdateRuleGroupRulesStatementByteMatchStatementFieldToMatchSingleQueryArgumentTypeDef,
        "AllQueryArguments": Dict[str, Any],
        "UriPath": Dict[str, Any],
        "QueryString": Dict[str, Any],
        "Body": Dict[str, Any],
        "Method": Dict[str, Any],
    },
    total=False,
)

ClientUpdateRuleGroupRulesStatementByteMatchStatementTextTransformationsTypeDef = TypedDict(
    "ClientUpdateRuleGroupRulesStatementByteMatchStatementTextTransformationsTypeDef",
    {
        "Priority": int,
        "Type": Literal[
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

ClientUpdateRuleGroupRulesStatementByteMatchStatementTypeDef = TypedDict(
    "ClientUpdateRuleGroupRulesStatementByteMatchStatementTypeDef",
    {
        "SearchString": bytes,
        "FieldToMatch": ClientUpdateRuleGroupRulesStatementByteMatchStatementFieldToMatchTypeDef,
        "TextTransformations": List[
            ClientUpdateRuleGroupRulesStatementByteMatchStatementTextTransformationsTypeDef
        ],
        "PositionalConstraint": Literal[
            "EXACTLY", "STARTS_WITH", "ENDS_WITH", "CONTAINS", "CONTAINS_WORD"
        ],
    },
    total=False,
)

ClientUpdateRuleGroupRulesStatementGeoMatchStatementTypeDef = TypedDict(
    "ClientUpdateRuleGroupRulesStatementGeoMatchStatementTypeDef",
    {
        "CountryCodes": List[
            Literal[
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
            ]
        ]
    },
    total=False,
)

ClientUpdateRuleGroupRulesStatementIPSetReferenceStatementTypeDef = TypedDict(
    "ClientUpdateRuleGroupRulesStatementIPSetReferenceStatementTypeDef", {"ARN": str}, total=False
)

ClientUpdateRuleGroupRulesStatementManagedRuleGroupStatementExcludedRulesTypeDef = TypedDict(
    "ClientUpdateRuleGroupRulesStatementManagedRuleGroupStatementExcludedRulesTypeDef",
    {"Name": str},
    total=False,
)

ClientUpdateRuleGroupRulesStatementManagedRuleGroupStatementTypeDef = TypedDict(
    "ClientUpdateRuleGroupRulesStatementManagedRuleGroupStatementTypeDef",
    {
        "VendorName": str,
        "Name": str,
        "ExcludedRules": List[
            ClientUpdateRuleGroupRulesStatementManagedRuleGroupStatementExcludedRulesTypeDef
        ],
    },
    total=False,
)

ClientUpdateRuleGroupRulesStatementNotStatementTypeDef = TypedDict(
    "ClientUpdateRuleGroupRulesStatementNotStatementTypeDef", {"Statement": Any}, total=False
)

ClientUpdateRuleGroupRulesStatementOrStatementTypeDef = TypedDict(
    "ClientUpdateRuleGroupRulesStatementOrStatementTypeDef", {"Statements": List[Any]}, total=False
)

ClientUpdateRuleGroupRulesStatementRateBasedStatementTypeDef = TypedDict(
    "ClientUpdateRuleGroupRulesStatementRateBasedStatementTypeDef",
    {"Limit": int, "AggregateKeyType": str, "ScopeDownStatement": Any},
    total=False,
)

ClientUpdateRuleGroupRulesStatementRegexPatternSetReferenceStatementFieldToMatchSingleHeaderTypeDef = TypedDict(
    "ClientUpdateRuleGroupRulesStatementRegexPatternSetReferenceStatementFieldToMatchSingleHeaderTypeDef",
    {"Name": str},
    total=False,
)

ClientUpdateRuleGroupRulesStatementRegexPatternSetReferenceStatementFieldToMatchSingleQueryArgumentTypeDef = TypedDict(
    "ClientUpdateRuleGroupRulesStatementRegexPatternSetReferenceStatementFieldToMatchSingleQueryArgumentTypeDef",
    {"Name": str},
    total=False,
)

ClientUpdateRuleGroupRulesStatementRegexPatternSetReferenceStatementFieldToMatchTypeDef = TypedDict(
    "ClientUpdateRuleGroupRulesStatementRegexPatternSetReferenceStatementFieldToMatchTypeDef",
    {
        "SingleHeader": ClientUpdateRuleGroupRulesStatementRegexPatternSetReferenceStatementFieldToMatchSingleHeaderTypeDef,
        "SingleQueryArgument": ClientUpdateRuleGroupRulesStatementRegexPatternSetReferenceStatementFieldToMatchSingleQueryArgumentTypeDef,
        "AllQueryArguments": Dict[str, Any],
        "UriPath": Dict[str, Any],
        "QueryString": Dict[str, Any],
        "Body": Dict[str, Any],
        "Method": Dict[str, Any],
    },
    total=False,
)

ClientUpdateRuleGroupRulesStatementRegexPatternSetReferenceStatementTextTransformationsTypeDef = TypedDict(
    "ClientUpdateRuleGroupRulesStatementRegexPatternSetReferenceStatementTextTransformationsTypeDef",
    {
        "Priority": int,
        "Type": Literal[
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

ClientUpdateRuleGroupRulesStatementRegexPatternSetReferenceStatementTypeDef = TypedDict(
    "ClientUpdateRuleGroupRulesStatementRegexPatternSetReferenceStatementTypeDef",
    {
        "ARN": str,
        "FieldToMatch": ClientUpdateRuleGroupRulesStatementRegexPatternSetReferenceStatementFieldToMatchTypeDef,
        "TextTransformations": List[
            ClientUpdateRuleGroupRulesStatementRegexPatternSetReferenceStatementTextTransformationsTypeDef
        ],
    },
    total=False,
)

ClientUpdateRuleGroupRulesStatementRuleGroupReferenceStatementExcludedRulesTypeDef = TypedDict(
    "ClientUpdateRuleGroupRulesStatementRuleGroupReferenceStatementExcludedRulesTypeDef",
    {"Name": str},
    total=False,
)

ClientUpdateRuleGroupRulesStatementRuleGroupReferenceStatementTypeDef = TypedDict(
    "ClientUpdateRuleGroupRulesStatementRuleGroupReferenceStatementTypeDef",
    {
        "ARN": str,
        "ExcludedRules": List[
            ClientUpdateRuleGroupRulesStatementRuleGroupReferenceStatementExcludedRulesTypeDef
        ],
    },
    total=False,
)

ClientUpdateRuleGroupRulesStatementSizeConstraintStatementFieldToMatchSingleHeaderTypeDef = TypedDict(
    "ClientUpdateRuleGroupRulesStatementSizeConstraintStatementFieldToMatchSingleHeaderTypeDef",
    {"Name": str},
    total=False,
)

ClientUpdateRuleGroupRulesStatementSizeConstraintStatementFieldToMatchSingleQueryArgumentTypeDef = TypedDict(
    "ClientUpdateRuleGroupRulesStatementSizeConstraintStatementFieldToMatchSingleQueryArgumentTypeDef",
    {"Name": str},
    total=False,
)

ClientUpdateRuleGroupRulesStatementSizeConstraintStatementFieldToMatchTypeDef = TypedDict(
    "ClientUpdateRuleGroupRulesStatementSizeConstraintStatementFieldToMatchTypeDef",
    {
        "SingleHeader": ClientUpdateRuleGroupRulesStatementSizeConstraintStatementFieldToMatchSingleHeaderTypeDef,
        "SingleQueryArgument": ClientUpdateRuleGroupRulesStatementSizeConstraintStatementFieldToMatchSingleQueryArgumentTypeDef,
        "AllQueryArguments": Dict[str, Any],
        "UriPath": Dict[str, Any],
        "QueryString": Dict[str, Any],
        "Body": Dict[str, Any],
        "Method": Dict[str, Any],
    },
    total=False,
)

ClientUpdateRuleGroupRulesStatementSizeConstraintStatementTextTransformationsTypeDef = TypedDict(
    "ClientUpdateRuleGroupRulesStatementSizeConstraintStatementTextTransformationsTypeDef",
    {
        "Priority": int,
        "Type": Literal[
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

ClientUpdateRuleGroupRulesStatementSizeConstraintStatementTypeDef = TypedDict(
    "ClientUpdateRuleGroupRulesStatementSizeConstraintStatementTypeDef",
    {
        "FieldToMatch": ClientUpdateRuleGroupRulesStatementSizeConstraintStatementFieldToMatchTypeDef,
        "ComparisonOperator": Literal["EQ", "NE", "LE", "LT", "GE", "GT"],
        "Size": int,
        "TextTransformations": List[
            ClientUpdateRuleGroupRulesStatementSizeConstraintStatementTextTransformationsTypeDef
        ],
    },
    total=False,
)

ClientUpdateRuleGroupRulesStatementSqliMatchStatementFieldToMatchSingleHeaderTypeDef = TypedDict(
    "ClientUpdateRuleGroupRulesStatementSqliMatchStatementFieldToMatchSingleHeaderTypeDef",
    {"Name": str},
    total=False,
)

ClientUpdateRuleGroupRulesStatementSqliMatchStatementFieldToMatchSingleQueryArgumentTypeDef = TypedDict(
    "ClientUpdateRuleGroupRulesStatementSqliMatchStatementFieldToMatchSingleQueryArgumentTypeDef",
    {"Name": str},
    total=False,
)

ClientUpdateRuleGroupRulesStatementSqliMatchStatementFieldToMatchTypeDef = TypedDict(
    "ClientUpdateRuleGroupRulesStatementSqliMatchStatementFieldToMatchTypeDef",
    {
        "SingleHeader": ClientUpdateRuleGroupRulesStatementSqliMatchStatementFieldToMatchSingleHeaderTypeDef,
        "SingleQueryArgument": ClientUpdateRuleGroupRulesStatementSqliMatchStatementFieldToMatchSingleQueryArgumentTypeDef,
        "AllQueryArguments": Dict[str, Any],
        "UriPath": Dict[str, Any],
        "QueryString": Dict[str, Any],
        "Body": Dict[str, Any],
        "Method": Dict[str, Any],
    },
    total=False,
)

ClientUpdateRuleGroupRulesStatementSqliMatchStatementTextTransformationsTypeDef = TypedDict(
    "ClientUpdateRuleGroupRulesStatementSqliMatchStatementTextTransformationsTypeDef",
    {
        "Priority": int,
        "Type": Literal[
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

ClientUpdateRuleGroupRulesStatementSqliMatchStatementTypeDef = TypedDict(
    "ClientUpdateRuleGroupRulesStatementSqliMatchStatementTypeDef",
    {
        "FieldToMatch": ClientUpdateRuleGroupRulesStatementSqliMatchStatementFieldToMatchTypeDef,
        "TextTransformations": List[
            ClientUpdateRuleGroupRulesStatementSqliMatchStatementTextTransformationsTypeDef
        ],
    },
    total=False,
)

ClientUpdateRuleGroupRulesStatementXssMatchStatementFieldToMatchSingleHeaderTypeDef = TypedDict(
    "ClientUpdateRuleGroupRulesStatementXssMatchStatementFieldToMatchSingleHeaderTypeDef",
    {"Name": str},
    total=False,
)

ClientUpdateRuleGroupRulesStatementXssMatchStatementFieldToMatchSingleQueryArgumentTypeDef = TypedDict(
    "ClientUpdateRuleGroupRulesStatementXssMatchStatementFieldToMatchSingleQueryArgumentTypeDef",
    {"Name": str},
    total=False,
)

ClientUpdateRuleGroupRulesStatementXssMatchStatementFieldToMatchTypeDef = TypedDict(
    "ClientUpdateRuleGroupRulesStatementXssMatchStatementFieldToMatchTypeDef",
    {
        "SingleHeader": ClientUpdateRuleGroupRulesStatementXssMatchStatementFieldToMatchSingleHeaderTypeDef,
        "SingleQueryArgument": ClientUpdateRuleGroupRulesStatementXssMatchStatementFieldToMatchSingleQueryArgumentTypeDef,
        "AllQueryArguments": Dict[str, Any],
        "UriPath": Dict[str, Any],
        "QueryString": Dict[str, Any],
        "Body": Dict[str, Any],
        "Method": Dict[str, Any],
    },
    total=False,
)

ClientUpdateRuleGroupRulesStatementXssMatchStatementTextTransformationsTypeDef = TypedDict(
    "ClientUpdateRuleGroupRulesStatementXssMatchStatementTextTransformationsTypeDef",
    {
        "Priority": int,
        "Type": Literal[
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

ClientUpdateRuleGroupRulesStatementXssMatchStatementTypeDef = TypedDict(
    "ClientUpdateRuleGroupRulesStatementXssMatchStatementTypeDef",
    {
        "FieldToMatch": ClientUpdateRuleGroupRulesStatementXssMatchStatementFieldToMatchTypeDef,
        "TextTransformations": List[
            ClientUpdateRuleGroupRulesStatementXssMatchStatementTextTransformationsTypeDef
        ],
    },
    total=False,
)

ClientUpdateRuleGroupRulesStatementTypeDef = TypedDict(
    "ClientUpdateRuleGroupRulesStatementTypeDef",
    {
        "ByteMatchStatement": ClientUpdateRuleGroupRulesStatementByteMatchStatementTypeDef,
        "SqliMatchStatement": ClientUpdateRuleGroupRulesStatementSqliMatchStatementTypeDef,
        "XssMatchStatement": ClientUpdateRuleGroupRulesStatementXssMatchStatementTypeDef,
        "SizeConstraintStatement": ClientUpdateRuleGroupRulesStatementSizeConstraintStatementTypeDef,
        "GeoMatchStatement": ClientUpdateRuleGroupRulesStatementGeoMatchStatementTypeDef,
        "RuleGroupReferenceStatement": ClientUpdateRuleGroupRulesStatementRuleGroupReferenceStatementTypeDef,
        "IPSetReferenceStatement": ClientUpdateRuleGroupRulesStatementIPSetReferenceStatementTypeDef,
        "RegexPatternSetReferenceStatement": ClientUpdateRuleGroupRulesStatementRegexPatternSetReferenceStatementTypeDef,
        "RateBasedStatement": ClientUpdateRuleGroupRulesStatementRateBasedStatementTypeDef,
        "AndStatement": ClientUpdateRuleGroupRulesStatementAndStatementTypeDef,
        "OrStatement": ClientUpdateRuleGroupRulesStatementOrStatementTypeDef,
        "NotStatement": ClientUpdateRuleGroupRulesStatementNotStatementTypeDef,
        "ManagedRuleGroupStatement": ClientUpdateRuleGroupRulesStatementManagedRuleGroupStatementTypeDef,
    },
    total=False,
)

ClientUpdateRuleGroupRulesVisibilityConfigTypeDef = TypedDict(
    "ClientUpdateRuleGroupRulesVisibilityConfigTypeDef",
    {"SampledRequestsEnabled": bool, "CloudWatchMetricsEnabled": bool, "MetricName": str},
    total=False,
)

ClientUpdateRuleGroupRulesTypeDef = TypedDict(
    "ClientUpdateRuleGroupRulesTypeDef",
    {
        "Name": str,
        "Priority": int,
        "Statement": ClientUpdateRuleGroupRulesStatementTypeDef,
        "Action": ClientUpdateRuleGroupRulesActionTypeDef,
        "OverrideAction": ClientUpdateRuleGroupRulesOverrideActionTypeDef,
        "VisibilityConfig": ClientUpdateRuleGroupRulesVisibilityConfigTypeDef,
    },
    total=False,
)

_RequiredClientUpdateRuleGroupVisibilityConfigTypeDef = TypedDict(
    "_RequiredClientUpdateRuleGroupVisibilityConfigTypeDef", {"SampledRequestsEnabled": bool}
)
_OptionalClientUpdateRuleGroupVisibilityConfigTypeDef = TypedDict(
    "_OptionalClientUpdateRuleGroupVisibilityConfigTypeDef",
    {"CloudWatchMetricsEnabled": bool, "MetricName": str},
    total=False,
)


class ClientUpdateRuleGroupVisibilityConfigTypeDef(
    _RequiredClientUpdateRuleGroupVisibilityConfigTypeDef,
    _OptionalClientUpdateRuleGroupVisibilityConfigTypeDef,
):
    pass


ClientUpdateWebAclDefaultActionTypeDef = TypedDict(
    "ClientUpdateWebAclDefaultActionTypeDef",
    {"Block": Dict[str, Any], "Allow": Dict[str, Any]},
    total=False,
)

ClientUpdateWebAclResponseTypeDef = TypedDict(
    "ClientUpdateWebAclResponseTypeDef", {"NextLockToken": str}, total=False
)

ClientUpdateWebAclRulesActionTypeDef = TypedDict(
    "ClientUpdateWebAclRulesActionTypeDef",
    {"Block": Dict[str, Any], "Allow": Dict[str, Any], "Count": Dict[str, Any]},
    total=False,
)

ClientUpdateWebAclRulesOverrideActionTypeDef = TypedDict(
    "ClientUpdateWebAclRulesOverrideActionTypeDef",
    {"Count": Dict[str, Any], "None": Dict[str, Any]},
    total=False,
)

ClientUpdateWebAclRulesStatementAndStatementTypeDef = TypedDict(
    "ClientUpdateWebAclRulesStatementAndStatementTypeDef", {"Statements": List[Any]}, total=False
)

ClientUpdateWebAclRulesStatementByteMatchStatementFieldToMatchSingleHeaderTypeDef = TypedDict(
    "ClientUpdateWebAclRulesStatementByteMatchStatementFieldToMatchSingleHeaderTypeDef",
    {"Name": str},
    total=False,
)

ClientUpdateWebAclRulesStatementByteMatchStatementFieldToMatchSingleQueryArgumentTypeDef = TypedDict(
    "ClientUpdateWebAclRulesStatementByteMatchStatementFieldToMatchSingleQueryArgumentTypeDef",
    {"Name": str},
    total=False,
)

ClientUpdateWebAclRulesStatementByteMatchStatementFieldToMatchTypeDef = TypedDict(
    "ClientUpdateWebAclRulesStatementByteMatchStatementFieldToMatchTypeDef",
    {
        "SingleHeader": ClientUpdateWebAclRulesStatementByteMatchStatementFieldToMatchSingleHeaderTypeDef,
        "SingleQueryArgument": ClientUpdateWebAclRulesStatementByteMatchStatementFieldToMatchSingleQueryArgumentTypeDef,
        "AllQueryArguments": Dict[str, Any],
        "UriPath": Dict[str, Any],
        "QueryString": Dict[str, Any],
        "Body": Dict[str, Any],
        "Method": Dict[str, Any],
    },
    total=False,
)

ClientUpdateWebAclRulesStatementByteMatchStatementTextTransformationsTypeDef = TypedDict(
    "ClientUpdateWebAclRulesStatementByteMatchStatementTextTransformationsTypeDef",
    {
        "Priority": int,
        "Type": Literal[
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

ClientUpdateWebAclRulesStatementByteMatchStatementTypeDef = TypedDict(
    "ClientUpdateWebAclRulesStatementByteMatchStatementTypeDef",
    {
        "SearchString": bytes,
        "FieldToMatch": ClientUpdateWebAclRulesStatementByteMatchStatementFieldToMatchTypeDef,
        "TextTransformations": List[
            ClientUpdateWebAclRulesStatementByteMatchStatementTextTransformationsTypeDef
        ],
        "PositionalConstraint": Literal[
            "EXACTLY", "STARTS_WITH", "ENDS_WITH", "CONTAINS", "CONTAINS_WORD"
        ],
    },
    total=False,
)

ClientUpdateWebAclRulesStatementGeoMatchStatementTypeDef = TypedDict(
    "ClientUpdateWebAclRulesStatementGeoMatchStatementTypeDef",
    {
        "CountryCodes": List[
            Literal[
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
            ]
        ]
    },
    total=False,
)

ClientUpdateWebAclRulesStatementIPSetReferenceStatementTypeDef = TypedDict(
    "ClientUpdateWebAclRulesStatementIPSetReferenceStatementTypeDef", {"ARN": str}, total=False
)

ClientUpdateWebAclRulesStatementManagedRuleGroupStatementExcludedRulesTypeDef = TypedDict(
    "ClientUpdateWebAclRulesStatementManagedRuleGroupStatementExcludedRulesTypeDef",
    {"Name": str},
    total=False,
)

ClientUpdateWebAclRulesStatementManagedRuleGroupStatementTypeDef = TypedDict(
    "ClientUpdateWebAclRulesStatementManagedRuleGroupStatementTypeDef",
    {
        "VendorName": str,
        "Name": str,
        "ExcludedRules": List[
            ClientUpdateWebAclRulesStatementManagedRuleGroupStatementExcludedRulesTypeDef
        ],
    },
    total=False,
)

ClientUpdateWebAclRulesStatementNotStatementTypeDef = TypedDict(
    "ClientUpdateWebAclRulesStatementNotStatementTypeDef", {"Statement": Any}, total=False
)

ClientUpdateWebAclRulesStatementOrStatementTypeDef = TypedDict(
    "ClientUpdateWebAclRulesStatementOrStatementTypeDef", {"Statements": List[Any]}, total=False
)

ClientUpdateWebAclRulesStatementRateBasedStatementTypeDef = TypedDict(
    "ClientUpdateWebAclRulesStatementRateBasedStatementTypeDef",
    {"Limit": int, "AggregateKeyType": str, "ScopeDownStatement": Any},
    total=False,
)

ClientUpdateWebAclRulesStatementRegexPatternSetReferenceStatementFieldToMatchSingleHeaderTypeDef = TypedDict(
    "ClientUpdateWebAclRulesStatementRegexPatternSetReferenceStatementFieldToMatchSingleHeaderTypeDef",
    {"Name": str},
    total=False,
)

ClientUpdateWebAclRulesStatementRegexPatternSetReferenceStatementFieldToMatchSingleQueryArgumentTypeDef = TypedDict(
    "ClientUpdateWebAclRulesStatementRegexPatternSetReferenceStatementFieldToMatchSingleQueryArgumentTypeDef",
    {"Name": str},
    total=False,
)

ClientUpdateWebAclRulesStatementRegexPatternSetReferenceStatementFieldToMatchTypeDef = TypedDict(
    "ClientUpdateWebAclRulesStatementRegexPatternSetReferenceStatementFieldToMatchTypeDef",
    {
        "SingleHeader": ClientUpdateWebAclRulesStatementRegexPatternSetReferenceStatementFieldToMatchSingleHeaderTypeDef,
        "SingleQueryArgument": ClientUpdateWebAclRulesStatementRegexPatternSetReferenceStatementFieldToMatchSingleQueryArgumentTypeDef,
        "AllQueryArguments": Dict[str, Any],
        "UriPath": Dict[str, Any],
        "QueryString": Dict[str, Any],
        "Body": Dict[str, Any],
        "Method": Dict[str, Any],
    },
    total=False,
)

ClientUpdateWebAclRulesStatementRegexPatternSetReferenceStatementTextTransformationsTypeDef = TypedDict(
    "ClientUpdateWebAclRulesStatementRegexPatternSetReferenceStatementTextTransformationsTypeDef",
    {
        "Priority": int,
        "Type": Literal[
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

ClientUpdateWebAclRulesStatementRegexPatternSetReferenceStatementTypeDef = TypedDict(
    "ClientUpdateWebAclRulesStatementRegexPatternSetReferenceStatementTypeDef",
    {
        "ARN": str,
        "FieldToMatch": ClientUpdateWebAclRulesStatementRegexPatternSetReferenceStatementFieldToMatchTypeDef,
        "TextTransformations": List[
            ClientUpdateWebAclRulesStatementRegexPatternSetReferenceStatementTextTransformationsTypeDef
        ],
    },
    total=False,
)

ClientUpdateWebAclRulesStatementRuleGroupReferenceStatementExcludedRulesTypeDef = TypedDict(
    "ClientUpdateWebAclRulesStatementRuleGroupReferenceStatementExcludedRulesTypeDef",
    {"Name": str},
    total=False,
)

ClientUpdateWebAclRulesStatementRuleGroupReferenceStatementTypeDef = TypedDict(
    "ClientUpdateWebAclRulesStatementRuleGroupReferenceStatementTypeDef",
    {
        "ARN": str,
        "ExcludedRules": List[
            ClientUpdateWebAclRulesStatementRuleGroupReferenceStatementExcludedRulesTypeDef
        ],
    },
    total=False,
)

ClientUpdateWebAclRulesStatementSizeConstraintStatementFieldToMatchSingleHeaderTypeDef = TypedDict(
    "ClientUpdateWebAclRulesStatementSizeConstraintStatementFieldToMatchSingleHeaderTypeDef",
    {"Name": str},
    total=False,
)

ClientUpdateWebAclRulesStatementSizeConstraintStatementFieldToMatchSingleQueryArgumentTypeDef = TypedDict(
    "ClientUpdateWebAclRulesStatementSizeConstraintStatementFieldToMatchSingleQueryArgumentTypeDef",
    {"Name": str},
    total=False,
)

ClientUpdateWebAclRulesStatementSizeConstraintStatementFieldToMatchTypeDef = TypedDict(
    "ClientUpdateWebAclRulesStatementSizeConstraintStatementFieldToMatchTypeDef",
    {
        "SingleHeader": ClientUpdateWebAclRulesStatementSizeConstraintStatementFieldToMatchSingleHeaderTypeDef,
        "SingleQueryArgument": ClientUpdateWebAclRulesStatementSizeConstraintStatementFieldToMatchSingleQueryArgumentTypeDef,
        "AllQueryArguments": Dict[str, Any],
        "UriPath": Dict[str, Any],
        "QueryString": Dict[str, Any],
        "Body": Dict[str, Any],
        "Method": Dict[str, Any],
    },
    total=False,
)

ClientUpdateWebAclRulesStatementSizeConstraintStatementTextTransformationsTypeDef = TypedDict(
    "ClientUpdateWebAclRulesStatementSizeConstraintStatementTextTransformationsTypeDef",
    {
        "Priority": int,
        "Type": Literal[
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

ClientUpdateWebAclRulesStatementSizeConstraintStatementTypeDef = TypedDict(
    "ClientUpdateWebAclRulesStatementSizeConstraintStatementTypeDef",
    {
        "FieldToMatch": ClientUpdateWebAclRulesStatementSizeConstraintStatementFieldToMatchTypeDef,
        "ComparisonOperator": Literal["EQ", "NE", "LE", "LT", "GE", "GT"],
        "Size": int,
        "TextTransformations": List[
            ClientUpdateWebAclRulesStatementSizeConstraintStatementTextTransformationsTypeDef
        ],
    },
    total=False,
)

ClientUpdateWebAclRulesStatementSqliMatchStatementFieldToMatchSingleHeaderTypeDef = TypedDict(
    "ClientUpdateWebAclRulesStatementSqliMatchStatementFieldToMatchSingleHeaderTypeDef",
    {"Name": str},
    total=False,
)

ClientUpdateWebAclRulesStatementSqliMatchStatementFieldToMatchSingleQueryArgumentTypeDef = TypedDict(
    "ClientUpdateWebAclRulesStatementSqliMatchStatementFieldToMatchSingleQueryArgumentTypeDef",
    {"Name": str},
    total=False,
)

ClientUpdateWebAclRulesStatementSqliMatchStatementFieldToMatchTypeDef = TypedDict(
    "ClientUpdateWebAclRulesStatementSqliMatchStatementFieldToMatchTypeDef",
    {
        "SingleHeader": ClientUpdateWebAclRulesStatementSqliMatchStatementFieldToMatchSingleHeaderTypeDef,
        "SingleQueryArgument": ClientUpdateWebAclRulesStatementSqliMatchStatementFieldToMatchSingleQueryArgumentTypeDef,
        "AllQueryArguments": Dict[str, Any],
        "UriPath": Dict[str, Any],
        "QueryString": Dict[str, Any],
        "Body": Dict[str, Any],
        "Method": Dict[str, Any],
    },
    total=False,
)

ClientUpdateWebAclRulesStatementSqliMatchStatementTextTransformationsTypeDef = TypedDict(
    "ClientUpdateWebAclRulesStatementSqliMatchStatementTextTransformationsTypeDef",
    {
        "Priority": int,
        "Type": Literal[
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

ClientUpdateWebAclRulesStatementSqliMatchStatementTypeDef = TypedDict(
    "ClientUpdateWebAclRulesStatementSqliMatchStatementTypeDef",
    {
        "FieldToMatch": ClientUpdateWebAclRulesStatementSqliMatchStatementFieldToMatchTypeDef,
        "TextTransformations": List[
            ClientUpdateWebAclRulesStatementSqliMatchStatementTextTransformationsTypeDef
        ],
    },
    total=False,
)

ClientUpdateWebAclRulesStatementXssMatchStatementFieldToMatchSingleHeaderTypeDef = TypedDict(
    "ClientUpdateWebAclRulesStatementXssMatchStatementFieldToMatchSingleHeaderTypeDef",
    {"Name": str},
    total=False,
)

ClientUpdateWebAclRulesStatementXssMatchStatementFieldToMatchSingleQueryArgumentTypeDef = TypedDict(
    "ClientUpdateWebAclRulesStatementXssMatchStatementFieldToMatchSingleQueryArgumentTypeDef",
    {"Name": str},
    total=False,
)

ClientUpdateWebAclRulesStatementXssMatchStatementFieldToMatchTypeDef = TypedDict(
    "ClientUpdateWebAclRulesStatementXssMatchStatementFieldToMatchTypeDef",
    {
        "SingleHeader": ClientUpdateWebAclRulesStatementXssMatchStatementFieldToMatchSingleHeaderTypeDef,
        "SingleQueryArgument": ClientUpdateWebAclRulesStatementXssMatchStatementFieldToMatchSingleQueryArgumentTypeDef,
        "AllQueryArguments": Dict[str, Any],
        "UriPath": Dict[str, Any],
        "QueryString": Dict[str, Any],
        "Body": Dict[str, Any],
        "Method": Dict[str, Any],
    },
    total=False,
)

ClientUpdateWebAclRulesStatementXssMatchStatementTextTransformationsTypeDef = TypedDict(
    "ClientUpdateWebAclRulesStatementXssMatchStatementTextTransformationsTypeDef",
    {
        "Priority": int,
        "Type": Literal[
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

ClientUpdateWebAclRulesStatementXssMatchStatementTypeDef = TypedDict(
    "ClientUpdateWebAclRulesStatementXssMatchStatementTypeDef",
    {
        "FieldToMatch": ClientUpdateWebAclRulesStatementXssMatchStatementFieldToMatchTypeDef,
        "TextTransformations": List[
            ClientUpdateWebAclRulesStatementXssMatchStatementTextTransformationsTypeDef
        ],
    },
    total=False,
)

ClientUpdateWebAclRulesStatementTypeDef = TypedDict(
    "ClientUpdateWebAclRulesStatementTypeDef",
    {
        "ByteMatchStatement": ClientUpdateWebAclRulesStatementByteMatchStatementTypeDef,
        "SqliMatchStatement": ClientUpdateWebAclRulesStatementSqliMatchStatementTypeDef,
        "XssMatchStatement": ClientUpdateWebAclRulesStatementXssMatchStatementTypeDef,
        "SizeConstraintStatement": ClientUpdateWebAclRulesStatementSizeConstraintStatementTypeDef,
        "GeoMatchStatement": ClientUpdateWebAclRulesStatementGeoMatchStatementTypeDef,
        "RuleGroupReferenceStatement": ClientUpdateWebAclRulesStatementRuleGroupReferenceStatementTypeDef,
        "IPSetReferenceStatement": ClientUpdateWebAclRulesStatementIPSetReferenceStatementTypeDef,
        "RegexPatternSetReferenceStatement": ClientUpdateWebAclRulesStatementRegexPatternSetReferenceStatementTypeDef,
        "RateBasedStatement": ClientUpdateWebAclRulesStatementRateBasedStatementTypeDef,
        "AndStatement": ClientUpdateWebAclRulesStatementAndStatementTypeDef,
        "OrStatement": ClientUpdateWebAclRulesStatementOrStatementTypeDef,
        "NotStatement": ClientUpdateWebAclRulesStatementNotStatementTypeDef,
        "ManagedRuleGroupStatement": ClientUpdateWebAclRulesStatementManagedRuleGroupStatementTypeDef,
    },
    total=False,
)

ClientUpdateWebAclRulesVisibilityConfigTypeDef = TypedDict(
    "ClientUpdateWebAclRulesVisibilityConfigTypeDef",
    {"SampledRequestsEnabled": bool, "CloudWatchMetricsEnabled": bool, "MetricName": str},
    total=False,
)

ClientUpdateWebAclRulesTypeDef = TypedDict(
    "ClientUpdateWebAclRulesTypeDef",
    {
        "Name": str,
        "Priority": int,
        "Statement": ClientUpdateWebAclRulesStatementTypeDef,
        "Action": ClientUpdateWebAclRulesActionTypeDef,
        "OverrideAction": ClientUpdateWebAclRulesOverrideActionTypeDef,
        "VisibilityConfig": ClientUpdateWebAclRulesVisibilityConfigTypeDef,
    },
    total=False,
)

_RequiredClientUpdateWebAclVisibilityConfigTypeDef = TypedDict(
    "_RequiredClientUpdateWebAclVisibilityConfigTypeDef", {"SampledRequestsEnabled": bool}
)
_OptionalClientUpdateWebAclVisibilityConfigTypeDef = TypedDict(
    "_OptionalClientUpdateWebAclVisibilityConfigTypeDef",
    {"CloudWatchMetricsEnabled": bool, "MetricName": str},
    total=False,
)


class ClientUpdateWebAclVisibilityConfigTypeDef(
    _RequiredClientUpdateWebAclVisibilityConfigTypeDef,
    _OptionalClientUpdateWebAclVisibilityConfigTypeDef,
):
    pass
