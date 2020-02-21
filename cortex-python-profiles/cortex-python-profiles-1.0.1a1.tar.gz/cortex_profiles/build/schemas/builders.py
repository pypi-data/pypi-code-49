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

from typing import List, Optional, Callable, cast

import attr

from cortex_common.types import ProfileAttributeSchema, ProfileFacetSchema, ProfileSchema, ProfileTagSchema, \
    ProfileTaxonomySchema
from cortex_profiles.build.schemas import for_app_users, for_tagged_entities, for_insight_consumers
from cortex_profiles.build.schemas.utils.schema_building_utils import implicitly_generate_group_schemas
from cortex_profiles.types.schema_config import SchemaTemplates, SchemaTemplateForAppUsers, \
    SchemaTemplateForInsightConsumers, SchemaTemplateForTaggedEntities


class ProfileSchemaBuilder(object):
    """
    Helps build Profile Schemas.
    """
    def __init__(self,
                 name:str=None,
                 title:Optional[str]=None,
                 description:Optional[str]=None,
                 schemaId:Optional[str]=None):
        self._schema: ProfileSchema = ProfileSchema(  #type:ignore
            name=name,
            title=title if title is not None else name,
            description=description if title is not None else name,
        )
        if schemaId is not None:
            self._schema = attr.evolve(self._schema, id=schemaId)

    def append_attributes_from_schema_config(self,
                                             schema_config:SchemaTemplates,
                                             disabledAttributes:Optional[List[str]]=None,
                                             contexts_to_cast:Optional[List[str]]=None) -> 'ProfileSchemaBuilder':
        """
        Generate attribute schemas based on schema template type ...
        :param schema_config:
        :param disabledAttributes:
        :param contexts_to_cast:
        :return:
        """
        attr_gen = cast(
            Callable,
            {
                SchemaTemplateForAppUsers: for_app_users.implicitly_generate_attribute_schemas,
                SchemaTemplateForInsightConsumers: for_insight_consumers.implicitly_generate_attribute_schemas,
                SchemaTemplateForTaggedEntities: for_tagged_entities.implicitly_generate_attribute_schemas,
            }[type(schema_config)]
        )

        attributes = attr_gen(
            schema_config,
            disabledAttributes=disabledAttributes,
            include_tags=True,
            contexts_to_cast=contexts_to_cast
        )

        return self.append_attributes(attributes)

    def append_tags_from_schema_config(self,
                                       schema_config:SchemaTemplates,
                                       additional_tags:Optional[List[ProfileTagSchema]]=None) -> 'ProfileSchemaBuilder':
        """
        Generate tag schemas based on schema template type ...
        :param schema_config:
        :param additional_tags:
        :return:
        """
        tag_gen = cast(
            Callable,
            {
                SchemaTemplateForAppUsers: for_app_users.implicitly_generate_tag_schemas,
                SchemaTemplateForInsightConsumers: for_insight_consumers.implicitly_generate_tag_schemas,
                SchemaTemplateForTaggedEntities: for_tagged_entities.implicitly_generate_tag_schemas,
            }[type(schema_config)]
        )
        tags = tag_gen(schema_config, additional_tags)
        return self.append_tags(tags)

    def append_implicit_facets(self) -> 'ProfileSchemaBuilder':
        """
        Auto generate implicit facets ...
        :return:
        """
        return self.append_facets(
            implicitly_generate_group_schemas(cast(List[ProfileTagSchema], self._schema.attributeTags))
        )

    def append_implicit_hierarchical_schema(self, schema_config:SchemaTemplates) -> 'ProfileSchemaBuilder':
        """
        Auto generate implicit hierarchy ...
        :return:
        """
        hierarchy_gen = cast(
            Callable,
            {
                SchemaTemplateForAppUsers: for_app_users.derive_hierarchy,
                SchemaTemplateForInsightConsumers: for_insight_consumers.derive_hierarchy,
                SchemaTemplateForTaggedEntities: for_tagged_entities.derive_hierarchy,
            }[type(schema_config)]
        )
        return self.append_hierarchy(hierarchy_gen())

    def append_from_schema_config(self,
                                  schema_confg:SchemaTemplates,
                                  disabledAttributes:Optional[List[str]]=None,
                                  additional_tags:Optional[List[ProfileTagSchema]]=None,
                                  contexts_to_cast:Optional[List[str]]=None) -> 'ProfileSchemaBuilder':
        """
        Appends schema from a schema config / template ...
        :param schema_confg:
        :param disabledAttributes:
        :param additional_tags:
        :param contexts_to_cast:
        :return:
        """
        additional_tags = additional_tags if additional_tags is not None else []
        return (
            self
                .append_attributes_from_schema_config(schema_confg, disabledAttributes, contexts_to_cast)
                .append_tags_from_schema_config(schema_confg, additional_tags)
                .append_implicit_facets()
                .append_implicit_hierarchical_schema(schema_confg)
        )

    def append_tags(self, attributeTags:List[ProfileTagSchema]) -> 'ProfileSchemaBuilder':
        """
        # TODO ... Adding tags should recreate the facets ... since new tags should have been added ...
        :param attributeTags:
        :return:
        """
        self._schema = attr.evolve(
            self._schema,
            attributeTags=(
                    cast(List, self._schema.attributeTags) +
                    cast(List, attributeTags)
            )
        )
        return self

    def append_facets(self, facets: List[ProfileFacetSchema]) -> 'ProfileSchemaBuilder':
        """
        Append facets to schema ...
        :param facets:
        :return:
        """
        # ... need to merge the tags in each group!
        self._schema = attr.evolve(
            self._schema,
            facets=(
                    cast(List, self._schema.facets) +
                    cast(List, facets)
            )
        )
        return self

    def append_attributes(self, attributes: List[ProfileAttributeSchema]) -> 'ProfileSchemaBuilder':
        """
        Append attributes to schema ...
        :param attributes:
        :return:
        """
        self._schema = attr.evolve(
            self._schema,
            attributes=(
                cast(List, self._schema.attributes) +
                cast(List, attributes)
            )
        )
        return self

    def append_hierarchy(self, taxonomy: List[ProfileTaxonomySchema]) -> 'ProfileSchemaBuilder':
        """
        Append heirarchy to schema ...
        :param taxonomy:
        :return:
        """
        self._schema = attr.evolve(
            self._schema,
            taxonomy=(
                cast(List, self._schema.taxonomy) +
                cast(List, taxonomy)
            )
        )
        return self

    def get_schema(self) -> ProfileSchema:
        return self._schema
