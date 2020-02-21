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

from functools import reduce
from typing import cast

import pydash

from cortex_common.types import ProfileTagSchema, ProfileValueTypeSummary, ProfileSchema, ProfileTaxonomySchema
from cortex_common.utils import dict_to_attr_class, flatten_list_recursively
from cortex_profiles.build.schemas.builders import ProfileSchemaBuilder
from cortex_profiles.build.schemas.utils.schema_building_utils import custom_attributes
from cortex_profiles.types import SchemaTemplates, SchemaTemplateForInsightConsumers, SchemaTemplateForAppUsers, \
    SchemaTemplateForTaggedEntities


def schema_config_dict_to_schema(additional_fields, schema_config_dict:dict) -> ProfileSchema:
    """
    Method to take dict that encapsulate schema config with other params and builds the appropriate schema.

    :param additional_fields:
    :param schema_config_dict:
    :return:
    """

    template_type = {
        "insight_consumer": SchemaTemplateForInsightConsumers,
        "tagged_entity": SchemaTemplateForTaggedEntities,
        "app_user": SchemaTemplateForAppUsers,
    }.get(schema_config_dict["template_type"], SchemaTemplateForInsightConsumers)

    schema_config_template: SchemaTemplates = cast(
        SchemaTemplates,
        template_type(**schema_config_dict["fill_implicit_schema_template_with"])  #type:ignore
    )
    additional_attributes = flatten_list_recursively([
        custom_attributes(
            attr_group["attributes"],
            schema_config_template,
            valueType=dict_to_attr_class(attr_group["valueType"], ProfileValueTypeSummary),
            tags=attr_group.get("tags", [])
        )
        for attr_group in schema_config_dict.get("additional_groups_of_attributes", [])
    ])
    additional_tags = [
        dict_to_attr_class(x, ProfileTagSchema)
        for x in schema_config_dict.get("additional_attribute_tags", [])
    ]
    disabled_attributes = schema_config_dict.get("disabled_attributes", [])

    name = pydash.get(additional_fields, "name")
    title = pydash.get(additional_fields, "title")
    description = pydash.get(additional_fields, "description")
    additional_heirarchy = [
        dict_to_attr_class(x, ProfileTaxonomySchema)
        for x in schema_config_dict.get("additional_heirarchy_nodes", [])
    ]

    schema = (
        ProfileSchemaBuilder(name, title, description)  #type:ignore
            .append_attributes(additional_attributes)
            .append_tags(additional_tags)
            .append_hierarchy(additional_heirarchy)
            .append_from_schema_config(schema_config_template, disabledAttributes=disabled_attributes, additional_tags=additional_tags, contexts_to_cast=schema_config_dict.get("profile_link_contexts"))
            .get_schema()
    )
    return schema


def build_custom_schema(schema_config_dict:dict) -> dict:
    """
    Helps build a profile schema ...

    :param schema_config_dict:
    :return:
    """
    additional_fields = schema_config_dict.get("additional_fields", {})
    schemas = list(map(
        lambda cfg: schema_config_dict_to_schema(additional_fields, cfg),
        schema_config_dict.get("schema_configs", [])
    ))
    schema = dict(reduce(
        lambda x, y: cast(ProfileSchema, x) + cast(ProfileSchema, y),
        schemas
    ))
    return pydash.merge(schema, schema_config_dict.get("additional_fields", {}))


def main():
    """
    Helper Main Method
    :return:
    """
    import json
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '-i', '--schema-config', '--schema-config-file', action='store', required=True)
    parser.add_argument('-o', '--output-file', action='store', required=True)
    args = parser.parse_args()

    schema_config_file = args.schema_config
    schema_file = args.output_file

    with open(schema_file, "w") as fhw:
        with open(schema_config_file, "r") as fh:
            new_schema = build_custom_schema(json.load(fh))
        json.dump(new_schema, fhw, indent=4)


if __name__ == '__main__':
    main()