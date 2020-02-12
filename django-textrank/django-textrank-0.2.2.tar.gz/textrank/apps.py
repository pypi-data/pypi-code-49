#
# Copyright (c) 2019, Grigoriy Kramarenko
# All rights reserved.
# This file is distributed under the BSD 3-Clause License.
#
from django.apps import AppConfig
from djangokit.utils.apps import DependencesMixin


class DefaultConfig(DependencesMixin, AppConfig):
    name = 'textrank'
    dependences = [
        'django.contrib.auth',
        'django.contrib.sessions',
        'djangokit',
    ]
