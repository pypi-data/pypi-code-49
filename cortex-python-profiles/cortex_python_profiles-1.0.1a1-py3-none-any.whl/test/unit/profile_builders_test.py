import json
import unittest

import attr
import pandas as pd

from cortex_profiles.build.attributes.builders import DeclaredAttributesBuilder
from cortex_profiles.build.schemas.builders import ProfileSchemaBuilder
from cortex_profiles.cli.schema_builder import build_custom_schema
from cortex_profiles.types import SchemaTemplateForInsightConsumers, SchemaTemplateForAppUsers, SchemaTemplateForTaggedEntities


class TestAgent(unittest.TestCase):

    def setUp(self):
        with open("./test/data/schema_configs/insight_consumers.json") as fh:
            self.insight_consumer_schema_config = SchemaTemplateForInsightConsumers(**json.load(fh))
        with open("./test/data/schema_configs/app_users.json") as fh:
            self.app_user_schema_config = SchemaTemplateForAppUsers(**json.load(fh))
        with open("./test/data/schema_configs/tagged_entities.json") as fh:
            self.tagged_entity_schema_config = SchemaTemplateForTaggedEntities(**json.load(fh))

        self.insight_consumer_schema = (
            ProfileSchemaBuilder("test/insight-consumer")
                .append_from_schema_config(self.insight_consumer_schema_config)
                .get_schema()
        )
        self.app_user_schema = (
            ProfileSchemaBuilder("test/app-user")
                .append_from_schema_config(self.app_user_schema_config)
                .get_schema()
        )
        self.tagged_entity_schema = (
            ProfileSchemaBuilder("test/tagged-entity")
                .append_from_schema_config(self.tagged_entity_schema_config)
                .get_schema()
        )

    def test_01_building_schemas(self):
        """
        Tests getting schemas from a mocked endpoint ...
        :return:
        """
        print(json.dumps(attr.asdict(self.insight_consumer_schema), indent=4))
        print(json.dumps(attr.asdict(self.app_user_schema), indent=4))
        print(json.dumps(attr.asdict(self.tagged_entity_schema), indent=4))

    def test_02_building_declared_attributes(self):
        kv_df = pd.DataFrame([
           {"profileId": "p1", "key": "profile.name", "value": "Jack"},
           {"profileId": "p1", "key": "profile.age", "value": 25},
           {"profileId": "p2", "key": "profile.name", "value": "Jill"},
           {"profileId": "p2", "key": "profile.age", "value": 26},
        ])

        value_only_df = pd.DataFrame([
            {"profileId": "p3", "name": "Adam", "age": 45},
            {"profileId": "p4", "name": "Eve", "age": 46},
        ])

        attributes = (
            DeclaredAttributesBuilder()
                .append_attributes_from_kv_df(kv_df)
                .append_attributes_from_column_in_df(value_only_df, key="profile.name", value_column="name")
                .append_attributes_from_column_in_df(value_only_df, key="profile.age", value_column="age")
                .get()
        )

        print("{} total attributes generated.".format(len(attributes)))
        for attribute in attributes:
            print(attribute)

    def test_03_profile_schema_equality(self):
        from cortex_common.types import ProfileAttributeSchema, ProfileValueTypeSummary
        self.assertEqual(
            ProfileAttributeSchema(
                name="n",
                type="t",
                valueType=ProfileValueTypeSummary(outerType="t", innerTypes=[]),
                label="l",
                description="d",
                questions=["q"],
                tags=["a", "b"],
            ),
            ProfileAttributeSchema(
                name="n",
                type="t",
                valueType=ProfileValueTypeSummary(outerType="t", innerTypes=[]),
                label="l",
                description="d",
                questions=["q"],
                tags=["a", "b"],
            )
        )

    @unittest.skip("disabled attribute queries")
    def test_04_querying_attributes_in_schema(self):
        from cortex_profiles.build.schemas.utils.attribute_query_utils import query_attributes
        from cortex_profiles.types import ProfileAttributeSchemaQuery

        def print_res(q, r):
            print("---")
            print("{} results for Query -> {}".format(len(r), attr.asdict(q, filter=lambda k, v: v is not None)))
            print(json.dumps(r, indent=4))
            print("---")

        queries = [
            ProfileAttributeSchemaQuery(all=True),
            ProfileAttributeSchemaQuery(attributesWithNames=[]),
            ProfileAttributeSchemaQuery(attributesWithAnyTags=["interaction/followed"]),
            ProfileAttributeSchemaQuery(attributesWithAnyTags=["interaction/followed", "interaction/ignored"]),
            ProfileAttributeSchemaQuery(
                inverse=ProfileAttributeSchemaQuery(attributesWithAnyTags=["interaction/followed"])),
            ProfileAttributeSchemaQuery(inverse=ProfileAttributeSchemaQuery(
                inverse=ProfileAttributeSchemaQuery(attributesWithAnyTags=["interaction/followed"]))),
            ProfileAttributeSchemaQuery(attributesInAnyGroups=["data-limits"]),
            ProfileAttributeSchemaQuery(attributesInAllGroups=["data-limits", "app-association"]),
            ProfileAttributeSchemaQuery(
                inverse=ProfileAttributeSchemaQuery(attributesInAllGroups=["data-limits", "app-association"])
            ),
        ]

        results = {
            k: list(query_attributes(v, self.schema))
            for k, v in enumerate(queries)
        }

        for k, v in results.items():
            print_res(queries[k], v)

    # @unittest.skip("skipping")
    def test_05_schema_building_tools(self):
        with open("./test/data/schema_configs/for_schema_building_tools.json") as fh:
            config = json.load(fh)
        schema = build_custom_schema(config)
        print(json.dumps(schema, indent=4))
