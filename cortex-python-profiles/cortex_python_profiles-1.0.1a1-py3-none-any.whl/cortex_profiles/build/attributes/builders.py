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

from typing import TypeVar, Generic, Optional, List, Union, Callable, Type, Dict

import attr
import pandas as pd
from cortex_common.types import AssignedProfileAttribute, ObservedProfileAttribute, DeclaredProfileAttribute, \
    ProfileAttributeValue, ProfileAttributeType, EntityEvent, ListOfAttributes
from cortex_common.utils import state_modifier
from cortex_profiles.build.attributes.from_app_interactions.for_app_users import \
    derive_implicit_attributes_from_application_interactions, \
    derive_implicit_attributes_from_timed_application_interactions
from cortex_profiles.build.attributes.from_app_interactions.for_app_users import \
    derive_implicit_profile_type_attribute as derive_implicit_profile_type_attribute_for_app_users
from cortex_profiles.build.attributes.from_declarations import derive_declared_attributes_from_key_value_df, \
    derive_declared_attributes_from_value_only_df
from cortex_profiles.build.attributes.from_insight_interactions.for_insight_consumers import \
    derive_implicit_profile_type_attribute as derive_implicit_profile_type_attribute_for_insight_consumers, \
    derive_implicit_attributes_from_insight_interactions
from cortex_profiles.build.attributes.from_insights.for_tagged_entities import \
    derive_implicit_profile_type_attribute as derive_implicit_profile_type_attribute_for_tagged_entites, \
    derive_implicit_attributes_for_entities_in_insight_tags
from cortex_profiles.build.attributes.from_sessions.for_app_users import derive_implicit_attributes_from_sessions
from cortex_profiles.build.attributes.utils.etl_utils import turn_attribute_into_entity_event

T = TypeVar('T')

# Can these builders be used to build attributes for more than 1 profile?

__all__ = [
    'AttributeBuilderForInsightConsumers',
    'AttributeBuilderForEntitiesTaggedInInsights',
    'AttributeBuildersForAppUsers',
    'DeclaredAttributesBuilder',
    'AttributeEntityEventBuilder',
]


class ListBuilder(Generic[T]):
    """
    Helps Build A List
    """
    def __init__(self, initialItems:Optional[List[T]]=None):
        self.items = initialItems if initialItems else []

    def __iter__(self):
        return iter(self.get())

    def get(self) -> List[T]:
        return self.items


append_response = lambda self, results: self.items.append(results)


extend_response = lambda self, results: self.items.extend(results)


class AttributeBuilderForInsightConsumers(ListBuilder[ProfileAttributeType]):
    """
    Helps build attributes for an entity that consumes insights.
    """
    @state_modifier(derive_implicit_profile_type_attribute_for_insight_consumers, append_response)
    def append_implicit_type_attribute(self, *args, **kwargs) -> 'AttributeBuilderForInsightConsumers':
        """
        See :func:`.derive_declared_attributes_from_value_only_df` for input argument instructions.
        :return: The builder itself, after its state has been modified with the appended attributes ...
        """
        return self

    @state_modifier(derive_implicit_attributes_from_insight_interactions, extend_response)
    def append_implicit_insight_interaction_attributes(self, *args, **kwargs) -> 'AttributeBuilderForInsightConsumers':
        """
        See :func:`.derive_declared_attributes_from_key_value_df` for input argument instructions.
        :return: The builder itself, after its state has been modified with the appended attributes ...
        """
        return self

    @state_modifier(derive_implicit_attributes_from_sessions, extend_response)
    def append_implicit_session_attributes(self, *args, **kwargs) -> 'AttributeBuilderForInsightConsumers':
        """
        See :func:`.derive_implicit_attributes_from_sessions` for input argument instructions.
        :return: The builder itself, after its state has been modified with the appended attributes ...
        """
        return self

    def append_attributes_for_single_insight_consumer(self,
                                                      profileId:str,
                                                      insights_df:pd.DataFrame,
                                                      interactions_df:pd.DataFrame,
                                                      sessions_df:pd.DataFrame) -> 'AttributeBuilderForInsightConsumers':
        """
        Append attributes to build a single profile of an insight consumer.
        :param profileId:
        :param insights_df:
        :param interactions_df:
        :param sessions_df:
        :return:
        """
        self.append_implicit_type_attribute(profileId)
        self.append_implicit_insight_interaction_attributes(insights_df, interactions_df)
        self.append_implicit_session_attributes(sessions_df)
        return self


