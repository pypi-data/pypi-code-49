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


"""Decorators for test units"""

import os
import shutil

import nose
import docker


# ----------------------------------------------------------


# Images used for docker-enabled tests within this and other BEAT packages
DOCKER_TEST_IMAGES = {
    "docker.idiap.ch/beat/beat.env.system.python": "1.3.0r5",
    "docker.idiap.ch/beat/beat.env.db.examples": "1.4.0r5",
    "docker.idiap.ch/beat/beat.env.cxx": "2.0.0r1",
    "docker.idiap.ch/beat/beat.env.client": "2.0.0r1",
}


def pull_docker_test_images():
    """To be called when you need to set up tests using ``DOCKER_TEST_IMAGES``

    This function will pull images that are not locally available yet
    This technique prevents errors if docker.idiap.ch is not available,
    e.g. when running outside the Idiap network
    """

    import docker

    client = docker.from_env()

    for image, tag in DOCKER_TEST_IMAGES.items():
        has_image = False

        for installed_image in client.images.list():
            for installed_tag in installed_image.tags:
                if installed_tag == ("%s:%s" % (image, tag)):
                    has_image = True

        if not has_image:  # must pull (network connection required)

            token = os.environ.get("CI_BUILD_TOKEN")
            args = (image, tag)
            kwargs = {}
            if token is not None:  # running on CI, setup
                auth_config = dict(username="gitlab-ci-token", password=token)
                kwargs["auth_config"] = auth_config
            client.images.pull(*args, **kwargs)


# ----------------------------------------------------------


def slow(t):
    """
    Label a test as 'slow'.

    The exact definition of a slow test is obviously both subjective and
    hardware-dependent, but in general any individual test that requires more
    than a second or two should be labeled as slow (the whole suite consists of
    thousands of tests, so even a second is significant).

    Parameters
    ----------
    t : callable
        The test to label as slow.

    Returns
    -------
    t : callable
        The decorated test `t`.

    Examples
    --------
    The `numpy.testing` module includes ``import decorators as dec``.
    A test can be decorated as slow like this::

      from numpy.testing import *

      @dec.slow
      def test_big(self):
        print('Big, slow test')

    """

    t.slow = True
    return t


# ----------------------------------------------------------


def skipif(skip_condition, msg=None):
    """
    Make function raise SkipTest exception if a given condition is true.

    If the condition is a callable, it is used at runtime to dynamically
    make the decision. This is useful for tests that may require costly
    imports, to delay the cost until the test suite is actually executed.

    Parameters
    ----------
    skip_condition : bool or callable
        Flag to determine whether to skip the decorated test.
    msg : str, optional
        Message to give on raising a SkipTest exception. Default is None.

    Returns
    -------
    decorator : function
        Decorator which, when applied to a function, causes SkipTest
        to be raised when `skip_condition` is True, and the function
        to be called normally otherwise.

    Notes
    -----
    The decorator itself is decorated with the ``nose.tools.make_decorator``
    function in order to transmit function name, and various other metadata.

    """

    class SkipCallable:
        """Helper class to handle both callable and boolean conditions"""

        def __init__(self, skip_condition):
            self.skip_condition = skip_condition

        def __call__(self):
            if callable(self.skip_condition):
                return skip_condition()
            else:
                return self.skip_condition

    def skip_decorator(f):

        # Allow for both boolean or callable skip conditions.
        skip_val = SkipCallable(skip_condition)

        # We need to define *two* skippers because Python doesn't allow both
        # return with value and yield inside the same function.
        def skipper_func(*args, **kwargs):
            """Skipper for normal test functions."""
            if skip_val():
                raise nose.SkipTest(msg)
            else:
                return f(*args, **kwargs)

        def skipper_gen(*args, **kwargs):
            """Skipper for test generators."""
            if skip_val():
                raise nose.SkipTest(msg)
            else:
                for x in f(*args, **kwargs):
                    yield x

        # Choose the right skipper to use when building the actual decorator.
        if nose.util.isgenerator(f):
            skipper = skipper_gen
        else:
            skipper = skipper_func

        return nose.tools.make_decorator(f)(skipper)

    return skip_decorator


# ----------------------------------------------------------


def cleanup():

    from . import prefix, tmp_prefix

    cache_path = os.path.join(prefix, "cache")
    if os.path.exists(cache_path):
        shutil.rmtree(cache_path)

    beat_path = os.path.join(prefix, ".beat")
    if os.path.exists(beat_path):
        shutil.rmtree(beat_path)

    if os.path.exists(tmp_prefix):
        os.makedirs(tmp_prefix + ".new")
        shutil.copymode(tmp_prefix, tmp_prefix + ".new")
        shutil.rmtree(tmp_prefix)
        shutil.move(tmp_prefix + ".new", tmp_prefix)


# ----------------------------------------------------------


def create_network(network_name):
    """ Create a docker network with the given name"""

    ipam_pool = docker.types.IPAMPool(subnet="193.169.0.0/24", gateway="193.169.0.254")

    ipam_config = docker.types.IPAMConfig(pool_configs=[ipam_pool])

    client = docker.from_env()
    network = client.networks.create(network_name, driver="bridge", ipam=ipam_config)
    return network
