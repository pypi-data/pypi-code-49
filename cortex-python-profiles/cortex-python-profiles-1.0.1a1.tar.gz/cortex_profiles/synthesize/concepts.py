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

import itertools
from typing import Set, List, Mapping, Optional, Tuple

from iso3166 import countries as countries

from cortex_common.utils import get_unique_cortex_objects, group_by_key, flatten_list_recursively
from cortex_profiles.datamodel.constants import DOMAIN_CONCEPTS
from cortex_profiles.synthesize.base import BaseProviderWithDependencies
from cortex_profiles.types.insights import Link

LIMITS_ON_COUNTS_CONCEPTS_OF_TYPE_WITHIN_UNIVERSE = {
    DOMAIN_CONCEPTS.PERSON: 50,
    DOMAIN_CONCEPTS.COMPANY: 50,
    DOMAIN_CONCEPTS.COUNTRY: 50,
    DOMAIN_CONCEPTS.CURRENCY: 50,
    DOMAIN_CONCEPTS.WEBSITE: 50
}


# TODO ... for the attribute building to work right ... the title needs to be the context of the tag ... not the name ...


def get_person(fake) -> dict:
    """
    Generate a synthetic person
    :param fake:
    :return:
    """
    return {
        "id": "{} {}".format(fake.first_name(), fake.last_name()),
        "context": DOMAIN_CONCEPTS.PERSON,
        "title": DOMAIN_CONCEPTS.PERSON,
    }


def get_company(fake) -> dict:
    """
    Generate a synthetic company
    :param fake:
    :return:
    """
    return {
        "id": fake.company(),
        "context": DOMAIN_CONCEPTS.COMPANY,
        "title": DOMAIN_CONCEPTS.COMPANY,
    }


def get_country(fake) -> dict:
    """
    Generate a synthetic country
    :param fake:
    :return:
    """
    country = countries.get(fake.country_code(representation='alpha-3'))
    return {
        "id": "{}({})".format(country.alpha3, country.name),
        "context": DOMAIN_CONCEPTS.COUNTRY,
        "title": DOMAIN_CONCEPTS.COUNTRY
    }


def get_currency(fake) -> dict:
    """
    Generate a synthetic currency
    :param fake:
    :return:
    """
    currency = fake.currency()
    return {
        "id": "{}({})".format(currency[0], currency[1]),
        "context": DOMAIN_CONCEPTS.CURRENCY,
        "title": DOMAIN_CONCEPTS.CURRENCY,
    }


def get_website(fake) -> dict:
    """
    Generate a synthetic website
    :param fake:
    :return:
    """
    return {
        "id": "{0}".format(fake.url()),
        "context": DOMAIN_CONCEPTS.WEBSITE,
        "title": DOMAIN_CONCEPTS.WEBSITE
    }


class CortexConceptsProvider(BaseProviderWithDependencies):
    """
    Generates synthetic concepts that can appear in insights.
    """

    def __init__(self, *args, concept_universe:List[dict]=None, concept_limits=LIMITS_ON_COUNTS_CONCEPTS_OF_TYPE_WITHIN_UNIVERSE, **kwargs):
        super(CortexConceptsProvider, self).__init__(*args, **kwargs)
        self.concepts_to_choose_from:List[dict] = concept_universe if concept_universe else self.universe_of_concepts(concept_limits)
        self.indexed_concepts_to_choose_from = group_by_key(self.concepts_to_choose_from, lambda x: x["context"])

    def dependencies(self) -> List[type]:
        """
        What providers does this provider depend on?
        :return:
        """
        return []

    def universe_of_concepts(self, limits) -> List[dict]:
        """
        This creates a universe of concepts indexed by the concept type where concepts are unique.
        :return:
        """
        concepts = [
            get_unique_cortex_objects(lambda: get_person(self.fake), limits[DOMAIN_CONCEPTS.PERSON]),
            get_unique_cortex_objects(lambda: get_company(self.fake), limits[DOMAIN_CONCEPTS.COMPANY]),
            get_unique_cortex_objects(lambda: get_country(self.fake), limits[DOMAIN_CONCEPTS.COUNTRY]),
            get_unique_cortex_objects(lambda: get_currency(self.fake), limits[DOMAIN_CONCEPTS.CURRENCY]),
            get_unique_cortex_objects(lambda: get_website(self.fake), limits[DOMAIN_CONCEPTS.WEBSITE])
        ]
        return flatten_list_recursively(concepts)

    def set_of_concepts(self, concept_limits:Mapping[str,Mapping[str, int]]) -> Set[Link]:
        """
        Its more likely that concept limits will be a default dict ... with like 1 ...
        Its more likely the universe will be a list of all the different options ...
        :param concept_limits:
        :return:
        """
        all_concepts = set(list(self.indexed_concepts_to_choose_from) + list(concept_limits))

        min_number_of_choosable_concepts_per_type = {
            concept_type: min(
                concept_limits.get(concept_type, {"min": 0})["min"],
                len(self.indexed_concepts_to_choose_from.get(concept_type, []))
            )
            for concept_type in all_concepts
        }
        max_number_of_choosable_concepts_per_type = {
            concept_type: min(
                concept_limits.get(concept_type, {"max": 0})["max"],
                len(self.indexed_concepts_to_choose_from.get(concept_type, []))
            )
            for concept_type in all_concepts
        }

        number_of_concepts_chosen_per_type = {
            concept_type: self.fake.random.randint(
                min_number_of_choosable_concepts_per_type[concept_type],
                max_number_of_choosable_concepts_per_type[concept_type]
            )
            for concept_type in all_concepts
        }
        concept_choices = [
            list(self.fake.random.choice(list(
                itertools.combinations(
                    concepts,
                    number_of_concepts_chosen_per_type[concept_type]
                )
            )))
            for concept_type, concepts in self.indexed_concepts_to_choose_from.items()
        ]
        return flatten_list_recursively(concept_choices, remove_empty_lists=True)

    def _concept(self, context) -> Optional[Link]:
        """
        Helper to generate a synthetic concept.
        :param context:
        :return:
        """
        concept = self.fake.random.choice(self.indexed_concepts_to_choose_from.get(context)) if context in self.indexed_concepts_to_choose_from else None
        return Link(**concept) if concept else None  #type:ignore

    def cortex_person(self) -> Optional[Link]:
        """
        Generate a synthetic person
        :return:
        """
        return self._concept(DOMAIN_CONCEPTS.PERSON)

    def cortex_company(self) -> Optional[Link]:
        """
        Generate a synthetic company
        :return:
        """
        return self._concept(DOMAIN_CONCEPTS.COMPANY)

    def cortex_country(self) -> Optional[Link]:
        """
        Generate a synthetic country
        :return:
        """
        return self._concept(DOMAIN_CONCEPTS.COUNTRY)

    def cortex_currency(self) -> Optional[Link]:
        """
        Generate a synthetic currency
        :return:
        """
        return self._concept(DOMAIN_CONCEPTS.CURRENCY)

    def cortex_website(self) -> Optional[Link]:
        """
        Generate a synthetic website
        :return:
        """
        return self._concept(DOMAIN_CONCEPTS.WEBSITE)

    def concept(self) -> Link:
        """
        Generate a synthetic concept
        :return:
        """
        returnVal = None
        while returnVal is None:
            random_category = self.fake.random.choice(list(self.indexed_concepts_to_choose_from))
            returnVal = self._concept(random_category)
        return returnVal
