#
# Copyright (c) 2018, Grigoriy Kramarenko
# All rights reserved.
# This file is distributed under the BSD 3-Clause License.
#
from django.contrib.postgres.fields import jsonb
from djangokit.utils.encoders import JSONEncoder


class JSONField(jsonb.JSONField):
    """Django PostgreSQL JSONField with custom encoder."""

    def __init__(self, *args, **kwargs):
        super(JSONField, self).__init__(*args, **kwargs)
        if not self.encoder:
            self.encoder = JSONEncoder
