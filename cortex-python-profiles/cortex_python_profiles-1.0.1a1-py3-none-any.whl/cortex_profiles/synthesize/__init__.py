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

import pydash
from faker import Factory, Generator

from cortex_profiles.synthesize.apps import AppProvider
from cortex_profiles.synthesize.attribute_values import AttributeValueProvider
from cortex_profiles.synthesize.attributes import AttributeProvider
from cortex_profiles.synthesize.concepts import CortexConceptsProvider
from cortex_profiles.synthesize.insights import InsightsProvider
from cortex_profiles.synthesize.interactions import InteractionsProvider
from cortex_profiles.synthesize.profiles import ProfileProvider
from cortex_profiles.synthesize.schema import SchemaProvider
from cortex_profiles.synthesize.sessions import SessionsProvider
from cortex_profiles.synthesize.tenant import TenantProvider


def add_provider_with_args(fake:Generator, provider, args):
    """
    Helper method to functionally initialize a provider with args and add it to the faker.
    :param fake:
    :param provider:
    :param args:
    :return:
    """
    initialized_provider = provider(fake, **args)
    fake.add_provider(initialized_provider)
    return fake


def add_profile_providers(fake:Generator, all_provider_args) -> None:
    """
    Adds profiles providers to the faker factory, initializing each provider with the appropriate args.
    # How do mark the order as mattering with the providers ... or at least that providers depend on each other ...!?
        # Order doesnt matter, but before a method is called , all dependent providers must be in scope!

    :param fake:
    :return:
    """

    # Add providers with args
    add_provider_with_args(fake, TenantProvider, pydash.pick(all_provider_args, ["profile_universe", "tenant_universe"]))
    add_provider_with_args(fake, CortexConceptsProvider, pydash.pick(all_provider_args, ["concept_universe"]))
    add_provider_with_args(fake, AppProvider, pydash.pick(all_provider_args, ["app_universe"]))
    add_provider_with_args(fake, InsightsProvider, pydash.pick(all_provider_args, ["insight_types", "concept_limits_per_insight"]))
    add_provider_with_args(fake, InteractionsProvider, pydash.pick(all_provider_args, ["interactions"]))
    # Add argless providers
    fake.add_provider(SessionsProvider)
    fake.add_provider(AttributeValueProvider)
    fake.add_provider(AttributeProvider)
    fake.add_provider(ProfileProvider)
    fake.add_provider(SchemaProvider)
    return fake


def create_profile_synthesizer(**kwargs):
    """
    Create a profile synthesizor, optionally providing args
    :param kwargs:
    :return:
    """
    profile_synthesizer = Factory.create()
    profile_synthesizer = add_profile_providers(profile_synthesizer, kwargs)
    return profile_synthesizer


# TODO ... make insights.tags get a set of concepts ...
# TODO ... make concept_limits_on_insights work ...
