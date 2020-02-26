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


"""
=====
utils
=====

Helper methods

Forward imports from :py:mod:`beat.backend.python.utils`
"""

import six
import sys
import tempfile
import socket
import contextlib
import string
import random
import logging

from beat.backend.python.utils import *  # noqa: F401, F403


# ----------------------------------------------------------


def temporary_directory(prefix="beat_"):
    """Generates a temporary directory"""

    if sys.platform == "darwin":
        return tempfile.mkdtemp(prefix=prefix, dir="/tmp")  # nosec
    else:
        return tempfile.mkdtemp(prefix=prefix)


# ----------------------------------------------------------


def uniq(seq):
    """Order preserving (very fast) uniq function for sequences"""

    seen = set()
    result = []
    for item in seq:
        if item in seen:
            continue
        seen.add(item)
        result.append(item)

    return result


# ----------------------------------------------------------


def send_multipart(socket, parts):
    """
    Send the parts through the socket after having encoded them if
    necessary.
    """

    for index, item in enumerate(parts):
        if isinstance(item, six.string_types):
            parts[index] = item.encode("utf-8")

    socket.send_multipart(parts)


# ----------------------------------------------------------


def find_free_port():
    """Returns the value of a free random port"""

    with contextlib.closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as s:
        s.bind(("", 0))
        return s.getsockname()[1]


# ----------------------------------------------------------


def find_free_port_in_range(min_port, max_port):
    """Returns the value of a free port in range"""

    for port in range(min_port, max_port):
        with contextlib.closing(
            socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ) as sock:
            try:
                sock.bind(("", port))
            except socket.error:
                continue
            else:
                return sock.getsockname()[1]


# ----------------------------------------------------------


def id_generator(
    size=6, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits
):
    """ Simple id generator based on
    https://stackoverflow.com/a/2257449/5843716
    """
    return "".join(random.choice(chars) for _ in range(size))  # nosec


# ----------------------------------------------------------


def setup_logging(verbosity, format_name, name=None, stream=None):
    """Setup logging """

    formatter = logging.Formatter(
        fmt="[%(asctime)s - '"
        + format_name
        + "' - %(name)s] %(levelname)s: %(message)s",
        datefmt="%d/%b/%Y %H:%M:%S",
    )

    handler = logging.StreamHandler(stream)
    handler.setFormatter(formatter)

    beat_core_logger = logging.getLogger("beat.core")
    beat_core_logger.addHandler(handler)

    beat_backend_logger = logging.getLogger("beat.backend.python")
    beat_backend_logger.addHandler(handler)

    if verbosity == 1:
        beat_core_logger.setLevel(logging.INFO)
        beat_backend_logger.setLevel(logging.INFO)
    elif verbosity == 2:
        beat_core_logger.setLevel(logging.DEBUG)
        beat_backend_logger.setLevel(logging.INFO)
    elif verbosity >= 3:
        beat_core_logger.setLevel(logging.DEBUG)
        beat_backend_logger.setLevel(logging.DEBUG)
    else:
        beat_core_logger.setLevel(logging.WARNING)
        beat_backend_logger.setLevel(logging.WARNING)

    return logging.getLogger(name)
