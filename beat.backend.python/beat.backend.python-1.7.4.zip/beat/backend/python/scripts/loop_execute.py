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


"""Executes a loop algorithm. (%(version)s)

usage:
  %(prog)s [--debug] <addr> <dir> <cache> [<db_addr>]
  %(prog)s (--help)
  %(prog)s (--version)


arguments:
  <addr>    Listen for incoming request on this address ('host:port')
  <dir>     Directory containing all configuration required to run the views
  <cache>   Path to the cache
  <db_addr> Address for databases-related I/O requests


options:
  -h, --help         Shows this help message and exit
  -V, --version      Shows program's version number and exit
  -d, --debug        Runs executor in debugging mode

"""

import logging

import os
import sys
import docopt
import simplejson as json
import subprocess  # nosec

import zmq

from beat.backend.python.execution import LoopExecutor
from beat.backend.python.execution import LoopMessageHandler
from beat.backend.python.exceptions import UserError


# ----------------------------------------------------------


def process_traceback(tb, prefix):
    import traceback

    algorithms_prefix = os.path.join(prefix, "algorithms") + os.sep

    for first_line, line in enumerate(tb):
        if line[0].startswith(algorithms_prefix):
            break

    s = "".join(traceback.format_list(tb[first_line:]))
    s = s.replace(algorithms_prefix, "").strip()

    return s


# ----------------------------------------------------------


def main(arguments=None):

    # Parse the command-line arguments
    if arguments is None:
        arguments = sys.argv[1:]

    package = __name__.rsplit(".", 2)[0]
    version = package + " v" + __import__("pkg_resources").require(package)[0].version

    prog = os.path.basename(sys.argv[0])

    args = docopt.docopt(
        __doc__ % dict(prog=prog, version=version), argv=arguments, version=version
    )

    # Setup the logging system
    formatter = logging.Formatter(
        fmt="[%(asctime)s - loop_provider.py - " "%(name)s] %(levelname)s: %(message)s",
        datefmt="%d/%b/%Y %H:%M:%S",
    )

    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    root_logger = logging.getLogger("beat.backend.python")
    root_logger.addHandler(handler)

    if args["--debug"]:
        root_logger.setLevel(logging.DEBUG)
    else:
        root_logger.setLevel(logging.INFO)

    logger = logging.getLogger(__name__)

    # Create the message handler
    message_handler = LoopMessageHandler(args["<addr>"])

    context = None
    db_socket = None
    if args["<db_addr>"]:
        context = zmq.Context()
        db_socket = context.socket(zmq.PAIR)
        db_socket.connect(args["<db_addr>"])
        logger.debug("loop: zmq client connected to db `%s'", args["<db_addr>"])

    # If necessary, change to another user (with less privileges, but has access
    # to the databases)

    # Check the dir
    if not os.path.exists(args["<dir>"]):
        raise IOError("Running directory `%s' not found" % args["<dir>"])

    # Load the configuration
    with open(os.path.join(args["<dir>"], "configuration.json"), "r") as f:
        cfg = json.load(f)

    user_id = cfg["uid"]

    # Create a new user with less privileges (if necessary)
    if os.getuid() != user_id:
        retcode = subprocess.call(  # nosec
            [
                "adduser",
                "--uid",
                str(user_id),
                "--no-create-home",
                "--disabled-password",
                "--disabled-login",
                "--gecos",
                '""',
                "-q",
                "beat-nobody",
            ]
        )
        if retcode != 0:
            msg = "Failed to create a user with the UID {}".format(user_id)
            message_handler.send_error(msg, "sys")
            message_handler.destroy()
            return 1

        # Change to the user with less privileges
        try:
            os.setgid(user_id)
            os.setuid(user_id)
        except Exception as e:
            msg = "Failed to change to user id {}: {}".format(cfg["uid"], e)
            message_handler.send_error(msg, "sys")
            message_handler.destroy()
            return 1

    try:
        # Sets up the execution
        try:
            loop_executor = LoopExecutor(
                message_handler=message_handler,
                directory=args["<dir>"],
                cache_root=args["<cache>"],
                db_socket=db_socket,
            )
        except (MemoryError):
            raise
        except Exception as e:
            import traceback

            exc_type, exc_value, exc_traceback = sys.exc_info()
            tb = traceback.extract_tb(exc_traceback)
            s = process_traceback(tb, os.path.join(args["<dir>"], "prefix"))
            raise UserError("%s%s: %s" % (s, type(e).__name__, e))

        try:
            status = loop_executor.setup()
            if not status:
                raise UserError("Could not setup loop algorithm (returned False)")
        except (UserError, MemoryError):
            raise
        except Exception as e:
            import traceback

            exc_type, exc_value, exc_traceback = sys.exc_info()
            tb = traceback.extract_tb(exc_traceback)
            s = process_traceback(tb, loop_executor.prefix)
            raise UserError("%s%s: %s" % (s, type(e).__name__, e))

        # Prepare the algorithm
        try:
            status = loop_executor.prepare()
            if not status:
                raise UserError("Could not prepare loop algorithm (returned False)")
        except (UserError, MemoryError):
            raise
        except Exception as e:
            import traceback

            exc_type, exc_value, exc_traceback = sys.exc_info()
            tb = traceback.extract_tb(exc_traceback)
            s = process_traceback(tb, loop_executor.prefix)
            raise UserError("%s%s: %s" % (s, type(e).__name__, e))

        # Execute the code
        try:
            logger.debug("loop: Starting process")
            loop_executor.process()
            loop_executor.wait()
            loop_executor.close()
        except (MemoryError):
            raise
        except Exception as e:
            import traceback

            exc_type, exc_value, exc_traceback = sys.exc_info()
            tb = traceback.extract_tb(exc_traceback)
            s = process_traceback(tb, os.path.join(args["<dir>"], "prefix"))
            raise UserError("%s%s: %s" % (s, type(e).__name__, e))

    except UserError as e:
        message_handler.send_error(str(e), "usr")
        message_handler.destroy()
        return 1

    except MemoryError:
        # Say something meaningful to the user
        msg = (
            "The user process for this block ran out of memory. We "
            "suggest you optimise your code to reduce memory usage or, "
            "if this is not an option, choose an appropriate processing "
            "queue with enough memory."
        )
        message_handler.send_error(msg, "usr")
        message_handler.destroy()
        return 1

    except Exception:
        import traceback

        message_handler.send_error(traceback.format_exc(), "sys")
        message_handler.destroy()
        return 1

    if db_socket is not None:
        db_socket.setsockopt(zmq.LINGER, 0)
        db_socket.close()

        context.term()
        logger.debug("loop: 0MQ client finished")

    message_handler.destroy()

    return 0


if __name__ == "__main__":
    sys.exit(main())
