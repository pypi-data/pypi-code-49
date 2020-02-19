#!/usr/bin/env python
# coding: utf-8

# Copyright (c) Alexey Strokach.
# Distributed under the terms of the Modified BSD License.

import pytest  # noqa

from ..example import MSAView


def test_example_creation_blank():
    w = MSAView()
    assert w.value == "Hello World"
