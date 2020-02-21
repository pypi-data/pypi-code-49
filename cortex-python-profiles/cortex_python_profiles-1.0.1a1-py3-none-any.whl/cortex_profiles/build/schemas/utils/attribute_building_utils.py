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

from typing import List, Optional, Union

from cortex_common.constants import ATTRIBUTES
from cortex_common.types import ListAttributeValue, StringAttributeValue, ProfileLink, \
    ProfileValueTypeSummary, ProfileAttributeSchema
from cortex_common.utils import str_or_context
from cortex_profiles.build.schemas.builtin_templates.attributes import Patterns, NameTemplates, TitleTemplates, \
    DescriptionTemplates, QuestionTemplates
from cortex_profiles.build.schemas.builtin_templates.tags import ImplicitTags
from cortex_profiles.datamodel.constants import UNIVERSAL_ATTRIBUTES
from .tag_building_utils import expand_tags_for_profile_attribute


def all_attribute_names_for_candidates(pattern: Patterns, candidates: list) -> List[str]:
    """
    Lists all the different attribute names.

    :param pattern:
    :param candidates:
    :return:
    """
    return [
        NameTemplates[pattern.name].format(**{k: v.id for k, v in cand.items()})
        for cand in candidates
    ]


def optionally_cast_to_profile_link(context:Union[str, type],
                                    contexts_to_cast:Optional[List[str]]=None) -> Optional[Union[str, type]]:
    """
    Optionally casts a context to a profile link ... if the context is listed to be casted.
    :param context:
    :param contexts_to_cast:
    :return:
    """
    plc = [] if contexts_to_cast is None else contexts_to_cast
    str_context = str_or_context(context)
    return str_context if str_context not in plc else ProfileLink


def expand_profile_attribute_schema(
            attribute_pattern: Patterns,
            attribute_filers:dict,
            valueType:ProfileValueTypeSummary,
            custom_subject:str=None,
            attributeContext:str=ATTRIBUTES.OBSERVED_PROFILE_ATTRIBUTE,
            include_tags:bool=True,
            additional_tags:Optional[List[str]]=None
        ) -> ProfileAttributeSchema:
    """
    Factory method to construct a ProfileAttributeSchema

    :param attribute_pattern:
    :param attribute_filers:
    :param valueType:
    :param custom_subject:
    :param attributeContext:
    :param include_tags:
    :param additional_tags:
    :return:
    """
    tags_to_add = additional_tags if additional_tags is not None else []
    return ProfileAttributeSchema(  #type:ignore
        name=NameTemplates[attribute_pattern.name].format(**{k: v.id for k, v in attribute_filers.items()}),
        type=attributeContext,
        valueType=valueType,
        label=TitleTemplates[attribute_pattern.name].format(**attribute_filers),
        description=DescriptionTemplates[attribute_pattern.name].format(**attribute_filers),
        questions=[QuestionTemplates[attribute_pattern.name].format(**attribute_filers)],
        tags=list(sorted(
            (expand_tags_for_profile_attribute(attribute_filers, attributeContext, custom_subject) + tags_to_add)
            if include_tags else [])
        )
    )


def schemas_for_universal_attributes(include_tags:bool=True, contexts_to_cast:Optional[List[str]]=None) -> List[ProfileAttributeSchema]:
    """
    What attribute schema can potentially apply to all schemas?
    :param include_tags:
    :param contexts_to_cast:
    :return:
    """
    return [
        ProfileAttributeSchema(  #type:ignore
            name=UNIVERSAL_ATTRIBUTES.TYPES,
            type=ATTRIBUTES.ASSIGNED_PROFILE_ATTRIBUTE,
            valueType=ListAttributeValue.detailed_schema_type(StringAttributeValue),
            label=TitleTemplates.TYPE,
            description=DescriptionTemplates.TYPE,
            questions=[QuestionTemplates.TYPE],
            tags=[ImplicitTags.ASSIGNED.name, ImplicitTags.GENERAL.name] if include_tags else []
        )
    ]


