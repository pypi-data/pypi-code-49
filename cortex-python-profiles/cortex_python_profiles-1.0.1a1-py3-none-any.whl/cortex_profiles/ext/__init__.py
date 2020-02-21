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

from typing import Optional

from cortex.client import Client
from cortex.utils import get_logger

from cortex_common.types import ProfileSchema
from cortex_profiles.ext import builders, clients
from cortex_profiles.ext.rest import ProfilesRestClient

log = get_logger(__name__)

__all__ = [
    'ProfileBuilder',
    'ProfileClient'
]


class ProfileBuilder(object):
    """
    Extends the Builder Pattern for Profiles with regards to the cortex-python-builders package.
    """

    def __init__(self, client:Client, bulk_mode=False, **kwargs):
        self.client = client
        self.bulk_mode = bulk_mode
        self.kwargs = kwargs

    def profile_schema(self, bareBoneSchema:ProfileSchema) -> builders.ProfileSchemaBuilder:
        """
        Builds a schema .. starting with barebone schema ...

        :param bareBoneSchema:
        :return:
        """
        profile_client = ProfilesRestClient(self.client._url, 3, self.client._token.token)
        return builders.ProfileSchemaBuilder(bareBoneSchema, profile_client)

    def profiles(self, schemaId:Optional[str]=None) -> builders.ProfilesBuilder:
        """
        Builds one or more profiles
        Optionally, a specific schema can be specified that the profiles must adhere to ...

        :param schemaId: Can be optionally provided to enable verification on the profile building events ...
        :return:
        """
        if self.bulk_mode:
            return builders.BulkProfilesBuilder(self.client, schemaId=schemaId, **self.kwargs)
        profile_client = ProfilesRestClient(self.client._url, 3, self.client._token.token)
        return builders.ProfilesBuilder(profile_client, schemaId=schemaId)


class ProfileClient(object):
    """
    Extends the Client Pattern for Profiles with regards to the cortex-python package.
    """

    def __init__(self, client:Client):
        self.client = client

    def profile(self, profileId:str, version:int=3) -> Optional[clients.Profile]:
        profile_client = ProfilesRestClient(self.client._url, version, self.client._token.token)
        return clients.Profile.get_profile(profileId, profile_client)

    def profile_schema(self, schemaId:str, version:int=3) -> Optional[clients.ProfileSchema]:
        profile_client = ProfilesRestClient(self.client._url, version, self.client._token.token)
        return clients.ProfileSchema.get_schema(schemaId, profile_client)


if __name__ == '__main__':
    from cortex import Cortex
    import attr, json

    client = Cortex.client()
    pc = ProfileClient(client)
    profile = pc.profile("60")
    if profile is not None:
        print(json.dumps(attr.asdict(profile.latest("bwii/user")), indent=4))

    # python - m "cortex.profiles.ext.__init__" | jq '.attributes | .[] | .attributeKey' | sort | wc - l