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

from typing import List, Optional

import attr
from attr import attrs

from cortex_common.types import ProfileTaxonomySchema
from cortex_common.utils.attr_utils import describableAttrib
from cortex_common.utils.object_utils import head, unique_id

__all__ = [
    "ProfileAttributeSchemaQuery",
    "RecursiveProfileHierarchyGroup",
]


@attrs(frozen=True)
class ProfileAttributeSchemaQuery(object):
    """
    Represents a query against attributes in a schema ...
    """
    # ---------------
    attributesWithNames = describableAttrib(type=Optional[List[str]], default=None, description="...?")
    attributesWithAnyTags = describableAttrib(type=Optional[List[str]], default=None, description="...?")
    attributesWithAllTags = describableAttrib(type=Optional[List[str]], default=None, description="...?")
    attributesInAnyGroups = describableAttrib(type=Optional[List[str]], default=None, description="...?")
    attributesInAllGroups = describableAttrib(type=Optional[List[str]], default=None, description="...?")
    none = describableAttrib(type=Optional[bool], default=None, description="Should any attributes be queried?")
    all = describableAttrib(type=Optional[bool], default=None, description="Should all attributes be queried?")
    # ---------------
    intersection = describableAttrib(
        type=Optional[List['ProfileAttributeSchemaQuery']], default=None,
        description="Should this query intersect with another query?"
    )
    union = describableAttrib(
        type=Optional[List['ProfileAttributeSchemaQuery']], default=None,
        description="How do I combine the results of multiple queries?"
    )
    inverse = describableAttrib(
        type=Optional['ProfileAttributeSchemaQuery'], default=None,
        description="How do I invert the results of a query?"
    )
    # ----------------
    intersection_as_default = describableAttrib(
        type=bool, default=True,
        description="If multiple options of the query are provided, will they be intersected by default?"
    )


def prepare_to_be_flattened(parentNode:'RecursiveProfileHierarchyGroup', childNode:'RecursiveProfileHierarchyGroup') -> 'RecursiveProfileHierarchyGroup':
    """
    Updates references in parent and children groups to include the hierarchical path.

    :param parentNode:
    :param childNode:
    :return:
    """
    oldChildName = childNode.name
    # Update the name of the child to have the parents name ...
    e1 = attr.evolve(childNode, name="{}/{}".format(parentNode.name, childNode.name))
    # Update all the children of the child node to point to the child nodes new name
    e2 = attr.evolve(e1, children=[
        attr.evolve(
            child_of_e1,
            parents=[attr.evolve(p, name=e1.name) if p.name == oldChildName else p for p in child_of_e1.parents]
        )
        for child_of_e1 in e1.children
    ])
    # Repeat process for all the children of the node ..
    e3 = attr.evolve(e2, children=[prepare_to_be_flattened(e2, child_of_e2) for child_of_e2 in e2.children])
    return e3


@attr.attrs(frozen=True)
class RecursiveProfileHierarchyGroup(object):
    """
    Helps with Programatically Defining recursive groups of attributes in a Profile Schema.
    """
    name = describableAttrib(type=str, description="What is the name of the profile hierarchy node?")
    label = describableAttrib(type=str, description="What is the label of the profile hierarchy node?")
    description = describableAttrib(type=str, description="What is the essential meaning of this group?")
    includedAttributes = describableAttrib(type=ProfileAttributeSchemaQuery, factory=list, description="What attributes are included in this group?")
    tags = describableAttrib(type=List[str], factory=list, description="What list of tags is applied to this group?")
    parents = describableAttrib(type=List['RecursiveProfileHierarchyGroup'], factory=list, description="What are the parents of this group of attributes ...?")
    children = describableAttrib(type=List['RecursiveProfileHierarchyGroup'], factory=list, description="What are the children of this group of attributes ...?")
    id = describableAttrib(type=str, factory=unique_id, description="What is the unique identifier for this group ...?")

    # Traversal method to help construct a recusive data structure
    def append_children(self, nodes:List['RecursiveProfileHierarchyGroup']) -> 'RecursiveProfileHierarchyGroup':
        """
        Children are to be associated later ...
        :param node:
        :return:
        """
        # The children are all siblings of the parent ...
        if not nodes:
            return self
        head, tail = nodes[0], nodes[1:]
        return self.append_child(head).append_children(tail)

    def append_child(self, node:'RecursiveProfileHierarchyGroup') -> 'RecursiveProfileHierarchyGroup':
        """
        Children are to be associated later ...
        :param node:
        :return:
        """
        return attr.evolve(self, children=self.children+[attr.evolve(node, tags=self.tags+node.tags, parents=node.parents+[self])]) #type:ignore


    def to_profile_hierarchy_schema(self) -> ProfileTaxonomySchema:
        """
        Previously ... this method used to take a ProfileSchema as input as well ... because it was needed to query the
                       attributes that were to be added to this schema ... this is no longer needed!
        :param schema:
        :return:
        """
        return ProfileTaxonomySchema(  #type:ignore
            name=self.name,
            label=self.label,
            description=self.description,
            tags=self.tags,
            parent=head([x.name for x in self.parents]),
            # attributes=query_attributes(self.includedAttributes, schema),
            # parents=[x.name for x in self.parents],
            # children=[x.name for x in self.children],
            id=self.id
        )

    def flatten(self) -> List[ProfileTaxonomySchema]:
        """
        Turns this RecursiveProfileHierarchyGroup into a ProfileTaxonomySchema
        :return:
        """
        schema_to_flatten = attr.evolve(self, children=[prepare_to_be_flattened(self, c) for c in self.children])
        return schema_to_flatten._flatten()

    def _flatten(self) -> List[ProfileTaxonomySchema]:
        """
        Internal method to help turn this RecursiveProfileHierarchyGroup into a ProfileTaxonomySchema
        :return:
        """
        hierarchical_schema = self.to_profile_hierarchy_schema()
        return [hierarchical_schema] + [x for child in self.children for x in child._flatten()]
