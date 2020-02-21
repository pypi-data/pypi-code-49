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

from typing import Mapping, List, Optional, cast
from uuid import uuid4

import arrow
from cortex_common.constants.contexts import CONTEXTS
from cortex_profiles.synthesize import defaults
from cortex_profiles.synthesize.apps import AppProvider
from cortex_profiles.synthesize.base import BaseProviderWithDependencies
from cortex_profiles.synthesize.concepts import CortexConceptsProvider
from cortex_profiles.synthesize.tenant import TenantProvider
from cortex_profiles.types.insights import InsightTag, Link, Insight

from .utils import pick_random_time_between


class InsightsProvider(BaseProviderWithDependencies):
    """
    Generates synthetic insights
    """

    def __init__(self, *args,
                 insight_types:Mapping[str, List[str]]=defaults.INSIGHT_TYPES_PER_APP,
                 concept_limits_per_insight:Optional[Mapping[str, Mapping[str, int]]]=defaults.LIMITS_ON_COUNTS_CONCEPTS_OF_TYPE_PER_CONCEPT_SET,
                 **kwargs):
        super(InsightsProvider, self).__init__(*args, **kwargs)
        self.insight_types = insight_types
        self.concept_limits_per_insight = concept_limits_per_insight

    def dependencies(self) -> List[type]:
        """
        What providers does this provider depend on?
        :return:
        """
        return [
            CortexConceptsProvider,
            TenantProvider,
            AppProvider
        ]

    def insightId(self):
        """
        Generates a synthetic insight id
        :return:
        """
        return str(uuid4())

    def insightType(self, appId:str):
        """
        Generates a synthetic insight type
        :param appId:
        :return:
        """
        return self.fake.random.choice(self.insightTypes(appId))

    def insightTypes(self, appId:str):
        """
        Generates a list of synthetic insight types
        :param appId:
        :return:
        """
        return self.insight_types[appId.split(":")[0]]

    def tag(self, insightId:str, taggedOn:str, concept:Optional[Link]=None) -> InsightTag:
        """
        Generates a synthetic insight tag
        :param insightId:
        :param taggedOn:
        :param concept:
        :return:
        """
        concept = concept if concept else self.fake.concept()
        return InsightTag(  #type:ignore
            id=str(uuid4()),
            insight=Link(  #type:ignore
                id=insightId,
                context=CONTEXTS.INSIGHT
            ),
            tagged=taggedOn,
            concept=concept,
            relationship=Link(  #type:ignore
                id=CONTEXTS.INSIGHT_TAG_RELATED_TO_RELATIONSHIP,
                context=CONTEXTS.INSIGHT_TAG_RELATIONSHIP,
            )
        )

    def tags(self, insightId:str, taggedOn:str, tagged_concepts:Optional[List[Link]]=None, up_to_n_tags:int=10) -> List[InsightTag]:
        """
        Generates a list of synthetic insight tags
        Generates 10 tags by default ...
        :param insightId:
        :param taggedOn:
        :param tagged_concepts:
        :return:
        """
        default_concepts: List[Optional[Link]] = [cast(Optional[Link], None) for x in range(0, up_to_n_tags)]
        concepts: List[Optional[Link]] = cast(
            List[Optional[Link]],
            default_concepts if tagged_concepts is None else cast(List[Link], tagged_concepts)
        )
        return [self.tag(insightId, taggedOn, concept=tagged_concept) for tagged_concept in concepts]

    def concepts_relevant_to_insight(self) -> List[Link]:
        """
        Generates a list of synthetic concepts that could be relevant for a specific insight.
        :return:
        """
        return list(self.fake.set_of_concepts(self.concept_limits_per_insight))

    def insight(self, profileId) -> Insight:
        """
        Generates a synthetic insight
        :param profileId:
        :return:
        """
        insightId = self.insightId()
        appId = self.fake.appId()
        dateGenerated = str(pick_random_time_between(self.fake, arrow.utcnow().shift(days=-30), arrow.utcnow()))
        return Insight(  #type:ignore
            id=insightId,
            tags=self.tags(insightId, dateGenerated, tagged_concepts=self.concepts_relevant_to_insight()),
            insightType=self.insightType(appId=appId),
            profileId=profileId,
            dateGeneratedUTCISO=dateGenerated,
            appId=appId
        )

    def insights(self, profileId:str=None, min_insights:int=50, max_insights:int=250) -> List[Insight]:
        """
        Generates a list of synthetic insights
        :param profileId:
        :param min_insights:
        :param max_insights:
        :return:
        """
        profileId = profileId if profileId else self.fake.profileId()
        return [
            self.insight(profileId=profileId)
            for x in range(0, self.fake.random.randint(min_insights, max_insights))
        ]

