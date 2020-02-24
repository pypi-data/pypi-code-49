# -*- coding: utf-8 -*-
import pytest


@pytest.fixture(params=[82, 86], ids=['82', '86'])
def folders(request):
    return request.param


@pytest.fixture
def folder():
    return 86
