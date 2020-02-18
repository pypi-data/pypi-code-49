# Copyright 2009-2020 Canonical Ltd.  This software is licensed under the
# GNU General Public License version 3.

import errno
import os
import signal

from fixtures import MockPatch
from testtools import TestCase

from txfixtures.osutils import (
    process_exists,
    two_stage_kill,
    )


class TestProcessExists(TestCase):

    def test_with_process_running(self):
        pid = os.getpid()
        self.assertTrue(process_exists(pid))

    def test_with_process_not_running(self):
        exception = OSError()
        exception.errno = errno.ESRCH
        self.useFixture(MockPatch('os.kill', side_effect=exception))
        self.assertFalse(process_exists(123))

    def test_with_unknown_error(self):
        exception = OSError()
        exception.errno = errno.ENOMEM
        self.useFixture(MockPatch('os.kill', side_effect=exception))
        self.assertRaises(OSError, process_exists, 123)


class TestTwoStageKill(TestCase):

    def test_already_dead(self):
        exception = OSError()
        exception.errno = errno.ESRCH
        kill_results = iter([None, exception])
        kill = self.useFixture(
            MockPatch('os.kill', side_effect=kill_results)).mock
        sleep = self.useFixture(MockPatch('time.sleep')).mock
        two_stage_kill(123)
        self.assertEqual(2, kill.call_count)
        kill.assert_has_calls([((123, signal.SIGTERM), {}), ((123, 0), {})])
        sleep.assert_not_called()

    def test_dies_immediately(self):
        exception = OSError()
        exception.errno = errno.ESRCH
        kill_results = iter([None, None, exception])
        kill = self.useFixture(
            MockPatch('os.kill', side_effect=kill_results)).mock
        sleep = self.useFixture(MockPatch('time.sleep')).mock
        two_stage_kill(123)
        self.assertEqual(3, kill.call_count)
        kill.assert_has_calls(
            [((123, signal.SIGTERM), {})] + [((123, 0), {})] * 2)
        sleep.assert_called_once_with(0.1)

    def test_dies_slowly(self):
        exception = OSError()
        exception.errno = errno.ESRCH
        kill_results = iter([None] * 50 + [exception])
        kill = self.useFixture(
            MockPatch('os.kill', side_effect=kill_results)).mock
        sleep = self.useFixture(MockPatch('time.sleep')).mock
        two_stage_kill(123)
        self.assertEqual(51, kill.call_count)
        kill.assert_has_calls(
            [((123, signal.SIGTERM), {})] + [((123, 0), {})] * 50)
        self.assertEqual(49, sleep.call_count)
        sleep.assert_has_calls([((0.1,), {})] * 49)

    def test_requires_sigkill(self):
        exception = OSError()
        exception.errno = errno.ESRCH
        kill_results = iter([None] * 52)
        kill = self.useFixture(
            MockPatch('os.kill', side_effect=kill_results)).mock
        sleep = self.useFixture(MockPatch('time.sleep')).mock
        two_stage_kill(123)
        self.assertEqual(52, kill.call_count)
        kill.assert_has_calls(
            [((123, signal.SIGTERM), {})] +
            [((123, 0), {})] * 50 +
            [((123, signal.SIGKILL), {})])
        self.assertEqual(50, sleep.call_count)
        sleep.assert_has_calls([((0.1,), {})] * 50)
