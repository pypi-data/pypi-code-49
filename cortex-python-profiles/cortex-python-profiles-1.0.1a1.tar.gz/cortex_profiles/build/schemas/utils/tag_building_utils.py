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

from typing import List, Mapping, Optional

from cortex_common.constants.contexts import ATTRIBUTES
from cortex_profiles.build.schemas.builtin_templates.groups import ImplicitGroups
from cortex_profiles.build.schemas.builtin_templates.tags import ImplicitTags, ImplicitTagTemplates
from cortex_profiles.build.schemas.builtin_templates.vocabulary import APP_ID, INSIGHT_TYPE, CONCEPT, \
    INTERACTION_TYPE


def expand_tags_for_profile_attribute(cand:Mapping[str, str], attribute_context:str, subject:Optional[str]) -> List[str]:
    """
    Determines which tags are applicable to a specific attribute ... based on the candidate being expanded ...
    Subjects lead to additional tags ...

    :param cand:
    :param attribute_context:
    :param subject:
    :return:
    """
    interaction_tag: Optional[str] = None if INTERACTION_TYPE not in cand else ImplicitTagTemplates.INTERACTION(cand).name
    insight_interaction_tag: Optional[str] = None if interaction_tag is None else ImplicitTags.INSIGHT_INTERACTIONS.name  #type:ignore

    app_association_tag: Optional[str] = None if APP_ID not in cand else ImplicitTagTemplates.APP_ASSOCIATED(cand).name
    app_specific_tag: Optional[str] = None if app_association_tag is None else ImplicitTags.APP_SPECIFIC.name  #type:ignore

    algo_association_tag: Optional[str] = None if INSIGHT_TYPE not in cand else ImplicitTagTemplates.ALGO_ASSOCIATED(cand).name
    concept_association_tag: Optional[str] = None if CONCEPT not in cand else ImplicitTagTemplates.CONCEPT_ASSOCIATED(cand).name

    # These two tags should be mutually exclusive ...
    concept_specific_tag: Optional[str] = None if concept_association_tag is None else ImplicitTags.CONCEPT_SPECIFIC.name  #type:ignore
    concept_agnostic_tag: Optional[str] = None if concept_specific_tag is not None else ImplicitTags.CONCEPT_AGNOSTIC.name  #type:ignore

    classification_tag: Optional[str] = {  #type:ignore
        ATTRIBUTES.DECLARED_PROFILE_ATTRIBUTE: ImplicitTags.DECLARED.name,
        ATTRIBUTES.OBSERVED_PROFILE_ATTRIBUTE: ImplicitTags.OBSERVED.name,
        ATTRIBUTES.INFERRED_PROFILE_ATTRIBUTE: ImplicitTags.INFERRED.name,
        ATTRIBUTES.ASSIGNED_PROFILE_ATTRIBUTE: ImplicitTags.ASSIGNED.name,
    }.get(attribute_context, None)

    subject_tag: Optional[str] = None if not subject else "{}/{}".format(ImplicitGroups.SUBJECTS.name, subject)

    applicable_tags: List[str] = [
        x
        for x in (
            interaction_tag, app_association_tag, algo_association_tag, concept_association_tag, classification_tag,
            subject_tag, concept_specific_tag, concept_agnostic_tag, app_specific_tag, insight_interaction_tag
        )
        if x is not None
    ]
    return applicable_tags