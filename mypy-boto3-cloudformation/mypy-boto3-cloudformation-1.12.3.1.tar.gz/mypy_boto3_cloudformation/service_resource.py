"""
Main interface for cloudformation service ServiceResource

Usage::

    import boto3
    from mypy_boto3.cloudformation import CloudFormationServiceResource
    import mypy_boto3.cloudformation.service_resource as cloudformation_resources

    resource: CloudFormationServiceResource = boto3.resource("cloudformation")
    session_resource: CloudFormationServiceResource = session.resource("cloudformation")

    Event: cloudformation_resources.Event = resource.Event(...)
    ...
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from datetime import datetime
import sys
from typing import Any, Dict, List, TYPE_CHECKING, Type, TypeVar
from boto3.resources.base import ServiceResource as Boto3ServiceResource
from boto3.resources.collection import ResourceCollection
from mypy_boto3_cloudformation.type_defs import (
    CreateStackOutputTypeDef,
    ParameterTypeDef,
    RollbackConfigurationTypeDef,
    TagTypeDef,
    UpdateStackOutputTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "CloudFormationServiceResource",
    "Event",
    "Stack",
    "StackResource",
    "StackResourceSummary",
    "ServiceResourceStacksCollection",
    "StackEventsCollection",
    "StackResourceSummariesCollection",
)

_ServiceResourceStacksCollectionType = TypeVar(
    "_ServiceResourceStacksCollectionType", bound="ServiceResourceStacksCollection"
)


class ServiceResourceStacksCollection(ResourceCollection):
    """
    [ServiceResource.stacks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.3/reference/services/cloudformation.html#CloudFormation.ServiceResource.stacks)
    """

    @classmethod
    def all(
        cls: Type[_ServiceResourceStacksCollectionType],
    ) -> Type[_ServiceResourceStacksCollectionType]:
        pass

    @classmethod
    def filter(
        cls: Type[_ServiceResourceStacksCollectionType],
        StackName: str = None,
        NextToken: str = None,
    ) -> Type[_ServiceResourceStacksCollectionType]:
        pass

    @classmethod
    def limit(
        cls: Type[_ServiceResourceStacksCollectionType], count: int
    ) -> Type[_ServiceResourceStacksCollectionType]:
        pass

    @classmethod
    def page_size(
        cls: Type[_ServiceResourceStacksCollectionType], count: int
    ) -> Type[_ServiceResourceStacksCollectionType]:
        pass

    @classmethod
    def pages(cls: Type[_ServiceResourceStacksCollectionType]) -> List["Stack"]:
        pass


_StackEventsCollectionType = TypeVar("_StackEventsCollectionType", bound="StackEventsCollection")


class StackEventsCollection(ResourceCollection):
    """
    [Stack.events documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.3/reference/services/cloudformation.html#CloudFormation.Stack.events)
    """

    @classmethod
    def all(cls: Type[_StackEventsCollectionType]) -> Type[_StackEventsCollectionType]:
        pass

    @classmethod
    def filter(
        cls: Type[_StackEventsCollectionType], StackName: str = None, NextToken: str = None
    ) -> Type[_StackEventsCollectionType]:
        pass

    @classmethod
    def limit(
        cls: Type[_StackEventsCollectionType], count: int
    ) -> Type[_StackEventsCollectionType]:
        pass

    @classmethod
    def page_size(
        cls: Type[_StackEventsCollectionType], count: int
    ) -> Type[_StackEventsCollectionType]:
        pass

    @classmethod
    def pages(cls: Type[_StackEventsCollectionType]) -> List["Event"]:
        pass


_StackResourceSummariesCollectionType = TypeVar(
    "_StackResourceSummariesCollectionType", bound="StackResourceSummariesCollection"
)


class StackResourceSummariesCollection(ResourceCollection):
    """
    [Stack.resource_summaries documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.3/reference/services/cloudformation.html#CloudFormation.Stack.resource_summaries)
    """

    @classmethod
    def all(
        cls: Type[_StackResourceSummariesCollectionType],
    ) -> Type[_StackResourceSummariesCollectionType]:
        pass

    @classmethod
    def filter(
        cls: Type[_StackResourceSummariesCollectionType], NextToken: str = None
    ) -> Type[_StackResourceSummariesCollectionType]:
        pass

    @classmethod
    def limit(
        cls: Type[_StackResourceSummariesCollectionType], count: int
    ) -> Type[_StackResourceSummariesCollectionType]:
        pass

    @classmethod
    def page_size(
        cls: Type[_StackResourceSummariesCollectionType], count: int
    ) -> Type[_StackResourceSummariesCollectionType]:
        pass

    @classmethod
    def pages(cls: Type[_StackResourceSummariesCollectionType]) -> List["StackResourceSummary"]:
        pass


_EventType = TypeVar("_EventType", bound="Event")


class Event(Boto3ServiceResource):
    """
    [Event documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.3/reference/services/cloudformation.html#CloudFormation.ServiceResource.Event)
    """

    stack_id: str
    event_id: str
    stack_name: str
    logical_resource_id: str
    physical_resource_id: str
    resource_type: str
    timestamp: datetime
    resource_status: str
    resource_status_reason: str
    resource_properties: str
    client_request_token: str
    id: str

    def get_available_subresources(self) -> List[str]:
        """
        [Event.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.3/reference/services/cloudformation.html#CloudFormation.Event.get_available_subresources)
        """


_Event = Event


_StackResourceType = TypeVar("_StackResourceType", bound="StackResource")


class StackResource(Boto3ServiceResource):
    """
    [StackResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.3/reference/services/cloudformation.html#CloudFormation.ServiceResource.StackResource)
    """

    stack_id: str
    logical_resource_id: str
    physical_resource_id: str
    resource_type: str
    last_updated_timestamp: datetime
    resource_status: str
    resource_status_reason: str
    description: str
    metadata: str
    drift_information: Dict[str, Any]
    stack_name: str
    logical_id: str

    def get_available_subresources(self) -> List[str]:
        """
        [StackResource.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.3/reference/services/cloudformation.html#CloudFormation.StackResource.get_available_subresources)
        """

    def load(self) -> None:
        """
        [StackResource.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.3/reference/services/cloudformation.html#CloudFormation.StackResource.load)
        """

    def reload(self) -> None:
        """
        [StackResource.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.3/reference/services/cloudformation.html#CloudFormation.StackResource.reload)
        """


_StackResource = StackResource


_StackResourceSummaryType = TypeVar("_StackResourceSummaryType", bound="StackResourceSummary")


class StackResourceSummary(Boto3ServiceResource):
    """
    [StackResourceSummary documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.3/reference/services/cloudformation.html#CloudFormation.ServiceResource.StackResourceSummary)
    """

    logical_resource_id: str
    physical_resource_id: str
    resource_type: str
    last_updated_timestamp: datetime
    resource_status: str
    resource_status_reason: str
    drift_information: Dict[str, Any]
    stack_name: str
    logical_id: str

    def get_available_subresources(self) -> List[str]:
        """
        [StackResourceSummary.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.3/reference/services/cloudformation.html#CloudFormation.StackResourceSummary.get_available_subresources)
        """


_StackResourceSummary = StackResourceSummary


_StackType = TypeVar("_StackType", bound="Stack")


class Stack(Boto3ServiceResource):
    """
    [Stack documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.3/reference/services/cloudformation.html#CloudFormation.ServiceResource.Stack)
    """

    stack_id: str
    stack_name: str
    change_set_id: str
    description: str
    parameters: List[Any]
    creation_time: datetime
    deletion_time: datetime
    last_updated_time: datetime
    rollback_configuration: Dict[str, Any]
    stack_status: str
    stack_status_reason: str
    disable_rollback: bool
    notification_arns: List[Any]
    timeout_in_minutes: int
    capabilities: List[Any]
    outputs: List[Any]
    role_arn: str
    tags: List[Any]
    enable_termination_protection: bool
    parent_id: str
    root_id: str
    drift_information: Dict[str, Any]
    name: str
    events: StackEventsCollection
    resource_summaries: StackResourceSummariesCollection

    def cancel_update(self, ClientRequestToken: str = None) -> None:
        """
        [Stack.cancel_update documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.3/reference/services/cloudformation.html#CloudFormation.Stack.cancel_update)
        """

    def delete(
        self, RetainResources: List[str] = None, RoleARN: str = None, ClientRequestToken: str = None
    ) -> None:
        """
        [Stack.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.3/reference/services/cloudformation.html#CloudFormation.Stack.delete)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Stack.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.3/reference/services/cloudformation.html#CloudFormation.Stack.get_available_subresources)
        """

    def load(self) -> None:
        """
        [Stack.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.3/reference/services/cloudformation.html#CloudFormation.Stack.load)
        """

    def reload(self) -> None:
        """
        [Stack.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.3/reference/services/cloudformation.html#CloudFormation.Stack.reload)
        """

    def update(
        self,
        TemplateBody: str = None,
        TemplateURL: str = None,
        UsePreviousTemplate: bool = None,
        StackPolicyDuringUpdateBody: str = None,
        StackPolicyDuringUpdateURL: str = None,
        Parameters: List[ParameterTypeDef] = None,
        Capabilities: List[
            Literal["CAPABILITY_IAM", "CAPABILITY_NAMED_IAM", "CAPABILITY_AUTO_EXPAND"]
        ] = None,
        ResourceTypes: List[str] = None,
        RoleARN: str = None,
        RollbackConfiguration: RollbackConfigurationTypeDef = None,
        StackPolicyBody: str = None,
        StackPolicyURL: str = None,
        NotificationARNs: List[str] = None,
        Tags: List[TagTypeDef] = None,
        ClientRequestToken: str = None,
    ) -> UpdateStackOutputTypeDef:
        """
        [Stack.update documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.3/reference/services/cloudformation.html#CloudFormation.Stack.update)
        """


_Stack = Stack


class CloudFormationServiceResource(Boto3ServiceResource):
    """
    [CloudFormation.ServiceResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.3/reference/services/cloudformation.html#CloudFormation.ServiceResource)
    """

    stacks: ServiceResourceStacksCollection

    def Event(self, id: str) -> _Event:
        """
        [ServiceResource.Event documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.3/reference/services/cloudformation.html#CloudFormation.ServiceResource.Event)
        """

    def Stack(self, name: str) -> _Stack:
        """
        [ServiceResource.Stack documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.3/reference/services/cloudformation.html#CloudFormation.ServiceResource.Stack)
        """

    def StackResource(self, stack_name: str, logical_id: str) -> _StackResource:
        """
        [ServiceResource.StackResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.3/reference/services/cloudformation.html#CloudFormation.ServiceResource.StackResource)
        """

    def StackResourceSummary(self, stack_name: str, logical_id: str) -> _StackResourceSummary:
        """
        [ServiceResource.StackResourceSummary documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.3/reference/services/cloudformation.html#CloudFormation.ServiceResource.StackResourceSummary)
        """

    def create_stack(
        self,
        StackName: str,
        TemplateBody: str = None,
        TemplateURL: str = None,
        Parameters: List[ParameterTypeDef] = None,
        DisableRollback: bool = None,
        RollbackConfiguration: RollbackConfigurationTypeDef = None,
        TimeoutInMinutes: int = None,
        NotificationARNs: List[str] = None,
        Capabilities: List[
            Literal["CAPABILITY_IAM", "CAPABILITY_NAMED_IAM", "CAPABILITY_AUTO_EXPAND"]
        ] = None,
        ResourceTypes: List[str] = None,
        RoleARN: str = None,
        OnFailure: Literal["DO_NOTHING", "ROLLBACK", "DELETE"] = None,
        StackPolicyBody: str = None,
        StackPolicyURL: str = None,
        Tags: List[TagTypeDef] = None,
        ClientRequestToken: str = None,
        EnableTerminationProtection: bool = None,
    ) -> CreateStackOutputTypeDef:
        """
        [ServiceResource.create_stack documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.3/reference/services/cloudformation.html#CloudFormation.ServiceResource.create_stack)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [ServiceResource.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.3/reference/services/cloudformation.html#CloudFormation.ServiceResource.get_available_subresources)
        """
