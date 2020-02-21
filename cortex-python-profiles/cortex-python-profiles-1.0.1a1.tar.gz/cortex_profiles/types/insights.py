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

from attr import attrs, validators

from cortex_common.constants import CONTEXTS, VERSION, DESCRIPTIONS
from cortex_common.utils import unique_id, utc_timestamp, describableAttrib, dict_to_attr_class

__all__ = [
    "Link",
    "InsightTag",
    "Insight",
    "InsightRelatedToConceptTag",
]


@attrs(frozen=True)
class Link(object):

    """
    Linking to a specific concept by id.
    """
    id = describableAttrib(type=str, description=DESCRIPTIONS.ID)
    # context in links are not internal ... since there is no link context! ... they are also not defaulted ... since they need to be specified ...
    context = describableAttrib(type=str, description=DESCRIPTIONS.CONTEXT)
    title = describableAttrib(type=Optional[str], default=None, description="What is the human friendly name of this link?")
    # TODO ... should we add a resourceLink so people can point to a website / some other db? ...
    version = describableAttrib(type=str, default=VERSION, description=DESCRIPTIONS.VERSION, internal=True)


@attrs(frozen=True)
class InsightTag(object):
    """
    Tags that can occur on insights.
    """
    id = describableAttrib(
        type=str,
        description=DESCRIPTIONS.ID
    )
    insight = describableAttrib(
        type=Link,
        converter=lambda x: dict_to_attr_class(x, Link),
        description="What insight is this tag about?"
    )
    tagged = describableAttrib(
        type=str,
        description="When was the insight tagged with this tag?"
    )
    concept = describableAttrib(
        type=Link,
        converter=lambda x: dict_to_attr_class(x, Link),
        description="What concept is being tagged by the insight?"
    )
    relationship = describableAttrib(
        type=Link,
        converter=lambda x: dict_to_attr_class(x, Link),
        description="What relationship does the tagged concept have with regards to the insight?"
    )
    context = describableAttrib(
        type=str,
        default=CONTEXTS.INSIGHT_CONCEPT_TAG,
        description=DESCRIPTIONS.CONTEXT,
        internal=True
    )
    version = describableAttrib(
        type=str,
        default=VERSION,
        description=DESCRIPTIONS.VERSION,
        internal=True
    )


@attrs(frozen=True)
class BaseInsight(object):
    """
    A piece of insightful information that may be relevant to many different users ...
    """
    id = describableAttrib(type=str, description=DESCRIPTIONS.ID)
    dateGeneratedUTCISO = describableAttrib(type=str, description="When was this insight generated?")
    insightType = describableAttrib(type=str, description="What kind of insight is this?")
    score = describableAttrib(type=Optional[float], description="When was this insight generated?")
    tags = describableAttrib(type=List[InsightTag], description="What concepts were tagged in this insight?")
    body = describableAttrib(type=Optional[dict], description="What is the main content captured within the insight?")
    context = describableAttrib(type=str, description=DESCRIPTIONS.CONTEXT, internal=True)
    version = describableAttrib(type=str, description=DESCRIPTIONS.VERSION, internal=True)


@attrs(frozen=True)
class CandidateInsight(BaseInsight):
    """
    A piece of insightful information that may be relevant to many different users ...
    """
    id = describableAttrib(type=str, factory=unique_id, description=DESCRIPTIONS.ID)
    dateGeneratedUTCISO = describableAttrib(type=str, factory=utc_timestamp, description="When was this insight generated?")
    score = describableAttrib(type=Optional[float], default=None, description="How relevant is this insight against all similar insights?")
    tags = describableAttrib(type=List[InsightTag], factory=list, description="What concepts relate to this insight?")
    body = describableAttrib(type=Optional[dict], factory=dict, description="What is the main content of the insight?")
    context = describableAttrib(type=str, default=CONTEXTS.CANDIDATE_INSIGHT, description=DESCRIPTIONS.CONTEXT, internal=True)
    version = describableAttrib(type=str, default=VERSION, description=DESCRIPTIONS.VERSION, internal=True)


@attrs(frozen=True)
class Insight(CandidateInsight):
    """
    A piece of information generated for a specific profile.
    i.e A personalized piece of information that has been presented in a specific way (or app)
        to a specific entity (end user, advisor, company, ...)
    """
    profileId = describableAttrib(type=str, default=None, validator=[validators.instance_of(str)], description="What profile was this insight generated for?")
    score = describableAttrib(type=Optional[float], default=None, description="How relevant is this insight for the intended recipient?")
    appId = describableAttrib(type=str, default=None, description="Which app will/did this insight surface in?")
    context = describableAttrib(type=str, default=CONTEXTS.INSIGHT, description=DESCRIPTIONS.CONTEXT, internal=True)


@attrs(frozen=True)
class InsightRelatedToConceptTag(InsightTag):
    """
    Tag relating an insight to another concept.
    """
    insightId = describableAttrib(type=str, factory=unique_id, description="What insight is this tag related to?")
    insight = describableAttrib(type=Link, description="What insight is this tag related to?")
    id = describableAttrib(type=str, factory=unique_id, description=DESCRIPTIONS.ID)
    tagged = describableAttrib(type=str, factory=utc_timestamp, description="When was the insight tagged with this tag?")
    relationship = describableAttrib(
        type=Link,
        default=Link(id=CONTEXTS.INSIGHT_TAG_RELATED_TO_RELATIONSHIP, context=CONTEXTS.INSIGHT_TAG_RELATIONSHIP),  #type: ignore
        description="What relationship does the tagged concept have with regards to the insight?"
    )

    @insight.default  #type: ignore
    def from_insight_id(self):
        return Link(
            id=self.insightId,
            context=CONTEXTS.INSIGHT,
            version=VERSION
        )

