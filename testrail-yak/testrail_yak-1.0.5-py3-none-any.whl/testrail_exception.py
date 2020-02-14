#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .testrail import APIError


# TestRail
class TestRailException(APIError):
    pass


class ValidationException(ValueError):
    pass
