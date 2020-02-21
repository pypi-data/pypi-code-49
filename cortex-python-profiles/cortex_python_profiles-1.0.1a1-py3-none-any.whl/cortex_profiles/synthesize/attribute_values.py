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

from typing import List, Optional, Any

from cortex_common.types import Dimension, NumberAttributeValue, PercentileAttributeValue, \
    PercentageAttributeValue, TotalAttributeValue, \
    DimensionalAttributeValue, StringAttributeValue, \
    BooleanAttributeValue, ListAttributeValue, WeightAttributeValue, EntityAttributeValue, EntityEvent, ProfileRelationshipEvent, EntityRelationshipEvent, ProfileLink, EntityRelationshipAttributeValue, ProfileRelationshipAttributeValue
from cortex_common.utils import unique_id, str_or_context
from cortex_profiles.synthesize.base import BaseProviderWithDependencies
from cortex_profiles.synthesize.defaults import PROFILE_TYPES
from cortex_profiles.synthesize.tenant import TenantProvider

__all__ = [
    "AttributeValueProvider",
]


class AttributeValueProvider(BaseProviderWithDependencies):
    """
    Generates synthetic attribute values
    """
    # def __init__(self, *args, **kwargs):
    #     super(AttributeValueProvider, self).__init__(*args, **kwargs)
    #     self.fake = args[0]

    def dependencies(self) -> List[type]:
        """
        What are the dependencies of this provider?
        :return:
        """
        return [
            TenantProvider
        ]

    def profile_link(self) -> ProfileLink:
        """
        Generates a synthetic profile link
        :return:
        """
        return ProfileLink(  #type:ignore
            profileId=self.fake.profileId(),
            schemaId=self.fake.profileSchema(),
            profileVersion=self.fake.random.choice([None] + list(range(1, 100)))  #type:ignore
        )

    def dimensional_value(self, max_dimensions=7) -> DimensionalAttributeValue:
        """
        Generates a synthetic dimensional attribute value
        :param max_dimensions:
        :return:
        """
        dimensions = [
            Dimension(  #type:ignore
                dimensionId=unique_id(),
                dimensionValue=self.total_value()
            )
            for x in self.fake.range(0, max_dimensions)
        ]
        return DimensionalAttributeValue(  #type:ignore
            value=dimensions,
            contextOfDimension = str_or_context(StringAttributeValue),
            contextOfDimensionValue = str_or_context(TotalAttributeValue)
        )

    def string_value(self) -> StringAttributeValue:
        """
        Generates a synthetic string attribute value
        :return:
        """
        return StringAttributeValue(value=self.fake.color_name())  #type:ignore

    def boolean_value(self) -> BooleanAttributeValue:
        """
        Generates a synthetic boolean attribute value
        :return:
        """
        return BooleanAttributeValue(value=self.fake.random.choice([True, False]))  #type:ignore

    def list_value(self) -> ListAttributeValue:
        """
        Generates a synthetic list attribute value
        :return:
        """
        return ListAttributeValue(  #type:ignore
            value=self.fake.generate_up_to_x_uniq_elements(self.fake.color_name, 10)
        )

    def percentile_value(self) -> PercentileAttributeValue:
        """
        Generates a synthetic percentile attribute value
        :return:
        """
        return PercentileAttributeValue(value=min(self.fake.random.randint(0, 100) * 0.98, 100))  #type:ignore

    def percentage_value(self) -> PercentageAttributeValue:
        """
        Generates a synthetic percentage attribute value
        :return:
        """
        return PercentageAttributeValue(value=min(self.fake.random.randint(0, 100) * 0.98, 100))  #type:ignore

    def total_value(self) -> TotalAttributeValue:
        """
        Generates a synthetic total attribute value
        :return:
        """
        return TotalAttributeValue(value=self.number_value().value)  #type:ignore

    def number_value(self) -> NumberAttributeValue:
        """
        Generates a synthetic number attribute value
        :return:
        """
        return NumberAttributeValue(value=self.fake.random.choice([int, float])(self.fake.random.randint(0,100) * 0.123))  #type:ignore

    def weight_value(self) -> WeightAttributeValue:
        """
        Generates a synthetic weight attribute value
        :return:
        """
        a, b = self.fake.random.randint(0,100), self.fake.random.randint(0,100)
        weight = min(a, b) / max(a, b)
        return WeightAttributeValue(value=weight)  #type:ignore

    def linked_dimensional_value(self, max_dimensions=7) -> DimensionalAttributeValue:
        """
        Generates a synthetic dimensional attribute value with links
        :param max_dimensions:
        :return:
        """
        return DimensionalAttributeValue(  #type:ignore
            value=self.fake.generate_up_to_x_uniq_elements(
                lambda: Dimension(  #type:ignore
                    dimensionId=self.profile_link(),
                    dimensionValue=self.total_value()
                ),
                max_dimensions
            ),
            contextOfDimension = str_or_context(ProfileLink),
            contextOfDimensionValue = str_or_context(TotalAttributeValue)
        )

    def linked_list_value(self) -> ListAttributeValue:
        """
        Generates a synthetic list attribute values with links
        :return:
        """
        return ListAttributeValue(  #type:ignore
            value=self.fake.generate_up_to_x_uniq_elements(self.profile_link, 10)
        )

    def entity_value(self, value:Optional[EntityEvent]=None) -> EntityAttributeValue:
        """
        Generates a synthetic entity attribute value
        :param value:
        :return:
        """
        return EntityAttributeValue(  #type:ignore
            value=(
                value if value is not None else
                EntityEvent(  # type: ignore
                    event="18thBirthday",
                    entityId=self.fake.profileId(),
                    entityType=self.fake.profileSchema(),
                    properties={
                        "attendees": self.fake.random.randint(10**1,10**4),
                    }
                )
            )
        )

    def entity_rel_value(self, value:Optional[EntityRelationshipEvent]=None) -> EntityRelationshipAttributeValue:
        """
        Generates a synthetic relationship attribute value to entities
        :param value:
        :return:
        """
        return EntityRelationshipAttributeValue(  #type:ignore
            value=(
                value if value is not None else
                EntityRelationshipEvent(  # type: ignore
                    event="knows",
                    entityId=self.fake.profileId(),
                    entityType=self.fake.profileSchema(),
                    properties={
                        "encounters": self.fake.random.randint(1, 10**2)
                    },
                    targetEntityId=self.fake.profileId(),
                    targetEntityType=self.fake.profileSchema(),
                )
            )
        )

    def profile_rel_value(self, value:Optional[ProfileRelationshipEvent]=None) -> ProfileRelationshipAttributeValue:
        """
        Generates a synthetic relationship attribute value to profiles
        :param value:
        :return:
        """
        pl = self.profile_link()
        return ProfileRelationshipAttributeValue(  #type:ignore
            value=(
                value if value is not None else
                ProfileRelationshipEvent(  # type: ignore
                    event="similarTo",
                    entityId=self.fake.profileId(),
                    entityType=self.fake.profileSchema(),
                    properties={ "score": 0.75 },
                    targetLink=pl,
                    targetEntityId=pl.profileId,
                    targetEntityType=pl.schemaId,
                )
            ),
            weight=0.75,
        )

    def profile_type_value(self) -> ListAttributeValue:
        """
        Generates a synthetic attribute value capturing the types for the profile
        :return:
        """
        return ListAttributeValue(  #type:ignore
            value=self.fake.random_subset_of_list([PROFILE_TYPES])
        )

    def attribute_value(self):
        """
        Generates a synthetic attribute value
        :return:
        """
        return self.fake.random.choice([
            self.dimensional_value,
            self.number_value,
            self.percentage_value,
            self.percentile_value,
            self.total_value,
            self.number_value,
            self.profile_type_value,
            self.weight_value,
            self.entity_value,
            self.entity_rel_value,
            self.profile_rel_value,
            self.linked_dimensional_value,
            self.linked_list_value,
        ])()
