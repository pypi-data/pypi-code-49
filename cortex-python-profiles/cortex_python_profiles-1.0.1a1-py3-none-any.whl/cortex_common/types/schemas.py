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

from functools import reduce
from typing import List, Optional, Union, cast

from attr import attrs, evolve, asdict, fields_dict

from cortex_common.constants import SCHEMA_CONTEXTS, DESCRIPTIONS, CAMEL
from cortex_common.utils import unique_id, utc_timestamp, describableAttrib, dicts_to_classes, attr_class_to_dict, \
    dict_to_attr_class, equal, hasher, merge_unique_objects_on

__all__ = [
    'value_type_converter',
    'ProfileValueTypeSummary',
    'ProfileTagSchema',
    'ProfileFacetSchema',
    'ProfileAttributeSchema',
    'ProfileTaxonomySchema',
    'ProfileSchema',
]


# [] TODO ... make sure _layout is gettable. ...

def attr_hasher(instance):
    """
    Hashes an attr class ...
    :param instance:
    :return:
    """
    return hasher(asdict(instance))


def value_type_converter(value_types:List[Union[dict, 'ProfileValueTypeSummary']]) -> List['ProfileValueTypeSummary']:
    """
    Recursively converts dicts `ProfileValueTypeSummary` into the python class!
    :param valueType:
    :return:
    """
    return [
        ProfileValueTypeSummary(  # type: ignore # ignore until mypy properyly supports attr ...
            outerType=value_type["outerType"] if isinstance(value_type, dict) else value_type.outerType,
            innerTypes=value_type_converter(value_type.get("innerTypes", []) if isinstance(value_type, dict) else value_type.innerTypes,)
        )
        for value_type in value_types
    ]


@attrs(frozen=True)
class ProfileValueTypeSummary(object):
    """
    Represents the type of a value an attribute can hold
    """
    outerType = describableAttrib(type=str, description="What is the primary type of an attribute's value?")
    innerTypes = describableAttrib(
        type=List['ProfileValueTypeSummary'], converter=value_type_converter,
        factory=list, description="What are the inner types of an attribute's value?"
    )

    def __eq__(self, other:object):
        if not isinstance(other, ProfileValueTypeSummary):
            raise NotImplementedError("Cannot add {} and {} types.".format(ProfileValueTypeSummary.__name__, type(other).__name__))
        return (
                (self.outerType == other.outerType)
            and equal(self.innerTypes, other.innerTypes)
        )


@attrs(frozen=True)
class ProfileTagSchema(object):
    """
    Represents a Tag that attributes in a ProfileSchema can be tagged with.
    """
    name = describableAttrib(type=str, description=DESCRIPTIONS.NAME)
    label = describableAttrib(type=str, description=DESCRIPTIONS.LABEL)
    description = describableAttrib(type=Optional[str], default="", description=DESCRIPTIONS.DESCRIPTION)
    id = describableAttrib(type=Optional[str], default=None, description=DESCRIPTIONS.ID)
    group = describableAttrib(type=Optional[str], default=None, skip_when_serializing=True, description="What Facet Group does this tag belong?")
    context = describableAttrib(type=str, default=SCHEMA_CONTEXTS.PROFILE_ATTRIBUTE_TAG,
        description="What is the type of this piece of data?")


@attrs(frozen=True)
class ProfileFacetSchema(object):
    """
    Represents a group of tags that can be collectively used as search facets when looking for attributes.
    Previously known as ProfileGroupSchema
    """
    name = describableAttrib(type=str, description=DESCRIPTIONS.NAME)
    label = describableAttrib(type=str, description=DESCRIPTIONS.LABEL)
    description = describableAttrib(type=Optional[str], default="", description=DESCRIPTIONS.DESCRIPTION)
    tags = describableAttrib(type=List[str], factory=list, description="What are the id's of all the tags that apply to this group?")
    id = describableAttrib(type=Optional[str], default=None, description=DESCRIPTIONS.ID)
    context = describableAttrib(type=str, default=SCHEMA_CONTEXTS.PROFILE_ATTRIBUTE_FACET,
        description="What is the type of this piece of data?")

    def __add__(self, other) -> 'ProfileFacetSchema':
        """
        Adding two facet groups together should effectively add their tags ...
        :param other:
        :return:
        """

        if not other:
            return self

        if not isinstance(other, ProfileFacetSchema):
            raise NotImplementedError("Cannot add {} and {} types.".format(ProfileFacetSchema.__name__, type(other).__name__))

        # Cant add ... if group ids are not the same ...
        if not self.name == other.name:
            raise NotImplementedError("Can not add facet groups with different ids.")

        unique_tags = list(set(self.tags + cast(ProfileFacetSchema, other).tags))  # type: ignore
        return evolve(self, tags=unique_tags)


