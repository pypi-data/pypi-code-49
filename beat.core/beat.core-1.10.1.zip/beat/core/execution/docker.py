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
======
docker
======

Execution utilities
"""

import os
import shutil
import logging
import requests
import simplejson as json

from beat.backend.python.execution import MessageHandler
from beat.backend.python.data import getAllFilenames

from .. import stats
from .. import utils

from .remote import RemoteExecutor


logger = logging.getLogger(__name__)


class DockerExecutor(RemoteExecutor):
    """DockerExecutor runs the code given an execution block information, externally


    Parameters:

      host (:py:class:`.dock.Host`): A configured docker host that will
        execute the user process. If the host does not have access to the
        required environment, an exception will be raised.

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


    Attributes:

      cache (str): The path to the cache currently being used

      errors (list): A list containing errors found while loading this execution
        block.

      data (dict): The original data for this executor, as loaded by our JSON
        decoder.

      algorithm (.algorithm.Algorithm): An object representing the algorithm to
        be run.

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

    CONTAINER_PREFIX_PATH = "/beat/prefix"
    CONTAINER_CACHE_PATH = "/beat/cache"

    def __init__(
        self,
        host,
        prefix,
        data,
        cache=None,
        dataformat_cache=None,
        database_cache=None,
        algorithm_cache=None,
        library_cache=None,
        custom_root_folders=None,
    ):

        super(DockerExecutor, self).__init__(
            prefix,
            data,
            host.ip,
            cache=cache,
            dataformat_cache=dataformat_cache,
            database_cache=database_cache,
            algorithm_cache=algorithm_cache,
            library_cache=library_cache,
            custom_root_folders=custom_root_folders,
        )

        # Initialisations
        self.host = host

    def __create_db_container(
        self, datasets_uid, network_name, configuration_name=None
    ):
        # Configuration and needed files
        databases_configuration_path = utils.temporary_directory()
        self.dump_databases_provider_configuration(databases_configuration_path)

        # Modify the paths to the databases in the dumped configuration files
        root_folder = os.path.join(databases_configuration_path, "prefix", "databases")

        database_paths = {}

        for db_name in self.databases.keys():
            json_path = os.path.join(root_folder, db_name + ".json")

            with open(json_path, "r") as f:
                db_data = json.load(f)

            database_paths[db_name] = db_data["root_folder"]
            db_data["root_folder"] = os.path.join("/databases", db_name)

            with open(json_path, "w") as f:
                json.dump(db_data, f, indent=4)

        # Determine the docker image to use for the databases
        try:
            databases_environment = self.host.db2docker(database_paths.keys())
        except Exception:
            raise RuntimeError(
                "No environment found for the databases `%s' "
                "- available environments are %s"
                % (
                    ", ".join(database_paths.keys()),
                    ", ".join(self.host.db_environments.keys()),
                )
            )

        # Creation of the container
        # Note: we only support one databases image loaded at the same time
        database_port = utils.find_free_port()

        cmd = [
            "databases_provider",
            "0.0.0.0:%d" % database_port,
            self.CONTAINER_PREFIX_PATH,
            self.CONTAINER_CACHE_PATH,
        ]

        if configuration_name:
            cmd.append(configuration_name)

        if logger.getEffectiveLevel() <= logging.DEBUG:
            cmd.insert(1, "--debug")

        databases_info_name = "beat_db_%s" % utils.id_generator()
        databases_info = self.host.create_container(databases_environment, cmd)
        databases_info.uid = datasets_uid
        databases_info.network_name = network_name
        databases_info.set_name(databases_info_name)

        # Specify the volumes to mount inside the container
        databases_info.add_volume(
            databases_configuration_path, self.CONTAINER_PREFIX_PATH
        )
        databases_info.add_volume(self.cache, self.CONTAINER_CACHE_PATH)

        for db_name, db_path in database_paths.items():
            databases_info.add_volume(db_path, os.path.join("/databases", db_name))

        # Start the container
        while True:
            try:
                databases_info.add_port(
                    database_port, database_port, host_address=self.host.ip
                )

                self.host.start(databases_info)

                break
            except Exception as e:
                if str(e).find("port is already allocated") < 0:
                    break

                databases_info.reset_ports()
                database_port = utils.find_free_port()

                cmd = [
                    x if not x.startswith("0.0.0.0:") else "0.0.0.0:%d" % database_port
                    for x in cmd
                ]
                databases_info.command = cmd

        database_ip = self.host.get_ipaddress(databases_info)
        retval = dict(
            configuration_path=databases_configuration_path,
            container=databases_info,
            address=database_ip,
            port=database_port,
        )
        return retval

    def __setup_io_volumes(
        self, algorithm_container, docker_cache_mount_point, configuration
    ):
        """Setup all the volumes for input and output files.

        Parameters:

          algorithm_container: container that will execute an algorithm

          configuration: json object containing the algorithm parameters
        """

        for item in configuration["inputs"].values():
            file_path = item["path"]
            source_path = os.path.join(self.cache, file_path)

            if docker_cache_mount_point is None:
                if os.path.isfile(source_path):
                    algorithm_container.add_volume(
                        source_path, os.path.join(self.CONTAINER_CACHE_PATH, file_path)
                    )
                else:
                    all_files = getAllFilenames(source_path)
                    for file_list in all_files:
                        for file_ in file_list:
                            target_path = file_[len(self.cache) + 1 :]
                            cache_path = os.path.join(
                                self.CONTAINER_CACHE_PATH, target_path
                            )
                            algorithm_container.add_volume(file_, cache_path)
            else:
                input_folder = file_path[: file_path.rfind("/")]
                source_folder = os.path.join(docker_cache_mount_point, input_folder)
                target_folder = os.path.join(self.CONTAINER_CACHE_PATH, input_folder)
                algorithm_container.add_volume(source_folder, target_folder)

        def __add_writable_volume(file_path):
            output_folder = file_path[: file_path.rfind("/")]
            source_folder = os.path.join(self.cache, output_folder)
            if not os.path.exists(source_folder):
                os.makedirs(source_folder)

            if docker_cache_mount_point is not None:
                source_folder = os.path.join(docker_cache_mount_point, output_folder)

            algorithm_container.add_volume(
                source_folder,
                os.path.join(self.CONTAINER_CACHE_PATH, output_folder),
                read_only=False,
            )

        for item in configuration.get("outputs", {}).values():
            file_path = item["path"]
            __add_writable_volume(file_path)

        result = configuration.get("result")
        if result:
            file_path = result["path"]
            __add_writable_volume(file_path)

    def process(
        self, virtual_memory_in_megabytes=0, max_cpu_percent=0, timeout_in_minutes=0
    ):
        """Executes the user algorithm code using an external program.

        The execution interface follows the backend API as described in our
        documentation.

        We use green subprocesses this implementation. Each co-process is
        linked to us via 2 uni-directional pipes which work as datain and
        dataout end-points. The parent process (i.e. the current one)
        establishes the connection to the child and then can pass/receive
        commands, data and logs.

        Usage of the data pipes (datain, dataout) is **synchronous** - you send
        a command and block for an answer. The co-process is normally
        controlled by the current process, except for data requests, which are
        user-code driven.  The nature of our problem does not require an
        *asynchronous* implementation which, in turn, would require a much more
        complex set of dependencies (on asyncio or Twisted for example).


        Parameters:

          virtual_memory_in_megabytes (:py:class:`int`, Optional): The amount
            of virtual memory (in Megabytes) available for the job. If set to
            zero, no limit will be applied.

          max_cpu_percent (:py:class:`int`, Optional): The maximum amount of
            CPU usage allowed in a system. This number must be an integer
            number between 0 and ``100*number_of_cores`` in your system. For
            instance, if your system has 2 cores, this number can go between 0
            and 200. If it is <= 0, then we don't track CPU usage.

          timeout_in_minutes (:py:class:`int`, Optional): The number of minutes
            to wait for the user process to execute. After this amount of time,
            the user process is killed with ``signal.SIGKILL``. If set to zero,
            no timeout will be applied.


        Returns:

          dict: A dictionary which is JSON formattable containing the summary
          of this block execution.

        """

        if not self.valid:
            raise RuntimeError(
                "execution information is bogus:\n  * %s" % "\n  * ".join(self.errors)
            )

        # Determine the docker image to use for the processing
        processing_environment = "%(name)s (%(version)s)" % self.data["environment"]
        if processing_environment not in self.host:
            raise RuntimeError(
                "Environment `%s' is not available on docker "
                "host `%s' - available environments are %s"
                % (
                    processing_environment,
                    self.host,
                    ", ".join(self.host.processing_environments.keys()),
                )
            )

        # Creates the message handler
        algorithm_container = None

        def _kill():
            self.host.kill(algorithm_container)

        address = self.host.ip
        port_range = self.data.pop("port_range", None)
        if port_range:
            min_port, max_port = port_range.split(":")
            port = utils.find_free_port_in_range(int(min_port), int(max_port))
            address += ":{}".format(port)

        volume_cache_mount_point = self.data.pop("cache_mount_point", None)

        self.message_handler = MessageHandler(address, kill_callback=_kill)

        # ----- (If necessary) Instantiate the docker container that provide the databases

        datasets_uid = self.data.pop("datasets_uid", None)
        network_name = self.data.pop("network_name", "bridge")
        databases_infos = {}

        if len(self.databases) > 0:
            databases_infos["db"] = self.__create_db_container(
                datasets_uid, network_name
            )

        # ----- Instantiate the algorithm container

        # Configuration and needed files
        configuration_path = utils.temporary_directory()
        self.dump_runner_configuration(configuration_path)

        loop_algorithm_container = None
        loop_algorithm_container_ip = None
        loop_algorithm_container_port = None

        if self.loop_algorithm is not None:
            if len(self.databases) > 0:
                databases_infos["loop_db"] = self.__create_db_container(
                    datasets_uid, network_name, "loop"
                )

            loop_algorithm_container_port = utils.find_free_port()
            cmd = [
                "loop_execute",
                "0.0.0.0:{}".format(loop_algorithm_container_port),
                self.CONTAINER_PREFIX_PATH,
                self.CONTAINER_CACHE_PATH,
            ]

            if len(self.databases) > 0:
                cmd.append(
                    "tcp://{}:{}".format(
                        databases_infos["loop_db"]["address"],
                        databases_infos["loop_db"]["port"],
                    )
                )

            if logger.getEffectiveLevel() <= logging.DEBUG:
                cmd.insert(1, "--debug")

            loop_algorithm_container = self.host.create_container(
                processing_environment, cmd
            )
            loop_algorithm_container.uid = datasets_uid
            loop_algorithm_container.network_name = network_name

            # Volumes
            loop_algorithm_container.add_volume(
                configuration_path, self.CONTAINER_PREFIX_PATH
            )
            self.__setup_io_volumes(
                loop_algorithm_container, volume_cache_mount_point, self.data["loop"]
            )

            # Start the container
            self.host.start(
                loop_algorithm_container,
                virtual_memory_in_megabytes=virtual_memory_in_megabytes,
                max_cpu_percent=max_cpu_percent,
            )
            loop_algorithm_container_ip = self.host.get_ipaddress(
                loop_algorithm_container
            )

        # Command to execute
        cmd = [
            "execute",
            "--cache={}".format(self.CONTAINER_CACHE_PATH),
            self.message_handler.address,
            self.CONTAINER_PREFIX_PATH,
        ]

        if len(self.databases) > 0:
            cmd.append(
                "tcp://%s:%d"
                % (databases_infos["db"]["address"], databases_infos["db"]["port"])
            )

        if self.loop_algorithm is not None:
            cmd.append(
                "--loop=tcp://%s:%d"
                % (loop_algorithm_container_ip, loop_algorithm_container_port)
            )

        if logger.getEffectiveLevel() <= logging.DEBUG:
            cmd.insert(1, "--debug")

        # Creation of the container
        algorithm_container = self.host.create_container(processing_environment, cmd)
        algorithm_container.uid = datasets_uid
        algorithm_container.network_name = network_name

        # Volumes
        algorithm_container.add_volume(configuration_path, self.CONTAINER_PREFIX_PATH)
        self.__setup_io_volumes(
            algorithm_container, volume_cache_mount_point, self.data
        )

        # Start the container
        self.host.start(
            algorithm_container,
            virtual_memory_in_megabytes=virtual_memory_in_megabytes,
            max_cpu_percent=max_cpu_percent,
        )

        # Process the messages until the container is done
        self.message_handler.start()

        timed_out = False

        try:
            timeout = (60 * timeout_in_minutes) if timeout_in_minutes else None
            status = self.host.wait(algorithm_container, timeout)

        except requests.exceptions.ReadTimeout:
            logger.warn(
                "user process has timed out after %d minutes", timeout_in_minutes
            )
            timed_out = True

            self.host.kill(algorithm_container)
            status = self.host.wait(algorithm_container)

        except KeyboardInterrupt:  # Developer pushed CTRL-C
            logger.info("stopping user process on CTRL-C console request")
            self.host.kill(algorithm_container)
            status = self.host.wait(algorithm_container)

        finally:
            for name, databases_info in databases_infos.items():
                logger.debug("Stopping database container " + name)
                container = databases_info["container"]
                self.host.kill(container)
                self.host.wait(container)

            self.message_handler.stop.set()
            self.message_handler.join()

        # Collects final information and returns to caller
        container_log = self.host.logs(algorithm_container)

        if status != 0:
            stdout = ""
            stderr = container_log
        else:
            stdout = container_log
            stderr = ""

        if logger.getEffectiveLevel() <= logging.DEBUG:
            logger.debug("Log of the container: " + container_log)

        retval = dict(
            status=status,
            stdout=stdout,
            stderr=stderr,
            timed_out=timed_out,
            statistics=self.host.statistics(algorithm_container),
            system_error=self.message_handler.system_error,
            user_error=self.message_handler.user_error,
        )

        retval["statistics"]["data"] = self.message_handler.statistics
        stats.update(retval["statistics"]["data"], self.io_statistics)

        self.host.rm(algorithm_container)

        for name, databases_info in databases_infos.items():
            container = databases_info["container"]
            db_container_log = self.host.logs(container)

            if logger.getEffectiveLevel() <= logging.DEBUG:
                logger.debug(
                    "Log of the" + name + "database container: " + db_container_log
                )

            if status != 0:
                retval["stderr"] += "\n" + db_container_log
            else:
                retval["stdout"] += "\n" + db_container_log

            self.host.rm(container)

        if loop_algorithm_container:
            self.host.rm(loop_algorithm_container)

        self.message_handler.destroy()
        self.message_handler = None

        if not self.debug:
            for _, databases_info in databases_infos.items():
                shutil.rmtree(databases_info["configuration_path"])
            shutil.rmtree(configuration_path)

        return retval
