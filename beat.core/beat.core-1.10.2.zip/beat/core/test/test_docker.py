#!/usr/bin/env python
# vim: set fileencoding=utf-8 :

###################################################################################
#                                                                                 #
# Copyright (c) 2019 Idiap Research Institute, http://www.idiap.ch/               #
# Contact: beat.support@idiap.ch                                                  #
#                                                                                 #
# Redistribution and use in source and binary forms, with or without              #
# modification, are permitted provided that the following conditions are met:     #
#                                                                                 #
# 1. Redistributions of source code must retain the above copyright notice, this  #
# list of conditions and the following disclaimer.                                #
#                                                                                 #
# 2. Redistributions in binary form must reproduce the above copyright notice,    #
# this list of conditions and the following disclaimer in the documentation       #
# and/or other materials provided with the distribution.                          #
#                                                                                 #
# 3. Neither the name of the copyright holder nor the names of its contributors   #
# may be used to endorse or promote products derived from this software without   #
# specific prior written permission.                                              #
#                                                                                 #
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND #
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED   #
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE          #
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE    #
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL      #
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR      #
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER      #
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,   #
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE   #
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.            #
#                                                                                 #
###################################################################################


"""Asynchronous process I/O with the Subprocess module"""

import os
import time
import tempfile
import unittest
import pkg_resources

from tempfile import TemporaryDirectory

from ..dock import Host

from . import tmp_prefix
from .utils import slow
from .utils import skipif

from . import network_name
from . import DOCKER_NETWORK_TEST_ENABLED


class NoDiscoveryTests(unittest.TestCase):
    """Test cases that don't require the discovery of database and runtime
    environments.
    """

    @classmethod
    def setUpClass(cls):
        cls.host = Host(raise_on_errors=False, discover=False)

    @classmethod
    def tearDownClass(cls):
        cls.host.teardown()

    def tearDown(self):
        self.host.teardown()
        self.assertFalse(self.host.containers)  # All containers are gone


class NetworkTest(NoDiscoveryTests):
    @slow
    @skipif(not DOCKER_NETWORK_TEST_ENABLED, "Network test disabled")
    def test_network(self):
        string = "hello world"
        container = self.host.create_container("debian:8.4", ["echo", string])
        container.network_name = network_name

        try:
            self.host.start(container)
            status = self.host.wait(container)
        except Exception:
            from . import network

            network.remove()
            raise

        self.assertEqual(status, 0)
        self.assertEqual(self.host.logs(container), string + "\n")

    @slow
    @skipif(not DOCKER_NETWORK_TEST_ENABLED, "Network test disabled")
    def test_non_existing_network(self):

        string = "hello world"
        network_name = "beat.core.fake"
        container = self.host.create_container("debian:8.4", ["echo", string])
        container.network_name = network_name

        try:
            self.host.start(container)
        except RuntimeError as e:
            self.assertTrue(str(e).find("network %s not found" % network_name) >= 0)


class UserTest(NoDiscoveryTests):
    @slow
    def test_user(self):
        """Test that the uid property is correctly used.
        """

        container = self.host.create_container("debian:8.4", ["id"])
        container.uid = 10000

        self.host.start(container)
        status = self.host.wait(container)

        self.assertEqual(status, 0)
        self.assertTrue(
            self.host.logs(container).startswith(
                "uid={0} gid={0}".format(container.uid)
            )
        )


class EnvironmentVariableTest(NoDiscoveryTests):
    @slow
    def test_environment_variable(self):
        """Test that the uid property is correctly used.
        """

        container = self.host.create_container("debian:8.4", ["env"])
        container.add_environment_variable("DOCKER_TEST", "good")

        self.host.start(container)
        status = self.host.wait(container)

        self.assertEqual(status, 0)
        self.assertTrue("DOCKER_TEST=good" in self.host.logs(container))


