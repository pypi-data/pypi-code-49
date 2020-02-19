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

Usage:
  %(prog)s [-v ... | --verbose ...] [ --name=<name>] [--prefix=<path>]
           [--cache=<path>] [--docker] [--docker-network=<name>]
           [--port-range=<range>] <scheduler_address>
  %(prog)s (--help | -h)
  %(prog)s (--version | -V)


Options:
  -h, --help                 Show this screen
  -V, --version              Show version
  -v, --verbose              Increases the output verbosity level
  -n <name>, --name=<name>   The unique name of this worker on the database.
                             This is typically the assigned hostname of the node,
                             but not necessarily [default: %(hostname)s]
  -p, --prefix=<path>        Comma-separated list of the prefix(es) of your local data [default: .]
  -c, --cache=<path>         Cache prefix, otherwise defaults to '<prefix>/cache'
  --docker-network=<name>    Name of the docker network to use
  --port-range=<range>  Range of port usable for communication with containers

"""

import os
import sys
import logging
import zmq
import signal
import simplejson as json
import multiprocessing
import six

try:
    import Queue
except ImportError:
    import queue as Queue

import tempfile
from docopt import docopt
from socket import gethostname

from ..version import __version__
from ..execution.local import LocalExecutor
from ..execution.docker import DockerExecutor
from ..dock import Host
from ..worker import WorkerController
from ..utils import send_multipart

stop = False
logger = None


# ----------------------------------------------------------


class ExecutionProcess(multiprocessing.Process):
    def __init__(self, queue, job_id, prefix, data, cache, docker, images_cache=None):
        super(ExecutionProcess, self).__init__()

        self.queue = queue
        self.job_id = job_id
        self.prefix = prefix
        self.data = data
        self.cache = cache
        self.docker = docker
        self.images_cache = images_cache

    def run(self):
        signal.signal(signal.SIGTERM, signal.SIG_DFL)
        signal.signal(signal.SIGINT, signal.SIG_DFL)

        logger.debug("Process (pid=%d) started for job #%s", self.pid, self.job_id)
        self.queue.put("STARTED")

        # Create the executor
        try:
            if self.docker:
                host = Host(images_cache=self.images_cache, raise_on_errors=False)
                executor = DockerExecutor(
                    host, self.prefix, self.data, cache=self.cache
                )
            else:
                executor = LocalExecutor(self.prefix, self.data, cache=self.cache)

            if not executor.valid:
                self.queue.put(
                    dict(
                        error="Failed to load the execution information",
                        details=executor.errors,
                    )
                )
                return

            # Execute the algorithm
            with executor:
                result = executor.process()

            self.queue.put(dict(result=result))
        except Exception:
            import traceback

            self.queue.put(dict(system_error=traceback.format_exc()))

        self.queue.close()

        logger.debug("Process (pid=%d) done", self.pid)
        return 0


# ----------------------------------------------------------


def connect_to_scheduler(address, name):
    # Starts our 0MQ server
    context = zmq.Context()
    socket = context.socket(zmq.DEALER)
    if not isinstance(name, six.text_type):
        name = six.u(name)
    socket.setsockopt_string(zmq.IDENTITY, name)

    if address.find("://") < 0:
        address = "tcp://" + address

    socket.connect(address)
    logger.info("Connected to '%s'", address)

    poller = zmq.Poller()
    poller.register(socket, zmq.POLLIN)

    # Tell the scheduler we are ready
    socket.send(WorkerController.READY)

    # Wait for a response from the scheduler
    logger.info("Waiting for the scheduler...")

    while not stop:
        socks = dict(poller.poll(100))
        if not (socket in socks) or (socks[socket] != zmq.POLLIN):
            continue

        response = socket.recv()

        if response != WorkerController.ACK:
            logger.error(
                "Can't talk with the scheduler at '%s', expected '%s', got '%s'",
                address,
                WorkerController.ACK,
                response,
            )
            socket.setsockopt(zmq.LINGER, 0)
            socket.close()
            context.destroy()
            return (None, None, None)

        break

    if stop:
        socket.setsockopt(zmq.LINGER, 0)
        socket.close()
        context.destroy()
        return (None, None, None)

    logger.info("The scheduler answered")
    return (context, socket, poller)


# ----------------------------------------------------------


def main(user_input=None):
    # Parse the command-line arguments
    if user_input is not None:
        arguments = user_input
    else:
        arguments = sys.argv[1:]

    prog = os.path.basename(sys.argv[0])
    completions = dict(prog=prog, version=__version__, hostname=gethostname())
    args = docopt(
        __doc__ % completions,
        argv=arguments,
        options_first=True,
        version="v%s" % __version__,
    )

    # Setup the logging
    formatter = logging.Formatter(
        fmt="[%(asctime)s - Worker '"
        + args["--name"]
        + "' - %(name)s] %(levelname)s: %(message)s",
        datefmt="%d/%b/%Y %H:%M:%S",
    )

    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    beat_core_logger = logging.getLogger("beat.core")
    beat_core_logger.addHandler(handler)

    beat_backend_logger = logging.getLogger("beat.backend.python")
    beat_backend_logger.addHandler(handler)

    if args["--verbose"] == 1:
        beat_core_logger.setLevel(logging.INFO)
        beat_backend_logger.setLevel(logging.INFO)
    elif args["--verbose"] == 2:
        beat_core_logger.setLevel(logging.DEBUG)
        beat_backend_logger.setLevel(logging.INFO)
    elif args["--verbose"] >= 3:
        beat_core_logger.setLevel(logging.DEBUG)
        beat_backend_logger.setLevel(logging.DEBUG)
    else:
        beat_core_logger.setLevel(logging.WARNING)
        beat_backend_logger.setLevel(logging.WARNING)

    global logger
    logger = logging.getLogger(__name__)

    # Check the prefix path
    prefix = args["--prefix"] if args["--prefix"] is not None else "."
    if not os.path.exists(prefix):
        logger.error("Prefix not found at: '%s'", prefix)
        return 1

    # Check the cache path
    cache = (
        args["--cache"]
        if args["--cache"] is not None
        else os.path.join(prefix, "cache")
    )
    if not os.path.exists(cache):
        logger.error("Cache not found at: '%s'", cache)
        return 1

    # Install a signal handler
    def handler(signum, frame):
        # Ignore further signals
        signal.signal(signal.SIGTERM, signal.SIG_IGN)
        signal.signal(signal.SIGINT, signal.SIG_IGN)

        logger.info("Signal %d caught, terminating...", signum)
        global stop
        stop = True

    signal.signal(signal.SIGTERM, handler)
    signal.signal(signal.SIGINT, handler)

    # (If necessary) Docker-related initialisations
    docker_images_cache = None
    docker_network_name = None
    docker_port_range = None
    if args["--docker"]:
        docker_images_cache = os.path.join(
            tempfile.gettempdir(), "beat-docker-images.json"
        )
        logger.info("Using docker images cache: '%s'", docker_images_cache)
        Host(images_cache=docker_images_cache, raise_on_errors=False)

        docker_network_name = args.get("--docker-network", None)
        if docker_network_name:
            logger.info("Using docker network: '%s'", docker_network_name)

        docker_port_range = args.get("--port-range", None)
        if docker_port_range:
            if len(docker_port_range.split(":")) != 2:
                logger.error("Invalid port range %s" % docker_port_range)
                return 1

    # Establish a connection with the scheduler
    (context, socket, poller) = connect_to_scheduler(
        args["<scheduler_address>"], args["--name"]
    )
    if context is None:
        return 1

    # Process the requests
    execution_processes = []
    scheduler_available = True
    global stop

    while not stop:
        # If necessary, wait for the comeback of the scheduler
        if not scheduler_available:
            (context, socket, poller) = connect_to_scheduler(
                args["<scheduler_address>"], args["--name"]
            )
            if context is None:
                break
            scheduler_available = True

        # Send the result of the processing (if any)
        for execution_process in execution_processes:
            try:
                result = execution_process.queue.get_nowait()
            except Queue.Empty:
                continue

            execution_process.join()

            if "result" in result:
                content = json.dumps(result["result"])

                status = WorkerController.DONE
                if result["result"]["status"] != 0:
                    status = WorkerController.JOB_ERROR

                logger.info("Job #%s completed", execution_process.job_id)
                logger.debug('send: """%s"""' % content.rstrip())

                message = [status, execution_process.job_id, content.encode()]
            elif "error" in result:
                logger.error(result["error"])

                message = [WorkerController.JOB_ERROR, execution_process.job_id]

                message += [k.encode() for k in result["details"]]

            else:
                logger.error(result["system_error"])

                message = [
                    WorkerController.ERROR,
                    execution_process.job_id,
                    result["system_error"].encode(),
                ]

            send_multipart(socket, message)

            execution_processes.remove(execution_process)

        if len(execution_processes) == 0:
            timeout = 1000  # ms
        else:
            timeout = 100

        socks = dict(poller.poll(timeout))
        if not (socket in socks) or (socks[socket] != zmq.POLLIN):
            continue

        # Read the next command
        parts = socket.recv_multipart()

        command = parts[0]

        logger.debug("recv: %s", command)

        # Command: execute <job-id> <json-command>
        if command == WorkerController.EXECUTE:
            job_id = parts[1]
            data = json.loads(parts[2])
            if args["--docker"]:
                if docker_network_name:
                    data["network_name"] = docker_network_name
                if docker_port_range:
                    data["port_range"] = docker_port_range

            # Start the execution
            logger.info("Running '%s' with job id #%s", data["algorithm"], job_id)

            execution_process = ExecutionProcess(
                multiprocessing.Queue(),
                job_id,
                prefix,
                data,
                cache,
                docker=args["--docker"],
                images_cache=docker_images_cache,
            )
            execution_process.start()

            execution_process.queue.get()

            execution_processes.append(execution_process)

        # Command: cancel
        elif command == WorkerController.CANCEL:
            job_id = parts[1]

            try:
                execution_process = [
                    p for p in execution_processes if p.job_id == job_id
                ][0]
            except IndexError:
                parts = [WorkerController.ERROR, b"Unknown job: %s" % job_id]
                send_multipart(socket, parts)
                continue

            # Kill the processing thread
            logger.info("Cancelling the job #%s", execution_process.job_id)

            execution_process.terminate()
            execution_process.join()
            execution_processes.remove(execution_process)

            socket.send_multipart([WorkerController.CANCELLED, job_id])

        # Command: scheduler shutdown
        elif command == WorkerController.SCHEDULER_SHUTDOWN:
            logger.info("The scheduler shut down, we will wait for it")
            scheduler_available = False

            socket.setsockopt(zmq.LINGER, 0)
            socket.close()
            context.destroy()

            poller = None
            socket = None
            context = None

    if socket:
        socket.send(WorkerController.EXIT)

    # Cleanup
    for execution_process in execution_processes:
        execution_process.terminate()
        execution_process.join()

    if context:
        socket.setsockopt(zmq.LINGER, 0)
        socket.close()
        context.destroy()

    if (docker_images_cache is not None) and os.path.exists(docker_images_cache):
        os.remove(docker_images_cache)

    return 0
