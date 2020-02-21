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

from typing import List, Mapping, Any, Callable, Optional

import attr

from cortex_common.types import ProfileTagSchema, ProfileFacetSchema
from cortex_common.utils import label_generator, AttrsAsDict
from cortex_profiles.build.schemas.builtin_templates.groups import ImplicitGroups
from cortex_profiles.build.schemas.builtin_templates.vocabulary import tag_template


def profile_tag_schema_in_group(tagId:str, group:ProfileFacetSchema, **kwargs:Mapping[str, Any]) -> ProfileTagSchema:
    """
    Factory method to create a Tag Schema for a tag in a specific group.
    :param tagId:
    :param group:
    :param kwargs:
    :return:
    """
    return ProfileTagSchema(  #type:ignore
        name="{}/{}".format(group.name, tagId.replace("/","-")),
        group=group.name,
        **kwargs
    )


class ImplicitAttributeSubjects(AttrsAsDict):
    """
    These are the different subjects expected to be used within the subject group ...
    """
    INTERACTIONS = "interactions"
    INSIGHT_INTERACTIONS = "insight-interactions"
    INSIGHT_APPEARANCES = "insight-appearances"
    APP_USAGE = "application-usage"


class ImplicitAttributeUsage(AttrsAsDict):
    """
    These are the different uasges expected to be used within the usage group ...
    """
    GENERAL = "general"
    APP_SPECIFIC = "app-specific"


class ImplicitTagDescriptions(AttrsAsDict):
    """
    Built in descriptions of tags that appear in some of the built-in templates.
    """
    DECLARED = "Which attributes are declared by the profile themself?"
    OBSERVED = "Which attributes are observed?"
    INFERRED = "Which attributes are inferred?"
    ASSIGNED = "Which attributes are assigned to the profile?"
    INTERACTION = "Which attributes capture a specific user interaction?"
    INSIGHT_INTERACTIONS = "Which attributes capture a part of the profile's interactions with insights?"
    INSIGHT_APPEARANCES = "Which attributes capture how this profile is featured in insights?"
    APP_USAGE = "Which attributes capture a part of the profile's application usage behavior?"
    APP_SPECIFIC = "Which attributes are specific to an specific application?"
    CONCEPT_SPECIFIC = "Which attributes are related to external concepts?"
    CONCEPT_AGNOSTIC = "Which attributes are agnostic of external concepts?"
    APP_INTERACTION = "Which attributes related to significant interactions that occured within a specific application?"
    GENERAL = "Which attributes are expected to be used generally?"


class ImplicitTagLabels(AttrsAsDict):
    """
    Built in labels of tags that appear in some of the built-in templates.
    """
    DECLARED = "ICD"
    OBSERVED = "ICO"
    INFERRED = "ICI"
    ASSIGNED = "ICA"
    INSIGHT_INTERACTIONS = "SII"
    INSIGHT_APPEARANCES = "SIA"
    APP_INTERACTION = "SAE"
    APP_USAGE = "SAU"
    APP_SPECIFIC = "CAS"
    CONCEPT_SPECIFIC = "CCS"
    CONCEPT_AGNOSTIC = "CCA"
    GENERAL = "GNR"


class ImplicitTags(AttrsAsDict):
    """
    Built in tags that appear in some of the built-in templates.
    """
    DECLARED = profile_tag_schema_in_group(  #type:ignore
        "declared", ImplicitGroups.ATTRIBUTE_TYPE,
        label=ImplicitTagLabels.DECLARED, description=ImplicitTagDescriptions.DECLARED
    )
    OBSERVED = profile_tag_schema_in_group(  #type:ignore
        "observed", ImplicitGroups.ATTRIBUTE_TYPE,
        label=ImplicitTagLabels.OBSERVED, description=ImplicitTagDescriptions.OBSERVED
    )
    INFERRED = profile_tag_schema_in_group(  #type:ignore
        "inferred", ImplicitGroups.ATTRIBUTE_TYPE,
        label=ImplicitTagLabels.INFERRED, description=ImplicitTagDescriptions.INFERRED
    )
    ASSIGNED = profile_tag_schema_in_group(  #type:ignore
        "assigned", ImplicitGroups.ATTRIBUTE_TYPE,
        label=ImplicitTagLabels.ASSIGNED, description=ImplicitTagDescriptions.ASSIGNED
    )

    CONCEPT_SPECIFIC = profile_tag_schema_in_group(  #type:ignore
        "concept-specific", ImplicitGroups.CLASSIFICATIONS,
        label=ImplicitTagLabels.CONCEPT_SPECIFIC, description=ImplicitTagDescriptions.CONCEPT_SPECIFIC
    )
    CONCEPT_AGNOSTIC = profile_tag_schema_in_group(  #type:ignore
        "concept-agnostic", ImplicitGroups.CLASSIFICATIONS,
        label=ImplicitTagLabels.CONCEPT_AGNOSTIC, description=ImplicitTagDescriptions.CONCEPT_AGNOSTIC
    )

    INSIGHT_INTERACTIONS = profile_tag_schema_in_group(  #type:ignore
        ImplicitAttributeSubjects.INSIGHT_INTERACTIONS, ImplicitGroups.SUBJECTS,
        label=ImplicitTagLabels.INSIGHT_INTERACTIONS, description=ImplicitTagDescriptions.INSIGHT_INTERACTIONS
    )
    INSIGHT_APPEARANCES = profile_tag_schema_in_group(  #type:ignore
        ImplicitAttributeSubjects.INSIGHT_APPEARANCES, ImplicitGroups.SUBJECTS,
        label=ImplicitTagLabels.INSIGHT_APPEARANCES, description=ImplicitTagDescriptions.INSIGHT_APPEARANCES
    )
    APP_USAGE = profile_tag_schema_in_group(  #type:ignore
        ImplicitAttributeSubjects.APP_USAGE, ImplicitGroups.SUBJECTS,
        label=ImplicitTagLabels.APP_USAGE, description=ImplicitTagDescriptions.APP_USAGE
    )
    APP_INTERACTION = profile_tag_schema_in_group(  #type:ignore
        ImplicitAttributeSubjects.INTERACTIONS, ImplicitGroups.SUBJECTS,
        label=ImplicitTagLabels.APP_INTERACTION, description=ImplicitTagDescriptions.APP_INTERACTION
    )

    APP_SPECIFIC = profile_tag_schema_in_group(  #type:ignore
        ImplicitAttributeUsage.APP_SPECIFIC, ImplicitGroups.USAGE,
        label=ImplicitTagLabels.APP_SPECIFIC, description=ImplicitTagDescriptions.APP_SPECIFIC
    )
    GENERAL = profile_tag_schema_in_group(  #type:ignore
        ImplicitAttributeUsage.GENERAL, ImplicitGroups.USAGE,
        label=ImplicitTagLabels.GENERAL, description=ImplicitTagDescriptions.GENERAL
    )


