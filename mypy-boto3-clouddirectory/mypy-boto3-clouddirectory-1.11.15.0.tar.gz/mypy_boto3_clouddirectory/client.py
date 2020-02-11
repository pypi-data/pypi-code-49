"""
Main interface for clouddirectory service client

Usage::

    import boto3
    from mypy_boto3.clouddirectory import CloudDirectoryClient

    session = boto3.Session()

    client: CloudDirectoryClient = boto3.client("clouddirectory")
    session_client: CloudDirectoryClient = session.client("clouddirectory")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_clouddirectory.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_clouddirectory.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_clouddirectory.type_defs import (
    ClientAddFacetToObjectObjectAttributeListTypeDef,
    ClientAddFacetToObjectObjectReferenceTypeDef,
    ClientAddFacetToObjectSchemaFacetTypeDef,
    ClientApplySchemaResponseTypeDef,
    ClientAttachObjectChildReferenceTypeDef,
    ClientAttachObjectParentReferenceTypeDef,
    ClientAttachObjectResponseTypeDef,
    ClientAttachPolicyObjectReferenceTypeDef,
    ClientAttachPolicyPolicyReferenceTypeDef,
    ClientAttachToIndexIndexReferenceTypeDef,
    ClientAttachToIndexResponseTypeDef,
    ClientAttachToIndexTargetReferenceTypeDef,
    ClientAttachTypedLinkAttributesTypeDef,
    ClientAttachTypedLinkResponseTypeDef,
    ClientAttachTypedLinkSourceObjectReferenceTypeDef,
    ClientAttachTypedLinkTargetObjectReferenceTypeDef,
    ClientAttachTypedLinkTypedLinkFacetTypeDef,
    ClientBatchReadOperationsTypeDef,
    ClientBatchReadResponseTypeDef,
    ClientBatchWriteOperationsTypeDef,
    ClientBatchWriteResponseTypeDef,
    ClientCreateDirectoryResponseTypeDef,
    ClientCreateFacetAttributesTypeDef,
    ClientCreateIndexOrderedIndexedAttributeListTypeDef,
    ClientCreateIndexParentReferenceTypeDef,
    ClientCreateIndexResponseTypeDef,
    ClientCreateObjectObjectAttributeListTypeDef,
    ClientCreateObjectParentReferenceTypeDef,
    ClientCreateObjectResponseTypeDef,
    ClientCreateObjectSchemaFacetsTypeDef,
    ClientCreateSchemaResponseTypeDef,
    ClientCreateTypedLinkFacetFacetTypeDef,
    ClientDeleteDirectoryResponseTypeDef,
    ClientDeleteObjectObjectReferenceTypeDef,
    ClientDeleteSchemaResponseTypeDef,
    ClientDetachFromIndexIndexReferenceTypeDef,
    ClientDetachFromIndexResponseTypeDef,
    ClientDetachFromIndexTargetReferenceTypeDef,
    ClientDetachObjectParentReferenceTypeDef,
    ClientDetachObjectResponseTypeDef,
    ClientDetachPolicyObjectReferenceTypeDef,
    ClientDetachPolicyPolicyReferenceTypeDef,
    ClientDetachTypedLinkTypedLinkSpecifierTypeDef,
    ClientDisableDirectoryResponseTypeDef,
    ClientEnableDirectoryResponseTypeDef,
    ClientGetAppliedSchemaVersionResponseTypeDef,
    ClientGetDirectoryResponseTypeDef,
    ClientGetFacetResponseTypeDef,
    ClientGetLinkAttributesResponseTypeDef,
    ClientGetLinkAttributesTypedLinkSpecifierTypeDef,
    ClientGetObjectAttributesObjectReferenceTypeDef,
    ClientGetObjectAttributesResponseTypeDef,
    ClientGetObjectAttributesSchemaFacetTypeDef,
    ClientGetObjectInformationObjectReferenceTypeDef,
    ClientGetObjectInformationResponseTypeDef,
    ClientGetSchemaAsJsonResponseTypeDef,
    ClientGetTypedLinkFacetInformationResponseTypeDef,
    ClientListAppliedSchemaArnsResponseTypeDef,
    ClientListAttachedIndicesResponseTypeDef,
    ClientListAttachedIndicesTargetReferenceTypeDef,
    ClientListDevelopmentSchemaArnsResponseTypeDef,
    ClientListDirectoriesResponseTypeDef,
    ClientListFacetAttributesResponseTypeDef,
    ClientListFacetNamesResponseTypeDef,
    ClientListIncomingTypedLinksFilterAttributeRangesTypeDef,
    ClientListIncomingTypedLinksFilterTypedLinkTypeDef,
    ClientListIncomingTypedLinksObjectReferenceTypeDef,
    ClientListIncomingTypedLinksResponseTypeDef,
    ClientListIndexIndexReferenceTypeDef,
    ClientListIndexRangesOnIndexedValuesTypeDef,
    ClientListIndexResponseTypeDef,
    ClientListManagedSchemaArnsResponseTypeDef,
    ClientListObjectAttributesFacetFilterTypeDef,
    ClientListObjectAttributesObjectReferenceTypeDef,
    ClientListObjectAttributesResponseTypeDef,
    ClientListObjectChildrenObjectReferenceTypeDef,
    ClientListObjectChildrenResponseTypeDef,
    ClientListObjectParentPathsObjectReferenceTypeDef,
    ClientListObjectParentPathsResponseTypeDef,
    ClientListObjectParentsObjectReferenceTypeDef,
    ClientListObjectParentsResponseTypeDef,
    ClientListObjectPoliciesObjectReferenceTypeDef,
    ClientListObjectPoliciesResponseTypeDef,
    ClientListOutgoingTypedLinksFilterAttributeRangesTypeDef,
    ClientListOutgoingTypedLinksFilterTypedLinkTypeDef,
    ClientListOutgoingTypedLinksObjectReferenceTypeDef,
    ClientListOutgoingTypedLinksResponseTypeDef,
    ClientListPolicyAttachmentsPolicyReferenceTypeDef,
    ClientListPolicyAttachmentsResponseTypeDef,
    ClientListPublishedSchemaArnsResponseTypeDef,
    ClientListTagsForResourceResponseTypeDef,
    ClientListTypedLinkFacetAttributesResponseTypeDef,
    ClientListTypedLinkFacetNamesResponseTypeDef,
    ClientLookupPolicyObjectReferenceTypeDef,
    ClientLookupPolicyResponseTypeDef,
    ClientPublishSchemaResponseTypeDef,
    ClientPutSchemaFromJsonResponseTypeDef,
    ClientRemoveFacetFromObjectObjectReferenceTypeDef,
    ClientRemoveFacetFromObjectSchemaFacetTypeDef,
    ClientTagResourceTagsTypeDef,
    ClientUpdateFacetAttributeUpdatesTypeDef,
    ClientUpdateLinkAttributesAttributeUpdatesTypeDef,
    ClientUpdateLinkAttributesTypedLinkSpecifierTypeDef,
    ClientUpdateObjectAttributesAttributeUpdatesTypeDef,
    ClientUpdateObjectAttributesObjectReferenceTypeDef,
    ClientUpdateObjectAttributesResponseTypeDef,
    ClientUpdateSchemaResponseTypeDef,
    ClientUpdateTypedLinkFacetAttributeUpdatesTypeDef,
    ClientUpgradeAppliedSchemaResponseTypeDef,
    ClientUpgradePublishedSchemaResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("CloudDirectoryClient",)


class CloudDirectoryClient:
    """
    [CloudDirectory.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/clouddirectory.html#CloudDirectory.Client)
    """

    exceptions: "client_scope.Exceptions"

    def add_facet_to_object(
        self,
        DirectoryArn: str,
        SchemaFacet: ClientAddFacetToObjectSchemaFacetTypeDef,
        ObjectReference: ClientAddFacetToObjectObjectReferenceTypeDef,
        ObjectAttributeList: List[ClientAddFacetToObjectObjectAttributeListTypeDef] = None,
    ) -> Dict[str, Any]:
        """
        [Client.add_facet_to_object documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/clouddirectory.html#CloudDirectory.Client.add_facet_to_object)
        """

    def apply_schema(
        self, PublishedSchemaArn: str, DirectoryArn: str
    ) -> ClientApplySchemaResponseTypeDef:
        """
        [Client.apply_schema documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/clouddirectory.html#CloudDirectory.Client.apply_schema)
        """

    def attach_object(
        self,
        DirectoryArn: str,
        ParentReference: ClientAttachObjectParentReferenceTypeDef,
        ChildReference: ClientAttachObjectChildReferenceTypeDef,
        LinkName: str,
    ) -> ClientAttachObjectResponseTypeDef:
        """
        [Client.attach_object documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/clouddirectory.html#CloudDirectory.Client.attach_object)
        """

    def attach_policy(
        self,
        DirectoryArn: str,
        PolicyReference: ClientAttachPolicyPolicyReferenceTypeDef,
        ObjectReference: ClientAttachPolicyObjectReferenceTypeDef,
    ) -> Dict[str, Any]:
        """
        [Client.attach_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/clouddirectory.html#CloudDirectory.Client.attach_policy)
        """

    def attach_to_index(
        self,
        DirectoryArn: str,
        IndexReference: ClientAttachToIndexIndexReferenceTypeDef,
        TargetReference: ClientAttachToIndexTargetReferenceTypeDef,
    ) -> ClientAttachToIndexResponseTypeDef:
        """
        [Client.attach_to_index documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/clouddirectory.html#CloudDirectory.Client.attach_to_index)
        """

    def attach_typed_link(
        self,
        DirectoryArn: str,
        SourceObjectReference: ClientAttachTypedLinkSourceObjectReferenceTypeDef,
        TargetObjectReference: ClientAttachTypedLinkTargetObjectReferenceTypeDef,
        TypedLinkFacet: ClientAttachTypedLinkTypedLinkFacetTypeDef,
        Attributes: List[ClientAttachTypedLinkAttributesTypeDef],
    ) -> ClientAttachTypedLinkResponseTypeDef:
        """
        [Client.attach_typed_link documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/clouddirectory.html#CloudDirectory.Client.attach_typed_link)
        """

    def batch_read(
        self,
        DirectoryArn: str,
        Operations: List[ClientBatchReadOperationsTypeDef],
        ConsistencyLevel: Literal["SERIALIZABLE", "EVENTUAL"] = None,
    ) -> ClientBatchReadResponseTypeDef:
        """
        [Client.batch_read documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/clouddirectory.html#CloudDirectory.Client.batch_read)
        """

    def batch_write(
        self, DirectoryArn: str, Operations: List[ClientBatchWriteOperationsTypeDef]
    ) -> ClientBatchWriteResponseTypeDef:
        """
        [Client.batch_write documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/clouddirectory.html#CloudDirectory.Client.batch_write)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/clouddirectory.html#CloudDirectory.Client.can_paginate)
        """

    def create_directory(self, Name: str, SchemaArn: str) -> ClientCreateDirectoryResponseTypeDef:
        """
        [Client.create_directory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/clouddirectory.html#CloudDirectory.Client.create_directory)
        """

    def create_facet(
        self,
        SchemaArn: str,
        Name: str,
        Attributes: List[ClientCreateFacetAttributesTypeDef] = None,
        ObjectType: Literal["NODE", "LEAF_NODE", "POLICY", "INDEX"] = None,
        FacetStyle: Literal["STATIC", "DYNAMIC"] = None,
    ) -> Dict[str, Any]:
        """
        [Client.create_facet documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/clouddirectory.html#CloudDirectory.Client.create_facet)
        """

    def create_index(
        self,
        DirectoryArn: str,
        OrderedIndexedAttributeList: List[ClientCreateIndexOrderedIndexedAttributeListTypeDef],
        IsUnique: bool,
        ParentReference: ClientCreateIndexParentReferenceTypeDef = None,
        LinkName: str = None,
    ) -> ClientCreateIndexResponseTypeDef:
        """
        [Client.create_index documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/clouddirectory.html#CloudDirectory.Client.create_index)
        """

    def create_object(
        self,
        DirectoryArn: str,
        SchemaFacets: List[ClientCreateObjectSchemaFacetsTypeDef],
        ObjectAttributeList: List[ClientCreateObjectObjectAttributeListTypeDef] = None,
        ParentReference: ClientCreateObjectParentReferenceTypeDef = None,
        LinkName: str = None,
    ) -> ClientCreateObjectResponseTypeDef:
        """
        [Client.create_object documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/clouddirectory.html#CloudDirectory.Client.create_object)
        """

    def create_schema(self, Name: str) -> ClientCreateSchemaResponseTypeDef:
        """
        [Client.create_schema documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/clouddirectory.html#CloudDirectory.Client.create_schema)
        """

    def create_typed_link_facet(
        self, SchemaArn: str, Facet: ClientCreateTypedLinkFacetFacetTypeDef
    ) -> Dict[str, Any]:
        """
        [Client.create_typed_link_facet documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/clouddirectory.html#CloudDirectory.Client.create_typed_link_facet)
        """

    def delete_directory(self, DirectoryArn: str) -> ClientDeleteDirectoryResponseTypeDef:
        """
        [Client.delete_directory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/clouddirectory.html#CloudDirectory.Client.delete_directory)
        """

    def delete_facet(self, SchemaArn: str, Name: str) -> Dict[str, Any]:
        """
        [Client.delete_facet documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/clouddirectory.html#CloudDirectory.Client.delete_facet)
        """

    def delete_object(
        self, DirectoryArn: str, ObjectReference: ClientDeleteObjectObjectReferenceTypeDef
    ) -> Dict[str, Any]:
        """
        [Client.delete_object documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/clouddirectory.html#CloudDirectory.Client.delete_object)
        """

    def delete_schema(self, SchemaArn: str) -> ClientDeleteSchemaResponseTypeDef:
        """
        [Client.delete_schema documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/clouddirectory.html#CloudDirectory.Client.delete_schema)
        """

    def delete_typed_link_facet(self, SchemaArn: str, Name: str) -> Dict[str, Any]:
        """
        [Client.delete_typed_link_facet documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/clouddirectory.html#CloudDirectory.Client.delete_typed_link_facet)
        """

    def detach_from_index(
        self,
        DirectoryArn: str,
        IndexReference: ClientDetachFromIndexIndexReferenceTypeDef,
        TargetReference: ClientDetachFromIndexTargetReferenceTypeDef,
    ) -> ClientDetachFromIndexResponseTypeDef:
        """
        [Client.detach_from_index documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/clouddirectory.html#CloudDirectory.Client.detach_from_index)
        """

    def detach_object(
        self,
        DirectoryArn: str,
        ParentReference: ClientDetachObjectParentReferenceTypeDef,
        LinkName: str,
    ) -> ClientDetachObjectResponseTypeDef:
        """
        [Client.detach_object documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/clouddirectory.html#CloudDirectory.Client.detach_object)
        """

    def detach_policy(
        self,
        DirectoryArn: str,
        PolicyReference: ClientDetachPolicyPolicyReferenceTypeDef,
        ObjectReference: ClientDetachPolicyObjectReferenceTypeDef,
    ) -> Dict[str, Any]:
        """
        [Client.detach_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/clouddirectory.html#CloudDirectory.Client.detach_policy)
        """

    def detach_typed_link(
        self, DirectoryArn: str, TypedLinkSpecifier: ClientDetachTypedLinkTypedLinkSpecifierTypeDef
    ) -> None:
        """
        [Client.detach_typed_link documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/clouddirectory.html#CloudDirectory.Client.detach_typed_link)
        """

    def disable_directory(self, DirectoryArn: str) -> ClientDisableDirectoryResponseTypeDef:
        """
        [Client.disable_directory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/clouddirectory.html#CloudDirectory.Client.disable_directory)
        """

    def enable_directory(self, DirectoryArn: str) -> ClientEnableDirectoryResponseTypeDef:
        """
        [Client.enable_directory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/clouddirectory.html#CloudDirectory.Client.enable_directory)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/clouddirectory.html#CloudDirectory.Client.generate_presigned_url)
        """

    def get_applied_schema_version(
        self, SchemaArn: str
    ) -> ClientGetAppliedSchemaVersionResponseTypeDef:
        """
        [Client.get_applied_schema_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/clouddirectory.html#CloudDirectory.Client.get_applied_schema_version)
        """

    def get_directory(self, DirectoryArn: str) -> ClientGetDirectoryResponseTypeDef:
        """
        [Client.get_directory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/clouddirectory.html#CloudDirectory.Client.get_directory)
        """

    def get_facet(self, SchemaArn: str, Name: str) -> ClientGetFacetResponseTypeDef:
        """
        [Client.get_facet documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/clouddirectory.html#CloudDirectory.Client.get_facet)
        """

    def get_link_attributes(
        self,
        DirectoryArn: str,
        TypedLinkSpecifier: ClientGetLinkAttributesTypedLinkSpecifierTypeDef,
        AttributeNames: List[str],
        ConsistencyLevel: Literal["SERIALIZABLE", "EVENTUAL"] = None,
    ) -> ClientGetLinkAttributesResponseTypeDef:
        """
        [Client.get_link_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/clouddirectory.html#CloudDirectory.Client.get_link_attributes)
        """

    def get_object_attributes(
        self,
        DirectoryArn: str,
        ObjectReference: ClientGetObjectAttributesObjectReferenceTypeDef,
        SchemaFacet: ClientGetObjectAttributesSchemaFacetTypeDef,
        AttributeNames: List[str],
        ConsistencyLevel: Literal["SERIALIZABLE", "EVENTUAL"] = None,
    ) -> ClientGetObjectAttributesResponseTypeDef:
        """
        [Client.get_object_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/clouddirectory.html#CloudDirectory.Client.get_object_attributes)
        """

    def get_object_information(
        self,
        DirectoryArn: str,
        ObjectReference: ClientGetObjectInformationObjectReferenceTypeDef,
        ConsistencyLevel: Literal["SERIALIZABLE", "EVENTUAL"] = None,
    ) -> ClientGetObjectInformationResponseTypeDef:
        """
        [Client.get_object_information documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/clouddirectory.html#CloudDirectory.Client.get_object_information)
        """

    def get_schema_as_json(self, SchemaArn: str) -> ClientGetSchemaAsJsonResponseTypeDef:
        """
        [Client.get_schema_as_json documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/clouddirectory.html#CloudDirectory.Client.get_schema_as_json)
        """

    def get_typed_link_facet_information(
        self, SchemaArn: str, Name: str
    ) -> ClientGetTypedLinkFacetInformationResponseTypeDef:
        """
        [Client.get_typed_link_facet_information documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/clouddirectory.html#CloudDirectory.Client.get_typed_link_facet_information)
        """

    def list_applied_schema_arns(
        self,
        DirectoryArn: str,
        SchemaArn: str = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientListAppliedSchemaArnsResponseTypeDef:
        """
        [Client.list_applied_schema_arns documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/clouddirectory.html#CloudDirectory.Client.list_applied_schema_arns)
        """

    def list_attached_indices(
        self,
        DirectoryArn: str,
        TargetReference: ClientListAttachedIndicesTargetReferenceTypeDef,
        NextToken: str = None,
        MaxResults: int = None,
        ConsistencyLevel: Literal["SERIALIZABLE", "EVENTUAL"] = None,
    ) -> ClientListAttachedIndicesResponseTypeDef:
        """
        [Client.list_attached_indices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/clouddirectory.html#CloudDirectory.Client.list_attached_indices)
        """

    def list_development_schema_arns(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ClientListDevelopmentSchemaArnsResponseTypeDef:
        """
        [Client.list_development_schema_arns documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/clouddirectory.html#CloudDirectory.Client.list_development_schema_arns)
        """

    def list_directories(
        self,
        NextToken: str = None,
        MaxResults: int = None,
        state: Literal["ENABLED", "DISABLED", "DELETED"] = None,
    ) -> ClientListDirectoriesResponseTypeDef:
        """
        [Client.list_directories documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/clouddirectory.html#CloudDirectory.Client.list_directories)
        """

    def list_facet_attributes(
        self, SchemaArn: str, Name: str, NextToken: str = None, MaxResults: int = None
    ) -> ClientListFacetAttributesResponseTypeDef:
        """
        [Client.list_facet_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/clouddirectory.html#CloudDirectory.Client.list_facet_attributes)
        """

    def list_facet_names(
        self, SchemaArn: str, NextToken: str = None, MaxResults: int = None
    ) -> ClientListFacetNamesResponseTypeDef:
        """
        [Client.list_facet_names documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/clouddirectory.html#CloudDirectory.Client.list_facet_names)
        """

    def list_incoming_typed_links(
        self,
        DirectoryArn: str,
        ObjectReference: ClientListIncomingTypedLinksObjectReferenceTypeDef,
        FilterAttributeRanges: List[
            ClientListIncomingTypedLinksFilterAttributeRangesTypeDef
        ] = None,
        FilterTypedLink: ClientListIncomingTypedLinksFilterTypedLinkTypeDef = None,
        NextToken: str = None,
        MaxResults: int = None,
        ConsistencyLevel: Literal["SERIALIZABLE", "EVENTUAL"] = None,
    ) -> ClientListIncomingTypedLinksResponseTypeDef:
        """
        [Client.list_incoming_typed_links documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/clouddirectory.html#CloudDirectory.Client.list_incoming_typed_links)
        """

    def list_index(
        self,
        DirectoryArn: str,
        IndexReference: ClientListIndexIndexReferenceTypeDef,
        RangesOnIndexedValues: List[ClientListIndexRangesOnIndexedValuesTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
        ConsistencyLevel: Literal["SERIALIZABLE", "EVENTUAL"] = None,
    ) -> ClientListIndexResponseTypeDef:
        """
        [Client.list_index documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/clouddirectory.html#CloudDirectory.Client.list_index)
        """

    def list_managed_schema_arns(
        self, SchemaArn: str = None, NextToken: str = None, MaxResults: int = None
    ) -> ClientListManagedSchemaArnsResponseTypeDef:
        """
        [Client.list_managed_schema_arns documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/clouddirectory.html#CloudDirectory.Client.list_managed_schema_arns)
        """

    def list_object_attributes(
        self,
        DirectoryArn: str,
        ObjectReference: ClientListObjectAttributesObjectReferenceTypeDef,
        NextToken: str = None,
        MaxResults: int = None,
        ConsistencyLevel: Literal["SERIALIZABLE", "EVENTUAL"] = None,
        FacetFilter: ClientListObjectAttributesFacetFilterTypeDef = None,
    ) -> ClientListObjectAttributesResponseTypeDef:
        """
        [Client.list_object_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/clouddirectory.html#CloudDirectory.Client.list_object_attributes)
        """

    def list_object_children(
        self,
        DirectoryArn: str,
        ObjectReference: ClientListObjectChildrenObjectReferenceTypeDef,
        NextToken: str = None,
        MaxResults: int = None,
        ConsistencyLevel: Literal["SERIALIZABLE", "EVENTUAL"] = None,
    ) -> ClientListObjectChildrenResponseTypeDef:
        """
        [Client.list_object_children documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/clouddirectory.html#CloudDirectory.Client.list_object_children)
        """

    def list_object_parent_paths(
        self,
        DirectoryArn: str,
        ObjectReference: ClientListObjectParentPathsObjectReferenceTypeDef,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientListObjectParentPathsResponseTypeDef:
        """
        [Client.list_object_parent_paths documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/clouddirectory.html#CloudDirectory.Client.list_object_parent_paths)
        """

    def list_object_parents(
        self,
        DirectoryArn: str,
        ObjectReference: ClientListObjectParentsObjectReferenceTypeDef,
        NextToken: str = None,
        MaxResults: int = None,
        ConsistencyLevel: Literal["SERIALIZABLE", "EVENTUAL"] = None,
        IncludeAllLinksToEachParent: bool = None,
    ) -> ClientListObjectParentsResponseTypeDef:
        """
        [Client.list_object_parents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/clouddirectory.html#CloudDirectory.Client.list_object_parents)
        """

    def list_object_policies(
        self,
        DirectoryArn: str,
        ObjectReference: ClientListObjectPoliciesObjectReferenceTypeDef,
        NextToken: str = None,
        MaxResults: int = None,
        ConsistencyLevel: Literal["SERIALIZABLE", "EVENTUAL"] = None,
    ) -> ClientListObjectPoliciesResponseTypeDef:
        """
        [Client.list_object_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/clouddirectory.html#CloudDirectory.Client.list_object_policies)
        """

    def list_outgoing_typed_links(
        self,
        DirectoryArn: str,
        ObjectReference: ClientListOutgoingTypedLinksObjectReferenceTypeDef,
        FilterAttributeRanges: List[
            ClientListOutgoingTypedLinksFilterAttributeRangesTypeDef
        ] = None,
        FilterTypedLink: ClientListOutgoingTypedLinksFilterTypedLinkTypeDef = None,
        NextToken: str = None,
        MaxResults: int = None,
        ConsistencyLevel: Literal["SERIALIZABLE", "EVENTUAL"] = None,
    ) -> ClientListOutgoingTypedLinksResponseTypeDef:
        """
        [Client.list_outgoing_typed_links documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/clouddirectory.html#CloudDirectory.Client.list_outgoing_typed_links)
        """

    def list_policy_attachments(
        self,
        DirectoryArn: str,
        PolicyReference: ClientListPolicyAttachmentsPolicyReferenceTypeDef,
        NextToken: str = None,
        MaxResults: int = None,
        ConsistencyLevel: Literal["SERIALIZABLE", "EVENTUAL"] = None,
    ) -> ClientListPolicyAttachmentsResponseTypeDef:
        """
        [Client.list_policy_attachments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/clouddirectory.html#CloudDirectory.Client.list_policy_attachments)
        """

    def list_published_schema_arns(
        self, SchemaArn: str = None, NextToken: str = None, MaxResults: int = None
    ) -> ClientListPublishedSchemaArnsResponseTypeDef:
        """
        [Client.list_published_schema_arns documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/clouddirectory.html#CloudDirectory.Client.list_published_schema_arns)
        """

    def list_tags_for_resource(
        self, ResourceArn: str, NextToken: str = None, MaxResults: int = None
    ) -> ClientListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/clouddirectory.html#CloudDirectory.Client.list_tags_for_resource)
        """

    def list_typed_link_facet_attributes(
        self, SchemaArn: str, Name: str, NextToken: str = None, MaxResults: int = None
    ) -> ClientListTypedLinkFacetAttributesResponseTypeDef:
        """
        [Client.list_typed_link_facet_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/clouddirectory.html#CloudDirectory.Client.list_typed_link_facet_attributes)
        """

    def list_typed_link_facet_names(
        self, SchemaArn: str, NextToken: str = None, MaxResults: int = None
    ) -> ClientListTypedLinkFacetNamesResponseTypeDef:
        """
        [Client.list_typed_link_facet_names documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/clouddirectory.html#CloudDirectory.Client.list_typed_link_facet_names)
        """

    def lookup_policy(
        self,
        DirectoryArn: str,
        ObjectReference: ClientLookupPolicyObjectReferenceTypeDef,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientLookupPolicyResponseTypeDef:
        """
        [Client.lookup_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/clouddirectory.html#CloudDirectory.Client.lookup_policy)
        """

    def publish_schema(
        self, DevelopmentSchemaArn: str, Version: str, MinorVersion: str = None, Name: str = None
    ) -> ClientPublishSchemaResponseTypeDef:
        """
        [Client.publish_schema documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/clouddirectory.html#CloudDirectory.Client.publish_schema)
        """

    def put_schema_from_json(
        self, SchemaArn: str, Document: str
    ) -> ClientPutSchemaFromJsonResponseTypeDef:
        """
        [Client.put_schema_from_json documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/clouddirectory.html#CloudDirectory.Client.put_schema_from_json)
        """

    def remove_facet_from_object(
        self,
        DirectoryArn: str,
        SchemaFacet: ClientRemoveFacetFromObjectSchemaFacetTypeDef,
        ObjectReference: ClientRemoveFacetFromObjectObjectReferenceTypeDef,
    ) -> Dict[str, Any]:
        """
        [Client.remove_facet_from_object documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/clouddirectory.html#CloudDirectory.Client.remove_facet_from_object)
        """

    def tag_resource(
        self, ResourceArn: str, Tags: List[ClientTagResourceTagsTypeDef]
    ) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/clouddirectory.html#CloudDirectory.Client.tag_resource)
        """

    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/clouddirectory.html#CloudDirectory.Client.untag_resource)
        """

    def update_facet(
        self,
        SchemaArn: str,
        Name: str,
        AttributeUpdates: List[ClientUpdateFacetAttributeUpdatesTypeDef] = None,
        ObjectType: Literal["NODE", "LEAF_NODE", "POLICY", "INDEX"] = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_facet documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/clouddirectory.html#CloudDirectory.Client.update_facet)
        """

    def update_link_attributes(
        self,
        DirectoryArn: str,
        TypedLinkSpecifier: ClientUpdateLinkAttributesTypedLinkSpecifierTypeDef,
        AttributeUpdates: List[ClientUpdateLinkAttributesAttributeUpdatesTypeDef],
    ) -> Dict[str, Any]:
        """
        [Client.update_link_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/clouddirectory.html#CloudDirectory.Client.update_link_attributes)
        """

    def update_object_attributes(
        self,
        DirectoryArn: str,
        ObjectReference: ClientUpdateObjectAttributesObjectReferenceTypeDef,
        AttributeUpdates: List[ClientUpdateObjectAttributesAttributeUpdatesTypeDef],
    ) -> ClientUpdateObjectAttributesResponseTypeDef:
        """
        [Client.update_object_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/clouddirectory.html#CloudDirectory.Client.update_object_attributes)
        """

    def update_schema(self, SchemaArn: str, Name: str) -> ClientUpdateSchemaResponseTypeDef:
        """
        [Client.update_schema documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/clouddirectory.html#CloudDirectory.Client.update_schema)
        """

    def update_typed_link_facet(
        self,
        SchemaArn: str,
        Name: str,
        AttributeUpdates: List[ClientUpdateTypedLinkFacetAttributeUpdatesTypeDef],
        IdentityAttributeOrder: List[str],
    ) -> Dict[str, Any]:
        """
        [Client.update_typed_link_facet documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/clouddirectory.html#CloudDirectory.Client.update_typed_link_facet)
        """

    def upgrade_applied_schema(
        self, PublishedSchemaArn: str, DirectoryArn: str, DryRun: bool = None
    ) -> ClientUpgradeAppliedSchemaResponseTypeDef:
        """
        [Client.upgrade_applied_schema documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/clouddirectory.html#CloudDirectory.Client.upgrade_applied_schema)
        """

    def upgrade_published_schema(
        self,
        DevelopmentSchemaArn: str,
        PublishedSchemaArn: str,
        MinorVersion: str,
        DryRun: bool = None,
    ) -> ClientUpgradePublishedSchemaResponseTypeDef:
        """
        [Client.upgrade_published_schema documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/clouddirectory.html#CloudDirectory.Client.upgrade_published_schema)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_applied_schema_arns"]
    ) -> "paginator_scope.ListAppliedSchemaArnsPaginator":
        """
        [Paginator.ListAppliedSchemaArns documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListAppliedSchemaArns)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_attached_indices"]
    ) -> "paginator_scope.ListAttachedIndicesPaginator":
        """
        [Paginator.ListAttachedIndices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListAttachedIndices)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_development_schema_arns"]
    ) -> "paginator_scope.ListDevelopmentSchemaArnsPaginator":
        """
        [Paginator.ListDevelopmentSchemaArns documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListDevelopmentSchemaArns)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_directories"]
    ) -> "paginator_scope.ListDirectoriesPaginator":
        """
        [Paginator.ListDirectories documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListDirectories)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_facet_attributes"]
    ) -> "paginator_scope.ListFacetAttributesPaginator":
        """
        [Paginator.ListFacetAttributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListFacetAttributes)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_facet_names"]
    ) -> "paginator_scope.ListFacetNamesPaginator":
        """
        [Paginator.ListFacetNames documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListFacetNames)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_incoming_typed_links"]
    ) -> "paginator_scope.ListIncomingTypedLinksPaginator":
        """
        [Paginator.ListIncomingTypedLinks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListIncomingTypedLinks)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_index"]
    ) -> "paginator_scope.ListIndexPaginator":
        """
        [Paginator.ListIndex documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListIndex)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_managed_schema_arns"]
    ) -> "paginator_scope.ListManagedSchemaArnsPaginator":
        """
        [Paginator.ListManagedSchemaArns documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListManagedSchemaArns)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_object_attributes"]
    ) -> "paginator_scope.ListObjectAttributesPaginator":
        """
        [Paginator.ListObjectAttributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListObjectAttributes)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_object_parent_paths"]
    ) -> "paginator_scope.ListObjectParentPathsPaginator":
        """
        [Paginator.ListObjectParentPaths documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListObjectParentPaths)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_object_policies"]
    ) -> "paginator_scope.ListObjectPoliciesPaginator":
        """
        [Paginator.ListObjectPolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListObjectPolicies)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_outgoing_typed_links"]
    ) -> "paginator_scope.ListOutgoingTypedLinksPaginator":
        """
        [Paginator.ListOutgoingTypedLinks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListOutgoingTypedLinks)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_policy_attachments"]
    ) -> "paginator_scope.ListPolicyAttachmentsPaginator":
        """
        [Paginator.ListPolicyAttachments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListPolicyAttachments)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_published_schema_arns"]
    ) -> "paginator_scope.ListPublishedSchemaArnsPaginator":
        """
        [Paginator.ListPublishedSchemaArns documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListPublishedSchemaArns)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_tags_for_resource"]
    ) -> "paginator_scope.ListTagsForResourcePaginator":
        """
        [Paginator.ListTagsForResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListTagsForResource)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_typed_link_facet_attributes"]
    ) -> "paginator_scope.ListTypedLinkFacetAttributesPaginator":
        """
        [Paginator.ListTypedLinkFacetAttributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListTypedLinkFacetAttributes)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_typed_link_facet_names"]
    ) -> "paginator_scope.ListTypedLinkFacetNamesPaginator":
        """
        [Paginator.ListTypedLinkFacetNames documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListTypedLinkFacetNames)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["lookup_policy"]
    ) -> "paginator_scope.LookupPolicyPaginator":
        """
        [Paginator.LookupPolicy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/clouddirectory.html#CloudDirectory.Paginator.LookupPolicy)
        """


class Exceptions:
    AccessDeniedException: Boto3ClientError
    BatchWriteException: Boto3ClientError
    CannotListParentOfRootException: Boto3ClientError
    ClientError: Boto3ClientError
    DirectoryAlreadyExistsException: Boto3ClientError
    DirectoryDeletedException: Boto3ClientError
    DirectoryNotDisabledException: Boto3ClientError
    DirectoryNotEnabledException: Boto3ClientError
    FacetAlreadyExistsException: Boto3ClientError
    FacetInUseException: Boto3ClientError
    FacetNotFoundException: Boto3ClientError
    FacetValidationException: Boto3ClientError
    IncompatibleSchemaException: Boto3ClientError
    IndexedAttributeMissingException: Boto3ClientError
    InternalServiceException: Boto3ClientError
    InvalidArnException: Boto3ClientError
    InvalidAttachmentException: Boto3ClientError
    InvalidFacetUpdateException: Boto3ClientError
    InvalidNextTokenException: Boto3ClientError
    InvalidRuleException: Boto3ClientError
    InvalidSchemaDocException: Boto3ClientError
    InvalidTaggingRequestException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    LinkNameAlreadyInUseException: Boto3ClientError
    NotIndexException: Boto3ClientError
    NotNodeException: Boto3ClientError
    NotPolicyException: Boto3ClientError
    ObjectAlreadyDetachedException: Boto3ClientError
    ObjectNotDetachedException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    RetryableConflictException: Boto3ClientError
    SchemaAlreadyExistsException: Boto3ClientError
    SchemaAlreadyPublishedException: Boto3ClientError
    StillContainsLinksException: Boto3ClientError
    UnsupportedIndexTypeException: Boto3ClientError
    ValidationException: Boto3ClientError
