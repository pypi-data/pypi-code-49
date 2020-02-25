# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 CESNET.
#
# oarepo-heartbeat-common is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Common heartbeat checks for OArepo instances."""
from invenio_rest.errors import RESTException


class DatabaseUninitialized(RESTException):
    """Database not yet initialized error."""

    code = 500
    description = 'Database is uninitialized.'


class DatabaseUnhealthy(RESTException):
    """Database not healthy error."""

    code = 500
    description = 'Database is unhealthy.'
