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

# Basic setup for slow tests

import os
import sys
import subprocess as sp  # nosec
import shutil
import tempfile
import pkg_resources
import logging

if sys.platform == "darwin":
    tmp_prefix = tempfile.mkdtemp(
        prefix=__name__, suffix=".tmpdir", dir="/tmp"  # nosec
    )
    prefix_folder = tempfile.mkdtemp(
        prefix=__name__, suffix=".prefix", dir="/tmp"  # nosec
    )
else:
    tmp_prefix = tempfile.mkdtemp(prefix=__name__, suffix=".tmpdir")
    prefix_folder = tempfile.mkdtemp(prefix=__name__, suffix=".prefix")


prefix = os.path.join(prefix_folder, "prefix")

DOCKER_NETWORK_TEST_ENABLED = (
    os.environ.get("DOCKER_NETWORK_TEST_ENABLED", False) == "True"
)
network_name = os.environ.get("DOCKER_TEST_NETWORK", "beat_core_test_network")
global network
network = None

# Setup the logging system
VERBOSE_TEST_LOGGING = os.environ.get("VERBOSE_TEST_LOGGING", False) == "True"
VERBOSE_BCP_LOGGING = os.environ.get("VERBOSE_BCP_LOGGING", False) == "True"

if VERBOSE_TEST_LOGGING:
    formatter = logging.Formatter(
        fmt="[%(asctime)s - TESTS - " "%(name)s] %(levelname)s: %(message)s",
        datefmt="%d/%b/%Y %H:%M:%S",
    )

    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    for logger_name in ["beat.core", "beat.backend.python"]:
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.DEBUG)
        logger.addHandler(handler)


def setup_package():
    prefixes = [
        pkg_resources.resource_filename("beat.backend.python.test", "prefix"),
        pkg_resources.resource_filename("beat.core.test", "prefix"),
    ]

    for path in prefixes:
        sp.check_call(["rsync", "-arz", path, prefix_folder])

    if DOCKER_NETWORK_TEST_ENABLED:
        import docker

        global network

        client = docker.from_env()
        try:
            network = client.networks.get(network_name)
        except docker.errors.NotFound:
            subnet = os.environ.get("DOCKER_TEST_SUBNET", "193.169.0.0/24")
            gateway = os.environ.get("DOCKER_TEST_GATEWAY", "193.169.0.254")
            ipam_pool = docker.types.IPAMPool(subnet=subnet, gateway=gateway)

            ipam_config = docker.types.IPAMConfig(pool_configs=[ipam_pool])

            network = client.networks.create(
                network_name, driver="bridge", ipam=ipam_config
            )


def teardown_package():
    if os.path.exists(tmp_prefix):
        shutil.rmtree(tmp_prefix)

    shutil.rmtree(prefix_folder)

    if DOCKER_NETWORK_TEST_ENABLED:
        global network
        if network:
            network.remove()
