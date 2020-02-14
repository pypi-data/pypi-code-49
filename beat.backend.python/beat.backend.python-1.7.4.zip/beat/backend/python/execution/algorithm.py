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
==================
Algorithm executor
==================

A class that can setup and execute algorithm blocks on the backend
"""

import logging
import os
import simplejson
import zmq

from ..algorithm import Algorithm
from ..helpers import create_inputs_from_configuration
from ..helpers import create_outputs_from_configuration
from ..helpers import AccessMode
from .. import stats

from .loop import LoopChannel

logger = logging.getLogger(__name__)


class AlgorithmExecutor(object):
    """Executors runs the code given an execution block information

    Parameters:

      socket (zmq.Socket): A pre-connected socket to send and receive messages
        from.

      directory (str): The path to a directory containing all the information
        required to run the user experiment.

      dataformat_cache (:py:class:`dict`, Optional): A dictionary mapping
        dataformat names to loaded dataformats. This parameter is optional and,
        if passed, may greatly speed-up database loading times as dataformats
        that are already loaded may be re-used. If you use this parameter, you
        must guarantee that the cache is refreshed as appropriate in case the
        underlying dataformats change.

      database_cache (:py:class:`dict`, Optional): A dictionary mapping
        database names to loaded databases. This parameter is optional and, if
        passed, may greatly speed-up database loading times as databases that
        are already loaded may be re-used. If you use this parameter, you must
        guarantee that the cache is refreshed as appropriate in case the
        underlying databases change.

      library_cache (:py:class:`dict`, Optional): A dictionary mapping library
        names to loaded libraries. This parameter is optional and, if passed,
        may greatly speed-up library loading times as libraries that are
        already loaded may be re-used. If you use this parameter, you must
        guarantee that the cache is refreshed as appropriate in case the
        underlying libraries change.  """

    def __init__(
        self,
        socket,
        directory,
        dataformat_cache=None,
        database_cache=None,
        library_cache=None,
        cache_root="/cache",
        db_socket=None,
        loop_socket=None,
    ):

        self.socket = socket
        self.db_socket = db_socket
        self.loop_socket = loop_socket
        self.loop_channel = None

        self.configuration = os.path.join(directory, "configuration.json")
        with open(self.configuration, "rb") as f:
            self.data = simplejson.loads(f.read().decode("utf-8"))

        self.prefix = os.path.join(directory, "prefix")
        self._runner = None

        # Temporary caches, if the user has not set them, for performance
        database_cache = database_cache if database_cache is not None else {}
        dataformat_cache = dataformat_cache if dataformat_cache is not None else {}
        library_cache = library_cache if library_cache is not None else {}

        # Load the algorithm
        self.algorithm = Algorithm(
            self.prefix, self.data["algorithm"], dataformat_cache, library_cache
        )

        if db_socket:
            db_access_mode = AccessMode.REMOTE
            databases = None
        else:
            db_access_mode = AccessMode.LOCAL
            databases = database_cache

        if self.algorithm.type == Algorithm.LEGACY:
            # Loads algorithm inputs
            (self.input_list, self.data_loaders) = create_inputs_from_configuration(
                self.data,
                self.algorithm,
                self.prefix,
                cache_root,
                cache_access=AccessMode.LOCAL,
                db_access=db_access_mode,
                socket=self.db_socket,
                databases=databases,
            )

            # Loads algorithm outputs
            (self.output_list, _) = create_outputs_from_configuration(
                self.data,
                self.algorithm,
                self.prefix,
                cache_root,
                input_list=self.input_list,
                data_loaders=self.data_loaders,
            )

        else:
            (self.input_list, self.data_loaders) = create_inputs_from_configuration(
                self.data,
                self.algorithm,
                self.prefix,
                cache_root,
                cache_access=AccessMode.LOCAL,
                db_access=db_access_mode,
                socket=self.db_socket,
                databases=databases,
            )

            # Loads algorithm outputs
            (self.output_list, _) = create_outputs_from_configuration(
                self.data,
                self.algorithm,
                self.prefix,
                cache_root,
                input_list=self.input_list,
                data_loaders=self.data_loaders,
                loop_socket=self.loop_socket,
            )

        if self.loop_socket:
            self.loop_channel = LoopChannel(self.loop_socket)
            self.loop_channel.setup(self.algorithm, self.prefix)

    @property
    def runner(self):
        """Returns the algorithm runner

        This property allows for lazy loading of the runner
        """

        if self._runner is None:
            self._runner = self.algorithm.runner()
        return self._runner

    def setup(self):
        """Sets up the algorithm to start processing"""

        retval = self.runner.setup(self.data["parameters"])
        logger.debug("User algorithm is setup")
        return retval

    def prepare(self):
        """Prepare the algorithm"""

        retval = self.runner.prepare(self.data_loaders)
        logger.debug("User algorithm is prepared")
        return retval

    def process(self):
        """Executes the user algorithm code using the current interpreter.
        """

        if self.algorithm.is_autonomous:
            if self.analysis:
                result = self.runner.process(
                    data_loaders=self.data_loaders, output=self.output_list[0]
                )
            else:
                result = self.runner.process(
                    data_loaders=self.data_loaders,
                    outputs=self.output_list,
                    loop_channel=self.loop_channel,
                )

            if not result:
                return False

        else:
            if self.algorithm.type == Algorithm.LEGACY:
                logger.warning(
                    "%s is using LEGACY I/O API, please upgrade this algorithm as soon as possible"
                    % self.algorithm.name
                )

            while self.input_list.hasMoreData():
                main_group = self.input_list.main_group
                main_group.restricted_access = False
                main_group.next()
                main_group.restricted_access = True

                if self.loop_socket:
                    self.loop_socket.send_string("rdi")
                    self.loop_socket.recv()

                if self.algorithm.type == Algorithm.LEGACY:
                    if self.analysis:
                        result = self.runner.process(
                            inputs=self.input_list, output=self.output_list[0]
                        )
                    else:
                        result = self.runner.process(
                            inputs=self.input_list, outputs=self.output_list
                        )

                elif self.algorithm.is_sequential:
                    if self.analysis:
                        result = self.runner.process(
                            inputs=self.input_list,
                            data_loaders=self.data_loaders,
                            output=self.output_list[0],
                        )
                    else:
                        try:
                            result = self.runner.process(
                                inputs=self.input_list,
                                data_loaders=self.data_loaders,
                                outputs=self.output_list,
                                loop_channel=self.loop_channel,
                            )
                        except Exception:
                            result = None

                if not result:
                    self.done({})
                    return False

        for output in self.output_list:
            output.close()

        missing_data_outputs = [x for x in self.output_list if x.isDataMissing()]

        if missing_data_outputs:
            raise RuntimeError(
                "Missing data on the following output(s): %s"
                % ", ".join([x.name for x in missing_data_outputs])
            )

        # Send the done command
        statistics = stats.io_statistics(self.data, self.input_list, self.output_list)

        logger.debug("Statistics: " + simplejson.dumps(statistics, indent=4))

        self.done(statistics)

        return True

    def done(self, statistics):
        """Indicates the infrastructure the execution is done"""

        if self.db_socket:
            logger.debug("send to db: (don) done")
            self.db_socket.send_string("don", zmq.SNDMORE)
            self.db_socket.send_string(simplejson.dumps(statistics))

            answer = self.db_socket.recv()  # ack
            logger.debug("recv from db: %s", answer)

        if self.loop_socket:
            logger.debug("send to loop: (don) done")
            self.loop_socket.send_string("don")

            answer = self.loop_socket.recv()  # ack
            logger.debug("recv from loop: %s", answer)

        logger.debug("send: (don) done")
        self.socket.send_string("don", zmq.SNDMORE)
        self.socket.send_string(simplejson.dumps(statistics))

        answer = self.socket.recv()  # ack
        logger.debug("recv: %s", answer)

    @property
    def schema_version(self):
        """Returns the schema version"""
        return self.data.get("schema_version", 1)

    @property
    def analysis(self):
        """A boolean that indicates if the current block is an analysis block
        """

        return "result" in self.data
