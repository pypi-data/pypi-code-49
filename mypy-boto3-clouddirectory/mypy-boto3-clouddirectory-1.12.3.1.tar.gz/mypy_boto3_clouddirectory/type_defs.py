"""
Main interface for clouddirectory service type definitions.

Usage::

    from mypy_boto3.clouddirectory.type_defs import ClientAddFacetToObjectObjectAttributeListKeyTypeDef

    data: ClientAddFacetToObjectObjectAttributeListKeyTypeDef = {...}
"""
from datetime import datetime
import sys
from typing import Any, Dict, IO, List, Union

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ClientAddFacetToObjectObjectAttributeListKeyTypeDef",
    "ClientAddFacetToObjectObjectAttributeListValueTypeDef",
    "ClientAddFacetToObjectObjectAttributeListTypeDef",
    "ClientAddFacetToObjectObjectReferenceTypeDef",
    "ClientAddFacetToObjectSchemaFacetTypeDef",
    "ClientApplySchemaResponseTypeDef",
    "ClientAttachObjectChildReferenceTypeDef",
    "ClientAttachObjectParentReferenceTypeDef",
    "ClientAttachObjectResponseTypeDef",
    "ClientAttachPolicyObjectReferenceTypeDef",
    "ClientAttachPolicyPolicyReferenceTypeDef",
    "ClientAttachToIndexIndexReferenceTypeDef",
    "ClientAttachToIndexResponseTypeDef",
    "ClientAttachToIndexTargetReferenceTypeDef",
    "ClientAttachTypedLinkAttributesValueTypeDef",
    "ClientAttachTypedLinkAttributesTypeDef",
    "ClientAttachTypedLinkResponseTypedLinkSpecifierIdentityAttributeValuesValueTypeDef",
    "ClientAttachTypedLinkResponseTypedLinkSpecifierIdentityAttributeValuesTypeDef",
    "ClientAttachTypedLinkResponseTypedLinkSpecifierSourceObjectReferenceTypeDef",
    "ClientAttachTypedLinkResponseTypedLinkSpecifierTargetObjectReferenceTypeDef",
    "ClientAttachTypedLinkResponseTypedLinkSpecifierTypedLinkFacetTypeDef",
    "ClientAttachTypedLinkResponseTypedLinkSpecifierTypeDef",
    "ClientAttachTypedLinkResponseTypeDef",
    "ClientAttachTypedLinkSourceObjectReferenceTypeDef",
    "ClientAttachTypedLinkTargetObjectReferenceTypeDef",
    "ClientAttachTypedLinkTypedLinkFacetTypeDef",
    "ClientBatchReadOperationsGetLinkAttributesTypedLinkSpecifierIdentityAttributeValuesValueTypeDef",
    "ClientBatchReadOperationsGetLinkAttributesTypedLinkSpecifierIdentityAttributeValuesTypeDef",
    "ClientBatchReadOperationsGetLinkAttributesTypedLinkSpecifierSourceObjectReferenceTypeDef",
    "ClientBatchReadOperationsGetLinkAttributesTypedLinkSpecifierTargetObjectReferenceTypeDef",
    "ClientBatchReadOperationsGetLinkAttributesTypedLinkSpecifierTypedLinkFacetTypeDef",
    "ClientBatchReadOperationsGetLinkAttributesTypedLinkSpecifierTypeDef",
    "ClientBatchReadOperationsGetLinkAttributesTypeDef",
    "ClientBatchReadOperationsGetObjectAttributesObjectReferenceTypeDef",
    "ClientBatchReadOperationsGetObjectAttributesSchemaFacetTypeDef",
    "ClientBatchReadOperationsGetObjectAttributesTypeDef",
    "ClientBatchReadOperationsGetObjectInformationObjectReferenceTypeDef",
    "ClientBatchReadOperationsGetObjectInformationTypeDef",
    "ClientBatchReadOperationsListAttachedIndicesTargetReferenceTypeDef",
    "ClientBatchReadOperationsListAttachedIndicesTypeDef",
    "ClientBatchReadOperationsListIncomingTypedLinksFilterAttributeRangesRangeEndValueTypeDef",
    "ClientBatchReadOperationsListIncomingTypedLinksFilterAttributeRangesRangeStartValueTypeDef",
    "ClientBatchReadOperationsListIncomingTypedLinksFilterAttributeRangesRangeTypeDef",
    "ClientBatchReadOperationsListIncomingTypedLinksFilterAttributeRangesTypeDef",
    "ClientBatchReadOperationsListIncomingTypedLinksFilterTypedLinkTypeDef",
    "ClientBatchReadOperationsListIncomingTypedLinksObjectReferenceTypeDef",
    "ClientBatchReadOperationsListIncomingTypedLinksTypeDef",
    "ClientBatchReadOperationsListIndexIndexReferenceTypeDef",
    "ClientBatchReadOperationsListIndexRangesOnIndexedValuesAttributeKeyTypeDef",
    "ClientBatchReadOperationsListIndexRangesOnIndexedValuesRangeEndValueTypeDef",
    "ClientBatchReadOperationsListIndexRangesOnIndexedValuesRangeStartValueTypeDef",
    "ClientBatchReadOperationsListIndexRangesOnIndexedValuesRangeTypeDef",
    "ClientBatchReadOperationsListIndexRangesOnIndexedValuesTypeDef",
    "ClientBatchReadOperationsListIndexTypeDef",
    "ClientBatchReadOperationsListObjectAttributesFacetFilterTypeDef",
    "ClientBatchReadOperationsListObjectAttributesObjectReferenceTypeDef",
    "ClientBatchReadOperationsListObjectAttributesTypeDef",
    "ClientBatchReadOperationsListObjectChildrenObjectReferenceTypeDef",
    "ClientBatchReadOperationsListObjectChildrenTypeDef",
    "ClientBatchReadOperationsListObjectParentPathsObjectReferenceTypeDef",
    "ClientBatchReadOperationsListObjectParentPathsTypeDef",
    "ClientBatchReadOperationsListObjectParentsObjectReferenceTypeDef",
    "ClientBatchReadOperationsListObjectParentsTypeDef",
    "ClientBatchReadOperationsListObjectPoliciesObjectReferenceTypeDef",
    "ClientBatchReadOperationsListObjectPoliciesTypeDef",
    "ClientBatchReadOperationsListOutgoingTypedLinksFilterAttributeRangesRangeEndValueTypeDef",
    "ClientBatchReadOperationsListOutgoingTypedLinksFilterAttributeRangesRangeStartValueTypeDef",
    "ClientBatchReadOperationsListOutgoingTypedLinksFilterAttributeRangesRangeTypeDef",
    "ClientBatchReadOperationsListOutgoingTypedLinksFilterAttributeRangesTypeDef",
    "ClientBatchReadOperationsListOutgoingTypedLinksFilterTypedLinkTypeDef",
    "ClientBatchReadOperationsListOutgoingTypedLinksObjectReferenceTypeDef",
    "ClientBatchReadOperationsListOutgoingTypedLinksTypeDef",
    "ClientBatchReadOperationsListPolicyAttachmentsPolicyReferenceTypeDef",
    "ClientBatchReadOperationsListPolicyAttachmentsTypeDef",
    "ClientBatchReadOperationsLookupPolicyObjectReferenceTypeDef",
    "ClientBatchReadOperationsLookupPolicyTypeDef",
    "ClientBatchReadOperationsTypeDef",
    "ClientBatchReadResponseResponsesExceptionResponseTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseGetLinkAttributesAttributesKeyTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseGetLinkAttributesAttributesValueTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseGetLinkAttributesAttributesTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseGetLinkAttributesTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseGetObjectAttributesAttributesKeyTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseGetObjectAttributesAttributesValueTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseGetObjectAttributesAttributesTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseGetObjectAttributesTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseGetObjectInformationSchemaFacetsTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseGetObjectInformationTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListAttachedIndicesIndexAttachmentsIndexedAttributesKeyTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListAttachedIndicesIndexAttachmentsIndexedAttributesValueTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListAttachedIndicesIndexAttachmentsIndexedAttributesTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListAttachedIndicesIndexAttachmentsTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListAttachedIndicesTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksLinkSpecifiersIdentityAttributeValuesValueTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksLinkSpecifiersIdentityAttributeValuesTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksLinkSpecifiersSourceObjectReferenceTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksLinkSpecifiersTargetObjectReferenceTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksLinkSpecifiersTypedLinkFacetTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksLinkSpecifiersTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListIndexIndexAttachmentsIndexedAttributesKeyTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListIndexIndexAttachmentsIndexedAttributesValueTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListIndexIndexAttachmentsIndexedAttributesTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListIndexIndexAttachmentsTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListIndexTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListObjectAttributesAttributesKeyTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListObjectAttributesAttributesValueTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListObjectAttributesAttributesTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListObjectAttributesTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListObjectChildrenTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListObjectParentPathsPathToObjectIdentifiersListTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListObjectParentPathsTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListObjectParentsParentLinksTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListObjectParentsTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListObjectPoliciesTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypedLinkSpecifiersIdentityAttributeValuesValueTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypedLinkSpecifiersIdentityAttributeValuesTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypedLinkSpecifiersSourceObjectReferenceTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypedLinkSpecifiersTargetObjectReferenceTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypedLinkSpecifiersTypedLinkFacetTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypedLinkSpecifiersTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListPolicyAttachmentsTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseLookupPolicyPolicyToPathListPoliciesTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseLookupPolicyPolicyToPathListTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseLookupPolicyTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseTypeDef",
    "ClientBatchReadResponseResponsesTypeDef",
    "ClientBatchReadResponseTypeDef",
    "ClientBatchWriteOperationsAddFacetToObjectObjectAttributeListKeyTypeDef",
    "ClientBatchWriteOperationsAddFacetToObjectObjectAttributeListValueTypeDef",
    "ClientBatchWriteOperationsAddFacetToObjectObjectAttributeListTypeDef",
    "ClientBatchWriteOperationsAddFacetToObjectObjectReferenceTypeDef",
    "ClientBatchWriteOperationsAddFacetToObjectSchemaFacetTypeDef",
    "ClientBatchWriteOperationsAddFacetToObjectTypeDef",
    "ClientBatchWriteOperationsAttachObjectChildReferenceTypeDef",
    "ClientBatchWriteOperationsAttachObjectParentReferenceTypeDef",
    "ClientBatchWriteOperationsAttachObjectTypeDef",
    "ClientBatchWriteOperationsAttachPolicyObjectReferenceTypeDef",
    "ClientBatchWriteOperationsAttachPolicyPolicyReferenceTypeDef",
    "ClientBatchWriteOperationsAttachPolicyTypeDef",
    "ClientBatchWriteOperationsAttachToIndexIndexReferenceTypeDef",
    "ClientBatchWriteOperationsAttachToIndexTargetReferenceTypeDef",
    "ClientBatchWriteOperationsAttachToIndexTypeDef",
    "ClientBatchWriteOperationsAttachTypedLinkAttributesValueTypeDef",
    "ClientBatchWriteOperationsAttachTypedLinkAttributesTypeDef",
    "ClientBatchWriteOperationsAttachTypedLinkSourceObjectReferenceTypeDef",
    "ClientBatchWriteOperationsAttachTypedLinkTargetObjectReferenceTypeDef",
    "ClientBatchWriteOperationsAttachTypedLinkTypedLinkFacetTypeDef",
    "ClientBatchWriteOperationsAttachTypedLinkTypeDef",
    "ClientBatchWriteOperationsCreateIndexOrderedIndexedAttributeListTypeDef",
    "ClientBatchWriteOperationsCreateIndexParentReferenceTypeDef",
    "ClientBatchWriteOperationsCreateIndexTypeDef",
    "ClientBatchWriteOperationsCreateObjectObjectAttributeListKeyTypeDef",
    "ClientBatchWriteOperationsCreateObjectObjectAttributeListValueTypeDef",
    "ClientBatchWriteOperationsCreateObjectObjectAttributeListTypeDef",
    "ClientBatchWriteOperationsCreateObjectParentReferenceTypeDef",
    "ClientBatchWriteOperationsCreateObjectSchemaFacetTypeDef",
    "ClientBatchWriteOperationsCreateObjectTypeDef",
    "ClientBatchWriteOperationsDeleteObjectObjectReferenceTypeDef",
    "ClientBatchWriteOperationsDeleteObjectTypeDef",
    "ClientBatchWriteOperationsDetachFromIndexIndexReferenceTypeDef",
    "ClientBatchWriteOperationsDetachFromIndexTargetReferenceTypeDef",
    "ClientBatchWriteOperationsDetachFromIndexTypeDef",
    "ClientBatchWriteOperationsDetachObjectParentReferenceTypeDef",
    "ClientBatchWriteOperationsDetachObjectTypeDef",
    "ClientBatchWriteOperationsDetachPolicyObjectReferenceTypeDef",
    "ClientBatchWriteOperationsDetachPolicyPolicyReferenceTypeDef",
    "ClientBatchWriteOperationsDetachPolicyTypeDef",
    "ClientBatchWriteOperationsDetachTypedLinkTypedLinkSpecifierIdentityAttributeValuesValueTypeDef",
    "ClientBatchWriteOperationsDetachTypedLinkTypedLinkSpecifierIdentityAttributeValuesTypeDef",
    "ClientBatchWriteOperationsDetachTypedLinkTypedLinkSpecifierSourceObjectReferenceTypeDef",
    "ClientBatchWriteOperationsDetachTypedLinkTypedLinkSpecifierTargetObjectReferenceTypeDef",
    "ClientBatchWriteOperationsDetachTypedLinkTypedLinkSpecifierTypedLinkFacetTypeDef",
    "ClientBatchWriteOperationsDetachTypedLinkTypedLinkSpecifierTypeDef",
    "ClientBatchWriteOperationsDetachTypedLinkTypeDef",
    "ClientBatchWriteOperationsRemoveFacetFromObjectObjectReferenceTypeDef",
    "ClientBatchWriteOperationsRemoveFacetFromObjectSchemaFacetTypeDef",
    "ClientBatchWriteOperationsRemoveFacetFromObjectTypeDef",
    "ClientBatchWriteOperationsUpdateLinkAttributesAttributeUpdatesAttributeActionAttributeUpdateValueTypeDef",
    "ClientBatchWriteOperationsUpdateLinkAttributesAttributeUpdatesAttributeActionTypeDef",
    "ClientBatchWriteOperationsUpdateLinkAttributesAttributeUpdatesAttributeKeyTypeDef",
    "ClientBatchWriteOperationsUpdateLinkAttributesAttributeUpdatesTypeDef",
    "ClientBatchWriteOperationsUpdateLinkAttributesTypedLinkSpecifierIdentityAttributeValuesValueTypeDef",
    "ClientBatchWriteOperationsUpdateLinkAttributesTypedLinkSpecifierIdentityAttributeValuesTypeDef",
    "ClientBatchWriteOperationsUpdateLinkAttributesTypedLinkSpecifierSourceObjectReferenceTypeDef",
    "ClientBatchWriteOperationsUpdateLinkAttributesTypedLinkSpecifierTargetObjectReferenceTypeDef",
    "ClientBatchWriteOperationsUpdateLinkAttributesTypedLinkSpecifierTypedLinkFacetTypeDef",
    "ClientBatchWriteOperationsUpdateLinkAttributesTypedLinkSpecifierTypeDef",
    "ClientBatchWriteOperationsUpdateLinkAttributesTypeDef",
    "ClientBatchWriteOperationsUpdateObjectAttributesAttributeUpdatesObjectAttributeActionObjectAttributeUpdateValueTypeDef",
    "ClientBatchWriteOperationsUpdateObjectAttributesAttributeUpdatesObjectAttributeActionTypeDef",
    "ClientBatchWriteOperationsUpdateObjectAttributesAttributeUpdatesObjectAttributeKeyTypeDef",
    "ClientBatchWriteOperationsUpdateObjectAttributesAttributeUpdatesTypeDef",
    "ClientBatchWriteOperationsUpdateObjectAttributesObjectReferenceTypeDef",
    "ClientBatchWriteOperationsUpdateObjectAttributesTypeDef",
    "ClientBatchWriteOperationsTypeDef",
    "ClientBatchWriteResponseResponsesAttachObjectTypeDef",
    "ClientBatchWriteResponseResponsesAttachToIndexTypeDef",
    "ClientBatchWriteResponseResponsesAttachTypedLinkTypedLinkSpecifierIdentityAttributeValuesValueTypeDef",
    "ClientBatchWriteResponseResponsesAttachTypedLinkTypedLinkSpecifierIdentityAttributeValuesTypeDef",
    "ClientBatchWriteResponseResponsesAttachTypedLinkTypedLinkSpecifierSourceObjectReferenceTypeDef",
    "ClientBatchWriteResponseResponsesAttachTypedLinkTypedLinkSpecifierTargetObjectReferenceTypeDef",
    "ClientBatchWriteResponseResponsesAttachTypedLinkTypedLinkSpecifierTypedLinkFacetTypeDef",
    "ClientBatchWriteResponseResponsesAttachTypedLinkTypedLinkSpecifierTypeDef",
    "ClientBatchWriteResponseResponsesAttachTypedLinkTypeDef",
    "ClientBatchWriteResponseResponsesCreateIndexTypeDef",
    "ClientBatchWriteResponseResponsesCreateObjectTypeDef",
    "ClientBatchWriteResponseResponsesDetachFromIndexTypeDef",
    "ClientBatchWriteResponseResponsesDetachObjectTypeDef",
    "ClientBatchWriteResponseResponsesUpdateObjectAttributesTypeDef",
    "ClientBatchWriteResponseResponsesTypeDef",
    "ClientBatchWriteResponseTypeDef",
    "ClientCreateDirectoryResponseTypeDef",
    "ClientCreateFacetAttributesAttributeDefinitionDefaultValueTypeDef",
    "ClientCreateFacetAttributesAttributeDefinitionRulesTypeDef",
    "ClientCreateFacetAttributesAttributeDefinitionTypeDef",
    "ClientCreateFacetAttributesAttributeReferenceTypeDef",
    "ClientCreateFacetAttributesTypeDef",
    "ClientCreateIndexOrderedIndexedAttributeListTypeDef",
    "ClientCreateIndexParentReferenceTypeDef",
    "ClientCreateIndexResponseTypeDef",
    "ClientCreateObjectObjectAttributeListKeyTypeDef",
    "ClientCreateObjectObjectAttributeListValueTypeDef",
    "ClientCreateObjectObjectAttributeListTypeDef",
    "ClientCreateObjectParentReferenceTypeDef",
    "ClientCreateObjectResponseTypeDef",
    "ClientCreateObjectSchemaFacetsTypeDef",
    "ClientCreateSchemaResponseTypeDef",
    "ClientCreateTypedLinkFacetFacetAttributesDefaultValueTypeDef",
    "ClientCreateTypedLinkFacetFacetAttributesRulesTypeDef",
    "ClientCreateTypedLinkFacetFacetAttributesTypeDef",
    "ClientCreateTypedLinkFacetFacetTypeDef",
    "ClientDeleteDirectoryResponseTypeDef",
    "ClientDeleteObjectObjectReferenceTypeDef",
    "ClientDeleteSchemaResponseTypeDef",
    "ClientDetachFromIndexIndexReferenceTypeDef",
    "ClientDetachFromIndexResponseTypeDef",
    "ClientDetachFromIndexTargetReferenceTypeDef",
    "ClientDetachObjectParentReferenceTypeDef",
    "ClientDetachObjectResponseTypeDef",
    "ClientDetachPolicyObjectReferenceTypeDef",
    "ClientDetachPolicyPolicyReferenceTypeDef",
    "ClientDetachTypedLinkTypedLinkSpecifierIdentityAttributeValuesValueTypeDef",
    "ClientDetachTypedLinkTypedLinkSpecifierIdentityAttributeValuesTypeDef",
    "ClientDetachTypedLinkTypedLinkSpecifierSourceObjectReferenceTypeDef",
    "ClientDetachTypedLinkTypedLinkSpecifierTargetObjectReferenceTypeDef",
    "ClientDetachTypedLinkTypedLinkSpecifierTypedLinkFacetTypeDef",
    "ClientDetachTypedLinkTypedLinkSpecifierTypeDef",
    "ClientDisableDirectoryResponseTypeDef",
    "ClientEnableDirectoryResponseTypeDef",
    "ClientGetAppliedSchemaVersionResponseTypeDef",
    "ClientGetDirectoryResponseDirectoryTypeDef",
    "ClientGetDirectoryResponseTypeDef",
    "ClientGetFacetResponseFacetTypeDef",
    "ClientGetFacetResponseTypeDef",
    "ClientGetLinkAttributesResponseAttributesKeyTypeDef",
    "ClientGetLinkAttributesResponseAttributesValueTypeDef",
    "ClientGetLinkAttributesResponseAttributesTypeDef",
    "ClientGetLinkAttributesResponseTypeDef",
    "ClientGetLinkAttributesTypedLinkSpecifierIdentityAttributeValuesValueTypeDef",
    "ClientGetLinkAttributesTypedLinkSpecifierIdentityAttributeValuesTypeDef",
    "ClientGetLinkAttributesTypedLinkSpecifierSourceObjectReferenceTypeDef",
    "ClientGetLinkAttributesTypedLinkSpecifierTargetObjectReferenceTypeDef",
    "ClientGetLinkAttributesTypedLinkSpecifierTypedLinkFacetTypeDef",
    "ClientGetLinkAttributesTypedLinkSpecifierTypeDef",
    "ClientGetObjectAttributesObjectReferenceTypeDef",
    "ClientGetObjectAttributesResponseAttributesKeyTypeDef",
    "ClientGetObjectAttributesResponseAttributesValueTypeDef",
    "ClientGetObjectAttributesResponseAttributesTypeDef",
    "ClientGetObjectAttributesResponseTypeDef",
    "ClientGetObjectAttributesSchemaFacetTypeDef",
    "ClientGetObjectInformationObjectReferenceTypeDef",
    "ClientGetObjectInformationResponseSchemaFacetsTypeDef",
    "ClientGetObjectInformationResponseTypeDef",
    "ClientGetSchemaAsJsonResponseTypeDef",
    "ClientGetTypedLinkFacetInformationResponseTypeDef",
    "ClientListAppliedSchemaArnsResponseTypeDef",
    "ClientListAttachedIndicesResponseIndexAttachmentsIndexedAttributesKeyTypeDef",
    "ClientListAttachedIndicesResponseIndexAttachmentsIndexedAttributesValueTypeDef",
    "ClientListAttachedIndicesResponseIndexAttachmentsIndexedAttributesTypeDef",
    "ClientListAttachedIndicesResponseIndexAttachmentsTypeDef",
    "ClientListAttachedIndicesResponseTypeDef",
    "ClientListAttachedIndicesTargetReferenceTypeDef",
    "ClientListDevelopmentSchemaArnsResponseTypeDef",
    "ClientListDirectoriesResponseDirectoriesTypeDef",
    "ClientListDirectoriesResponseTypeDef",
    "ClientListFacetAttributesResponseAttributesAttributeDefinitionDefaultValueTypeDef",
    "ClientListFacetAttributesResponseAttributesAttributeDefinitionRulesTypeDef",
    "ClientListFacetAttributesResponseAttributesAttributeDefinitionTypeDef",
    "ClientListFacetAttributesResponseAttributesAttributeReferenceTypeDef",
    "ClientListFacetAttributesResponseAttributesTypeDef",
    "ClientListFacetAttributesResponseTypeDef",
    "ClientListFacetNamesResponseTypeDef",
    "ClientListIncomingTypedLinksFilterAttributeRangesRangeEndValueTypeDef",
    "ClientListIncomingTypedLinksFilterAttributeRangesRangeStartValueTypeDef",
    "ClientListIncomingTypedLinksFilterAttributeRangesRangeTypeDef",
    "ClientListIncomingTypedLinksFilterAttributeRangesTypeDef",
    "ClientListIncomingTypedLinksFilterTypedLinkTypeDef",
    "ClientListIncomingTypedLinksObjectReferenceTypeDef",
    "ClientListIncomingTypedLinksResponseLinkSpecifiersIdentityAttributeValuesValueTypeDef",
    "ClientListIncomingTypedLinksResponseLinkSpecifiersIdentityAttributeValuesTypeDef",
    "ClientListIncomingTypedLinksResponseLinkSpecifiersSourceObjectReferenceTypeDef",
    "ClientListIncomingTypedLinksResponseLinkSpecifiersTargetObjectReferenceTypeDef",
    "ClientListIncomingTypedLinksResponseLinkSpecifiersTypedLinkFacetTypeDef",
    "ClientListIncomingTypedLinksResponseLinkSpecifiersTypeDef",
    "ClientListIncomingTypedLinksResponseTypeDef",
    "ClientListIndexIndexReferenceTypeDef",
    "ClientListIndexRangesOnIndexedValuesAttributeKeyTypeDef",
    "ClientListIndexRangesOnIndexedValuesRangeEndValueTypeDef",
    "ClientListIndexRangesOnIndexedValuesRangeStartValueTypeDef",
    "ClientListIndexRangesOnIndexedValuesRangeTypeDef",
    "ClientListIndexRangesOnIndexedValuesTypeDef",
    "ClientListIndexResponseIndexAttachmentsIndexedAttributesKeyTypeDef",
    "ClientListIndexResponseIndexAttachmentsIndexedAttributesValueTypeDef",
    "ClientListIndexResponseIndexAttachmentsIndexedAttributesTypeDef",
    "ClientListIndexResponseIndexAttachmentsTypeDef",
    "ClientListIndexResponseTypeDef",
    "ClientListManagedSchemaArnsResponseTypeDef",
    "ClientListObjectAttributesFacetFilterTypeDef",
    "ClientListObjectAttributesObjectReferenceTypeDef",
    "ClientListObjectAttributesResponseAttributesKeyTypeDef",
    "ClientListObjectAttributesResponseAttributesValueTypeDef",
    "ClientListObjectAttributesResponseAttributesTypeDef",
    "ClientListObjectAttributesResponseTypeDef",
    "ClientListObjectChildrenObjectReferenceTypeDef",
    "ClientListObjectChildrenResponseTypeDef",
    "ClientListObjectParentPathsObjectReferenceTypeDef",
    "ClientListObjectParentPathsResponsePathToObjectIdentifiersListTypeDef",
    "ClientListObjectParentPathsResponseTypeDef",
    "ClientListObjectParentsObjectReferenceTypeDef",
    "ClientListObjectParentsResponseParentLinksTypeDef",
    "ClientListObjectParentsResponseTypeDef",
    "ClientListObjectPoliciesObjectReferenceTypeDef",
    "ClientListObjectPoliciesResponseTypeDef",
    "ClientListOutgoingTypedLinksFilterAttributeRangesRangeEndValueTypeDef",
    "ClientListOutgoingTypedLinksFilterAttributeRangesRangeStartValueTypeDef",
    "ClientListOutgoingTypedLinksFilterAttributeRangesRangeTypeDef",
    "ClientListOutgoingTypedLinksFilterAttributeRangesTypeDef",
    "ClientListOutgoingTypedLinksFilterTypedLinkTypeDef",
    "ClientListOutgoingTypedLinksObjectReferenceTypeDef",
    "ClientListOutgoingTypedLinksResponseTypedLinkSpecifiersIdentityAttributeValuesValueTypeDef",
    "ClientListOutgoingTypedLinksResponseTypedLinkSpecifiersIdentityAttributeValuesTypeDef",
    "ClientListOutgoingTypedLinksResponseTypedLinkSpecifiersSourceObjectReferenceTypeDef",
    "ClientListOutgoingTypedLinksResponseTypedLinkSpecifiersTargetObjectReferenceTypeDef",
    "ClientListOutgoingTypedLinksResponseTypedLinkSpecifiersTypedLinkFacetTypeDef",
    "ClientListOutgoingTypedLinksResponseTypedLinkSpecifiersTypeDef",
    "ClientListOutgoingTypedLinksResponseTypeDef",
    "ClientListPolicyAttachmentsPolicyReferenceTypeDef",
    "ClientListPolicyAttachmentsResponseTypeDef",
    "ClientListPublishedSchemaArnsResponseTypeDef",
    "ClientListTagsForResourceResponseTagsTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientListTypedLinkFacetAttributesResponseAttributesDefaultValueTypeDef",
    "ClientListTypedLinkFacetAttributesResponseAttributesRulesTypeDef",
    "ClientListTypedLinkFacetAttributesResponseAttributesTypeDef",
    "ClientListTypedLinkFacetAttributesResponseTypeDef",
    "ClientListTypedLinkFacetNamesResponseTypeDef",
    "ClientLookupPolicyObjectReferenceTypeDef",
    "ClientLookupPolicyResponsePolicyToPathListPoliciesTypeDef",
    "ClientLookupPolicyResponsePolicyToPathListTypeDef",
    "ClientLookupPolicyResponseTypeDef",
    "ClientPublishSchemaResponseTypeDef",
    "ClientPutSchemaFromJsonResponseTypeDef",
    "ClientRemoveFacetFromObjectObjectReferenceTypeDef",
    "ClientRemoveFacetFromObjectSchemaFacetTypeDef",
    "ClientTagResourceTagsTypeDef",
    "ClientUpdateFacetAttributeUpdatesAttributeAttributeDefinitionDefaultValueTypeDef",
    "ClientUpdateFacetAttributeUpdatesAttributeAttributeDefinitionRulesTypeDef",
    "ClientUpdateFacetAttributeUpdatesAttributeAttributeDefinitionTypeDef",
    "ClientUpdateFacetAttributeUpdatesAttributeAttributeReferenceTypeDef",
    "ClientUpdateFacetAttributeUpdatesAttributeTypeDef",
    "ClientUpdateFacetAttributeUpdatesTypeDef",
    "ClientUpdateLinkAttributesAttributeUpdatesAttributeActionAttributeUpdateValueTypeDef",
    "ClientUpdateLinkAttributesAttributeUpdatesAttributeActionTypeDef",
    "ClientUpdateLinkAttributesAttributeUpdatesAttributeKeyTypeDef",
    "ClientUpdateLinkAttributesAttributeUpdatesTypeDef",
    "ClientUpdateLinkAttributesTypedLinkSpecifierIdentityAttributeValuesValueTypeDef",
    "ClientUpdateLinkAttributesTypedLinkSpecifierIdentityAttributeValuesTypeDef",
    "ClientUpdateLinkAttributesTypedLinkSpecifierSourceObjectReferenceTypeDef",
    "ClientUpdateLinkAttributesTypedLinkSpecifierTargetObjectReferenceTypeDef",
    "ClientUpdateLinkAttributesTypedLinkSpecifierTypedLinkFacetTypeDef",
    "ClientUpdateLinkAttributesTypedLinkSpecifierTypeDef",
    "ClientUpdateObjectAttributesAttributeUpdatesObjectAttributeActionObjectAttributeUpdateValueTypeDef",
    "ClientUpdateObjectAttributesAttributeUpdatesObjectAttributeActionTypeDef",
    "ClientUpdateObjectAttributesAttributeUpdatesObjectAttributeKeyTypeDef",
    "ClientUpdateObjectAttributesAttributeUpdatesTypeDef",
    "ClientUpdateObjectAttributesObjectReferenceTypeDef",
    "ClientUpdateObjectAttributesResponseTypeDef",
    "ClientUpdateSchemaResponseTypeDef",
    "ClientUpdateTypedLinkFacetAttributeUpdatesAttributeDefaultValueTypeDef",
    "ClientUpdateTypedLinkFacetAttributeUpdatesAttributeRulesTypeDef",
    "ClientUpdateTypedLinkFacetAttributeUpdatesAttributeTypeDef",
    "ClientUpdateTypedLinkFacetAttributeUpdatesTypeDef",
    "ClientUpgradeAppliedSchemaResponseTypeDef",
    "ClientUpgradePublishedSchemaResponseTypeDef",
    "ListAppliedSchemaArnsResponseTypeDef",
    "AttributeKeyTypeDef",
    "TypedAttributeValueTypeDef",
    "AttributeKeyAndValueTypeDef",
    "IndexAttachmentTypeDef",
    "ListAttachedIndicesResponseTypeDef",
    "ListDevelopmentSchemaArnsResponseTypeDef",
    "DirectoryTypeDef",
    "ListDirectoriesResponseTypeDef",
    "RuleTypeDef",
    "FacetAttributeDefinitionTypeDef",
    "FacetAttributeReferenceTypeDef",
    "FacetAttributeTypeDef",
    "ListFacetAttributesResponseTypeDef",
    "ListFacetNamesResponseTypeDef",
    "AttributeNameAndValueTypeDef",
    "ObjectReferenceTypeDef",
    "TypedLinkSchemaAndFacetNameTypeDef",
    "TypedLinkSpecifierTypeDef",
    "ListIncomingTypedLinksResponseTypeDef",
    "ListIndexResponseTypeDef",
    "ListManagedSchemaArnsResponseTypeDef",
    "ListObjectAttributesResponseTypeDef",
    "PathToObjectIdentifiersTypeDef",
    "ListObjectParentPathsResponseTypeDef",
    "ListObjectPoliciesResponseTypeDef",
    "ListOutgoingTypedLinksResponseTypeDef",
    "ListPolicyAttachmentsResponseTypeDef",
    "ListPublishedSchemaArnsResponseTypeDef",
    "TagTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "TypedLinkAttributeDefinitionTypeDef",
    "ListTypedLinkFacetAttributesResponseTypeDef",
    "ListTypedLinkFacetNamesResponseTypeDef",
    "PolicyAttachmentTypeDef",
    "PolicyToPathTypeDef",
    "LookupPolicyResponseTypeDef",
    "TypedAttributeValueRangeTypeDef",
    "ObjectAttributeRangeTypeDef",
    "PaginatorConfigTypeDef",
    "SchemaFacetTypeDef",
    "TypedLinkAttributeRangeTypeDef",
)

