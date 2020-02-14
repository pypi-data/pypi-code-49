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


"""Executes a single algorithm. (%(version)s)

usage:
  %(prog)s [--debug] [--cache=<path>] [--loop=<loop_addr>] <addr> <dir> [<db_addr>]
  %(prog)s (--help)
  %(prog)s (--version)


arguments:
  <addr>      Address of the controlling process
  <dir>       Directory containing all configuration required to run the user
              algorithm
  <db_addr>   Address for databases-related I/O requests

options:
  -h, --help         Shows this help message and exit
  -V, --version      Shows program's version number and exit
  -d, --debug        Runs executor in debugging mode
  -c, --cache=path   Cache prefix [default: /cache].
  --loop=loop_addr   Address for loop-related I/O requests

"""

import logging

import os
import sys
import docopt
import simplejson
import subprocess  # nosec

import zmq

from beat.backend.python.execution import AlgorithmExecutor
from beat.backend.python.exceptions import UserError


# ----------------------------------------------------------


def send_error(logger, socket, tp, message):
    """Sends a user (usr) or system (sys) error message to the infrastructure"""

    logger.debug("send: (err) error")
    socket.send_string("err", zmq.SNDMORE)
    socket.send_string(tp, zmq.SNDMORE)
    logger.debug('send: """%s"""' % message.rstrip())
    socket.send_string(message)

    poller = zmq.Poller()
    poller.register(socket, zmq.POLLIN)

    this_try = 1
    max_tries = 5
    timeout = 1000  # ms
    while this_try <= max_tries:
        socks = dict(poller.poll(timeout))  # blocks here, for 5 seconds at most
        if socket in socks and socks[socket] == zmq.POLLIN:
            answer = socket.recv()  # ack
            logger.debug("recv: %s", answer)
            break
        logger.warn('(try %d) waited %d ms for "ack" from server', this_try, timeout)
        this_try += 1
        if this_try > max_tries:
            logger.error("could not send error message to server")
            logger.error("stopping 0MQ client anyway")


# ----------------------------------------------------------


def close(logger, sockets, context):
    for socket in sockets:
        if socket is not None:
            socket.setsockopt(zmq.LINGER, 0)
            socket.close()

    context.term()
    logger.debug("0MQ client finished")


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


def main():

    """
    # This is an important outcome of this process and must be available
    # to different processing phases of this script
    """

    package = __name__.rsplit(".", 2)[0]
    version = package + " v" + __import__("pkg_resources").require(package)[0].version
    prog = os.path.basename(sys.argv[0])

    args = docopt.docopt(__doc__ % dict(prog=prog, version=version), version=version)

    # Setup the logging system
    formatter = logging.Formatter(
        fmt="[%(asctime)s - execute.py - " "%(name)s] %(levelname)s: %(message)s",
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

    # Retrieve the cache path
    cache = args.get("--cache")

    # Creates the 0MQ socket for communication with BEAT
    context = zmq.Context()
    socket = context.socket(zmq.PAIR)
    address = args["<addr>"]
    socket.connect(address)
    logger.debug("zmq client connected to `%s'", address)

    # Creates the 0MQ socket for communication with the databases (if necessary)
    db_socket = None
    db_addr = args.get("<db_addr>")
    if db_addr:
        db_socket = context.socket(zmq.PAIR)
        db_socket.connect(db_addr)
        logger.debug("zmq client connected to db `%s'", db_addr)

    loop_socket = None
    loop_addr = args.get("--loop")
    if loop_addr:
        loop_socket = context.socket(zmq.PAIR)
        loop_socket.connect(loop_addr)
        logger.debug("zmq client connected to loop `%s'", loop_addr)

    # Check the dir
    run_directory = args["<dir>"]
    if not os.path.exists(run_directory):
        send_error(
            logger, socket, "sys", "Running directory `%s' not found" % run_directory
        )
        close(logger, [socket, db_socket, loop_socket], context)
        return 1

    # Load the configuration
    with open(os.path.join(run_directory, "configuration.json"), "r") as f:
        cfg = simplejson.load(f)

    # Create a new user with less privileges (if necessary)
    user_id = cfg["uid"]
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
            send_error(
                logger,
                socket,
                "sys",
                "Failed to create an user with the UID %d" % user_id,
            )
            close(logger, [socket, db_socket, loop_socket], context)
            return 1

        # Change to the user with less privileges
        try:
            os.setgid(user_id)
            os.setuid(user_id)
        except Exception:
            import traceback

            send_error(logger, socket, "sys", traceback.format_exc())
            close(logger, [socket, db_socket, loop_socket], context)
            return 1

    try:
        # Sets up the execution
        executor = AlgorithmExecutor(
            socket,
            run_directory,
            cache_root=cache,
            db_socket=db_socket,
            loop_socket=loop_socket,
        )

        try:
            status = executor.setup()
            if not status:
                raise UserError("Could not setup algorithm (returned False)")
        except (UserError, MemoryError):
            raise
        except Exception as e:
            import traceback

            exc_type, exc_value, exc_traceback = sys.exc_info()
            tb = traceback.extract_tb(exc_traceback)
            s = process_traceback(tb, executor.prefix)
            raise UserError("%s%s: %s" % (s, type(e).__name__, e))

        # Prepare the algorithm
        try:
            status = executor.prepare()
            if not status:
                raise UserError("Could not prepare algorithm (returned False)")
        except (UserError, MemoryError):
            raise
        except Exception as e:
            import traceback

            exc_type, exc_value, exc_traceback = sys.exc_info()
            tb = traceback.extract_tb(exc_traceback)
            s = process_traceback(tb, executor.prefix)
            raise UserError("%s%s: %s" % (s, type(e).__name__, e))

        # Execute the code
        try:
            status = executor.process()
            if not status:
                raise UserError("Could not run algorithm (returned False)")
        except (UserError, MemoryError):
            raise
        except Exception as e:
            import traceback

            exc_type, exc_value, exc_traceback = sys.exc_info()
            tb = traceback.extract_tb(exc_traceback)
            s = process_traceback(tb, executor.prefix)
            raise UserError("%s%s: %s" % (s, type(e).__name__, e))

    except UserError as e:
        send_error(logger, socket, "usr", str(e))
        return 1

    except MemoryError:
        # Say something meaningful to the user
        msg = (
            "The user process for this block ran out of memory. We "
            "suggest you optimise your code to reduce memory usage or, "
            "if this is not an option, choose an appropriate processing "
            "queue with enough memory."
        )
        send_error(logger, socket, "usr", msg)
        return 1

    except Exception:
        import traceback

        send_error(logger, socket, "sys", traceback.format_exc())
        return 1

    finally:
        close(logger, [socket, db_socket, loop_socket], context)

    return 0


# ----------------------------------------------------------


if __name__ == "__main__":
    sys.exit(main())
