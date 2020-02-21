"""
Copyright 2019 Cognitive Scale, Inc. All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from typing import Optional

from attr import attrs

from cortex_common.constants import CONTEXTS, DESCRIPTIONS as DESC
from cortex_common.utils import describableAttrib, describableStrAttrib, dict_to_attr_class, BaseAttrClass, \
    time_converter, unique_id, utc_timestamp

from cortex_common.utils import attr_class_to_dict

__all__ = [
    'ProfileLink',
    'EventSource',
    'EntityEvent',
    'EntityRelationshipEvent',
    'ProfileRelationshipEvent',
]


@attrs(frozen=True)
class ProfileLink(object):
    """
    A pointer that links attributes in a profiles to specific attribute.
    """
    profileId = describableAttrib(type=str, description="What is the id of the profile that was linked?")
    schemaId = describableAttrib(type=str, description="What schema does the linked profile adhere to?")
    profileVersion = describableAttrib(type=Optional[int], default=None, description="Was a specific version of the profile linked?")
    context = describableAttrib(type=str, default=CONTEXTS.PROFILE_LINK, description=DESC.CONTEXT)


@attrs(frozen=True)
class EventSource(object):
    """
    Representing the source of an Entity Event ...
    """
    title = describableAttrib(type=str)
    description = describableAttrib(type=Optional[str])
    rights = describableAttrib(type=Optional[str])
    category = describableAttrib(type=Optional[str])
    sector = describableAttrib(type=Optional[str])
    region = describableAttrib(type=Optional[str])
    creator = describableAttrib(type=Optional[str])
    publisher = describableAttrib(type=Optional[str])
    language = describableAttrib(type=Optional[str])
    url = describableAttrib(type=Optional[str])


@attrs(frozen=True)
class BaseEntityEvent(BaseAttrClass):
    """
    Representing an Event that Modifies a representation of an Entity.
    """
    event = describableStrAttrib(description="What is the name of the event?")
    entityId = describableStrAttrib(description="Does this event relate an entity to another entity?")
    entityType = describableStrAttrib(description="What is the type of the entity?")


@attrs(frozen=True)
class BaseEntityRelationshipEvent(BaseEntityEvent):
    """
    Representing an Event that Modifies a representation of an Entity.
    """
    targetEntityId = describableStrAttrib(description="Does this event relate an entity to another entity?")
    targetEntityType = describableStrAttrib(description="What is the type of entity this event relates to?")


@attrs(frozen=True)
class BaseProfileRelationshipEvent(BaseEntityRelationshipEvent):
    """
    Representing an Event that Modifies a representation of an Entity.
    """
    targetLink = describableAttrib(
        type=ProfileLink,
        converter=lambda x: dict_to_attr_class(x, ProfileLink),
        description="What profiles does this relationship target?"
    )


@attrs(frozen=True)
class RemainingEventProperties(object):
    """
    Representing an Event that Modifies a representation of an Entity.
    """
    properties = describableAttrib(type=dict, factory=dict, description="What are the properties associated with this event?")
    meta = describableAttrib(type=dict, factory=dict, description="What is custom metadata associated with this event?")
    eventLabel = describableAttrib(type=Optional[str], default=None, description="What is the name of the event?")
    eventTime = describableAttrib(
        type=Optional[int],
        factory=utc_timestamp,  # The timestamp used in node is 1k times the arrow timestamp.
        converter=time_converter,
        description="When did the event occur?"
    )
    source = describableAttrib(
        type=Optional[EventSource],
        default=None,  # The timestamp used in node is 1k times the arrow timestamp.
        converter=lambda x: dict_to_attr_class(x, EventSource),
        description="What is the name of the event?"
    )
    # TODO ... add these to JS?
    eventId = describableAttrib(type=Optional[str], factory=unique_id, skip_when_serializing=True, description="What is id for this event?")
    triggerId = describableAttrib(type=Optional[str], factory=unique_id, skip_when_serializing=True, description="What is id of the occurrence that triggered this event?")


# Mixins work with Attrs ... do they work with other data representation packages?

@attrs(frozen=True)
class EntityEvent(BaseEntityEvent, RemainingEventProperties):
    """
    Base Entity Event
    """

    def __iter__(self):
        return iter(attr_class_to_dict(self, hide_internal_attributes=True).items())


@attrs(frozen=True)
class EntityRelationshipEvent(BaseEntityRelationshipEvent, RemainingEventProperties):
    """
    Entity Event with a relationship to another target entity
    """
    pass


@attrs(frozen=True)
class ProfileRelationshipEvent(BaseProfileRelationshipEvent, RemainingEventProperties):
    """
    Profile Event with a relationship to another target profile
    """
    pass


if __name__ == '__main__':
    from typing import Iterator, Tuple, cast, Dict
    ee = cast(Iterator[Tuple[str,str]], [['event', 'entityId', 'entityType']]*2)
    er = cast(Iterator[Tuple[str, str]], [['event', 'entityId', 'entityType', 'targetEntityId', 'targetEntityType']] * 2)
    ee_args: Dict[str,str] = dict(zip(*ee))  # type: ignore
    er_args: Dict[str,str] = dict(zip(*er))  # type: ignore
    print(ee_args, er_args)
    print(EntityEvent(**ee_args))  # type: ignore
    print(EntityRelationshipEvent(**er_args))  # type: ignore