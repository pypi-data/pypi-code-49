#  Copyright (c) 2019 Samsung, Inc. and its affiliates.
#
#  This source code is licensed under the RESTRICTED license found in the
#  LICENSE file in the root directory of this source tree.

import warnings

import pytest


@pytest.fixture(scope='session', autouse=True)
def ignore_deprecation_warning(request):
    warnings.filterwarnings('ignore', category=DeprecationWarning)
