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

import deprecation
import pydash


@deprecation.deprecated(deprecated_in='1.0.0', details='No Longer Needed / Supported.')
def upgrade_old_attributes_into_new_ones(attributes, schema="cortex/end-user:1"):
    """
    A method to update attributes generated old profile attributes into new ones.
    This is no longer needed ...

    :param attributes:
    :param schema:
    :return:
    """
    keysToRemove = ["tenantId", "environmentId", "onLatestProfile", "commits", "attributeValue.summary"]
    upgraded_attributes = list(map(
        lambda x: pydash.set_(
            pydash.set_(
                pydash.omit(x, *keysToRemove),
                "profileSchema",
                schema
            ),
            "profileId",
            "{}".format(x["profileId"])
        ),
        attributes if isinstance(attributes, list) else [attributes]
    ))
    return upgraded_attributes if isinstance(attributes, list) else upgraded_attributes[0]


if __name__ == '__main__':

    import json
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--profile-schema', action='store', default="cortex/end-user:1")
    parser.add_argument('-s', '-i', '--old-attributes', '--old-attributes-file', action='store', required=True)
    parser.add_argument('-o', '--output-file', '--new-attributes', action='store', required=True)
    args = parser.parse_args()

    old_attrs = args.old_attributes
    new_attrs = args.output_file
    profile_schema = args.profile_schema

    with open(new_attrs, "w") as fhw:
        with open(old_attrs, "r") as fhr:
            attributes = json.load(fhr)
        json.dump(upgrade_old_attributes_into_new_ones(attributes, schema=profile_schema), fhw, indent=4)
