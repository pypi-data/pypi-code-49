#
# Copyright (c) 2019, Grigoriy Kramarenko
# All rights reserved.
# This file is distributed under the BSD 3-Clause License.
#
from django.contrib.postgres.forms import jsonb
from django.utils.translation import gettext_lazy as _
from djangokit.utils.encoders import dump_to_json


class JSONField(jsonb.JSONField):
    default_error_messages = {
        'invalid': _('Введите правильный JSON.'),
    }

    def prepare_value(self, value):
        if isinstance(value, str):
            return value
        kwargs = {'indent': 2, 'ensure_ascii': False}
        return dump_to_json(value, **kwargs)