class AttributeBuilderForEntitiesTaggedInInsights(ListBuilder[Union[AssignedProfileAttribute, ObservedProfileAttribute]]):
    """
    Helps build attributes for an entity that is tagged in insights.
    """
    @state_modifier(derive_implicit_profile_type_attribute_for_tagged_entites, append_response)
    def append_implicit_type_attribute(self, *args, **kwargs):
        """
        See :func:`.derive_declared_attributes_from_value_only_df` for input argument instructions.
        :return: The builder itself, after its state has been modified with the appended attributes ...
        """
        return self

    @state_modifier(derive_implicit_attributes_for_entities_in_insight_tags, extend_response)
    def append_implicit_attributes_from_insight_tags(self, *args, **kwargs):
        """
        See :func:`.derive_declared_attributes_from_key_value_df` for input argument instructions.
        :return: The builder itself, after its state has been modified with the appended attributes ...
        """
        return self


class AttributeBuildersForAppUsers(ListBuilder[Union[AssignedProfileAttribute, ObservedProfileAttribute]]):
    """
    Helps build attributes for entity that uses specific application(s).
    """
    @state_modifier(derive_implicit_profile_type_attribute_for_app_users, append_response)
    def append_implicit_type_attribute(self, *args, **kwargs):
        """
        See :func:`.derive_declared_attributes_from_value_only_df` for input argument instructions.
        :return: The builder itself, after its state has been modified with the appended attributes ...
        """
        return self

    @state_modifier(derive_implicit_attributes_from_application_interactions, extend_response)
    def append_implicit_attributes_from_instantaneous_app_interactions(self, *args, **kwargs):
        """
        See :func:`.derive_declared_attributes_from_key_value_df` for input argument instructions.
        :return: The builder itself, after its state has been modified with the appended attributes ...
        """
        return self

    @state_modifier(derive_implicit_attributes_from_timed_application_interactions, extend_response)
    def append_implicit_attributes_from_spanning_app_interactions(self, *args, **kwargs):
        """
        See :func:`.derive_declared_attributes_from_key_value_df` for input argument instructions.
        :return: The builder itself, after its state has been modified with the appended attributes ...
        """
        return self


class DeclaredAttributesBuilder(ListBuilder[DeclaredProfileAttribute]):
    """
    Helps build declared attributes for entities.
    """
    @state_modifier(derive_declared_attributes_from_key_value_df, extend_response)
    def append_attributes_from_kv_df(self, *args, **kwargs):
        """
        See :func:`.derive_declared_attributes_from_key_value_df` for input argument instructions.
        :return: The builder itself, after its state has been modified with the appended attributes ...
        """
        return self

    @state_modifier(derive_declared_attributes_from_value_only_df, extend_response)
    def append_attributes_from_column_in_df(self, *args, **kwargs):
        """
        See :func:`.derive_declared_attributes_from_value_only_df` for input argument instructions.
        :return: The builder itself, after its state has been modified with the appended attributes ...
        """
        return self

    def append_attribute_from_key_in_dict(self,
                                          d:Dict,
                                          key_to_transform:str,
                                          attributeKey:Optional[str]=None,
                                          profileIdKey:str="profileId",
                                          profileSchemaKey:str="profileSchema",
                                          attribute_class:Type[ProfileAttributeType]=DeclaredProfileAttribute,
                                          value_constructor:Union[Callable, Type[ProfileAttributeValue]]=None):
        """
        Turns ...
        >>> {
        >>>     "profileId": "Bob",
        >>>     "dailyLogins": {
        >>>         "2019-10-01": 1,
        >>>         "2019-10-02": 1
        >>>     }
        >>> }
        Into a dimensional attribute ...
        """

        if profileIdKey not in d:
            raise Exception(f'Dict to build profiles from must contain a key named: {profileIdKey}')

        # Skips keys not actually in dict ...
        if key_to_transform not in d:
            return self

        attribute = attribute_class(  # type:ignore
            profileId=str(d[profileIdKey]),
            profileSchema=d.get(profileSchemaKey),
            attributeKey=attributeKey if attributeKey is not None else key_to_transform,
            attributeValue=value_constructor(d[key_to_transform])  #type:ignore
        )
        self.items.append(attribute)  #type:ignore
        return self


