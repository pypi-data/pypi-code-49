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

from typing import List, Tuple, Optional, cast, Type

import pandas as pd

from cortex_common.types import ProfileAttribute, DeclaredProfileAttribute, InferredProfileAttribute, \
    ObservedProfileAttribute, AssignedProfileAttribute, ProfileAttributeType
from cortex_common.types import ProfileAttributeValue
from cortex_common.utils import unique_id, utc_timestamp, list_of_attrs_to_df
from cortex_profiles.build import AttributeBuilderForInsightConsumers
from cortex_profiles.synthesize.attribute_values import AttributeValueProvider
from cortex_profiles.synthesize.base import BaseProviderWithDependencies
from cortex_profiles.synthesize.insights import InsightsProvider
from cortex_profiles.synthesize.interactions import InteractionsProvider
from cortex_profiles.synthesize.sessions import SessionsProvider
from cortex_profiles.synthesize.tenant import TenantProvider
from cortex_profiles.types.insights import Insight
from cortex_profiles.types.interactions import Session, InsightInteractionEvent

value = ["duration", "count", "total", "distribution"]
app_specififity = ["app-specific", "app-agnostic"]
algo_specififity = ["algo-specific", "algo-agnostic",]
timeframe = ["{}{}".format(x, y) for x in range(0, 6) for y in ["week", "month", "year"]] + ["recent", "eternal"]
purpose = ["insight-interaction", "app-activity", "app-preferences", "algo-preferences", "user-declarations"]


