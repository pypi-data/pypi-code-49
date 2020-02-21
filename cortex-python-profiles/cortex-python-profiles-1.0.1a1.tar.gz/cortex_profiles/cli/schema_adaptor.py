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

from cortex_common.utils import head


def upgrade_old_profile_schema(old_schema:dict) -> dict:
    """
    Transforms an old profile schema into a new one ...
    :param old_schema:
    :return:
    """


    keysToRemove = ["tenantId", "environmentId", "id", "createdAt", "version", ]
    remapped_schema = pydash.rename_keys(
        pydash.omit(
            # Remap tags ...
            pydash.set_(
                # Remap taxonomy ... and add label ...
                pydash.set_(
                    # Remap groups ...set group id as name ...
                    pydash.set_(
                        old_schema,
                        "groups",
                        list(map(
                            lambda group: pydash.omit(pydash.rename_keys(group, {"id": "name"}), "version"),
                            old_schema["groups"]
                        ))
                    ),
                    "taxonomy",
                    list(map(
                        lambda tax: pydash.omit(
                            pydash.set_(tax, "parent", head(tax["parents"])) if head(tax["parents"]) else tax,
                            "parents", "children", "attributes"
                        )
                        ,
                        old_schema["taxonomy"]
                    ))
                ),
                "tags",
                list(map(
                    lambda tag: pydash.rename_keys(pydash.omit(tag, "group", "version"), {"id": "name"}),
                    old_schema["tags"]
                ))
            ),
            *keysToRemove
        ),
        {
            "groups": "facets",
            "tags": "attributeTags",
        }
    )
    return remapped_schema


if __name__ == '__main__':
    import json
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '-i', '--old-schema', '--old-schema-file', action='store', required=True)
    parser.add_argument('-o', '--output-file', '--new-schema', action='store', required=True)
    args = parser.parse_args()

    old_schema_file = args.old_schema
    new_schema_file = args.output_file

    with open(new_schema_file, "w") as fhw:
        with open(old_schema_file, "r") as fhr:
            old_schema = json.load(fhr)
        json.dump(
            upgrade_old_profile_schema(old_schema),
            fhw,
            indent=4
        )