@attrs(frozen=True, cmp=False, hash=False)
class ProfileAttributeSchema(object):
    """
    Represents the structural expectation of a single attribute in the profile.
    """
    name = describableAttrib(type=str, description=DESCRIPTIONS.NAME)
    type = describableAttrib(type=str, description="What is the type of the profile attribute?")
    valueType = describableAttrib(
        type=ProfileValueTypeSummary,
        converter=lambda d: dict_to_attr_class(d, ProfileValueTypeSummary),
        description="What is the type of the profile attribute?"
    )
    label = describableAttrib(type=str, description=DESCRIPTIONS.LABEL)
    description = describableAttrib(type=Optional[str], default="", description=DESCRIPTIONS.DESCRIPTION)
    questions = describableAttrib(type=Optional[List[str]], factory=list, description="What questions is this attribute capable of answering?")
    tags = describableAttrib(type=Optional[List[str]], factory=list, description="What are the id's of all the tags that apply to this attribute?")

    __hash__ =  attr_hasher

    # Need this to be able to be able to make a Set[ProfileAttributeSchema] !
    def __eq__(self, other):
        fields = fields_dict(ProfileAttributeSchema).keys()
        return all([equal(getattr(self, x), getattr(other, x)) for x in fields])


@attrs(frozen=True)
class ProfileTaxonomySchema(object):
    """
    Represents a hierarchical grouping of attributes.
    Previously known as `ProfileHierarchySchema`
    """
    name = describableAttrib(type=str, description=DESCRIPTIONS.NAME)
    label = describableAttrib(type=str, description=DESCRIPTIONS.LABEL)
    description = describableAttrib(type=str, description=DESCRIPTIONS.DESCRIPTION)
    tags = describableAttrib(type=List[str], factory=list, description="What are the id's of the tags that need to be collectively found on attributes that to belong to this group?")
    parent = describableAttrib(type=Optional[str], default=None, description="Does this group extend a parent group of attributes ...?")
    id = describableAttrib(type=Optional[str], factory=unique_id, description=DESCRIPTIONS.ID)
    context = describableAttrib(type=str, default=SCHEMA_CONTEXTS.PROFILE_ATTRIBUTE_TAXONOMY, description=DESCRIPTIONS.CONTEXT)