_RequiredClientAddFacetToObjectObjectAttributeListKeyTypeDef = TypedDict(
    "_RequiredClientAddFacetToObjectObjectAttributeListKeyTypeDef", {"SchemaArn": str}
)
_OptionalClientAddFacetToObjectObjectAttributeListKeyTypeDef = TypedDict(
    "_OptionalClientAddFacetToObjectObjectAttributeListKeyTypeDef",
    {"FacetName": str, "Name": str},
    total=False,
)


class ClientAddFacetToObjectObjectAttributeListKeyTypeDef(
    _RequiredClientAddFacetToObjectObjectAttributeListKeyTypeDef,
    _OptionalClientAddFacetToObjectObjectAttributeListKeyTypeDef,
):
    pass


ClientAddFacetToObjectObjectAttributeListValueTypeDef = TypedDict(
    "ClientAddFacetToObjectObjectAttributeListValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)

_RequiredClientAddFacetToObjectObjectAttributeListTypeDef = TypedDict(
    "_RequiredClientAddFacetToObjectObjectAttributeListTypeDef",
    {"Key": ClientAddFacetToObjectObjectAttributeListKeyTypeDef},
)
_OptionalClientAddFacetToObjectObjectAttributeListTypeDef = TypedDict(
    "_OptionalClientAddFacetToObjectObjectAttributeListTypeDef",
    {"Value": ClientAddFacetToObjectObjectAttributeListValueTypeDef},
    total=False,
)


class ClientAddFacetToObjectObjectAttributeListTypeDef(
    _RequiredClientAddFacetToObjectObjectAttributeListTypeDef,
    _OptionalClientAddFacetToObjectObjectAttributeListTypeDef,
):
    pass


ClientAddFacetToObjectObjectReferenceTypeDef = TypedDict(
    "ClientAddFacetToObjectObjectReferenceTypeDef", {"Selector": str}, total=False
)

ClientAddFacetToObjectSchemaFacetTypeDef = TypedDict(
    "ClientAddFacetToObjectSchemaFacetTypeDef", {"SchemaArn": str, "FacetName": str}, total=False
)

ClientApplySchemaResponseTypeDef = TypedDict(
    "ClientApplySchemaResponseTypeDef", {"AppliedSchemaArn": str, "DirectoryArn": str}, total=False
)

ClientAttachObjectChildReferenceTypeDef = TypedDict(
    "ClientAttachObjectChildReferenceTypeDef", {"Selector": str}, total=False
)

ClientAttachObjectParentReferenceTypeDef = TypedDict(
    "ClientAttachObjectParentReferenceTypeDef", {"Selector": str}, total=False
)

ClientAttachObjectResponseTypeDef = TypedDict(
    "ClientAttachObjectResponseTypeDef", {"AttachedObjectIdentifier": str}, total=False
)

ClientAttachPolicyObjectReferenceTypeDef = TypedDict(
    "ClientAttachPolicyObjectReferenceTypeDef", {"Selector": str}, total=False
)

ClientAttachPolicyPolicyReferenceTypeDef = TypedDict(
    "ClientAttachPolicyPolicyReferenceTypeDef", {"Selector": str}, total=False
)

ClientAttachToIndexIndexReferenceTypeDef = TypedDict(
    "ClientAttachToIndexIndexReferenceTypeDef", {"Selector": str}, total=False
)

ClientAttachToIndexResponseTypeDef = TypedDict(
    "ClientAttachToIndexResponseTypeDef", {"AttachedObjectIdentifier": str}, total=False
)

ClientAttachToIndexTargetReferenceTypeDef = TypedDict(
    "ClientAttachToIndexTargetReferenceTypeDef", {"Selector": str}, total=False
)

ClientAttachTypedLinkAttributesValueTypeDef = TypedDict(
    "ClientAttachTypedLinkAttributesValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)

_RequiredClientAttachTypedLinkAttributesTypeDef = TypedDict(
    "_RequiredClientAttachTypedLinkAttributesTypeDef", {"AttributeName": str}
)
_OptionalClientAttachTypedLinkAttributesTypeDef = TypedDict(
    "_OptionalClientAttachTypedLinkAttributesTypeDef",
    {"Value": ClientAttachTypedLinkAttributesValueTypeDef},
    total=False,
)


class ClientAttachTypedLinkAttributesTypeDef(
    _RequiredClientAttachTypedLinkAttributesTypeDef, _OptionalClientAttachTypedLinkAttributesTypeDef
):
    pass


ClientAttachTypedLinkResponseTypedLinkSpecifierIdentityAttributeValuesValueTypeDef = TypedDict(
    "ClientAttachTypedLinkResponseTypedLinkSpecifierIdentityAttributeValuesValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)

ClientAttachTypedLinkResponseTypedLinkSpecifierIdentityAttributeValuesTypeDef = TypedDict(
    "ClientAttachTypedLinkResponseTypedLinkSpecifierIdentityAttributeValuesTypeDef",
    {
        "AttributeName": str,
        "Value": ClientAttachTypedLinkResponseTypedLinkSpecifierIdentityAttributeValuesValueTypeDef,
    },
    total=False,
)

ClientAttachTypedLinkResponseTypedLinkSpecifierSourceObjectReferenceTypeDef = TypedDict(
    "ClientAttachTypedLinkResponseTypedLinkSpecifierSourceObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)

ClientAttachTypedLinkResponseTypedLinkSpecifierTargetObjectReferenceTypeDef = TypedDict(
    "ClientAttachTypedLinkResponseTypedLinkSpecifierTargetObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)

ClientAttachTypedLinkResponseTypedLinkSpecifierTypedLinkFacetTypeDef = TypedDict(
    "ClientAttachTypedLinkResponseTypedLinkSpecifierTypedLinkFacetTypeDef",
    {"SchemaArn": str, "TypedLinkName": str},
    total=False,
)

ClientAttachTypedLinkResponseTypedLinkSpecifierTypeDef = TypedDict(
    "ClientAttachTypedLinkResponseTypedLinkSpecifierTypeDef",
    {
        "TypedLinkFacet": ClientAttachTypedLinkResponseTypedLinkSpecifierTypedLinkFacetTypeDef,
        "SourceObjectReference": ClientAttachTypedLinkResponseTypedLinkSpecifierSourceObjectReferenceTypeDef,
        "TargetObjectReference": ClientAttachTypedLinkResponseTypedLinkSpecifierTargetObjectReferenceTypeDef,
        "IdentityAttributeValues": List[
            ClientAttachTypedLinkResponseTypedLinkSpecifierIdentityAttributeValuesTypeDef
        ],
    },
    total=False,
)

ClientAttachTypedLinkResponseTypeDef = TypedDict(
    "ClientAttachTypedLinkResponseTypeDef",
    {"TypedLinkSpecifier": ClientAttachTypedLinkResponseTypedLinkSpecifierTypeDef},
    total=False,
)

ClientAttachTypedLinkSourceObjectReferenceTypeDef = TypedDict(
    "ClientAttachTypedLinkSourceObjectReferenceTypeDef", {"Selector": str}, total=False
)

ClientAttachTypedLinkTargetObjectReferenceTypeDef = TypedDict(
    "ClientAttachTypedLinkTargetObjectReferenceTypeDef", {"Selector": str}, total=False
)

_RequiredClientAttachTypedLinkTypedLinkFacetTypeDef = TypedDict(
    "_RequiredClientAttachTypedLinkTypedLinkFacetTypeDef", {"SchemaArn": str}
)
_OptionalClientAttachTypedLinkTypedLinkFacetTypeDef = TypedDict(
    "_OptionalClientAttachTypedLinkTypedLinkFacetTypeDef", {"TypedLinkName": str}, total=False
)


class ClientAttachTypedLinkTypedLinkFacetTypeDef(
    _RequiredClientAttachTypedLinkTypedLinkFacetTypeDef,
    _OptionalClientAttachTypedLinkTypedLinkFacetTypeDef,
):
    pass


ClientBatchReadOperationsGetLinkAttributesTypedLinkSpecifierIdentityAttributeValuesValueTypeDef = TypedDict(
    "ClientBatchReadOperationsGetLinkAttributesTypedLinkSpecifierIdentityAttributeValuesValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)

ClientBatchReadOperationsGetLinkAttributesTypedLinkSpecifierIdentityAttributeValuesTypeDef = TypedDict(
    "ClientBatchReadOperationsGetLinkAttributesTypedLinkSpecifierIdentityAttributeValuesTypeDef",
    {
        "AttributeName": str,
        "Value": ClientBatchReadOperationsGetLinkAttributesTypedLinkSpecifierIdentityAttributeValuesValueTypeDef,
    },
    total=False,
)

ClientBatchReadOperationsGetLinkAttributesTypedLinkSpecifierSourceObjectReferenceTypeDef = TypedDict(
    "ClientBatchReadOperationsGetLinkAttributesTypedLinkSpecifierSourceObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)

ClientBatchReadOperationsGetLinkAttributesTypedLinkSpecifierTargetObjectReferenceTypeDef = TypedDict(
    "ClientBatchReadOperationsGetLinkAttributesTypedLinkSpecifierTargetObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)

ClientBatchReadOperationsGetLinkAttributesTypedLinkSpecifierTypedLinkFacetTypeDef = TypedDict(
    "ClientBatchReadOperationsGetLinkAttributesTypedLinkSpecifierTypedLinkFacetTypeDef",
    {"SchemaArn": str, "TypedLinkName": str},
    total=False,
)

ClientBatchReadOperationsGetLinkAttributesTypedLinkSpecifierTypeDef = TypedDict(
    "ClientBatchReadOperationsGetLinkAttributesTypedLinkSpecifierTypeDef",
    {
        "TypedLinkFacet": ClientBatchReadOperationsGetLinkAttributesTypedLinkSpecifierTypedLinkFacetTypeDef,
        "SourceObjectReference": ClientBatchReadOperationsGetLinkAttributesTypedLinkSpecifierSourceObjectReferenceTypeDef,
        "TargetObjectReference": ClientBatchReadOperationsGetLinkAttributesTypedLinkSpecifierTargetObjectReferenceTypeDef,
        "IdentityAttributeValues": List[
            ClientBatchReadOperationsGetLinkAttributesTypedLinkSpecifierIdentityAttributeValuesTypeDef
        ],
    },
    total=False,
)

ClientBatchReadOperationsGetLinkAttributesTypeDef = TypedDict(
    "ClientBatchReadOperationsGetLinkAttributesTypeDef",
    {
        "TypedLinkSpecifier": ClientBatchReadOperationsGetLinkAttributesTypedLinkSpecifierTypeDef,
        "AttributeNames": List[str],
    },
    total=False,
)

ClientBatchReadOperationsGetObjectAttributesObjectReferenceTypeDef = TypedDict(
    "ClientBatchReadOperationsGetObjectAttributesObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)

ClientBatchReadOperationsGetObjectAttributesSchemaFacetTypeDef = TypedDict(
    "ClientBatchReadOperationsGetObjectAttributesSchemaFacetTypeDef",
    {"SchemaArn": str, "FacetName": str},
    total=False,
)

ClientBatchReadOperationsGetObjectAttributesTypeDef = TypedDict(
    "ClientBatchReadOperationsGetObjectAttributesTypeDef",
    {
        "ObjectReference": ClientBatchReadOperationsGetObjectAttributesObjectReferenceTypeDef,
        "SchemaFacet": ClientBatchReadOperationsGetObjectAttributesSchemaFacetTypeDef,
        "AttributeNames": List[str],
    },
    total=False,
)

ClientBatchReadOperationsGetObjectInformationObjectReferenceTypeDef = TypedDict(
    "ClientBatchReadOperationsGetObjectInformationObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)

ClientBatchReadOperationsGetObjectInformationTypeDef = TypedDict(
    "ClientBatchReadOperationsGetObjectInformationTypeDef",
    {"ObjectReference": ClientBatchReadOperationsGetObjectInformationObjectReferenceTypeDef},
    total=False,
)

ClientBatchReadOperationsListAttachedIndicesTargetReferenceTypeDef = TypedDict(
    "ClientBatchReadOperationsListAttachedIndicesTargetReferenceTypeDef",
    {"Selector": str},
    total=False,
)

ClientBatchReadOperationsListAttachedIndicesTypeDef = TypedDict(
    "ClientBatchReadOperationsListAttachedIndicesTypeDef",
    {
        "TargetReference": ClientBatchReadOperationsListAttachedIndicesTargetReferenceTypeDef,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ClientBatchReadOperationsListIncomingTypedLinksFilterAttributeRangesRangeEndValueTypeDef = TypedDict(
    "ClientBatchReadOperationsListIncomingTypedLinksFilterAttributeRangesRangeEndValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)

ClientBatchReadOperationsListIncomingTypedLinksFilterAttributeRangesRangeStartValueTypeDef = TypedDict(
    "ClientBatchReadOperationsListIncomingTypedLinksFilterAttributeRangesRangeStartValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)

ClientBatchReadOperationsListIncomingTypedLinksFilterAttributeRangesRangeTypeDef = TypedDict(
    "ClientBatchReadOperationsListIncomingTypedLinksFilterAttributeRangesRangeTypeDef",
    {
        "StartMode": Literal[
            "FIRST", "LAST", "LAST_BEFORE_MISSING_VALUES", "INCLUSIVE", "EXCLUSIVE"
        ],
        "StartValue": ClientBatchReadOperationsListIncomingTypedLinksFilterAttributeRangesRangeStartValueTypeDef,
        "EndMode": Literal["FIRST", "LAST", "LAST_BEFORE_MISSING_VALUES", "INCLUSIVE", "EXCLUSIVE"],
        "EndValue": ClientBatchReadOperationsListIncomingTypedLinksFilterAttributeRangesRangeEndValueTypeDef,
    },
    total=False,
)

ClientBatchReadOperationsListIncomingTypedLinksFilterAttributeRangesTypeDef = TypedDict(
    "ClientBatchReadOperationsListIncomingTypedLinksFilterAttributeRangesTypeDef",
    {
        "AttributeName": str,
        "Range": ClientBatchReadOperationsListIncomingTypedLinksFilterAttributeRangesRangeTypeDef,
    },
    total=False,
)

ClientBatchReadOperationsListIncomingTypedLinksFilterTypedLinkTypeDef = TypedDict(
    "ClientBatchReadOperationsListIncomingTypedLinksFilterTypedLinkTypeDef",
    {"SchemaArn": str, "TypedLinkName": str},
    total=False,
)

ClientBatchReadOperationsListIncomingTypedLinksObjectReferenceTypeDef = TypedDict(
    "ClientBatchReadOperationsListIncomingTypedLinksObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)

ClientBatchReadOperationsListIncomingTypedLinksTypeDef = TypedDict(
    "ClientBatchReadOperationsListIncomingTypedLinksTypeDef",
    {
        "ObjectReference": ClientBatchReadOperationsListIncomingTypedLinksObjectReferenceTypeDef,
        "FilterAttributeRanges": List[
            ClientBatchReadOperationsListIncomingTypedLinksFilterAttributeRangesTypeDef
        ],
        "FilterTypedLink": ClientBatchReadOperationsListIncomingTypedLinksFilterTypedLinkTypeDef,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ClientBatchReadOperationsListIndexIndexReferenceTypeDef = TypedDict(
    "ClientBatchReadOperationsListIndexIndexReferenceTypeDef", {"Selector": str}, total=False
)

ClientBatchReadOperationsListIndexRangesOnIndexedValuesAttributeKeyTypeDef = TypedDict(
    "ClientBatchReadOperationsListIndexRangesOnIndexedValuesAttributeKeyTypeDef",
    {"SchemaArn": str, "FacetName": str, "Name": str},
    total=False,
)

ClientBatchReadOperationsListIndexRangesOnIndexedValuesRangeEndValueTypeDef = TypedDict(
    "ClientBatchReadOperationsListIndexRangesOnIndexedValuesRangeEndValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)

ClientBatchReadOperationsListIndexRangesOnIndexedValuesRangeStartValueTypeDef = TypedDict(
    "ClientBatchReadOperationsListIndexRangesOnIndexedValuesRangeStartValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)

ClientBatchReadOperationsListIndexRangesOnIndexedValuesRangeTypeDef = TypedDict(
    "ClientBatchReadOperationsListIndexRangesOnIndexedValuesRangeTypeDef",
    {
        "StartMode": Literal[
            "FIRST", "LAST", "LAST_BEFORE_MISSING_VALUES", "INCLUSIVE", "EXCLUSIVE"
        ],
        "StartValue": ClientBatchReadOperationsListIndexRangesOnIndexedValuesRangeStartValueTypeDef,
        "EndMode": Literal["FIRST", "LAST", "LAST_BEFORE_MISSING_VALUES", "INCLUSIVE", "EXCLUSIVE"],
        "EndValue": ClientBatchReadOperationsListIndexRangesOnIndexedValuesRangeEndValueTypeDef,
    },
    total=False,
)

ClientBatchReadOperationsListIndexRangesOnIndexedValuesTypeDef = TypedDict(
    "ClientBatchReadOperationsListIndexRangesOnIndexedValuesTypeDef",
    {
        "AttributeKey": ClientBatchReadOperationsListIndexRangesOnIndexedValuesAttributeKeyTypeDef,
        "Range": ClientBatchReadOperationsListIndexRangesOnIndexedValuesRangeTypeDef,
    },
    total=False,
)

ClientBatchReadOperationsListIndexTypeDef = TypedDict(
    "ClientBatchReadOperationsListIndexTypeDef",
    {
        "RangesOnIndexedValues": List[
            ClientBatchReadOperationsListIndexRangesOnIndexedValuesTypeDef
        ],
        "IndexReference": ClientBatchReadOperationsListIndexIndexReferenceTypeDef,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ClientBatchReadOperationsListObjectAttributesFacetFilterTypeDef = TypedDict(
    "ClientBatchReadOperationsListObjectAttributesFacetFilterTypeDef",
    {"SchemaArn": str, "FacetName": str},
    total=False,
)

ClientBatchReadOperationsListObjectAttributesObjectReferenceTypeDef = TypedDict(
    "ClientBatchReadOperationsListObjectAttributesObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)

_RequiredClientBatchReadOperationsListObjectAttributesTypeDef = TypedDict(
    "_RequiredClientBatchReadOperationsListObjectAttributesTypeDef",
    {"ObjectReference": ClientBatchReadOperationsListObjectAttributesObjectReferenceTypeDef},
)
_OptionalClientBatchReadOperationsListObjectAttributesTypeDef = TypedDict(
    "_OptionalClientBatchReadOperationsListObjectAttributesTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "FacetFilter": ClientBatchReadOperationsListObjectAttributesFacetFilterTypeDef,
    },
    total=False,
)


class ClientBatchReadOperationsListObjectAttributesTypeDef(
    _RequiredClientBatchReadOperationsListObjectAttributesTypeDef,
    _OptionalClientBatchReadOperationsListObjectAttributesTypeDef,
):
    pass


ClientBatchReadOperationsListObjectChildrenObjectReferenceTypeDef = TypedDict(
    "ClientBatchReadOperationsListObjectChildrenObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)

ClientBatchReadOperationsListObjectChildrenTypeDef = TypedDict(
    "ClientBatchReadOperationsListObjectChildrenTypeDef",
    {
        "ObjectReference": ClientBatchReadOperationsListObjectChildrenObjectReferenceTypeDef,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ClientBatchReadOperationsListObjectParentPathsObjectReferenceTypeDef = TypedDict(
    "ClientBatchReadOperationsListObjectParentPathsObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)

ClientBatchReadOperationsListObjectParentPathsTypeDef = TypedDict(
    "ClientBatchReadOperationsListObjectParentPathsTypeDef",
    {
        "ObjectReference": ClientBatchReadOperationsListObjectParentPathsObjectReferenceTypeDef,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ClientBatchReadOperationsListObjectParentsObjectReferenceTypeDef = TypedDict(
    "ClientBatchReadOperationsListObjectParentsObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)

ClientBatchReadOperationsListObjectParentsTypeDef = TypedDict(
    "ClientBatchReadOperationsListObjectParentsTypeDef",
    {
        "ObjectReference": ClientBatchReadOperationsListObjectParentsObjectReferenceTypeDef,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ClientBatchReadOperationsListObjectPoliciesObjectReferenceTypeDef = TypedDict(
    "ClientBatchReadOperationsListObjectPoliciesObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)

ClientBatchReadOperationsListObjectPoliciesTypeDef = TypedDict(
    "ClientBatchReadOperationsListObjectPoliciesTypeDef",
    {
        "ObjectReference": ClientBatchReadOperationsListObjectPoliciesObjectReferenceTypeDef,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ClientBatchReadOperationsListOutgoingTypedLinksFilterAttributeRangesRangeEndValueTypeDef = TypedDict(
    "ClientBatchReadOperationsListOutgoingTypedLinksFilterAttributeRangesRangeEndValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)

ClientBatchReadOperationsListOutgoingTypedLinksFilterAttributeRangesRangeStartValueTypeDef = TypedDict(
    "ClientBatchReadOperationsListOutgoingTypedLinksFilterAttributeRangesRangeStartValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)

ClientBatchReadOperationsListOutgoingTypedLinksFilterAttributeRangesRangeTypeDef = TypedDict(
    "ClientBatchReadOperationsListOutgoingTypedLinksFilterAttributeRangesRangeTypeDef",
    {
        "StartMode": Literal[
            "FIRST", "LAST", "LAST_BEFORE_MISSING_VALUES", "INCLUSIVE", "EXCLUSIVE"
        ],
        "StartValue": ClientBatchReadOperationsListOutgoingTypedLinksFilterAttributeRangesRangeStartValueTypeDef,
        "EndMode": Literal["FIRST", "LAST", "LAST_BEFORE_MISSING_VALUES", "INCLUSIVE", "EXCLUSIVE"],
        "EndValue": ClientBatchReadOperationsListOutgoingTypedLinksFilterAttributeRangesRangeEndValueTypeDef,
    },
    total=False,
)

ClientBatchReadOperationsListOutgoingTypedLinksFilterAttributeRangesTypeDef = TypedDict(
    "ClientBatchReadOperationsListOutgoingTypedLinksFilterAttributeRangesTypeDef",
    {
        "AttributeName": str,
        "Range": ClientBatchReadOperationsListOutgoingTypedLinksFilterAttributeRangesRangeTypeDef,
    },
    total=False,
)

ClientBatchReadOperationsListOutgoingTypedLinksFilterTypedLinkTypeDef = TypedDict(
    "ClientBatchReadOperationsListOutgoingTypedLinksFilterTypedLinkTypeDef",
    {"SchemaArn": str, "TypedLinkName": str},
    total=False,
)

ClientBatchReadOperationsListOutgoingTypedLinksObjectReferenceTypeDef = TypedDict(
    "ClientBatchReadOperationsListOutgoingTypedLinksObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)

ClientBatchReadOperationsListOutgoingTypedLinksTypeDef = TypedDict(
    "ClientBatchReadOperationsListOutgoingTypedLinksTypeDef",
    {
        "ObjectReference": ClientBatchReadOperationsListOutgoingTypedLinksObjectReferenceTypeDef,
        "FilterAttributeRanges": List[
            ClientBatchReadOperationsListOutgoingTypedLinksFilterAttributeRangesTypeDef
        ],
        "FilterTypedLink": ClientBatchReadOperationsListOutgoingTypedLinksFilterTypedLinkTypeDef,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ClientBatchReadOperationsListPolicyAttachmentsPolicyReferenceTypeDef = TypedDict(
    "ClientBatchReadOperationsListPolicyAttachmentsPolicyReferenceTypeDef",
    {"Selector": str},
    total=False,
)

ClientBatchReadOperationsListPolicyAttachmentsTypeDef = TypedDict(
    "ClientBatchReadOperationsListPolicyAttachmentsTypeDef",
    {
        "PolicyReference": ClientBatchReadOperationsListPolicyAttachmentsPolicyReferenceTypeDef,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ClientBatchReadOperationsLookupPolicyObjectReferenceTypeDef = TypedDict(
    "ClientBatchReadOperationsLookupPolicyObjectReferenceTypeDef", {"Selector": str}, total=False
)

ClientBatchReadOperationsLookupPolicyTypeDef = TypedDict(
    "ClientBatchReadOperationsLookupPolicyTypeDef",
    {
        "ObjectReference": ClientBatchReadOperationsLookupPolicyObjectReferenceTypeDef,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ClientBatchReadOperationsTypeDef = TypedDict(
    "ClientBatchReadOperationsTypeDef",
    {
        "ListObjectAttributes": ClientBatchReadOperationsListObjectAttributesTypeDef,
        "ListObjectChildren": ClientBatchReadOperationsListObjectChildrenTypeDef,
        "ListAttachedIndices": ClientBatchReadOperationsListAttachedIndicesTypeDef,
        "ListObjectParentPaths": ClientBatchReadOperationsListObjectParentPathsTypeDef,
        "GetObjectInformation": ClientBatchReadOperationsGetObjectInformationTypeDef,
        "GetObjectAttributes": ClientBatchReadOperationsGetObjectAttributesTypeDef,
        "ListObjectParents": ClientBatchReadOperationsListObjectParentsTypeDef,
        "ListObjectPolicies": ClientBatchReadOperationsListObjectPoliciesTypeDef,
        "ListPolicyAttachments": ClientBatchReadOperationsListPolicyAttachmentsTypeDef,
        "LookupPolicy": ClientBatchReadOperationsLookupPolicyTypeDef,
        "ListIndex": ClientBatchReadOperationsListIndexTypeDef,
        "ListOutgoingTypedLinks": ClientBatchReadOperationsListOutgoingTypedLinksTypeDef,
        "ListIncomingTypedLinks": ClientBatchReadOperationsListIncomingTypedLinksTypeDef,
        "GetLinkAttributes": ClientBatchReadOperationsGetLinkAttributesTypeDef,
    },
    total=False,
)

ClientBatchReadResponseResponsesExceptionResponseTypeDef = TypedDict(
    "ClientBatchReadResponseResponsesExceptionResponseTypeDef",
    {
        "Type": Literal[
            "ValidationException",
            "InvalidArnException",
            "ResourceNotFoundException",
            "InvalidNextTokenException",
            "AccessDeniedException",
            "NotNodeException",
            "FacetValidationException",
            "CannotListParentOfRootException",
            "NotIndexException",
            "NotPolicyException",
            "DirectoryNotEnabledException",
            "LimitExceededException",
            "InternalServiceException",
        ],
        "Message": str,
    },
    total=False,
)

ClientBatchReadResponseResponsesSuccessfulResponseGetLinkAttributesAttributesKeyTypeDef = TypedDict(
    "ClientBatchReadResponseResponsesSuccessfulResponseGetLinkAttributesAttributesKeyTypeDef",
    {"SchemaArn": str, "FacetName": str, "Name": str},
    total=False,
)

ClientBatchReadResponseResponsesSuccessfulResponseGetLinkAttributesAttributesValueTypeDef = TypedDict(
    "ClientBatchReadResponseResponsesSuccessfulResponseGetLinkAttributesAttributesValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)

ClientBatchReadResponseResponsesSuccessfulResponseGetLinkAttributesAttributesTypeDef = TypedDict(
    "ClientBatchReadResponseResponsesSuccessfulResponseGetLinkAttributesAttributesTypeDef",
    {
        "Key": ClientBatchReadResponseResponsesSuccessfulResponseGetLinkAttributesAttributesKeyTypeDef,
        "Value": ClientBatchReadResponseResponsesSuccessfulResponseGetLinkAttributesAttributesValueTypeDef,
    },
    total=False,
)

ClientBatchReadResponseResponsesSuccessfulResponseGetLinkAttributesTypeDef = TypedDict(
    "ClientBatchReadResponseResponsesSuccessfulResponseGetLinkAttributesTypeDef",
    {
        "Attributes": List[
            ClientBatchReadResponseResponsesSuccessfulResponseGetLinkAttributesAttributesTypeDef
        ]
    },
    total=False,
)

ClientBatchReadResponseResponsesSuccessfulResponseGetObjectAttributesAttributesKeyTypeDef = TypedDict(
    "ClientBatchReadResponseResponsesSuccessfulResponseGetObjectAttributesAttributesKeyTypeDef",
    {"SchemaArn": str, "FacetName": str, "Name": str},
    total=False,
)

ClientBatchReadResponseResponsesSuccessfulResponseGetObjectAttributesAttributesValueTypeDef = TypedDict(
    "ClientBatchReadResponseResponsesSuccessfulResponseGetObjectAttributesAttributesValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)

ClientBatchReadResponseResponsesSuccessfulResponseGetObjectAttributesAttributesTypeDef = TypedDict(
    "ClientBatchReadResponseResponsesSuccessfulResponseGetObjectAttributesAttributesTypeDef",
    {
        "Key": ClientBatchReadResponseResponsesSuccessfulResponseGetObjectAttributesAttributesKeyTypeDef,
        "Value": ClientBatchReadResponseResponsesSuccessfulResponseGetObjectAttributesAttributesValueTypeDef,
    },
    total=False,
)

ClientBatchReadResponseResponsesSuccessfulResponseGetObjectAttributesTypeDef = TypedDict(
    "ClientBatchReadResponseResponsesSuccessfulResponseGetObjectAttributesTypeDef",
    {
        "Attributes": List[
            ClientBatchReadResponseResponsesSuccessfulResponseGetObjectAttributesAttributesTypeDef
        ]
    },
    total=False,
)

ClientBatchReadResponseResponsesSuccessfulResponseGetObjectInformationSchemaFacetsTypeDef = TypedDict(
    "ClientBatchReadResponseResponsesSuccessfulResponseGetObjectInformationSchemaFacetsTypeDef",
    {"SchemaArn": str, "FacetName": str},
    total=False,
)

ClientBatchReadResponseResponsesSuccessfulResponseGetObjectInformationTypeDef = TypedDict(
    "ClientBatchReadResponseResponsesSuccessfulResponseGetObjectInformationTypeDef",
    {
        "SchemaFacets": List[
            ClientBatchReadResponseResponsesSuccessfulResponseGetObjectInformationSchemaFacetsTypeDef
        ],
        "ObjectIdentifier": str,
    },
    total=False,
)

ClientBatchReadResponseResponsesSuccessfulResponseListAttachedIndicesIndexAttachmentsIndexedAttributesKeyTypeDef = TypedDict(
    "ClientBatchReadResponseResponsesSuccessfulResponseListAttachedIndicesIndexAttachmentsIndexedAttributesKeyTypeDef",
    {"SchemaArn": str, "FacetName": str, "Name": str},
    total=False,
)

ClientBatchReadResponseResponsesSuccessfulResponseListAttachedIndicesIndexAttachmentsIndexedAttributesValueTypeDef = TypedDict(
    "ClientBatchReadResponseResponsesSuccessfulResponseListAttachedIndicesIndexAttachmentsIndexedAttributesValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)

ClientBatchReadResponseResponsesSuccessfulResponseListAttachedIndicesIndexAttachmentsIndexedAttributesTypeDef = TypedDict(
    "ClientBatchReadResponseResponsesSuccessfulResponseListAttachedIndicesIndexAttachmentsIndexedAttributesTypeDef",
    {
        "Key": ClientBatchReadResponseResponsesSuccessfulResponseListAttachedIndicesIndexAttachmentsIndexedAttributesKeyTypeDef,
        "Value": ClientBatchReadResponseResponsesSuccessfulResponseListAttachedIndicesIndexAttachmentsIndexedAttributesValueTypeDef,
    },
    total=False,
)

ClientBatchReadResponseResponsesSuccessfulResponseListAttachedIndicesIndexAttachmentsTypeDef = TypedDict(
    "ClientBatchReadResponseResponsesSuccessfulResponseListAttachedIndicesIndexAttachmentsTypeDef",
    {
        "IndexedAttributes": List[
            ClientBatchReadResponseResponsesSuccessfulResponseListAttachedIndicesIndexAttachmentsIndexedAttributesTypeDef
        ],
        "ObjectIdentifier": str,
    },
    total=False,
)

ClientBatchReadResponseResponsesSuccessfulResponseListAttachedIndicesTypeDef = TypedDict(
    "ClientBatchReadResponseResponsesSuccessfulResponseListAttachedIndicesTypeDef",
    {
        "IndexAttachments": List[
            ClientBatchReadResponseResponsesSuccessfulResponseListAttachedIndicesIndexAttachmentsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksLinkSpecifiersIdentityAttributeValuesValueTypeDef = TypedDict(
    "ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksLinkSpecifiersIdentityAttributeValuesValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)

ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksLinkSpecifiersIdentityAttributeValuesTypeDef = TypedDict(
    "ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksLinkSpecifiersIdentityAttributeValuesTypeDef",
    {
        "AttributeName": str,
        "Value": ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksLinkSpecifiersIdentityAttributeValuesValueTypeDef,
    },
    total=False,
)

ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksLinkSpecifiersSourceObjectReferenceTypeDef = TypedDict(
    "ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksLinkSpecifiersSourceObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)

ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksLinkSpecifiersTargetObjectReferenceTypeDef = TypedDict(
    "ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksLinkSpecifiersTargetObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)

ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksLinkSpecifiersTypedLinkFacetTypeDef = TypedDict(
    "ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksLinkSpecifiersTypedLinkFacetTypeDef",
    {"SchemaArn": str, "TypedLinkName": str},
    total=False,
)

ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksLinkSpecifiersTypeDef = TypedDict(
    "ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksLinkSpecifiersTypeDef",
    {
        "TypedLinkFacet": ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksLinkSpecifiersTypedLinkFacetTypeDef,
        "SourceObjectReference": ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksLinkSpecifiersSourceObjectReferenceTypeDef,
        "TargetObjectReference": ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksLinkSpecifiersTargetObjectReferenceTypeDef,
        "IdentityAttributeValues": List[
            ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksLinkSpecifiersIdentityAttributeValuesTypeDef
        ],
    },
    total=False,
)

ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksTypeDef = TypedDict(
    "ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksTypeDef",
    {
        "LinkSpecifiers": List[
            ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksLinkSpecifiersTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientBatchReadResponseResponsesSuccessfulResponseListIndexIndexAttachmentsIndexedAttributesKeyTypeDef = TypedDict(
    "ClientBatchReadResponseResponsesSuccessfulResponseListIndexIndexAttachmentsIndexedAttributesKeyTypeDef",
    {"SchemaArn": str, "FacetName": str, "Name": str},
    total=False,
)

ClientBatchReadResponseResponsesSuccessfulResponseListIndexIndexAttachmentsIndexedAttributesValueTypeDef = TypedDict(
    "ClientBatchReadResponseResponsesSuccessfulResponseListIndexIndexAttachmentsIndexedAttributesValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)

ClientBatchReadResponseResponsesSuccessfulResponseListIndexIndexAttachmentsIndexedAttributesTypeDef = TypedDict(
    "ClientBatchReadResponseResponsesSuccessfulResponseListIndexIndexAttachmentsIndexedAttributesTypeDef",
    {
        "Key": ClientBatchReadResponseResponsesSuccessfulResponseListIndexIndexAttachmentsIndexedAttributesKeyTypeDef,
        "Value": ClientBatchReadResponseResponsesSuccessfulResponseListIndexIndexAttachmentsIndexedAttributesValueTypeDef,
    },
    total=False,
)

ClientBatchReadResponseResponsesSuccessfulResponseListIndexIndexAttachmentsTypeDef = TypedDict(
    "ClientBatchReadResponseResponsesSuccessfulResponseListIndexIndexAttachmentsTypeDef",
    {
        "IndexedAttributes": List[
            ClientBatchReadResponseResponsesSuccessfulResponseListIndexIndexAttachmentsIndexedAttributesTypeDef
        ],
        "ObjectIdentifier": str,
    },
    total=False,
)

ClientBatchReadResponseResponsesSuccessfulResponseListIndexTypeDef = TypedDict(
    "ClientBatchReadResponseResponsesSuccessfulResponseListIndexTypeDef",
    {
        "IndexAttachments": List[
            ClientBatchReadResponseResponsesSuccessfulResponseListIndexIndexAttachmentsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientBatchReadResponseResponsesSuccessfulResponseListObjectAttributesAttributesKeyTypeDef = TypedDict(
    "ClientBatchReadResponseResponsesSuccessfulResponseListObjectAttributesAttributesKeyTypeDef",
    {"SchemaArn": str, "FacetName": str, "Name": str},
    total=False,
)

ClientBatchReadResponseResponsesSuccessfulResponseListObjectAttributesAttributesValueTypeDef = TypedDict(
    "ClientBatchReadResponseResponsesSuccessfulResponseListObjectAttributesAttributesValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)

ClientBatchReadResponseResponsesSuccessfulResponseListObjectAttributesAttributesTypeDef = TypedDict(
    "ClientBatchReadResponseResponsesSuccessfulResponseListObjectAttributesAttributesTypeDef",
    {
        "Key": ClientBatchReadResponseResponsesSuccessfulResponseListObjectAttributesAttributesKeyTypeDef,
        "Value": ClientBatchReadResponseResponsesSuccessfulResponseListObjectAttributesAttributesValueTypeDef,
    },
    total=False,
)

ClientBatchReadResponseResponsesSuccessfulResponseListObjectAttributesTypeDef = TypedDict(
    "ClientBatchReadResponseResponsesSuccessfulResponseListObjectAttributesTypeDef",
    {
        "Attributes": List[
            ClientBatchReadResponseResponsesSuccessfulResponseListObjectAttributesAttributesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientBatchReadResponseResponsesSuccessfulResponseListObjectChildrenTypeDef = TypedDict(
    "ClientBatchReadResponseResponsesSuccessfulResponseListObjectChildrenTypeDef",
    {"Children": Dict[str, str], "NextToken": str},
    total=False,
)

ClientBatchReadResponseResponsesSuccessfulResponseListObjectParentPathsPathToObjectIdentifiersListTypeDef = TypedDict(
    "ClientBatchReadResponseResponsesSuccessfulResponseListObjectParentPathsPathToObjectIdentifiersListTypeDef",
    {"Path": str, "ObjectIdentifiers": List[str]},
    total=False,
)

ClientBatchReadResponseResponsesSuccessfulResponseListObjectParentPathsTypeDef = TypedDict(
    "ClientBatchReadResponseResponsesSuccessfulResponseListObjectParentPathsTypeDef",
    {
        "PathToObjectIdentifiersList": List[
            ClientBatchReadResponseResponsesSuccessfulResponseListObjectParentPathsPathToObjectIdentifiersListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientBatchReadResponseResponsesSuccessfulResponseListObjectParentsParentLinksTypeDef = TypedDict(
    "ClientBatchReadResponseResponsesSuccessfulResponseListObjectParentsParentLinksTypeDef",
    {"ObjectIdentifier": str, "LinkName": str},
    total=False,
)

ClientBatchReadResponseResponsesSuccessfulResponseListObjectParentsTypeDef = TypedDict(
    "ClientBatchReadResponseResponsesSuccessfulResponseListObjectParentsTypeDef",
    {
        "ParentLinks": List[
            ClientBatchReadResponseResponsesSuccessfulResponseListObjectParentsParentLinksTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientBatchReadResponseResponsesSuccessfulResponseListObjectPoliciesTypeDef = TypedDict(
    "ClientBatchReadResponseResponsesSuccessfulResponseListObjectPoliciesTypeDef",
    {"AttachedPolicyIds": List[str], "NextToken": str},
    total=False,
)

ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypedLinkSpecifiersIdentityAttributeValuesValueTypeDef = TypedDict(
    "ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypedLinkSpecifiersIdentityAttributeValuesValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)

ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypedLinkSpecifiersIdentityAttributeValuesTypeDef = TypedDict(
    "ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypedLinkSpecifiersIdentityAttributeValuesTypeDef",
    {
        "AttributeName": str,
        "Value": ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypedLinkSpecifiersIdentityAttributeValuesValueTypeDef,
    },
    total=False,
)

ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypedLinkSpecifiersSourceObjectReferenceTypeDef = TypedDict(
    "ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypedLinkSpecifiersSourceObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)

ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypedLinkSpecifiersTargetObjectReferenceTypeDef = TypedDict(
    "ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypedLinkSpecifiersTargetObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)

ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypedLinkSpecifiersTypedLinkFacetTypeDef = TypedDict(
    "ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypedLinkSpecifiersTypedLinkFacetTypeDef",
    {"SchemaArn": str, "TypedLinkName": str},
    total=False,
)

ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypedLinkSpecifiersTypeDef = TypedDict(
    "ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypedLinkSpecifiersTypeDef",
    {
        "TypedLinkFacet": ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypedLinkSpecifiersTypedLinkFacetTypeDef,
        "SourceObjectReference": ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypedLinkSpecifiersSourceObjectReferenceTypeDef,
        "TargetObjectReference": ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypedLinkSpecifiersTargetObjectReferenceTypeDef,
        "IdentityAttributeValues": List[
            ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypedLinkSpecifiersIdentityAttributeValuesTypeDef
        ],
    },
    total=False,
)

ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypeDef = TypedDict(
    "ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypeDef",
    {
        "TypedLinkSpecifiers": List[
            ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypedLinkSpecifiersTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientBatchReadResponseResponsesSuccessfulResponseListPolicyAttachmentsTypeDef = TypedDict(
    "ClientBatchReadResponseResponsesSuccessfulResponseListPolicyAttachmentsTypeDef",
    {"ObjectIdentifiers": List[str], "NextToken": str},
    total=False,
)

ClientBatchReadResponseResponsesSuccessfulResponseLookupPolicyPolicyToPathListPoliciesTypeDef = TypedDict(
    "ClientBatchReadResponseResponsesSuccessfulResponseLookupPolicyPolicyToPathListPoliciesTypeDef",
    {"PolicyId": str, "ObjectIdentifier": str, "PolicyType": str},
    total=False,
)

ClientBatchReadResponseResponsesSuccessfulResponseLookupPolicyPolicyToPathListTypeDef = TypedDict(
    "ClientBatchReadResponseResponsesSuccessfulResponseLookupPolicyPolicyToPathListTypeDef",
    {
        "Path": str,
        "Policies": List[
            ClientBatchReadResponseResponsesSuccessfulResponseLookupPolicyPolicyToPathListPoliciesTypeDef
        ],
    },
    total=False,
)

ClientBatchReadResponseResponsesSuccessfulResponseLookupPolicyTypeDef = TypedDict(
    "ClientBatchReadResponseResponsesSuccessfulResponseLookupPolicyTypeDef",
    {
        "PolicyToPathList": List[
            ClientBatchReadResponseResponsesSuccessfulResponseLookupPolicyPolicyToPathListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientBatchReadResponseResponsesSuccessfulResponseTypeDef = TypedDict(
    "ClientBatchReadResponseResponsesSuccessfulResponseTypeDef",
    {
        "ListObjectAttributes": ClientBatchReadResponseResponsesSuccessfulResponseListObjectAttributesTypeDef,
        "ListObjectChildren": ClientBatchReadResponseResponsesSuccessfulResponseListObjectChildrenTypeDef,
        "GetObjectInformation": ClientBatchReadResponseResponsesSuccessfulResponseGetObjectInformationTypeDef,
        "GetObjectAttributes": ClientBatchReadResponseResponsesSuccessfulResponseGetObjectAttributesTypeDef,
        "ListAttachedIndices": ClientBatchReadResponseResponsesSuccessfulResponseListAttachedIndicesTypeDef,
        "ListObjectParentPaths": ClientBatchReadResponseResponsesSuccessfulResponseListObjectParentPathsTypeDef,
        "ListObjectPolicies": ClientBatchReadResponseResponsesSuccessfulResponseListObjectPoliciesTypeDef,
        "ListPolicyAttachments": ClientBatchReadResponseResponsesSuccessfulResponseListPolicyAttachmentsTypeDef,
        "LookupPolicy": ClientBatchReadResponseResponsesSuccessfulResponseLookupPolicyTypeDef,
        "ListIndex": ClientBatchReadResponseResponsesSuccessfulResponseListIndexTypeDef,
        "ListOutgoingTypedLinks": ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypeDef,
        "ListIncomingTypedLinks": ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksTypeDef,
        "GetLinkAttributes": ClientBatchReadResponseResponsesSuccessfulResponseGetLinkAttributesTypeDef,
        "ListObjectParents": ClientBatchReadResponseResponsesSuccessfulResponseListObjectParentsTypeDef,
    },
    total=False,
)

ClientBatchReadResponseResponsesTypeDef = TypedDict(
    "ClientBatchReadResponseResponsesTypeDef",
    {
        "SuccessfulResponse": ClientBatchReadResponseResponsesSuccessfulResponseTypeDef,
        "ExceptionResponse": ClientBatchReadResponseResponsesExceptionResponseTypeDef,
    },
    total=False,
)

ClientBatchReadResponseTypeDef = TypedDict(
    "ClientBatchReadResponseTypeDef",
    {"Responses": List[ClientBatchReadResponseResponsesTypeDef]},
    total=False,
)

ClientBatchWriteOperationsAddFacetToObjectObjectAttributeListKeyTypeDef = TypedDict(
    "ClientBatchWriteOperationsAddFacetToObjectObjectAttributeListKeyTypeDef",
    {"SchemaArn": str, "FacetName": str, "Name": str},
    total=False,
)

ClientBatchWriteOperationsAddFacetToObjectObjectAttributeListValueTypeDef = TypedDict(
    "ClientBatchWriteOperationsAddFacetToObjectObjectAttributeListValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)

ClientBatchWriteOperationsAddFacetToObjectObjectAttributeListTypeDef = TypedDict(
    "ClientBatchWriteOperationsAddFacetToObjectObjectAttributeListTypeDef",
    {
        "Key": ClientBatchWriteOperationsAddFacetToObjectObjectAttributeListKeyTypeDef,
        "Value": ClientBatchWriteOperationsAddFacetToObjectObjectAttributeListValueTypeDef,
    },
    total=False,
)

ClientBatchWriteOperationsAddFacetToObjectObjectReferenceTypeDef = TypedDict(
    "ClientBatchWriteOperationsAddFacetToObjectObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)

ClientBatchWriteOperationsAddFacetToObjectSchemaFacetTypeDef = TypedDict(
    "ClientBatchWriteOperationsAddFacetToObjectSchemaFacetTypeDef",
    {"SchemaArn": str, "FacetName": str},
    total=False,
)

ClientBatchWriteOperationsAddFacetToObjectTypeDef = TypedDict(
    "ClientBatchWriteOperationsAddFacetToObjectTypeDef",
    {
        "SchemaFacet": ClientBatchWriteOperationsAddFacetToObjectSchemaFacetTypeDef,
        "ObjectAttributeList": List[
            ClientBatchWriteOperationsAddFacetToObjectObjectAttributeListTypeDef
        ],
        "ObjectReference": ClientBatchWriteOperationsAddFacetToObjectObjectReferenceTypeDef,
    },
    total=False,
)

ClientBatchWriteOperationsAttachObjectChildReferenceTypeDef = TypedDict(
    "ClientBatchWriteOperationsAttachObjectChildReferenceTypeDef", {"Selector": str}, total=False
)

ClientBatchWriteOperationsAttachObjectParentReferenceTypeDef = TypedDict(
    "ClientBatchWriteOperationsAttachObjectParentReferenceTypeDef", {"Selector": str}, total=False
)

ClientBatchWriteOperationsAttachObjectTypeDef = TypedDict(
    "ClientBatchWriteOperationsAttachObjectTypeDef",
    {
        "ParentReference": ClientBatchWriteOperationsAttachObjectParentReferenceTypeDef,
        "ChildReference": ClientBatchWriteOperationsAttachObjectChildReferenceTypeDef,
        "LinkName": str,
    },
    total=False,
)

ClientBatchWriteOperationsAttachPolicyObjectReferenceTypeDef = TypedDict(
    "ClientBatchWriteOperationsAttachPolicyObjectReferenceTypeDef", {"Selector": str}, total=False
)

ClientBatchWriteOperationsAttachPolicyPolicyReferenceTypeDef = TypedDict(
    "ClientBatchWriteOperationsAttachPolicyPolicyReferenceTypeDef", {"Selector": str}, total=False
)

ClientBatchWriteOperationsAttachPolicyTypeDef = TypedDict(
    "ClientBatchWriteOperationsAttachPolicyTypeDef",
    {
        "PolicyReference": ClientBatchWriteOperationsAttachPolicyPolicyReferenceTypeDef,
        "ObjectReference": ClientBatchWriteOperationsAttachPolicyObjectReferenceTypeDef,
    },
    total=False,
)

ClientBatchWriteOperationsAttachToIndexIndexReferenceTypeDef = TypedDict(
    "ClientBatchWriteOperationsAttachToIndexIndexReferenceTypeDef", {"Selector": str}, total=False
)

ClientBatchWriteOperationsAttachToIndexTargetReferenceTypeDef = TypedDict(
    "ClientBatchWriteOperationsAttachToIndexTargetReferenceTypeDef", {"Selector": str}, total=False
)

ClientBatchWriteOperationsAttachToIndexTypeDef = TypedDict(
    "ClientBatchWriteOperationsAttachToIndexTypeDef",
    {
        "IndexReference": ClientBatchWriteOperationsAttachToIndexIndexReferenceTypeDef,
        "TargetReference": ClientBatchWriteOperationsAttachToIndexTargetReferenceTypeDef,
    },
    total=False,
)

ClientBatchWriteOperationsAttachTypedLinkAttributesValueTypeDef = TypedDict(
    "ClientBatchWriteOperationsAttachTypedLinkAttributesValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)

ClientBatchWriteOperationsAttachTypedLinkAttributesTypeDef = TypedDict(
    "ClientBatchWriteOperationsAttachTypedLinkAttributesTypeDef",
    {
        "AttributeName": str,
        "Value": ClientBatchWriteOperationsAttachTypedLinkAttributesValueTypeDef,
    },
    total=False,
)

ClientBatchWriteOperationsAttachTypedLinkSourceObjectReferenceTypeDef = TypedDict(
    "ClientBatchWriteOperationsAttachTypedLinkSourceObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)

ClientBatchWriteOperationsAttachTypedLinkTargetObjectReferenceTypeDef = TypedDict(
    "ClientBatchWriteOperationsAttachTypedLinkTargetObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)

ClientBatchWriteOperationsAttachTypedLinkTypedLinkFacetTypeDef = TypedDict(
    "ClientBatchWriteOperationsAttachTypedLinkTypedLinkFacetTypeDef",
    {"SchemaArn": str, "TypedLinkName": str},
    total=False,
)

ClientBatchWriteOperationsAttachTypedLinkTypeDef = TypedDict(
    "ClientBatchWriteOperationsAttachTypedLinkTypeDef",
    {
        "SourceObjectReference": ClientBatchWriteOperationsAttachTypedLinkSourceObjectReferenceTypeDef,
        "TargetObjectReference": ClientBatchWriteOperationsAttachTypedLinkTargetObjectReferenceTypeDef,
        "TypedLinkFacet": ClientBatchWriteOperationsAttachTypedLinkTypedLinkFacetTypeDef,
        "Attributes": List[ClientBatchWriteOperationsAttachTypedLinkAttributesTypeDef],
    },
    total=False,
)

ClientBatchWriteOperationsCreateIndexOrderedIndexedAttributeListTypeDef = TypedDict(
    "ClientBatchWriteOperationsCreateIndexOrderedIndexedAttributeListTypeDef",
    {"SchemaArn": str, "FacetName": str, "Name": str},
    total=False,
)

ClientBatchWriteOperationsCreateIndexParentReferenceTypeDef = TypedDict(
    "ClientBatchWriteOperationsCreateIndexParentReferenceTypeDef", {"Selector": str}, total=False
)

ClientBatchWriteOperationsCreateIndexTypeDef = TypedDict(
    "ClientBatchWriteOperationsCreateIndexTypeDef",
    {
        "OrderedIndexedAttributeList": List[
            ClientBatchWriteOperationsCreateIndexOrderedIndexedAttributeListTypeDef
        ],
        "IsUnique": bool,
        "ParentReference": ClientBatchWriteOperationsCreateIndexParentReferenceTypeDef,
        "LinkName": str,
        "BatchReferenceName": str,
    },
    total=False,
)

ClientBatchWriteOperationsCreateObjectObjectAttributeListKeyTypeDef = TypedDict(
    "ClientBatchWriteOperationsCreateObjectObjectAttributeListKeyTypeDef",
    {"SchemaArn": str, "FacetName": str, "Name": str},
    total=False,
)

ClientBatchWriteOperationsCreateObjectObjectAttributeListValueTypeDef = TypedDict(
    "ClientBatchWriteOperationsCreateObjectObjectAttributeListValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)

ClientBatchWriteOperationsCreateObjectObjectAttributeListTypeDef = TypedDict(
    "ClientBatchWriteOperationsCreateObjectObjectAttributeListTypeDef",
    {
        "Key": ClientBatchWriteOperationsCreateObjectObjectAttributeListKeyTypeDef,
        "Value": ClientBatchWriteOperationsCreateObjectObjectAttributeListValueTypeDef,
    },
    total=False,
)

ClientBatchWriteOperationsCreateObjectParentReferenceTypeDef = TypedDict(
    "ClientBatchWriteOperationsCreateObjectParentReferenceTypeDef", {"Selector": str}, total=False
)

ClientBatchWriteOperationsCreateObjectSchemaFacetTypeDef = TypedDict(
    "ClientBatchWriteOperationsCreateObjectSchemaFacetTypeDef",
    {"SchemaArn": str, "FacetName": str},
    total=False,
)

_RequiredClientBatchWriteOperationsCreateObjectTypeDef = TypedDict(
    "_RequiredClientBatchWriteOperationsCreateObjectTypeDef",
    {"SchemaFacet": List[ClientBatchWriteOperationsCreateObjectSchemaFacetTypeDef]},
)
_OptionalClientBatchWriteOperationsCreateObjectTypeDef = TypedDict(
    "_OptionalClientBatchWriteOperationsCreateObjectTypeDef",
    {
        "ObjectAttributeList": List[
            ClientBatchWriteOperationsCreateObjectObjectAttributeListTypeDef
        ],
        "ParentReference": ClientBatchWriteOperationsCreateObjectParentReferenceTypeDef,
        "LinkName": str,
        "BatchReferenceName": str,
    },
    total=False,
)


class ClientBatchWriteOperationsCreateObjectTypeDef(
    _RequiredClientBatchWriteOperationsCreateObjectTypeDef,
    _OptionalClientBatchWriteOperationsCreateObjectTypeDef,
):
    pass


ClientBatchWriteOperationsDeleteObjectObjectReferenceTypeDef = TypedDict(
    "ClientBatchWriteOperationsDeleteObjectObjectReferenceTypeDef", {"Selector": str}, total=False
)

ClientBatchWriteOperationsDeleteObjectTypeDef = TypedDict(
    "ClientBatchWriteOperationsDeleteObjectTypeDef",
    {"ObjectReference": ClientBatchWriteOperationsDeleteObjectObjectReferenceTypeDef},
    total=False,
)

ClientBatchWriteOperationsDetachFromIndexIndexReferenceTypeDef = TypedDict(
    "ClientBatchWriteOperationsDetachFromIndexIndexReferenceTypeDef", {"Selector": str}, total=False
)

ClientBatchWriteOperationsDetachFromIndexTargetReferenceTypeDef = TypedDict(
    "ClientBatchWriteOperationsDetachFromIndexTargetReferenceTypeDef",
    {"Selector": str},
    total=False,
)

ClientBatchWriteOperationsDetachFromIndexTypeDef = TypedDict(
    "ClientBatchWriteOperationsDetachFromIndexTypeDef",
    {
        "IndexReference": ClientBatchWriteOperationsDetachFromIndexIndexReferenceTypeDef,
        "TargetReference": ClientBatchWriteOperationsDetachFromIndexTargetReferenceTypeDef,
    },
    total=False,
)

ClientBatchWriteOperationsDetachObjectParentReferenceTypeDef = TypedDict(
    "ClientBatchWriteOperationsDetachObjectParentReferenceTypeDef", {"Selector": str}, total=False
)

ClientBatchWriteOperationsDetachObjectTypeDef = TypedDict(
    "ClientBatchWriteOperationsDetachObjectTypeDef",
    {
        "ParentReference": ClientBatchWriteOperationsDetachObjectParentReferenceTypeDef,
        "LinkName": str,
        "BatchReferenceName": str,
    },
    total=False,
)

ClientBatchWriteOperationsDetachPolicyObjectReferenceTypeDef = TypedDict(
    "ClientBatchWriteOperationsDetachPolicyObjectReferenceTypeDef", {"Selector": str}, total=False
)

ClientBatchWriteOperationsDetachPolicyPolicyReferenceTypeDef = TypedDict(
    "ClientBatchWriteOperationsDetachPolicyPolicyReferenceTypeDef", {"Selector": str}, total=False
)

ClientBatchWriteOperationsDetachPolicyTypeDef = TypedDict(
    "ClientBatchWriteOperationsDetachPolicyTypeDef",
    {
        "PolicyReference": ClientBatchWriteOperationsDetachPolicyPolicyReferenceTypeDef,
        "ObjectReference": ClientBatchWriteOperationsDetachPolicyObjectReferenceTypeDef,
    },
    total=False,
)

ClientBatchWriteOperationsDetachTypedLinkTypedLinkSpecifierIdentityAttributeValuesValueTypeDef = TypedDict(
    "ClientBatchWriteOperationsDetachTypedLinkTypedLinkSpecifierIdentityAttributeValuesValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)

ClientBatchWriteOperationsDetachTypedLinkTypedLinkSpecifierIdentityAttributeValuesTypeDef = TypedDict(
    "ClientBatchWriteOperationsDetachTypedLinkTypedLinkSpecifierIdentityAttributeValuesTypeDef",
    {
        "AttributeName": str,
        "Value": ClientBatchWriteOperationsDetachTypedLinkTypedLinkSpecifierIdentityAttributeValuesValueTypeDef,
    },
    total=False,
)

ClientBatchWriteOperationsDetachTypedLinkTypedLinkSpecifierSourceObjectReferenceTypeDef = TypedDict(
    "ClientBatchWriteOperationsDetachTypedLinkTypedLinkSpecifierSourceObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)

ClientBatchWriteOperationsDetachTypedLinkTypedLinkSpecifierTargetObjectReferenceTypeDef = TypedDict(
    "ClientBatchWriteOperationsDetachTypedLinkTypedLinkSpecifierTargetObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)

ClientBatchWriteOperationsDetachTypedLinkTypedLinkSpecifierTypedLinkFacetTypeDef = TypedDict(
    "ClientBatchWriteOperationsDetachTypedLinkTypedLinkSpecifierTypedLinkFacetTypeDef",
    {"SchemaArn": str, "TypedLinkName": str},
    total=False,
)

ClientBatchWriteOperationsDetachTypedLinkTypedLinkSpecifierTypeDef = TypedDict(
    "ClientBatchWriteOperationsDetachTypedLinkTypedLinkSpecifierTypeDef",
    {
        "TypedLinkFacet": ClientBatchWriteOperationsDetachTypedLinkTypedLinkSpecifierTypedLinkFacetTypeDef,
        "SourceObjectReference": ClientBatchWriteOperationsDetachTypedLinkTypedLinkSpecifierSourceObjectReferenceTypeDef,
        "TargetObjectReference": ClientBatchWriteOperationsDetachTypedLinkTypedLinkSpecifierTargetObjectReferenceTypeDef,
        "IdentityAttributeValues": List[
            ClientBatchWriteOperationsDetachTypedLinkTypedLinkSpecifierIdentityAttributeValuesTypeDef
        ],
    },
    total=False,
)

ClientBatchWriteOperationsDetachTypedLinkTypeDef = TypedDict(
    "ClientBatchWriteOperationsDetachTypedLinkTypeDef",
    {"TypedLinkSpecifier": ClientBatchWriteOperationsDetachTypedLinkTypedLinkSpecifierTypeDef},
    total=False,
)

ClientBatchWriteOperationsRemoveFacetFromObjectObjectReferenceTypeDef = TypedDict(
    "ClientBatchWriteOperationsRemoveFacetFromObjectObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)

ClientBatchWriteOperationsRemoveFacetFromObjectSchemaFacetTypeDef = TypedDict(
    "ClientBatchWriteOperationsRemoveFacetFromObjectSchemaFacetTypeDef",
    {"SchemaArn": str, "FacetName": str},
    total=False,
)

ClientBatchWriteOperationsRemoveFacetFromObjectTypeDef = TypedDict(
    "ClientBatchWriteOperationsRemoveFacetFromObjectTypeDef",
    {
        "SchemaFacet": ClientBatchWriteOperationsRemoveFacetFromObjectSchemaFacetTypeDef,
        "ObjectReference": ClientBatchWriteOperationsRemoveFacetFromObjectObjectReferenceTypeDef,
    },
    total=False,
)

ClientBatchWriteOperationsUpdateLinkAttributesAttributeUpdatesAttributeActionAttributeUpdateValueTypeDef = TypedDict(
    "ClientBatchWriteOperationsUpdateLinkAttributesAttributeUpdatesAttributeActionAttributeUpdateValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)

ClientBatchWriteOperationsUpdateLinkAttributesAttributeUpdatesAttributeActionTypeDef = TypedDict(
    "ClientBatchWriteOperationsUpdateLinkAttributesAttributeUpdatesAttributeActionTypeDef",
    {
        "AttributeActionType": Literal["CREATE_OR_UPDATE", "DELETE"],
        "AttributeUpdateValue": ClientBatchWriteOperationsUpdateLinkAttributesAttributeUpdatesAttributeActionAttributeUpdateValueTypeDef,
    },
    total=False,
)

ClientBatchWriteOperationsUpdateLinkAttributesAttributeUpdatesAttributeKeyTypeDef = TypedDict(
    "ClientBatchWriteOperationsUpdateLinkAttributesAttributeUpdatesAttributeKeyTypeDef",
    {"SchemaArn": str, "FacetName": str, "Name": str},
    total=False,
)

ClientBatchWriteOperationsUpdateLinkAttributesAttributeUpdatesTypeDef = TypedDict(
    "ClientBatchWriteOperationsUpdateLinkAttributesAttributeUpdatesTypeDef",
    {
        "AttributeKey": ClientBatchWriteOperationsUpdateLinkAttributesAttributeUpdatesAttributeKeyTypeDef,
        "AttributeAction": ClientBatchWriteOperationsUpdateLinkAttributesAttributeUpdatesAttributeActionTypeDef,
    },
    total=False,
)

ClientBatchWriteOperationsUpdateLinkAttributesTypedLinkSpecifierIdentityAttributeValuesValueTypeDef = TypedDict(
    "ClientBatchWriteOperationsUpdateLinkAttributesTypedLinkSpecifierIdentityAttributeValuesValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)

ClientBatchWriteOperationsUpdateLinkAttributesTypedLinkSpecifierIdentityAttributeValuesTypeDef = TypedDict(
    "ClientBatchWriteOperationsUpdateLinkAttributesTypedLinkSpecifierIdentityAttributeValuesTypeDef",
    {
        "AttributeName": str,
        "Value": ClientBatchWriteOperationsUpdateLinkAttributesTypedLinkSpecifierIdentityAttributeValuesValueTypeDef,
    },
    total=False,
)

ClientBatchWriteOperationsUpdateLinkAttributesTypedLinkSpecifierSourceObjectReferenceTypeDef = TypedDict(
    "ClientBatchWriteOperationsUpdateLinkAttributesTypedLinkSpecifierSourceObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)

ClientBatchWriteOperationsUpdateLinkAttributesTypedLinkSpecifierTargetObjectReferenceTypeDef = TypedDict(
    "ClientBatchWriteOperationsUpdateLinkAttributesTypedLinkSpecifierTargetObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)

ClientBatchWriteOperationsUpdateLinkAttributesTypedLinkSpecifierTypedLinkFacetTypeDef = TypedDict(
    "ClientBatchWriteOperationsUpdateLinkAttributesTypedLinkSpecifierTypedLinkFacetTypeDef",
    {"SchemaArn": str, "TypedLinkName": str},
    total=False,
)

ClientBatchWriteOperationsUpdateLinkAttributesTypedLinkSpecifierTypeDef = TypedDict(
    "ClientBatchWriteOperationsUpdateLinkAttributesTypedLinkSpecifierTypeDef",
    {
        "TypedLinkFacet": ClientBatchWriteOperationsUpdateLinkAttributesTypedLinkSpecifierTypedLinkFacetTypeDef,
        "SourceObjectReference": ClientBatchWriteOperationsUpdateLinkAttributesTypedLinkSpecifierSourceObjectReferenceTypeDef,
        "TargetObjectReference": ClientBatchWriteOperationsUpdateLinkAttributesTypedLinkSpecifierTargetObjectReferenceTypeDef,
        "IdentityAttributeValues": List[
            ClientBatchWriteOperationsUpdateLinkAttributesTypedLinkSpecifierIdentityAttributeValuesTypeDef
        ],
    },
    total=False,
)

ClientBatchWriteOperationsUpdateLinkAttributesTypeDef = TypedDict(
    "ClientBatchWriteOperationsUpdateLinkAttributesTypeDef",
    {
        "TypedLinkSpecifier": ClientBatchWriteOperationsUpdateLinkAttributesTypedLinkSpecifierTypeDef,
        "AttributeUpdates": List[
            ClientBatchWriteOperationsUpdateLinkAttributesAttributeUpdatesTypeDef
        ],
    },
    total=False,
)

ClientBatchWriteOperationsUpdateObjectAttributesAttributeUpdatesObjectAttributeActionObjectAttributeUpdateValueTypeDef = TypedDict(
    "ClientBatchWriteOperationsUpdateObjectAttributesAttributeUpdatesObjectAttributeActionObjectAttributeUpdateValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)

ClientBatchWriteOperationsUpdateObjectAttributesAttributeUpdatesObjectAttributeActionTypeDef = TypedDict(
    "ClientBatchWriteOperationsUpdateObjectAttributesAttributeUpdatesObjectAttributeActionTypeDef",
    {
        "ObjectAttributeActionType": Literal["CREATE_OR_UPDATE", "DELETE"],
        "ObjectAttributeUpdateValue": ClientBatchWriteOperationsUpdateObjectAttributesAttributeUpdatesObjectAttributeActionObjectAttributeUpdateValueTypeDef,
    },
    total=False,
)

ClientBatchWriteOperationsUpdateObjectAttributesAttributeUpdatesObjectAttributeKeyTypeDef = TypedDict(
    "ClientBatchWriteOperationsUpdateObjectAttributesAttributeUpdatesObjectAttributeKeyTypeDef",
    {"SchemaArn": str, "FacetName": str, "Name": str},
    total=False,
)

ClientBatchWriteOperationsUpdateObjectAttributesAttributeUpdatesTypeDef = TypedDict(
    "ClientBatchWriteOperationsUpdateObjectAttributesAttributeUpdatesTypeDef",
    {
        "ObjectAttributeKey": ClientBatchWriteOperationsUpdateObjectAttributesAttributeUpdatesObjectAttributeKeyTypeDef,
        "ObjectAttributeAction": ClientBatchWriteOperationsUpdateObjectAttributesAttributeUpdatesObjectAttributeActionTypeDef,
    },
    total=False,
)

ClientBatchWriteOperationsUpdateObjectAttributesObjectReferenceTypeDef = TypedDict(
    "ClientBatchWriteOperationsUpdateObjectAttributesObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)

ClientBatchWriteOperationsUpdateObjectAttributesTypeDef = TypedDict(
    "ClientBatchWriteOperationsUpdateObjectAttributesTypeDef",
    {
        "ObjectReference": ClientBatchWriteOperationsUpdateObjectAttributesObjectReferenceTypeDef,
        "AttributeUpdates": List[
            ClientBatchWriteOperationsUpdateObjectAttributesAttributeUpdatesTypeDef
        ],
    },
    total=False,
)

ClientBatchWriteOperationsTypeDef = TypedDict(
    "ClientBatchWriteOperationsTypeDef",
    {
        "CreateObject": ClientBatchWriteOperationsCreateObjectTypeDef,
        "AttachObject": ClientBatchWriteOperationsAttachObjectTypeDef,
        "DetachObject": ClientBatchWriteOperationsDetachObjectTypeDef,
        "UpdateObjectAttributes": ClientBatchWriteOperationsUpdateObjectAttributesTypeDef,
        "DeleteObject": ClientBatchWriteOperationsDeleteObjectTypeDef,
        "AddFacetToObject": ClientBatchWriteOperationsAddFacetToObjectTypeDef,
        "RemoveFacetFromObject": ClientBatchWriteOperationsRemoveFacetFromObjectTypeDef,
        "AttachPolicy": ClientBatchWriteOperationsAttachPolicyTypeDef,
        "DetachPolicy": ClientBatchWriteOperationsDetachPolicyTypeDef,
        "CreateIndex": ClientBatchWriteOperationsCreateIndexTypeDef,
        "AttachToIndex": ClientBatchWriteOperationsAttachToIndexTypeDef,
        "DetachFromIndex": ClientBatchWriteOperationsDetachFromIndexTypeDef,
        "AttachTypedLink": ClientBatchWriteOperationsAttachTypedLinkTypeDef,
        "DetachTypedLink": ClientBatchWriteOperationsDetachTypedLinkTypeDef,
        "UpdateLinkAttributes": ClientBatchWriteOperationsUpdateLinkAttributesTypeDef,
    },
    total=False,
)

ClientBatchWriteResponseResponsesAttachObjectTypeDef = TypedDict(
    "ClientBatchWriteResponseResponsesAttachObjectTypeDef",
    {"attachedObjectIdentifier": str},
    total=False,
)

ClientBatchWriteResponseResponsesAttachToIndexTypeDef = TypedDict(
    "ClientBatchWriteResponseResponsesAttachToIndexTypeDef",
    {"AttachedObjectIdentifier": str},
    total=False,
)

ClientBatchWriteResponseResponsesAttachTypedLinkTypedLinkSpecifierIdentityAttributeValuesValueTypeDef = TypedDict(
    "ClientBatchWriteResponseResponsesAttachTypedLinkTypedLinkSpecifierIdentityAttributeValuesValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)

ClientBatchWriteResponseResponsesAttachTypedLinkTypedLinkSpecifierIdentityAttributeValuesTypeDef = TypedDict(
    "ClientBatchWriteResponseResponsesAttachTypedLinkTypedLinkSpecifierIdentityAttributeValuesTypeDef",
    {
        "AttributeName": str,
        "Value": ClientBatchWriteResponseResponsesAttachTypedLinkTypedLinkSpecifierIdentityAttributeValuesValueTypeDef,
    },
    total=False,
)

ClientBatchWriteResponseResponsesAttachTypedLinkTypedLinkSpecifierSourceObjectReferenceTypeDef = TypedDict(
    "ClientBatchWriteResponseResponsesAttachTypedLinkTypedLinkSpecifierSourceObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)

ClientBatchWriteResponseResponsesAttachTypedLinkTypedLinkSpecifierTargetObjectReferenceTypeDef = TypedDict(
    "ClientBatchWriteResponseResponsesAttachTypedLinkTypedLinkSpecifierTargetObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)

ClientBatchWriteResponseResponsesAttachTypedLinkTypedLinkSpecifierTypedLinkFacetTypeDef = TypedDict(
    "ClientBatchWriteResponseResponsesAttachTypedLinkTypedLinkSpecifierTypedLinkFacetTypeDef",
    {"SchemaArn": str, "TypedLinkName": str},
    total=False,
)

ClientBatchWriteResponseResponsesAttachTypedLinkTypedLinkSpecifierTypeDef = TypedDict(
    "ClientBatchWriteResponseResponsesAttachTypedLinkTypedLinkSpecifierTypeDef",
    {
        "TypedLinkFacet": ClientBatchWriteResponseResponsesAttachTypedLinkTypedLinkSpecifierTypedLinkFacetTypeDef,
        "SourceObjectReference": ClientBatchWriteResponseResponsesAttachTypedLinkTypedLinkSpecifierSourceObjectReferenceTypeDef,
        "TargetObjectReference": ClientBatchWriteResponseResponsesAttachTypedLinkTypedLinkSpecifierTargetObjectReferenceTypeDef,
        "IdentityAttributeValues": List[
            ClientBatchWriteResponseResponsesAttachTypedLinkTypedLinkSpecifierIdentityAttributeValuesTypeDef
        ],
    },
    total=False,
)

ClientBatchWriteResponseResponsesAttachTypedLinkTypeDef = TypedDict(
    "ClientBatchWriteResponseResponsesAttachTypedLinkTypeDef",
    {
        "TypedLinkSpecifier": ClientBatchWriteResponseResponsesAttachTypedLinkTypedLinkSpecifierTypeDef
    },
    total=False,
)

ClientBatchWriteResponseResponsesCreateIndexTypeDef = TypedDict(
    "ClientBatchWriteResponseResponsesCreateIndexTypeDef", {"ObjectIdentifier": str}, total=False
)

ClientBatchWriteResponseResponsesCreateObjectTypeDef = TypedDict(
    "ClientBatchWriteResponseResponsesCreateObjectTypeDef", {"ObjectIdentifier": str}, total=False
)

ClientBatchWriteResponseResponsesDetachFromIndexTypeDef = TypedDict(
    "ClientBatchWriteResponseResponsesDetachFromIndexTypeDef",
    {"DetachedObjectIdentifier": str},
    total=False,
)

ClientBatchWriteResponseResponsesDetachObjectTypeDef = TypedDict(
    "ClientBatchWriteResponseResponsesDetachObjectTypeDef",
    {"detachedObjectIdentifier": str},
    total=False,
)

ClientBatchWriteResponseResponsesUpdateObjectAttributesTypeDef = TypedDict(
    "ClientBatchWriteResponseResponsesUpdateObjectAttributesTypeDef",
    {"ObjectIdentifier": str},
    total=False,
)

ClientBatchWriteResponseResponsesTypeDef = TypedDict(
    "ClientBatchWriteResponseResponsesTypeDef",
    {
        "CreateObject": ClientBatchWriteResponseResponsesCreateObjectTypeDef,
        "AttachObject": ClientBatchWriteResponseResponsesAttachObjectTypeDef,
        "DetachObject": ClientBatchWriteResponseResponsesDetachObjectTypeDef,
        "UpdateObjectAttributes": ClientBatchWriteResponseResponsesUpdateObjectAttributesTypeDef,
        "DeleteObject": Dict[str, Any],
        "AddFacetToObject": Dict[str, Any],
        "RemoveFacetFromObject": Dict[str, Any],
        "AttachPolicy": Dict[str, Any],
        "DetachPolicy": Dict[str, Any],
        "CreateIndex": ClientBatchWriteResponseResponsesCreateIndexTypeDef,
        "AttachToIndex": ClientBatchWriteResponseResponsesAttachToIndexTypeDef,
        "DetachFromIndex": ClientBatchWriteResponseResponsesDetachFromIndexTypeDef,
        "AttachTypedLink": ClientBatchWriteResponseResponsesAttachTypedLinkTypeDef,
        "DetachTypedLink": Dict[str, Any],
        "UpdateLinkAttributes": Dict[str, Any],
    },
    total=False,
)

ClientBatchWriteResponseTypeDef = TypedDict(
    "ClientBatchWriteResponseTypeDef",
    {"Responses": List[ClientBatchWriteResponseResponsesTypeDef]},
    total=False,
)

ClientCreateDirectoryResponseTypeDef = TypedDict(
    "ClientCreateDirectoryResponseTypeDef",
    {"DirectoryArn": str, "Name": str, "ObjectIdentifier": str, "AppliedSchemaArn": str},
    total=False,
)

ClientCreateFacetAttributesAttributeDefinitionDefaultValueTypeDef = TypedDict(
    "ClientCreateFacetAttributesAttributeDefinitionDefaultValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)

ClientCreateFacetAttributesAttributeDefinitionRulesTypeDef = TypedDict(
    "ClientCreateFacetAttributesAttributeDefinitionRulesTypeDef",
    {
        "Type": Literal["BINARY_LENGTH", "NUMBER_COMPARISON", "STRING_FROM_SET", "STRING_LENGTH"],
        "Parameters": Dict[str, str],
    },
    total=False,
)

ClientCreateFacetAttributesAttributeDefinitionTypeDef = TypedDict(
    "ClientCreateFacetAttributesAttributeDefinitionTypeDef",
    {
        "Type": Literal["STRING", "BINARY", "BOOLEAN", "NUMBER", "DATETIME", "VARIANT"],
        "DefaultValue": ClientCreateFacetAttributesAttributeDefinitionDefaultValueTypeDef,
        "IsImmutable": bool,
        "Rules": Dict[str, ClientCreateFacetAttributesAttributeDefinitionRulesTypeDef],
    },
    total=False,
)

ClientCreateFacetAttributesAttributeReferenceTypeDef = TypedDict(
    "ClientCreateFacetAttributesAttributeReferenceTypeDef",
    {"TargetFacetName": str, "TargetAttributeName": str},
    total=False,
)

_RequiredClientCreateFacetAttributesTypeDef = TypedDict(
    "_RequiredClientCreateFacetAttributesTypeDef", {"Name": str}
)
_OptionalClientCreateFacetAttributesTypeDef = TypedDict(
    "_OptionalClientCreateFacetAttributesTypeDef",
    {
        "AttributeDefinition": ClientCreateFacetAttributesAttributeDefinitionTypeDef,
        "AttributeReference": ClientCreateFacetAttributesAttributeReferenceTypeDef,
        "RequiredBehavior": Literal["REQUIRED_ALWAYS", "NOT_REQUIRED"],
    },
    total=False,
)


class ClientCreateFacetAttributesTypeDef(
    _RequiredClientCreateFacetAttributesTypeDef, _OptionalClientCreateFacetAttributesTypeDef
):
    pass


_RequiredClientCreateIndexOrderedIndexedAttributeListTypeDef = TypedDict(
    "_RequiredClientCreateIndexOrderedIndexedAttributeListTypeDef", {"SchemaArn": str}
)
_OptionalClientCreateIndexOrderedIndexedAttributeListTypeDef = TypedDict(
    "_OptionalClientCreateIndexOrderedIndexedAttributeListTypeDef",
    {"FacetName": str, "Name": str},
    total=False,
)


class ClientCreateIndexOrderedIndexedAttributeListTypeDef(
    _RequiredClientCreateIndexOrderedIndexedAttributeListTypeDef,
    _OptionalClientCreateIndexOrderedIndexedAttributeListTypeDef,
):
    pass


ClientCreateIndexParentReferenceTypeDef = TypedDict(
    "ClientCreateIndexParentReferenceTypeDef", {"Selector": str}, total=False
)

ClientCreateIndexResponseTypeDef = TypedDict(
    "ClientCreateIndexResponseTypeDef", {"ObjectIdentifier": str}, total=False
)

_RequiredClientCreateObjectObjectAttributeListKeyTypeDef = TypedDict(
    "_RequiredClientCreateObjectObjectAttributeListKeyTypeDef", {"SchemaArn": str}
)
_OptionalClientCreateObjectObjectAttributeListKeyTypeDef = TypedDict(
    "_OptionalClientCreateObjectObjectAttributeListKeyTypeDef",
    {"FacetName": str, "Name": str},
    total=False,
)


class ClientCreateObjectObjectAttributeListKeyTypeDef(
    _RequiredClientCreateObjectObjectAttributeListKeyTypeDef,
    _OptionalClientCreateObjectObjectAttributeListKeyTypeDef,
):
    pass


ClientCreateObjectObjectAttributeListValueTypeDef = TypedDict(
    "ClientCreateObjectObjectAttributeListValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)

_RequiredClientCreateObjectObjectAttributeListTypeDef = TypedDict(
    "_RequiredClientCreateObjectObjectAttributeListTypeDef",
    {"Key": ClientCreateObjectObjectAttributeListKeyTypeDef},
)
_OptionalClientCreateObjectObjectAttributeListTypeDef = TypedDict(
    "_OptionalClientCreateObjectObjectAttributeListTypeDef",
    {"Value": ClientCreateObjectObjectAttributeListValueTypeDef},
    total=False,
)


class ClientCreateObjectObjectAttributeListTypeDef(
    _RequiredClientCreateObjectObjectAttributeListTypeDef,
    _OptionalClientCreateObjectObjectAttributeListTypeDef,
):
    pass


ClientCreateObjectParentReferenceTypeDef = TypedDict(
    "ClientCreateObjectParentReferenceTypeDef", {"Selector": str}, total=False
)

ClientCreateObjectResponseTypeDef = TypedDict(
    "ClientCreateObjectResponseTypeDef", {"ObjectIdentifier": str}, total=False
)

ClientCreateObjectSchemaFacetsTypeDef = TypedDict(
    "ClientCreateObjectSchemaFacetsTypeDef", {"SchemaArn": str, "FacetName": str}, total=False
)

ClientCreateSchemaResponseTypeDef = TypedDict(
    "ClientCreateSchemaResponseTypeDef", {"SchemaArn": str}, total=False
)

ClientCreateTypedLinkFacetFacetAttributesDefaultValueTypeDef = TypedDict(
    "ClientCreateTypedLinkFacetFacetAttributesDefaultValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)

ClientCreateTypedLinkFacetFacetAttributesRulesTypeDef = TypedDict(
    "ClientCreateTypedLinkFacetFacetAttributesRulesTypeDef",
    {
        "Type": Literal["BINARY_LENGTH", "NUMBER_COMPARISON", "STRING_FROM_SET", "STRING_LENGTH"],
        "Parameters": Dict[str, str],
    },
    total=False,
)

ClientCreateTypedLinkFacetFacetAttributesTypeDef = TypedDict(
    "ClientCreateTypedLinkFacetFacetAttributesTypeDef",
    {
        "Name": str,
        "Type": Literal["STRING", "BINARY", "BOOLEAN", "NUMBER", "DATETIME", "VARIANT"],
        "DefaultValue": ClientCreateTypedLinkFacetFacetAttributesDefaultValueTypeDef,
        "IsImmutable": bool,
        "Rules": Dict[str, ClientCreateTypedLinkFacetFacetAttributesRulesTypeDef],
        "RequiredBehavior": Literal["REQUIRED_ALWAYS", "NOT_REQUIRED"],
    },
    total=False,
)

_RequiredClientCreateTypedLinkFacetFacetTypeDef = TypedDict(
    "_RequiredClientCreateTypedLinkFacetFacetTypeDef",
    {"Name": str, "Attributes": List[ClientCreateTypedLinkFacetFacetAttributesTypeDef]},
)
_OptionalClientCreateTypedLinkFacetFacetTypeDef = TypedDict(
    "_OptionalClientCreateTypedLinkFacetFacetTypeDef",
    {"IdentityAttributeOrder": List[str]},
    total=False,
)


class ClientCreateTypedLinkFacetFacetTypeDef(
    _RequiredClientCreateTypedLinkFacetFacetTypeDef, _OptionalClientCreateTypedLinkFacetFacetTypeDef
):
    pass


ClientDeleteDirectoryResponseTypeDef = TypedDict(
    "ClientDeleteDirectoryResponseTypeDef", {"DirectoryArn": str}, total=False
)

ClientDeleteObjectObjectReferenceTypeDef = TypedDict(
    "ClientDeleteObjectObjectReferenceTypeDef", {"Selector": str}, total=False
)

ClientDeleteSchemaResponseTypeDef = TypedDict(
    "ClientDeleteSchemaResponseTypeDef", {"SchemaArn": str}, total=False
)

ClientDetachFromIndexIndexReferenceTypeDef = TypedDict(
    "ClientDetachFromIndexIndexReferenceTypeDef", {"Selector": str}, total=False
)

ClientDetachFromIndexResponseTypeDef = TypedDict(
    "ClientDetachFromIndexResponseTypeDef", {"DetachedObjectIdentifier": str}, total=False
)

ClientDetachFromIndexTargetReferenceTypeDef = TypedDict(
    "ClientDetachFromIndexTargetReferenceTypeDef", {"Selector": str}, total=False
)

ClientDetachObjectParentReferenceTypeDef = TypedDict(
    "ClientDetachObjectParentReferenceTypeDef", {"Selector": str}, total=False
)

ClientDetachObjectResponseTypeDef = TypedDict(
    "ClientDetachObjectResponseTypeDef", {"DetachedObjectIdentifier": str}, total=False
)

ClientDetachPolicyObjectReferenceTypeDef = TypedDict(
    "ClientDetachPolicyObjectReferenceTypeDef", {"Selector": str}, total=False
)

ClientDetachPolicyPolicyReferenceTypeDef = TypedDict(
    "ClientDetachPolicyPolicyReferenceTypeDef", {"Selector": str}, total=False
)

ClientDetachTypedLinkTypedLinkSpecifierIdentityAttributeValuesValueTypeDef = TypedDict(
    "ClientDetachTypedLinkTypedLinkSpecifierIdentityAttributeValuesValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)

ClientDetachTypedLinkTypedLinkSpecifierIdentityAttributeValuesTypeDef = TypedDict(
    "ClientDetachTypedLinkTypedLinkSpecifierIdentityAttributeValuesTypeDef",
    {
        "AttributeName": str,
        "Value": ClientDetachTypedLinkTypedLinkSpecifierIdentityAttributeValuesValueTypeDef,
    },
    total=False,
)

ClientDetachTypedLinkTypedLinkSpecifierSourceObjectReferenceTypeDef = TypedDict(
    "ClientDetachTypedLinkTypedLinkSpecifierSourceObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)

ClientDetachTypedLinkTypedLinkSpecifierTargetObjectReferenceTypeDef = TypedDict(
    "ClientDetachTypedLinkTypedLinkSpecifierTargetObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)

_RequiredClientDetachTypedLinkTypedLinkSpecifierTypedLinkFacetTypeDef = TypedDict(
    "_RequiredClientDetachTypedLinkTypedLinkSpecifierTypedLinkFacetTypeDef", {"SchemaArn": str}
)
_OptionalClientDetachTypedLinkTypedLinkSpecifierTypedLinkFacetTypeDef = TypedDict(
    "_OptionalClientDetachTypedLinkTypedLinkSpecifierTypedLinkFacetTypeDef",
    {"TypedLinkName": str},
    total=False,
)


class ClientDetachTypedLinkTypedLinkSpecifierTypedLinkFacetTypeDef(
    _RequiredClientDetachTypedLinkTypedLinkSpecifierTypedLinkFacetTypeDef,
    _OptionalClientDetachTypedLinkTypedLinkSpecifierTypedLinkFacetTypeDef,
):
    pass


_RequiredClientDetachTypedLinkTypedLinkSpecifierTypeDef = TypedDict(
    "_RequiredClientDetachTypedLinkTypedLinkSpecifierTypeDef",
    {"TypedLinkFacet": ClientDetachTypedLinkTypedLinkSpecifierTypedLinkFacetTypeDef},
)
_OptionalClientDetachTypedLinkTypedLinkSpecifierTypeDef = TypedDict(
    "_OptionalClientDetachTypedLinkTypedLinkSpecifierTypeDef",
    {
        "SourceObjectReference": ClientDetachTypedLinkTypedLinkSpecifierSourceObjectReferenceTypeDef,
        "TargetObjectReference": ClientDetachTypedLinkTypedLinkSpecifierTargetObjectReferenceTypeDef,
        "IdentityAttributeValues": List[
            ClientDetachTypedLinkTypedLinkSpecifierIdentityAttributeValuesTypeDef
        ],
    },
    total=False,
)


class ClientDetachTypedLinkTypedLinkSpecifierTypeDef(
    _RequiredClientDetachTypedLinkTypedLinkSpecifierTypeDef,
    _OptionalClientDetachTypedLinkTypedLinkSpecifierTypeDef,
):
    pass


ClientDisableDirectoryResponseTypeDef = TypedDict(
    "ClientDisableDirectoryResponseTypeDef", {"DirectoryArn": str}, total=False
)

ClientEnableDirectoryResponseTypeDef = TypedDict(
    "ClientEnableDirectoryResponseTypeDef", {"DirectoryArn": str}, total=False
)

ClientGetAppliedSchemaVersionResponseTypeDef = TypedDict(
    "ClientGetAppliedSchemaVersionResponseTypeDef", {"AppliedSchemaArn": str}, total=False
)

ClientGetDirectoryResponseDirectoryTypeDef = TypedDict(
    "ClientGetDirectoryResponseDirectoryTypeDef",
    {
        "Name": str,
        "DirectoryArn": str,
        "State": Literal["ENABLED", "DISABLED", "DELETED"],
        "CreationDateTime": datetime,
    },
    total=False,
)

ClientGetDirectoryResponseTypeDef = TypedDict(
    "ClientGetDirectoryResponseTypeDef",
    {"Directory": ClientGetDirectoryResponseDirectoryTypeDef},
    total=False,
)

ClientGetFacetResponseFacetTypeDef = TypedDict(
    "ClientGetFacetResponseFacetTypeDef",
    {
        "Name": str,
        "ObjectType": Literal["NODE", "LEAF_NODE", "POLICY", "INDEX"],
        "FacetStyle": Literal["STATIC", "DYNAMIC"],
    },
    total=False,
)

ClientGetFacetResponseTypeDef = TypedDict(
    "ClientGetFacetResponseTypeDef", {"Facet": ClientGetFacetResponseFacetTypeDef}, total=False
)

ClientGetLinkAttributesResponseAttributesKeyTypeDef = TypedDict(
    "ClientGetLinkAttributesResponseAttributesKeyTypeDef",
    {"SchemaArn": str, "FacetName": str, "Name": str},
    total=False,
)

ClientGetLinkAttributesResponseAttributesValueTypeDef = TypedDict(
    "ClientGetLinkAttributesResponseAttributesValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)

ClientGetLinkAttributesResponseAttributesTypeDef = TypedDict(
    "ClientGetLinkAttributesResponseAttributesTypeDef",
    {
        "Key": ClientGetLinkAttributesResponseAttributesKeyTypeDef,
        "Value": ClientGetLinkAttributesResponseAttributesValueTypeDef,
    },
    total=False,
)

ClientGetLinkAttributesResponseTypeDef = TypedDict(
    "ClientGetLinkAttributesResponseTypeDef",
    {"Attributes": List[ClientGetLinkAttributesResponseAttributesTypeDef]},
    total=False,
)

ClientGetLinkAttributesTypedLinkSpecifierIdentityAttributeValuesValueTypeDef = TypedDict(
    "ClientGetLinkAttributesTypedLinkSpecifierIdentityAttributeValuesValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)

ClientGetLinkAttributesTypedLinkSpecifierIdentityAttributeValuesTypeDef = TypedDict(
    "ClientGetLinkAttributesTypedLinkSpecifierIdentityAttributeValuesTypeDef",
    {
        "AttributeName": str,
        "Value": ClientGetLinkAttributesTypedLinkSpecifierIdentityAttributeValuesValueTypeDef,
    },
    total=False,
)

ClientGetLinkAttributesTypedLinkSpecifierSourceObjectReferenceTypeDef = TypedDict(
    "ClientGetLinkAttributesTypedLinkSpecifierSourceObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)

ClientGetLinkAttributesTypedLinkSpecifierTargetObjectReferenceTypeDef = TypedDict(
    "ClientGetLinkAttributesTypedLinkSpecifierTargetObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)

_RequiredClientGetLinkAttributesTypedLinkSpecifierTypedLinkFacetTypeDef = TypedDict(
    "_RequiredClientGetLinkAttributesTypedLinkSpecifierTypedLinkFacetTypeDef", {"SchemaArn": str}
)
_OptionalClientGetLinkAttributesTypedLinkSpecifierTypedLinkFacetTypeDef = TypedDict(
    "_OptionalClientGetLinkAttributesTypedLinkSpecifierTypedLinkFacetTypeDef",
    {"TypedLinkName": str},
    total=False,
)


class ClientGetLinkAttributesTypedLinkSpecifierTypedLinkFacetTypeDef(
    _RequiredClientGetLinkAttributesTypedLinkSpecifierTypedLinkFacetTypeDef,
    _OptionalClientGetLinkAttributesTypedLinkSpecifierTypedLinkFacetTypeDef,
):
    pass


_RequiredClientGetLinkAttributesTypedLinkSpecifierTypeDef = TypedDict(
    "_RequiredClientGetLinkAttributesTypedLinkSpecifierTypeDef",
    {"TypedLinkFacet": ClientGetLinkAttributesTypedLinkSpecifierTypedLinkFacetTypeDef},
)
_OptionalClientGetLinkAttributesTypedLinkSpecifierTypeDef = TypedDict(
    "_OptionalClientGetLinkAttributesTypedLinkSpecifierTypeDef",
    {
        "SourceObjectReference": ClientGetLinkAttributesTypedLinkSpecifierSourceObjectReferenceTypeDef,
        "TargetObjectReference": ClientGetLinkAttributesTypedLinkSpecifierTargetObjectReferenceTypeDef,
        "IdentityAttributeValues": List[
            ClientGetLinkAttributesTypedLinkSpecifierIdentityAttributeValuesTypeDef
        ],
    },
    total=False,
)


class ClientGetLinkAttributesTypedLinkSpecifierTypeDef(
    _RequiredClientGetLinkAttributesTypedLinkSpecifierTypeDef,
    _OptionalClientGetLinkAttributesTypedLinkSpecifierTypeDef,
):
    pass


ClientGetObjectAttributesObjectReferenceTypeDef = TypedDict(
    "ClientGetObjectAttributesObjectReferenceTypeDef", {"Selector": str}, total=False
)

ClientGetObjectAttributesResponseAttributesKeyTypeDef = TypedDict(
    "ClientGetObjectAttributesResponseAttributesKeyTypeDef",
    {"SchemaArn": str, "FacetName": str, "Name": str},
    total=False,
)

ClientGetObjectAttributesResponseAttributesValueTypeDef = TypedDict(
    "ClientGetObjectAttributesResponseAttributesValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)

ClientGetObjectAttributesResponseAttributesTypeDef = TypedDict(
    "ClientGetObjectAttributesResponseAttributesTypeDef",
    {
        "Key": ClientGetObjectAttributesResponseAttributesKeyTypeDef,
        "Value": ClientGetObjectAttributesResponseAttributesValueTypeDef,
    },
    total=False,
)

ClientGetObjectAttributesResponseTypeDef = TypedDict(
    "ClientGetObjectAttributesResponseTypeDef",
    {"Attributes": List[ClientGetObjectAttributesResponseAttributesTypeDef]},
    total=False,
)

ClientGetObjectAttributesSchemaFacetTypeDef = TypedDict(
    "ClientGetObjectAttributesSchemaFacetTypeDef", {"SchemaArn": str, "FacetName": str}, total=False
)

ClientGetObjectInformationObjectReferenceTypeDef = TypedDict(
    "ClientGetObjectInformationObjectReferenceTypeDef", {"Selector": str}, total=False
)

ClientGetObjectInformationResponseSchemaFacetsTypeDef = TypedDict(
    "ClientGetObjectInformationResponseSchemaFacetsTypeDef",
    {"SchemaArn": str, "FacetName": str},
    total=False,
)

ClientGetObjectInformationResponseTypeDef = TypedDict(
    "ClientGetObjectInformationResponseTypeDef",
    {
        "SchemaFacets": List[ClientGetObjectInformationResponseSchemaFacetsTypeDef],
        "ObjectIdentifier": str,
    },
    total=False,
)

ClientGetSchemaAsJsonResponseTypeDef = TypedDict(
    "ClientGetSchemaAsJsonResponseTypeDef", {"Name": str, "Document": str}, total=False
)

ClientGetTypedLinkFacetInformationResponseTypeDef = TypedDict(
    "ClientGetTypedLinkFacetInformationResponseTypeDef",
    {"IdentityAttributeOrder": List[str]},
    total=False,
)

ClientListAppliedSchemaArnsResponseTypeDef = TypedDict(
    "ClientListAppliedSchemaArnsResponseTypeDef",
    {"SchemaArns": List[str], "NextToken": str},
    total=False,
)

ClientListAttachedIndicesResponseIndexAttachmentsIndexedAttributesKeyTypeDef = TypedDict(
    "ClientListAttachedIndicesResponseIndexAttachmentsIndexedAttributesKeyTypeDef",
    {"SchemaArn": str, "FacetName": str, "Name": str},
    total=False,
)

ClientListAttachedIndicesResponseIndexAttachmentsIndexedAttributesValueTypeDef = TypedDict(
    "ClientListAttachedIndicesResponseIndexAttachmentsIndexedAttributesValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)

ClientListAttachedIndicesResponseIndexAttachmentsIndexedAttributesTypeDef = TypedDict(
    "ClientListAttachedIndicesResponseIndexAttachmentsIndexedAttributesTypeDef",
    {
        "Key": ClientListAttachedIndicesResponseIndexAttachmentsIndexedAttributesKeyTypeDef,
        "Value": ClientListAttachedIndicesResponseIndexAttachmentsIndexedAttributesValueTypeDef,
    },
    total=False,
)

ClientListAttachedIndicesResponseIndexAttachmentsTypeDef = TypedDict(
    "ClientListAttachedIndicesResponseIndexAttachmentsTypeDef",
    {
        "IndexedAttributes": List[
            ClientListAttachedIndicesResponseIndexAttachmentsIndexedAttributesTypeDef
        ],
        "ObjectIdentifier": str,
    },
    total=False,
)

ClientListAttachedIndicesResponseTypeDef = TypedDict(
    "ClientListAttachedIndicesResponseTypeDef",
    {
        "IndexAttachments": List[ClientListAttachedIndicesResponseIndexAttachmentsTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientListAttachedIndicesTargetReferenceTypeDef = TypedDict(
    "ClientListAttachedIndicesTargetReferenceTypeDef", {"Selector": str}, total=False
)

ClientListDevelopmentSchemaArnsResponseTypeDef = TypedDict(
    "ClientListDevelopmentSchemaArnsResponseTypeDef",
    {"SchemaArns": List[str], "NextToken": str},
    total=False,
)

ClientListDirectoriesResponseDirectoriesTypeDef = TypedDict(
    "ClientListDirectoriesResponseDirectoriesTypeDef",
    {
        "Name": str,
        "DirectoryArn": str,
        "State": Literal["ENABLED", "DISABLED", "DELETED"],
        "CreationDateTime": datetime,
    },
    total=False,
)

ClientListDirectoriesResponseTypeDef = TypedDict(
    "ClientListDirectoriesResponseTypeDef",
    {"Directories": List[ClientListDirectoriesResponseDirectoriesTypeDef], "NextToken": str},
    total=False,
)

ClientListFacetAttributesResponseAttributesAttributeDefinitionDefaultValueTypeDef = TypedDict(
    "ClientListFacetAttributesResponseAttributesAttributeDefinitionDefaultValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)

ClientListFacetAttributesResponseAttributesAttributeDefinitionRulesTypeDef = TypedDict(
    "ClientListFacetAttributesResponseAttributesAttributeDefinitionRulesTypeDef",
    {
        "Type": Literal["BINARY_LENGTH", "NUMBER_COMPARISON", "STRING_FROM_SET", "STRING_LENGTH"],
        "Parameters": Dict[str, str],
    },
    total=False,
)

ClientListFacetAttributesResponseAttributesAttributeDefinitionTypeDef = TypedDict(
    "ClientListFacetAttributesResponseAttributesAttributeDefinitionTypeDef",
    {
        "Type": Literal["STRING", "BINARY", "BOOLEAN", "NUMBER", "DATETIME", "VARIANT"],
        "DefaultValue": ClientListFacetAttributesResponseAttributesAttributeDefinitionDefaultValueTypeDef,
        "IsImmutable": bool,
        "Rules": Dict[
            str, ClientListFacetAttributesResponseAttributesAttributeDefinitionRulesTypeDef
        ],
    },
    total=False,
)

ClientListFacetAttributesResponseAttributesAttributeReferenceTypeDef = TypedDict(
    "ClientListFacetAttributesResponseAttributesAttributeReferenceTypeDef",
    {"TargetFacetName": str, "TargetAttributeName": str},
    total=False,
)

ClientListFacetAttributesResponseAttributesTypeDef = TypedDict(
    "ClientListFacetAttributesResponseAttributesTypeDef",
    {
        "Name": str,
        "AttributeDefinition": ClientListFacetAttributesResponseAttributesAttributeDefinitionTypeDef,
        "AttributeReference": ClientListFacetAttributesResponseAttributesAttributeReferenceTypeDef,
        "RequiredBehavior": Literal["REQUIRED_ALWAYS", "NOT_REQUIRED"],
    },
    total=False,
)

ClientListFacetAttributesResponseTypeDef = TypedDict(
    "ClientListFacetAttributesResponseTypeDef",
    {"Attributes": List[ClientListFacetAttributesResponseAttributesTypeDef], "NextToken": str},
    total=False,
)

ClientListFacetNamesResponseTypeDef = TypedDict(
    "ClientListFacetNamesResponseTypeDef", {"FacetNames": List[str], "NextToken": str}, total=False
)

ClientListIncomingTypedLinksFilterAttributeRangesRangeEndValueTypeDef = TypedDict(
    "ClientListIncomingTypedLinksFilterAttributeRangesRangeEndValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)

ClientListIncomingTypedLinksFilterAttributeRangesRangeStartValueTypeDef = TypedDict(
    "ClientListIncomingTypedLinksFilterAttributeRangesRangeStartValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)

ClientListIncomingTypedLinksFilterAttributeRangesRangeTypeDef = TypedDict(
    "ClientListIncomingTypedLinksFilterAttributeRangesRangeTypeDef",
    {
        "StartMode": Literal[
            "FIRST", "LAST", "LAST_BEFORE_MISSING_VALUES", "INCLUSIVE", "EXCLUSIVE"
        ],
        "StartValue": ClientListIncomingTypedLinksFilterAttributeRangesRangeStartValueTypeDef,
        "EndMode": Literal["FIRST", "LAST", "LAST_BEFORE_MISSING_VALUES", "INCLUSIVE", "EXCLUSIVE"],
        "EndValue": ClientListIncomingTypedLinksFilterAttributeRangesRangeEndValueTypeDef,
    },
    total=False,
)

ClientListIncomingTypedLinksFilterAttributeRangesTypeDef = TypedDict(
    "ClientListIncomingTypedLinksFilterAttributeRangesTypeDef",
    {"AttributeName": str, "Range": ClientListIncomingTypedLinksFilterAttributeRangesRangeTypeDef},
    total=False,
)

_RequiredClientListIncomingTypedLinksFilterTypedLinkTypeDef = TypedDict(
    "_RequiredClientListIncomingTypedLinksFilterTypedLinkTypeDef", {"SchemaArn": str}
)
_OptionalClientListIncomingTypedLinksFilterTypedLinkTypeDef = TypedDict(
    "_OptionalClientListIncomingTypedLinksFilterTypedLinkTypeDef",
    {"TypedLinkName": str},
    total=False,
)


class ClientListIncomingTypedLinksFilterTypedLinkTypeDef(
    _RequiredClientListIncomingTypedLinksFilterTypedLinkTypeDef,
    _OptionalClientListIncomingTypedLinksFilterTypedLinkTypeDef,
):
    pass


ClientListIncomingTypedLinksObjectReferenceTypeDef = TypedDict(
    "ClientListIncomingTypedLinksObjectReferenceTypeDef", {"Selector": str}, total=False
)

ClientListIncomingTypedLinksResponseLinkSpecifiersIdentityAttributeValuesValueTypeDef = TypedDict(
    "ClientListIncomingTypedLinksResponseLinkSpecifiersIdentityAttributeValuesValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)

ClientListIncomingTypedLinksResponseLinkSpecifiersIdentityAttributeValuesTypeDef = TypedDict(
    "ClientListIncomingTypedLinksResponseLinkSpecifiersIdentityAttributeValuesTypeDef",
    {
        "AttributeName": str,
        "Value": ClientListIncomingTypedLinksResponseLinkSpecifiersIdentityAttributeValuesValueTypeDef,
    },
    total=False,
)

ClientListIncomingTypedLinksResponseLinkSpecifiersSourceObjectReferenceTypeDef = TypedDict(
    "ClientListIncomingTypedLinksResponseLinkSpecifiersSourceObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)

ClientListIncomingTypedLinksResponseLinkSpecifiersTargetObjectReferenceTypeDef = TypedDict(
    "ClientListIncomingTypedLinksResponseLinkSpecifiersTargetObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)

ClientListIncomingTypedLinksResponseLinkSpecifiersTypedLinkFacetTypeDef = TypedDict(
    "ClientListIncomingTypedLinksResponseLinkSpecifiersTypedLinkFacetTypeDef",
    {"SchemaArn": str, "TypedLinkName": str},
    total=False,
)

ClientListIncomingTypedLinksResponseLinkSpecifiersTypeDef = TypedDict(
    "ClientListIncomingTypedLinksResponseLinkSpecifiersTypeDef",
    {
        "TypedLinkFacet": ClientListIncomingTypedLinksResponseLinkSpecifiersTypedLinkFacetTypeDef,
        "SourceObjectReference": ClientListIncomingTypedLinksResponseLinkSpecifiersSourceObjectReferenceTypeDef,
        "TargetObjectReference": ClientListIncomingTypedLinksResponseLinkSpecifiersTargetObjectReferenceTypeDef,
        "IdentityAttributeValues": List[
            ClientListIncomingTypedLinksResponseLinkSpecifiersIdentityAttributeValuesTypeDef
        ],
    },
    total=False,
)

ClientListIncomingTypedLinksResponseTypeDef = TypedDict(
    "ClientListIncomingTypedLinksResponseTypeDef",
    {
        "LinkSpecifiers": List[ClientListIncomingTypedLinksResponseLinkSpecifiersTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientListIndexIndexReferenceTypeDef = TypedDict(
    "ClientListIndexIndexReferenceTypeDef", {"Selector": str}, total=False
)

_RequiredClientListIndexRangesOnIndexedValuesAttributeKeyTypeDef = TypedDict(
    "_RequiredClientListIndexRangesOnIndexedValuesAttributeKeyTypeDef", {"SchemaArn": str}
)
_OptionalClientListIndexRangesOnIndexedValuesAttributeKeyTypeDef = TypedDict(
    "_OptionalClientListIndexRangesOnIndexedValuesAttributeKeyTypeDef",
    {"FacetName": str, "Name": str},
    total=False,
)


class ClientListIndexRangesOnIndexedValuesAttributeKeyTypeDef(
    _RequiredClientListIndexRangesOnIndexedValuesAttributeKeyTypeDef,
    _OptionalClientListIndexRangesOnIndexedValuesAttributeKeyTypeDef,
):
    pass


ClientListIndexRangesOnIndexedValuesRangeEndValueTypeDef = TypedDict(
    "ClientListIndexRangesOnIndexedValuesRangeEndValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)

ClientListIndexRangesOnIndexedValuesRangeStartValueTypeDef = TypedDict(
    "ClientListIndexRangesOnIndexedValuesRangeStartValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)

ClientListIndexRangesOnIndexedValuesRangeTypeDef = TypedDict(
    "ClientListIndexRangesOnIndexedValuesRangeTypeDef",
    {
        "StartMode": Literal[
            "FIRST", "LAST", "LAST_BEFORE_MISSING_VALUES", "INCLUSIVE", "EXCLUSIVE"
        ],
        "StartValue": ClientListIndexRangesOnIndexedValuesRangeStartValueTypeDef,
        "EndMode": Literal["FIRST", "LAST", "LAST_BEFORE_MISSING_VALUES", "INCLUSIVE", "EXCLUSIVE"],
        "EndValue": ClientListIndexRangesOnIndexedValuesRangeEndValueTypeDef,
    },
    total=False,
)

ClientListIndexRangesOnIndexedValuesTypeDef = TypedDict(
    "ClientListIndexRangesOnIndexedValuesTypeDef",
    {
        "AttributeKey": ClientListIndexRangesOnIndexedValuesAttributeKeyTypeDef,
        "Range": ClientListIndexRangesOnIndexedValuesRangeTypeDef,
    },
    total=False,
)

ClientListIndexResponseIndexAttachmentsIndexedAttributesKeyTypeDef = TypedDict(
    "ClientListIndexResponseIndexAttachmentsIndexedAttributesKeyTypeDef",
    {"SchemaArn": str, "FacetName": str, "Name": str},
    total=False,
)

ClientListIndexResponseIndexAttachmentsIndexedAttributesValueTypeDef = TypedDict(
    "ClientListIndexResponseIndexAttachmentsIndexedAttributesValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)

ClientListIndexResponseIndexAttachmentsIndexedAttributesTypeDef = TypedDict(
    "ClientListIndexResponseIndexAttachmentsIndexedAttributesTypeDef",
    {
        "Key": ClientListIndexResponseIndexAttachmentsIndexedAttributesKeyTypeDef,
        "Value": ClientListIndexResponseIndexAttachmentsIndexedAttributesValueTypeDef,
    },
    total=False,
)

ClientListIndexResponseIndexAttachmentsTypeDef = TypedDict(
    "ClientListIndexResponseIndexAttachmentsTypeDef",
    {
        "IndexedAttributes": List[ClientListIndexResponseIndexAttachmentsIndexedAttributesTypeDef],
        "ObjectIdentifier": str,
    },
    total=False,
)

ClientListIndexResponseTypeDef = TypedDict(
    "ClientListIndexResponseTypeDef",
    {"IndexAttachments": List[ClientListIndexResponseIndexAttachmentsTypeDef], "NextToken": str},
    total=False,
)

ClientListManagedSchemaArnsResponseTypeDef = TypedDict(
    "ClientListManagedSchemaArnsResponseTypeDef",
    {"SchemaArns": List[str], "NextToken": str},
    total=False,
)

ClientListObjectAttributesFacetFilterTypeDef = TypedDict(
    "ClientListObjectAttributesFacetFilterTypeDef",
    {"SchemaArn": str, "FacetName": str},
    total=False,
)

ClientListObjectAttributesObjectReferenceTypeDef = TypedDict(
    "ClientListObjectAttributesObjectReferenceTypeDef", {"Selector": str}, total=False
)

ClientListObjectAttributesResponseAttributesKeyTypeDef = TypedDict(
    "ClientListObjectAttributesResponseAttributesKeyTypeDef",
    {"SchemaArn": str, "FacetName": str, "Name": str},
    total=False,
)

ClientListObjectAttributesResponseAttributesValueTypeDef = TypedDict(
    "ClientListObjectAttributesResponseAttributesValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)

ClientListObjectAttributesResponseAttributesTypeDef = TypedDict(
    "ClientListObjectAttributesResponseAttributesTypeDef",
    {
        "Key": ClientListObjectAttributesResponseAttributesKeyTypeDef,
        "Value": ClientListObjectAttributesResponseAttributesValueTypeDef,
    },
    total=False,
)

ClientListObjectAttributesResponseTypeDef = TypedDict(
    "ClientListObjectAttributesResponseTypeDef",
    {"Attributes": List[ClientListObjectAttributesResponseAttributesTypeDef], "NextToken": str},
    total=False,
)

ClientListObjectChildrenObjectReferenceTypeDef = TypedDict(
    "ClientListObjectChildrenObjectReferenceTypeDef", {"Selector": str}, total=False
)

ClientListObjectChildrenResponseTypeDef = TypedDict(
    "ClientListObjectChildrenResponseTypeDef",
    {"Children": Dict[str, str], "NextToken": str},
    total=False,
)

ClientListObjectParentPathsObjectReferenceTypeDef = TypedDict(
    "ClientListObjectParentPathsObjectReferenceTypeDef", {"Selector": str}, total=False
)

ClientListObjectParentPathsResponsePathToObjectIdentifiersListTypeDef = TypedDict(
    "ClientListObjectParentPathsResponsePathToObjectIdentifiersListTypeDef",
    {"Path": str, "ObjectIdentifiers": List[str]},
    total=False,
)

ClientListObjectParentPathsResponseTypeDef = TypedDict(
    "ClientListObjectParentPathsResponseTypeDef",
    {
        "PathToObjectIdentifiersList": List[
            ClientListObjectParentPathsResponsePathToObjectIdentifiersListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientListObjectParentsObjectReferenceTypeDef = TypedDict(
    "ClientListObjectParentsObjectReferenceTypeDef", {"Selector": str}, total=False
)

ClientListObjectParentsResponseParentLinksTypeDef = TypedDict(
    "ClientListObjectParentsResponseParentLinksTypeDef",
    {"ObjectIdentifier": str, "LinkName": str},
    total=False,
)

ClientListObjectParentsResponseTypeDef = TypedDict(
    "ClientListObjectParentsResponseTypeDef",
    {
        "Parents": Dict[str, str],
        "NextToken": str,
        "ParentLinks": List[ClientListObjectParentsResponseParentLinksTypeDef],
    },
    total=False,
)

ClientListObjectPoliciesObjectReferenceTypeDef = TypedDict(
    "ClientListObjectPoliciesObjectReferenceTypeDef", {"Selector": str}, total=False
)

ClientListObjectPoliciesResponseTypeDef = TypedDict(
    "ClientListObjectPoliciesResponseTypeDef",
    {"AttachedPolicyIds": List[str], "NextToken": str},
    total=False,
)

ClientListOutgoingTypedLinksFilterAttributeRangesRangeEndValueTypeDef = TypedDict(
    "ClientListOutgoingTypedLinksFilterAttributeRangesRangeEndValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)

ClientListOutgoingTypedLinksFilterAttributeRangesRangeStartValueTypeDef = TypedDict(
    "ClientListOutgoingTypedLinksFilterAttributeRangesRangeStartValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)

ClientListOutgoingTypedLinksFilterAttributeRangesRangeTypeDef = TypedDict(
    "ClientListOutgoingTypedLinksFilterAttributeRangesRangeTypeDef",
    {
        "StartMode": Literal[
            "FIRST", "LAST", "LAST_BEFORE_MISSING_VALUES", "INCLUSIVE", "EXCLUSIVE"
        ],
        "StartValue": ClientListOutgoingTypedLinksFilterAttributeRangesRangeStartValueTypeDef,
        "EndMode": Literal["FIRST", "LAST", "LAST_BEFORE_MISSING_VALUES", "INCLUSIVE", "EXCLUSIVE"],
        "EndValue": ClientListOutgoingTypedLinksFilterAttributeRangesRangeEndValueTypeDef,
    },
    total=False,
)

ClientListOutgoingTypedLinksFilterAttributeRangesTypeDef = TypedDict(
    "ClientListOutgoingTypedLinksFilterAttributeRangesTypeDef",
    {"AttributeName": str, "Range": ClientListOutgoingTypedLinksFilterAttributeRangesRangeTypeDef},
    total=False,
)

_RequiredClientListOutgoingTypedLinksFilterTypedLinkTypeDef = TypedDict(
    "_RequiredClientListOutgoingTypedLinksFilterTypedLinkTypeDef", {"SchemaArn": str}
)
_OptionalClientListOutgoingTypedLinksFilterTypedLinkTypeDef = TypedDict(
    "_OptionalClientListOutgoingTypedLinksFilterTypedLinkTypeDef",
    {"TypedLinkName": str},
    total=False,
)


class ClientListOutgoingTypedLinksFilterTypedLinkTypeDef(
    _RequiredClientListOutgoingTypedLinksFilterTypedLinkTypeDef,
    _OptionalClientListOutgoingTypedLinksFilterTypedLinkTypeDef,
):
    pass


ClientListOutgoingTypedLinksObjectReferenceTypeDef = TypedDict(
    "ClientListOutgoingTypedLinksObjectReferenceTypeDef", {"Selector": str}, total=False
)

ClientListOutgoingTypedLinksResponseTypedLinkSpecifiersIdentityAttributeValuesValueTypeDef = TypedDict(
    "ClientListOutgoingTypedLinksResponseTypedLinkSpecifiersIdentityAttributeValuesValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)

ClientListOutgoingTypedLinksResponseTypedLinkSpecifiersIdentityAttributeValuesTypeDef = TypedDict(
    "ClientListOutgoingTypedLinksResponseTypedLinkSpecifiersIdentityAttributeValuesTypeDef",
    {
        "AttributeName": str,
        "Value": ClientListOutgoingTypedLinksResponseTypedLinkSpecifiersIdentityAttributeValuesValueTypeDef,
    },
    total=False,
)

ClientListOutgoingTypedLinksResponseTypedLinkSpecifiersSourceObjectReferenceTypeDef = TypedDict(
    "ClientListOutgoingTypedLinksResponseTypedLinkSpecifiersSourceObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)

ClientListOutgoingTypedLinksResponseTypedLinkSpecifiersTargetObjectReferenceTypeDef = TypedDict(
    "ClientListOutgoingTypedLinksResponseTypedLinkSpecifiersTargetObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)

ClientListOutgoingTypedLinksResponseTypedLinkSpecifiersTypedLinkFacetTypeDef = TypedDict(
    "ClientListOutgoingTypedLinksResponseTypedLinkSpecifiersTypedLinkFacetTypeDef",
    {"SchemaArn": str, "TypedLinkName": str},
    total=False,
)

ClientListOutgoingTypedLinksResponseTypedLinkSpecifiersTypeDef = TypedDict(
    "ClientListOutgoingTypedLinksResponseTypedLinkSpecifiersTypeDef",
    {
        "TypedLinkFacet": ClientListOutgoingTypedLinksResponseTypedLinkSpecifiersTypedLinkFacetTypeDef,
        "SourceObjectReference": ClientListOutgoingTypedLinksResponseTypedLinkSpecifiersSourceObjectReferenceTypeDef,
        "TargetObjectReference": ClientListOutgoingTypedLinksResponseTypedLinkSpecifiersTargetObjectReferenceTypeDef,
        "IdentityAttributeValues": List[
            ClientListOutgoingTypedLinksResponseTypedLinkSpecifiersIdentityAttributeValuesTypeDef
        ],
    },
    total=False,
)

ClientListOutgoingTypedLinksResponseTypeDef = TypedDict(
    "ClientListOutgoingTypedLinksResponseTypeDef",
    {
        "TypedLinkSpecifiers": List[ClientListOutgoingTypedLinksResponseTypedLinkSpecifiersTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientListPolicyAttachmentsPolicyReferenceTypeDef = TypedDict(
    "ClientListPolicyAttachmentsPolicyReferenceTypeDef", {"Selector": str}, total=False
)

ClientListPolicyAttachmentsResponseTypeDef = TypedDict(
    "ClientListPolicyAttachmentsResponseTypeDef",
    {"ObjectIdentifiers": List[str], "NextToken": str},
    total=False,
)

ClientListPublishedSchemaArnsResponseTypeDef = TypedDict(
    "ClientListPublishedSchemaArnsResponseTypeDef",
    {"SchemaArns": List[str], "NextToken": str},
    total=False,
)

ClientListTagsForResourceResponseTagsTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientListTagsForResourceResponseTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTypeDef",
    {"Tags": List[ClientListTagsForResourceResponseTagsTypeDef], "NextToken": str},
    total=False,
)

ClientListTypedLinkFacetAttributesResponseAttributesDefaultValueTypeDef = TypedDict(
    "ClientListTypedLinkFacetAttributesResponseAttributesDefaultValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)

ClientListTypedLinkFacetAttributesResponseAttributesRulesTypeDef = TypedDict(
    "ClientListTypedLinkFacetAttributesResponseAttributesRulesTypeDef",
    {
        "Type": Literal["BINARY_LENGTH", "NUMBER_COMPARISON", "STRING_FROM_SET", "STRING_LENGTH"],
        "Parameters": Dict[str, str],
    },
    total=False,
)

ClientListTypedLinkFacetAttributesResponseAttributesTypeDef = TypedDict(
    "ClientListTypedLinkFacetAttributesResponseAttributesTypeDef",
    {
        "Name": str,
        "Type": Literal["STRING", "BINARY", "BOOLEAN", "NUMBER", "DATETIME", "VARIANT"],
        "DefaultValue": ClientListTypedLinkFacetAttributesResponseAttributesDefaultValueTypeDef,
        "IsImmutable": bool,
        "Rules": Dict[str, ClientListTypedLinkFacetAttributesResponseAttributesRulesTypeDef],
        "RequiredBehavior": Literal["REQUIRED_ALWAYS", "NOT_REQUIRED"],
    },
    total=False,
)

ClientListTypedLinkFacetAttributesResponseTypeDef = TypedDict(
    "ClientListTypedLinkFacetAttributesResponseTypeDef",
    {
        "Attributes": List[ClientListTypedLinkFacetAttributesResponseAttributesTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientListTypedLinkFacetNamesResponseTypeDef = TypedDict(
    "ClientListTypedLinkFacetNamesResponseTypeDef",
    {"FacetNames": List[str], "NextToken": str},
    total=False,
)

ClientLookupPolicyObjectReferenceTypeDef = TypedDict(
    "ClientLookupPolicyObjectReferenceTypeDef", {"Selector": str}, total=False
)

ClientLookupPolicyResponsePolicyToPathListPoliciesTypeDef = TypedDict(
    "ClientLookupPolicyResponsePolicyToPathListPoliciesTypeDef",
    {"PolicyId": str, "ObjectIdentifier": str, "PolicyType": str},
    total=False,
)

ClientLookupPolicyResponsePolicyToPathListTypeDef = TypedDict(
    "ClientLookupPolicyResponsePolicyToPathListTypeDef",
    {"Path": str, "Policies": List[ClientLookupPolicyResponsePolicyToPathListPoliciesTypeDef]},
    total=False,
)

ClientLookupPolicyResponseTypeDef = TypedDict(
    "ClientLookupPolicyResponseTypeDef",
    {"PolicyToPathList": List[ClientLookupPolicyResponsePolicyToPathListTypeDef], "NextToken": str},
    total=False,
)

ClientPublishSchemaResponseTypeDef = TypedDict(
    "ClientPublishSchemaResponseTypeDef", {"PublishedSchemaArn": str}, total=False
)

ClientPutSchemaFromJsonResponseTypeDef = TypedDict(
    "ClientPutSchemaFromJsonResponseTypeDef", {"Arn": str}, total=False
)

ClientRemoveFacetFromObjectObjectReferenceTypeDef = TypedDict(
    "ClientRemoveFacetFromObjectObjectReferenceTypeDef", {"Selector": str}, total=False
)

ClientRemoveFacetFromObjectSchemaFacetTypeDef = TypedDict(
    "ClientRemoveFacetFromObjectSchemaFacetTypeDef",
    {"SchemaArn": str, "FacetName": str},
    total=False,
)

ClientTagResourceTagsTypeDef = TypedDict(
    "ClientTagResourceTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientUpdateFacetAttributeUpdatesAttributeAttributeDefinitionDefaultValueTypeDef = TypedDict(
    "ClientUpdateFacetAttributeUpdatesAttributeAttributeDefinitionDefaultValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)

ClientUpdateFacetAttributeUpdatesAttributeAttributeDefinitionRulesTypeDef = TypedDict(
    "ClientUpdateFacetAttributeUpdatesAttributeAttributeDefinitionRulesTypeDef",
    {
        "Type": Literal["BINARY_LENGTH", "NUMBER_COMPARISON", "STRING_FROM_SET", "STRING_LENGTH"],
        "Parameters": Dict[str, str],
    },
    total=False,
)

ClientUpdateFacetAttributeUpdatesAttributeAttributeDefinitionTypeDef = TypedDict(
    "ClientUpdateFacetAttributeUpdatesAttributeAttributeDefinitionTypeDef",
    {
        "Type": Literal["STRING", "BINARY", "BOOLEAN", "NUMBER", "DATETIME", "VARIANT"],
        "DefaultValue": ClientUpdateFacetAttributeUpdatesAttributeAttributeDefinitionDefaultValueTypeDef,
        "IsImmutable": bool,
        "Rules": Dict[
            str, ClientUpdateFacetAttributeUpdatesAttributeAttributeDefinitionRulesTypeDef
        ],
    },
    total=False,
)

ClientUpdateFacetAttributeUpdatesAttributeAttributeReferenceTypeDef = TypedDict(
    "ClientUpdateFacetAttributeUpdatesAttributeAttributeReferenceTypeDef",
    {"TargetFacetName": str, "TargetAttributeName": str},
    total=False,
)

_RequiredClientUpdateFacetAttributeUpdatesAttributeTypeDef = TypedDict(
    "_RequiredClientUpdateFacetAttributeUpdatesAttributeTypeDef", {"Name": str}
)
_OptionalClientUpdateFacetAttributeUpdatesAttributeTypeDef = TypedDict(
    "_OptionalClientUpdateFacetAttributeUpdatesAttributeTypeDef",
    {
        "AttributeDefinition": ClientUpdateFacetAttributeUpdatesAttributeAttributeDefinitionTypeDef,
        "AttributeReference": ClientUpdateFacetAttributeUpdatesAttributeAttributeReferenceTypeDef,
        "RequiredBehavior": Literal["REQUIRED_ALWAYS", "NOT_REQUIRED"],
    },
    total=False,
)


class ClientUpdateFacetAttributeUpdatesAttributeTypeDef(
    _RequiredClientUpdateFacetAttributeUpdatesAttributeTypeDef,
    _OptionalClientUpdateFacetAttributeUpdatesAttributeTypeDef,
):
    pass


ClientUpdateFacetAttributeUpdatesTypeDef = TypedDict(
    "ClientUpdateFacetAttributeUpdatesTypeDef",
    {
        "Attribute": ClientUpdateFacetAttributeUpdatesAttributeTypeDef,
        "Action": Literal["CREATE_OR_UPDATE", "DELETE"],
    },
    total=False,
)

ClientUpdateLinkAttributesAttributeUpdatesAttributeActionAttributeUpdateValueTypeDef = TypedDict(
    "ClientUpdateLinkAttributesAttributeUpdatesAttributeActionAttributeUpdateValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)

ClientUpdateLinkAttributesAttributeUpdatesAttributeActionTypeDef = TypedDict(
    "ClientUpdateLinkAttributesAttributeUpdatesAttributeActionTypeDef",
    {
        "AttributeActionType": Literal["CREATE_OR_UPDATE", "DELETE"],
        "AttributeUpdateValue": ClientUpdateLinkAttributesAttributeUpdatesAttributeActionAttributeUpdateValueTypeDef,
    },
    total=False,
)

_RequiredClientUpdateLinkAttributesAttributeUpdatesAttributeKeyTypeDef = TypedDict(
    "_RequiredClientUpdateLinkAttributesAttributeUpdatesAttributeKeyTypeDef", {"SchemaArn": str}
)
_OptionalClientUpdateLinkAttributesAttributeUpdatesAttributeKeyTypeDef = TypedDict(
    "_OptionalClientUpdateLinkAttributesAttributeUpdatesAttributeKeyTypeDef",
    {"FacetName": str, "Name": str},
    total=False,
)


class ClientUpdateLinkAttributesAttributeUpdatesAttributeKeyTypeDef(
    _RequiredClientUpdateLinkAttributesAttributeUpdatesAttributeKeyTypeDef,
    _OptionalClientUpdateLinkAttributesAttributeUpdatesAttributeKeyTypeDef,
):
    pass


ClientUpdateLinkAttributesAttributeUpdatesTypeDef = TypedDict(
    "ClientUpdateLinkAttributesAttributeUpdatesTypeDef",
    {
        "AttributeKey": ClientUpdateLinkAttributesAttributeUpdatesAttributeKeyTypeDef,
        "AttributeAction": ClientUpdateLinkAttributesAttributeUpdatesAttributeActionTypeDef,
    },
    total=False,
)

ClientUpdateLinkAttributesTypedLinkSpecifierIdentityAttributeValuesValueTypeDef = TypedDict(
    "ClientUpdateLinkAttributesTypedLinkSpecifierIdentityAttributeValuesValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)

ClientUpdateLinkAttributesTypedLinkSpecifierIdentityAttributeValuesTypeDef = TypedDict(
    "ClientUpdateLinkAttributesTypedLinkSpecifierIdentityAttributeValuesTypeDef",
    {
        "AttributeName": str,
        "Value": ClientUpdateLinkAttributesTypedLinkSpecifierIdentityAttributeValuesValueTypeDef,
    },
    total=False,
)

ClientUpdateLinkAttributesTypedLinkSpecifierSourceObjectReferenceTypeDef = TypedDict(
    "ClientUpdateLinkAttributesTypedLinkSpecifierSourceObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)

ClientUpdateLinkAttributesTypedLinkSpecifierTargetObjectReferenceTypeDef = TypedDict(
    "ClientUpdateLinkAttributesTypedLinkSpecifierTargetObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)

_RequiredClientUpdateLinkAttributesTypedLinkSpecifierTypedLinkFacetTypeDef = TypedDict(
    "_RequiredClientUpdateLinkAttributesTypedLinkSpecifierTypedLinkFacetTypeDef", {"SchemaArn": str}
)
_OptionalClientUpdateLinkAttributesTypedLinkSpecifierTypedLinkFacetTypeDef = TypedDict(
    "_OptionalClientUpdateLinkAttributesTypedLinkSpecifierTypedLinkFacetTypeDef",
    {"TypedLinkName": str},
    total=False,
)


class ClientUpdateLinkAttributesTypedLinkSpecifierTypedLinkFacetTypeDef(
    _RequiredClientUpdateLinkAttributesTypedLinkSpecifierTypedLinkFacetTypeDef,
    _OptionalClientUpdateLinkAttributesTypedLinkSpecifierTypedLinkFacetTypeDef,
):
    pass


_RequiredClientUpdateLinkAttributesTypedLinkSpecifierTypeDef = TypedDict(
    "_RequiredClientUpdateLinkAttributesTypedLinkSpecifierTypeDef",
    {"TypedLinkFacet": ClientUpdateLinkAttributesTypedLinkSpecifierTypedLinkFacetTypeDef},
)
_OptionalClientUpdateLinkAttributesTypedLinkSpecifierTypeDef = TypedDict(
    "_OptionalClientUpdateLinkAttributesTypedLinkSpecifierTypeDef",
    {
        "SourceObjectReference": ClientUpdateLinkAttributesTypedLinkSpecifierSourceObjectReferenceTypeDef,
        "TargetObjectReference": ClientUpdateLinkAttributesTypedLinkSpecifierTargetObjectReferenceTypeDef,
        "IdentityAttributeValues": List[
            ClientUpdateLinkAttributesTypedLinkSpecifierIdentityAttributeValuesTypeDef
        ],
    },
    total=False,
)


class ClientUpdateLinkAttributesTypedLinkSpecifierTypeDef(
    _RequiredClientUpdateLinkAttributesTypedLinkSpecifierTypeDef,
    _OptionalClientUpdateLinkAttributesTypedLinkSpecifierTypeDef,
):
    pass


ClientUpdateObjectAttributesAttributeUpdatesObjectAttributeActionObjectAttributeUpdateValueTypeDef = TypedDict(
    "ClientUpdateObjectAttributesAttributeUpdatesObjectAttributeActionObjectAttributeUpdateValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)

ClientUpdateObjectAttributesAttributeUpdatesObjectAttributeActionTypeDef = TypedDict(
    "ClientUpdateObjectAttributesAttributeUpdatesObjectAttributeActionTypeDef",
    {
        "ObjectAttributeActionType": Literal["CREATE_OR_UPDATE", "DELETE"],
        "ObjectAttributeUpdateValue": ClientUpdateObjectAttributesAttributeUpdatesObjectAttributeActionObjectAttributeUpdateValueTypeDef,
    },
    total=False,
)

_RequiredClientUpdateObjectAttributesAttributeUpdatesObjectAttributeKeyTypeDef = TypedDict(
    "_RequiredClientUpdateObjectAttributesAttributeUpdatesObjectAttributeKeyTypeDef",
    {"SchemaArn": str},
)
_OptionalClientUpdateObjectAttributesAttributeUpdatesObjectAttributeKeyTypeDef = TypedDict(
    "_OptionalClientUpdateObjectAttributesAttributeUpdatesObjectAttributeKeyTypeDef",
    {"FacetName": str, "Name": str},
    total=False,
)


class ClientUpdateObjectAttributesAttributeUpdatesObjectAttributeKeyTypeDef(
    _RequiredClientUpdateObjectAttributesAttributeUpdatesObjectAttributeKeyTypeDef,
    _OptionalClientUpdateObjectAttributesAttributeUpdatesObjectAttributeKeyTypeDef,
):
    pass


ClientUpdateObjectAttributesAttributeUpdatesTypeDef = TypedDict(
    "ClientUpdateObjectAttributesAttributeUpdatesTypeDef",
    {
        "ObjectAttributeKey": ClientUpdateObjectAttributesAttributeUpdatesObjectAttributeKeyTypeDef,
        "ObjectAttributeAction": ClientUpdateObjectAttributesAttributeUpdatesObjectAttributeActionTypeDef,
    },
    total=False,
)

ClientUpdateObjectAttributesObjectReferenceTypeDef = TypedDict(
    "ClientUpdateObjectAttributesObjectReferenceTypeDef", {"Selector": str}, total=False
)

ClientUpdateObjectAttributesResponseTypeDef = TypedDict(
    "ClientUpdateObjectAttributesResponseTypeDef", {"ObjectIdentifier": str}, total=False
)

ClientUpdateSchemaResponseTypeDef = TypedDict(
    "ClientUpdateSchemaResponseTypeDef", {"SchemaArn": str}, total=False
)

ClientUpdateTypedLinkFacetAttributeUpdatesAttributeDefaultValueTypeDef = TypedDict(
    "ClientUpdateTypedLinkFacetAttributeUpdatesAttributeDefaultValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)

ClientUpdateTypedLinkFacetAttributeUpdatesAttributeRulesTypeDef = TypedDict(
    "ClientUpdateTypedLinkFacetAttributeUpdatesAttributeRulesTypeDef",
    {
        "Type": Literal["BINARY_LENGTH", "NUMBER_COMPARISON", "STRING_FROM_SET", "STRING_LENGTH"],
        "Parameters": Dict[str, str],
    },
    total=False,
)

_RequiredClientUpdateTypedLinkFacetAttributeUpdatesAttributeTypeDef = TypedDict(
    "_RequiredClientUpdateTypedLinkFacetAttributeUpdatesAttributeTypeDef", {"Name": str}
)
_OptionalClientUpdateTypedLinkFacetAttributeUpdatesAttributeTypeDef = TypedDict(
    "_OptionalClientUpdateTypedLinkFacetAttributeUpdatesAttributeTypeDef",
    {
        "Type": Literal["STRING", "BINARY", "BOOLEAN", "NUMBER", "DATETIME", "VARIANT"],
        "DefaultValue": ClientUpdateTypedLinkFacetAttributeUpdatesAttributeDefaultValueTypeDef,
        "IsImmutable": bool,
        "Rules": Dict[str, ClientUpdateTypedLinkFacetAttributeUpdatesAttributeRulesTypeDef],
        "RequiredBehavior": Literal["REQUIRED_ALWAYS", "NOT_REQUIRED"],
    },
    total=False,
)


class ClientUpdateTypedLinkFacetAttributeUpdatesAttributeTypeDef(
    _RequiredClientUpdateTypedLinkFacetAttributeUpdatesAttributeTypeDef,
    _OptionalClientUpdateTypedLinkFacetAttributeUpdatesAttributeTypeDef,
):
    pass


_RequiredClientUpdateTypedLinkFacetAttributeUpdatesTypeDef = TypedDict(
    "_RequiredClientUpdateTypedLinkFacetAttributeUpdatesTypeDef",
    {"Attribute": ClientUpdateTypedLinkFacetAttributeUpdatesAttributeTypeDef},
)
_OptionalClientUpdateTypedLinkFacetAttributeUpdatesTypeDef = TypedDict(
    "_OptionalClientUpdateTypedLinkFacetAttributeUpdatesTypeDef",
    {"Action": Literal["CREATE_OR_UPDATE", "DELETE"]},
    total=False,
)


class ClientUpdateTypedLinkFacetAttributeUpdatesTypeDef(
    _RequiredClientUpdateTypedLinkFacetAttributeUpdatesTypeDef,
    _OptionalClientUpdateTypedLinkFacetAttributeUpdatesTypeDef,
):
    pass


ClientUpgradeAppliedSchemaResponseTypeDef = TypedDict(
    "ClientUpgradeAppliedSchemaResponseTypeDef",
    {"UpgradedSchemaArn": str, "DirectoryArn": str},
    total=False,
)

ClientUpgradePublishedSchemaResponseTypeDef = TypedDict(
    "ClientUpgradePublishedSchemaResponseTypeDef", {"UpgradedSchemaArn": str}, total=False
)

ListAppliedSchemaArnsResponseTypeDef = TypedDict(
    "ListAppliedSchemaArnsResponseTypeDef", {"SchemaArns": List[str], "NextToken": str}, total=False
)

AttributeKeyTypeDef = TypedDict(
    "AttributeKeyTypeDef", {"SchemaArn": str, "FacetName": str, "Name": str}
)

TypedAttributeValueTypeDef = TypedDict(
    "TypedAttributeValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": Union[bytes, IO],
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)

AttributeKeyAndValueTypeDef = TypedDict(
    "AttributeKeyAndValueTypeDef", {"Key": AttributeKeyTypeDef, "Value": TypedAttributeValueTypeDef}
)

IndexAttachmentTypeDef = TypedDict(
    "IndexAttachmentTypeDef",
    {"IndexedAttributes": List[AttributeKeyAndValueTypeDef], "ObjectIdentifier": str},
    total=False,
)

ListAttachedIndicesResponseTypeDef = TypedDict(
    "ListAttachedIndicesResponseTypeDef",
    {"IndexAttachments": List[IndexAttachmentTypeDef], "NextToken": str},
    total=False,
)

ListDevelopmentSchemaArnsResponseTypeDef = TypedDict(
    "ListDevelopmentSchemaArnsResponseTypeDef",
    {"SchemaArns": List[str], "NextToken": str},
    total=False,
)

DirectoryTypeDef = TypedDict(
    "DirectoryTypeDef",
    {
        "Name": str,
        "DirectoryArn": str,
        "State": Literal["ENABLED", "DISABLED", "DELETED"],
        "CreationDateTime": datetime,
    },
    total=False,
)

_RequiredListDirectoriesResponseTypeDef = TypedDict(
    "_RequiredListDirectoriesResponseTypeDef", {"Directories": List[DirectoryTypeDef]}
)
_OptionalListDirectoriesResponseTypeDef = TypedDict(
    "_OptionalListDirectoriesResponseTypeDef", {"NextToken": str}, total=False
)


class ListDirectoriesResponseTypeDef(
    _RequiredListDirectoriesResponseTypeDef, _OptionalListDirectoriesResponseTypeDef
):
    pass


RuleTypeDef = TypedDict(
    "RuleTypeDef",
    {
        "Type": Literal["BINARY_LENGTH", "NUMBER_COMPARISON", "STRING_FROM_SET", "STRING_LENGTH"],
        "Parameters": Dict[str, str],
    },
    total=False,
)

_RequiredFacetAttributeDefinitionTypeDef = TypedDict(
    "_RequiredFacetAttributeDefinitionTypeDef",
    {"Type": Literal["STRING", "BINARY", "BOOLEAN", "NUMBER", "DATETIME", "VARIANT"]},
)
_OptionalFacetAttributeDefinitionTypeDef = TypedDict(
    "_OptionalFacetAttributeDefinitionTypeDef",
    {
        "DefaultValue": TypedAttributeValueTypeDef,
        "IsImmutable": bool,
        "Rules": Dict[str, RuleTypeDef],
    },
    total=False,
)


class FacetAttributeDefinitionTypeDef(
    _RequiredFacetAttributeDefinitionTypeDef, _OptionalFacetAttributeDefinitionTypeDef
):
    pass


FacetAttributeReferenceTypeDef = TypedDict(
    "FacetAttributeReferenceTypeDef", {"TargetFacetName": str, "TargetAttributeName": str}
)

_RequiredFacetAttributeTypeDef = TypedDict("_RequiredFacetAttributeTypeDef", {"Name": str})
_OptionalFacetAttributeTypeDef = TypedDict(
    "_OptionalFacetAttributeTypeDef",
    {
        "AttributeDefinition": FacetAttributeDefinitionTypeDef,
        "AttributeReference": FacetAttributeReferenceTypeDef,
        "RequiredBehavior": Literal["REQUIRED_ALWAYS", "NOT_REQUIRED"],
    },
    total=False,
)


class FacetAttributeTypeDef(_RequiredFacetAttributeTypeDef, _OptionalFacetAttributeTypeDef):
    pass


ListFacetAttributesResponseTypeDef = TypedDict(
    "ListFacetAttributesResponseTypeDef",
    {"Attributes": List[FacetAttributeTypeDef], "NextToken": str},
    total=False,
)

ListFacetNamesResponseTypeDef = TypedDict(
    "ListFacetNamesResponseTypeDef", {"FacetNames": List[str], "NextToken": str}, total=False
)

AttributeNameAndValueTypeDef = TypedDict(
    "AttributeNameAndValueTypeDef", {"AttributeName": str, "Value": TypedAttributeValueTypeDef}
)

ObjectReferenceTypeDef = TypedDict("ObjectReferenceTypeDef", {"Selector": str}, total=False)

TypedLinkSchemaAndFacetNameTypeDef = TypedDict(
    "TypedLinkSchemaAndFacetNameTypeDef", {"SchemaArn": str, "TypedLinkName": str}
)

TypedLinkSpecifierTypeDef = TypedDict(
    "TypedLinkSpecifierTypeDef",
    {
        "TypedLinkFacet": TypedLinkSchemaAndFacetNameTypeDef,
        "SourceObjectReference": ObjectReferenceTypeDef,
        "TargetObjectReference": ObjectReferenceTypeDef,
        "IdentityAttributeValues": List[AttributeNameAndValueTypeDef],
    },
)

ListIncomingTypedLinksResponseTypeDef = TypedDict(
    "ListIncomingTypedLinksResponseTypeDef",
    {"LinkSpecifiers": List[TypedLinkSpecifierTypeDef], "NextToken": str},
    total=False,
)

ListIndexResponseTypeDef = TypedDict(
    "ListIndexResponseTypeDef",
    {"IndexAttachments": List[IndexAttachmentTypeDef], "NextToken": str},
    total=False,
)

ListManagedSchemaArnsResponseTypeDef = TypedDict(
    "ListManagedSchemaArnsResponseTypeDef", {"SchemaArns": List[str], "NextToken": str}, total=False
)

ListObjectAttributesResponseTypeDef = TypedDict(
    "ListObjectAttributesResponseTypeDef",
    {"Attributes": List[AttributeKeyAndValueTypeDef], "NextToken": str},
    total=False,
)

PathToObjectIdentifiersTypeDef = TypedDict(
    "PathToObjectIdentifiersTypeDef", {"Path": str, "ObjectIdentifiers": List[str]}, total=False
)

ListObjectParentPathsResponseTypeDef = TypedDict(
    "ListObjectParentPathsResponseTypeDef",
    {"PathToObjectIdentifiersList": List[PathToObjectIdentifiersTypeDef], "NextToken": str},
    total=False,
)

ListObjectPoliciesResponseTypeDef = TypedDict(
    "ListObjectPoliciesResponseTypeDef",
    {"AttachedPolicyIds": List[str], "NextToken": str},
    total=False,
)

ListOutgoingTypedLinksResponseTypeDef = TypedDict(
    "ListOutgoingTypedLinksResponseTypeDef",
    {"TypedLinkSpecifiers": List[TypedLinkSpecifierTypeDef], "NextToken": str},
    total=False,
)

ListPolicyAttachmentsResponseTypeDef = TypedDict(
    "ListPolicyAttachmentsResponseTypeDef",
    {"ObjectIdentifiers": List[str], "NextToken": str},
    total=False,
)

ListPublishedSchemaArnsResponseTypeDef = TypedDict(
    "ListPublishedSchemaArnsResponseTypeDef",
    {"SchemaArns": List[str], "NextToken": str},
    total=False,
)

TagTypeDef = TypedDict("TagTypeDef", {"Key": str, "Value": str}, total=False)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef", {"Tags": List[TagTypeDef], "NextToken": str}, total=False
)

_RequiredTypedLinkAttributeDefinitionTypeDef = TypedDict(
    "_RequiredTypedLinkAttributeDefinitionTypeDef",
    {
        "Name": str,
        "Type": Literal["STRING", "BINARY", "BOOLEAN", "NUMBER", "DATETIME", "VARIANT"],
        "RequiredBehavior": Literal["REQUIRED_ALWAYS", "NOT_REQUIRED"],
    },
)
_OptionalTypedLinkAttributeDefinitionTypeDef = TypedDict(
    "_OptionalTypedLinkAttributeDefinitionTypeDef",
    {
        "DefaultValue": TypedAttributeValueTypeDef,
        "IsImmutable": bool,
        "Rules": Dict[str, RuleTypeDef],
    },
    total=False,
)


class TypedLinkAttributeDefinitionTypeDef(
    _RequiredTypedLinkAttributeDefinitionTypeDef, _OptionalTypedLinkAttributeDefinitionTypeDef
):
    pass


ListTypedLinkFacetAttributesResponseTypeDef = TypedDict(
    "ListTypedLinkFacetAttributesResponseTypeDef",
    {"Attributes": List[TypedLinkAttributeDefinitionTypeDef], "NextToken": str},
    total=False,
)

ListTypedLinkFacetNamesResponseTypeDef = TypedDict(
    "ListTypedLinkFacetNamesResponseTypeDef",
    {"FacetNames": List[str], "NextToken": str},
    total=False,
)

PolicyAttachmentTypeDef = TypedDict(
    "PolicyAttachmentTypeDef",
    {"PolicyId": str, "ObjectIdentifier": str, "PolicyType": str},
    total=False,
)

PolicyToPathTypeDef = TypedDict(
    "PolicyToPathTypeDef", {"Path": str, "Policies": List[PolicyAttachmentTypeDef]}, total=False
)

LookupPolicyResponseTypeDef = TypedDict(
    "LookupPolicyResponseTypeDef",
    {"PolicyToPathList": List[PolicyToPathTypeDef], "NextToken": str},
    total=False,
)

_RequiredTypedAttributeValueRangeTypeDef = TypedDict(
    "_RequiredTypedAttributeValueRangeTypeDef",
    {
        "StartMode": Literal[
            "FIRST", "LAST", "LAST_BEFORE_MISSING_VALUES", "INCLUSIVE", "EXCLUSIVE"
        ],
        "EndMode": Literal["FIRST", "LAST", "LAST_BEFORE_MISSING_VALUES", "INCLUSIVE", "EXCLUSIVE"],
    },
)
_OptionalTypedAttributeValueRangeTypeDef = TypedDict(
    "_OptionalTypedAttributeValueRangeTypeDef",
    {"StartValue": TypedAttributeValueTypeDef, "EndValue": TypedAttributeValueTypeDef},
    total=False,
)


class TypedAttributeValueRangeTypeDef(
    _RequiredTypedAttributeValueRangeTypeDef, _OptionalTypedAttributeValueRangeTypeDef
):
    pass


ObjectAttributeRangeTypeDef = TypedDict(
    "ObjectAttributeRangeTypeDef",
    {"AttributeKey": AttributeKeyTypeDef, "Range": TypedAttributeValueRangeTypeDef},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

SchemaFacetTypeDef = TypedDict(
    "SchemaFacetTypeDef", {"SchemaArn": str, "FacetName": str}, total=False
)

_RequiredTypedLinkAttributeRangeTypeDef = TypedDict(
    "_RequiredTypedLinkAttributeRangeTypeDef", {"Range": TypedAttributeValueRangeTypeDef}
)
_OptionalTypedLinkAttributeRangeTypeDef = TypedDict(
    "_OptionalTypedLinkAttributeRangeTypeDef", {"AttributeName": str}, total=False
)


class TypedLinkAttributeRangeTypeDef(
    _RequiredTypedLinkAttributeRangeTypeDef, _OptionalTypedLinkAttributeRangeTypeDef
):
    pass
