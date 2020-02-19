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


"""Starts the worker process (%(version)s)

Based on the Majordomo Protocol broker example of the ZMQ Guide.

Usage:
  %(prog)s [-v ... | --verbose ...] <port>
  %(prog)s (--help | -h)
  %(prog)s (--version | -V)


Options:
  -h, --help                 Show this screen
  -V, --version              Show version
  -v, --verbose              Increases the output verbosity level
"""

import os
import sys

from docopt import docopt

from ..bcpapi.broker import BeatComputationBroker
from ..version import __version__
from ..utils import setup_logging


def run(port=5555, verbose=1, callbacks=None):
    """Start the broker

    Parameters:

        port (int): Port to use for tcp connection
        verbose (int): Level of verbosity
        callbacks (tuple): Pair of methods to call when workers are ready or gone
    """

    setup_logging(verbose, __name__, __name__)

    address = "tcp://*:{}".format(port)
    broker = BeatComputationBroker(verbose == 3)
    if callbacks:
        broker.set_worker_callbacks(*callbacks)
    broker.bind(address)
    broker.mediate()


def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]

    prog = os.path.basename(sys.argv[0])
    completions = dict(prog=prog, version=__version__)
    args = docopt(
        __doc__ % completions,
        argv=argv,
        options_first=True,
        version="v%s" % __version__,
    )
    broker_port = args.pop("<port>")

    return run(broker_port, args["--verbose"])


if __name__ == "__main__":
    main()