class AttributeEntityEventBuilder(ListBuilder[EntityEvent]):
    """
    Helps build Entity Events
    """

    def append_events_from_attributes(self, attributes:ListOfAttributes) -> 'AttributeEntityEventBuilder':
        """
        This method will help create entity building events from a list of attributes
        :return:
        """
        self.items.extend([
            turn_attribute_into_entity_event(a)
            for a in attributes
        ])
        return self

    def append_attribute_building_events_for_single_profile(
            self,
            profile_schema:str,
            data_for_single_profiles: Dict,
            attribute_value_types_per_attribute: Dict[str, Callable],
            profileId_key: str = "profileId",
            attribute_renamers:Optional[Dict[str,str]]=None,
            time_of_attribute_occurance:Optional[int]=None) -> 'AttributeEntityEventBuilder':
        """
        Takes ...
        {
            "customer_id": "123ABC",
            "age": 56,
            "name": "bob",
            "children": ["tim", "tom"],
        }
        And
        {
            "age": NumberAttributeValue,
            "name": StringAttributeValue,
            "children": lambda children: ListAttributeValue([StringAttributeValue(child) for child in children])
        }
        ....
        We also need to know the profileSchema that we are building these attributes for ...
        Along with the key that represents the profileId in the dictionary

        Optionally Provide keys to rename ...
        Optionally provide time that we became aware of all of these attributes ...
        """

        rename = attribute_renamers if attribute_renamers is not None else {}

        if profileId_key not in data_for_single_profiles:
            raise Exception(f'Dict to build profiles from must contain a key named: {profileId_key}')

        optionally_set_created_at = lambda x: (
            x if time_of_attribute_occurance is None else attr.evolve(x, createdAt=time_of_attribute_occurance)  #type:ignore
        )

        events = [
            turn_attribute_into_entity_event(
                # It doesnt matter that we are using declared here ... just need to do so for the method turn_attr
                # method to work ...
                optionally_set_created_at(
                    DeclaredProfileAttribute(  #type:ignore
                        profileId=data_for_single_profiles[profileId_key],
                        profileSchema=profile_schema,
                        attributeKey=rename.get(k, k),
                        attributeValue=attribute_constructor(data_for_single_profiles.get(k)),
                    )
                ),
                defaultEntityType=profile_schema
            )
            for k, attribute_constructor in attribute_value_types_per_attribute.items()
        ]

        self.items.extend(events)  #type:ignore
        return self

if __name__ == '__main__':
    pass
    # from cortex_common.types import NumberAttributeValue, StringAttributeValue, ListAttributeValue, DimensionalAttributeValue, Dimension, PercentageAttributeValue
    #
    # # TODO ... can we have multiple transformers for the same key? ... or just call it twice
    # builder = AttributeEntityEventBuilder()
    # builder.append_attribute_building_events_for_single_profile(
    #     "cortex/user",
    #     {
    #         "customer_id": "123ABC",
    #         "age": 56,
    #         "name": "bob",
    #         "children": ["tim", "tom"],
    #         "movies": {"Batman": 0.71, "Spiderman": 0.12, "Avengers": 0.98}
    #     },
    #     {
    #         "age": NumberAttributeValue,
    #         "name": StringAttributeValue,
    #         "children": lambda children: ListAttributeValue([StringAttributeValue(child) for child in children]),
    #         "movies": lambda movieScores: DimensionalAttributeValue(  #type:ignore
    #             value=[
    #                 Dimension(movie, PercentageAttributeValue(score))  #type:ignore
    #                 for movie, score in movieScores.items()
    #             ],
    #             contextOfDimension=StringAttributeValue,
    #             contextOfDimensionValue=PercentageAttributeValue,
    #         ),
    #     },
    #     attribute_renamers={
    #         "movies": "favoriteMovies"
    #     },
    #     profileId_key="customer_id"
    # )
    # for x in builder.get():
    #     print(dict(x))
    #
