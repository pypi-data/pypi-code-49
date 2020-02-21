# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 CESNET.
#
# oarepo-heartbeat-common is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Common heartbeat checks for OArepo instances."""

from __future__ import absolute_import, print_function

from .ext import OARepoHeartbeatCommon
from .version import __version__

__all__ = ('__version__', 'OARepoHeartbeatCommon')
