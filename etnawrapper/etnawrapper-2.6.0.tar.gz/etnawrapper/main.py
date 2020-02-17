#!/usr/bin/env python
"""
Period check of ETNA's services
"""
from dataclasses import dataclass


@dataclass
class Target:
    url: str
    timeout: int
    auth: bool


def
