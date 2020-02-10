# -*- coding: utf-8 -*-
"""Namespace: LoadBalancing."""

import enum


@enum.unique
class Method(enum.IntFlag):
    """
    c.f. `policy/misc/load-balancing.zeek <https://docs.zeek.org/en/stable/scripts/policy/misc/load-balancing.zeek.html>`__
    """

    _ignore_ = 'Method _'
    Method = vars()

    # Apply BPF filters to each worker in a way that causes them to
    # automatically flow balance traffic between them.
    Method['AUTO_BPF'] = enum.auto()
