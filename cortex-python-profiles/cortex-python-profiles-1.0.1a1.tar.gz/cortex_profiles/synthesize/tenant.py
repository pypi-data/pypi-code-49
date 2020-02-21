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

from cortex_common.utils import unique_id
from cortex_profiles.synthesize.base import BaseProviderWithDependencies


class TenantProvider(BaseProviderWithDependencies):
    """
    Tenant specific domain entities.
    """

    def __init__(self, *args, profile_universe:Optional[List[str]]=None, tenant_universe:Optional[List[str]]=None, environment_universe:Optional[List[str]]=None, **kwargs):
        super(TenantProvider, self).__init__(*args, **kwargs)
        self.profileIds = profile_universe
        self.tenantIds = tenant_universe
        self.environmentIds = environment_universe

    def dependencies(self) -> List[type]:
        return []

    # def tenantId(self) -> str:
    #     return self.fake.random.choice(self.tenantIds) if self.tenantIds else "cogscale"
    #
    # def environmentId(self) -> str:
    #     return self.fake.random.choice(self.environmentIds) if self.environmentIds else "cortex/default"

    def profileId(self) -> str:
        return self.fake.random.choice(self.profileIds) if self.profileIds else unique_id()

    def profileSchema(self) -> str:
        return "cortex/synthetic"

    def profileType(self) -> str:
        return "cortex/end-user"
