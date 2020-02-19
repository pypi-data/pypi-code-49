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
==========
management
==========

Execution utilities
"""

import logging
import multiprocessing
import signal
import zmq
import simplejson as json

from ..dock import Host
from ..execution.local import LocalExecutor
from ..execution.docker import DockerExecutor

from . import BCP


class ExecutionProcess(multiprocessing.Process):
    """Worker process using ZMQ to communicate back to the caller"""

    def __init__(self, address, job_id, prefix, data, cache, docker, images_cache=None):
        super(ExecutionProcess, self).__init__()

        self.socket = None
        self.queue = multiprocessing.Queue()
        self.address = address
        self.job_id = job_id
        self.identity = "worker_{}".format(self.job_id.decode("utf-8"))
        self.prefix = prefix
        self.data = data
        self.cache = cache
        self.docker = docker
        self.images_cache = images_cache
        self.logger = logging.getLogger(self.identity)

    def __send_message(self, status, message=None):
        """Format and send message"""

        data = [status, self.job_id]
        if message:
            if not isinstance(message, list):
                message = [message]
            data += message
        self.socket.send_multipart(data)

    def run(self):
        signal.signal(signal.SIGTERM, signal.SIG_DFL)
        signal.signal(signal.SIGINT, signal.SIG_DFL)

        self.queue.put("started")

        ctx = zmq.Context()
        self.socket = ctx.socket(zmq.DEALER)
        self.socket.linger = 0
        self.socket.setsockopt_string(zmq.IDENTITY, self.identity)
        self.socket.connect(self.address)

        self.logger.debug("Process (pid=%d) started for job #%s", self.pid, self.job_id)

        # Create the executor
        if self.docker:
            host = Host(images_cache=self.images_cache, raise_on_errors=False)
            executor = DockerExecutor(host, self.prefix, self.data, cache=self.cache)
        else:
            executor = LocalExecutor(self.prefix, self.data, cache=self.cache)

        status = BCP.BCPP_JOB_DONE
        message = None
        if executor.valid:
            try:
                # Execute the algorithm
                with executor:
                    result = executor.process()

                if result["status"] != 0:
                    status = BCP.BCPP_JOB_ERROR

                message = json.dumps(result).encode()
            except Exception:
                import traceback

                status = BCP.BCPP_ERROR
                message = traceback.format_exc().encode()
        else:
            status = BCP.BCPP_JOB_ERROR
            message = [error.encode() for error in executor.errors]

        self.logger.debug("Process (pid=%d) done", self.pid)
        self.__send_message(status, message)
        self.socket.close()
        ctx.destroy()
        self.socket = None

        self.queue.put("done")
        self.queue.close()
