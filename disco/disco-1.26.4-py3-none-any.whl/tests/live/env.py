#  Copyright (c) 2019 Samsung, Inc. and its affiliates.
#
#  This source code is licensed under the RESTRICTED license found in the
#  LICENSE file in the root directory of this source tree.

import os
from disco.core import constants

skip = 'DISCO_LIVE_TESTS' not in os.environ
reason = ('Please pass an environment variable DISCO_LIVE_TESTS if you want'
          ' to run the integration tests on a live environment. Don\'t forget'
          ' to set environment variables for connecting to Dis.co servers')

LIVE_TESTS_TIMEOUT_SECONDS = 9 * constants.MINUTE
LIVE_TESTS_JOB_START_WAIT_TIME = 1 * constants.MINUTE
LIVE_TESTS_TASKS_RUNNING_WAIT_TIME = 3 * constants.MINUTE
