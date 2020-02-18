# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

import json
from pkg_resources import resource_string

profile_payload_template = json.loads(
    resource_string(__name__, "data/mms_profile_payload_template.json").decode("ascii")
)

old_profile_payload_template = json.loads(
    resource_string(__name__, "data/old_mms_profile_payload_template.json").decode(
        "ascii"
    )
)
