import unittest

import attr
import json
import pandas as pd
from typing import List
from cortex_profiles.build import DeclaredAttributesBuilder, AttributeBuilderForEntitiesTaggedInInsights
from cortex_profiles.synthesize import create_profile_synthesizer
from cortex_profiles.types import Insight, InsightRelatedToConceptTag, Link
from cortex_common.types import DimensionalAttributeValue, CounterAttributeValue, TotalAttributeValue, NumberAttributeValue, StringAttributeValue, BooleanAttributeValue, PercentileAttributeValue, PercentageAttributeValue, ListAttributeValue


def simplify_attribute_value(v):
    if isinstance(v, DimensionalAttributeValue):
        return {
            d.dimensionId: d.dimensionValue.value for d in v.value
        }
    else:
        return v.value

def kv_dict_for_profiles_in_attributes(iter:List)->dict:
    attributes = list(iter)
    pids = list(set([a.profileId for a in attributes]))
    return {
        pid: {
            a.attributeKey: simplify_attribute_value(a.attributeValue)
            for a in attributes if a.profileId == pid
        }
        for pid in pids
    }


class TestAgent(unittest.TestCase):

    def setUp(self):
        self.faker = create_profile_synthesizer()

    def test_01_declared_builders(self):
        """
        Tests getting schemas from a mocked endpoint ...
        :return:
        """
        kv_df = pd.DataFrame([
            {"profileId": "p1", "key": "profile.name", "value": "Jack"},
            {"profileId": "p1", "key": "profile.age", "value": 25},
            {"profileId": "p2", "key": "profile.name", "value": "Jill"},
            {"profileId": "p2", "key": "profile.age", "value": 26},
        ])

        attrs = DeclaredAttributesBuilder().append_attributes_from_kv_df(kv_df)
        profiles = kv_dict_for_profiles_in_attributes(attrs)
        self.assertEqual(profiles["p1"]["profile.name"], "Jack")
        self.assertEqual(profiles["p1"]["profile.age"], 25)
        self.assertEqual(profiles["p2"]["profile.name"], "Jill")
        self.assertEqual(profiles["p2"]["profile.age"], 26)

    def test_02_declared_builders(self):
        df = pd.DataFrame([
            {"profileId": "p3", "name": "Adam", "age": 45},
            {"profileId": "p4", "name": "Eve", "age": 46},
        ])

        attrs = (
            DeclaredAttributesBuilder()
                .append_attributes_from_column_in_df(df, "name", key="profile.name")
                .append_attributes_from_column_in_df(df, "age", key="profile.age")
        )

        profiles = {
            pid: {
                a.attributeKey: a.attributeValue.value
                for a in attrs if a.profileId == pid
            }
            for pid in df.profileId.unique()
        }

        self.assertEqual(profiles["p3"]["profile.name"], "Adam")
        self.assertEqual(profiles["p3"]["profile.age"], 45)
        self.assertEqual(profiles["p4"]["profile.name"], "Eve")
        self.assertEqual(profiles["p4"]["profile.age"], 46)


    def test_04_builder_for_tagged_entities(self):
        pid = self.faker.profileId()
        app = self.faker.appId()
        [it1, it2, *rest] = self.faker.insightTypes(app)

        insights = [
            Insight(
                insightType=it1,
                profileId=pid,
                appId=app,
                tags=[
                    InsightRelatedToConceptTag(
                        concept=Link(
                            id="1/a",
                            context="type/1"
                        )
                    ),
                    InsightRelatedToConceptTag(
                        concept=Link(
                            id="2/a",
                            context="type/2"
                        )
                    ),
                    # This should be ignored ...
                    InsightRelatedToConceptTag(
                        concept=Link(
                            id="9/a",
                            context="type/9"
                        )
                    ),
                ]
            ),
            Insight(
                insightType=it2, # Co-occurance is not insight type specific ...
                profileId=pid,
                appId=app,
                tags=[
                    InsightRelatedToConceptTag(
                        concept=Link(
                            id="3/a",
                            context="type/3"
                        )
                    ),
                    InsightRelatedToConceptTag(
                        concept=Link(
                            id="2/a",
                            context="type/2"
                        )
                    ),
                    InsightRelatedToConceptTag(
                        concept=Link(
                            id="1/a",
                            context="type/1"
                        )
                    ),
                    InsightRelatedToConceptTag(
                        concept=Link(
                            id="1/b",
                            context="type/1"
                        )
                    ),
                ]
            )
        ]

        insights_df = pd.DataFrame(list(map(lambda x: attr.asdict(x, recurse=False), insights)))
        builder = AttributeBuilderForEntitiesTaggedInInsights()
        builder.append_implicit_attributes_from_insight_tags(insights_df, "type/1", ["type/1", "type/2", "type/3"])
        profiles = kv_dict_for_profiles_in_attributes(builder)
        print(json.dumps(profiles, indent=4))


    def test_5_ensuring_attribute_values_can_be_easily_initialized(self):
        v = 1912323

        self.assertEqual(PercentileAttributeValue(v).value, v)
        self.assertEqual(PercentageAttributeValue(v).value, v)

        self.assertEqual(NumberAttributeValue(v).value,  v)
        self.assertEqual(NumberAttributeValue(v).with_unit("a", "c", "b", True).value,  v)

        self.assertEqual(TotalAttributeValue(v).value,  v)
        self.assertEqual(TotalAttributeValue(v).with_unit("a", "c", "b", True).value,  v)

        self.assertEqual(CounterAttributeValue(v).value,  v)
        self.assertEqual(CounterAttributeValue(v).with_unit("a", "c", "b", True).value,  v)

        self.assertEqual(BooleanAttributeValue(True).value, True)
        self.assertEqual(BooleanAttributeValue(False).value, False)

        self.assertEqual(StringAttributeValue("ABC").value, "ABC")

        self.assertEqual(ListAttributeValue([1,2,3]).value, [1,2,3])

    def test_6_test_casting(self):
        # TODO ...
        pass