class AttributeProvider(BaseProviderWithDependencies):
    """
    Generates synthetic attributes for users.
    """

    def __init__(self, *args, concept_universe: List[dict]=None, **kwargs):
        super(AttributeProvider, self).__init__(*args, **kwargs)
        self.conceptsToMakeEntityEventsFor = [x.get("context") for x in concept_universe or [] if x.get("context")]

    def dependencies(self) -> List[type]:
        """
        What other providers does this provider depend on?
        :return:
        """
        return [
            InsightsProvider,
            InteractionsProvider,
            SessionsProvider,
            AttributeValueProvider,
            TenantProvider
        ]

    def data_to_build_single_profile(self,
                                     profileId:str=None,
                                     max_sessions=10,
                                     max_insights=100
                                     ) -> Tuple[str,List[Session],List[Insight],List[InsightInteractionEvent]]:
        """
        Generates synthetic data to build a single insight-consuming profile
        :param profileId:
        :param max_sessions:
        :param max_insights:
        :return:
        """
        profileId = profileId if profileId else self.fake.profileId()
        sessions = self.fake.sessions(profileId=profileId, max_sessions=max_sessions)
        insights = self.fake.insights(profileId=profileId, max_insights=max_insights)
        interactions = self.fake.interactions(profileId, sessions, insights)
        return (profileId, sessions, insights, interactions)

    def dfs_to_build_single_profile(self, profileId:str=None) -> Tuple[str, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
        """
        Generates synthetic dfs of data needed to build a single insight-consuming profile.
        :param profileId:
        :return:
        """
        profileId, sessions, insights, interactions = self.data_to_build_single_profile(profileId=profileId)
        return (
            profileId, list_of_attrs_to_df(sessions), list_of_attrs_to_df(insights), list_of_attrs_to_df(interactions)
        )

    def attributes_for_single_profile(self, profileId:str=None) -> List[ProfileAttributeType]:
        """
        This returns a list of synthesized implicit attributes that cortex is capable of generating for profiles.
        :param profileId:
        :return:
        """
        (profileId, sessions_df, insights_df, interactions_df) = self.dfs_to_build_single_profile(profileId=profileId)
        return (
            AttributeBuilderForInsightConsumers()
                .append_attributes_for_single_insight_consumer(profileId, insights_df, interactions_df, sessions_df)
                .get()
        )

    def unique_attribute_key(self):
        """
        Generates a synthetic attribute key
        :return:
        """
        v = self.fake.random.choice(value)
        app = self.fake.random.choice(app_specififity)
        algo = self.fake.random.choice(algo_specififity)
        tf = self.fake.random.choice(timeframe)
        p = self.fake.random.choice(purpose)
        return f"{v}.app[{app}].algo[{algo}].timeframe[{tf}].purpose[{p}]"

    def inferred_attribute(self,
                           attributeKey:Optional[str]=None,
                           attribute_value:Optional[ProfileAttributeValue]=None) -> InferredProfileAttribute:
        """
        Generates a syntheric inferred attribute.
        TODO ... there are attribute values that are more likely to be inferred ...
        :param attributeKey:
        :param attribute_value:
        :return:
        """
        return cast(
            InferredProfileAttribute,
            self.attribute(
                attributeKey=attributeKey, attribute_class=InferredProfileAttribute, attribute_value=attribute_value
            )
        )

    def declared_attribute(self,
                           attributeKey:Optional[str]=None,
                           attribute_value:Optional[ProfileAttributeValue]=None) -> DeclaredProfileAttribute:
        """
        Generates a syntheric declared attribute.
        TODO ... there are attribute values that are more likely to be declared ...
        :param attributeKey:
        :param attribute_value:
        :return:
        """
        return cast(
            DeclaredProfileAttribute,
            self.attribute(
                attributeKey=attributeKey, attribute_class=DeclaredProfileAttribute, attribute_value=attribute_value
            )
        )

    def observed_attribute(self,
                           attributeKey:Optional[str]=None,
                           attribute_value:Optional[ProfileAttributeValue]=None) -> ObservedProfileAttribute:
        """
        Generates a syntheric observed attribute.
        TODO ... there are attribute values that are more likely to be observed ...
        :param attributeKey:
        :param attribute_value:
        :return:
        """
        return cast(
            ObservedProfileAttribute,
            self.attribute(
                attributeKey=attributeKey, attribute_class=ObservedProfileAttribute, attribute_value=attribute_value
            )
        )

    def assigned_attribute(self,
                           attributeKey:Optional[str]=None,
                           attribute_value:Optional[ProfileAttributeValue]=None) -> AssignedProfileAttribute:
        """
        Generates a syntheric assigned attribute.
        TODO ... there are attribute values that are more likely to be assigned ...
        :param attributeKey:
        :param attribute_value:
        :return:
        """
        return cast(
            AssignedProfileAttribute,
            self.attribute(
                attributeKey=attributeKey, attribute_class=AssignedProfileAttribute, attribute_value=attribute_value
            )
        )

    def attribute(self,
                  attributeKey:Optional[str]=None,
                  attribute_class:Optional[Type[ProfileAttribute]]=None,
                  attribute_value:Optional[ProfileAttributeValue]=None) -> ProfileAttribute:
        """
        Generates a synthetic attribute.
        :param attributeKey:
        :param attribute_class:
        :param attribute_value:
        :return:
        """
        attr_key = attributeKey if attributeKey else self.unique_attribute_key()
        attr_class = attribute_class if attribute_class else self.fake.random.choice(
            [DeclaredProfileAttribute, InferredProfileAttribute, ObservedProfileAttribute, AssignedProfileAttribute]
        )
        attr_value = attribute_value if attribute_value else self.fake.attribute_value()
        return attr_class(
            id=unique_id(),
            profileId=self.fake.profileId(),
            profileSchema="cortex/synthetic-schema",
            createdAt=utc_timestamp(),
            attributeKey=attr_key,
            attributeValue=attr_value,
            seq=self.fake.random.randint(0, 100),
        )

    def attributes(self, limit=100) -> List[ProfileAttribute]:
        """
        Generates a list of synthetic attributes.
        :param limit:
        :return:
        """
        return [
            self.attribute() for x in self.fake.range(0, limit)
        ]
