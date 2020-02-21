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

from itertools import product
from typing import List, Union, Type, Optional

import attr

from cortex_common.constants.contexts import ATTRIBUTE_VALUES
from cortex_common.types import ProfileAttributeSchema, ProfileTagSchema, ProfileValueTypeSummary, \
    DeclaredProfileAttribute, ProfileFacetSchema, ProfileAttributeType, ProfileAttributeValue
from cortex_common.utils import group_objects_by
from cortex_profiles.build.schemas.builtin_templates.groups import ImplicitGroups
from cortex_profiles.build.schemas.builtin_templates.vocabulary import \
    construct_vocabulary_from_schema_template_candidate
from cortex_profiles.types import SchemaTemplates


def determine_detailed_type_of_attribute_value(attribute:dict) -> ProfileValueTypeSummary:
    """
    Inferes the ProfileValueTypeSummar from an profile attribute dict.
    :param attribute:
    :return:
    """
    if attribute["attributeValue"]["context"] == ATTRIBUTE_VALUES.DIMENSIONAL_PROFILE_ATTRIBUTE_VALUE:
        return ProfileValueTypeSummary(  #type:ignore
            outerType = attribute["attributeValue"]["context"],
            innerTypes = [
                ProfileValueTypeSummary(outerType=attribute["attributeValue"]["contextOfDimension"]),  #type:ignore
                ProfileValueTypeSummary(outerType=attribute["attributeValue"]["contextOfDimensionValue"])  #type:ignore
            ]
        )
    else:
        return ProfileValueTypeSummary(outerType=attribute["attributeValue"]["context"])  #type:ignore


def find_tag_in_group_for(group, key):
    """
    Formats a key belonging to a specific group.
    :param group:
    :param key:
    :return:
    """
    return "{}/{}".format(group, key) if key else None


def prepare_template_candidates_from_schema_fields(schema_config:SchemaTemplates, attr_fields:List) -> List[dict]:
    """
    Prepares a list of candidates to populate attribute schemas based on the schema config
    :param schema_config:
    :param attr_fields:
    :return:
    """
    relevant_schema = attr.asdict(schema_config, recurse=False, filter=lambda a, v: a in attr_fields)
    candidates = [
        construct_vocabulary_from_schema_template_candidate(dict(zip(relevant_schema.keys(), z)), schema_config)
        for z in list(product(*[x for x in relevant_schema.values()]))
    ]
    return candidates


def custom_attributes(
        attributes:List[dict],
        schema_config:SchemaTemplates,
        valueType:Optional[ProfileValueTypeSummary]=None,
        attributeType:Type[ProfileAttributeType]=DeclaredProfileAttribute,
        tags:List[str]=[],
        valueTypeClass:Optional[Type[ProfileAttributeValue]]=None) -> List[ProfileAttributeSchema]:
    """
    Factory method to construct ProfileAttributeSchemas for custom attributes when populating schema templates.
    :param attributes:
    :param schema_config:
    :param valueType:
    :param attributeType:
    :param tags:
    :return:
    """

    if valueType is None and valueTypeClass is None:
        raise Exception("Either valueType or valueTypeClass must be provided. Both can not be None.")

    set_fields_in_schema_config = [
        f
        for f in attr.fields(type(schema_config))
        if attr.asdict(schema_config).get(f.name)
    ]
    candidates = prepare_template_candidates_from_schema_fields(schema_config, set_fields_in_schema_config)
    return list(set([
        ProfileAttributeSchema(  #type:ignore
            name=attribute["name"].format(**cand),
            type=attr.fields(attributeType).context.default,
            valueType=valueType if valueType is not None else valueTypeClass.detailed_schema_type(),  #type:ignore
            label=attribute["label"],
            description=attribute["description"],
            questions=[attribute["question"]],
            tags=[x.format(**cand) for x in tags],
        )
        for cand in candidates
        for attribute in attributes
    ]))


def implicitly_generate_group_schemas(attributeTags:List[ProfileTagSchema]) -> List[ProfileFacetSchema]:
    """
    Generate implicit attribute facet groups in schemas.
    :param attributeTags:
    :return:
    """
    all_groups = list(ImplicitGroups.values())
    all_tags = attributeTags
    tags_grouped_by_group = group_objects_by(all_tags, lambda t: t.group)
    groups_grouped_by_id = group_objects_by(all_groups, lambda g: g.name)
    tag_groups = [
        attr.evolve(
            group_schemas[0],
            tags=list(sorted(map(lambda x: x.name, tags_grouped_by_group.get(group_id, []))))
        )
        for group_id, group_schemas in groups_grouped_by_id.items()
    ]
    return [x for x in tag_groups if len(x.tags) > 0]