@attrs(frozen=True)
class ProfileSchema(object):
    """
    Represents a group of attributes shared by a class of entities.
    """
    # ----
    name = describableAttrib(type=str, description=DESCRIPTIONS.NAME)
    title = describableAttrib(type=str, description=DESCRIPTIONS.TITLE)
    description = describableAttrib(type=str, validator=[lambda inst, a, v: v], description=DESCRIPTIONS.DESCRIPTION)
    # ----
    attributes = describableAttrib(type=List[ProfileAttributeSchema],
        converter=lambda l: dicts_to_classes(l, ProfileAttributeSchema), factory=list,
        description="What attributes are applicable to the profile schema?"
    )
    attributeTags = describableAttrib(type=List[ProfileTagSchema],
        converter=lambda l: dicts_to_classes(l, ProfileTagSchema), factory=list,
        description="What tags are applicable to attributes in the profile schema?"
    )
    facets = describableAttrib(type=List[ProfileFacetSchema],
        converter=lambda l: dicts_to_classes(l, ProfileFacetSchema), factory=list,
        description="How does the schema define how tags are grouped?"
    )
    taxonomy = describableAttrib(type=List[ProfileTaxonomySchema],
        converter=lambda l: dicts_to_classes(l, ProfileTaxonomySchema), factory=list,
        description="How does the schema define how attributes are grouped?"
    )
    # ----
    profileType = describableAttrib(type=str, description="What type of profile adheres to this schema?")
    tags = describableAttrib(type=List[str], factory=list, description=DESCRIPTIONS.TAGS)
    camel = describableAttrib(type=str, default=CAMEL, description=DESCRIPTIONS.CAMEL)
    context = describableAttrib(type=str, default=SCHEMA_CONTEXTS.PROFILE_SCHEMA, description=DESCRIPTIONS.CONTEXT)
    createdAt = describableAttrib(type=str, factory=utc_timestamp, description=DESCRIPTIONS.CREATED_AT, skip_when_serializing=True)
    _version = describableAttrib(type=Optional[int], default=None, skip_when_serializing=True, description="What is the schema's current version")
    id = describableAttrib(type=str, skip_when_serializing=True, description="What is the id of the schema?")

    @profileType.default  # type: ignore # ignore until mypy properyly supports attr ...
    def default_profile_type(self) -> str:
        return cast(str, self.name)

    @id.default  # type: ignore # ignore until mypy properyly supports attr ...
    def id_helper(self):
        return "{}:{}".format(self.name, self._version) if self._version is not None else self.name

    def __iter__(self):
        return iter(attr_class_to_dict(self, skip_nulls=True).items())

    def to_dict_with_internals(self):
        return attr_class_to_dict(self, skip_when_serializing=False, skip_nulls=True)

    def __add__(self, other) -> 'ProfileSchema':

        if not other:
            return self

        if not isinstance(other, ProfileSchema):
            raise NotImplementedError("Cannot add {} and {} types.".format(ProfileSchema.__name__, type(other).__name__))

        # Cant add ... if the profile types are not the same ...
        if not self.profileType == other.profileType:
            raise NotImplementedError("Can not add schemas with different profile types.")

        unique_attributes = merge_unique_objects_on(
            self.attributes + other.attributes, lambda x: x.name  # type: ignore
        )
        # TODO Warn if duplicate attributes are detected ...

        combined_tags = ((self.attributeTags or []) + (other.attributeTags or []))  # type: ignore
        unique_tags = merge_unique_objects_on(combined_tags , lambda x: x.name)
        # TODO Warn if duplicate tags are detected ...

        combined_facets = ((self.facets or []) + (other.facets or []))  # type: ignore
        unique_facets = merge_unique_objects_on(combined_facets, lambda x: x.name, lambda values: reduce(lambda x, y: x + y, values))
        # TODO Warn if duplicate facets are detected ...

        return evolve(self,
            attributes=unique_attributes,
            facets=unique_facets,
            attributeTags=unique_tags,
        )

# TODO Move this to the profiles/types!

@attrs(frozen=True)
class ProfileSchemaSummary(object):
    """
    Summary of a schema ...
    """
    schemaId = describableAttrib(type=str, description="What is the id of the schema?")
    timestamp = describableAttrib(type=str, description="When was this schema created?")
    profileType = describableAttrib(type=str, description="What type of profile is this schema for?")
    attributes = describableAttrib(type=int, description="How many attributes are defined in the schema?")
    attributeTags = describableAttrib(type=int, description="How many attributeTags are defined in the schema?")
    facets = describableAttrib(type=int, description="How many facets are defined in the schema?")
    # TODO ... add taxonomy to summary ...

    # ----

    @classmethod
    def from_profile_schema(cls, schema:ProfileSchema) -> 'ProfileSchemaSummary':
        return cls(  # type: ignore
            schemaId=schema.id,
            timestamp=schema.createdAt,
            profileType=schema.profileType,
            attributes=None if schema.attributes is None else len(schema.attributes),
            attributeTags=None if schema.attributeTags is None else len(schema.attributeTags),
            facets=None if schema.facets is None else len(schema.facets)
        )


# TODO ... derive list of profile Hierarchy Schemas from recursive group ...