# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 CESNET.
#
# oarepo-heartbeat-common is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Common heartbeat checks for OArepo instances."""

from __future__ import absolute_import, print_function

from oarepo_heartbeat import liveliness_probe, readiness_probe

from oarepo_heartbeat_common.checks import check_db_health, \
    check_db_readiness, check_elasticsearch, check_redis


def connect_liveliness_checks():
    """Connect checks to a liveliness probe signal."""
    liveliness_probe.connect(check_db_health)
    liveliness_probe.connect(check_elasticsearch)
    liveliness_probe.connect(check_redis)


def connect_readiness_checks():
    """Connect checks to a readiness probe signal."""
    readiness_probe.connect(check_db_readiness)
    readiness_probe.connect(check_elasticsearch)
    readiness_probe.connect(check_redis)


class OARepoHeartbeatCommon(object):
    """oarepo-heartbeat-common extension."""

    def __init__(self, app=None):
        """Extension initialization."""
        if app:
            self.init_app(app)

    def init_app(self, app):
        """Flask application initialization."""
        app.extensions['oarepo-heartbeat-common'] = self

        connect_liveliness_checks()
        connect_readiness_checks()
