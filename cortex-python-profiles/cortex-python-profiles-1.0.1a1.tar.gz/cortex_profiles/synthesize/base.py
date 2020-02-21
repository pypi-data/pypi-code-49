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

from itertools import combinations
from typing import List, Callable

from faker.providers import BaseProvider


class BaseProviderWithDependencies(BaseProvider):
    """
    Base Provider inherited by other providers
    """

    def validate_dependencies(self):
        """
        Base validation for providers, ensuring their deps have been met!
        :return:
        """
        dependencies = self.dependencies()
        available_providers = list(map(lambda x: type(x), self.fake.providers))
        missing_providers = [dep for dep in dependencies if dep not in available_providers]
        assert not missing_providers, "Faker missing the following dependencies [{}] for [{}]".format(missing_providers, type(self).__name__)

    def __init__(self, *args, **kwargs):
        """
        Base init method for providers, validating deps ...
        :param args:
        :param kwargs:
        """
        super(BaseProviderWithDependencies, self).__init__(*args, **kwargs)
        self.fake = args[0]
        self.validate_dependencies()

    def random_subset_of_list(self, l:List):
        """
        Helper method to get random subset of list
        :param l:
        :return:
        """
        if not l:
            return l
        return list(self.fake.random.choice(
            list(combinations(
                l, self.fake.random.randint(0, len(l))
            ))
        )) if l else l

    def range(self, min=0, max=100):
        """
        Synthesize a range
        :param min:
        :param max:
        :return:
        """
        return [x for x in range(min, self.fake.random.randint(1, max))]

    def generate_up_to_x_uniq_elements(self, generator:Callable, x:int=10):
        """
        Generate up to x synthetic elements from the provided generator method.
        :param generator:
        :param x:
        :return:
        """
        return self.random_subset_of_list(
            list(set(list(
                map(lambda e: e(), [generator] * x)
            )))
        )