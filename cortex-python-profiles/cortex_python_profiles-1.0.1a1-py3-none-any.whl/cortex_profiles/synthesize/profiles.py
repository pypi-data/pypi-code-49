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

from typing import List, Optional

from cortex_common.types import Profile
from cortex_common.utils import unique_id, utc_timestamp
from cortex_profiles.synthesize.attributes import AttributeProvider
from cortex_profiles.synthesize.base import BaseProviderWithDependencies
from cortex_profiles.synthesize.tenant import TenantProvider


class ProfileProvider(BaseProviderWithDependencies):
    """
    Creates synthetic profiles
    """

    def __init__(self, *args, **kwargs):
        super(ProfileProvider, self).__init__(*args, **kwargs)

    def dependencies(self) -> List[type]:
        """
        What providers does this provider depend on?
        :return:
        """
        return [
            TenantProvider,
            AttributeProvider
        ]

    def profile(self, profileId:Optional[str]=None, max_attributes:int=3) -> Profile:
        """
        Generate a synthetic profile with attributes.
        :param profileId:
        :param max_attributes:
        :return:
        """
        return Profile(  #type:ignore
            profileId=self.fake.profileId() if not profileId else profileId,
            createdAt=utc_timestamp(),
            profileSchema=self.fake.profileSchema(),
            attributes = self.fake.attributes(limit=self.fake.random.randint(1, max_attributes))
        )

    # TODO ...
    # def profile_with_all_attribute_variations(self, profileId:Optional[str]=None) -> Profile:
