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

from typing import List

from cortex_profiles.synthesize import defaults
from cortex_profiles.synthesize.base import BaseProviderWithDependencies

__all__ = [
    "AppProvider",
]


class AppProvider(BaseProviderWithDependencies):
    """
    Creates synthetic applications.
    """
    def dependencies(self) -> List[type]:
        """
        Does this provider depend on other providers?
        :return:
        """
        return []

    def __init__(self, *args, app_universe:List[str]=defaults.APPS, **kwargs):
        super(AppProvider, self).__init__(*args, **kwargs)
        self.apps = app_universe

    def appId(self, random_version=False) -> str:
        """
        Generates a random appId
        :param random_version:
        :return:
        """
        if random_version:
            version = self.symanticVersion()
        else:
            version = "1.0.0"
        return "{}:{}".format(self.fake.random.choice(self.apps), version)

    def appIds(self) -> List[str]:
        """
        Generates a list of random app Ids
        :return:
        """
        version = "1.0.0"
        return ["{}:{}".format(app, version) for app in self.apps]

    def detailedAppId(self):
        """
        Generates a detailed application id.
        :return:
        """
        return "{}:{}".format(self.fake.random.choice(self.apps), self.symanticVersion())

    def symanticVersion(self):
        """
        Randomly picks a symantic version.
        :return:
        """
        return self.fake.random.choice([
            "{}.{}.{}-alpha".format(self.fake.random.randint(0, 5), self.fake.random.randint(0, 10), self.fake.random.randint(0, 10)),
            "{}.{}.{}-alpha.{}".format(self.fake.random.randint(0, 5), self.fake.random.randint(0, 10), self.fake.random.randint(0, 100), self.fake.random.randint(0, 10)),
            "{}.{}.{}-alpha.beta".format(self.fake.random.randint(0, 5), self.fake.random.randint(0, 10), self.fake.random.randint(0, 10)),
            "{}.{}.{}-beta".format(self.fake.random.randint(0, 5), self.fake.random.randint(0, 10), self.fake.random.randint(0, 10)),
            "{}.{}.{}-beta.{}".format(self.fake.random.randint(0, 5), self.fake.random.randint(0, 10), self.fake.random.randint(0, 100), self.fake.random.randint(0, 10)),
            "{}.{}.{}-rc.{}".format(self.fake.random.randint(0, 5), self.fake.random.randint(0, 10), self.fake.random.randint(0, 100), self.fake.random.randint(0, 10)),
            "{}.{}.{}".format(self.fake.random.randint(0, 5), self.fake.random.randint(0, 10), self.fake.random.randint(0, 10)),
        ])
