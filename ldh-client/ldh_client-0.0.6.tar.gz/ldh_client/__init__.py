#!/usr/bin/env python3
# Copyright 2017-2020 Purism SPC
# SPDX-License-Identifier: AGPL-3.0-or-later

import pkg_resources
import ruamel.yaml as yaml

default_yaml = pkg_resources.resource_string(
    __name__, "../data/default.strict.yaml"
).decode("utf-8")

DEFAULT = yaml.safe_load(default_yaml)
