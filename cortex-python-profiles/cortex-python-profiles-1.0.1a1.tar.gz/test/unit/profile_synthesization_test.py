import json
import unittest

import attr

from cortex_profiles.build.attributes.builders import AttributeBuilderForInsightConsumers
from cortex_profiles.synthesize import create_profile_synthesizer, defaults
from cortex_profiles.synthesize.concepts import CortexConceptsProvider


def insight_distribution_test(f):

    derived_interactions = f.raw_insight_distributions(f.insights("abc"))
    for i in defaults.INTERACTION_CONFIG:
        assert len(derived_interactions[i["interaction"]]) == len(set(derived_interactions[i["interaction"]]))

    mutually_exclusive_pairs = [
        (i["interaction"], me)
        for i in defaults.INTERACTION_CONFIG
        for me in i["mutuallyExlusiveOf"]
        if i["mutuallyExlusiveOf"]
    ]

    print(mutually_exclusive_pairs)
    for me_a, me_b in mutually_exclusive_pairs:
        assert len(set(derived_interactions[me_a]).intersection(set(derived_interactions[me_b]))) == 0, f"{me_a} and {me_b} are not mutually exclusive"

    print(f.insight_distributions(f.insights("abc")))


def insight_interaction_events_test(f):
    print(f.interactions("test-user-1", f.sessions("test-user-1"), f.insights(profileId="test-user-1")))


def generate_attribute_value_samples(synthesizer):
    samples = {
        "string_value": synthesizer.string_value(),
        "number_value": synthesizer.number_value(),
        "total_value": synthesizer.total_value(),
        "weight_value": synthesizer.weight_value(),
        "dimensional_value": synthesizer.dimensional_value(),
        "boolean_value": synthesizer.boolean_value(),
        "list_value": synthesizer.list_value(),
        "percentile_value": synthesizer.percentile_value(),
        "percentage_value": synthesizer.percentage_value(),
        "entity_value": synthesizer.entity_value(),
        "entity_rel_value": synthesizer.entity_rel_value(),
        "profile_rel_value": synthesizer.profile_rel_value(),
        # "relationship_value": synthesizer.relationship_value(),
    }
    return {
        k: attr.asdict(v) for k, v in samples.items()
    }


def generate_attribute_samples(synthesizer) -> dict:
    samples = {
        "inferred_attribute": synthesizer.inferred_attribute(
            "profile.interestIn.TechCompanies", synthesizer.weight_value()
        ),
        "declared_attribute": synthesizer.declared_attribute(
            "profile.favorite_color", synthesizer.string_value()
        ),
        "observed_attribute": synthesizer.observed_attribute(
            "profile.likes.insights.relatedToMicrosoft", synthesizer.total_value()
        ),
        "assigned_attribute": synthesizer.assigned_attribute(
            "profile.types", synthesizer.profile_type_value()
        ),
    }
    return {
        k: attr.asdict(v) for k, v in samples.items()
    }


class TestAgent(unittest.TestCase):

    def setUp(self):
        self.faker = create_profile_synthesizer()
        with open("./test/data/synthesizor_config.json") as fh:
            self.faker_config = json.load(fh)
        self.configured_faker = create_profile_synthesizer(**self.faker_config)

    def test_00_configured_synthesizer(self):
        print(self.configured_faker.attributes_for_single_profile())
        # TODO ... ensure that all concepts are from pool in config ...

    def test_01_app_synthesizer(self):
        """
        Tests getting schemas from a mocked endpoint ...
        :return:
        """
        for x in range(0, 100):
            print(self.faker.appId())

    def test_02_attr_values_synthesizer(self):
        """
        Tests getting schemas from a mocked endpoint ...
        :return:
        """
        for x in range(0, 100):
            print(self.faker.attribute_value())

        print(json.dumps(
            generate_attribute_value_samples(self.faker),
            indent=4,
        ))

    def test_03_attr_synthesizer(self):
        """
        Tests getting schemas from a mocked endpoint ...
        :return:
        """
        for x in range(0, 2):
            print(x, self.faker.attributes_for_single_profile(str(x)))
        print(json.dumps(
            generate_attribute_samples(self.faker),
            indent=4,
        ))

    def test_04_concept_synthesizer(self):
        f = CortexConceptsProvider(self.faker, concept_universe=[
            {
                "id": self.faker.name(),
                "context": "cortex/person",
                "title": "cortex/person"
            } for x in range(0, 100)
        ])
        for x in range(0, 2):
            print(f.concept())
        print(defaults.LIMITS_ON_COUNTS_CONCEPTS_OF_TYPE_PER_CONCEPT_SET)
        for x in range(0, 5):
            print(json.dumps(f.set_of_concepts(defaults.LIMITS_ON_COUNTS_CONCEPTS_OF_TYPE_PER_CONCEPT_SET)))

    def test_05_insights_synthesizer(self):
        print(json.dumps(self.faker.concepts_relevant_to_insight(), indent=4))
        for x in range(0, 100):
            print(self.faker.insight("1"))

    def test_06_interaction_synthesization(self):
        insight_distribution_test(self.faker)
        insight_interaction_events_test(self.faker)

    def test_07_profile_synthesization(self):
        for x in range(0, 100):
            print(self.faker.profileId())
        print(json.dumps(attr.asdict(self.faker.profile()), indent=4))

    def test_08_profile_schema_synthesization(self):
        print(self.faker.profile_schema())

    def test_09_session_synthesization(self):
        for x in range(0, 5):
            print(self.faker.sessions())

    def test_10_tenant_synthesization(self):
        for x in range(0, 5):
            print(self.faker.profileType())

    def test_building_profiles_from_synthetic_data(self):
        profileId, sessions_df, insights_df, interactions_df = self.faker.dfs_to_build_single_profile()
        attributes = (
            AttributeBuilderForInsightConsumers()
                .append_implicit_insight_interaction_attributes(insights_df, interactions_df)
                .append_implicit_type_attribute(profileId)
                .get()
        )
        for attribute in attributes:
            print(attribute)

    # @unittest.skip("skipping")