class ImplicitTagTemplate(AttrsAsDict):
    """
    Templates for tags that appear in some of the built-in templates.
    """
    INTERACTION = tag_template("{{{interaction_type}}}")
    APP_ASSOCIATED = tag_template("{{{app_id}}}")
    ALGO_ASSOCIATED = tag_template("{{{insight_type_id}}}")
    CONCEPT_ASSOCIATED = tag_template("{{{concept_id}}}")


class ImplicitTagTemplateName(AttrsAsDict):
    """
    This includes the group name in the template ...
    The tag here ... is generated the same way the tag id in profile_tag_schema_in_group is generated ...
    """
    INTERACTION = profile_tag_schema_in_group(  #type:ignore
        tag_template("{{{interaction_type}}}"), ImplicitGroups["INTERACTION"], label=None, description=None
    ).name
    APP_ASSOCIATED = profile_tag_schema_in_group(  #type:ignore
        tag_template("{{{app_id}}}"), ImplicitGroups["APP_ASSOCIATED"], label=None, description=None
    ).name
    ALGO_ASSOCIATED = profile_tag_schema_in_group(  #type:ignore
        tag_template("{{{insight_type_id}}}"), ImplicitGroups["ALGO_ASSOCIATED"], label=None, description=None
    ).name
    CONCEPT_ASSOCIATED = profile_tag_schema_in_group(  #type:ignore
        tag_template("{{{concept_id}}}"), ImplicitGroups["CONCEPT_ASSOCIATED"], label=None, description=None
    ).name


def expand_template_for_tag(tag_template_name:str) -> Callable:
    """
    There needs to be a ImplicitGroup with the same name as the tag tempalte ...
    :param tag_template_name:
    :return:
    """
    def callable(candidate, used_tags:Optional[List[str]]=None) -> ProfileTagSchema:
        """
        :param candidate:
        :param used_tags: Used for automatic label generation ... dont want to reuse tag labels ...
        :return:
        """
        tag_name = ImplicitTagTemplate[tag_template_name].format(**candidate)
        tag = profile_tag_schema_in_group(  #type:ignore
            tag_name,
            ImplicitGroups[tag_template_name],
            label=None,
            description=DescriptionTemplates[tag_template_name].format(**candidate)
        )
        if used_tags is not None:
            tag = attr.evolve(tag, label=label_generator(tag.name, used_tags))  #type:ignore
        return tag
    return callable


# https://stackoverflow.com/questions/31907060/python-3-enums-with-function-values
class ImplicitTagTemplates(AttrsAsDict):
    """
    Whats the difference between this and `ImplicitTagTemplate` above?
        Looks like expand_template_for_tag references ImplicitTagTemplate, but why is this needed?
    """
    INTERACTION = expand_template_for_tag("INTERACTION")
    APP_ASSOCIATED = expand_template_for_tag("APP_ASSOCIATED")
    ALGO_ASSOCIATED = expand_template_for_tag("ALGO_ASSOCIATED")
    CONCEPT_ASSOCIATED = expand_template_for_tag("CONCEPT_ASSOCIATED")
    # TODO ... CUSTOM SUBJECT TAG ...


class DescriptionTemplates(AttrsAsDict):
    """
    Built in descriptions for tag templates that appear in some of the built-in templates.
    """
    INTERACTION = tag_template("Which attributes are associated with insights {{{interaction_statement}}} the profile?")
    APP_ASSOCIATED = tag_template("Which attributes are associated with the {{{app_name}}} ({{{app_symbol}}})?")
    ALGO_ASSOCIATED = tag_template("Which attributes are associated with the {{{insight_type}}} ({{{insight_type_symbol}}}) Algorithm?")
    CONCEPT_ASSOCIATED = tag_template("Which attributes are associated with {{{concepts}}}?")