class WorkdirTest(NoDiscoveryTests):
    @slow
    def test_workdir(self):
        """Test that the workdir property is correctly used.
        """

        with TemporaryDirectory() as tmp_folder:
            test_file = "test.txt"
            container = self.host.create_container(
                "debian:8.4", ["cp", "/etc/debian_version", test_file]
            )
            container.add_volume(tmp_folder, "/test_workdir", read_only=False)
            container.set_workdir("/test_workdir")

            self.host.start(container)
            status = self.host.wait(container)
            if status != 0:
                print(self.host.logs(container))

            self.assertEqual(status, 0)

            with open(os.path.join(tmp_folder, test_file), "rt") as file:
                content = file.read()
                self.assertEqual(content, "8.4\n")


class EntrypointTest(NoDiscoveryTests):
    @slow
    def test_entrypoint(self):
        """Test that the entrypoint property is correctly used.
        """

        container = self.host.create_container("debian:8.4", ["42"])
        container.set_entrypoint("echo")

        self.host.start(container)
        status = self.host.wait(container)
        logs = self.host.logs(container)
        if status != 0:
            print(logs)

        self.assertEqual(status, 0)
        self.assertEqual(logs, "42\n")


class AsyncTest(NoDiscoveryTests):
    @slow
    def test_echo(self):

        string = "hello, world"

        container = self.host.create_container("debian:8.4", ["echo", string])
        self.host.start(container)
        status = self.host.wait(container)

        self.assertEqual(status, 0)
        self.assertEqual(self.host.logs(container), string + "\n")

    @slow
    def test_non_existing(self):

        container = self.host.create_container("debian:8.4", ["sdfsdfdsf329909092"])

        try:
            self.host.start(container)
        except Exception as e:
            self.assertTrue(str(e).find("Failed to create the container") >= 0)

        self.assertFalse(self.host.containers)  # All containers are gone

    @slow
    def test_timeout(self):

        sleep_for = 100  # seconds

        container = self.host.create_container("debian:8.4", ["sleep", str(sleep_for)])
        self.host.start(container)

        retval = self.host.wait(container, timeout=0.5)
        self.assertTrue(retval is None)

        self.host.kill(container)

        retval = self.host.wait(container)

        self.assertEqual(self.host.status(container), "exited")
        self.assertEqual(retval, 137)
        self.assertEqual(self.host.logs(container), "")

    @slow
    def test_does_not_timeout(self):

        sleep_for = 0.5  # seconds

        container = self.host.create_container("debian:8.4", ["sleep", str(sleep_for)])
        self.host.start(container)

        status = self.host.wait(container, timeout=5)  # Should not timeout

        self.assertEqual(self.host.status(container), "exited")
        self.assertEqual(status, 0)
        self.assertEqual(self.host.logs(container), "")


class AsyncWithEnvironmentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.host = Host(raise_on_errors=False)
        cls.test_environment = cls.host.full_environment_name("Python 2.7")

    @classmethod
    def tearDownClass(cls):
        cls.host.teardown()

    def tearDown(self):
        self.host.teardown()
        self.assertFalse(self.host.containers)  # All containers are gone

    @slow
    def test_memory_limit(self):

        cmd = [
            "python",
            "-c",
            "; ".join(
                [
                    "print('Before')",
                    "import sys; sys.stdout.flush()",
                    "d = '0' * (40 * 1024 * 1024)",
                    "import time; time.sleep(5)",
                    "print('After')",
                ]
            ),
        ]

        container = self.host.create_container(self.test_environment, cmd)
        # The amount of memory in megabytes should be greater than whatever
        # the docker process is started with (see:
        # https://unix.stackexchange.com/questions/412040/cgroups-memory-limit-write-error-device-or-resource-busy)
        # If you start seeing EBUSY (device or resource busy errors) from
        # docker, then try increasing a bit this value such that it still
        # triggers the memory allocation error for the array defined above.
        self.host.start(container, virtual_memory_in_megabytes=20)

        time.sleep(2)

        self.host.statistics(container)

        status = self.host.wait(container)

        self.assertEqual(self.host.status(container), "exited")
        self.assertEqual(status, 137)
        self.assertEqual(self.host.logs(container).strip(), "Before")

    @slow
    def test_memory_limit2(self):

        cmd = [
            "python",
            "-c",
            "; ".join(
                [
                    "print('Before')",
                    "import sys; sys.stdout.flush()",
                    "d = '0' * (10 * 1024 * 1024)",
                    "import time; time.sleep(5)",
                    "print('After')",
                ]
            ),
        ]

        container = self.host.create_container(self.test_environment, cmd)
        self.host.start(container, virtual_memory_in_megabytes=100)

        time.sleep(2)

        stats = self.host.statistics(container)

        status = self.host.wait(container)

        self.assertTrue(
            stats["memory"]["percent"] > 10,
            ("Memory check failed, " "%d%% <= 10%%" % stats["memory"]["percent"]),
        )

        self.assertTrue(
            stats["memory"]["percent"] < 20,
            ("Memory check failed, " "%d%% >= 15%%" % stats["memory"]["percent"]),
        )

        self.assertEqual(self.host.status(container), "exited")
        self.assertEqual(status, 0)
        self.assertEqual(self.host.logs(container).strip(), "Before\nAfter")

    def _run_cpulimit(self, processes, max_cpu_percent, sleep_time):

        tmp_folder = tempfile.gettempdir()
        program = pkg_resources.resource_filename(__name__, "cpu_stress.py")
        dst_name = os.path.join(tmp_folder, os.path.basename(program))

        container = self.host.create_container(
            self.test_environment, ["python", dst_name, str(processes)]
        )

        container.add_volume(program, os.path.join(tmp_folder, "cpu_stress.py"))

        self.host.start(container, max_cpu_percent=max_cpu_percent)

        time.sleep(sleep_time)

        stats = self.host.statistics(container)

        self.assertEqual(self.host.status(container), "running")

        percent = stats["cpu"]["percent"]
        self.assertTrue(
            percent < (1.1 * max_cpu_percent),
            (
                "%.2f%% is more than 20%% off the expected ceiling at %d%%!"
                % (percent, max_cpu_percent)
            ),
        )

        # make sure nothing is there anymore
        self.host.kill(container)
        self.assertEqual(self.host.wait(container), 137)

    @slow
    def test_cpulimit_at_20percent(self):
        # runs 1 process that should consume at most 20% of the host CPU
        self._run_cpulimit(1, 20, 3)

    @slow
    def test_cpulimit_at_100percent(self):
        # runs 4 processes that should consume 50% of the host CPU
        self._run_cpulimit(4, 100, 3)


class HostTest(unittest.TestCase):
    def setUp(self):
        Host.images_cache = {}

    @slow
    def test_images_cache(self):
        self.assertEqual(len(Host.images_cache), 0)

        # Might take some time
        start = time.time()

        host = Host(raise_on_errors=False)
        host.teardown()

        stop = time.time()

        nb_images = len(Host.images_cache)
        self.assertTrue(nb_images > 0)

        self.assertTrue(stop - start > 2.0)

        # Should be instantaneous
        start = time.time()

        host = Host(raise_on_errors=False)
        host.teardown()

        stop = time.time()

        self.assertEqual(len(Host.images_cache), nb_images)

        self.assertTrue(stop - start < 1.0)

    @slow
    def test_images_cache_file(self):
        self.assertEqual(len(Host.images_cache), 0)

        # Might take some time
        start = time.time()

        host = Host(
            images_cache=os.path.join(tmp_prefix, "images_cache.json"),
            raise_on_errors=False,
        )
        host.teardown()

        stop = time.time()

        nb_images = len(Host.images_cache)
        self.assertTrue(nb_images > 0)

        self.assertTrue(stop - start > 2.0)

        Host.images_cache = {}

        # Should be instantaneous
        start = time.time()

        host = Host(
            images_cache=os.path.join(tmp_prefix, "images_cache.json"),
            raise_on_errors=False,
        )
        host.teardown()

        stop = time.time()

        self.assertEqual(len(Host.images_cache), nb_images)

        self.assertTrue(stop - start < 1.0)
