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
from typing import List, Optional, Callable, Set

import attr
from objectpath import Tree

from cortex_common.types import ProfileSchema
from cortex_profiles.types import ProfileAttributeSchemaQuery


def run_list_producing_query(schemaTree:Tree, query) -> List:
    """
    Runs a query on the schema tree to produce a list of attributes

    :param schemaTree:
    :param query:
    :return:
    """
    results = schemaTree.execute(query)
    return list(results) if results is not None else []


def query_inverse_of_attributes(schemaTree:Tree, attributes:List[str]) -> List:
    """
    Queries an inverse of the attributes from the schema tree.
    :param schemaTree:
    :param attributes:
    :return:
    """
    if not attributes:
        return attributes
    return run_list_producing_query(schemaTree, "$.attributes[ @.name not in {} ].name".format(attributes))


def query_all_attributes(schemaTree:Tree) -> List:
    """
    Queries all attributes.
    :param schemaTree:
    :return:
    """
    return run_list_producing_query(schemaTree, "$.attributes.*.name")


def query_attributes_with_names(schemaTree:Tree, names:List[str]) -> List:
    """
    Queries attributes with specific names.
    :param schemaTree:
    :param names:
    :return:
    """
    if not names:
        return names
    return run_list_producing_query(schemaTree, "$.attributes[ @.name in {} ].name".format(names))


def query_attributes_with_any_tags(schemaTree:Tree, tags:List[str]) -> List:
    """
    Queries attributes with any of the provided tags.
    :param schemaTree:
    :param tags:
    :return:
    """
    if not tags:
        return tags
    combine_sets: Callable[[Set, Set], Set] =  lambda setA, setB: setA.union(setB)
    sets_to_combine: List[Set] = [
        set(run_list_producing_query(schemaTree, f"$.attributes[ '{tag}' in @.tags ].name"))
        for tag in tags
    ]
    return list(reduce(combine_sets, sets_to_combine))  #type:ignore


def query_attributes_with_all_tags(schemaTree:Tree, tags:List[str]) -> List:
    """
    Queries attributes that contain all of the tags.
    :param schemaTree:
    :param tags:
    :return:
    """
    if not tags:
        return tags
    overlapping_items_in_sets: Callable[[Set, Set], Set] = lambda setA, setB: setA.intersection(setB)
    sets_to_combine: List[Set] = [
        set(run_list_producing_query(schemaTree, f"$.attributes[ '{tag}' in @.tags ].name"))
        for tag in tags
    ]
    return list(reduce(overlapping_items_in_sets, sets_to_combine))  #type:ignore


def tags_in_group(schemaTree:Tree, group:str) -> List:
    """
    Retreives all tags in a specific group.
    :param schemaTree:
    :param group:
    :return:
    """
    return [
        y
        for x in run_list_producing_query(schemaTree, f"$.groups[ '{group}' is @.id].tags")
        for y in x
    ]


def query_attributes_in_any_groups(schemaTree:Tree, groups:List[str]) -> List:
    """
    Queries attributes in a specific group.
    :param schemaTree:
    :param groups:
    :return:
    """
    if not groups:
        return groups
    combine_sets: Callable[[Set, Set], Set] = lambda setA, setB: setA.union(setB)
    sets_to_combine: List[Set] = [
        set(query_attributes_with_any_tags(schemaTree, tags_in_group(schemaTree, group)))
        for group in groups
    ]
    return list(reduce(combine_sets, sets_to_combine))  #type:ignore


def query_attributes_in_all_groups(schemaTree:Tree, groups:List[str]) -> List:
    """
    Queries attributes in all of the provided groups.
    :param schemaTree:
    :param groups:
    :return:
    """
    if not groups:
        return groups
    overlapping_items_in_sets: Callable[[Set, Set], Set] = lambda setA, setB: setA.intersection(setB)
    sets_to_combine: List[Set] = [
        set(query_attributes_with_any_tags(schemaTree, tags_in_group(schemaTree, group)))
        for group in groups
    ]
    return list(reduce(overlapping_items_in_sets, sets_to_combine))  #type:ignore


def query_attributes(query: ProfileAttributeSchemaQuery, schema:ProfileSchema, tree:Optional[Tree]=None) -> List[str]:
    """
    Runs an attribute query on a schema.
    :param query:
    :param schema:
    :param tree:
    :return:
    """
    tree = Tree(attr.asdict(schema)) if tree is None else tree
    query_result_sets: List = [
        [] if query.none else None,
        query_all_attributes(tree) if query.all is not None else None,
        query_attributes_with_names(tree, query.attributesWithNames) if query.attributesWithNames is not None else None,  #type:ignore
        query_attributes_with_any_tags(tree, query.attributesWithAnyTags) if query.attributesWithAnyTags is not None else None,  #type:ignore
        query_attributes_with_all_tags(tree, query.attributesWithAllTags) if query.attributesWithAllTags is not None else None,  #type:ignore
        query_attributes_in_any_groups(tree, query.attributesInAnyGroups) if query.attributesInAnyGroups is not None else None,  #type:ignore
        query_attributes_in_all_groups(tree, query.attributesInAllGroups) if query.attributesInAllGroups is not None else None,  #type:ignore
        reduce(  #type:ignore
            lambda setA, setB: setA.intersection(setB),
            [set(query_attributes(inner_query, schema, tree)) for inner_query in query.intersection]
        ) if query.intersection is not None else None,
        reduce(  #type:ignore
            lambda setA, setB: setA.union(setB),
            [set(query_attributes(inner_query, schema, tree)) for inner_query in query.union]
        ) if query.union is not None else None,
        query_inverse_of_attributes(tree, query_attributes(query.inverse, schema, tree)) if query.inverse is not None else None  #type:ignore
    ]
    results = reduce(
        lambda setA, setB: setA.intersection(setB) if query.intersection_as_default else setA.union(setB),
        [set(x) for x in query_result_sets if x is not None ]
    )
    return list(results)
