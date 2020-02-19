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
subprocess
==========

Execution utilities
"""

import os
import shutil
import logging
import sys
import subprocess as sp  # nosec
import tempfile

from beat.backend.python.execution import MessageHandler

from .. import stats
from .. import utils

from .remote import RemoteExecutor


logger = logging.getLogger(__name__)


def _which(program):
    """Pythonic version of the `which` command-line application"""

    def is_exe(fpath):
        return os.path.isfile(fpath) and os.access(fpath, os.X_OK)

    fpath, fname = os.path.split(program)
    if fpath and is_exe(program):
        return program
    else:
        for path in os.environ["PATH"].split(os.pathsep):
            exe_file = os.path.join(path, fname)
            if is_exe(exe_file):
                return exe_file

    return None


class SubprocessExecutor(RemoteExecutor):
    """SubprocessExecutor runs the code given an execution block information,
    using a subprocess


    Parameters:

      prefix (str): Establishes the prefix of your installation.

      data (dict, str): The piece of data representing the block to be executed.
        It must validate against the schema defined for execution blocks. If a
        string is passed, it is supposed to be a fully qualified absolute path to
        a JSON file containing the block execution information.

      cache (:py:class:`str`, Optional): If your cache is not located under
        ``<prefix>/cache``, then specify a full path here. It will be used
        instead.

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

      algorithm_cache (:py:class:`dict`, Optional): A dictionary mapping
        algorithm names to loaded algorithms. This parameter is optional and,
        if passed, may greatly speed-up database loading times as algorithms
        that are already loaded may be re-used. If you use this parameter, you
        must guarantee that the cache is refreshed as appropriate in case the
        underlying algorithms change.

      library_cache (:py:class:`dict`, Optional): A dictionary mapping library
        names to loaded libraries. This parameter is optional and, if passed,
        may greatly speed-up library loading times as libraries that are
        already loaded may be re-used. If you use this parameter, you must
        guarantee that the cache is refreshed as appropriate in case the
        underlying libraries change.

      custom_root_folders (dict): A dictionary mapping databases name and
        their location on disk
      ip_address (str): IP address of the machine to connect to for the database
        execution and message handlers.
      python_path (str): Path to the python executable of the environment to use
        for experiment execution.

    Attributes:

      cache (str): The path to the cache currently being used

      errors (list): A list containing errors found while loading this execution
        block.

      data (dict): The original data for this executor, as loaded by our JSON
        decoder.

      algorithm (beat.core.algorithm.Algorithm): An object representing the
        algorithm to be run.

      databases (dict): A dictionary in which keys are strings with database
        names and values are :py:class:`.database.Database`, representing the
        databases required for running this block. The dictionary may be empty
        in case all inputs are taken from the file cache.

      views (dict): A dictionary in which the keys are tuples pointing to the
        ``(<database-name>, <protocol>, <set>)`` and the value is a setup view
        for that particular combination of details. The dictionary may be empty
        in case all inputs are taken from the file cache.

      input_list (beat.backend.python.inputs.InputList): A list of inputs that
        will be served to the algorithm.

      output_list (beat.backend.python.outputs.OutputList): A list of outputs
        that the algorithm will produce.

      data_sources (list): A list with all data-sources created by our execution
        loader.

      data_sinks (list): A list with all data-sinks created by our execution
        loader. These are useful for clean-up actions in case of problems.

    """

    def __init__(
        self,
        prefix,
        data,
        cache=None,
        dataformat_cache=None,
        database_cache=None,
        algorithm_cache=None,
        library_cache=None,
        custom_root_folders=None,
        ip_address="127.0.0.1",
        python_path=None,
    ):
        super(SubprocessExecutor, self).__init__(
            prefix,
            data,
            ip_address,
            cache=cache,
            dataformat_cache=dataformat_cache,
            database_cache=database_cache,
            algorithm_cache=algorithm_cache,
            library_cache=library_cache,
            custom_root_folders=custom_root_folders,
        )

        if python_path is None:
            base_path = os.path.dirname(sys.argv[0])

            # We need three apps to run this function: databases_provider and execute
            self.EXECUTE_BIN = _which(os.path.join(base_path, "execute"))
            self.LOOP_EXECUTE_BIN = _which(os.path.join(base_path, "loop_execute"))
            self.DBPROVIDER_BIN = _which(os.path.join(base_path, "databases_provider"))
        else:
            base_path = os.path.dirname(python_path)
            self.EXECUTE_BIN = os.path.join(base_path, "execute")
            self.LOOP_EXECUTE_BIN = os.path.join(base_path, "loop_execute")
            self.DBPROVIDER_BIN = os.path.join(base_path, "databases_provider")

        if any(
            [
                not os.path.exists(executable)
                for executable in [
                    self.EXECUTE_BIN,
                    self.LOOP_EXECUTE_BIN,
                    self.DBPROVIDER_BIN,
                ]
            ]
        ):
            raise RuntimeError("Invalid environment")

    def __create_db_process(self, configuration_name=None):
        databases_process = None
        databases_configuration_path = None
        database_port = None

        database_port = utils.find_free_port()

        # Configuration and needed files
        databases_configuration_path = utils.temporary_directory()
        self.dump_databases_provider_configuration(databases_configuration_path)

        # Creation of the subprocess
        # Note: we only support one databases image loaded at the same time

        cmd = [
            self.DBPROVIDER_BIN,
            self.ip_address + (":%d" % database_port),
            databases_configuration_path,
            self.cache,
        ]

        if logger.getEffectiveLevel() <= logging.DEBUG:
            cmd.insert(1, "--debug")

        if configuration_name is not None:
            cmd.append(configuration_name)

        databases_process_stdout = tempfile.NamedTemporaryFile(delete=False)
        databases_process_stderr = tempfile.NamedTemporaryFile(delete=False)

        logger.debug("Starting database process with: %s" % " ".join(cmd))

        databases_process = sp.Popen(
            cmd, stdout=databases_process_stdout, stderr=databases_process_stderr
        )

        retval = dict(
            configuration_path=databases_configuration_path,
            process=databases_process,
            port=database_port,
            stdout=databases_process_stdout,
            stderr=databases_process_stderr,
        )
        return retval

    def process(
        self, virtual_memory_in_megabytes=0, max_cpu_percent=0, timeout_in_minutes=0
    ):
        """Executes the user algorithm code using an external program.

        The execution interface follows the backend API as described in our
        documentation.

        We use green subprocesses this implementation. Each co-process is linked
        to us via 2 uni-directional pipes which work as datain and dataout
        end-points. The parent process (i.e. the current one) establishes the
        connection to the child and then can pass/receive commands, data and logs.

        Usage of the data pipes (datain, dataout) is **synchronous** - you send a
        command and block for an answer. The co-process is normally controlled by
        the current process, except for data requests, which are user-code driven.
        The nature of our problem does not require an *asynchronous* implementation
        which, in turn, would require a much more complex set of dependencies (on
        asyncio or Twisted for example).


        Parameters:

          virtual_memory_in_megabytes (:py:class:`int`, Optional): The amount
            of virtual memory (in Megabytes) available for the job. If set to
            zero, no limit will be applied.

          max_cpu_percent (:py:class:`int`, Optional): The maximum amount of
            CPU usage allowed in a system. This number must be an integer
            number between 0 and ``100*number_of_cores`` in your system. For
            instance, if your system has 2 cores, this number can go between 0
            and 200. If it is <= 0, then we don't track CPU usage.

          timeout_in_minutes (int): The number of minutes to wait for the user
            process to execute. After this amount of time, the user process is
            killed with ``signal.SIGKILL``. If set to zero, no timeout will
            be applied.

        Returns:

          dict: A dictionary which is JSON formattable containing the summary of
            this block execution.

        """

        if not self.valid:
            raise RuntimeError(
                "execution information is bogus:\n  * %s" % "\n  * ".join(self.errors)
            )

        missing_scripts = []
        if (len(self.databases) > 0) and self.DBPROVIDER_BIN is None:
            missing_scripts.append("databases_provider")

        if self.EXECUTE_BIN is None:
            missing_scripts.append("execute")

        if self.LOOP_EXECUTE_BIN is None:
            missing_scripts.append("loop_execute")

        if missing_scripts:
            raise RuntimeError(
                "Scripts not found at PATH (%s): %s"
                % (os.environ.get("PATH", ""), ", ".join(missing_scripts))
            )

        # Creates the message handler
        algorithm_process = None

        def _kill():
            algorithm_process.terminate()

        self.message_handler = MessageHandler(self.ip_address, kill_callback=_kill)

        # ----- (If necessary) Instantiate the subprocess that provide the databases

        database_infos = {}

        if len(self.databases) > 0:
            database_infos["db"] = self.__create_db_process()

        # Configuration and needed files
        configuration_path = utils.temporary_directory()
        self.dump_runner_configuration(configuration_path)

        # import ipdb;ipdb.set_trace()

        # ----- Instantiate the algorithm subprocess
        loop_algorithm_port = None
        loop_algorithm_process = None

        if self.loop_algorithm is not None:
            if len(self.databases) > 0:
                database_infos["loop_db"] = self.__create_db_process("loop")

            loop_algorithm_port = utils.find_free_port()
            cmd = [
                self.LOOP_EXECUTE_BIN,
                self.ip_address + (":%d" % loop_algorithm_port),
                configuration_path,
                self.cache,
            ]

            if len(self.databases) > 0:
                cmd.append(
                    "tcp://"
                    + self.ip_address
                    + (":%d" % database_infos["loop_db"]["port"])
                )

            if logger.getEffectiveLevel() <= logging.DEBUG:
                cmd.insert(1, "--debug")

            # Creation of the container
            loop_algorithm_process_stdout = tempfile.NamedTemporaryFile(delete=False)
            loop_algorithm_process_stderr = tempfile.NamedTemporaryFile(delete=False)

            logger.debug("Starting loop process with: %s" % " ".join(cmd))

            loop_algorithm_process = sp.Popen(
                cmd,
                stdout=loop_algorithm_process_stdout,
                stderr=loop_algorithm_process_stderr,
            )

            # Process the messages until the subprocess is done
            # self.loop_message_handler.start()

        # ----- Instantiate the algorithms subprocess

        # Command to execute
        cmd = [
            self.EXECUTE_BIN,
            "--cache=%s" % self.cache,
            self.message_handler.address,
            configuration_path,
        ]

        if len(self.databases) > 0:
            cmd.append(
                "tcp://" + self.ip_address + (":%d" % database_infos["db"]["port"])
            )

        if self.loop_algorithm is not None:
            cmd.append(
                "--loop=tcp://" + self.ip_address + (":%d" % loop_algorithm_port)
            )

        if logger.getEffectiveLevel() <= logging.DEBUG:
            cmd.insert(1, "--debug")

        # Creation of the container
        algorithm_process_stdout = tempfile.NamedTemporaryFile(delete=False)
        algorithm_process_stderr = tempfile.NamedTemporaryFile(delete=False)

        logger.debug("Starting algorithm process with: %s" % " ".join(cmd))

        algorithm_process = sp.Popen(
            cmd, stdout=algorithm_process_stdout, stderr=algorithm_process_stderr
        )

        # Process the messages until the subprocess is done
        self.message_handler.start()

        try:
            algorithm_process.communicate()
            status = algorithm_process.returncode

        except KeyboardInterrupt:  # Developer pushed CTRL-C
            logger.info("stopping user process on CTRL-C console request")
            algorithm_process.kill()
            status = algorithm_process.wait()

        except Exception:
            algorithm_process.kill()
            status = algorithm_process.wait()

        finally:
            self.message_handler.stop.set()

        # Collects final information and returns to caller
        with open(algorithm_process_stdout.name, "r") as f:
            stdout = f.read()

        stderr = ""
        if status != 0:
            with open(algorithm_process_stderr.name, "r") as f:
                stderr = f.read()

        retval = dict(
            status=status,
            stdout=stdout,
            stderr=stderr,
            timed_out=False,
            statistics={
                "data": self.message_handler.statistics,
                "cpu": {
                    "user": 0.0,
                    "system": 0.0,
                    "total": 0.0,
                    "percent": 0.0,
                    "processors": 1,
                },
                "memory": {"rss": 0, "limit": 0, "percent": 0.0},
            },
            system_error=self.message_handler.system_error,
            user_error=self.message_handler.user_error,
        )

        stats.update(retval["statistics"]["data"], self.io_statistics)

        for name, db_info in database_infos.items():
            logger.debug("Stopping %s process" % name)
            databases_process = db_info["process"]

            databases_process.terminate()
            databases_process.communicate()
            status = databases_process.returncode

            with open(db_info["stdout"].name, "r") as f:
                retval["stdout"] += "\n" + f.read()

            if status != 0:
                with open(db_info["stderr"].name, "r") as f:
                    retval["stderr"] += "\n" + f.read()

        if loop_algorithm_process is not None:
            logger.debug("Stopping loop process")
            loop_algorithm_process.terminate()
            loop_algorithm_process.communicate()
            status = loop_algorithm_process.returncode

            with open(loop_algorithm_process_stdout.name, "r") as f:
                retval["stdout"] += "\n" + f.read()

            if status != 0:
                with open(loop_algorithm_process_stderr.name, "r") as f:
                    retval["stderr"] += "\n" + f.read()

        self.message_handler.destroy()
        self.message_handler = None

        if not self.debug:
            for _, db_info in database_infos.items():
                shutil.rmtree(db_info["configuration_path"])
            shutil.rmtree(configuration_path)

        return retval
