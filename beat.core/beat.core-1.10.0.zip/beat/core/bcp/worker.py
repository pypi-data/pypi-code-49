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

Based on the Majordomo Protocol worker example of the ZMQ Guide.

Usage:
  %(prog)s [-v ... | --verbose ...] [ --name=<name>] [--prefix=<path>]
           [--cache=<path>] [--docker] [--docker-network=<name>]
           [--port-range=<range>] <broker_address>
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
import signal
import tempfile
import simplejson as json

import zmq

from socket import gethostname
from docopt import docopt

from ..bcpapi import BCP
from ..bcpapi.worker import BeatComputationWorker
from ..bcpapi.processor import BeatComputationProcessor
from ..bcpapi.execution import ExecutionProcess
from ..dock import Host
from ..utils import find_free_port
from ..utils import setup_logging
from ..version import __version__


logger = None


def setup_signal_handler():
    """Install a signal handler"""

    def handler(signum, frame):
        global logger
        logger.info("Signal %d caught, stopping...", signum)
        global stop
        stop = True

    signal.signal(signal.SIGTERM, handler)
    signal.signal(signal.SIGINT, handler)


def run(
    broker_address,
    service_name=gethostname(),
    verbose=1,
    prefix=None,
    cache=None,
    use_docker=False,
    docker_network_name=None,
    docker_port_range=None,
    docker_images_cache=None,
):
    """Start the worker

    Parameters:

        broker_address (str): Address of the broker
        service_name (str): Name to advertise
        verbose (int): Verbosity level
        prefix (str): Path to the prefix
        cache (str): Path to the cache
        use_docker (bool): Whether to use docker as backend
        docker_network_name (str): Docker network name to use
        docker_port_range (str): Port range in the format <start:end>
        docker_images_cache (str): Path to docker images cache
    """

    global logger

    if logger is None:
        if isinstance(service_name, bytes):
            name = service_name.decode("utf-8")
        else:
            name = service_name

        logging_name = "Worker '{}'".format(name)
        logger = setup_logging(verbose, logging_name, __name__)

    setup_signal_handler()

    poller = zmq.Poller()

    port = find_free_port()
    processor_address = "tcp://*:{}".format(port)
    worker_address = "tcp://localhost:{}".format(port)

    worker = BeatComputationWorker(poller, broker_address, service_name, verbose == 3)
    processor = BeatComputationProcessor(poller, processor_address, verbose == 3)

    execution_processes = []
    global stop
    stop = False
    while not stop:
        try:
            items = dict(poller.poll(worker.timeout))
        except KeyboardInterrupt:
            stop = True
            continue

        if processor.sink in items:
            reply = processor.process()
            reply.pop(0)  # processor name
            status = reply[0]
            job_id = reply[1]

            # Processing job status
            if status == BCP.BCPP_JOB_DONE:
                logger.info("Job {} done".format(job_id))
                execution_process = next(
                    (p for p in execution_processes if p.job_id == job_id), None
                )
                if execution_process is None:
                    logger.warning("Done job {} not found".format(job_id))
                    reply = None
                else:
                    execution_processes.remove(execution_process)
                    del execution_process

            if verbose:
                logger.info("Sending {}".format(reply))

            if reply is not None:
                worker.send(reply)

        if worker.worker in items:
            request = worker.process()

            if request is None:
                # Received something other than request
                continue

            command = request.pop(0)
            # Command: execute <job-id> <json-command>
            if command == BCP.BCPE_EXECUTE:
                job_id = request.pop(0)
                job_data = request.pop(0)
                data = json.loads(job_data)

                reply = [BCP.BCPP_JOB_RECEIVED, job_id]
                worker.send(reply)

                if use_docker:
                    if docker_network_name:
                        data["network_name"] = docker_network_name
                    if docker_port_range:
                        data["port_range"] = docker_port_range

                # Start the execution
                logger.info("Running '%s' with job id #%s", data["algorithm"], job_id)

                execution_process = ExecutionProcess(
                    worker_address,
                    job_id,
                    prefix,
                    data,
                    cache,
                    docker=use_docker,
                    images_cache=docker_images_cache,
                )
                execution_processes.append(execution_process)
                execution_process.start()
                execution_process.queue.get()

                reply = [BCP.BCPP_JOB_STARTED, job_id]
                worker.send(reply)

            # Command: cancel
            elif command == BCP.BCPE_CANCEL:
                job_id = request.pop(0)

                execution_process = next(
                    (p for p in execution_processes if p.job_id == job_id), None
                )

                if execution_process is None:
                    reply = [BCP.BCPP_ERROR, b"Unknown job: %s" % job_id]
                else:
                    # Kill the processing thread
                    logger.info("Cancelling the job #%s", execution_process.job_id)
                    execution_process.terminate()
                    execution_process.join()
                    execution_processes.remove(execution_process)
                    del execution_process
                    reply = [BCP.BCPP_JOB_CANCELLED, job_id]

                worker.send(reply)

            # Command: scheduler shutdown
            elif command == BCP.BCPE_SCHEDULER_SHUTDOWN:
                logger.info("The scheduler shut down, we will wait for it")
                worker.destroy()

    worker.destroy()
    # Cleanup
    for execution_process in execution_processes:
        execution_process.terminate()
        execution_process.join()

    processor.destroy()

    if (docker_images_cache is not None) and os.path.exists(docker_images_cache):
        os.remove(docker_images_cache)

    return 0


def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]

    prog = os.path.basename(__name__.split(".")[0])
    completions = dict(prog=prog, version=__version__, hostname=gethostname())
    args = docopt(
        __doc__ % completions,
        argv=argv,
        options_first=True,
        version="v%s" % __version__,
    )
    broker_address = args.pop("<broker_address>")

    global logger

    logging_name = "Worker '" + args.get("--name") + "'"
    logger = setup_logging(args.get("--verbose"), logging_name)

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
            logger.info("Using port range %s", docker_port_range)

    return run(
        broker_address,
        service_name=args.get("--name"),
        verbose=args.get("--verbose"),
        prefix=prefix,
        cache=cache,
        use_docker=args["--docker"],
        docker_network_name=docker_network_name,
        docker_port_range=docker_port_range,
        docker_images_cache=docker_images_cache,
    )


if __name__ == "__main__":
    main()
